from PyQt5 import QtWidgets
from controladores.controladorLogin import Controlador_login
import sys
from CA.CAR.CAR import CAR


if __name__ == '__main__':                      #  Iniciador del código
    app = QtWidgets.QApplication(sys.argv)
    login = Controlador_login()
    login.show()
    ca = CAR()
    sys.exit(app.exec_())