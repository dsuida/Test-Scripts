'''THis is a test script to read thru a text file that
simulates the output of "sho run int g2/0/1" and pulls
out each element using RE and groups.'''

import re

with open('show run interfaces.txt', 'r') as f:
    IntConfig = f.read()

intID = re.search(r'interface (.*)', IntConfig)[1]
intDesc = re.search(r'description (.*)', IntConfig)[1]
IPinfo = re.search(r'ip address (.*) (.*)', IntConfig)
IPAdd = IPinfo[1]
subMask = IPinfo[2]

print(f'Interface ID: {intID}')
print(f'Interface Description: {intDesc}')
print(f'Interface IP Address: {IPAdd}')
print(f'Interface subnet mask: {subMask}')
