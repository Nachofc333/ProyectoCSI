from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interfaces.RestauranteW import Ui_Restaurante
from restaurantes.restaurante1.Restaurante1 import Restaurante1
from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4
from restaurantes.restaurante1.jsonAlmacenPedidoDesencriptado1 import JsonAlmacenPedidoDesencriptado1
from restaurantes.restaurante2.jsonAlmacenPedidoDesencriptado2 import JsonAlmacenPedidoDesencriptado2
from restaurantes.restaurante3.jsonAlmacenPedidoDesencriptado3 import JsonAlmacenPedidoDesencriptado3
from restaurantes.restaurante4.jsonAlmacenPedidoDesencriptado4 import JsonAlmacenPedidoDesencriptado4
from restaurantes.restaurante1.jsonAlmacenPedidos1 import JsonAlmacenPedidos1
from restaurantes.restaurante2.jsonAlmacenPedidos2 import JsonAlmacenPedidos2
from restaurantes.restaurante3.jsonAlmacenPedidos3 import JsonAlmacenPedidos3
from restaurantes.restaurante4.jsonAlmacenPedidos4 import JsonAlmacenPedidos4
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
            self.almacencifrado = JsonAlmacenPedidos1()
            self.almacen = JsonAlmacenPedidoDesencriptado1()
        elif restaurante == "Restaurante2":
            self.restaurante = Restaurante2()
            self.almacencifrado = JsonAlmacenPedidos2()
            self.almacen = JsonAlmacenPedidoDesencriptado2()
        elif restaurante == "Restaurante3":
            self.restaurante = Restaurante3()
            self.almacencifrado = JsonAlmacenPedidos3()
            self.almacen = JsonAlmacenPedidoDesencriptado3()
        elif restaurante == "Restaurante4":
            self.restaurante = Restaurante4()
            self.almacencifrado = JsonAlmacenPedidos4()
            self.almacen = JsonAlmacenPedidoDesencriptado4()
        self.mostrarPedidos()

    def mostrarPedidos(self):
        data = self.almacencifrado.data()

        if data == []:
            QMessageBox.information(self, 'Error', 'Este restaurante no tiene pedidos registrados',
                                    QMessageBox.Ok)
            return
        for item in data:
            pedidocifrado = PedidoCifrado(
                pedido = item["Pedido"].encode("latin-1"))
            pedido = self.restaurante.desencriptarPedidos(pedidocifrado)
            self.almacen.add_item(pedido)
        self.terminar()

    def terminar(self):
        alerta = QMessageBox.information(self, 'Exito', 'Se ha creado un almacen con el pedido desencriptado', QMessageBox.Ok)
        self.close()

