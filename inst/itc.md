# read temperature
print(itc.query('get_1K'))
print(itc.query('get_SHD_TOP'))
print(itc.query('get_MAG_TOP'))
print(itc.query('get_MAG_BOT'))

# set needle valve
amount should be string, between 0 and 49
itc.query('set_NV','20')
