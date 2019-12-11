from PyQt5 import QtWidgets, Qt, QtCore
import UI.UI_Users, UI.UI_addDebt
import Controllers.ControllerUser

user_controller = Controllers.ControllerUser.User_Controller

class FirstPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QtWidgets.QGridLayout(self)
        self.user_section = UI.UI_Users.Wrapper_Users(self)
        self.debt_section = UI.UI_addDebt.Wrapper_AddDebt(self)
        self.layout.addWidget(self.debt_section,0,0)
        self.layout.addWidget(self.user_section,0,1)
        self.setStyleSheet('border-width: 2px; border-style: solid; border-color: pink;')

