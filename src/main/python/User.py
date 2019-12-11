
class User():
    def __init__(self, name: str, phone_nr: str = None, acc_nr: str = None):
        super().__init__()
        self.name = name
        self.phone_nr = phone_nr
        self.acc_nr = acc_nr

    def getID(self):
        return id(self)

    def __str__(self):
        r_str = 'ID: {}\nName: {}\nPhone Number: {}\nAccount Number: {}\n'.format(self.getID(),self.name,self.phone_nr,self.acc_nr)
        return r_str
    