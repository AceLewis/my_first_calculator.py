num1 = int(input('Enter 1st number\n'))
operator = input('Select 1 operator -,+,*,/\n')
num2 = int(input('Enter 2nd number\n'))
try:
    problem = f'{num1} {operator} {num2}'
    print(f'{problem} = {eval(problem)}')

except:
    print('Invalid Input')
