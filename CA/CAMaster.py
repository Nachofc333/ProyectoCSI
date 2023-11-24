import os
import datetime

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

class CAMaster():

    _KEY = ""
    _FILE_NAME_KEY = ""
    _FILE_NAME_CERT = ""
    _FILE_NAME_CSR = ""
    def __init__(self):
        super().__init__()
        self._private_key = ""
        self.public_key = ""
        self.cert = ""

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
            csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
                # Provide various details about who we are.
                x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
                x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
                x509.NameAttribute(NameOID.COMMON_NAME, "mysite.com"),
            ])).add_extension(
                x509.SubjectAlternativeName([
                    # Describe what sites we want this certificate for.
                    x509.DNSName("mysite.com"),
                    x509.DNSName("www.mysite.com"),
                    x509.DNSName("subdomain.mysite.com"),
                ]),
                critical=False,
                # Sign the CSR with our private key.
            ).sign(self._private_key, hashes.SHA256())
            # Write our CSR out to disk.
            with open(self._FILE_NAME_CSR, "wb") as f:
                f.write(csr.public_bytes(serialization.Encoding.PEM))
            self.crearCA(csr, self.public_key)

