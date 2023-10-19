from interfaces.InicioW import Ui_login
from usuario.usuario import Usuario
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.controladorRegistro import Controlador_regristro
from controladores.controladorPedido import Controlador_pedido
from almacen.jsonAlmacen import JsonAlmacen
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

class Controlador_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()  # Pantalla de inicio de sesion
        self.ui.setupUi(self)
        self.controlador_registro = Controlador_regristro()
        self.controlador_pedido = None
        self.InicializarGui()
        self.almacen = JsonAlmacen()

    def InicializarGui(self):
        self.ui.btnIniciarSesion.clicked.connect(self.validarCredenciales)  # Valida las credenciales si se ha dado a iniciar sesion
        self.ui.btnRegistrar.clicked.connect(self.registrarUsuario)  # Pasa a registrar usuario si se ha dado click a registrar usuario

    def validarCredenciales(self):  # Esta función comprueba que el usuario ya esta registrado en la base de datos
        usuario = self.ui.txt_user.text()
        password = self.ui.txt_password.text()
        if not usuario or not password:
            QMessageBox.information(self, 'Error', 'Por favor, complete los campos', QMessageBox.Ok)
            return
        match = self.almacen.find_name(usuario)  # Busca al usuario en la baswe de datos
        try:
            current_user = Usuario(match["nombre"],
                               match["password"].encode("latin-1"),
                               match["telefono"],
                               match["salt"].encode("latin-1"))
            self.controlador_pedido = Controlador_pedido(current_user)  # Abre la seccion del pedido si se ha iniciado sesion
        except:
            alerta = QMessageBox.information(self, 'Error', 'Usuario no encontrado', QMessageBox.Ok)


        if match:
            salt = match["salt"]  # Se crea un salt al iniciar sesion para guardar una derivacion de la contraseña
            kdf = Scrypt(
                salt=salt.encode("latin-1"),
                length=32,
                n=2 ** 14,
                r=8,
                p=1,
            )
            try:
                kdf.verify(password.encode('latin-1'), match["password"].encode('latin-1'))
                self.abrirVentanaPrincipal(match)
            except:
                alerta = QMessageBox.information(self, 'Error', 'Contraseña incorrecta', QMessageBox.Ok)

    def registrarUsuario(self):
        self.controlador_registro.show()

    def abrirVentanaPrincipal(self, user):
        self.controlador_pedido.show()
        self.close()