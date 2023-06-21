animais = ['Cachorro', 'Gato', 'Leão', 'Elefante', 'Tigre', 'Girafa', 'Urso',
           'Zebra', 'Hipopótamo', 'Rinoceronte', 'Cobra', 'Aranha',
           'Avestruz', 'Pinguim', 'Golfinho', 'Tubarão', 'Peixe', 'Jacaré',
           'Tartaruga', 'Coruja']

animais.sort(reverse=False)

an = [print(animal) for animal in animais]

f = open('animais.csv', 'x')

f.write("tipo,\n")
writeAnimal = [f.write(f'{animal},\n') for animal in animais]
