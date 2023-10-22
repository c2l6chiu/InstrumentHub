from multiprocessing.connection import Client


class teset():
    address = '127.0.0.1'
    port = 5002

    
    def __init__(self) -> None:
        pass
    def foo(self):
        self.port_app_inst= Client((self.address,self.port), authkey=b'vf@pnml1234')

        command1 = 'do,status_update'
        command2 = "do,bark"
        command3 = "do,sleep"
        command4 = "do,wakeup"


        self.port_app_inst.send(command2)
        tmp = self.port_app_inst.recv()
        # port_app_inst.send('stop')
        print(tmp)
        
    def __del__(self):
        self.port_app_inst.send('stop')


        
if __name__ == '__main__':
    a = teset()
    a.foo()


