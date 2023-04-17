class Passaro():
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som

    def emitirSom(self):
        print(f'{self.especie} emitindo som...')
        print(self.som)

    def voar(self):
        print(self.especie)
        print('Voando...')


class Pardal(Passaro):
    def __init__(self, especie='Pardal', som='Piu Piu'):
        super().__init__(especie, som)


class Pato(Passaro):
    def __init__(self, especie='Pato', som='Quack Quack'):
        super().__init__(especie, som)


pato = Pato()
pardal = Pardal()

pato.voar()
pato.emitirSom()
pardal.voar()
pardal.emitirSom()
