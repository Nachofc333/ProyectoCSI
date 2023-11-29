import os
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

class CAMaster():

    _NAME = ""
    _FILE_NAME_KEY = ""
    _FILE_NAME_CERT = ""
    _FILE_NAME_CSR = ""

    def __init__(self):
        super().__init__()
        self.name = self.generarNombre()
        self._private_key = ""
        self.public_key = ""
        self.cert = ""

    def generarNombre(self):
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "ES"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Madrid"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "Colmenarejo"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, self._NAME),
            x509.NameAttribute(NameOID.COMMON_NAME, "glovo.com"),
        ])
        return subject

    def genererkey(self):
        if not os.path.exists(self._FILE_NAME_KEY):
            # Si no existe, genera la clave privada
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
            )

            # Guarda la clave privada en un archivo PEM
            with open(self._FILE_NAME_KEY, "wb") as f:
                f.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))

        # Lee la clave privada desde un archivo PEM
        with open(self._FILE_NAME_KEY, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )
        return private_key

    def generarCSR(self):
        if not os.path.exists(self._FILE_NAME_CERT):
            csr = x509.CertificateSigningRequestBuilder().subject_name(self.name).add_extension(
                x509.SubjectAlternativeName([
                    # Describe what sites we want this certificate for.
                    x509.DNSName("glovo.com"),
                    x509.DNSName("www.glovo.com"),
                    x509.DNSName("subdomain.glovo.com"),
                ]),
                critical=False,
                # Sign the CSR with our private key.
            ).sign(self._private_key, hashes.SHA256())
            # Write our CSR out to disk.
            with open(self._FILE_NAME_CSR, "wb") as f:
                f.write(csr.public_bytes(serialization.Encoding.PEM))
            return csr

    def verificarFirma(self, csr, public_key):
        try:
            # Verifica la firma de la CSR
            public_key.verify(
                csr.signature,
                csr.tbs_certrequest_bytes,
                padding.PKCS1v15(),
                # Esto debería coincidir con el algoritmo utilizado para firmar la CSR
                hashes.SHA256(),
            )
            return True
        except Exception:
            return False

    def crearCA(self, csr, public_key, name):
        if not self.verificarFirma(csr, public_key):
            return None
        certificate = x509.CertificateBuilder().subject_name(
            csr.subject
        ).issuer_name(
            name
        ).public_key(
            public_key
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.utcnow()
        ).not_valid_after(
            # El certificado será válido por 10 días days=730
            datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
            critical=False,
            # Firmamos el certificado con la clave privada de la Autoridad de Certificación
        ).sign(self._private_key, hashes.SHA256(), default_backend())
        return certificate


