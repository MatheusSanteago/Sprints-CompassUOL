def myMax(data, y, n):  # Função com a resolução das atividades 1 e 2
    f = open(f'./RespostasTXT/etapa-{n}.txt', 'w')

    axis_num = [data[x][y] for x in range(len(data)) if data[x][y] > 0]
    i = axis_num.index(max(axis_num))
    if y == 2:
        content = f'O ator/atriz {data[i][0]} participou de {data[i][y]} filmes.'
        f.write(content)
    else:
        content = f'O ator/atriz {data[i][0]} obteve a maior média de \
faturamento por filme, equivalente a {data[i][y]} \n'
        f.write(content)
    f.close()


def avgBruto(a):
    return round(a[1] / a[2], 2)


def avgFaturamentoBruto(data):  # Função atividade 3
    f = open(f'./RespostasTXT/etapa-{3}.txt', 'w')

    aux = list(map(avgBruto, data))
    for i in range(len(data)):
        content = f'Ator/Atriz: {data[i][0]} -- Média \
de Faturamento bruto: {aux[i]} \n'
        f.write(content)
    f.close()


def filmeFrequente(data):  # Função atividade 4
    f = open(f'./RespostasTXT/etapa-{4}.txt', 'w')

    movies = [data[i][4] for i in range(len(data))]
    movie = max(movies, key=movies.count)

    text = f'O filme mais frequente é {movie} com \
 {movies.count(movie)} frequências'
    f.write(text)
    f.close()


def maiorFaturamento(data):  # Função atividade 5
    f = open(f'./RespostasTXT/etapa-{5}.txt', 'w')

    matriz = []
    for i in data:
        matriz.append([i[0], i[1]])

    matriz.pop(0)
    matriz.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(matriz)):
        content = f'O ator/atriz {matriz[i][0]} teve o faturamento bruto de \
{matriz[i][1]}\n'
        f.write(content)
    f.close()
