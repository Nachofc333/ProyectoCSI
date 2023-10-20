
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from restaurantes.restauranteMaster import RestauranteMaster
import os
JSON_FILES_PATH = os.path.dirname(__file__)

class Restaurante4(RestauranteMaster):
    _FILE_NAME = JSON_FILES_PATH + "/keyR4.pem"

    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key = self.genererkey()
        self.public_key = self._private_key.public_key()
        self.iv = os.urandom(16)
        self._key = ""

    """def genererkey(self):
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
        return private_key"""
