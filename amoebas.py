from threading import Thread
from multiprocessing.connection import Listener
from queue import Queue
import subprocess
from Kernel import System,Shell,AppServer,InstrumentMom,InstrumentServer,BootInstrument
import time

jobs = Queue()

#the system that store all the inforamtion
sys = System()

#generate shell
shell = Shell(jobs,sys)
t_shell = Thread(target=shell.run,args=())
t_shell.start()

#create AppServer
app = AppServer(sys)
t_app = Thread(target=app.server,args=())
t_app.start()

#create InstrumentMom
instMom = InstrumentMom(sys)
t_instMom = Thread(target=instMom.server,args=())
t_instMom.start()

#pre-launch Instrument
# pre_instrument_list = ['inst_dog',"inst_itc"]
pre_instrument_list = ['inst_dog',"inst_itc","inst_nanonis"]
# pre_instrument_list = ["inst_nanonis"]

for name in pre_instrument_list:
    sys.queue_InstServer[name] = Queue()
    sys.port_InstServer[name] = sys.port_InstServer_available.pop()
    #laucn new interpreter
    launch = BootInstrument(sys,name)
    status = launch.boot()
    if status == "failed":
        del sys.queue_InstServer[name]
        sys.port_InstServer_available.append(sys.port_InstServer[name])
        del sys.port_InstServer[name]
    else:
        instServer = InstrumentServer(sys,name)
        sys.Inst_status[name] = True
        #create/store thread
        t_instServer = Thread(target=instServer.server,args=())
        sys.InstServer_thread_pool[name] = t_instServer
        t_instServer.start()


while sys.status:
    request = jobs.get()
    peices = request.split(' ')
    commend = peices[0].lower()
    if len(peices) > 1: arg = peices[1:]

    if commend in ['application?' , "application" , "app" , "app?"]:
        print(sys.port_inst_app)

    if commend in ['instrument?' , "instrument" , "inst" , "inst?"]:
        print(sys.port_InstServer)
        print(sys.Inst_status)

    if commend in ['connection?' , "connection" , "conn" , "conn?"]:
        print(sys.port_inst_app)

    if commend in ["boot","start","launch"]:
        pass

    if commend in ['exit',"quit","stop","exit()" ]:
        sys.status = False  #this will shut down AppServer, shell
        inst = []
        for ser in sys.InstServer_thread_pool:
            inst.append(ser)
        for ser in inst:
            sys.kill_InstServ(ser)



        #launch instrument with all the address,authkey
        #create a InstrumentCoordinator and run it
        pass

    
    # elif peices[0] == "exit":
    #     sys.status = False
    #     t_app.terminate()
    #     t_shell.terminate()
    #     t_instMom.terminate()
    #     t_instServer.terminate()
        # break
