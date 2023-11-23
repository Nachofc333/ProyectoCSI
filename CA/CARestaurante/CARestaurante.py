import os
from CA.CAMaster import CAMaster

JSON_FILES_PATH = os.path.dirname(__file__)


class CARestaurante(CAMaster):
    _FILE_NAME = JSON_FILES_PATH + "/CARestaurante.pem"

    def __init__(self):
        super(CAMaster, self).__init__()
        self._private_key = self.genererkey()
        self.public_key = self._private_key.public_key()
