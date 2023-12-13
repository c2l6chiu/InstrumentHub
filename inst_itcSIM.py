class Inst():
    def __init__(self):
        self.t = 1.2
        self.NV = 0
    def get_1K(self):
        return self.t
    
    def set_NV(self,nv):
        self.NV = nv
        self.t = 1.2+nv*0.01