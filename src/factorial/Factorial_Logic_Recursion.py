def calc_factorial(a):
    if a == 1:
        return a
    else:
        return a * calc_factorial(a - 1)


print(calc_factorial(5))
