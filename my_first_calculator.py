# MY_FIRST_CALCULATOR.py by AceLewis

print('\t\t\t\t\t\tWELCOME TO THE CALCULATOR -> created by AceLewis')
print("It can add, subtract, multiply and divide\n") 

while True:
    operation = input("WHAT YOU WANT TO DO ? ENTER\n + FOR ADDITION, -FOR SUBRACTION, * FOR MULTIPLICATION, / FOR FORDIVISON\n")
    num1 = int(input("ENETR YOUR FIRST NUMBER ="))
    num2 = int(input("ENETR YOUR SECOND NUMBER ="))

    if operation == "+":        # for add
        add_re = num1+num2
        print(f"The addition of {num1},{num2} is {add_re}\n")
    elif operation == "-":      # for subract
        sub_re = num1-num2
        print(f"The subraction of {num1},{num2} is {sub_re}\n")
    elif operation == "*":      # for multiply
        mul_re = num1*num2
        print(f"The multiplication of {num1},{num2} is {mul_re}\n")
    elif operation == "/":      # for divide
        div_re = num1/num2
        print(f"The division of {num1},{num2} is {div_re}\n")
    else:
        print("YOU HAVE ENTERED INVALID INPUT! please check the input.\n")
