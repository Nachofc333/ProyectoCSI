from vistas.InicioW import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Controlador_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.InicializarGui()

    def InicializarGui(self):
        self.ui.IniciarSesion.clicked.connect(self.validarCredenciales)
    def validarCredenciales(self):
        usuario = self.ui.txt_user.text()
        password = self.ui.txt_password.text()

        if usuario == "Hola" and password == "Hola":
            self.abrirVentanaPrincipal()
        else:
            alerta = QMessageBox.information(self, 'Error', 'Usiario o contraseña incorrectos', QMessageBox.Ok)

    def abrirVentanaPrincipal(self):
        self.close()