#! usr/bin/env python
from PyQt5 import QtWidgets, uic
import sys


class AlgoritmoView(QtWidgets.QDialog):
    def __init__(self):
        super(AlgoritmoView, self).__init__()
        uic.loadUi('Views/QtViews/Algoritmo_Window.ui', self)
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.inicio.clicked.connect(self.setClose)
        self._isClose = False
    
    def setClose(self):
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose