def t(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs.values():
        print(i)


t(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
