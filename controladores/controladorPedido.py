from interfaces.PedidoW2 import Ui_Pedido
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
            if self.comprobarPlatos():
                self.crearPedido()
        else:
            alerta = QMessageBox.information(self, 'Error', 'Selecciona un restaurante válido', QMessageBox.Ok)

    def comprobarPlatos(self):
        platos = [self.ui.Pasta.checkState(), self.ui.Filete.checkState(), self.ui.Lentejas.checkState(),
                  self.ui.Hamburguesa.checkState()]
        if not any(plato > 0 for plato in platos):
            QMessageBox.information(self, 'Error', 'Selecciona al menos un plato', QMessageBox.Ok)
            return False
        return True

    def crearPedido(self):
        pedido = Pedido(
            restaurante=self.ui.SelectorRestaurante.currentText(),
            pasta = self.ui.Pasta.checkState() -1 if self.ui.Pasta.checkState() >0 else 0,
            filete = self.ui.Filete.checkState() -1 if self.ui.Filete.checkState() > 0 else 0,
            lentejas = self.ui.Lentejas.checkState() -1 if self.ui.Lentejas.checkState() > 0 else 0,
            hamburguesa = self.ui.Hamburguesa.checkState() -1 if self.ui.Hamburguesa.checkState() > 0 else 0,
            tarta = self.ui.Tarta.checkState() -1 if self.ui.Tarta.checkState() >0 else 0,
            brownie = self.ui.Brownie.checkState() -1 if self.ui.Brownie.checkState() else 0)
        ct = self.user.encriptar(pedido)
        if ct:
            pedido_cifrado = PedidoCifrado(ct)
            self.almacen.add_item(pedido_cifrado)
            self.terminar()

    def terminar(self):
        alerta =  QMessageBox.information(self, 'Exito', 'Pedido realizado con éxito', QMessageBox.Ok)
        self.close()



