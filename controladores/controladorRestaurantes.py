from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interfaces.RestauranteW import Ui_Restaurante
from restaurantes.restaurante1.Restaurante1 import Restaurante1
from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4
import binascii
from pedido.pedidoCifrado import PedidoCifrado


class Controlador_restaurante(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Restaurante()
        self.ui.setupUi(self)
        self.InicializarGui()

        self.restaurante = None
        self.almacencifrado = None
        self.almacen = None


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

    def terminar(self):
        alerta = QMessageBox.information(self, 'Exito', 'Se ha creado un almacen con el pedido desencriptado', QMessageBox.Ok)
        self.close()
