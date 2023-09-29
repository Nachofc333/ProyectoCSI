from interfaces.InicioW import Ui_login
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.controladorRegistro import Controlador_regristro
from almacen.jsonAlmacen import JsonAlmacen
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
class Controlador_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_login()
        self.ui.setupUi(self)
        self.controlador_registro = Controlador_regristro()
        self.InicializarGui()
        self.almacen = JsonAlmacen()
    def InicializarGui(self):
        self.ui.btnIniciarSesion.clicked.connect(self.validarCredenciales)
        self.ui.btnRegistrar.clicked.connect(self.registrarUsuario)
    def validarCredenciales(self):
        usuario = self.ui.txt_user.text()
        password = self.ui.txt_password.text()
        match = self.almacen.find_name(usuario)
        if match:
            salt = match["salt"]
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt.encode('latin-1'),
                iterations=480000,
            )
            try:
                kdf.verify(password.encode('latin-1'), match["password"].encode('latin-1'))
                self.abrirVentanaPrincipal()
            except:
                alerta = QMessageBox.information(self, 'Error', 'Contraseña incorrecta', QMessageBox.Ok)
        else:
            alerta = QMessageBox.information(self, 'Error', 'Usuario no encontrado', QMessageBox.Ok)

    def registrarUsuario(self):
        self.controlador_registro.show()

    def abrirVentanaPrincipal(self):
        print("Todo piola")
        self.close()