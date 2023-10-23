from threading import Thread
from multiprocessing.connection import Listener
from queue import Queue
import subprocess
from Kernel import System,Shell,AppServer,InstrumentMom,InstrumentServer,BootInstrument

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
pre_instrument_list = ['inst_dog',"inst_itc"]

for name in pre_instrument_list:
    sys.queue_InstServer[name] = Queue()
    sys.port_InstServer[name] = sys.port_InstServer_available.pop()
    #laucn new interpreter
    launch = BootInstrument(sys,name)
    launch.boot()
    instServer = InstrumentServer(sys,name)
    sys.Inst_status[name] = True
    #create/store thread
    t_instServer = Thread(target=instServer.server,args=())
    sys.InstServer_thread_pool[name] = t_instServer
    t_instServer.start()


while True:
    request = jobs.get()
    # print(request)

    peices = request.split(' ')

    if peices[0] == 'port':
        print(sys.port_inst_app)
    if peices[0] == 'instrument?':
        print(sys.port_InstServer)
    elif peices[0] == 'instrument':
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
