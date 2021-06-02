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
from Views import TokenizarSentences as Ts
from Controller import Controlador as Ctd
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
        self.SwView._isClose = False
        self.SwView.menu = False
        self.SwView.exec_()
        if(self.SwView.isClose() == True):
            if(self.SwView.menu == True):
                self.show()
            if(self.SwView.menu == False):
                self.setClose()

    def Paso2(self):
        self.TnView._isClose = False
        self.TnView.menu = False
        self.TnView.exec_()
        if(self.TnView.isClose() == True):
            if(self.TnView.menu == True):
                self.show()
            if(self.TnView.menu == False):
                self.setClose()

    def Paso3(self):
        self.TfView._isClose = False
        self.TfView.menu = False
        self.TfView.exec_()
        if(self.TfView.isClose() == True):
            if(self.TfView.menu == True):
                self.show()
            if(self.TfView.menu == False):
                self.setClose()

    def Paso4(self):
        self.TsView._isClose = False
        self.TsView.menu = False
        self.TsView.exec_()
        if(self.TsView.isClose() == True):
            if(self.TsView.menu == True):
                self.show()
            if(self.TsView.menu == False):
                self.setClose()

    def Paso5(self):
        self.PoView._isClose = False
        self.PoView.menu = False
        self.PoView.exec_()
        if(self.PoView.isClose() == True):
            if(self.PoView.menu == True):
                self.show()
            if(self.PoView.menu == False):
                self.setClose()

    def Paso6(self):
        self.SfView._isClose = False
        self.SfView.menu = False
        self.SfView.exec_()
        if(self.SfView.isClose() == True):
            if(self.SfView.menu == True):
                self.show()
            if(self.SfView.menu == False):
                self.setClose()

    def Paso7(self):
        self.PmView._isClose = False
        self.PmView.menu = False
        self.PmView.exec_()
        if(self.PmView.isClose() == True):
            if(self.PmView.menu == True):
                self.show()
            if(self.PmView.menu == False):
                self.setClose()

    def Paso8(self):
        self.AgView._isClose = False
        self.AgView.menu = False
        self.AgView.exec_()
        if(self.AgView.isClose() == True):
            if(self.AgView.menu == True):
                self.show()
            if(self.AgView.menu == False):
                self.setClose()

    def Paso9(self):
        self.SoView._isClose = False
        self.SoView.menu = False
        self.SoView.exec_()
        if(self.SoView.isClose() == True):
            if(self.SoView.menu == True):
                self.show()
            if(self.SoView.menu == False):
                self.setClose()

    def Paso10(self):
        self.RmView._isClose = False
        self.RmView.menu = False
        self.RmView.exec_()
        if(self.RmView.isClose() == True):
            if(self.RmView.menu == True):
                self.show()
            if(self.RmView.menu == False):
                self.setClose()

    def setClose(self):
        self._isClose = True
        self.isClose()

    def isClose(self):
        return self._isClose
