from PyQt5 import QtWidgets, Qt, QtCore
import Controllers.ControllerUser

user_controller = Controllers.ControllerUser.User_Controller

#Put ListWidget_Users and ButtonWidget_AddUser here
class Wrapper_Users(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.user_label = QtWidgets.QLabel('Users',self)
        self.user_list = ListWidget_Users(self)
        self.add_button = ButtonWidget_AddUser(self)
        self.layout.addWidget(self.user_label)
        self.layout.addWidget(self.user_list)
        self.layout.addWidget(self.add_button)

class ListWidget_Users(QtWidgets.QListWidget):
    users = {}
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        user_controller.addListener(self)
        self.clicked.connect(lambda: self._OpenPopup())
    
    #Should show user specific info
    def _OpenPopup(self):
        print('Opening User Information Popup!')
        self.popup = Popup_InformationUser()
        self.popup.setGeometry(QtCore.QRect(100,100,400,200))
        self.popup.show()
    
    #Add function that retrieves userinfo on update/event/regularly
    def update(self):
        users = user_controller.getUsers()
        self.clear()
        for k,user in enumerate(users):
            self.users[k] = user
            self.insertItem(k,user['name'])

#Maybe better to use a stacked widget for editing/updating user information
class Popup_InformationUser(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.name_label = QtWidgets.QLabel('Name', self)
        self.layout.addWidget(self.name_label)

class Popup_NewUser(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.name_label = QtWidgets.QLabel('Name', self)
        self.name_edit = QtWidgets.QLineEdit(self)
        self.phone_label = QtWidgets.QLabel('Phone Number', self)
        self.phone_edit = QtWidgets.QLineEdit(self)
        self.account_label = QtWidgets.QLabel('Account Number', self)
        self.account_edit = QtWidgets.QLineEdit(self)
        self.submit_button = QtWidgets.QPushButton('Submit', self)
        self.submit_button.clicked.connect(lambda: self._addUser())
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(self.phone_label)
        self.layout.addWidget(self.phone_edit)
        self.layout.addWidget(self.account_label)
        self.layout.addWidget(self.account_edit)
        self.layout.addWidget(self.submit_button)

    #TODO empty fields, user_names taken, illegal values
    def _addUser(self):
        dic = {'name': self.name_edit.text(), 'phone': self.phone_edit.text(), 'account': self.account_edit.text()}
        user_controller.addUser(dic['name'],dic['phone'],dic['account'])
        
class ButtonWidget_AddUser(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setText('Add New User')
        self.clicked.connect(lambda: self._OpenPopup())

    def _OpenPopup(self):
        print('Opening popup!')
        self.popup = Popup_NewUser()
        self.popup.setGeometry(QtCore.QRect(100,100,400,200))
        self.popup.show()
