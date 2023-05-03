from statistics import mean

file = 'estudantes.csv'
lista = []


with open(file) as alunos:
    for aluno in alunos:
        lista.append(aluno.rstrip('\n').split(','))

listaAlunos = sorted(lista)
listaAlunos.sort()
alunos = list(map(lambda a: a[0], listaAlunos))
notasStr = list(map(lambda a: a[1:], listaAlunos))
melhoresNotas = [list((map(int, x))) for x in notasStr]


for x in range(len(alunos)):
    nome = alunos[x]
    notas = sorted(melhoresNotas[x], reverse=True)[0:3]
    media = float(round(mean(notas), 2))
    print(f"Nome: {nome} Notas: {notas} Média: {media}")
