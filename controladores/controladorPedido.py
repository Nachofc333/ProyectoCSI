from interfaces.PedidoW import Ui_Pedido
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pedido.pedido import Pedido
from pedido.pedidoCifrado import PedidoCifrado
from almacen.jsonAlmacenPedidos import JsonAlmacenPedidos


class Controlador_pedido(QtWidgets.QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.ui=Ui_Pedido()
        self.ui.setupUi(self)
        self.InicializarGui()
        self.almacen = JsonAlmacenPedidos()
    def InicializarGui(self):
        self.ui.EnviarPedido.clicked.connect(self.ComprobarRestaurante)

    def ComprobarRestaurante(self):
        restaurante = self.ui.SelectorRestaurante.currentText()
        if restaurante != "Selecciona restaurante":
            self.crearPedido()
        else:
            alerta = QMessageBox.information(self, 'Error', 'Selecciona un restaurante válido', QMessageBox.Ok)
    def crearPedido(self):
        pedido = Pedido(
            restaurante=self.ui.SelectorRestaurante.currentText(),
            pasta = self.ui.Pasta.checkState(),
            filete = self.ui.Filete.checkState(),
            lentejas = self.ui.Lentejas.checkState(),
            hamburguesa = self.ui.Hamburguesa.checkState(),
            tarta = self.ui.Tarta.checkState())
        pedido_cifrado = PedidoCifrado(self.user.encriptar(pedido))
        self.almacen.add_item(pedido_cifrado)
        self.terminar()

    def terminar(self):
        alerta =  QMessageBox.information(self, 'Exito', 'Pedido realizado con éxito', QMessageBox.Ok)
        self.close()



