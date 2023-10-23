from ApplicationKernel import AppServer
app = AppServer("app_interact_with_dog")
dog = app.addInstrument('inst_dog')


commend = ["bark()","bark()","sleep()","bark()","wakeup()","bark()"]

while True:
    for c in commend:
        print(dog.query(c))