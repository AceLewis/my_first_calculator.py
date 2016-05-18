# Generator by ArtaMan

fout = open('my_first_calculator.py', 'w') #opens a python file
#min, max numbers
min_num = 0
max_num = 50

#printing a head
print("""# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from {} to {}')
""".format(min_num, max_num), file=fout)

#printing a function
print("def calculator():", file=fout)
#inputs
print("    num1 = int(input('Please choose your first number: '))", file=fout)
print("    sign = input('What do you want to do? +, -, /, or *: ')", file=fout)
print("    num2 = int(input('Please choose your second number: '))", file=fout)
#printing ifs for '+' operation
for i in range(min_num, max_num + 1):
    for j in range(min_num, max_num + 1):
        equals = i + j
        print('    if num1 == {} and sign == "+" and num2 == {}:'.format(i, j), file=fout)
        print('        print("{} + {}  = {}")'.format(i, j, equals), file=fout)

#printing ifs for '-' operation
for i in range(min_num, max_num + 1):
    for j in range(min_num, max_num + 1):
        equals = i - j
        print('    if num1 == {} and sign == "-" and num2 == {}:'.format(i, j), file=fout)
        print('        print("{} - {}  = {}")'.format(i, j, equals), file=fout)

#printing ifs for '*' operation
for i in range(min_num, max_num + 1):
    for j in range(min_num, max_num + 1):
        equals = i * j
        print('    if num1 == {} and sign == "*" and num2 == {}:'.format(i, j), file=fout)
        print('        print("{} * {}  = {}")'.format(i, j, equals), file=fout)

#printing ifs for '/' operation
for i in range(min_num, max_num + 1):
    for j in range(min_num, max_num + 1):
        #You can't devide by zero
        if j != 0:
            equals = i / j
            print('    if num1 == {} and sign == "/" and num2 == {}:'.format(i, j), file=fout)
            print('        print("{} / {}  = {}")'.format(i, j, equals), file=fout)
        else:
            print('    if num1 == {} and sign == "/" and num2 == {}:'.format(i, j), file=fout)
            print('        #ZeroDivisionError: division by zero', file=fout)
            print("""        print("You can't divide by zero :(")""", file=fout)

print("    print('')", file=fout)
print("    print('Thanks for using my calculator!')", file=fout)
print("    print('')", file=fout)
#calling the function again
print('    calculator()', file=fout)

#calling the function for first time
print('calculator()', file=fout)
fout.close()