from fnmatch import translate
import tracemalloc


file = 'actors.csv'
actorsGross = []


def extracao(file, data):   # Extração
    with open(file) as actorsData:
        for i in actorsData:
            lineContent = i.rstrip('\n').split(',')
            data.append(lineContent)


def transformacao(data):  # Transformação
    for i in range(len(data)):
        for x in range(len(data[i])):
            if data[i][x][0].isnumeric():
                data[i][x] = float((data[i][x]).replace(' ', ''))
    return data


if __name__ == '__main__':
    extracao(file, actorsGross)
    actors = transformacao(actorsGross)
    print(actors)
