import time
from threading import Thread
from multiprocessing.connection import Listener
from Kernel import AppServer,InstrumentMom,System
from Shell import Shell


pre_instrument_list = [('inst_dog' , False),\
                        ('inst_itc' , True),\
                        ('inst_nanonis' , False),\
                        ('inst_arduino' , False),\
                        ('inst_SR860' , True)]




while True:
    try:
        sys = System(pre_instrument_list)          #the system that store all the inforamtion

        #create AppServer
        app = AppServer(sys)
        t_app = Thread(target=app.server,args=())
        t_app.start()

        #create InstrumentMom
        # instMom = InstrumentMom(sys)
        # t_instMom = Thread(target=instMom.server,args=())
        # t_instMom.start()

        #pre-launch Instrument
        sys.start_inst(pre_list=pre_instrument_list , debugMode=False)  
        shell = Shell(sys)
        shell.run()

    except:
        inst_to_kill = list(sys.port_InstServer.keys())
        for i in inst_to_kill[:]:
            sys.kill_InstServ_and_Inst(i)
        del sys
        del app
        del shell
        time.sleep(5)
        print('Restart')
