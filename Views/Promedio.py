#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Controller import Controlador as Ctd
import sys


class PromedioView(QtWidgets.QDialog):
    def __init__(self):
        super(PromedioView, self).__init__()
        uic.loadUi('Views/QtViews/Promedio_Window.ui', self)
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.ver = self.findChild(QtWidgets.QPushButton, 'ver')
        self.contenedor = self.findChild(QtWidgets.QTextEdit, 'contenedor')
        self.inicio.clicked.connect(self.setClose)
        self.ver.clicked.connect(self.getPromedio)
        self.controller = Ctd.Controlador()
        self._isClose = False

    def getPromedio(self):
        stops = "\""
        stops += '"\t"'.join(self.controller.getStopWord())
        stops += "\""
        self.contenedor.setText(stops)


    def setClose(self):
        self.contenedor.setText("")
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose
