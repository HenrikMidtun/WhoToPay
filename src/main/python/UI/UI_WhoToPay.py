from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets, Qt, QtCore
from UI.Page1 import FirstPage
import sys

class UI_MainWindow(object):
    def setupUI(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.resize(514,514)

class UI_StackedWidget(object):
    def setupUI(self, StackedWidget: QtWidgets.QStackedWidget):
        StackedWidget.setStyleSheet('border-width: 2px; border-style: solid; border-color: black;')

class ControllerMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = UI_MainWindow()
        self.ui.setupUI(self)
        cw = ControllerStackedWidget(self)
        self.setCentralWidget(cw)

class ControllerStackedWidget(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = UI_StackedWidget()
        self.ui.setupUI(self)
        #self.layout = QtWidgets.QVBoxLayout(self)
        self.page1  = FirstPage(self)
        self.addWidget(self.page1)
        

