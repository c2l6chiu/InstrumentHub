import telnetlib

HOST = '10.0.0.4'

tn = telnetlib.Telnet(HOST)
# tn.open()
# print(tn.read_until(b'\r\n'))
# print('cool')
# tn.write(b'OFLT 6\r\n')
# print('ok')
# tn.write(b'SLVL 0.01\r\n')

# print(int(tn.read_some()))
# print(tn.read_until(b'\r',timeout=0.1))
print(tn.read_some())

tn.close()