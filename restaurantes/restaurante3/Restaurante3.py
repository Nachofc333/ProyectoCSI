from restaurantes.restauranteMaster import RestauranteMaster
import os
from restaurantes.restaurante3.jsonAlmacenPedidos3 import JsonAlmacenPedidos3
from restaurantes.restaurante3.jsonAlmacenPedidoDesencriptado3 import JsonAlmacenPedidoDesencriptado3
JSON_FILES_PATH = os.path.dirname(__file__)


class Restaurante3(RestauranteMaster):
    _FILE_NAME = JSON_FILES_PATH + "/keyR3.pem"
    _NAME = "RESTAURANTE3"

    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key =self.genererkey()
        self.public_key = self._private_key.public_key()
        self.iv = ""
        self._key = ""
        self.almacen = JsonAlmacenPedidos3()
        self.almacenDesencriptado = JsonAlmacenPedidoDesencriptado3()