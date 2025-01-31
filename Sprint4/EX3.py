from functools import reduce

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]


def calcula_saldo(lancamentos) -> float:
    debito = list(filter(lambda l: l[1] in 'D', lancamentos))
    credito = list(filter(lambda l: l[1] in 'C', lancamentos))

    valorEmDebito = list(map(lambda a: a[0], debito))
    valorEmCredito = list(map(lambda a: a[0], credito))

    return reduce(lambda x, y: x+y, valorEmCredito) - reduce(lambda x, y: x+y, valorEmDebito)


calcula_saldo(lancamentos)
