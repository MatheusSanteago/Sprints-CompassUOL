file = 'number.txt'
numList = []

with open(file) as numbers:
    try:
        for num in numbers:
            numList.append(num.rstrip('\n'))
    finally:
        numList = list(map(int, numList))


maioresPares = list(filter(lambda n: n % 2 == 0, numList))
cincoMaiores = sorted((maioresPares), reverse=True)[:5]

print(cincoMaiores)
print(sum(cincoMaiores))
