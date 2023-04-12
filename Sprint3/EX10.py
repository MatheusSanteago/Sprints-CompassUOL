lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']


def removerDuplicados(e):
    new_list = list(set(e))
    print(new_list)
    return new_list


removerDuplicados(lista)
