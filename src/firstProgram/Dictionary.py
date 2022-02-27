# Dictionary
print('----DICTIONARY----')
var = {
    1: 'Anand',
    2: 'Parkash'
}
print(type(var))
print(var)
print(var[1])

var[3] = ['Aggarwal']
print(var)

var.update({4: 'Ullas', 5: 'Ratna', 6: 'Aggrawal', 7: 'Dummy 1', 8: 'Dummy 2'})
print(var)

del var[7]
print(var)

var.pop(8)
print(var)
print('\n')
