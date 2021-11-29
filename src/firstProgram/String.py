# String
print('----STRING----')
var = 'Anand Aggarwal'
print(var)
print(type(var))
print(var[4])
print(var[-4])
print(var[0:10])
print('\n')

# Formatted String
print('----FORMATTED STRING----')
first = 'Anand'
last = 'Aggarwal'
msg = f'{first} [{last}] is an awesome Automation Tester'
print(type(msg))
print(msg)
print(len(msg))
print(msg.upper())
print(msg.find('A'))
print(msg.replace('Aggarwal', 'Parkash Aggarwal'))
print('Anand' in msg)
print('\n')
