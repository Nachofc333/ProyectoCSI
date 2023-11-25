import os
from CA.CAMaster import CAMaster
from CA.CAR.CAR import CAR

JSON_FILES_PATH = os.path.dirname(__file__)


class CARestaurante(CAMaster):
    _NAME = "CARestaurante"
    _FILE_NAME = JSON_FILES_PATH + "/CARestaurante_key.pem"
    _FILE_NAME_CSR = JSON_FILES_PATH + "/CARestaurante_csr.pem"

    def __init__(self):
        super(CAMaster, self).__init__()
        self._private_key = self.genererkey()
        self.public_key = self._private_key.public_key()
        self.CA = CAR()

