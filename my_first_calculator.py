# my_first_calculator.py by AceLewis

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = float(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = float(input('Please choose your second number: '))

if num1 == 0 and sign == '+' and num2 == 0:
    print("0+0 = 0")
elif num1 == 2.2 and sign == '-' and num2 == 0.1:
    print("2.2-0.1 = 2.1")
else:
    # We have to learn something new...
    new_if = ("elif num1 == %s and sign == '%s' and num2 == %s:\n"
        "    print(\"%s%s%s = %s\")\n" % (num1, sign, num2, num1, sign, num2,
            eval(str(num1) + sign + str(num2))))
    import os, sys
    os.rename(__file__, __file__ + ".tmp")
    with open(__file__ + ".tmp", "r") as fin, open(__file__, "w") as fout:
        for line in fin:
            if line == "else:\n":
                fout.write(new_if)
            fout.write(line)
    os.chmod(__file__, 0o755)
    print("Sorry, I didn't know it, please ask again")

print("Thanks for using this calculator, goodbye :)")
