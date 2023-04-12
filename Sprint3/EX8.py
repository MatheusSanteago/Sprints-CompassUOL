palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for j in range(len(palavras)):
    palavra = palavras[j]
    for i in range(len(palavra)):
        if i == 0:
            if palavras[j] == palavra[::-1]:
                print(('A palavra: {} é um palíndromo').format(palavras[j]))
            else:
                print(('A palavra: {} não é um palíndromo').format(
                    palavras[j]))
