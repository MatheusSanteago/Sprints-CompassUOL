file = 'estudantes.csv'
listaAlunos = []

with open(file) as alunos:
    for aluno in alunos:
        listaAlunos.append(aluno.rstrip('\n').split(','))

listaAlunos.sort()
alunos = list(map(lambda a: a[0], listaAlunos))
notasStr = list(map(lambda a: a[1:], listaAlunos))
melhoresNotas = [list((map(int, x))) for x in notasStr]


for x in range(len(alunos)):
    nome = alunos[x]
    notas = sorted(melhoresNotas[x], reverse=True)[0:3]
    media = round(sum(notas) / 3, 2)
    print(f"Nome: {nome} Notas: {notas} Média: {media}")
