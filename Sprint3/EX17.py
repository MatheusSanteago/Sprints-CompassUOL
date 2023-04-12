lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = []


def dividir(lista):
    aux = 0
    for i in range(4, len(lista) + 1, 4):
        if aux == 8:
            new_list.append(lista[aux:])
        else:
            new_list.append(lista[aux:i])
            aux = i


dividir(lista)
print(new_list[0], new_list[1], new_list[2])
