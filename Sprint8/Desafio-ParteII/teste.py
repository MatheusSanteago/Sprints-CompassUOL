import json

f = open('js.json')

data = json.load(f)

print(data[0])