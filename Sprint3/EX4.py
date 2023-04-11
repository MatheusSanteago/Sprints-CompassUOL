for i in range(2, 100):
    if i > 1:
        primosx = [x for x in [2, 3, 5, 7] if i %
                   x == 0 and (i != 2 and i != 3 and i != 5 and i != 7)]
        if len(primosx) > 0:
            pass
        else:
            print(i)
