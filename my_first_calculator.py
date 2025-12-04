# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = int(input('Please choose your first number: '))
operator = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))



if operator == '+':
    print("Result:", num1 + num2)

elif operator == '-':
    print("Result:", num1 - num2)

elif operator == '*':
    print("Result:", num1 * num2)

elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator!")

print("Thanks for using calculator")
