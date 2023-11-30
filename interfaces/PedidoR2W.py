# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PedidoR2W.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pedido2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -20, 841, 661))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.506, y2:1, stop:0 rgba(0, 142, 202, 255), stop:0.846591 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 371, 71))
        self.label_2.setStyleSheet("font: 20pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.SelectorRestaurante = QtWidgets.QComboBox(self.centralwidget)
        self.SelectorRestaurante.setGeometry(QtCore.QRect(260, 70, 261, 31))
        self.SelectorRestaurante.setObjectName("SelectorRestaurante")
        self.SelectorRestaurante.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 331, 71))
        self.label_3.setStyleSheet("font: 20pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 210, 371, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Pasta = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.Pasta.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.Pasta.setObjectName("Pasta")
        self.gridLayout.addWidget(self.Pasta, 0, 0, 1, 1)
        self.Lentejas = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.Lentejas.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.Lentejas.setObjectName("Lentejas")
        self.gridLayout.addWidget(self.Lentejas, 2, 0, 1, 1)
        self.Filete = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.Filete.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.Filete.setObjectName("Filete")
        self.gridLayout.addWidget(self.Filete, 1, 0, 1, 1)
        self.Hamburguesa = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.Hamburguesa.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.Hamburguesa.setObjectName("Hamburguesa")
        self.gridLayout.addWidget(self.Hamburguesa, 4, 0, 1, 1)
        self.EnviarPedido = QtWidgets.QPushButton(self.centralwidget)
        self.EnviarPedido.setGeometry(QtCore.QRect(490, 400, 291, 131))
        self.EnviarPedido.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EnviarPedido.setStyleSheet("font: 26pt \"Segoe UI\";")
        self.EnviarPedido.setObjectName("EnviarPedido")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 390, 371, 73))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Tarta = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.Tarta.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.Tarta.setObjectName("Tarta")
        self.gridLayout_2.addWidget(self.Tarta, 0, 0, 1, 1)
        self.Brownie = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.Brownie.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.Brownie.setObjectName("Brownie")
        self.gridLayout_2.addWidget(self.Brownie, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 91, 41))
        self.label_4.setStyleSheet("font: 15pt \"Segoe UI\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 350, 101, 41))
        self.label_5.setStyleSheet("font: 15pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 10, 231, 41))
        self.label_6.setStyleSheet("\n"
"font: 20pt \"Wide Latin\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.label_7.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"background-color: rgb(42, 170, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.Pedidos = QtWidgets.QPushButton(self.centralwidget)
        self.Pedidos.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.Pedidos.setStyleSheet("background-color: rgb(37, 179, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.Pedidos.setObjectName("Pedidos")
        self.label.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.SelectorRestaurante.raise_()
        self.label_3.raise_()
        self.gridLayoutWidget.raise_()
        self.EnviarPedido.raise_()
        self.gridLayoutWidget_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.Pedidos.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Restaurante"))
        self.SelectorRestaurante.setItemText(0, _translate("MainWindow", "Restaurante 2"))
        self.label_3.setText(_translate("MainWindow", "Selecciona el Pedido"))
        self.Pasta.setText(_translate("MainWindow", "Pasta a la carbonara"))
        self.Lentejas.setText(_translate("MainWindow", "Lentejas de la abuela"))
        self.Filete.setText(_translate("MainWindow", "Filete de ternera"))
        self.Hamburguesa.setText(_translate("MainWindow", "Hamburguesa tradicional"))
        self.EnviarPedido.setText(_translate("MainWindow", "Enviar pedido"))
        self.Tarta.setText(_translate("MainWindow", "Tarta de queso"))
        self.Brownie.setText(_translate("MainWindow", "Brownie"))
        self.label_4.setText(_translate("MainWindow", "Platos:"))
        self.label_5.setText(_translate("MainWindow", "Postres:"))
        self.label_6.setText(_translate("MainWindow", "GLOVO"))
        self.Pedidos.setText(_translate("MainWindow", "Restaurantes"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Pedido2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())