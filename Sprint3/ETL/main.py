from transformacao.functions import avgFaturamentoBruto,\
    filmeFrequente, maiorFaturamento, myMax  # Funções


file = 'actors.csv'
actorsGross = []  # Lista com dados brutos.


def extracao(file, data):
    with open(file) as actorsData:
        for i in actorsData:
            if '"Robert Downey, Jr."' in i:
                data.append(i.replace(',', '', 1).replace(
                    '.', '', 1).replace(
                    '"', '', 2).rstrip('\n').split(','))
            else:
                lineContent = i.rstrip('\n').split(',')
                data.append(lineContent)


def transformacao(data):
    data.pop(0)  # Remover Header do CSV
    for i in range(len(data)):
        for x in range(len(data[i])):
            if data[i][x][0].isnumeric():
                if x == 2:
                    data[i][x] = int((data[i][x]).replace(' ', ''))
                else:
                    data[i][x] = float((data[i][x]).replace(' ', ''))

    return data


if __name__ == '__main__':
    extracao(file, actorsGross)
    actors = transformacao(actorsGross)
    # Resultados
    myMax(actors, 2, 1)
    myMax(actors, 3, 2)
    avgFaturamentoBruto(actors)
    filmeFrequente(actors)
    maiorFaturamento(actors)
