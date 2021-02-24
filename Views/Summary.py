from PyQt5 import QtWidgets, uic
import sys

class SummaryView(QtWidgets.QDialog) :
    def __init__(self):
        super(SummaryView, self).__init__()
        uic.loadUi('Views/QtViews/Summary_Window.ui', self)
        self.generated = self.findChild(QtWidgets.QPushButton, 'generar')
        self.exported = self.findChild(QtWidgets.QPushButton, 'exportar')
        self.inicio = self.findChild(QtWidgets.QPushButton, 'inicio')
        self.inicio.clicked.connect(self.setClose)
        self.generated.clicked.connect(self.LoadFile)
        self._isClose = False

    def LoadFile(self):
        print("Cargando el documento")

    def setClose(self):
        self._isClose = True
        self.isClose()

    def isClose(self):
        self.hide()
        return self._isClose
