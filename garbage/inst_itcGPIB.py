import pyvisa
import time

class Inst():
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self.itc = rm.open_resource('GPIB0::23::INSTR')
        self.itc.read_termination = '\r'
        self.itc.timeout = 20

    def __del__(self):
        self.itc.close()
        pass

    def get_t1(self):
        self.itc.write('R1')
        time.sleep(0.1)
        try: 
            result = str(self.itc.read())
        except:
            result = "0000"
        try:
            while True: self.itc.read()
        except:
            pass
        return float(result[1:])

    # def set_nv(self, amount):
    #     if amount > 50:
    #         raise Exception('open needle valve too much')
    #     string = 'G0{:3.1f}'.format(float(amount))
    #     self.itc.write(string)
    #     time.sleep(0.1)
    #     try:
    #         while True: result = self.itc.read()
    #     except:
    #         pass
    #     return True

    # def remote(self):
    #     self.itc.write(b'C3\r')
    #     self.itc.read()
    # def local(self):
    #     self.itc.write(b'C0\r')
    #     self.itc.read()

# 0 : Local and locked
# 1 : Remote and locked
# 2 : Local and unlocked
# 3 : Remote and unlocked

