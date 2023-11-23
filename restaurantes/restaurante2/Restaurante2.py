from restaurantes.restauranteMaster import RestauranteMaster
import os
from restaurantes.restaurante2.jsonAlmacenPedidos2 import JsonAlmacenPedidos2
from restaurantes.restaurante2.jsonAlmacenPedidoDesencriptado2 import JsonAlmacenPedidoDesencriptado2
JSON_FILES_PATH = os.path.dirname(__file__)


class Restaurante2(RestauranteMaster):
    _FILE_NAME = JSON_FILES_PATH + "/keyR2.pem"
    _NAME = "RESTAURANTE2"
    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key =self.genererkey()
        self.public_key = self._private_key.public_key()
        self.iv = ""
        self._key = ""
        self.almacen = JsonAlmacenPedidos2()
        self.almacenDesencriptado = JsonAlmacenPedidoDesencriptado2()
