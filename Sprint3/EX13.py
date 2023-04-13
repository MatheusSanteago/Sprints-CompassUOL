a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def my_map(list, f):
    new_values = []
    for i in range(len(list)):
        new_values.append(f(list[i], 2))
    print(new_values)


my_map(a, pow)
