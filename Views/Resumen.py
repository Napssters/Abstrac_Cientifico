#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Controller import Controlador as Ctd
import sys


class ResumenView(QtWidgets.QDialog):
    def __init__(self):
        super(ResumenView, self).__init__()
        uic.loadUi('Views/QtViews/Resumen_Window.ui', self)
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.ver = self.findChild(QtWidgets.QPushButton, 'ver')
        self.contenedor = self.findChild(QtWidgets.QTextEdit, 'contenedor')
        self.algoritmo = self.findChild(QtWidgets.QPushButton, 'algoritmo')
        self.algoritmo.clicked.connect(self.MenuAlgoritmo)
        self.inicio.clicked.connect(self.setClose)
        self.ver.clicked.connect(self.getResumen)
        self.controller = Ctd.Controlador()
        self._isClose = False
        self.menu = False

    def getResumen(self):
        stops = "\""
        stops += '"\t"'.join(self.controller.getStopWord())
        stops += "\""
        self.contenedor.setText(stops)

    def MenuAlgoritmo(self):
        self.contenedor.setText("")
        self._isClose = True
        self.menu = True
        self.isClose()
        return self.menu
        
    def setClose(self):
        self.contenedor.setText("")
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose
