from restaurantes.Restaurante1 import Restaurante1
from restaurantes.Restaurante2 import Restaurante2
from restaurantes.Restaurante3 import Restaurante3
from restaurantes.Restaurante4 import Restaurante4
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
class Usuario():
    def __init__(self, nombre, contraseña, telefono, salt):
        self.nombre = nombre
        self.contraseña = contraseña.decode('latin-1')
        self.telefono = telefono
        self.salt = salt.decode('latin-1')

    def __dict__(self):
        return {"nombre": self.nombre, "password": self.contraseña, "telefono": self.telefono, "salt":self.salt}

    def encriptar(self, pedido):
        restaurante_pedido = pedido.restaurante
        restaurante = None
        if restaurante_pedido == "Restaurante1":
            restaurante = Restaurante1()
        elif restaurante_pedido == "Restaurante2":
            restaurante = Restaurante2()
        elif restaurante_pedido == "Restaurante3":
            restaurante = Restaurante3()
        elif restaurante_pedido == "Restaurante4":
            restaurante = Restaurante4()
        else:
            print("error")
        pk_restaurante = restaurante.public_key
        message = str(pedido).encode("latin-1")
        ciphertext = pk_restaurante.encrypt(
                message,
                padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        restaurante.descifrar(ciphertext)
        return ciphertext

