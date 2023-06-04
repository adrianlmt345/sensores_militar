# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensores.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 291)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tabla = QtWidgets.QPushButton(self.centralwidget)
        self.Tabla.setGeometry(QtCore.QRect(20, 10, 75, 23))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.Tabla.setFont(font)
        self.Tabla.setStyleSheet("color: rgb(0, 0, 0);")
        self.Tabla.setObjectName("Tabla")
        self.Temperatura = QtWidgets.QPushButton(self.centralwidget)
        self.Temperatura.setGeometry(QtCore.QRect(110, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.Temperatura.setFont(font)
        self.Temperatura.setObjectName("Temperatura")
        self.Movimiento = QtWidgets.QPushButton(self.centralwidget)
        self.Movimiento.setGeometry(QtCore.QRect(240, 10, 91, 23))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.Movimiento.setFont(font)
        self.Movimiento.setObjectName("Movimiento")
        self.Vibraciones = QtWidgets.QPushButton(self.centralwidget)
        self.Vibraciones.setGeometry(QtCore.QRect(350, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.Vibraciones.setFont(font)
        self.Vibraciones.setObjectName("Vibraciones")
        self.Sonido = QtWidgets.QPushButton(self.centralwidget)
        self.Sonido.setGeometry(QtCore.QRect(480, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.Sonido.setFont(font)
        self.Sonido.setObjectName("Sonido")
        self.Salir = QtWidgets.QPushButton(self.centralwidget)
        self.Salir.setGeometry(QtCore.QRect(310, 90, 75, 23))
        self.Salir.setObjectName("Salir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 60, 171, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabla_sensores = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_sensores.setGeometry(QtCore.QRect(20, 50, 256, 192))
        self.tabla_sensores.setObjectName("tabla_sensores")
        self.tabla_sensores.setColumnCount(0)
        self.tabla_sensores.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Salir.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tabla.setText(_translate("MainWindow", "Tabla"))
        self.Temperatura.setText(_translate("MainWindow", "Temperatura"))
        self.Movimiento.setText(_translate("MainWindow", "Movimiento"))
        self.Vibraciones.setText(_translate("MainWindow", "Vibraciones"))
        self.Sonido.setText(_translate("MainWindow", "Sonido"))
        self.Salir.setText(_translate("MainWindow", "Salir"))

