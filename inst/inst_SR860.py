import pyvisa
import telnetlib
import time

class Inst():
    def __init__(self):
        self.sen_dic = ['1V','500mV','200mV',"100mV",'50mV','20mV',"10mV",'5mV','2mV',"1mV",\
                   '500uV','200uV',"100uV",'50uV','20uV',"10uV",'5uV','2uV',"1uV",\
                    '500nV','200nV',"100nV",'50nV','20nV',"10nV",'5nV','2nV']
        self.tconst_dic = ['1us','3us','10us','30us','100us','300us','1ms','3ms','10ms',\
                      '30ms','100ms','300ms','1s','3s','10s','30s','100s','300s',\
                        '1000s','3000s']
        self.timeout=0.1
        
        self.rm = pyvisa.ResourceManager()
        # self.rm.list_resources()
        
        self.inst = self.rm.open_resource('TCPIP0::10.0.0.4::inst0::INSTR')
        # HOST = '10.0.0.4'
        # self.inst = telnetlib.Telnet(HOST)
        # self.inst.read_some()

    def __del__(self):
        # self.osc(0)
        # self.rm.close()
        pass

    def sens(self,level):
        sen = self.sen_dic.index(level) if level in self.sen_dic else 0
        # input = 'SCAL '+str(sen)+'\r'
        # self.inst.write(input.encode())
        self.write('SCAL '+str(sen))
        # time.sleep(0.01)
        return

    def sens_q(self):
        # self.inst.write(b'SCAL?\r')
        # result = int(self.inst.read_until(b'\r'))
        result = int(float(self.query('SCAL?')))
        if result in [id for id in range(len(self.sen_dic))]:
            return self.sen_dic[result]
        else:
            return self.sen_dic[0]
    
    def osc(self,oscillation):
        # input = 'SLVL '+str(oscillation)+'\r'
        # self.inst.write(input.encode())
        self.write('SLVL '+str(oscillation))
        # time.sleep(0.01)
        return
        
    def osc_q(self):
        # self.inst.write(b'SLVL?\r')
        # result = float(self.inst.read_until(b'\r'))
        result = float(self.query('SLVL?'))
        return result
    
    def freq(self,frequency):
        # input = 'FREQ '+str(frequency)+'\r'
        # self.inst.write(input.encode())
        self.write('FREQ '+str(frequency))
        # time.sleep(0.01)
        return
        
    def freq_q(self):
        # self.inst.write(b'FREQ?\r')
        # result = float(self.inst.read_until(b'\r'))
        result = float(self.query('FREQ?'))
        return result

    def tconst(self,level):
        timeConstant = self.tconst_dic.index(level) if level in self.tconst_dic else 7
        # input = 'OFLT '+str(timeConstant)+'\r'
        # self.inst.write(input.encode())
        self.write('OFLT '+str(timeConstant))
        # time.sleep(0.01)
        return

    def tconst_q(self):
        # self.inst.write(b'OFLT?\r')
        # result = int(self.inst.read_until(b'\r'))
        result = int(float(self.query('OFLT?')))
        if result in [id for id in range(len(self.tconst_dic))]:
            return self.tconst_dic[result]
        else:
            return self.tconst_dic[7]
        
    def phi(self,phase):
        # input = 'PHAS '+str(phase)+'\r'
        # self.inst.write(input.encode())
        self.write('PHAS '+str(phase))
        # time.sleep(0.01)
        return
        
    def phi_q(self):
        # self.inst.write(b'PHAS?\r')
        # result = float(self.inst.read_until(b'\r'))
        result = float(self.query('PHAS?'))
        return result
    
    def harm(self,harmonics):
        # input = 'HARM '+str(harmonics)+'\r'
        # self.inst.write(input.encode())
        self.write('HARM '+str(harmonics))
        # time.sleep(0.01)
        return
        
    def harm_q(self):
        # self.inst.write(b'HARM?\r')
        # result = int(self.inst.read_until(b'\r'))
        result = int(self.query('HARM?'))
        return result

    def autoPhase(self):
        # self.inst.write(b'APHS'+'\r')
        self.write('APHS')
        # time.sleep(0.01)
        return
    
    def query(self,msg):
        # self.inst.read_until(b'\r',timeout=0.01)
        # result = b''
        # count = 0
        # while len(result)==0:
        #     self.inst.write((msg+'\r').encode())
        #     time.sleep(0.01)
        #     result = self.inst.read_until(b'\r',timeout=self.timeout)
        #     count+=1
        #     if count>5: break
        #     time.sleep(0.02)
        # self.inst.read_until(b'\r',timeout=0.01)


        result = self.inst.query(msg)

        return result
    
    def write(self,msg):
        # self.inst.read_until(b'\r',timeout=0.01)
        # self.inst.write((msg+'\r').encode())
        # self.inst.read_until(b'\r',timeout=0.01)
        

        self.inst.write(msg)
