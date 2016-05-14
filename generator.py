from decimal import Decimal as d
import decimal
# Generator used to create my_first_calculator

# Open a file that we can write to
python_file = open('my_first_calculator.py', 'w')
# The minimum and maximum numbers we can use
min_num = 0
max_num = 50
nums = range(min_num, max_num+1)
signs = ['+', '-', '/', '*']
num_of_ifs = len(signs)*(max_num-min_num+1)**2

print("""# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from {} to {}')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
""".format(min_num, max_num), file=python_file)

# For all the numbers and all the
for sign in signs:
    for num1 in nums:
        for num2 in nums:
            equation = "d({}){}d({})".format(num1, sign, num2)
            try:
                equals = eval(equation)
            except ZeroDivisionError:
                equals = 'Inf'
            except decimal.InvalidOperation as error:
                if error == decimal.DivisionByZero:
                    equals = 'Inf'
                else:
                    equals = 'Undefined'
            # No elif's used to be true to the story and also because
            # Python will throw a recursion error when too many are used
            print("if num1 == {} and sign == '{}' and num2 == {}:".format(num1, sign, num2), file=python_file)
            print('    print("{}{}{} = {}")'.format(num1, sign, num2, equals), file=python_file)

print('', file=python_file)
print('print("Thanks for using this calculator, goodbye :)")', file=python_file)

# Close the file we have written to
python_file.close()
