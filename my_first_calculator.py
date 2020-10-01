# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can Add, Subtract, Multiply and Divide whole numbers from 0 to 50')
num1 = int(input('Please enter your first number: '))
sign = input('What do you want to do? Add(+), Subtract(-), Divide(/), or Multiply(*) : ')
num2 = int(input('Please enter your second number: '))

if sign == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif sign == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif sign == '/':
    result = num1/num2
    print(f"{num1} / {num2} = {result}")

elif sign == '*':
    result = num1*num2
    print(f"{num1} * {num2} = {result}")
   
else:
    print("Invalid Choice! Choose correct operation from +, -, *, /")
