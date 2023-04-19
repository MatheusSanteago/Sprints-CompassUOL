from myfunctions.functions import avgFaturamentoBruto, \
    filmeFrequente, maiorFaturamento, myMax  # Funções

file = 'actors.csv'
actorsGross = []  # Lista com dados brutos.


def extracao(f, dataList):
    try:
        with open(f) as actorsData:
            for actor in actorsData:
                if '"Robert Downey, Jr."' in actor:
                    dataList.append(actor.replace(',', '', 1).replace(
                        '.', '', 1).replace(
                        '"', '', 2).rstrip('\n').split(','))
                else:
                    actorData = actor.rstrip('\n').split(',')
                    dataList.append(actorData)
        return True
    except FileNotFoundError:
        print('Arquivo não encotrado')
        return False


def transformacao(data):
    data.pop(0)
    for i in range(len(data)):
        for x in range(len(data[i])):
            if data[i][x][0].isnumeric():
                if x == 2:
                    data[i][x] = int((data[i][x]).strip())
                else:
                    data[i][x] = float((data[i][x]).strip())
    return data


if __name__ == '__main__':
    actors = []
    try:
        loading = extracao(file, actorsGross)
        if loading:
            actors = transformacao(actorsGross)
            try:
                myMax(actors, 2, 1)
                myMax(actors, 3, 2)
                avgFaturamentoBruto(actors)
                filmeFrequente(actors)
                maiorFaturamento(actors)
            finally:
                print('Resultados exportados.')
                stats = True
        else:
            stats = False
            pass
    finally:
        print('Operação concluída ' + ('sem sucesso.', 'com Sucesso.')[stats])
