def generator(x, y, z):
    a = []
    for i in range(x, y, z):
        a.append(i)
    return a
print(generator(10, 20, 2))
