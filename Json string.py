'''To play with JSON sting within python file'''

import json

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@whateve.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-3242",
      "emails": null,
      "has_license": true
    }
  ]
}  
'''

data = json.loads(people_string)

print('The type of "people" in data as is: ' + str(type(data['people'])))

print('\nItems in list are: ')
for person in data['people']: # can itterate thru as type of data['people'] is a list object (list of diccts)
    print(person)

print('\nPerson and phone number are:')
for person in data['people']:
    print(person['name'], person['phone'])

#delete phone number in dic
for person in data['people']:
    del person['phone']

#turn dic without phone number into a new json string formated as json object
new_data = json.dumps(data,indent=2)
print('\njson string with phone number removed is:\n')
print(new_data)