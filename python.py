n=input("enter the calculation to be done in format <number> <operator> <number> (e to exit) :   ")
while(n!='e'):
    x=n.split(" ")
    a=int(x[0])
    c=(x[1])
    b=int(x[2])
    if (c=='+'):
        print(a+b)
    elif(c=='-'):
       print(a-b)
    elif(c=='*'):
        print(a*b)
    elif(c=='/'):
        print(a/b)
    elif(c=='^'):
        print(a**b)
    else:
        print("invalid syntax")
    n=input("enter the calculation to be done in format <number> <operator> <number> (e to exit) :   ")


