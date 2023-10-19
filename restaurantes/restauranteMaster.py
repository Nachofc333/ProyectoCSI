from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class RestauranteMaster(QtWidgets.QMainWindow):
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

    def descifrarPedido(self,ct, signature):  #funcion encargada de descifrar el pedido con la key simetrica descifrada
        h = hmac.HMAC(self._key, hashes.SHA256())
        h.update(ct)
        try:
            h.verify(signature)
            cipher = Cipher(algorithms.AES(self._key), modes.CBC(self.iv))
            decryptor = cipher.decryptor()
            plaintext = decryptor.update(ct) + decryptor.finalize()
            alerta = QMessageBox.information(self, 'Pedido', plaintext.decode("latin-1"), QMessageBox.Ok)
            return True
        except:
            alerta = QMessageBox.information(self, 'Error', "Pedido modificado", QMessageBox.Ok)
            return False
