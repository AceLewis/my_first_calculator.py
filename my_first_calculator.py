print('Operations are carried out only on two numbers at a time')
print('Type "help" for help')

# addition function
def add(x, y):
    print(x + y)


# subtraction function
def subtract(x, y):
    print(x - y)


# multiplication function
def multiply(x, y):
    print(x * y)


# division function
def divide(x, y):
    print(x / y)


# modulo function
def modulo(x, y):
    print(x % y)


# exponentiation function
def index(x, y):
    print(x ** y)

# circle area
def circle_area(x):
    print(x**2 * 3.141592654)

# triangle area
def triangle_area(x):
    print("The result is based on the triangle height hence this calculator is limited")
    print(0.5 * x)

# rectangle area
def rectangle_area(x, y):
    print(x * y)

def help():
    print('WELCOME TO HELP')
    print('Type "addition" for addition operation')
    print('Type "subtraction" for subtraction operation')
    print('Type "multiplication" for multiplication operation')
    print('Type "division" for division operation')
    print('Type "modulo" for modulo operation')
    print('Type "exponentiation" for exponentiation operation')
    print('Type "triangle area" for triangle area calculation')
    print('Type "circle area" to calculate the area of a circle')
    print('Type "rectangle area for rectangle area calculation')

operation = (input("ENTER AN OPERATION :"))


if operation == 'addition': #addition operation
    x = float(input('ENTER YOUR FIRST NUMBER :'))   #setting the input to float to accept decimal numbers input
    y = float(input('ENTER YOUR SECOND NUMBER :'))
    (add(x, y)) #using the defined 'add' function above to add the numbers
elif operation == 'subtraction': #subtraction operation
    x = float(input('ENTER FIRST NUMBER :'))
    y = float(input('ENTER SECOND NUMBER :'))
    (subtract(x, y))
elif operation == 'multiplication': #multiplication operation
    x = float(input('ENTER FIRST NUMBER :'))
    y = float(input('ENTER SECOND NUMBER :'))
    (multiply(x, y))
elif operation == 'division':
    x = float(input('ENTER FIRST NUMBER :'))
    y = float(input('ENTER SECOND NUMBER :'))
    divide(x, y)
elif operation == 'modulo': #modulo operation
    x = float(input('ENTER FIRST NUMBER :'))
    y = float(input('ENTER SECOND NUMBER :'))
    (modulo(x, y))
elif operation == 'exponentiation': #exponentiation operation
    x = float(input('ENTER BASE NUMBER :'))
    y = float(input('ENTER POWER NUMBER :'))
    (index(x, y))
elif operation == 'help':
    help()
elif operation == "circle area":
    x = float(input("Enter the radius :"))
    circle_area(x)
elif operation == "triangle area":
    x = float(input('Enter height of triangle :'))
    triangle_area(x)
elif operation == "rectangle area":
    x = float(input('ENTER LENGTH OF TRIANGLE :'))
    y = float(input('ENTER WIDTH OF TRIANGLE :'))
    rectangle_area(x, y)
else:
    print('UNKNOWN COMMAND OR INPUT') #error handling if user input is not included in the program
    #error handling could also be done with the try and except functions

print('Thanks for using NEGA CALCULATOR. Feel free to modify and add new features')
#Feel free to modify and add new features
#This program will be very useful to beginers :)
#If there are lacks in this code(program/software), you are completely free to modify, add, or remove any part of the code
#This program is licensed under the MIT license
