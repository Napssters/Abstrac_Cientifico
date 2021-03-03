#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Model import PdfReader as Rd
import sys

class SummaryView(QtWidgets.QDialog) :
    def __init__(self):
        super(SummaryView, self).__init__()
        self.Reader = Rd.Reader()
        uic.loadUi('Views/QtViews/Summary_Window.ui', self)
        self.generated = self.findChild(QtWidgets.QPushButton, 'generar')
        self.exported = self.findChild(QtWidgets.QPushButton, 'exportar')
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.summary = self.findChild(QtWidgets.QTextEdit, 'summary')
        self.inicio.clicked.connect(self.setClose)
        self.generated.clicked.connect(self.LoadFile)
        self._isClose = False

    def LoadFile(self):
        pdf = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir Archivo', 'c:\\', "PDF-Files (*.pdf)")
        file = pdf[0]
        self.summary.setText(self.Reader.getPdf(file))
        self.summary.setReadOnly(True)


    def setClose(self):
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose
