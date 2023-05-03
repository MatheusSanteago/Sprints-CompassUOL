file = 'estudantes.csv'
listaAlunos = []


with open(file) as alunos:
    try:
        for aluno in alunos:
            listaAlunos.append(aluno.rstrip('\n').split(','))
    finally:
        listaAlunos.sort()
        notasStr = list(map(lambda a: a[1:], listaAlunos))
        melhoresNotas = [list((map(int, x))) for x in notasStr]

for x in range(len(alunos)):
    notas = sorted(melhoresNotas[x], reverse=True)[0:3]
    media = round(sum(notas) / 3, 2)
    print(f"Nome: {listaAlunos[x][0]} Notas: {notas} Média: {media}")
