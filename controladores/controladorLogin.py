from interfaces.InicioW import Ui_login
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.controladorRegistro import Controlador_regristro

class Controlador_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_login()
        self.ui.setupUi(self)
        self.controlador_registro = Controlador_regristro()
        self.InicializarGui()

    def InicializarGui(self):
        self.ui.btnIniciarSesion.clicked.connect(self.validarCredenciales)
        self.ui.btnRegistrar.clicked.connect(self.registrarUsuario)
    def validarCredenciales(self):
        usuario = self.ui.txt_user.text()
        password = self.ui.txt_password.text()

        if usuario == "Hola" and password == "Hola":
            self.abrirVentanaPrincipal()
        else:
            alerta = QMessageBox.information(self, 'Error', 'Usuario o contraseña incorrectos', QMessageBox.Ok)

    def registrarUsuario(self):
        self.controlador_registro.show()

    def abrirVentanaPrincipal(self):
        self.close()