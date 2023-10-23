import serial
import time

class Inst():
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = 'COM4'
        self.ser.timeout = 0.02
        self.ser.open()
        self.remote()

    def __del__(self):
        self.close()

    def close(self):
        self.ser.close
        self.local()

    def get_t1(self):
        self.remote()
        self.ser.write(b'R1\r')
        result =str(self.ser.read(100),'utf-8')
        try:
            temperature = float(result.replace('R','').replace('\r', ''))
            
        except:
            temperature =  0

        return temperature

    def set_nv(self, amount):
        if amount > 50:
            raise Exception('open needle valve too much')
        string = 'G0{:3.1f}\r'.format(float(amount))
        self.remote()
        self.ser.write(bytes(string,'utf-8'))
        self.ser.read(100)

    

    def remote(self):
        self.ser.write(b'C3\r')
        self.ser.read(2)
    def local(self):
        self.ser.write(b'C0\r')
        self.ser.read(2)

# 0 : Local and locked
# 1 : Remote and locked
# 2 : Local and unlocked
# 3 : Remote and unlocked

