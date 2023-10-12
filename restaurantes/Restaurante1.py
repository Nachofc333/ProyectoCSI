from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from restauranteMaster import RestauranteMaster
class Restaurante1(RestauranteMaster):
    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key =rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            )
        self.public_key = self.private_key.public_key()

a = Restaurante1()
pem = a.public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)
pem.splitlines()[0]
print(pem)
print(pem.splitlines()[0])

pem = a.private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.TraditionalOpenSSL,
   encryption_algorithm=serialization.NoEncryption()
)
pem.splitlines()[0]
print(pem)
print(pem.splitlines()[0])