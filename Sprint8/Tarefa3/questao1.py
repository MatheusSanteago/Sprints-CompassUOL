import random

num = []

for i in range(1, 251):
    num.append(random.randint(0, 250))

numverse = reversed(num)
for i in numverse:
    print(i)
