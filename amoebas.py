import os
from threading import Thread
from multiprocessing.connection import Listener
from queue import Queue
import subprocess
from Kernel import System,Shell,AppServer,InstrumentMom,InstrumentServer,BootInstrument
import time


pre_instrument_list = [('inst_dog' , False),\
                        ('inst_itc' , True),\
                        ('inst_nanonis' , False),\
                        ('inst_arduino' , False),\
                        ('inst_SR860' , True)]


jobs = Queue()          #for shell to pass on commend
sys = System()          #the system that store all the inforamtion

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
sys.start_inst(pre_list=pre_instrument_list , debugMode=False)  


while sys.status:
    request = jobs.get()
    if request == "": continue

    peices = request.split(' ')
    commend = peices[0].lower()
    if len(peices) > 1: arg = peices[1:]


    if commend in ['application?' , "app?"]:
        print(sys.port_inst_app)


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
        boot = BootInstrument(sys,arg[0],debugMode=True)
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
        sys.start_inst(pre_list=pre_instrument_list , debugMode=False)     

    elif commend in ["debug"]:
        #remove
        inst_to_kill = list(sys.port_InstServer.keys())
        for i in inst_to_kill[:]:
            sys.kill_InstServ_and_Inst(i)
        # restart
        time.sleep(1)
        sys.start_inst(pre_list=pre_instrument_list , debugMode=True)     

    # elif commend in ['exit',"quit","stop","exit()" ]:
    #     sys.status = False  #this will shut down AppServer, shell
    #     inst = []
    #     for ser in sys.InstServer_thread_pool:
    #         inst.append(ser)
    #     for ser in inst:
    #         sys.kill_InstServ_and_Inst(ser)

    else:
        if os.path.exists(os.getcwd()+"/app/"+commend+".py"):
            subprocess.Popen("conda run --no-capture-output -n "+sys.env+" python "+commend+".py", shell=True, cwd=os.getcwd()+"/app")
            print('starting '+commend+'.py......')
        else:
            print("commend not found")
        