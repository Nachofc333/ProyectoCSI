
from cryptography.hazmat.primitives.asymmetric import rsa
from restaurantes.restauranteMaster import RestauranteMaster
from restaurantes.restaurante2 import jsonAlmacenPedidoDesencriptado2
import os
JSON_FILES_PATH = os.path.dirname(__file__)
class Restaurante2(RestauranteMaster):
    _FILE_NAME = JSON_FILES_PATH + "/keyR2.pem"
    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key =self.genererkey()
        self.public_key = self._private_key.public_key()
        self.iv = ""
        self._key = ""
