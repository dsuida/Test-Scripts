#! Python3


import re
from netmiko import ConnectHandler

devname = input('Devices name or IP: ')
vlan = input('Vlan ID: ')

print('Connecting to device...')

# establish connection to device
userName = os.environ.get('TACACS_USER')  # creds stored as environ variables
password = os.environ.get('TACACS_PASS')  # creds stored as environ variables


netConn = ConnectHandler(device_type='cisco_ios', ip=devname, username=userName, password=pasword)

# enter enable mode
netConn.enable()

# add the output of the show command to the string 'results'
results = netConn.find_prompt() + '\n'
results += netConn.send_command('show arp', delay_factor=2)
netConn.disconnect()

# split the resulting string into a list based on new line
results = results.split('\n')

# initialize dictionary
interfaces = {}

for i in range(2, len(results)):  # 1st few lines in results are switch name and column header
    results[i] = results[i].split()

print('Done')
