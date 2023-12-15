import random

class Inst():
    def __init__(self):
        self.t = 1.2
        self.NV = 0

    def change_baseT(self,newT):
        self.t = newT

    def get_1K(self):
        return self.t+random.gauss(0,0.02)

    def get_SHD_TOP(self):
        return self.t+random.gauss(0,0.02)

    def get_MAG_TOP(self):
        return self.t+random.gauss(0,0.02)

    def get_MAG_BOT(self):
        return self.t+random.gauss(0,0.02)
    
    def get_NV(self):
        return self.NV

    def set_NV(self,nv):
        self.NV = int(nv)
        self.t = 1.2+nv*0.01
