import hashlib
import json
class Pedido():
    def __init__(self, restaurante, pasta, filete, lentejas, hamburguesa, tarta, brownie):
        self.restaurante = restaurante
        self.pasta = pasta
        self.filete = filete
        self.lentejas = lentejas
        self.hamburguesa = hamburguesa
        self.tarta = tarta
        self.brownie = brownie
        id_str = json.dumps(self.__dict__(), sort_keys=True)
        self.id = hashlib.sha256(id_str.encode()).hexdigest()
    def __str__(self):
        return "Pedido:" + json.dumps(self.__dict__(), sort_keys=True)

    def __dict__(self):
        dict_ = {
            "restaurante": self.restaurante,

        }
        if self.pasta != 0:
            dict_["pasta"] = self.pasta
        if self.filete != 0:
            dict_["filete"] = self.filete
        if self.lentejas != 0:
            dict_["lentejas"] = self.lentejas
        if self.hamburguesa != 0:
            dict_["hamburguesa"] = self.hamburguesa
        if self.tarta != 0:
            dict_["tarta"] = self.tarta
        if self.brownie != 0:
            dict_["brownie"] = self.brownie

        if hasattr(self, 'id'):  # Solo incluimos 'id' si ya existe
            dict_["id"] = self.id
        return dict_