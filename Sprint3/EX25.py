class Aviao():
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'Azul'
        self.capacidade = capacidade


boeing = Aviao('BOIENG456', 1500, 400)
embraer = Aviao('Embraer Praetor 600', 863, 14)
antonov = Aviao('Antonov An-2', 258, 12)

avioes = [boeing, embraer, antonov]

for i in range(len(avioes)):
    print(f'O avião de modelo {avioes[i].modelo} possui uma velocidade máxima de {avioes[i].velocidade_maxima}, capacidade para {avioes[i].capacidade} passageiros e é da cor {avioes[i].cor}.')
