from restaurantes.Restaurante1 import Restaurante1
from restaurantes.Restaurante2 import Restaurante2
from restaurantes.Restaurante3 import Restaurante3
from restaurantes.Restaurante4 import Restaurante4
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as pd
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Usuario():
    def __init__(self, nombre, contraseña, telefono, salt):
        self.nombre = nombre
        self.contraseña = contraseña.decode('latin-1')
        self.telefono = telefono
        self.salt = salt.decode('latin-1')
        self._key = os.urandom(32)

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
        self.encriptarKEY(restaurante, self._key)
        return self.encriptarPedido(pedido, restaurante, self._key, restaurante.iv)

    def encriptarPedido(self, pedido, restaurante, key, iv):
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(str(pedido).encode("latin-1")) + padder.finalize()
        ct = encryptor.update(padded_data) + encryptor.finalize()
        restaurante.descifrarPedido(ct)
        return ct

    """def encriptarPedido(self, pedido, restaurante, key):
        nonce = os.urandom(12)
        aesgcm = AESGCM(key)
        ct = aesgcm.encrypt(nonce, str(pedido).encode("latin-1"), None)
        restaurante.descifrarPedido(nonce, ct)
        return ct"""
    def encriptarKEY(self, restaurante, key):
        pk_restaurante = restaurante.public_key
        message = key
        cipherkey = pk_restaurante.encrypt(
            message,
            pd.OAEP(
                mgf=pd.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        restaurante.descifrarKEY(cipherkey)


    """"def encriptarKEY(self, pedido):
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
"""
