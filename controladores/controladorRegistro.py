from interfaces.RegistroW import Ui_registro
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from almacen.jsonAlmacen import JsonAlmacen
from usuario.usuario import Usuario

class Controlador_regristro(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui=Ui_registro()
        self.ui.setupUi(self)
        self.InicializarGui()
        self.almacen = JsonAlmacen()

    def InicializarGui(self):
        self.ui.btnRegistrar.clicked.connect(self.validarUsuario)

    def validarUsuario(self):
        """
        Tenemos que hacer que se  compruebe q el usuario no esta en la base de datos
        """
        nombre = self.ui.txt_user.text()
        ### buscar el usuatio en el almacen si no lo encuentra lo crea
        self.validarContraseña(nombre)

    def validarContraseña(self, nombre):
        contraseña = self.ui.txt_password.text()
        comprobar = self.ui.txt_password_2.text()
        if contraseña != comprobar:
            alerta = QMessageBox.information(self, 'Error', 'Las contraseñas no coinciden', QMessageBox.Ok)
        else:
            self.crearUsuario(nombre, contraseña)

    def crearUsuario(self, nombre, contraseña):
        """
        Tenemos q hacer q cree el usuario y se guarde en la base de datos
        """
        telefono  = self.ui.txt_telefono.text()
        usuario = Usuario (nombre, contraseña, telefono)
        self.almacen.add_item(usuario)
        self.close()
