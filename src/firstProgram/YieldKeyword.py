def fun():
    s = 0

    for i in range(10):
        s += i
        yield s


for i in fun():
    print(i)
