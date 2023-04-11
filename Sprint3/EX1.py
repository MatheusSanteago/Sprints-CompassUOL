import datetime

nome = input('Digite seu nome! ')
idade = int(input('Digite sua idade! '))
anos_restantes = 100 - idade
centenario = int(datetime.datetime.now().year) + anos_restantes

print(centenario)
