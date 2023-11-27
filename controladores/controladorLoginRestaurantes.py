import binascii

from interfaces.InicioW import Ui_login
from interfaces.InicioRW import Ui_loginR
from pedido.pedidoCifrado import PedidoCifrado
from usuario.usuario import Usuario
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.controladorRegistro import Controlador_regristro
from controladores.controladorPedido import Controlador_pedido
from controladores.controladorSeleccionR import Controlador_SeleccionRestaurante
from almacen.jsonAlmacen2 import JsonAlmacen2
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import os

class Controlador_loginRestaurantes(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginR()  # Pantalla de inicio de sesion
        self.ui.setupUi(self)
        self.InicializarGui()
        self.almacen = JsonAlmacen2()

    def InicializarGui(self):
        self.ui.btnIniciarSesion.clicked.connect(self.validarCredenciales)  # Valida las credenciales si se ha dado a iniciar sesion
        self.ui.btnIniciarSesion_2.clicked.connect(self.inicioUsuarios)

    def validarCredenciales(self):  # Esta función comprueba que el usuario ya esta registrado en la base de datos
        usuario = self.ui.txt_user.text()
        password = self.ui.txt_password.text()
        if not usuario or not password:     # No se ha rellenado algún campo
            QMessageBox.information(self, 'Error', 'Por favor, complete los campos', QMessageBox.Ok)
            return
        match = self.almacen.find_name(usuario)  # Busca al usuario en la baswe de datos
        try:
            current_user = Usuario(match["nombre"],
                               match["password"].encode("latin-1"),
                               match["telefono"],
                               match["salt"].encode("latin-1"))

        except:
            alerta = QMessageBox.information(self, 'Error', 'Usuario no encontrado', QMessageBox.Ok)
        self.mostrarPedidos()
        if match:
            salt = match["salt"]        # Se crea un salt al iniciar sesion para guardar una derivacion de la contraseña
            kdf = Scrypt(               # Se crea el mismo derivador que el usado para uniciar sesión
                salt=salt.encode("latin-1"),
                length=32,
                n=2 ** 14,
                r=8,
                p=1,
            )
            try:
                kdf.verify(password.encode('latin-1'), match["password"].encode('latin-1'))     #Compreba que sean iguales
                self.actualizarSalt(usuario, password, match)

            except:
                alerta = QMessageBox.information(self, 'Error', 'Contraseña incorrecta', QMessageBox.Ok)

    def actualizarSalt(self, usuario, password, match):  # Se actualiza el salt cada vez que el usuario accede a la app para mayor seguridad
        salt = os.urandom(16)
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = kdf.derive(bytes(password, "utf-8"))
        self.almacen.modify_user(usuario, key, salt)    # Modificar los datos en el almacén

    def inicioUsuarios(self):
        self.close()

    def mostrarPedidos(self):
        data = self.almacencifrado.data()
        print(data)
        if data == []:
            QMessageBox.information(self, 'Error', 'Este restaurante no tiene pedidos registrados',
                                    QMessageBox.Ok)
            return
        for item in data:
            pedidocifrado = PedidoCifrado(
                pedido=[binascii.unhexlify(i.encode("latin-1").hex()) for i in item["Pedido"]], modo=1)
            print("pedidocifrado.pedido: ", pedidocifrado.pedido)
            pedido = self.restaurante.desencriptarPedidos(pedidocifrado)
            self.almacen.add_item(pedido)

        self.terminar()

    def terminar(self):
        alerta = QMessageBox.information(self, 'Exito', 'Se ha creado un almacen con el pedido desencriptado', QMessageBox.Ok)
        self.close()