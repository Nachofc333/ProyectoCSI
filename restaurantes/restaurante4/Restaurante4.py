from restaurantes.restauranteMaster import RestauranteMaster
import os
from restaurantes.restaurante4.jsonAlmacenPedidos4 import JsonAlmacenPedidos4
from restaurantes.restaurante4.jsonAlmacenPedidoDesencriptado4 import JsonAlmacenPedidoDesencriptado4
JSON_FILES_PATH = os.path.dirname(__file__)


class Restaurante4(RestauranteMaster):
    _FILE_NAME = JSON_FILES_PATH + "/keyR4.pem"

    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key = self.genererkey()
        self.public_key = self._private_key.public_key()
        self.iv = ""
        self._key = ""
        self.almacen = JsonAlmacenPedidos4()
        self.almacenDesencriptado = JsonAlmacenPedidoDesencriptado4()
