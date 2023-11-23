from PyQt5 import QtWidgets
from controladores.controladorLogin import Controlador_login
from CA.CAR.CAR import CAR
from CA.CAUsuarios.CAUsuarios import CAUsuarios
from CA.CARestaurante.CARestaurante import CARestaurante

import sys

def generarCA():

    pass


if __name__ == '__main__':                      #  Iniciador del código
    app = QtWidgets.QApplication(sys.argv)
    login = Controlador_login()
    login.show()
    generarCA()
    sys.exit(app.exec_())