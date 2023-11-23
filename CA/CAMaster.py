import os
import datetime

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

class CAMaster():

    _KEY = ""
    _FILE_NAME = ""

    def __init__(self):
        super().__init__()
        self._private_key = ""
        self.public_key = ""

    def genererkey(self):
        if not os.path.exists(self._FILE_NAME):
            # Si no existe, genera la clave privada
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
            )

            # Guarda la clave privada en un archivo PEM
            with open(self._FILE_NAME, "wb") as f:
                f.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))

        # Lee la clave privada desde un archivo PEM
        with open(self._FILE_NAME, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )
        return private_key

    def crearCA(self, public_key, csr):
        CApublic_key = csr.public_key()
        isinstance(CApublic_key, public_key)
        