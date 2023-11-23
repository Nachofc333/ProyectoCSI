from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interfaces.RestauranteW import Ui_Restaurante
from restaurantes.restaurante1.Restaurante1 import Restaurante1
from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4

from pedido.pedidoCifrado import PedidoCifrado


class Controlador_restaurante(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Restaurante()
        self.ui.setupUi(self)
        self.InicializarGui()

        self.restaurante = None
        self.almacencifrado = None
        self.alacen = None


    def InicializarGui(self):
        self.ui.DescifrarAlmacen.clicked.connect(self.seleccionarRestaurante)

    def seleccionarRestaurante(self):
        restaurante = self.ui.Restaurante.currentText()
        if restaurante == "Restaurante1":
            self.restaurante = Restaurante1()
            self.almacencifrado = self.restaurante.almacen
            self.almacen = self.restaurante.almacenDesencriptado
        elif restaurante == "Restaurante2":
            self.restaurante = Restaurante2()
            self.almacencifrado = self.restaurante.almacen
            self.almacen = self.restaurante.almacenDesencriptado
        elif restaurante == "Restaurante3":
            self.restaurante = Restaurante3()
            self.almacencifrado = self.restaurante.almacen
            self.almacen = self.restaurante.almacenDesencriptado
        elif restaurante == "Restaurante4":
            self.restaurante = Restaurante4()
            self.almacencifrado = self.restaurante.almacen
            self.almacen = self.restaurante.almacenDesencriptado
        self.mostrarPedidos()

    def mostrarPedidos(self):
        data = self.almacencifrado.data()

        if data == []:
            QMessageBox.information(self, 'Error', 'Este restaurante no tiene pedidos registrados',
                                    QMessageBox.Ok)
            return
        for item in data:
            pedidocifrado = PedidoCifrado(
                pedido = item["Pedido"].encode("latin-1"), modo=0)
            pedido = self.restaurante.desencriptarPedidos(pedidocifrado)
            self.almacen.add_item(pedido)
        self.terminar()

    def terminar(self):
        alerta = QMessageBox.information(self, 'Exito', 'Se ha creado un almacen con el pedido desencriptado', QMessageBox.Ok)
        self.close()


    """
        def mostrarPedidos(self):
        data = self.almacencifrado.data()
        pedido = ""
        if data == []:
            QMessageBox.information(self, 'Error', 'Este restaurante no tiene pedidos registrados', QMessageBox.Ok)
            return
        for item in data:
            for i in item:
                if i != "Pedido":
                    pedido += self.restaurante.desencriptarPedidos(i.encode("latin-1"))
        self.almacen.add_item(pedido)
        self.terminar()
    """

