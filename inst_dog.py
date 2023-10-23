class Inst():
    def __init__(self):
        self.status= True
        self.label = "instrument dog"

    def bark(self):
        if self.status:
            # print('bark')
            return "bark"
        else:
            # print('zzz')
            return "zzz"
    
    def sleep(self):
        if self.status:
            self.status = False
            return True
        else:
            return False
    def wakeup(self):
        if not self.status:
            self.status = True
            return True
        else:
            return False


