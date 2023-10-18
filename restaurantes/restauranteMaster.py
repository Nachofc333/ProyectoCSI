from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
class RestauranteMaster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._private_key = ""
        self.public_key = ""
        self.iv = ""
        self._key = ""



    def descifrarKEY(self, key):
        key = self._private_key.decrypt(
            key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        self._key = key
    def descifrarPedido(self,ct):
        cipher = Cipher(algorithms.AES(self._key), modes.CBC(self.iv))
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ct) + decryptor.finalize()
        alerta = QMessageBox.information(self, 'Pedido', plaintext.decode("latin-1"), QMessageBox.Ok)

    """def descifrarPedido(self, ct, nonce):
        aesgcm = AESGCM(self._key)
        try:
            plaintext = aesgcm.decrypt(nonce, ct, None)
            alerta = QMessageBox.information(self, 'Pedido', plaintext.decode("latin-1"), QMessageBox.Ok)
        except:
            print("Tag inválido. Los datos han sido manipulados.")
"""