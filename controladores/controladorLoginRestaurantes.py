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
from restaurantes.restaurante1.Restaurante1 import Restaurante1
from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4
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
        self.restaurante = None
        self.almacencifrado = None
        self.almacendescifrado = None

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
            u = {"nombre": match["nombre"], "password": match["password"].encode("latin-1"),
                 "telefono": match["telefono"], "salt":match["salt"].encode("latin-1")}

        except:
            alerta = QMessageBox.information(self, 'Error', 'Usuario no encontrado', QMessageBox.Ok)

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
                self.seleccionarRestaurante(usuario)

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
        data = self.restaurante.almacen.data()
        if data == []:
            QMessageBox.information(self, 'Error', 'Este restaurante no tiene pedidos registrados',
                                    QMessageBox.Ok)
            return
        for item in data:
            pedidocifrado = PedidoCifrado(
                pedido=item["Pedido"].encode("latin-1"),
                key=item["Cipher_key"].encode("latin-1"),
                iv=item["Cipher_IV"].encode("latin-1"))
            pedido = self.restaurante.desencriptarPedidos(pedidocifrado)
            self.almacendescifrado.add_item(pedido)
        self.terminar()

    def seleccionarRestaurante(self, restaurante):
        if restaurante == "Restaurante1":
            self.restaurante = Restaurante1()
            self.almacencifrado = self.restaurante.almacen
            self.almacendescifrado = self.restaurante.almacenDesencriptado
        elif restaurante == "Restaurante2":
            self.restaurante = Restaurante2()
            self.almacencifrado = self.restaurante.almacen
            self.almacendescifrado = self.restaurante.almacenDesencriptado
        elif restaurante == "Restaurante3":
            self.restaurante = Restaurante3()
            self.almacencifrado = self.restaurante.almacen
            self.almacendescifrado = self.restaurante.almacenDesencriptado
        elif restaurante == "Restaurante4":
            self.restaurante = Restaurante4()
            self.almacencifrado = self.restaurante.almacen
            self.almacendescifrado = self.restaurante.almacenDesencriptado
        self.mostrarPedidos()

    def terminar(self):
        alerta = QMessageBox.information(self, 'Exito', 'Se ha creado un almacen con el pedido desencriptado', QMessageBox.Ok)
        self.close()