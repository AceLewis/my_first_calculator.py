# my_first_calculator.py by AceLewis
# Note to AceLewis: You can replace your hard work with these few lines of code. :) Hope it helps you.


  
count = 5
while count >= 1:
    print("This is just a Simple Calculator")
    num_1 = int(input("Please Enter Your First Number: "))
    num_2 = int(input("Please Enter Your Second Number: "))
    operator = input("Please Enter The Operator (+ or - or * or /) : ")
    if operator == '+':
        print(f'Sum = {num_1 + num_2}')
        count -= 1
    elif operator == '-':
        print(f'Sum = {num_1 - num_2}')
        count -= 1
    elif operator == '*':
        print(f'Sum = {num_1 * num_2}')
        count -= 1
    elif operator == '/':
        print(f'Sum = {num_1 / num_2}')
        count -= 1
    else:
        print(
            ":( I don't understand that operator, please use '+' for addition, '-' for subtraction, '*' or 'x' for multiplication and '/' for division. "
        )
        count -= 1
