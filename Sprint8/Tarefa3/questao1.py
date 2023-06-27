import random

num = []

for i in range(1, 251):
    num.append(random.randint(0, 250))

numverse = reversed(num)
for i in numverse:
    print(i)

# Outra variação

lista = [random.randint(1, 250) for _ in range(250)]
invertida = lista[::-1]
print(len(invertida))
