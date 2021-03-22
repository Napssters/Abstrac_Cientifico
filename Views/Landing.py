#! usr/bin/env python
from PyQt5 import QtWidgets, uic
from Views import Summary as Sm
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Views/QtViews/Landing_Window.ui', self)
        self.abstracts = self.findChild(QtWidgets.QPushButton, 'abstracts')
        self.abstracts.clicked.connect(self.StartSummary)
        self.SmView = Sm.SummaryView()

    def StartSummary(self):
        self.hide()
        self.SmView._isClose = False
        self.SmView.exec_()
        if(self.SmView.isClose() == True):
            self.show()


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
