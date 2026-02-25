while True:
    try:
        print("Please input the first number:")
        n1 = int(input())
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        print("Please input the second number:")
        n2 = int(input())
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    print("Please input the operation you want to perform(+, -, *, /):")
    op = input().strip()
    if op in ['+', '-', '*', '/']:
        break
    print("Invalid operation. Please use one of: +, -, *, /")

match op:
    case '+':
        print("The result is: " + str(n1 + n2))
    case '-':
        print("The result is: " + str(n1 - n2))
    case '*':
        print("The result is: " + str(n1 * n2))
    case '/':
        print("The result is: " + str(n1 / n2))