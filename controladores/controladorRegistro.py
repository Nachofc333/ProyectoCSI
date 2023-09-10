from interfaces.RegistroW import Ui_registro
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Controlador_regristro(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui=Ui_registro()
        self.ui.setupUi(self)
        self.InicializarGui()

    def InicializarGui(self):
        self.ui.btnRegistrar.clicked.connect(self.validarUsuario)

    def validarUsuario(self):
        """
        Tenemos que hacer que se  compruebe q el usuario no esta en la base de datos
        """
        self.validarContraseña()

    def validarContraseña(self):
        contraseña = self.ui.txt_password.text()
        comprobar = self.ui.txt_password_2.text()
        if contraseña != comprobar:
            alerta = QMessageBox.information(self, 'Error', 'Las contraseñas no coinciden', QMessageBox.Ok)
        else:
            self.crearUsuario()

    def crearUsuario(self):
        """
        Tenemos q hacer q cree el usuario y se guarde en la base de datos
        """
        self.close()
        from controladores.controladorLogin import Controlador_login
        login = Controlador_login()
        login.show()

