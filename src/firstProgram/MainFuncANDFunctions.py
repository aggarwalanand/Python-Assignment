def hello():
    print('hello')
    print('hello again')


def get_integer():
    input_var = int(input('Enter an Integer : '))
    return input_var


def add(var1, var2):
    return var1 + var2


def main():
    print('Main function')
    value = get_integer()
    print('Integer value', value)
    print('Sum is', add(12, value))


hello()

if __name__ == '__main__':
    main()
