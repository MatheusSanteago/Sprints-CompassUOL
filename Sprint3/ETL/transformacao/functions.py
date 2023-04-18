def myMax(data, y, n):  # Função com a resolução das atividades 1 e 2
    f = open(f'etapa-{n}.txt', 'w')

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
    f = open(f'etapa-{3}.txt', 'w')

    aux = list(map(avgBruto, data))
    for i in range(len(data)):
        content = f'Ator/Atriz: {data[i][0]} -- Média \
de Faturamento bruto: {aux[i]} \n'
        f.write(content)

    f.close()


def filmeFrequente(data):  # Função atividade 4
    f = open(f'etapa-{4}.txt', 'w')

    movies = [data[i][4] for i in range(len(data))]
    mostWatch = {
        'movie': '',
        'frequency': 0
    }
    for i in range(len(movies)):
        counter = movies.count(movies[i])
        if counter > mostWatch['frequency']:
            mostWatch['frequency'], mostWatch['movie'] = counter, movies[i]
        else:
            pass
        if i == len(data) - 1:
            text = f'O filme mais frequente é {mostWatch["movie"]} com \
{mostWatch["frequency"] + 1} frequências'
            f.write(text)

    f.close()


def maiorFaturamento(data):  # Função atividade 5
    f = open(f'etapa-{5}.txt', 'w')

    aux = sorted([data[i][1] for i in range(len(data))], reverse=True)
    for i in range(len(aux)):
        for x in range(len(aux)):
            if aux[i] == data[x][1]:
                content = f'{data[x][0]} --- {aux[i]} \n'
                f.write(content)

    f.close()
