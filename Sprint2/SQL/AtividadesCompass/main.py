# GERAR ARQUIVOS SQL

name = 'EX'
extension = '.sql'
qtd = 16

for i in range(1, qtd + 1):
    f = open(name + str(i) + extension, 'x')
