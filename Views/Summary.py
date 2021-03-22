#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Controller import Controlador as Ctd
import sys

class SummaryView(QtWidgets.QDialog) :
    def __init__(self):
        super(SummaryView, self).__init__()
        uic.loadUi('Views/QtViews/Summary_Window.ui', self)
        self.generated = self.findChild(QtWidgets.QPushButton, 'generar')
        self.exported = self.findChild(QtWidgets.QPushButton, 'exportar')
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.summary = self.findChild(QtWidgets.QTextEdit, 'summary')
        self.inicio.clicked.connect(self.setClose)
        self.generated.clicked.connect(self.LoadFile)
        self.exported.clicked.connect(self.ExportFile)
        self.controller = Ctd.Controlador()
        self.summarytext = ""
        self._isClose = False

    def LoadFile(self):
        pdf = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir Archivo', 'c:\\', "PDF-Files (*.pdf)")
        file = pdf[0]
        self.summarytext = self.controller.DoSummary(file)
        self.summary.setText(self.summarytext)
        self.summary.setReadOnly(True)

    def ExportFile(self):
        option = QtWidgets.QFileDialog.Options()
        filess = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File Window Title', 'default.txt', "All Files (*)", options=option)
        try:
            file = open(filess[0], "w")
            summary = str (self.summarytext)
            file.write(summary)
            file.close()
        except:
            pass

    def setClose(self):
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose
