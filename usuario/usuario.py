from restaurantes.restaurante1.Restaurante1 import Restaurante1
from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4
from cryptography.hazmat.primitives.asymmetric import padding as pd
import os
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Usuario():
    def __init__(self, nombre, contraseña, telefono, salt):
        self.nombre = nombre
        self.contraseña = contraseña.decode('latin-1')
        self.telefono = telefono
        self.salt = salt.decode('latin-1')
        self._key = os.urandom(32)
        self.iv = os.urandom(16)
        self.cipherkey = ""

    def __dict__(self):
        return {"nombre": self.nombre, "password": self.contraseña, "telefono": self.telefono, "salt":self.salt}

    def encriptariv(self, restaurante):
        pk_restaurante = restaurante.public_key
        self.ivencrip = pk_restaurante.encrypt(
            self.iv,
            pd.OAEP(
                mgf=pd.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        return self.ivencrip

    def encriptar(self, pedido):  # funcion encargada de buscar el restaurante al que se esta pidiendo, para obtener su PK
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
        self.encriptarKEY(restaurante, self._key)  # llamada a encriptarKey, que encriptará la key con la PK del restaurante
        ct = self.encriptarPedido(pedido, restaurante, self._key, self.iv)  # pedido encriptado simetricamente
        if ct:
            return ct
        return False

    def encriptarPedido(self, pedido, restaurante, key, iv):  # funcion encargada de encriptar el pedido de forma simetrica
        h = hmac.HMAC(self._key, hashes.SHA256())
        h.update(str(pedido).encode('latin-1'))
        signature = h.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        # Crear un nuevo padder para el pedido
        padder_pedido = padding.PKCS7(128).padder()
        padded_data = padder_pedido.update(str(pedido).encode("latin-1")) + padder_pedido.finalize()
        ct = encryptor.update(padded_data) + encryptor.finalize()

        # Crear un nuevo padder para la firma
        padder_signature = padding.PKCS7(128).padder()
        padded_signature = padder_signature.update(signature)

        # Crear un nuevo encryptor para la firma
        cipher_signature = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor_signature = cipher_signature.encryptor()
        cs = encryptor_signature.update(padded_signature) + encryptor_signature.finalize()
        ivencrip = self.encriptariv(restaurante)
        if restaurante.descifrarPedido(ct, cs, ivencrip):  # el restaurante descifrara el pedido con la key descifrada
            return ct, self.cipherkey
        return False

    def encriptarKEY(self, restaurante, key):  # funcion encargada de encriptar la key simetrica con la pk del restaurante al que se le realizo el pedido
        pk_restaurante = restaurante.public_key
        message = key
        self.cipherkey = pk_restaurante.encrypt(
            message,
            pd.OAEP(
                mgf=pd.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        restaurante.descifrarKEY(self.cipherkey)  # el restaurante descifrara la key con su clave privada