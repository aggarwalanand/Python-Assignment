cube = lambda x: x * x * x
sum = lambda a, b: a + b


def return_lambda(n):
    return lambda a: a * n


subtract = return_lambda(15)  # Sets the value of n
print(subtract(15))  # Assign value to a
print(cube(8))
print(sum(10, 15))

result = cube(8) * sum(10, 15)
print("Result is ", result)
