from ApplicationKernel import AppServer

app = AppServer("app_figure_trackZ")
nanonis = app.addInstrument('inst_nanonis')
print(nanonis.query("read_channel('0,22')"))
