import os
from CA.CAMaster import CAMaster
from CA.CAR.CAR import CAR
from cryptography.hazmat.primitives import serialization
from datetime import datetime

JSON_FILES_PATH = os.path.dirname(__file__)
now = datetime.utcnow()

class CARestaurante(CAMaster):
    _NAME = "CARestaurante"
    _FILE_NAME_KEY = JSON_FILES_PATH + "/CARestaurante_key.pem"
    _FILE_NAME_CSR = JSON_FILES_PATH + "/CARestaurante_csr.pem"
    _FILE_NAME_CTR = JSON_FILES_PATH + "/CARestaurante_cert.pem"

    def __init__(self):
        super(CAMaster, self).__init__()
        self._private_key = self.genererkey()
        self.public_key = self._private_key.public_key()
        self.name = self.generarNombre()
        self.CA = CAR()
        self.cert = self.CA.crearCA(self.generarCSR(), self.public_key, self.name)
        self.cargarCert()
        if not self.cert.not_valid_before <= now <= self.cert.not_valid_after:
            self.recargarCA()
            self.cargarCert()

    def cargarCert(self):
        if not os.path.exists(self._FILE_NAME_CTR):
            with open(self._FILE_NAME_CTR, "wb") as f:
                f.write(self.cert.public_bytes(serialization.Encoding.PEM))

    def recargarCA(self):
        os.remove(self._FILE_NAME_CTR)
        os.remove(self._FILE_NAME_CSR)
        self.cert = self.CA.crearCA(self.generarCSR(), self.public_key, self.name)