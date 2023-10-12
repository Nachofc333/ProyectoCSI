import hashlib
import json
class Pedido():
    def __init__(self, restaurante, pasta, filete, lentejas, hamburguesa, tarta):
        self.restaurante = restaurante
        self.pasta = pasta
        self.filete = filete
        self.lentejas = lentejas
        self.hamburguesa = hamburguesa
        self.tarta = tarta
        id_str = json.dumps(self.__dict__(), sort_keys=True)
        self.id = hashlib.sha256(id_str.encode()).hexdigest()
        print(self)
        print(self.id)
        print(self.__dict__())
    def __str__(self):
        return "Pedido:" + json.dumps(self.__dict__(), sort_keys=True)

    def __dict__(self):
        dict_ = {
            "restaurante": self.restaurante,
            "pasta": self.pasta,
            "filete": self.filete,
            "lentejas": self.lentejas,
            "hamburguesa": self.hamburguesa,
            "tarta": self.tarta,
        }
        if hasattr(self, 'id'):  # Solo incluimos 'id' si ya existe
            dict_["id"] = self.id
        return dict_