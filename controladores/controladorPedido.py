from interfaces.PedidoW import Ui_Pedido
from PyQt5 import QtWidgets
import json
from PyQt5.QtWidgets import QMessageBox
from pedido.pedido import Pedido
from pedido.pedidoCifrado import PedidoCifrado
from restaurantes.restaurante1.jsonAlmacenPedidos1 import JsonAlmacenPedidos1
from restaurantes.restaurante2.jsonAlmacenPedidos2 import JsonAlmacenPedidos2
from restaurantes.restaurante3.jsonAlmacenPedidos3 import JsonAlmacenPedidos3
from restaurantes.restaurante4.jsonAlmacenPedidos4 import JsonAlmacenPedidos4
from restaurantes.restaurante1.jsonAlmacenPedidoDesencriptado1 import JsonAlmacenPedidoDesencriptado1
from restaurantes.restaurante2.jsonAlmacenPedidoDesencriptado2 import JsonAlmacenPedidoDesencriptado2
from restaurantes.restaurante3.jsonAlmacenPedidoDesencriptado3 import JsonAlmacenPedidoDesencriptado3
from restaurantes.restaurante4.jsonAlmacenPedidoDesencriptado4 import JsonAlmacenPedidoDesencriptado4
from restaurantes.restaurante1.Restaurante1 import Restaurante1
from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4
from controladores.controladorRestaurantes import Controlador_restaurante


class Controlador_pedido(QtWidgets.QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.ui=Ui_Pedido()
        self.ui.setupUi(self)
        self.InicializarGui()
        self.controlador_restaurantes = Controlador_restaurante()
        self.almacen1 = JsonAlmacenPedidos1()
        self.almacen1des = JsonAlmacenPedidoDesencriptado1()
        self.almacen2 = JsonAlmacenPedidos2()
        self.almacen2des = JsonAlmacenPedidoDesencriptado2()
        self.almacen3 = JsonAlmacenPedidos3()
        self.almacen3des = JsonAlmacenPedidoDesencriptado3()
        self.almacen4 = JsonAlmacenPedidos4()
        self.almacen4des = JsonAlmacenPedidoDesencriptado4()

    def InicializarGui(self):
        self.ui.EnviarPedido.clicked.connect(self.ComprobarRestaurante)
        self.ui.Pedidos.clicked.connect(self.IniciarRestaurantes)

    def IniciarRestaurantes(self):
        self.controlador_restaurantes.show()
        self.close()

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
        ct, key, cs, iv = self.user.encriptar(pedido)
        if ct:
            pedido_cifrado = PedidoCifrado(ct, key, cs, iv)
            if restaurante == "Restaurante1":
                restaurante = Restaurante1()
                self.almacen1.add_item(pedido_cifrado)
                """pedido_descifrado = restaurante.desencriptarPedidos(pedido_cifrado)
                self.almacen1des.add_item(pedido_descifrado)"""
            elif restaurante == "Restaurante2":
                restaurante = Restaurante2()
                self.almacen2.add_item(pedido_cifrado)
                """pedido_descifrado = restaurante.desencriptarPedidos(pedido_cifrado)
                self.almacen2des.add_item(pedido_descifrado)"""
            elif restaurante == "Restaurante3":
                restaurante = Restaurante3()
                self.almacen3.add_item(pedido_cifrado)
                """pedido_descifrado = restaurante.desencriptarPedidos(pedido_cifrado)
                self.almacen3des.add_item(pedido_descifrado)"""
            elif restaurante == "Restaurante4":
                restaurante = Restaurante4()
                self.almacen4.add_item(pedido_cifrado)
                """pedido_descifrado = restaurante.desencriptarPedidos(pedido_cifrado)
                self.almacen4des.add_item(pedido_descifrado)"""
            self.terminar()

    def terminar(self):
        alerta = QMessageBox.information(self, 'Exito', 'Pedido realizado con éxito', QMessageBox.Ok)
        self.close()



