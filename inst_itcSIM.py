import random

class Inst():
    def __init__(self):
        self.base = 1.2
        self.t = 1.2
        self.delta = 0
        self.NV = 0
        

    def change_baseT(self,newT):
        self.delta = newT

    def get_1K(self):
        return self.t+self.delta+random.gauss(0,0.02)

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
        self.t = self.base + nv*0.01
