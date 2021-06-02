#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Views import Agrupar as Ag
from Views import PesosOraciones as Po
from Views import Promedio as Pm
from Views import Resumen as Rm
from Views import SorteoOraciones as So
from Views import StopWords as Sw
from Views import SumaFrecuencia as Sf
from Views import TablaFrecuencia as Tf
from Views import Tokenizar as Tn
from Views import TokenizarSenteces as Ts
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
        self.AgView = Ag.AgruparView()
        self.PoView = Po.PesosOracionesView()
        self.PmView = Pm.PromedioView()
        self.RmView = Rm.ResumenView()
        self.SoView = So.SorteoOracionesView()
        self.SwView = Sw.StopWordsView()
        self.SfView = Sf.SumaFrecuenciaView()
        self.TfView = Tf.TablaFrecuenciaView()
        self.TnView = Tn.TokenizarView()
        self.TsView = Ts.TokenizarSentencesView()
        self._isClose = False

    def Paso1(self):
        self.hide()
        self.SwView._isClose = False
        self.SwView.exec_()
        if(self.SwView.isClose() == True):
            self.setClose()

    def Paso2(self):
        self.hide()
        self.TnView._isClose = False
        self.TnView.exec_()
        if(self.TnView.isClose() == True):
            self.setClose()

    def Paso3(self):
        self.hide()
        self.TfView._isClose = False
        self.TfView.exec_()
        if(self.TfView.isClose() == True):
            self.setClose()

    def Paso4(self):
        self.hide()
        self.TsView._isClose = False
        self.TsView.exec_()
        if(self.TsView.isClose() == True):
            self.setClose()

    def Paso5(self):
        self.hide()
        self.PoView._isClose = False
        self.PoView.exec_()
        if(self.PoView.isClose() == True):
            self.setClose()

    def Paso6(self):
        self.hide()
        self.SfView._isClose = False
        self.SfView.exec_()
        if(self.SfView.isClose() == True):
            self.setClose()

    def Paso7(self):
        self.hide()
        self.PmView._isClose = False
        self.PmView.exec_()
        if(self.PmView.isClose() == True):
            self.setClose()

    def Paso8(self):
        self.hide()
        self.AgView._isClose = False
        self.AgView.exec_()
        if(self.AgView.isClose() == True):
            self.setClose()

    def Paso9(self):
        self.hide()
        self.SoView._isClose = False
        self.SoView.exec_()
        if(self.SoView.isClose() == True):
            self.setClose()

    def Paso10(self):
        self.hide()
        self.RmView._isClose = False
        self.RmView.exec_()
        if(self.RmView.isClose() == True):
            self.setClose()

    def setClose(self):
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose
