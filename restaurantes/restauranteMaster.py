from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
class RestauranteMaster():
    def __init__(self):
        self.private_key = ""
        self.public_key = ""