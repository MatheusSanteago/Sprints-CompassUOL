class Pessoa:
    def __init__(self, id):
        self._nome = ''
        self.id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, a):
        self._nome = a


pessoa = Pessoa(0)
pessoa.nome = "Fulano de Tal"
print(pessoa.nome)
