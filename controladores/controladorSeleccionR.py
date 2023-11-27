from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.controladorPedido import Controlador_pedido
from interfaces.RestauranteW import Ui_Restaurante
from interfaces.SeleccionRestauranteW import Ui_SeleccionRestaurante
from interfaces.PedidoW import Ui_Pedido
from restaurantes.restaurante1.Restaurante1 import Restaurante1

from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4
import binascii
from pedido.pedidoCifrado import PedidoCifrado


class Controlador_SeleccionRestaurante(QtWidgets.QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_SeleccionRestaurante()
        self.current_user = user
        self.controlador_pedido = None
        self.restaurante = None
        self.ui.setupUi(self)
        self.InicializarGui()
        self.close()

    def InicializarGui(self):
        self.ui.Restaurante1.clicked.connect(self.abrirPedidoR1)
        self.ui.Restaurante2.clicked.connect(self.abrirPedidoR2)
        self.ui.Restaurante3.clicked.connect(self.abrirPedidoR3)
        self.ui.Restaurante4.clicked.connect(self.abrirPedidoR4)

    def abrirPedidoR1(self):
        self.restaurante = "Restaurante1"
        self.controlador_pedido = Controlador_pedido(self.current_user, self.restaurante)
        self.controlador_pedido.show()


    def abrirPedidoR2(self):
        self.restaurante = "Restaurante2"
        self.controlador_pedido = Controlador_pedido(self.current_user, self.restaurante)
        self.controlador_pedido.show()


    def abrirPedidoR3(self):
        self.restaurante = "Restaurante3"
        self.controlador_pedido = Controlador_pedido(self.current_user, self.restaurante)
        self.controlador_pedido.show()


    def abrirPedidoR4(self):
        self.restaurante = "Restaurante4"
        self.controlador_pedido = Controlador_pedido(self.current_user, self.restaurante)
        self.controlador_pedido.show()
