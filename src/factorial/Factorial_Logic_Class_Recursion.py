class Factorial:

    def calc_factorial(self, a):
        if a == 1:
            return a
        else:
            return a * self.calc_factorial(a - 1)


factObj = Factorial()

print(factObj.calc_factorial(5))
