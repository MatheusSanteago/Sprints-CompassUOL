file = 'actors.csv'
actorsGross = []


def extracao(file, data):   # Extração
    with open(file) as actorsData:
        for i in actorsData:
            lineContent = i.rstrip('\n').split(',')
            data.append(lineContent)


def transformacao(data):  # Transformação
    data.pop(0)
    for i in range(len(data)):
        if len(data[i]) >= 7:
            data[i][0] = data[i][0] + data[i][1]
            data[i].pop(1)
        for x in range(len(data[i])):
            if data[i][x][0].isnumeric():
                if x == 2:
                    data[i][x] = int((data[i][x]).replace(
                        ' ', ''))
                else:
                    data[i][x] = float((data[i][x]).replace(
                        ' ', ''))

    return data


if __name__ == '__main__':
    extracao(file, actorsGross)
    actors = transformacao(actorsGross)
    # for i in actors:
    #     print(i[2] is int)
    # Resultados
