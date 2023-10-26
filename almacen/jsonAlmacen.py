"""MODULES"""
from almacen.jsonMaster import JsonStoreMaster
import os
JSON_FILES_PATH = os.path.dirname(__file__)
class JsonAlmacen(JsonStoreMaster):
    """Clase JsonAlmacen"""
    _FILE_PATH = JSON_FILES_PATH +"/almacen.json"
    _data_list = []
    _ID_FIELD = "nombre"

    def __init__(self)->None:
        """Constructor de JsonAlmacen"""
        super(JsonStoreMaster, self).__init__()

    def find_name(self, data_to_find:str):
        self.load_store()
        return self.find_data(data_to_find)

    def modify_user(self, nombre, contraseña, salt):
        self.load_store()
        for item in self._data_list:
            if item[self._ID_FIELD] == nombre:
                item['password'] = contraseña.decode('latin-1')
                item['salt'] = salt.decode('latin-1')
        self.save_store()