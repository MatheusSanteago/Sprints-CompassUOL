class Passaro():
    def __init__(self):
        pass

    def emitirSom(self):
        print(f'{self._especie} emitindo som...')
        print(self._som)

    def voar(self):
        print(self._especie)
        print('Voando...')


class Pato(Passaro):
    def __init__(self):
        self._especie = 'Pato'
        self._som = 'Quack Quack'


class Pardal(Passaro):
    def __init__(self):
        self._especie = 'Pardal'
        self._som = 'Piu Piu'


pato = Pato()
pardal = Pardal()

pato.voar()
pato.emitirSom()
pardal.voar()
pardal.emitirSom()
