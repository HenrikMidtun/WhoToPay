import sys
import os

sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from UI.UI_WhoToPay import ControllerMainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()
    MainWindow = ControllerMainWindow()
    MainWindow.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
