class Calculo():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def somar(self):
        print(f'Somando: {self.x} + {self.y} = {self.x + self.y}')

    def subtrair(self):
        print(f'Subtraindo: {self.x} - {self.y} = {self.x - self.y}')


calc = Calculo(4, 5)
calc.somar()
calc.subtrair()
