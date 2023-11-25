import os
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
