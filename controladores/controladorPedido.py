from interfaces.PedidoW import Ui_Pedido
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pedido.pedido import Pedido

class Controlador_pedido(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_Pedido()
        self.ui.setupUi(self)
        self.InicializarGui()
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

