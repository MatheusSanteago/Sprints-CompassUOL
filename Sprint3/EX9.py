primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, pessoa in enumerate(primeirosNomes):
    print(('{} - {} {} está com {} anos').format(i,
          pessoa, sobreNomes[i], idades[i]))
