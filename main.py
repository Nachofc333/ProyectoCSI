from PyQt5 import QtWidgets
from controladores.controladorLogin import Controlador_login

import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windowExample = Controlador_login()
    windowExample.show()
    sys.exit(app.exec_())