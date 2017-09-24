def add(num1,num2):
    Result = num1 + num2
    return(Result)

def sub(num1,num2):
    Result = num1 - num2
    return(Result)

def div(num1,num2):
    Result = num1 / num2
    return(Result)

def mult(num1,num2):
    Result = num1 * num2
    return(Result)

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
   
if (sign == "+") or (sign == "+") or (sign == "/") or (sign == "*"):
    if sign == "+":
        result = add(num1,num2)
        print(num1,'+',num2,'=',result)
 
    if sign == "-":
        result = sub(num1,num2)
        print(num1,'-',num2,'=',result)
 
    if sign == "/":
        result = div(num1,num2)
        print(num1,'/',num2,'=',result)
    
    if sign == "*":
        result = mult(num1,num2)
        print(num1,'*',num2,'=',result)
else:
    print('Invalid Operation! use +, -, /, or *')
   
print('Thanks for using this calculator, goodbye :)')
