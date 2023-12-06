# import pyvisa

# rm = pyvisa.ResourceManager()
# itc = rm.open_resource('GPIB0::24::INSTR')
# itc.read_termination = '\r'
# itc.timeout = 20
# itc.baud_rate = 96400
# print(rm.list_resources())

# print(itc.query('G025.0'))
# print(itc.query('R1'))

# print(itc.query('R1'))
# print(itc.read())
# print(itc.read())
# print(itc.read())
# print(itc.read())
# print(itc.read())
# print(itc.read())
# print(itc.read_bytes(8))

