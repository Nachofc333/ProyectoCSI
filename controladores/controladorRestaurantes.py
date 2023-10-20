from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interfaces.RestauranteW import Ui_Restaurante

class Controlador_restaurante(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Restaurante()
        self.ui.setupUi(self)
        self.InicializarGui()

    def InicializarGui(self):
        print("Hecho")

