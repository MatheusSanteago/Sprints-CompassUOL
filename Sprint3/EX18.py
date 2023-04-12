speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44,
         'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
new_list = []

for i, campo in enumerate(speed):
    new_list.append(speed[campo])

print(list(set(new_list)))
