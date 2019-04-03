import re

while True:
    devIP = input ('IP address:')
    if re.match ('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', devIP ):
        break
    else:
        print ('not an ip address')