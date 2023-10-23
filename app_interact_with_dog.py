from Application import AppServer
app = AppServer("app_interact_with_dog")
dog = app.addInstrument('inst_dog')


commend = ["bark()","bark()","sleep()","bark()","wakeup()","bark()"]


for c in commend:
    print(dog.query(c))