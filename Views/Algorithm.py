#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Views import StopWords as Sw
import sys


class AlgoritmoView(QtWidgets.QDialog):
    def __init__(self):
        super(AlgoritmoView, self).__init__()
        uic.loadUi('Views/QtViews/Algoritmo_Window.ui', self)
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.paso1 = self.findChild(QtWidgets.QPushButton, 'paso1')
        self.inicio.clicked.connect(self.setClose)
        self.paso1.clicked.connect(self.Paso1)
        self.SwView = Sw.StopWordsView()
        self._isClose = False
    
    def Paso1(self):
        self.hide()
        self.SwView._isClose = False
        self.SwView.exec_()
        if(self.SwView.isClose() == True):
            self.setClose()

    def setClose(self):
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose