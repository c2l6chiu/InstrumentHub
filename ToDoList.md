in application.AppServer
    make sure that I don't need to close the connection to allow other connection






in application.AppServer.askPort
    handle timeout

in application.Coordinator.ask:
    clear buffer

in application.Coordinator.query:
    handle time out error




Instrumentation:
    need to deal with the proper way to shut down
    =>tell the Kernel that instrument is gone before dying