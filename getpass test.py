# Getpass works fine in command shell, but not in Pycharm.
#

import getpass
newPass = getpass.win_getpass("Password")
print(f'Your password is {newPass}.')

print('Hello there.  This is a '
      'very, very long line that \n'
      'I don\'t know when to stop.')
