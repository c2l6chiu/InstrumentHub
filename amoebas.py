from threading import Thread
from queue import Queue
from Kernel import System,Shell,AppServer,InstrumentMom,InstrumentServer

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


########## launch instrument ##########
instrument_list = ['inst_dog.py']

name = instrument_list[0]
#laucn another interpreter


sys.queue_InstServer[name] = Queue()
sys.port_InstServer[name] = sys.port_InstServer_available.pop()
#create InstrumentServer
instServer = InstrumentServer(sys,name)

#create/store thread
t_instServer = Thread(target=instServer.server,args=())
sys.InstServer_thread_pool[name] = t_instServer
t_instServer.start()


while True:
    request = jobs.get()
    print(request)

    peices = request.split(' ')

    if peices[0] == 'port':
        print(sys.port_inst_app)

    elif peices[0] == 'instrument':
        #launch instrument with all the address,authkey
        #create a InstrumentCoordinator and run it
        pass
