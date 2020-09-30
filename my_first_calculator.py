print ("====================")
print ("Simple Calculator")
print ("By : Acelewis")
print ("====================")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")
pilih = input("Choose No 1-4 = ")
if pilih=="1":
    print ("==============")
    print ("Add")
    print ("==============")
    x = int(input("Input your Num1 ="))
    z = int(input("Input your Num2 ="))
    hasil = x+z
    print ("Result =",  hasil)
elif pilih=="2":
    print ("==============")
    print ("Subtract")
    print ("==============")
    x = int(input("Input your Num1 ="))
    z = int(input("Input your Num2 ="))
    hasil = x-z
    print ("Result =",  hasil)
elif pilih=="3":
    print ("==============")
    print ("Multiply")
    print ("==============")
    x = int(input("Input your Num1 ="))
    z = int(input("Input your Num2 ="))
    hasil = x*z
    print ("Result =",  hasil)
elif pilih=="4":
    print ("==============")
    print ("Divide")
    print ("==============")
    x = int(input("Input your Num1 ="))
    z = int(input("Input your Num2 ="))
    hasil = x/z
    print ("Result =",  hasil)
else:
   print("Sorry!") 