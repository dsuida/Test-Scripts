#! Python3

''' This program is to test netmiko by connecting to a Cisco switch, pulling in the results of the show interfaces
status command and then parse out the connected interfaces and place them in a list.'''

import sys
import os
import re
from netmiko import ConnectHandler

# establish conection to device
net_conn = ConnectHandler(device_type='cisco_ios', ip='172.20.96.3', username='dsuida', password='Peanut1234')

# enter enable mode
net_conn.enable()

# add the output of the show command to the string 'results'
results = net_conn.find_prompt() + '\n'
results += net_conn.send_command('show int status', delay_factor=2)
net_conn.disconnect()

#split the resulting string into a list based on new line
results = results.split('\n')

del results[0:3]

interfaces = []

# loop thru the results list and parse out the connected interfaces and add them to the interfaces list
for i in range(0, len(results)):
    if 'connected' in results[i] and 'Po' not in results[i] :
        interfaces.append(re.match('^\w*\d/\d/\d*',results[i]))

print('There are '+ str(len(interfaces)) + ' interfaces up.  They are:')
for i in range(0, len(interfaces)):
    print(interfaces[i].group())

print()






