from restaurantes.restauranteMaster import RestauranteMaster
from restaurantes.restaurante1.jsonAlmacenPedidos1 import JsonAlmacenPedidos1
from restaurantes.restaurante1.jsonAlmacenPedidoDesencriptado1 import JsonAlmacenPedidoDesencriptado1

import os
JSON_FILES_PATH = os.path.dirname(__file__)


class Restaurante1(RestauranteMaster):
    _FILE_NAME = JSON_FILES_PATH + "/keyR1.pem"
    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key =self.genererkey()
        self.public_key = self._private_key.public_key()
        self.iv = ""
        self._key = ""
        self.almacen = JsonAlmacenPedidos1()
        self.almacenDesencriptado = JsonAlmacenPedidoDesencriptado1()

