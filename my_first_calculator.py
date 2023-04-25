# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mul(n1, n2):
    return n1 * n2

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))

#  The original implementation was hardcoded for every number between 0 to 50
#  I have altered this to work for all numbers now by implementing functions
#  and just callin the functions with the numbers the user has inputted
#  This way is much simpler than hardcoding every single number 

if sign == "+":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif sign == "-":
    print(f"{num1} - {num2} = {sub(num1, num2)}")
elif sign == "/":
    print(f"{num1} / {num2} = {div(num1, num2)}")
elif sign == "*":
    print(f"{num1} * {num2} = {mul(num1, num2)}")


print("Thanks for using this calculator, goodbye :)")
