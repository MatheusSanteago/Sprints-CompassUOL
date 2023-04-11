palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for j in range(len(palavras)):
    palavra = palavras[j]
    palavraReversa = ''
    for i in range(len(palavra) - 1, -1, -1):
        palavraReversa += palavra[i]
        if i == 0:
            if palavras[j] == palavraReversa:
                print(('A palavra: {} é um palíndromo').format(palavras[j]))
            else:
                print(('A palavra: {} não é um palíndromo').format(
                    palavras[j]))
