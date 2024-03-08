import serial
import time

class Inst():
    def __init__(self):
        self.ser = serial.Serial()
        # self.ser.baudrate = 9600
        self.ser.port = 'COM4'
        self.ser.timeout = 0.4
        self.ser.open()

        self.ser2 = serial.Serial()
        self.ser2.port = 'COM6'
        self.ser2.timeout = 0.4
        self.ser2.open()


        # input = 'R7\r'
        # self.ser.write(input.encode())
        # time.sleep(0.1)
        # result =str(self.ser.read(6),'utf-8')
        # self.ser.reset_input_buffer()
        # self.NV = float(result.replace('R+','').replace('\r', ''))

    def __del__(self):
        try:
            self.local()
        except:
            pass
        self.ser.close()

    # def close(self):
    #     self.ser.close
        # self.local()

    def get_1K(self):
        return self.get_t(self.ser,1)

    def get_SHD_TOP(self):
        return self.get_t(self.ser2,1)

    def get_MAG_TOP(self):
        return self.get_t(self.ser2,2)

    def get_MAG_BOT(self):
        return self.get_t(self.ser2,3)

    def get_t(self,ser,n):
        input = 'R'+str(n)+'\r'

        ser.write(input.encode())
        time.sleep(0.1)
        result =str(ser.read(6),'utf-8')
        ser.reset_input_buffer()

        if len(result) == 0:
            return 0

        if "?" in result: return self.get_t(ser,n)
        if 'R' not in result: return self.get_t(ser,n)
        
        temperature = float(result.replace('R','').replace('\r', ''))

        if temperature < 1 or temperature > 401:  return self.get_t(ser,n)
        else: return temperature
    
    def must_get_t(self,ser,n):
        input = 'R'+str(n)+'\r'
        ser.write(input.encode())
        time.sleep(0.1)
        result =str(ser.read(6),'utf-8')
        ser.reset_input_buffer()

        if len(result) == 0:
            return 0

        temperature = float(result.replace('R','').replace('\r', ''))

        return temperature

    def get_NV(self):
        # input = 'R7\r'
        # self.ser.write(input.encode())
        # time.sleep(0.1)
        # result =str(self.ser.read(6),'utf-8')
        # self.ser.reset_input_buffer()
        # NV = float(result.replace('R+','').replace('\r', ''))
        return self.NV
        # return NV
    
    def set_NV(self, amount):
        if float(amount) > 50:
            raise Exception('open needle valve too much')
        input = 'G0{:3.1f}\r'.format(float(amount))

        self.remote()
        self.ser.reset_input_buffer()
        self.ser.write(input.encode())
        self.local()
        time.sleep(0.1)
        self.remote()
        self.ser.reset_input_buffer()
        self.ser.write(input.encode())
        self.local()
        self.remote()
        self.ser.reset_input_buffer()
        self.ser.write(input.encode())
        self.local()

        self.NV = amount

    def remote(self):
        self.ser.write(b'C3\r')
        time.sleep(0.1)
        self.ser.reset_input_buffer()

    def local(self):
        self.ser.write(b'C0\r')
        time.sleep(0.1)
        self.ser.reset_input_buffer()

# 0 : Local and locked
# 1 : Remote and locked
# 2 : Local and unlocked
# 3 : Remote and unlocked

