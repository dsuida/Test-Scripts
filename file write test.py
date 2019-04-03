import pickle
import json

stuff = ['test1', 'test2']
stuff_dict = {'name': 'Doug', 'age:': 49}

# write items in list one at a time
with open('write_test.txt', 'w') as text:
    for item in stuff:
        text.write(f'{item}\n')
        # text.write(f'{item}, ')

# write txt file as a list.  i.e.  ['test1', 'test2']
with open('write_test_2.txt', 'w') as text:
    text.writelines(f'{stuff}\n')

# use pickle to write list as binary file (not human readable)
with open('pickle test.data', 'wb') as dill:
    pickle.dump(stuff, dill)

# use pickle to read above created file back into a new list.
# note that 'new_stuff' did not need to be declared as a list object
with open('pickle test.data', 'rb') as dilly:
    new_stuff = pickle.load(dilly)

print(f'Pickle data: {new_stuff}')
print(f'Pickle type: {type(new_stuff)}')

# as json file
with open('test.json', 'w') as text:
    json.dump(stuff_dict, text)

# read back in json data
with open('test.json') as text:
    new_stuff_dict = json.load(text)

print(f'json read: {new_stuff}')
print(new_stuff_dict)
