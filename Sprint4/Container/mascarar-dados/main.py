import hashlib


def mascarar_dados():
    i = 0
    while i < 3:
        try:
            data = input('Digite um texto: ')
        except EOFError:
            break
        dataEncoded = data.encode('utf-8')
        m = hashlib.sha1(dataEncoded)
        print(m.hexdigest())
        i += 1
        if i == 3:
            print('Fechando...')
            break


mascarar_dados()
