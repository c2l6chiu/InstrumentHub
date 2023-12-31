import os
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
pre_instrument_list = ['inst_itc']
# pre_instrument_list = ['inst_dog',"inst_itc","inst_nanonis","inst_nanonisUDP" ]
# pre_instrument_list = ["inst_nanonis","inst_itc"]

for name in pre_instrument_list:
    boot = BootInstrument(sys,name)
    boot.boot()
    del boot
    # sys.queue_InstServer[name] = Queue()
    # sys.port_InstServer[name] = sys.port_InstServer_available.pop()
    # #laucn new interpreter
    # launch = BootInstrument(sys,name)
    # status = launch.boot()
    # if status == "failed":
    #     del sys.queue_InstServer[name]
    #     sys.port_InstServer_available.append(sys.port_InstServer[name])
    #     del sys.port_InstServer[name]
    # else:
    #     instServer = InstrumentServer(sys,name)
    #     sys.Inst_status[name] = True
    #     #create/store thread
    #     t_instServer = Thread(target=instServer.server,args=())
    #     sys.InstServer_thread_pool[name] = t_instServer
    #     t_instServer.start()


while sys.status:
    request = jobs.get()
    if request == "": continue

    peices = request.split(' ')
    commend = peices[0].lower()
    if len(peices) > 1: arg = peices[1:]


    if commend in ['application?' , "app?"]:
        print(sys.port_inst_app)

    elif commend in ['application' , "app"]:
        print('start app_'+arg[0]+'.py')
        subprocess.Popen("conda run --no-capture-output -n "+sys.env+" python app_"+arg[0]+".py", shell=True, cwd=os.getcwd()+"/app")


    elif commend in ['instrument?' , "inst?"]:
        print(sys.port_InstServer)
        print(sys.Inst_status)

    elif commend in ['instrument' , "inst"]:
        boot = BootInstrument(sys,arg[0])
        boot.boot()
        del boot

    elif commend in ['connection?' , "connection" , "conn" , "conn?"]:
        print(sys.port_inst_app)

    elif commend in ["add","boot","start","launch","connect"]:
        boot = BootInstrument(sys,arg[0])
        boot.boot()
        del boot

    elif commend in ["remove"]:
        sys.kill_InstServ_and_Inst(arg[0])

    elif commend in ["restart","reboot","rrr"]:
        #remove
        inst_to_kill = list(sys.port_InstServer.keys())
        for i in inst_to_kill[:]:
            sys.kill_InstServ_and_Inst(i)
        # restart
        time.sleep(1)
        for name in pre_instrument_list:
            boot = BootInstrument(sys,name)
            boot.boot()
            del boot        

    elif commend in ['exit',"quit","stop","exit()" ]:
        sys.status = False  #this will shut down AppServer, shell
        inst = []
        for ser in sys.InstServer_thread_pool:
            inst.append(ser)
        for ser in inst:
            sys.kill_InstServ_and_Inst(ser)

    else:
        print("commend not found")