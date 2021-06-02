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
        self.paso2 = self.findChild(QtWidgets.QPushButton, 'paso2')
        self.paso3 = self.findChild(QtWidgets.QPushButton, 'paso3')
        self.paso4 = self.findChild(QtWidgets.QPushButton, 'paso4')
        self.paso5 = self.findChild(QtWidgets.QPushButton, 'paso5')
        self.paso6 = self.findChild(QtWidgets.QPushButton, 'paso6')
        self.paso7 = self.findChild(QtWidgets.QPushButton, 'paso7')
        self.paso8 = self.findChild(QtWidgets.QPushButton, 'paso8')
        self.paso9 = self.findChild(QtWidgets.QPushButton, 'paso9')
        self.paso10 = self.findChild(QtWidgets.QPushButton, 'paso10')
        self.inicio.clicked.connect(self.setClose)
        self.paso1.clicked.connect(self.Paso1)
        self.paso2.clicked.connect(self.Paso2)
        self.paso3.clicked.connect(self.Paso3)
        self.paso4.clicked.connect(self.Paso4)
        self.paso5.clicked.connect(self.Paso5)
        self.paso6.clicked.connect(self.Paso6)
        self.paso7.clicked.connect(self.Paso7)
        self.paso8.clicked.connect(self.Paso8)
        self.paso9.clicked.connect(self.Paso9)
        self.paso10.clicked.connect(self.Paso10)
        self.SwView = Sw.StopWordsView()
        self._isClose = False

    def Paso1(self):
        self.hide()
        self.SwView._isClose = False
        self.SwView.exec_()
        if(self.SwView.isClose() == True):
            self.setClose()

    def Paso2(self):
        self.hide()

    def Paso3(self):
        self.hide()

    def Paso4(self):
        self.hide()

    def Paso5(self):
        self.hide()

    def Paso6(self):
        self.hide()

    def Paso7(self):
        self.hide()

    def Paso8(self):
        self.hide()

    def Paso9(self):
        self.hide()

    def Paso10(self):
        self.hide()

    def setClose(self):
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose
