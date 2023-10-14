from interfaces.RegistroW import Ui_registro
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from almacen.jsonAlmacen import JsonAlmacen
from usuario.usuario import Usuario
import re
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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

        if not nombre:
            QMessageBox.information(self, 'Error', 'Por favor, introduce tu nombre de usuario', QMessageBox.Ok)
            return

        ### buscar el usuatio en el almacen si no lo encuentra lo crea
        match =self.almacen.find_name(nombre)
        if not match:
            self.validarContraseña(nombre)
        else:
            alerta = QMessageBox.information(self, 'Error', 'El usuario ya existe', QMessageBox.Ok)


    def validarContraseña(self, nombre):
        contraseña = self.ui.txt_password.text()
        comprobar = self.ui.txt_password_2.text()
        if not contraseña or not comprobar:
            QMessageBox.information(self, 'Error', 'Por favor, rellene todos los campos', QMessageBox.Ok)
            return

        if contraseña != comprobar:
            alerta = QMessageBox.information(self, 'Error', 'Las contraseñas no coinciden', QMessageBox.Ok)
        else:
            derivación, salt = self.derivarContraseña(contraseña)
            self.crearUsuario(nombre, derivación, salt)

    def derivarContraseña(self, password):
        salt = os.urandom(16)
        # derive
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = kdf.derive(bytes(password, "utf-8"))
        return key, salt
    def crearUsuario(self, nombre, contraseña, salt):
        """
        Tenemos q hacer q cree el usuario y se guarde en la base de datos
        """
        telefono = self.ui.txt_telefono.text()
        if not re.match(r'^\+?1?\d{9,15}$', telefono):
            QMessageBox.information(self, 'Error', 'Por favor, introduce un número de teléfono válido', QMessageBox.Ok)
            return

        usuario = Usuario(nombre, contraseña, telefono, salt)
        self.almacen.add_item(usuario)
        self.almacen.load_store()
        self.close()
