from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

class RestauranteMaster(QtWidgets.QMainWindow):
    _KEY = ""
    _FILE_NAME = ""
    def __init__(self):
        super().__init__()
        self._private_key = ""
        self.public_key = ""
        self.iv = b""
        self._key = b""

    def descifrarKEY(self, key):  # funcion encargada de descifrar la key simetrica con la clave privada del restaurante
        key = self._private_key.decrypt(
            key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        self._key = key

    def descifrariv(self, ivencrip):
        iv = self._private_key.decrypt(
            ivencrip,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        self.iv = iv

    def descifrarPedido(self,ct, cs, ivencrip):  #funcion encargada de descifrar el pedido con la key simetrica descifrada
        self.descifrariv(ivencrip)

        cipher = Cipher(algorithms.AES(self._key), modes.CBC(self.iv))

        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ct) + decryptor.finalize()

        # Quitar el padding
        plaintextf = plaintext.rstrip(plaintext[-1:]).decode('latin-1')
        # Crear un nuevo decryptor para la firma
        cipher_signature = Cipher(algorithms.AES(self._key), modes.CBC(self.iv))
        decryptor_signature = cipher_signature.decryptor()
        signature = decryptor_signature.update(cs) + decryptor_signature.finalize()

        h = hmac.HMAC(self._key, hashes.SHA256())
        h.update(plaintextf.encode("latin-1"))
        try:
            h.verify(signature)
            alerta = QMessageBox.information(self, 'Pedido', plaintextf, QMessageBox.Ok)
            return plaintextf
        except:
            alerta = QMessageBox.information(self, 'Error', "Pedido modificado", QMessageBox.Ok)
            return False

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

    def desencriptarPedidos(self, pedidocifrado):
        self.descifrarKEY(pedidocifrado.key.encode("latin-1"))  # key descifrada

        self.descifrariv(pedidocifrado.iv.encode("latin-1"))  # iv descifrado

        cipher = Cipher(algorithms.AES(self._key), modes.CBC(self.iv))
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(pedidocifrado.pedido.encode("latin-1")) + decryptor.finalize()  # pedido descifrado

        # Quitar el padding
        plaintextf = plaintext.rstrip(plaintext[-1:]).decode('latin-1')
        return plaintextf

