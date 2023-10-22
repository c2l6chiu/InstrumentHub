from Application import AppServer

app = AppServer()
dog = app.addInstrument('dog')


commend = ["bark()","bark()","sleep()","bark()","wakeup()","bark()"]


for c in commend:
    print(dog.query(c))