'''
Testing netconf with csr100v set up in GNS3 topology "netconf"
CSR connects to vmnet1 so it can be reached by script.
Note that output is filtered to a single interface.
'''


from ncclient import manager
import xmltodict
from xml.dom import minidom
import sys

interface_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>{int_name}</name>
    </interface>
  </interfaces>
</filter>
"""

# open netconf connection to devise
try:
    with manager.connect(host='192.168.31.139',
                         username = 'admin',
                         password = 'password',
                         hostkey_verify = False) as m:

        # create netconf  filter and get config
        filter = interface_filter.format(int_name = 'GigabitEthernet1')
        r = m.get_config('running', filter)
except:
    print('\nCannot connect to device.  Is GNS3 topology running?')
    sys.exit()


# pretty print raw xml to screen
xml_doc = minidom.parseString(r.xml)
print(xml_doc.toprettyxml(indent='  '))

# process xml into python dict
interface = xmltodict.parse(r.xml)

# Only if RPC returned data
if not interface["rpc-reply"]["data"] is None:
    interface = interface["rpc-reply"]["data"]["interfaces"]["interface"]

    print("The interface {name} has ip address {ip}/{mask} with desc of '{desc}'".format(
            name = interface["name"]["#text"],
            ip = interface["ipv4"]["address"]["ip"],
            mask = interface["ipv4"]["address"]["netmask"],
            desc = interface['description']
            )
        )
else:
    print("No interface {} found".format("GigabitEthernet2"))


