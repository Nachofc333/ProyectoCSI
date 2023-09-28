from almacen.jsonAlmacen import JsonAlmacen
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
salt = os.urandom(16)
a = JsonAlmacen()
match = a.find_name("l")
if match:
    print("Y")

password = "Hola"
salt = os.urandom(16)
kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
        )
salt = salt.decode("utf-8")
key = kdf.derive(password.encode("utf-8"))
kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode("utf-8"),
        iterations=480000,
        )
kdf.verify(password.encode("utf-8"), key)
