#! Python3

'''Testing config changes on hard coded test switch.  Simply finds any
interfaces selected vlan and puts them in new vlan'''

import datetime
import os
from netmiko import ConnectHandler

fromVlan = input('From VLAN: ')
toVlan = input('To VLAN: ')

# establish connection to device
netConn = ConnectHandler(device_type='cisco_ios', ip='cpr-dga-temp', username='dsuida', password='Peanut1234')

print('\nConnection established')
print('\nGathering data...\n')

# enter enable mode
netConn.enable()

# add the output of the show command to the string 'output'
output = netConn.find_prompt() + '\n'
output += netConn.send_command('show int status', delay_factor=2)

# split the resulting string into a list based on new line
output = output.split('\n')

# initialize lists
configCommands = []
interfaces = []

# Find interfaces in fromVlan and add to interfaces list
for i in range(3, len(output)):  # 1st few lines in output are switch name and column header
  output[i] = output[i].split()
  if output[i][-4] == fromVlan:
      interfaces.append(output[i][0])

if len(interfaces) > 0:
    logFile = open('Vlan Update.log', 'a')
    logFile.write ( datetime.datetime.now ( ).strftime ( '%m/%d/%Y  %H:%M:%S' ) + '\n')
    logFile.write('VLAN Change logfile for switch: ' + output[0][:len(output[0])-1] + '.\n')
    for i in range(len(interfaces)):
        print('Updating interface ' + interfaces[i] + '.')
        configCommands = ['int ' + interfaces[i], 'switchport access vlan ' + toVlan]
        logFile.write('Changed ' + interfaces[i] + ' from VLAN ' + fromVlan + ' to VLAN ' + toVlan + '.\n')
        command = netConn.send_config_set(configCommands)

    print('\nDone.  Saving changes.')
    print('\nThere are no interfaces in the selected VLAN.')

print()

# Disconnect from switch
netConn.disconnect()
    command = netConn.send_command('copy run start \r')
    logFile.write('\n\n')
    logFile.close()

else: