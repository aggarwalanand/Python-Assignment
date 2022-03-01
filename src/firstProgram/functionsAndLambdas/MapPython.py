from functools import reduce

myNums = [2, 3, 4, 5, 6, 7, 8, 9, 0, 10]


def is_even(n):
    return n % 2 == 0


evens = filter(is_even, myNums)

# Iterate on all the values of evens
myDouble = list(map(lambda x: x * 6, evens))
print(myDouble)

# Returns a single value.
mySum = reduce(lambda a, b: a + b, myDouble)
print(mySum)

# Either the for loop will work or the for loop
# for s in evens:
#     print(s)

# print(list(evens))
m = [45, 55, 60]
x = [2, 3, 4]
bmi = reduce(lambda a, b: a + b, (map(lambda a, b: a * b, m, x)))
print(bmi)
