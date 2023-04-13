def transformar(string):
    lista = string.split(',')
    num = []
    for i, n in enumerate(lista):
        num.append(int(lista[i]))
    print(sum(num))


transformar("1,3,4,6,10,76")
