import random

random_list = random.sample(range(500), 50)
random_list.sort()

n = len(random_list)

if n % 2 == 0:
    mediana = (random_list[n // 2] + random_list[n // 2 - 1]) / 2
else:
    mediana = random_list[n // 2]

media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(('Media: {}, Mediana: {}, Mínimo: {}, Máximo: {}').format(
    media, mediana, valor_minimo, valor_maximo))
