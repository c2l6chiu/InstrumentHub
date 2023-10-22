from multiprocessing.connection import Listener,Client


address_AppServer = '127.0.0.1'
port_AppServer = 5723
authkey_AppServer = b'vf@pnml1234'
authkey_serviceLine = b'vf@pnml9876'



port_AppServer = Listener((address_AppServer,port_AppServer) , authkey= authkey_AppServer)

client = port_AppServer.accept()
while True:
    try:
        msg = client.recv()
        print(msg)

        #pretend kernal sending port number to instrument
        address_InstCoor = '127.0.0.1'
        port_InstCoor = 7788
        authkey_InstCoor = b'vf@pnml4321'

        port_kern_inst =  Client((address_InstCoor,port_InstCoor),
                                        authkey=authkey_InstCoor)

        port_kern_inst.send('open-7890')
        port_kern_inst.recv()
        port_kern_inst.close()

        #telling application that there is a port ready to use
        client.send(( (address_AppServer,7890), authkey_serviceLine))

        

    except EOFError:
        client = port_AppServer.accept()
