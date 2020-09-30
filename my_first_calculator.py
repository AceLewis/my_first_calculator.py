#This is an easy calculator
a = float(input("Enter 1st number: "))
b =  float(input("Enter 2nd number: "))
print("Square of 1st number is:", a**2)
print("Square of 2nd number is:", b**2)
print("Cube of 1st number is:", a**3)
print("Cube of 2nd number is:", b**3)
print('Sum of the numbers is:', (a+b))
print('Multiplication of the numbers is:', (a*b))
if a>=b:
    print('Subtraction of the numbers is:', (a-b))
    print('Division of the numbers is:', (a/b))
elif b>a:
    print('Subtraction of the numbers is:', (b-a))
    print('Division of the numbers is:', (b/a))
if a % 2 == 0:
    print("Your first number is even.")
else:
    print("Your first number is odd.")
if b % 2 == 0:
    print("Your second number is even.")
else:
    print("Your second number is odd.")
   
