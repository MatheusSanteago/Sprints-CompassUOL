operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]


def calculo(a, b, c):
    match b:
        case '+':
            return a + c
        case '-':
            return a - c
        case '*':
            return a * c
        case '/':
            return a / c
        case '%':
            return a % c
        case _:
            pass


def calcular_valor_maximo(operadores, operandos) -> float:
    t = tuple(zip(operadores, operandos))
    num1 = list((map(lambda a: a[1][0], t)))
    num2 = list((map(lambda a: a[1][1], t)))
    listaCalculada = list(map(calculo, num1, operadores, num2))
    maxValue = max(listaCalculada)
    return maxValue


print(calcular_valor_maximo(operadores, operandos))
