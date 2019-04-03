# from Corry Schafer video on Regular Expressions in Python
# https://www.youtube.com/watch?v=K8L6KVGG-7o

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

results = []
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'M(rs|r|s)\.*\s[A-Za-z]+')
# pattern is caital M followed by either 'rs' or 'r' or 's' follow by optional period (escaped as the . is
# regex for "any character' and want a literal period)  followed by a space and then one or more capital
# or lower case letters

matches = pattern.finditer(text_to_search)


# matches is an iterable object and does not have indexes
# only has a 'next item' method so need to loop thru and
# append matched ranges to a list.
for item in matches:
    results.append(item.group(0))  # adds item to list
    print(f'{item.group(0)} - {item.start()}:{item.end()-1}')


print('\nThe list is:')
for i in range(0,len(results)):
    print(results[i]) # prints items in list

