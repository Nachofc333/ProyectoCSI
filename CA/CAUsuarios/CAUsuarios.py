import os
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from CA.CAMaster import CAMaster

JSON_FILES_PATH = os.path.dirname(__file__)


class CAUsuarios(CAMaster):
    _NAME = "CAUsuario"
    _FILE_NAME = JSON_FILES_PATH + "/CAUsuario.pem"

    def __init__(self):
        super(CAMaster, self).__init__()
        self.name = "CAUsuarios"
        self._private_key = self.genererkey()
        self.public_key = self._private_key.public_key()

    def requestCA2(self, publick_key, csr):
        Autoridad = CAMaster()
        certificate = Autoridad.crearCA(publick_key, csr)
        return certificate
