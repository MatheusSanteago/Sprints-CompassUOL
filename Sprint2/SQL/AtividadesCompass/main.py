# GERAR ARQUIVOS SQL

name = 'EX'
extension = '.sql'
qtd = 18

for i in range(1, qtd + 1):
    f = open(name + str(i) + extension, 'x')
