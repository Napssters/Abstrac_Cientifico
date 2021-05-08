#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Controller import Controlador as Ctd
import sys


class StopWordsView(QtWidgets.QDialog):
    def __init__(self):
        super(StopWordsView, self).__init__()
        uic.loadUi('Views/QtViews/StopWords_Window.ui', self)
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.ver = self.findChild(QtWidgets.QPushButton, 'ver')
        self.stopword = self.findChild(QtWidgets.QTextEdit, 'stopwords')
        self.inicio.clicked.connect(self.setClose)
        self.ver.clicked.connect(self.getStopWords)
        self.controller = Ctd.Controlador()
        self._isClose = False
    
    def getStopWords(self):
        stops = "\""
        stops += '"\t"'.join(self.controller.getStopWord())
        stops += "\""
        self.stopword.setText(stops)


    def setClose(self):
        self.stopword.setText("")
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose