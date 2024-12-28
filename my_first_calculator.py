# my_first_calculator.py by AceLewis
def main():
    print('Welcome to this calculator!')
    print('It can add, subtract, multiply and divide whole numbers from 0 to 50')

    operators = set('+-*/')

    while True:
        try:
            num1 = float(input('Please choose your first number: '))
            break
        except ValueError:
            continue
    while True:
        sign = input('What do you want to do? +, -, /, or *: ')
        if sign.strip() not in operators:
            continue
        else: break

    while True:
        try:
            num2 = float(input('Please choose your second number: '))
            break
        except ValueError:
            continue
            
    if sign.strip() == '+':
        res = num1 + num2
        if res == int(res): return int(res)
        else: return res
    elif sign.strip() == '-':
        res = num1 - num2
        if res == int(res): return int(res)
        else: return res
    elif sign.strip() == '*':
        res = num1 * num2
        if res == int(res): return int(res)
        else: return res
    elif sign.strip() == '/':
        if num2 == 0:
            return 'You cannot divide by zero'
        else:
            res = num1 / num2
        if res == int(res): return int(sresum)
        else: return res

    print("Thanks for using this calculator, goodbye :)")
print(main())
