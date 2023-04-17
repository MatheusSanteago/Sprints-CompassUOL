class Aviao():
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'Azul'
        self.capacidade = capacidade
        print(
            f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima},apacidade para {self.capacidade} passageiros e é da cor {self.cor}.')


Aviao('BOIENG456', 1500, 400)
Aviao('Embraer Praetor 600', 863, 14)
Aviao('Antonov An-2', 258, 12)
