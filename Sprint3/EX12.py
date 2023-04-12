import json

file = open('person.json', 'r')
user = ''
for i in file.readlines():
    user += i.rstrip('\n')

user = json.loads(user)
print(dict(user))
