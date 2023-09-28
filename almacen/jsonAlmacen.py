"""MODULES"""
from almacen.jsonMaster import JsonStoreMaster
import os
JSON_FILES_PATH = os.path.dirname(__file__)
class JsonAlmacen(JsonStoreMaster):
    """Clase JsonDeliverStore"""
    _FILE_PATH = JSON_FILES_PATH +"/almacen.json"
    _data_list = []
    _ID_FIELD = "nombre"

    def __init__(self)->None:
        """Constructor de JsonDeliverStore"""
        super(JsonStoreMaster, self).__init__()

