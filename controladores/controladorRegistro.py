from interfaces.RegistroW import Ui_registro
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from almacen.jsonAlmacen import JsonAlmacen
from usuario.usuario import Usuario
import re
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


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
        nombre = self.ui.txt_user.text()

        if not nombre:
            QMessageBox.information(self, 'Error', 'Por favor, introduce tu nombre de usuario', QMessageBox.Ok)
            return

        match =self.almacen.find_name(nombre)   # buscar el usuatio en el almacen si no lo encuentra lo crea
        if not match:
            self.contaseñaSegura(nombre)
        else:
            alerta = QMessageBox.information(self, 'Error', 'El usuario ya existe', QMessageBox.Ok)

    def contaseñaSegura(self, nombre):
        contraseña = self.ui.txt_password.text()
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.])[A-Za-z\d@$!%*?&.]{8,}$", contraseña):
            self.validarContraseña(nombre, contraseña)
        else:
            QMessageBox.information(self, 'Error', 'La contraseña debe incluir una mayúscula y una minúscula, un número y un carácter respecial. La longitud mínima es de 8 caracteres.', QMessageBox.Ok)

    def validarContraseña(self, nombre, contraseña):
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
        kdf = Scrypt(                                   # Algoritmo usado Scrypt
            salt=salt,
            length=32,
            n=2 ** 14,                                  # Coste de la CPU
            r=8,                                        # Tamaño de bloque
            p=1,                                        # Paralelización
        )
        key = kdf.derive(bytes(password, "latin-1"))    # Deriva la contraseña
        return key, salt
    def crearUsuario(self, nombre, contraseña, salt):
        telefono = self.ui.txt_telefono.text()
        if not re.match(r'^\+?1?\d{9,15}$', telefono):
            QMessageBox.information(self, 'Error', 'Por favor, introduce un número de teléfono válido', QMessageBox.Ok)
            return
        usuario = Usuario(nombre, contraseña, telefono, salt)
        self.almacen.add_item(usuario)
        self.almacen.load_store()
        self.close()
