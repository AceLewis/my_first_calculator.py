# Generator used to create my_first_calculator

# Open a file that we can write to
with open('my_first_calculator.py', 'w') as python_file:
    # The minimum and maximum numbers we can use
    min_num = 0
    max_num = 50
    nums = range(min_num, max_num+1)
    signs = ['+', '-', '/', '*']
    num_of_ifs = len(signs)*(max_num-min_num)**2

    python_file.write("""# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from {} to {}')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
""".format(min_num, max_num))

    # For all the numbers and all the
    for sign in signs:
        for num1 in nums:
            for num2 in nums:
                equation = "{}{}{}".format(num1, sign, num2)
                try:
                    equals = eval(equation)
                except ZeroDivisionError:
                    equals = 'Inf'
                # No elif's used to be true to the story and also because
                # Python will throw a recursion error when too many are used
                python_file.write("if num1 == {} and sign == '{}' and "
                                  "num2 == {}:\n".format(num1, sign, num2))
                python_file.write('    print("{} = {}")\n'.format(equation,
                                                                  equals))

    python_file.write('\n')
    python_file.write('print("Thanks for using this calculator, goodbye :)")'
                      '\n')
