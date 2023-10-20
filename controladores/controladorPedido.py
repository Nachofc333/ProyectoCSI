from interfaces.PedidoW2 import Ui_Pedido
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pedido.pedido import Pedido
from pedido.pedidoCifrado import PedidoCifrado
from restaurantes.restaurante1.jsonAlmacenPedidos1 import JsonAlmacenPedidos1
from restaurantes.restaurante2.jsonAlmacenPedidos2 import JsonAlmacenPedidos2
from restaurantes.restaurante3.jsonAlmacenPedidos3 import JsonAlmacenPedidos3
from restaurantes.restaurante4.jsonAlmacenPedidos4 import JsonAlmacenPedidos4


class Controlador_pedido(QtWidgets.QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.ui=Ui_Pedido()
        self.ui.setupUi(self)
        self.InicializarGui()
        self.almacen1 = JsonAlmacenPedidos1()
        self.almacen2 = JsonAlmacenPedidos2()
        self.almacen3 = JsonAlmacenPedidos3()
        self.almacen4 = JsonAlmacenPedidos4()

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
        restaurante = self.ui.SelectorRestaurante.currentText()
        pedido = Pedido(
            restaurante=restaurante,
            pasta = self.ui.Pasta.checkState() -1 if self.ui.Pasta.checkState() >0 else 0,
            filete = self.ui.Filete.checkState() -1 if self.ui.Filete.checkState() > 0 else 0,
            lentejas = self.ui.Lentejas.checkState() -1 if self.ui.Lentejas.checkState() > 0 else 0,
            hamburguesa = self.ui.Hamburguesa.checkState() -1 if self.ui.Hamburguesa.checkState() > 0 else 0,
            tarta = self.ui.Tarta.checkState() -1 if self.ui.Tarta.checkState() >0 else 0,
            brownie = self.ui.Brownie.checkState() -1 if self.ui.Brownie.checkState() else 0)
        ct, key = self.user.encriptar(pedido)
        if ct:
            pedido_cifrado = PedidoCifrado(ct, key)
            if restaurante == "Restaurante1":
                self.almacen1.add_item(pedido_cifrado)
            elif restaurante == "Restaurante2":
                self.almacen2.add_item(pedido_cifrado)
            elif restaurante == "Restaurante3":
                self.almacen3.add_item(pedido_cifrado)
            elif restaurante == "Restaurante4":
                self.almacen4.add_item(pedido_cifrado)
            self.terminar()

    def terminar(self):
        alerta =  QMessageBox.information(self, 'Exito', 'Pedido realizado con éxito', QMessageBox.Ok)
        self.close()



