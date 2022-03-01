myNums = [2, 3, 4, 5, 6, 7, 8, 9, 0, 10]


def is_even(n):
    return n % 2 == 0


evens = filter(is_even, myNums)

# Either the for loop will work or the for loop
# for s in evens:
#     print(s)

print(list(evens))
