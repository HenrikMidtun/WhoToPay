from PyQt5 import QtWidgets, Qt, QtCore
import Controllers.ControllerUser
import Controllers.ControllerDebt

user_controller = Controllers.ControllerUser.User_Controller
debt_controller = Controllers.ControllerDebt.Debt_Controller

class Wrapper_AddDebt(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.layout = QtWidgets.QGridLayout(self)
        self.field1_label = QtWidgets.QLabel('User 1',self)
        self.field2_label = QtWidgets.QLabel('User 2',self)
        self.field1_edit = DropDown_Users(self)
        self.field2_edit = DropDown_Users(self)
        self.direction_button = ButtonWidget_Direction(self)
        self.add_button = ButtonWidget_AddDebt(self.field1_edit,self.field2_edit,self)
        self.direction_button.addListener(self.add_button)
        self.layout.addWidget(self.field1_label,0,0)
        self.layout.addWidget(self.field1_edit,1,0)
        self.layout.addWidget(self.field2_label,0,2)
        self.layout.addWidget(self.field2_edit,1,2)
        self.layout.addWidget(self.direction_button,1,1)
        self.layout.addWidget(self.add_button,2,1)

#TODO Now storing user objects, rewrite to store pointers to objects/id's
class DropDown_Users(QtWidgets.QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        user_controller.addListener(self)
    
    def update(self):
        self.clear()
        users = user_controller.getUsers()
        for k,user in enumerate(users):
            self.addItem(user['name'],user['id'])
        
class ButtonWidget_Direction(QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText('>')
        self.pointingRight = True
        self.clicked.connect(lambda: self._ChangeDirection())
        self.listeners = []

    #To be used in conjunction with objects carrying 'setDirection(bool)'
    def addListener(self, listener: QtWidgets.QWidget):
        self.listeners.append(listener)
    
    def _ChangeDirection(self):
        if self.pointingRight:
            self.setText('<')
            self.pointingRight = False
        else:
            self.setText('>')
            self.pointingRight = True
        self._NotifyListeners()

    def _NotifyListeners(self):
        print('Notifying listeners')
        for listener in self.listeners:
            listener.setDirection(self.pointingRight)

class ButtonWidget_AddDebt(QtWidgets.QPushButton):
    def __init__(self, dd1: QtWidgets.QComboBox, dd2: 'DropDown_Users', parent = None):
        super().__init__(parent)
        self.setText('Add Debt')
        self.dd1 = dd1
        self.dd2 = dd2
        self.direction = None
        self.clicked.connect(lambda: self._addDebt())

    def setDirection(self, direction: bool):
        self.direction = direction
        print(direction)

    def _addDebt(self):
        print(self.dd1.currentData())
        if self.direction:
            debt_controller.addDebt(self.dd1.currentData(),self.dd2.currentData(),20)
        else:
            debt_controller.addDebt(self.dd2.currentData(),self.dd1.currentData(),20)
        

