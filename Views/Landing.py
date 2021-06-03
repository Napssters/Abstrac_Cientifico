#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Views import Summary as Sm
from Views import Algorithm as At
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Views/QtViews/Landing_Window.ui', self)
        self.abstracts = self.findChild(QtWidgets.QPushButton, 'abstracts')
        self.algorithm = self.findChild(QtWidgets.QPushButton, 'algoritmo')
        self.abstracts.clicked.connect(self.StartSummary)
        self.algorithm.clicked.connect(self.StartAlgorithm)
        self.SmView = Sm.SummaryView()
        self.AtView = At.AlgoritmoView()

    def StartSummary(self):
        self.hide()
        self.SmView._isClose = False
        self.SmView.exec_()
        if(self.SmView.isClose() == True):
            self.show()

    def StartAlgorithm(self):
        self.hide()
        self.AtView.DoDocument()
        self.AtView._isClose = False
        self.AtView.exec_()
        if(self.AtView.isClose() == True):
            self.show()

def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
