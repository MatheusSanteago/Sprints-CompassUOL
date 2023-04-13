palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in range(len(palavras)):
    if i == 0:
        if palavras[i] == palavras[::-1]:
            print(('A palavra: {} é um palíndromo').format(palavras[i]))
    else:
        print(('A palavra: {} não é um palíndromo').format(
            palavras[i]))
