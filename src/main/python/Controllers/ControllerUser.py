import User
from utils.HomebrewUtils import Singleton

class _ControllerUser(metaclass=Singleton):

    def __init__(self):
        super().__init__()
        self.listeners = []
        self.users = {}

    def addUser(self, name: str, phone_nr: str = None, acc_nr: str = None):
        user = User.User(name, phone_nr, acc_nr)
        self.users[id(user)] = user
        self._notifyListeners()
        return id(user)
    
    def delUser(self, id):
        self.users.pop(id)
        self._notifyListeners()
    
    def getUserInformation(self, id) -> {}:
        user = self.users[id]
        return {'id': id, 'name': user.name, 'phone_nr': user.phone_nr, 'account_nr': user.acc_nr}

    def updateName(self, id, name:str):
        self.users[id].name = name
        self._notifyListeners()
    
    def updatePhoneNumber(self, id, phone_nr:str):
        self.users[id].phone_nr = phone_nr
        self._notifyListeners()
    
    def updateAccountNumber(self, id, acc_nr:str):
        self.users[id].acc_nr = acc_nr
        self._notifyListeners()

    def getUsers(self):
        r_list = []
        for id in self.users:
            r_list.append(self.getUserInformation(id))
        return r_list
    
    def printUsers(self):
        users = self.getUsers()
        r_str = ''
        for user in users:
            r_str += (str(user) + '\n')
        print(r_str)

    def addListener(self, listener):
        self.listeners.append(listener)

    def _notifyListeners(self):
        for listener in self.listeners:
            listener.update()
#Exported instance
User_Controller = _ControllerUser()


