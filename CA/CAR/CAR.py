import os
import datetime
from CA.CAMaster import CAMaster
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from datetime import datetime

JSON_FILES_PATH = os.path.dirname(__file__)
now = datetime.utcnow()

class CAR(CAMaster):
    _FILE_NAME_KEY = JSON_FILES_PATH + "/CAR_key.pem"
    _FILE_NAME_CTR = JSON_FILES_PATH + "/CAR_cert.pem"
    _NAME = "CAR"
    def __init__(self):
        super(CAMaster, self).__init__()

        self._private_key = self.genererkey()
        self.public_key = self._private_key.public_key()
        self.cert = self.generarCAR()
        if not self.cert.not_valid_before <= now <= self.cert.not_valid_after:
            self.recargarCA()

    def generarCAR(self):
        if not os.path.exists(self._FILE_NAME_CTR):
            subject = issuer = x509.Name([
                x509.NameAttribute(NameOID.COUNTRY_NAME, "ES"),
                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Madrid"),
                x509.NameAttribute(NameOID.LOCALITY_NAME, "Colmenarejo"),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, self._NAME),
                x509.NameAttribute(NameOID.COMMON_NAME, "glovo.com"),
            ])
            cert = x509.CertificateBuilder().subject_name(
                subject
            ).issuer_name(
                issuer
            ).public_key(
                self._private_key.public_key()
            ).serial_number(
                x509.random_serial_number()
            ).not_valid_before(
                datetime.datetime.now(datetime.timezone.utc)
            ).not_valid_after(
                # Our certificate will be valid for 10 days
                datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10)
            ).add_extension(
                x509.SubjectAlternativeName([x509.DNSName("localhost")]),
                critical=False,
                # Sign our certificate with our private key
            ).sign(self._private_key, hashes.SHA256())
            with open(self._FILE_NAME_CTR, "wb") as f:
                f.write(cert.public_bytes(serialization.Encoding.PEM))
            return cert

        with open(self._FILE_NAME_CTR, "rb") as f:
            pem_data = f.read()

        # Cargar el certificado
        cert = x509.load_pem_x509_certificate(
            pem_data
        )
        return cert

    def recargarCA(self):
        os.remove(self._FILE_NAME_CTR)
        self.cert = self.generarCAR()


