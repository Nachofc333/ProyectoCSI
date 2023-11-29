from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from CA.CAR.CAR import CAR
from CA.CAUsuarios.CAUsuarios import CAUsuarios
from CA.CARestaurante.CARestaurante import CARestaurante
from datetime import datetime

JSON_FILES_PATH = os.path.dirname(__file__)
now = datetime.utcnow()
class RestauranteMaster(QtWidgets.QMainWindow):
    _KEY = ""
    _FILE_NAME = ""
    _NAME = ""

    def __init__(self):
        super().__init__()
        self._private_key = ""
        self.public_key = ""
        self.iv = b""
        self._key = b""
        self.almacen = None
        self.almacenDesencriptado = None
        self.name = self.generarName()
        self.cert = self.requestCA()
        if not self.cert.not_valid_before <= now <= self.cert.not_valid_after:
            self.recargarCA()
        self.car = CAR()
        self.CAUsuario = CAUsuarios()

    def descifrarKEY(self, key):  # funcion encargada de descifrar la key simetrica con la clave privada del restaurante
        key = self._private_key.decrypt(
            key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        self._key = key

    def descifrariv(self, ivencrip):  # funcion encargada de descifrar el iv de la comunicación simétrica con la clave privada del restauranteb
        iv = self._private_key.decrypt(
            ivencrip,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        self.iv = iv

    def descifrarPedido(self, ct, signature, ivencrip, pk_usuario, cert_usuario):  # funcion encargada de descifrar el pedido con la key simetrica descifrada
        if self.validarCertificados(self.car.cert, self.CAUsuario.cert, cert_usuario):

            self.descifrariv(ivencrip)

            cipher = Cipher(algorithms.AES(self._key), modes.CBC(self.iv))

            decryptor = cipher.decryptor()
            plaintext = decryptor.update(ct) + decryptor.finalize()

            # Quitar el padding
            plaintextf = plaintext.rstrip(plaintext[-1:]).decode('latin-1')

            h = hmac.HMAC(self._key, hashes.SHA256())
            h.update(plaintextf.encode("latin-1"))
            hash = h.finalize()
            # Crear un nuevo decryptor para la firma

            try:
                pk_usuario.verify(
                    signature,
                    hash,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )
                alerta = QMessageBox.information(self, 'Pedido', plaintextf, QMessageBox.Ok)
            except:
                alerta = QMessageBox.information(self, 'Error', "Pedido modificado", QMessageBox.Ok)
                return False
            return True
        return None

    def genererkey(self):
        if not os.path.exists(self._FILE_NAME):
            # Si no existe, genera la clave privada
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
            )

            # Guarda la clave privada en un archivo PEM
            with open(self._FILE_NAME, "wb") as f:
                f.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))

        # Lee la clave privada desde un archivo PEM
        with open(self._FILE_NAME, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )
        return private_key

    def desencriptarPedidos(self, pedidocifrado):
        self.descifrarKEY(pedidocifrado.key.encode("latin-1"))  # key descifrada

        self.descifrariv(pedidocifrado.iv.encode("latin-1"))  # iv descifrado

        cipher = Cipher(algorithms.AES(self._key), modes.CBC(self.iv))
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(pedidocifrado.pedido.encode("latin-1")) + decryptor.finalize()  # pedido descifrado

        # Quitar el padding del pedido
        plaintextf = plaintext.rstrip(plaintext[-1:]).decode('latin-1')
        return plaintextf

    def generarName(self):
        return x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, self._NAME),
        ])
    def requestCA(self):
        # Generate a CSR
        csr = x509.CertificateSigningRequestBuilder().subject_name(self.name).sign(self._private_key, hashes.SHA256())
        Autoridad = CARestaurante()
        certificado = Autoridad.crearCA(csr, self.public_key, self.name)
        path = JSON_FILES_PATH +"/"+ self._NAME + "/cert.pem"
        with open(path, "wb") as f:
            f.write(certificado.public_bytes(serialization.Encoding.PEM))
        return certificado
    def recargarCA(self):
        path = JSON_FILES_PATH +"/"+ self._NAME + "/cert.pem"
        os.remove(path)
        self.cert = self.requestCA()

    def validarCertificados(self, caR, caUs, usuario):
        # Se verifica la cadena de certificados
        try:
            caR.public_key().verify(
                caUs.signature,
                caUs.tbs_certificate_bytes,
                padding.PKCS1v15(),
                hashes.SHA256(),
            )
            caUs.public_key().verify(
                usuario.signature,
                usuario.tbs_certificate_bytes,
                padding.PKCS1v15(),
                hashes.SHA256(),
            )
            return True
        except Exception:
            return False


