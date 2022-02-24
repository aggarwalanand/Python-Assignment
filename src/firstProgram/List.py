# List
print('----LIST----')
var = [1, 'Anand', 2, 'Aggarwal', 3, 4, 5, 6]
var2 = [7, 8, 9]
var3 = var2 + var
print(var3)
print(var2 + var)
print(type(var))
print(var)
print(var[1])
print(var[0:4])
print(var[-1])
var.append(7)
print(var)
var[0] = 0
print(var)
var.extend([8, 9])
print(var)

print('----INSERT----')
var = [1, 2, 3]
var.insert(0, 0)
print(var.index(3))
print(var)

print('----REMOVE----')
var = [1, 2, 3]
var.remove(1)
print(var)

print('----CLEAR----')
var = [1, 2, 3]
var.clear()
print(var)

print('----POP----')
var = [1, 2, 3]
var.pop()
print(var)
