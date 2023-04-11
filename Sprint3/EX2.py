numeros = []
i = 0
while i < 3:
    numeros.append(int(input('Digite um número! ')))
    i += 1

for x in range(0, len(numeros)):
    n = numeros[x] % 2 == 0
    if n:
        print(('Par: {}').format(numeros[x]))
    else:
        print(('Ímpar: {}').format(numeros[x]))
