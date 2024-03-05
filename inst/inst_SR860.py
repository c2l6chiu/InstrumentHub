import pyvisa

class Inst():
    def __init__(self):
        self.sen_dic = ['1V','500mV','200mV',"100mV",'50mV','20mV',"10mV",'5mV','2mV',"1mV",\
                   '500uV','200uV',"100uV",'50uV','20uV',"10uV",'5uV','2uV',"1uV",\
                    '500nV','200nV',"100nV",'50nV','20nV',"10nV",'5nV','2nV']
        self.tconst_dic = ['1us','3us','10us','30us','100us','300us','1ms','3ms','10ms',\
                      '30ms','100ms','300ms','1s','3s','10s','30s','100s','300s',\
                        '1000s','3000s']
        
        rm = pyvisa.ResourceManager()
        rm.list_resources()
        
        self.inst = rm.open_resource('TCPIP0::10.0.0.4::inst0::INSTR')

    def sens(self,level):
        sen = self.sen_dic.index(level) if level in self.sen_dic else 0
        self.inst.write('SCAL '+str(sen))
        return

    def sens_q(self):
        result = int(self.inst.query('SCAL?'))
        if result in [id for id in range(len(self.sen_dic))]:
            return self.sen_dic[result]
        else:
            return self.sen_dic[0]
    
    def osc(self,oscillation):
        self.inst.write('SLVL '+str(oscillation))
        return
        
    def osc_q(self):
        result = self.inst.query('SLVL?')
        return result
    
    def freq(self,oscillation):
        self.inst.write('FREQ '+str(oscillation))
        return
        
    def freq_q(self):
        result = self.inst.query('FREQ?')
        return result

    def tconst(self,level):

        sen = self.tconst_dic.index(level) if level in self.tconst_dic else 7
        self.inst.write('OFLT '+str(sen))
        return

    def tconst_q(self):
        result = int(self.inst.query('OFLT?'))
        if result in [id for id in range(len(self.tconst_dic))]:
            return self.tconst_dic[result]
        else:
            return self.tconst_dic[7]
        
    def phi(self,phase):
        self.inst.write('PHAS '+str(phase))
        return
        
    def phi_q(self):
        result = self.inst.query('PHAS?')
        return result
    
    def harm(self,harmonics):
        self.inst.write('HARM '+str(harmonics))
        return
        
    def harm_q(self):
        result = self.inst.query('HARM?')
        return result

    def autoPhase(self):
        self.inst.write('APHS')
        return

# print(SR.query("sens('50mV')"))
# print(SR.query("sens_q()"))
# print(SR.query("osc('0.001')"))
# print(SR.query("osc_q()"))
# print(SR.query("freq('4001')"))
# print(SR.query("fre_q()"))
# print(SR.query("tconst('3ms')"))
# print(SR.query("tconst_q()"))
# print(SR.query("phi(28.256095983)"))
# print(SR.query("phi_q()"))
# print(SR.query("harm('1')"))
# print(SR.query("harm_q()"))