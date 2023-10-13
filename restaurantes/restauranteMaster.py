from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
class RestauranteMaster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._private_key = ""
        self.public_key = ""

    def descifrar(self, pedidoCifrado):
        plaintext = self._private_key.decrypt(
            pedidoCifrado,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        alerta = QMessageBox.information(self, 'Pedido', plaintext.decode("latin-1"), QMessageBox.Ok)