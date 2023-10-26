Finish read current / Walker / Move

Finish Scan/Grid/LockIn

Finish Ardrino /  RS232 / Keithley

Merge two Labview file



Application crash:
    did the destructor being called correctely?
    if the communication stuck, how to close the connection?


in application.AppServer.askPort
    handle timeout

in application.Coordinator.ask:
    clear buffer



Instrumentation:
    need to deal with the proper way to shut down
    =>tell the Kernel that instrument is gone before dying


In kernel AppServer.checkInstrument
    check if instrument is still alive by handshaking


In Kernel deal with bad application connection
    1. attemp to connect to same instrument twice
    2. application disappear
    3. application froze