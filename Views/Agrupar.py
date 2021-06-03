#! usr/bin/env python
from PyQt5 import QtWidgets, uic
import sys


class AgruparView(QtWidgets.QDialog):
    def __init__(self):
        super(AgruparView, self).__init__()
        uic.loadUi('Views/QtViews/Agrupar_Window.ui', self)
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.ver = self.findChild(QtWidgets.QPushButton, 'ver')
        self.contenedor = self.findChild(QtWidgets.QTextEdit, 'contenedor')
        self.algoritmo = self.findChild(QtWidgets.QPushButton, 'algoritmo')
        self.algoritmo.clicked.connect(self.MenuAlgoritmo)
        self.inicio.clicked.connect(self.setClose)
        self.ver.clicked.connect(self.getAgrupar)
        self._isClose = False
        self.menu = False
        self.step = ""

    def getAgrupar(self):
        stops = "\""
        stops += '"\t"' + self.step
        stops += "\""
        self.contenedor.setText(stops)

    def MenuAlgoritmo(self):
        self.menu = True
        self.setClose()
        return self.menu

    def setClose(self):
        self.contenedor.setText("")
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose
