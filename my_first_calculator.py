# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))

def calculate (num1,sign,num2):
    if num1 == 0 and sign == '+' and num2 == 0:
        return("0+0 = 0")
    if num1 == 0 and sign == '+' and num2 == 1:
        return("0+1 = 1")
    if num1 == 0 and sign == '+' and num2 == 2:
        return("0+2 = 2")
    if num1 == 0 and sign == '+' and num2 == 3:
        return("0+3 = 3")
    if num1 == 0 and sign == '+' and num2 == 4:
        return("0+4 = 4")
    if num1 == 0 and sign == '+' and num2 == 5:
        return("0+5 = 5")
    if num1 == 0 and sign == '+' and num2 == 6:
        return("0+6 = 6")
    if num1 == 0 and sign == '+' and num2 == 7:
        return("0+7 = 7")
    if num1 == 0 and sign == '+' and num2 == 8:
        return("0+8 = 8")
    if num1 == 0 and sign == '+' and num2 == 9:
        return("0+9 = 9")
    if num1 == 0 and sign == '+' and num2 == 10:
        return("0+10 = 10")
    if num1 == 0 and sign == '+' and num2 == 11:
        return("0+11 = 11")
    if num1 == 0 and sign == '+' and num2 == 12:
        return("0+12 = 12")
    if num1 == 0 and sign == '+' and num2 == 13:
        return("0+13 = 13")
    if num1 == 0 and sign == '+' and num2 == 14:
        return("0+14 = 14")
    if num1 == 0 and sign == '+' and num2 == 15:
        return("0+15 = 15")
    if num1 == 0 and sign == '+' and num2 == 16:
        return("0+16 = 16")
    if num1 == 0 and sign == '+' and num2 == 17:
        return("0+17 = 17")
    if num1 == 0 and sign == '+' and num2 == 18:
        return("0+18 = 18")
    if num1 == 0 and sign == '+' and num2 == 19:
        return("0+19 = 19")
    if num1 == 0 and sign == '+' and num2 == 20:
        return("0+20 = 20")
    if num1 == 0 and sign == '+' and num2 == 21:
        return("0+21 = 21")
    if num1 == 0 and sign == '+' and num2 == 22:
        return("0+22 = 22")
    if num1 == 0 and sign == '+' and num2 == 23:
        return("0+23 = 23")
    if num1 == 0 and sign == '+' and num2 == 24:
        return("0+24 = 24")
    if num1 == 0 and sign == '+' and num2 == 25:
        return("0+25 = 25")
    if num1 == 0 and sign == '+' and num2 == 26:
        return("0+26 = 26")
    if num1 == 0 and sign == '+' and num2 == 27:
        return("0+27 = 27")
    if num1 == 0 and sign == '+' and num2 == 28:
        return("0+28 = 28")
    if num1 == 0 and sign == '+' and num2 == 29:
        return("0+29 = 29")
    if num1 == 0 and sign == '+' and num2 == 30:
        return("0+30 = 30")
    if num1 == 0 and sign == '+' and num2 == 31:
        return("0+31 = 31")
    if num1 == 0 and sign == '+' and num2 == 32:
        return("0+32 = 32")
    if num1 == 0 and sign == '+' and num2 == 33:
        return("0+33 = 33")
    if num1 == 0 and sign == '+' and num2 == 34:
        return("0+34 = 34")
    if num1 == 0 and sign == '+' and num2 == 35:
        return("0+35 = 35")
    if num1 == 0 and sign == '+' and num2 == 36:
        return("0+36 = 36")
    if num1 == 0 and sign == '+' and num2 == 37:
        return("0+37 = 37")
    if num1 == 0 and sign == '+' and num2 == 38:
        return("0+38 = 38")
    if num1 == 0 and sign == '+' and num2 == 39:
        return("0+39 = 39")
    if num1 == 0 and sign == '+' and num2 == 40:
        return("0+40 = 40")
    if num1 == 0 and sign == '+' and num2 == 41:
        return("0+41 = 41")
    if num1 == 0 and sign == '+' and num2 == 42:
        return("0+42 = 42")
    if num1 == 0 and sign == '+' and num2 == 43:
        return("0+43 = 43")
    if num1 == 0 and sign == '+' and num2 == 44:
        return("0+44 = 44")
    if num1 == 0 and sign == '+' and num2 == 45:
        return("0+45 = 45")
    if num1 == 0 and sign == '+' and num2 == 46:
        return("0+46 = 46")
    if num1 == 0 and sign == '+' and num2 == 47:
        return("0+47 = 47")
    if num1 == 0 and sign == '+' and num2 == 48:
        return("0+48 = 48")
    if num1 == 0 and sign == '+' and num2 == 49:
        return("0+49 = 49")
    if num1 == 0 and sign == '+' and num2 == 50:
        return("0+50 = 50")
    if num1 == 1 and sign == '+' and num2 == 0:
        return("1+0 = 1")
    if num1 == 1 and sign == '+' and num2 == 1:
        return("1+1 = 2")
    if num1 == 1 and sign == '+' and num2 == 2:
        return("1+2 = 3")
    if num1 == 1 and sign == '+' and num2 == 3:
        return("1+3 = 4")
    if num1 == 1 and sign == '+' and num2 == 4:
        return("1+4 = 5")
    if num1 == 1 and sign == '+' and num2 == 5:
        return("1+5 = 6")
    if num1 == 1 and sign == '+' and num2 == 6:
        return("1+6 = 7")
    if num1 == 1 and sign == '+' and num2 == 7:
        return("1+7 = 8")
    if num1 == 1 and sign == '+' and num2 == 8:
        return("1+8 = 9")
    if num1 == 1 and sign == '+' and num2 == 9:
        return("1+9 = 10")
    if num1 == 1 and sign == '+' and num2 == 10:
        return("1+10 = 11")
    if num1 == 1 and sign == '+' and num2 == 11:
        return("1+11 = 12")
    if num1 == 1 and sign == '+' and num2 == 12:
        return("1+12 = 13")
    if num1 == 1 and sign == '+' and num2 == 13:
        return("1+13 = 14")
    if num1 == 1 and sign == '+' and num2 == 14:
        return("1+14 = 15")
    if num1 == 1 and sign == '+' and num2 == 15:
        return("1+15 = 16")
    if num1 == 1 and sign == '+' and num2 == 16:
        return("1+16 = 17")
    if num1 == 1 and sign == '+' and num2 == 17:
        return("1+17 = 18")
    if num1 == 1 and sign == '+' and num2 == 18:
        return("1+18 = 19")
    if num1 == 1 and sign == '+' and num2 == 19:
        return("1+19 = 20")
    if num1 == 1 and sign == '+' and num2 == 20:
        return("1+20 = 21")
    if num1 == 1 and sign == '+' and num2 == 21:
        return("1+21 = 22")
    if num1 == 1 and sign == '+' and num2 == 22:
        return("1+22 = 23")
    if num1 == 1 and sign == '+' and num2 == 23:
        return("1+23 = 24")
    if num1 == 1 and sign == '+' and num2 == 24:
        return("1+24 = 25")
    if num1 == 1 and sign == '+' and num2 == 25:
        return("1+25 = 26")
    if num1 == 1 and sign == '+' and num2 == 26:
        return("1+26 = 27")
    if num1 == 1 and sign == '+' and num2 == 27:
        return("1+27 = 28")
    if num1 == 1 and sign == '+' and num2 == 28:
        return("1+28 = 29")
    if num1 == 1 and sign == '+' and num2 == 29:
        return("1+29 = 30")
    if num1 == 1 and sign == '+' and num2 == 30:
        return("1+30 = 31")
    if num1 == 1 and sign == '+' and num2 == 31:
        return("1+31 = 32")
    if num1 == 1 and sign == '+' and num2 == 32:
        return("1+32 = 33")
    if num1 == 1 and sign == '+' and num2 == 33:
        return("1+33 = 34")
    if num1 == 1 and sign == '+' and num2 == 34:
        return("1+34 = 35")
    if num1 == 1 and sign == '+' and num2 == 35:
        return("1+35 = 36")
    if num1 == 1 and sign == '+' and num2 == 36:
        return("1+36 = 37")
    if num1 == 1 and sign == '+' and num2 == 37:
        return("1+37 = 38")
    if num1 == 1 and sign == '+' and num2 == 38:
        return("1+38 = 39")
    if num1 == 1 and sign == '+' and num2 == 39:
        return("1+39 = 40")
    if num1 == 1 and sign == '+' and num2 == 40:
        return("1+40 = 41")
    if num1 == 1 and sign == '+' and num2 == 41:
        return("1+41 = 42")
    if num1 == 1 and sign == '+' and num2 == 42:
        return("1+42 = 43")
    if num1 == 1 and sign == '+' and num2 == 43:
        return("1+43 = 44")
    if num1 == 1 and sign == '+' and num2 == 44:
        return("1+44 = 45")
    if num1 == 1 and sign == '+' and num2 == 45:
        return("1+45 = 46")
    if num1 == 1 and sign == '+' and num2 == 46:
        return("1+46 = 47")
    if num1 == 1 and sign == '+' and num2 == 47:
        return("1+47 = 48")
    if num1 == 1 and sign == '+' and num2 == 48:
        return("1+48 = 49")
    if num1 == 1 and sign == '+' and num2 == 49:
        return("1+49 = 50")
    if num1 == 1 and sign == '+' and num2 == 50:
        return("1+50 = 51")
    if num1 == 2 and sign == '+' and num2 == 0:
        return("2+0 = 2")
    if num1 == 2 and sign == '+' and num2 == 1:
        return("2+1 = 3")
    if num1 == 2 and sign == '+' and num2 == 2:
        return("2+2 = 4")
    if num1 == 2 and sign == '+' and num2 == 3:
        return("2+3 = 5")
    if num1 == 2 and sign == '+' and num2 == 4:
        return("2+4 = 6")
    if num1 == 2 and sign == '+' and num2 == 5:
        return("2+5 = 7")
    if num1 == 2 and sign == '+' and num2 == 6:
        return("2+6 = 8")
    if num1 == 2 and sign == '+' and num2 == 7:
        return("2+7 = 9")
    if num1 == 2 and sign == '+' and num2 == 8:
        return("2+8 = 10")
    if num1 == 2 and sign == '+' and num2 == 9:
        return("2+9 = 11")
    if num1 == 2 and sign == '+' and num2 == 10:
        return("2+10 = 12")
    if num1 == 2 and sign == '+' and num2 == 11:
        return("2+11 = 13")
    if num1 == 2 and sign == '+' and num2 == 12:
        return("2+12 = 14")
    if num1 == 2 and sign == '+' and num2 == 13:
        return("2+13 = 15")
    if num1 == 2 and sign == '+' and num2 == 14:
        return("2+14 = 16")
    if num1 == 2 and sign == '+' and num2 == 15:
        return("2+15 = 17")
    if num1 == 2 and sign == '+' and num2 == 16:
        return("2+16 = 18")
    if num1 == 2 and sign == '+' and num2 == 17:
        return("2+17 = 19")
    if num1 == 2 and sign == '+' and num2 == 18:
        return("2+18 = 20")
    if num1 == 2 and sign == '+' and num2 == 19:
        return("2+19 = 21")
    if num1 == 2 and sign == '+' and num2 == 20:
        return("2+20 = 22")
    if num1 == 2 and sign == '+' and num2 == 21:
        return("2+21 = 23")
    if num1 == 2 and sign == '+' and num2 == 22:
        return("2+22 = 24")
    if num1 == 2 and sign == '+' and num2 == 23:
        return("2+23 = 25")
    if num1 == 2 and sign == '+' and num2 == 24:
        return("2+24 = 26")
    if num1 == 2 and sign == '+' and num2 == 25:
        return("2+25 = 27")
    if num1 == 2 and sign == '+' and num2 == 26:
        return("2+26 = 28")
    if num1 == 2 and sign == '+' and num2 == 27:
        return("2+27 = 29")
    if num1 == 2 and sign == '+' and num2 == 28:
        return("2+28 = 30")
    if num1 == 2 and sign == '+' and num2 == 29:
        return("2+29 = 31")
    if num1 == 2 and sign == '+' and num2 == 30:
        return("2+30 = 32")
    if num1 == 2 and sign == '+' and num2 == 31:
        return("2+31 = 33")
    if num1 == 2 and sign == '+' and num2 == 32:
        return("2+32 = 34")
    if num1 == 2 and sign == '+' and num2 == 33:
        return("2+33 = 35")
    if num1 == 2 and sign == '+' and num2 == 34:
        return("2+34 = 36")
    if num1 == 2 and sign == '+' and num2 == 35:
        return("2+35 = 37")
    if num1 == 2 and sign == '+' and num2 == 36:
        return("2+36 = 38")
    if num1 == 2 and sign == '+' and num2 == 37:
        return("2+37 = 39")
    if num1 == 2 and sign == '+' and num2 == 38:
        return("2+38 = 40")
    if num1 == 2 and sign == '+' and num2 == 39:
        return("2+39 = 41")
    if num1 == 2 and sign == '+' and num2 == 40:
        return("2+40 = 42")
    if num1 == 2 and sign == '+' and num2 == 41:
        return("2+41 = 43")
    if num1 == 2 and sign == '+' and num2 == 42:
        return("2+42 = 44")
    if num1 == 2 and sign == '+' and num2 == 43:
        return("2+43 = 45")
    if num1 == 2 and sign == '+' and num2 == 44:
        return("2+44 = 46")
    if num1 == 2 and sign == '+' and num2 == 45:
        return("2+45 = 47")
    if num1 == 2 and sign == '+' and num2 == 46:
        return("2+46 = 48")
    if num1 == 2 and sign == '+' and num2 == 47:
        return("2+47 = 49")
    if num1 == 2 and sign == '+' and num2 == 48:
        return("2+48 = 50")
    if num1 == 2 and sign == '+' and num2 == 49:
        return("2+49 = 51")
    if num1 == 2 and sign == '+' and num2 == 50:
        return("2+50 = 52")
    if num1 == 3 and sign == '+' and num2 == 0:
        return("3+0 = 3")
    if num1 == 3 and sign == '+' and num2 == 1:
        return("3+1 = 4")
    if num1 == 3 and sign == '+' and num2 == 2:
        return("3+2 = 5")
    if num1 == 3 and sign == '+' and num2 == 3:
        return("3+3 = 6")
    if num1 == 3 and sign == '+' and num2 == 4:
        return("3+4 = 7")
    if num1 == 3 and sign == '+' and num2 == 5:
        return("3+5 = 8")
    if num1 == 3 and sign == '+' and num2 == 6:
        return("3+6 = 9")
    if num1 == 3 and sign == '+' and num2 == 7:
        return("3+7 = 10")
    if num1 == 3 and sign == '+' and num2 == 8:
        return("3+8 = 11")
    if num1 == 3 and sign == '+' and num2 == 9:
        return("3+9 = 12")
    if num1 == 3 and sign == '+' and num2 == 10:
        return("3+10 = 13")
    if num1 == 3 and sign == '+' and num2 == 11:
        return("3+11 = 14")
    if num1 == 3 and sign == '+' and num2 == 12:
        return("3+12 = 15")
    if num1 == 3 and sign == '+' and num2 == 13:
        return("3+13 = 16")
    if num1 == 3 and sign == '+' and num2 == 14:
        return("3+14 = 17")
    if num1 == 3 and sign == '+' and num2 == 15:
        return("3+15 = 18")
    if num1 == 3 and sign == '+' and num2 == 16:
        return("3+16 = 19")
    if num1 == 3 and sign == '+' and num2 == 17:
        return("3+17 = 20")
    if num1 == 3 and sign == '+' and num2 == 18:
        return("3+18 = 21")
    if num1 == 3 and sign == '+' and num2 == 19:
        return("3+19 = 22")
    if num1 == 3 and sign == '+' and num2 == 20:
        return("3+20 = 23")
    if num1 == 3 and sign == '+' and num2 == 21:
        return("3+21 = 24")
    if num1 == 3 and sign == '+' and num2 == 22:
        return("3+22 = 25")
    if num1 == 3 and sign == '+' and num2 == 23:
        return("3+23 = 26")
    if num1 == 3 and sign == '+' and num2 == 24:
        return("3+24 = 27")
    if num1 == 3 and sign == '+' and num2 == 25:
        return("3+25 = 28")
    if num1 == 3 and sign == '+' and num2 == 26:
        return("3+26 = 29")
    if num1 == 3 and sign == '+' and num2 == 27:
        return("3+27 = 30")
    if num1 == 3 and sign == '+' and num2 == 28:
        return("3+28 = 31")
    if num1 == 3 and sign == '+' and num2 == 29:
        return("3+29 = 32")
    if num1 == 3 and sign == '+' and num2 == 30:
        return("3+30 = 33")
    if num1 == 3 and sign == '+' and num2 == 31:
        return("3+31 = 34")
    if num1 == 3 and sign == '+' and num2 == 32:
        return("3+32 = 35")
    if num1 == 3 and sign == '+' and num2 == 33:
        return("3+33 = 36")
    if num1 == 3 and sign == '+' and num2 == 34:
        return("3+34 = 37")
    if num1 == 3 and sign == '+' and num2 == 35:
        return("3+35 = 38")
    if num1 == 3 and sign == '+' and num2 == 36:
        return("3+36 = 39")
    if num1 == 3 and sign == '+' and num2 == 37:
        return("3+37 = 40")
    if num1 == 3 and sign == '+' and num2 == 38:
        return("3+38 = 41")
    if num1 == 3 and sign == '+' and num2 == 39:
        return("3+39 = 42")
    if num1 == 3 and sign == '+' and num2 == 40:
        return("3+40 = 43")
    if num1 == 3 and sign == '+' and num2 == 41:
        return("3+41 = 44")
    if num1 == 3 and sign == '+' and num2 == 42:
        return("3+42 = 45")
    if num1 == 3 and sign == '+' and num2 == 43:
        return("3+43 = 46")
    if num1 == 3 and sign == '+' and num2 == 44:
        return("3+44 = 47")
    if num1 == 3 and sign == '+' and num2 == 45:
        return("3+45 = 48")
    if num1 == 3 and sign == '+' and num2 == 46:
        return("3+46 = 49")
    if num1 == 3 and sign == '+' and num2 == 47:
        return("3+47 = 50")
    if num1 == 3 and sign == '+' and num2 == 48:
        return("3+48 = 51")
    if num1 == 3 and sign == '+' and num2 == 49:
        return("3+49 = 52")
    if num1 == 3 and sign == '+' and num2 == 50:
        return("3+50 = 53")
    if num1 == 4 and sign == '+' and num2 == 0:
        return("4+0 = 4")
    if num1 == 4 and sign == '+' and num2 == 1:
        return("4+1 = 5")
    if num1 == 4 and sign == '+' and num2 == 2:
        return("4+2 = 6")
    if num1 == 4 and sign == '+' and num2 == 3:
        return("4+3 = 7")
    if num1 == 4 and sign == '+' and num2 == 4:
        return("4+4 = 8")
    if num1 == 4 and sign == '+' and num2 == 5:
        return("4+5 = 9")
    if num1 == 4 and sign == '+' and num2 == 6:
        return("4+6 = 10")
    if num1 == 4 and sign == '+' and num2 == 7:
        return("4+7 = 11")
    if num1 == 4 and sign == '+' and num2 == 8:
        return("4+8 = 12")
    if num1 == 4 and sign == '+' and num2 == 9:
        return("4+9 = 13")
    if num1 == 4 and sign == '+' and num2 == 10:
        return("4+10 = 14")
    if num1 == 4 and sign == '+' and num2 == 11:
        return("4+11 = 15")
    if num1 == 4 and sign == '+' and num2 == 12:
        return("4+12 = 16")
    if num1 == 4 and sign == '+' and num2 == 13:
        return("4+13 = 17")
    if num1 == 4 and sign == '+' and num2 == 14:
        return("4+14 = 18")
    if num1 == 4 and sign == '+' and num2 == 15:
        return("4+15 = 19")
    if num1 == 4 and sign == '+' and num2 == 16:
        return("4+16 = 20")
    if num1 == 4 and sign == '+' and num2 == 17:
        return("4+17 = 21")
    if num1 == 4 and sign == '+' and num2 == 18:
        return("4+18 = 22")
    if num1 == 4 and sign == '+' and num2 == 19:
        return("4+19 = 23")
    if num1 == 4 and sign == '+' and num2 == 20:
        return("4+20 = 24")
    if num1 == 4 and sign == '+' and num2 == 21:
        return("4+21 = 25")
    if num1 == 4 and sign == '+' and num2 == 22:
        return("4+22 = 26")
    if num1 == 4 and sign == '+' and num2 == 23:
        return("4+23 = 27")
    if num1 == 4 and sign == '+' and num2 == 24:
        return("4+24 = 28")
    if num1 == 4 and sign == '+' and num2 == 25:
        return("4+25 = 29")
    if num1 == 4 and sign == '+' and num2 == 26:
        return("4+26 = 30")
    if num1 == 4 and sign == '+' and num2 == 27:
        return("4+27 = 31")
    if num1 == 4 and sign == '+' and num2 == 28:
        return("4+28 = 32")
    if num1 == 4 and sign == '+' and num2 == 29:
        return("4+29 = 33")
    if num1 == 4 and sign == '+' and num2 == 30:
        return("4+30 = 34")
    if num1 == 4 and sign == '+' and num2 == 31:
        return("4+31 = 35")
    if num1 == 4 and sign == '+' and num2 == 32:
        return("4+32 = 36")
    if num1 == 4 and sign == '+' and num2 == 33:
        return("4+33 = 37")
    if num1 == 4 and sign == '+' and num2 == 34:
        return("4+34 = 38")
    if num1 == 4 and sign == '+' and num2 == 35:
        return("4+35 = 39")
    if num1 == 4 and sign == '+' and num2 == 36:
        return("4+36 = 40")
    if num1 == 4 and sign == '+' and num2 == 37:
        return("4+37 = 41")
    if num1 == 4 and sign == '+' and num2 == 38:
        return("4+38 = 42")
    if num1 == 4 and sign == '+' and num2 == 39:
        return("4+39 = 43")
    if num1 == 4 and sign == '+' and num2 == 40:
        return("4+40 = 44")
    if num1 == 4 and sign == '+' and num2 == 41:
        return("4+41 = 45")
    if num1 == 4 and sign == '+' and num2 == 42:
        return("4+42 = 46")
    if num1 == 4 and sign == '+' and num2 == 43:
        return("4+43 = 47")
    if num1 == 4 and sign == '+' and num2 == 44:
        return("4+44 = 48")
    if num1 == 4 and sign == '+' and num2 == 45:
        return("4+45 = 49")
    if num1 == 4 and sign == '+' and num2 == 46:
        return("4+46 = 50")
    if num1 == 4 and sign == '+' and num2 == 47:
        return("4+47 = 51")
    if num1 == 4 and sign == '+' and num2 == 48:
        return("4+48 = 52")
    if num1 == 4 and sign == '+' and num2 == 49:
        return("4+49 = 53")
    if num1 == 4 and sign == '+' and num2 == 50:
        return("4+50 = 54")
    if num1 == 5 and sign == '+' and num2 == 0:
        return("5+0 = 5")
    if num1 == 5 and sign == '+' and num2 == 1:
        return("5+1 = 6")
    if num1 == 5 and sign == '+' and num2 == 2:
        return("5+2 = 7")
    if num1 == 5 and sign == '+' and num2 == 3:
        return("5+3 = 8")
    if num1 == 5 and sign == '+' and num2 == 4:
        return("5+4 = 9")
    if num1 == 5 and sign == '+' and num2 == 5:
        return("5+5 = 10")
    if num1 == 5 and sign == '+' and num2 == 6:
        return("5+6 = 11")
    if num1 == 5 and sign == '+' and num2 == 7:
        return("5+7 = 12")
    if num1 == 5 and sign == '+' and num2 == 8:
        return("5+8 = 13")
    if num1 == 5 and sign == '+' and num2 == 9:
        return("5+9 = 14")
    if num1 == 5 and sign == '+' and num2 == 10:
        return("5+10 = 15")
    if num1 == 5 and sign == '+' and num2 == 11:
        return("5+11 = 16")
    if num1 == 5 and sign == '+' and num2 == 12:
        return("5+12 = 17")
    if num1 == 5 and sign == '+' and num2 == 13:
        return("5+13 = 18")
    if num1 == 5 and sign == '+' and num2 == 14:
        return("5+14 = 19")
    if num1 == 5 and sign == '+' and num2 == 15:
        return("5+15 = 20")
    if num1 == 5 and sign == '+' and num2 == 16:
        return("5+16 = 21")
    if num1 == 5 and sign == '+' and num2 == 17:
        return("5+17 = 22")
    if num1 == 5 and sign == '+' and num2 == 18:
        return("5+18 = 23")
    if num1 == 5 and sign == '+' and num2 == 19:
        return("5+19 = 24")
    if num1 == 5 and sign == '+' and num2 == 20:
        return("5+20 = 25")
    if num1 == 5 and sign == '+' and num2 == 21:
        return("5+21 = 26")
    if num1 == 5 and sign == '+' and num2 == 22:
        return("5+22 = 27")
    if num1 == 5 and sign == '+' and num2 == 23:
        return("5+23 = 28")
    if num1 == 5 and sign == '+' and num2 == 24:
        return("5+24 = 29")
    if num1 == 5 and sign == '+' and num2 == 25:
        return("5+25 = 30")
    if num1 == 5 and sign == '+' and num2 == 26:
        return("5+26 = 31")
    if num1 == 5 and sign == '+' and num2 == 27:
        return("5+27 = 32")
    if num1 == 5 and sign == '+' and num2 == 28:
        return("5+28 = 33")
    if num1 == 5 and sign == '+' and num2 == 29:
        return("5+29 = 34")
    if num1 == 5 and sign == '+' and num2 == 30:
        return("5+30 = 35")
    if num1 == 5 and sign == '+' and num2 == 31:
        return("5+31 = 36")
    if num1 == 5 and sign == '+' and num2 == 32:
        return("5+32 = 37")
    if num1 == 5 and sign == '+' and num2 == 33:
        return("5+33 = 38")
    if num1 == 5 and sign == '+' and num2 == 34:
        return("5+34 = 39")
    if num1 == 5 and sign == '+' and num2 == 35:
        return("5+35 = 40")
    if num1 == 5 and sign == '+' and num2 == 36:
        return("5+36 = 41")
    if num1 == 5 and sign == '+' and num2 == 37:
        return("5+37 = 42")
    if num1 == 5 and sign == '+' and num2 == 38:
        return("5+38 = 43")
    if num1 == 5 and sign == '+' and num2 == 39:
        return("5+39 = 44")
    if num1 == 5 and sign == '+' and num2 == 40:
        return("5+40 = 45")
    if num1 == 5 and sign == '+' and num2 == 41:
        return("5+41 = 46")
    if num1 == 5 and sign == '+' and num2 == 42:
        return("5+42 = 47")
    if num1 == 5 and sign == '+' and num2 == 43:
        return("5+43 = 48")
    if num1 == 5 and sign == '+' and num2 == 44:
        return("5+44 = 49")
    if num1 == 5 and sign == '+' and num2 == 45:
        return("5+45 = 50")
    if num1 == 5 and sign == '+' and num2 == 46:
        return("5+46 = 51")
    if num1 == 5 and sign == '+' and num2 == 47:
        return("5+47 = 52")
    if num1 == 5 and sign == '+' and num2 == 48:
        return("5+48 = 53")
    if num1 == 5 and sign == '+' and num2 == 49:
        return("5+49 = 54")
    if num1 == 5 and sign == '+' and num2 == 50:
        return("5+50 = 55")
    if num1 == 6 and sign == '+' and num2 == 0:
        return("6+0 = 6")
    if num1 == 6 and sign == '+' and num2 == 1:
        return("6+1 = 7")
    if num1 == 6 and sign == '+' and num2 == 2:
        return("6+2 = 8")
    if num1 == 6 and sign == '+' and num2 == 3:
        return("6+3 = 9")
    if num1 == 6 and sign == '+' and num2 == 4:
        return("6+4 = 10")
    if num1 == 6 and sign == '+' and num2 == 5:
        return("6+5 = 11")
    if num1 == 6 and sign == '+' and num2 == 6:
        return("6+6 = 12")
    if num1 == 6 and sign == '+' and num2 == 7:
        return("6+7 = 13")
    if num1 == 6 and sign == '+' and num2 == 8:
        return("6+8 = 14")
    if num1 == 6 and sign == '+' and num2 == 9:
        return("6+9 = 15")
    if num1 == 6 and sign == '+' and num2 == 10:
        return("6+10 = 16")
    if num1 == 6 and sign == '+' and num2 == 11:
        return("6+11 = 17")
    if num1 == 6 and sign == '+' and num2 == 12:
        return("6+12 = 18")
    if num1 == 6 and sign == '+' and num2 == 13:
        return("6+13 = 19")
    if num1 == 6 and sign == '+' and num2 == 14:
        return("6+14 = 20")
    if num1 == 6 and sign == '+' and num2 == 15:
        return("6+15 = 21")
    if num1 == 6 and sign == '+' and num2 == 16:
        return("6+16 = 22")
    if num1 == 6 and sign == '+' and num2 == 17:
        return("6+17 = 23")
    if num1 == 6 and sign == '+' and num2 == 18:
        return("6+18 = 24")
    if num1 == 6 and sign == '+' and num2 == 19:
        return("6+19 = 25")
    if num1 == 6 and sign == '+' and num2 == 20:
        return("6+20 = 26")
    if num1 == 6 and sign == '+' and num2 == 21:
        return("6+21 = 27")
    if num1 == 6 and sign == '+' and num2 == 22:
        return("6+22 = 28")
    if num1 == 6 and sign == '+' and num2 == 23:
        return("6+23 = 29")
    if num1 == 6 and sign == '+' and num2 == 24:
        return("6+24 = 30")
    if num1 == 6 and sign == '+' and num2 == 25:
        return("6+25 = 31")
    if num1 == 6 and sign == '+' and num2 == 26:
        return("6+26 = 32")
    if num1 == 6 and sign == '+' and num2 == 27:
        return("6+27 = 33")
    if num1 == 6 and sign == '+' and num2 == 28:
        return("6+28 = 34")
    if num1 == 6 and sign == '+' and num2 == 29:
        return("6+29 = 35")
    if num1 == 6 and sign == '+' and num2 == 30:
        return("6+30 = 36")
    if num1 == 6 and sign == '+' and num2 == 31:
        return("6+31 = 37")
    if num1 == 6 and sign == '+' and num2 == 32:
        return("6+32 = 38")
    if num1 == 6 and sign == '+' and num2 == 33:
        return("6+33 = 39")
    if num1 == 6 and sign == '+' and num2 == 34:
        return("6+34 = 40")
    if num1 == 6 and sign == '+' and num2 == 35:
        return("6+35 = 41")
    if num1 == 6 and sign == '+' and num2 == 36:
        return("6+36 = 42")
    if num1 == 6 and sign == '+' and num2 == 37:
        return("6+37 = 43")
    if num1 == 6 and sign == '+' and num2 == 38:
        return("6+38 = 44")
    if num1 == 6 and sign == '+' and num2 == 39:
        return("6+39 = 45")
    if num1 == 6 and sign == '+' and num2 == 40:
        return("6+40 = 46")
    if num1 == 6 and sign == '+' and num2 == 41:
        return("6+41 = 47")
    if num1 == 6 and sign == '+' and num2 == 42:
        return("6+42 = 48")
    if num1 == 6 and sign == '+' and num2 == 43:
        return("6+43 = 49")
    if num1 == 6 and sign == '+' and num2 == 44:
        return("6+44 = 50")
    if num1 == 6 and sign == '+' and num2 == 45:
        return("6+45 = 51")
    if num1 == 6 and sign == '+' and num2 == 46:
        return("6+46 = 52")
    if num1 == 6 and sign == '+' and num2 == 47:
        return("6+47 = 53")
    if num1 == 6 and sign == '+' and num2 == 48:
        return("6+48 = 54")
    if num1 == 6 and sign == '+' and num2 == 49:
        return("6+49 = 55")
    if num1 == 6 and sign == '+' and num2 == 50:
        return("6+50 = 56")
    if num1 == 7 and sign == '+' and num2 == 0:
        return("7+0 = 7")
    if num1 == 7 and sign == '+' and num2 == 1:
        return("7+1 = 8")
    if num1 == 7 and sign == '+' and num2 == 2:
        return("7+2 = 9")
    if num1 == 7 and sign == '+' and num2 == 3:
        return("7+3 = 10")
    if num1 == 7 and sign == '+' and num2 == 4:
        return("7+4 = 11")
    if num1 == 7 and sign == '+' and num2 == 5:
        return("7+5 = 12")
    if num1 == 7 and sign == '+' and num2 == 6:
        return("7+6 = 13")
    if num1 == 7 and sign == '+' and num2 == 7:
        return("7+7 = 14")
    if num1 == 7 and sign == '+' and num2 == 8:
        return("7+8 = 15")
    if num1 == 7 and sign == '+' and num2 == 9:
        return("7+9 = 16")
    if num1 == 7 and sign == '+' and num2 == 10:
        return("7+10 = 17")
    if num1 == 7 and sign == '+' and num2 == 11:
        return("7+11 = 18")
    if num1 == 7 and sign == '+' and num2 == 12:
        return("7+12 = 19")
    if num1 == 7 and sign == '+' and num2 == 13:
        return("7+13 = 20")
    if num1 == 7 and sign == '+' and num2 == 14:
        return("7+14 = 21")
    if num1 == 7 and sign == '+' and num2 == 15:
        return("7+15 = 22")
    if num1 == 7 and sign == '+' and num2 == 16:
        return("7+16 = 23")
    if num1 == 7 and sign == '+' and num2 == 17:
        return("7+17 = 24")
    if num1 == 7 and sign == '+' and num2 == 18:
        return("7+18 = 25")
    if num1 == 7 and sign == '+' and num2 == 19:
        return("7+19 = 26")
    if num1 == 7 and sign == '+' and num2 == 20:
        return("7+20 = 27")
    if num1 == 7 and sign == '+' and num2 == 21:
        return("7+21 = 28")
    if num1 == 7 and sign == '+' and num2 == 22:
        return("7+22 = 29")
    if num1 == 7 and sign == '+' and num2 == 23:
        return("7+23 = 30")
    if num1 == 7 and sign == '+' and num2 == 24:
        return("7+24 = 31")
    if num1 == 7 and sign == '+' and num2 == 25:
        return("7+25 = 32")
    if num1 == 7 and sign == '+' and num2 == 26:
        return("7+26 = 33")
    if num1 == 7 and sign == '+' and num2 == 27:
        return("7+27 = 34")
    if num1 == 7 and sign == '+' and num2 == 28:
        return("7+28 = 35")
    if num1 == 7 and sign == '+' and num2 == 29:
        return("7+29 = 36")
    if num1 == 7 and sign == '+' and num2 == 30:
        return("7+30 = 37")
    if num1 == 7 and sign == '+' and num2 == 31:
        return("7+31 = 38")
    if num1 == 7 and sign == '+' and num2 == 32:
        return("7+32 = 39")
    if num1 == 7 and sign == '+' and num2 == 33:
        return("7+33 = 40")
    if num1 == 7 and sign == '+' and num2 == 34:
        return("7+34 = 41")
    if num1 == 7 and sign == '+' and num2 == 35:
        return("7+35 = 42")
    if num1 == 7 and sign == '+' and num2 == 36:
        return("7+36 = 43")
    if num1 == 7 and sign == '+' and num2 == 37:
        return("7+37 = 44")
    if num1 == 7 and sign == '+' and num2 == 38:
        return("7+38 = 45")
    if num1 == 7 and sign == '+' and num2 == 39:
        return("7+39 = 46")
    if num1 == 7 and sign == '+' and num2 == 40:
        return("7+40 = 47")
    if num1 == 7 and sign == '+' and num2 == 41:
        return("7+41 = 48")
    if num1 == 7 and sign == '+' and num2 == 42:
        return("7+42 = 49")
    if num1 == 7 and sign == '+' and num2 == 43:
        return("7+43 = 50")
    if num1 == 7 and sign == '+' and num2 == 44:
        return("7+44 = 51")
    if num1 == 7 and sign == '+' and num2 == 45:
        return("7+45 = 52")
    if num1 == 7 and sign == '+' and num2 == 46:
        return("7+46 = 53")
    if num1 == 7 and sign == '+' and num2 == 47:
        return("7+47 = 54")
    if num1 == 7 and sign == '+' and num2 == 48:
        return("7+48 = 55")
    if num1 == 7 and sign == '+' and num2 == 49:
        return("7+49 = 56")
    if num1 == 7 and sign == '+' and num2 == 50:
        return("7+50 = 57")
    if num1 == 8 and sign == '+' and num2 == 0:
        return("8+0 = 8")
    if num1 == 8 and sign == '+' and num2 == 1:
        return("8+1 = 9")
    if num1 == 8 and sign == '+' and num2 == 2:
        return("8+2 = 10")
    if num1 == 8 and sign == '+' and num2 == 3:
        return("8+3 = 11")
    if num1 == 8 and sign == '+' and num2 == 4:
        return("8+4 = 12")
    if num1 == 8 and sign == '+' and num2 == 5:
        return("8+5 = 13")
    if num1 == 8 and sign == '+' and num2 == 6:
        return("8+6 = 14")
    if num1 == 8 and sign == '+' and num2 == 7:
        return("8+7 = 15")
    if num1 == 8 and sign == '+' and num2 == 8:
        return("8+8 = 16")
    if num1 == 8 and sign == '+' and num2 == 9:
        return("8+9 = 17")
    if num1 == 8 and sign == '+' and num2 == 10:
        return("8+10 = 18")
    if num1 == 8 and sign == '+' and num2 == 11:
        return("8+11 = 19")
    if num1 == 8 and sign == '+' and num2 == 12:
        return("8+12 = 20")
    if num1 == 8 and sign == '+' and num2 == 13:
        return("8+13 = 21")
    if num1 == 8 and sign == '+' and num2 == 14:
        return("8+14 = 22")
    if num1 == 8 and sign == '+' and num2 == 15:
        return("8+15 = 23")
    if num1 == 8 and sign == '+' and num2 == 16:
        return("8+16 = 24")
    if num1 == 8 and sign == '+' and num2 == 17:
        return("8+17 = 25")
    if num1 == 8 and sign == '+' and num2 == 18:
        return("8+18 = 26")
    if num1 == 8 and sign == '+' and num2 == 19:
        return("8+19 = 27")
    if num1 == 8 and sign == '+' and num2 == 20:
        return("8+20 = 28")
    if num1 == 8 and sign == '+' and num2 == 21:
        return("8+21 = 29")
    if num1 == 8 and sign == '+' and num2 == 22:
        return("8+22 = 30")
    if num1 == 8 and sign == '+' and num2 == 23:
        return("8+23 = 31")
    if num1 == 8 and sign == '+' and num2 == 24:
        return("8+24 = 32")
    if num1 == 8 and sign == '+' and num2 == 25:
        return("8+25 = 33")
    if num1 == 8 and sign == '+' and num2 == 26:
        return("8+26 = 34")
    if num1 == 8 and sign == '+' and num2 == 27:
        return("8+27 = 35")
    if num1 == 8 and sign == '+' and num2 == 28:
        return("8+28 = 36")
    if num1 == 8 and sign == '+' and num2 == 29:
        return("8+29 = 37")
    if num1 == 8 and sign == '+' and num2 == 30:
        return("8+30 = 38")
    if num1 == 8 and sign == '+' and num2 == 31:
        return("8+31 = 39")
    if num1 == 8 and sign == '+' and num2 == 32:
        return("8+32 = 40")
    if num1 == 8 and sign == '+' and num2 == 33:
        return("8+33 = 41")
    if num1 == 8 and sign == '+' and num2 == 34:
        return("8+34 = 42")
    if num1 == 8 and sign == '+' and num2 == 35:
        return("8+35 = 43")
    if num1 == 8 and sign == '+' and num2 == 36:
        return("8+36 = 44")
    if num1 == 8 and sign == '+' and num2 == 37:
        return("8+37 = 45")
    if num1 == 8 and sign == '+' and num2 == 38:
        return("8+38 = 46")
    if num1 == 8 and sign == '+' and num2 == 39:
        return("8+39 = 47")
    if num1 == 8 and sign == '+' and num2 == 40:
        return("8+40 = 48")
    if num1 == 8 and sign == '+' and num2 == 41:
        return("8+41 = 49")
    if num1 == 8 and sign == '+' and num2 == 42:
        return("8+42 = 50")
    if num1 == 8 and sign == '+' and num2 == 43:
        return("8+43 = 51")
    if num1 == 8 and sign == '+' and num2 == 44:
        return("8+44 = 52")
    if num1 == 8 and sign == '+' and num2 == 45:
        return("8+45 = 53")
    if num1 == 8 and sign == '+' and num2 == 46:
        return("8+46 = 54")
    if num1 == 8 and sign == '+' and num2 == 47:
        return("8+47 = 55")
    if num1 == 8 and sign == '+' and num2 == 48:
        return("8+48 = 56")
    if num1 == 8 and sign == '+' and num2 == 49:
        return("8+49 = 57")
    if num1 == 8 and sign == '+' and num2 == 50:
        return("8+50 = 58")
    if num1 == 9 and sign == '+' and num2 == 0:
        return("9+0 = 9")
    if num1 == 9 and sign == '+' and num2 == 1:
        return("9+1 = 10")
    if num1 == 9 and sign == '+' and num2 == 2:
        return("9+2 = 11")
    if num1 == 9 and sign == '+' and num2 == 3:
        return("9+3 = 12")
    if num1 == 9 and sign == '+' and num2 == 4:
        return("9+4 = 13")
    if num1 == 9 and sign == '+' and num2 == 5:
        return("9+5 = 14")
    if num1 == 9 and sign == '+' and num2 == 6:
        return("9+6 = 15")
    if num1 == 9 and sign == '+' and num2 == 7:
        return("9+7 = 16")
    if num1 == 9 and sign == '+' and num2 == 8:
        return("9+8 = 17")
    if num1 == 9 and sign == '+' and num2 == 9:
        return("9+9 = 18")
    if num1 == 9 and sign == '+' and num2 == 10:
        return("9+10 = 19")
    if num1 == 9 and sign == '+' and num2 == 11:
        return("9+11 = 20")
    if num1 == 9 and sign == '+' and num2 == 12:
        return("9+12 = 21")
    if num1 == 9 and sign == '+' and num2 == 13:
        return("9+13 = 22")
    if num1 == 9 and sign == '+' and num2 == 14:
        return("9+14 = 23")
    if num1 == 9 and sign == '+' and num2 == 15:
        return("9+15 = 24")
    if num1 == 9 and sign == '+' and num2 == 16:
        return("9+16 = 25")
    if num1 == 9 and sign == '+' and num2 == 17:
        return("9+17 = 26")
    if num1 == 9 and sign == '+' and num2 == 18:
        return("9+18 = 27")
    if num1 == 9 and sign == '+' and num2 == 19:
        return("9+19 = 28")
    if num1 == 9 and sign == '+' and num2 == 20:
        return("9+20 = 29")
    if num1 == 9 and sign == '+' and num2 == 21:
        return("9+21 = 30")
    if num1 == 9 and sign == '+' and num2 == 22:
        return("9+22 = 31")
    if num1 == 9 and sign == '+' and num2 == 23:
        return("9+23 = 32")
    if num1 == 9 and sign == '+' and num2 == 24:
        return("9+24 = 33")
    if num1 == 9 and sign == '+' and num2 == 25:
        return("9+25 = 34")
    if num1 == 9 and sign == '+' and num2 == 26:
        return("9+26 = 35")
    if num1 == 9 and sign == '+' and num2 == 27:
        return("9+27 = 36")
    if num1 == 9 and sign == '+' and num2 == 28:
        return("9+28 = 37")
    if num1 == 9 and sign == '+' and num2 == 29:
        return("9+29 = 38")
    if num1 == 9 and sign == '+' and num2 == 30:
        return("9+30 = 39")
    if num1 == 9 and sign == '+' and num2 == 31:
        return("9+31 = 40")
    if num1 == 9 and sign == '+' and num2 == 32:
        return("9+32 = 41")
    if num1 == 9 and sign == '+' and num2 == 33:
        return("9+33 = 42")
    if num1 == 9 and sign == '+' and num2 == 34:
        return("9+34 = 43")
    if num1 == 9 and sign == '+' and num2 == 35:
        return("9+35 = 44")
    if num1 == 9 and sign == '+' and num2 == 36:
        return("9+36 = 45")
    if num1 == 9 and sign == '+' and num2 == 37:
        return("9+37 = 46")
    if num1 == 9 and sign == '+' and num2 == 38:
        return("9+38 = 47")
    if num1 == 9 and sign == '+' and num2 == 39:
        return("9+39 = 48")
    if num1 == 9 and sign == '+' and num2 == 40:
        return("9+40 = 49")
    if num1 == 9 and sign == '+' and num2 == 41:
        return("9+41 = 50")
    if num1 == 9 and sign == '+' and num2 == 42:
        return("9+42 = 51")
    if num1 == 9 and sign == '+' and num2 == 43:
        return("9+43 = 52")
    if num1 == 9 and sign == '+' and num2 == 44:
        return("9+44 = 53")
    if num1 == 9 and sign == '+' and num2 == 45:
        return("9+45 = 54")
    if num1 == 9 and sign == '+' and num2 == 46:
        return("9+46 = 55")
    if num1 == 9 and sign == '+' and num2 == 47:
        return("9+47 = 56")
    if num1 == 9 and sign == '+' and num2 == 48:
        return("9+48 = 57")
    if num1 == 9 and sign == '+' and num2 == 49:
        return("9+49 = 58")
    if num1 == 9 and sign == '+' and num2 == 50:
        return("9+50 = 59")
    if num1 == 10 and sign == '+' and num2 == 0:
        return("10+0 = 10")
    if num1 == 10 and sign == '+' and num2 == 1:
        return("10+1 = 11")
    if num1 == 10 and sign == '+' and num2 == 2:
        return("10+2 = 12")
    if num1 == 10 and sign == '+' and num2 == 3:
        return("10+3 = 13")
    if num1 == 10 and sign == '+' and num2 == 4:
        return("10+4 = 14")
    if num1 == 10 and sign == '+' and num2 == 5:
        return("10+5 = 15")
    if num1 == 10 and sign == '+' and num2 == 6:
        return("10+6 = 16")
    if num1 == 10 and sign == '+' and num2 == 7:
        return("10+7 = 17")
    if num1 == 10 and sign == '+' and num2 == 8:
        return("10+8 = 18")
    if num1 == 10 and sign == '+' and num2 == 9:
        return("10+9 = 19")
    if num1 == 10 and sign == '+' and num2 == 10:
        return("10+10 = 20")
    if num1 == 10 and sign == '+' and num2 == 11:
        return("10+11 = 21")
    if num1 == 10 and sign == '+' and num2 == 12:
        return("10+12 = 22")
    if num1 == 10 and sign == '+' and num2 == 13:
        return("10+13 = 23")
    if num1 == 10 and sign == '+' and num2 == 14:
        return("10+14 = 24")
    if num1 == 10 and sign == '+' and num2 == 15:
        return("10+15 = 25")
    if num1 == 10 and sign == '+' and num2 == 16:
        return("10+16 = 26")
    if num1 == 10 and sign == '+' and num2 == 17:
        return("10+17 = 27")
    if num1 == 10 and sign == '+' and num2 == 18:
        return("10+18 = 28")
    if num1 == 10 and sign == '+' and num2 == 19:
        return("10+19 = 29")
    if num1 == 10 and sign == '+' and num2 == 20:
        return("10+20 = 30")
    if num1 == 10 and sign == '+' and num2 == 21:
        return("10+21 = 31")
    if num1 == 10 and sign == '+' and num2 == 22:
        return("10+22 = 32")
    if num1 == 10 and sign == '+' and num2 == 23:
        return("10+23 = 33")
    if num1 == 10 and sign == '+' and num2 == 24:
        return("10+24 = 34")
    if num1 == 10 and sign == '+' and num2 == 25:
        return("10+25 = 35")
    if num1 == 10 and sign == '+' and num2 == 26:
        return("10+26 = 36")
    if num1 == 10 and sign == '+' and num2 == 27:
        return("10+27 = 37")
    if num1 == 10 and sign == '+' and num2 == 28:
        return("10+28 = 38")
    if num1 == 10 and sign == '+' and num2 == 29:
        return("10+29 = 39")
    if num1 == 10 and sign == '+' and num2 == 30:
        return("10+30 = 40")
    if num1 == 10 and sign == '+' and num2 == 31:
        return("10+31 = 41")
    if num1 == 10 and sign == '+' and num2 == 32:
        return("10+32 = 42")
    if num1 == 10 and sign == '+' and num2 == 33:
        return("10+33 = 43")
    if num1 == 10 and sign == '+' and num2 == 34:
        return("10+34 = 44")
    if num1 == 10 and sign == '+' and num2 == 35:
        return("10+35 = 45")
    if num1 == 10 and sign == '+' and num2 == 36:
        return("10+36 = 46")
    if num1 == 10 and sign == '+' and num2 == 37:
        return("10+37 = 47")
    if num1 == 10 and sign == '+' and num2 == 38:
        return("10+38 = 48")
    if num1 == 10 and sign == '+' and num2 == 39:
        return("10+39 = 49")
    if num1 == 10 and sign == '+' and num2 == 40:
        return("10+40 = 50")
    if num1 == 10 and sign == '+' and num2 == 41:
        return("10+41 = 51")
    if num1 == 10 and sign == '+' and num2 == 42:
        return("10+42 = 52")
    if num1 == 10 and sign == '+' and num2 == 43:
        return("10+43 = 53")
    if num1 == 10 and sign == '+' and num2 == 44:
        return("10+44 = 54")
    if num1 == 10 and sign == '+' and num2 == 45:
        return("10+45 = 55")
    if num1 == 10 and sign == '+' and num2 == 46:
        return("10+46 = 56")
    if num1 == 10 and sign == '+' and num2 == 47:
        return("10+47 = 57")
    if num1 == 10 and sign == '+' and num2 == 48:
        return("10+48 = 58")
    if num1 == 10 and sign == '+' and num2 == 49:
        return("10+49 = 59")
    if num1 == 10 and sign == '+' and num2 == 50:
        return("10+50 = 60")
    if num1 == 11 and sign == '+' and num2 == 0:
        return("11+0 = 11")
    if num1 == 11 and sign == '+' and num2 == 1:
        return("11+1 = 12")
    if num1 == 11 and sign == '+' and num2 == 2:
        return("11+2 = 13")
    if num1 == 11 and sign == '+' and num2 == 3:
        return("11+3 = 14")
    if num1 == 11 and sign == '+' and num2 == 4:
        return("11+4 = 15")
    if num1 == 11 and sign == '+' and num2 == 5:
        return("11+5 = 16")
    if num1 == 11 and sign == '+' and num2 == 6:
        return("11+6 = 17")
    if num1 == 11 and sign == '+' and num2 == 7:
        return("11+7 = 18")
    if num1 == 11 and sign == '+' and num2 == 8:
        return("11+8 = 19")
    if num1 == 11 and sign == '+' and num2 == 9:
        return("11+9 = 20")
    if num1 == 11 and sign == '+' and num2 == 10:
        return("11+10 = 21")
    if num1 == 11 and sign == '+' and num2 == 11:
        return("11+11 = 22")
    if num1 == 11 and sign == '+' and num2 == 12:
        return("11+12 = 23")
    if num1 == 11 and sign == '+' and num2 == 13:
        return("11+13 = 24")
    if num1 == 11 and sign == '+' and num2 == 14:
        return("11+14 = 25")
    if num1 == 11 and sign == '+' and num2 == 15:
        return("11+15 = 26")
    if num1 == 11 and sign == '+' and num2 == 16:
        return("11+16 = 27")
    if num1 == 11 and sign == '+' and num2 == 17:
        return("11+17 = 28")
    if num1 == 11 and sign == '+' and num2 == 18:
        return("11+18 = 29")
    if num1 == 11 and sign == '+' and num2 == 19:
        return("11+19 = 30")
    if num1 == 11 and sign == '+' and num2 == 20:
        return("11+20 = 31")
    if num1 == 11 and sign == '+' and num2 == 21:
        return("11+21 = 32")
    if num1 == 11 and sign == '+' and num2 == 22:
        return("11+22 = 33")
    if num1 == 11 and sign == '+' and num2 == 23:
        return("11+23 = 34")
    if num1 == 11 and sign == '+' and num2 == 24:
        return("11+24 = 35")
    if num1 == 11 and sign == '+' and num2 == 25:
        return("11+25 = 36")
    if num1 == 11 and sign == '+' and num2 == 26:
        return("11+26 = 37")
    if num1 == 11 and sign == '+' and num2 == 27:
        return("11+27 = 38")
    if num1 == 11 and sign == '+' and num2 == 28:
        return("11+28 = 39")
    if num1 == 11 and sign == '+' and num2 == 29:
        return("11+29 = 40")
    if num1 == 11 and sign == '+' and num2 == 30:
        return("11+30 = 41")
    if num1 == 11 and sign == '+' and num2 == 31:
        return("11+31 = 42")
    if num1 == 11 and sign == '+' and num2 == 32:
        return("11+32 = 43")
    if num1 == 11 and sign == '+' and num2 == 33:
        return("11+33 = 44")
    if num1 == 11 and sign == '+' and num2 == 34:
        return("11+34 = 45")
    if num1 == 11 and sign == '+' and num2 == 35:
        return("11+35 = 46")
    if num1 == 11 and sign == '+' and num2 == 36:
        return("11+36 = 47")
    if num1 == 11 and sign == '+' and num2 == 37:
        return("11+37 = 48")
    if num1 == 11 and sign == '+' and num2 == 38:
        return("11+38 = 49")
    if num1 == 11 and sign == '+' and num2 == 39:
        return("11+39 = 50")
    if num1 == 11 and sign == '+' and num2 == 40:
        return("11+40 = 51")
    if num1 == 11 and sign == '+' and num2 == 41:
        return("11+41 = 52")
    if num1 == 11 and sign == '+' and num2 == 42:
        return("11+42 = 53")
    if num1 == 11 and sign == '+' and num2 == 43:
        return("11+43 = 54")
    if num1 == 11 and sign == '+' and num2 == 44:
        return("11+44 = 55")
    if num1 == 11 and sign == '+' and num2 == 45:
        return("11+45 = 56")
    if num1 == 11 and sign == '+' and num2 == 46:
        return("11+46 = 57")
    if num1 == 11 and sign == '+' and num2 == 47:
        return("11+47 = 58")
    if num1 == 11 and sign == '+' and num2 == 48:
        return("11+48 = 59")
    if num1 == 11 and sign == '+' and num2 == 49:
        return("11+49 = 60")
    if num1 == 11 and sign == '+' and num2 == 50:
        return("11+50 = 61")
    if num1 == 12 and sign == '+' and num2 == 0:
        return("12+0 = 12")
    if num1 == 12 and sign == '+' and num2 == 1:
        return("12+1 = 13")
    if num1 == 12 and sign == '+' and num2 == 2:
        return("12+2 = 14")
    if num1 == 12 and sign == '+' and num2 == 3:
        return("12+3 = 15")
    if num1 == 12 and sign == '+' and num2 == 4:
        return("12+4 = 16")
    if num1 == 12 and sign == '+' and num2 == 5:
        return("12+5 = 17")
    if num1 == 12 and sign == '+' and num2 == 6:
        return("12+6 = 18")
    if num1 == 12 and sign == '+' and num2 == 7:
        return("12+7 = 19")
    if num1 == 12 and sign == '+' and num2 == 8:
        return("12+8 = 20")
    if num1 == 12 and sign == '+' and num2 == 9:
        return("12+9 = 21")
    if num1 == 12 and sign == '+' and num2 == 10:
        return("12+10 = 22")
    if num1 == 12 and sign == '+' and num2 == 11:
        return("12+11 = 23")
    if num1 == 12 and sign == '+' and num2 == 12:
        return("12+12 = 24")
    if num1 == 12 and sign == '+' and num2 == 13:
        return("12+13 = 25")
    if num1 == 12 and sign == '+' and num2 == 14:
        return("12+14 = 26")
    if num1 == 12 and sign == '+' and num2 == 15:
        return("12+15 = 27")
    if num1 == 12 and sign == '+' and num2 == 16:
        return("12+16 = 28")
    if num1 == 12 and sign == '+' and num2 == 17:
        return("12+17 = 29")
    if num1 == 12 and sign == '+' and num2 == 18:
        return("12+18 = 30")
    if num1 == 12 and sign == '+' and num2 == 19:
        return("12+19 = 31")
    if num1 == 12 and sign == '+' and num2 == 20:
        return("12+20 = 32")
    if num1 == 12 and sign == '+' and num2 == 21:
        return("12+21 = 33")
    if num1 == 12 and sign == '+' and num2 == 22:
        return("12+22 = 34")
    if num1 == 12 and sign == '+' and num2 == 23:
        return("12+23 = 35")
    if num1 == 12 and sign == '+' and num2 == 24:
        return("12+24 = 36")
    if num1 == 12 and sign == '+' and num2 == 25:
        return("12+25 = 37")
    if num1 == 12 and sign == '+' and num2 == 26:
        return("12+26 = 38")
    if num1 == 12 and sign == '+' and num2 == 27:
        return("12+27 = 39")
    if num1 == 12 and sign == '+' and num2 == 28:
        return("12+28 = 40")
    if num1 == 12 and sign == '+' and num2 == 29:
        return("12+29 = 41")
    if num1 == 12 and sign == '+' and num2 == 30:
        return("12+30 = 42")
    if num1 == 12 and sign == '+' and num2 == 31:
        return("12+31 = 43")
    if num1 == 12 and sign == '+' and num2 == 32:
        return("12+32 = 44")
    if num1 == 12 and sign == '+' and num2 == 33:
        return("12+33 = 45")
    if num1 == 12 and sign == '+' and num2 == 34:
        return("12+34 = 46")
    if num1 == 12 and sign == '+' and num2 == 35:
        return("12+35 = 47")
    if num1 == 12 and sign == '+' and num2 == 36:
        return("12+36 = 48")
    if num1 == 12 and sign == '+' and num2 == 37:
        return("12+37 = 49")
    if num1 == 12 and sign == '+' and num2 == 38:
        return("12+38 = 50")
    if num1 == 12 and sign == '+' and num2 == 39:
        return("12+39 = 51")
    if num1 == 12 and sign == '+' and num2 == 40:
        return("12+40 = 52")
    if num1 == 12 and sign == '+' and num2 == 41:
        return("12+41 = 53")
    if num1 == 12 and sign == '+' and num2 == 42:
        return("12+42 = 54")
    if num1 == 12 and sign == '+' and num2 == 43:
        return("12+43 = 55")
    if num1 == 12 and sign == '+' and num2 == 44:
        return("12+44 = 56")
    if num1 == 12 and sign == '+' and num2 == 45:
        return("12+45 = 57")
    if num1 == 12 and sign == '+' and num2 == 46:
        return("12+46 = 58")
    if num1 == 12 and sign == '+' and num2 == 47:
        return("12+47 = 59")
    if num1 == 12 and sign == '+' and num2 == 48:
        return("12+48 = 60")
    if num1 == 12 and sign == '+' and num2 == 49:
        return("12+49 = 61")
    if num1 == 12 and sign == '+' and num2 == 50:
        return("12+50 = 62")
    if num1 == 13 and sign == '+' and num2 == 0:
        return("13+0 = 13")
    if num1 == 13 and sign == '+' and num2 == 1:
        return("13+1 = 14")
    if num1 == 13 and sign == '+' and num2 == 2:
        return("13+2 = 15")
    if num1 == 13 and sign == '+' and num2 == 3:
        return("13+3 = 16")
    if num1 == 13 and sign == '+' and num2 == 4:
        return("13+4 = 17")
    if num1 == 13 and sign == '+' and num2 == 5:
        return("13+5 = 18")
    if num1 == 13 and sign == '+' and num2 == 6:
        return("13+6 = 19")
    if num1 == 13 and sign == '+' and num2 == 7:
        return("13+7 = 20")
    if num1 == 13 and sign == '+' and num2 == 8:
        return("13+8 = 21")
    if num1 == 13 and sign == '+' and num2 == 9:
        return("13+9 = 22")
    if num1 == 13 and sign == '+' and num2 == 10:
        return("13+10 = 23")
    if num1 == 13 and sign == '+' and num2 == 11:
        return("13+11 = 24")
    if num1 == 13 and sign == '+' and num2 == 12:
        return("13+12 = 25")
    if num1 == 13 and sign == '+' and num2 == 13:
        return("13+13 = 26")
    if num1 == 13 and sign == '+' and num2 == 14:
        return("13+14 = 27")
    if num1 == 13 and sign == '+' and num2 == 15:
        return("13+15 = 28")
    if num1 == 13 and sign == '+' and num2 == 16:
        return("13+16 = 29")
    if num1 == 13 and sign == '+' and num2 == 17:
        return("13+17 = 30")
    if num1 == 13 and sign == '+' and num2 == 18:
        return("13+18 = 31")
    if num1 == 13 and sign == '+' and num2 == 19:
        return("13+19 = 32")
    if num1 == 13 and sign == '+' and num2 == 20:
        return("13+20 = 33")
    if num1 == 13 and sign == '+' and num2 == 21:
        return("13+21 = 34")
    if num1 == 13 and sign == '+' and num2 == 22:
        return("13+22 = 35")
    if num1 == 13 and sign == '+' and num2 == 23:
        return("13+23 = 36")
    if num1 == 13 and sign == '+' and num2 == 24:
        return("13+24 = 37")
    if num1 == 13 and sign == '+' and num2 == 25:
        return("13+25 = 38")
    if num1 == 13 and sign == '+' and num2 == 26:
        return("13+26 = 39")
    if num1 == 13 and sign == '+' and num2 == 27:
        return("13+27 = 40")
    if num1 == 13 and sign == '+' and num2 == 28:
        return("13+28 = 41")
    if num1 == 13 and sign == '+' and num2 == 29:
        return("13+29 = 42")
    if num1 == 13 and sign == '+' and num2 == 30:
        return("13+30 = 43")
    if num1 == 13 and sign == '+' and num2 == 31:
        return("13+31 = 44")
    if num1 == 13 and sign == '+' and num2 == 32:
        return("13+32 = 45")
    if num1 == 13 and sign == '+' and num2 == 33:
        return("13+33 = 46")
    if num1 == 13 and sign == '+' and num2 == 34:
        return("13+34 = 47")
    if num1 == 13 and sign == '+' and num2 == 35:
        return("13+35 = 48")
    if num1 == 13 and sign == '+' and num2 == 36:
        return("13+36 = 49")
    if num1 == 13 and sign == '+' and num2 == 37:
        return("13+37 = 50")
    if num1 == 13 and sign == '+' and num2 == 38:
        return("13+38 = 51")
    if num1 == 13 and sign == '+' and num2 == 39:
        return("13+39 = 52")
    if num1 == 13 and sign == '+' and num2 == 40:
        return("13+40 = 53")
    if num1 == 13 and sign == '+' and num2 == 41:
        return("13+41 = 54")
    if num1 == 13 and sign == '+' and num2 == 42:
        return("13+42 = 55")
    if num1 == 13 and sign == '+' and num2 == 43:
        return("13+43 = 56")
    if num1 == 13 and sign == '+' and num2 == 44:
        return("13+44 = 57")
    if num1 == 13 and sign == '+' and num2 == 45:
        return("13+45 = 58")
    if num1 == 13 and sign == '+' and num2 == 46:
        return("13+46 = 59")
    if num1 == 13 and sign == '+' and num2 == 47:
        return("13+47 = 60")
    if num1 == 13 and sign == '+' and num2 == 48:
        return("13+48 = 61")
    if num1 == 13 and sign == '+' and num2 == 49:
        return("13+49 = 62")
    if num1 == 13 and sign == '+' and num2 == 50:
        return("13+50 = 63")
    if num1 == 14 and sign == '+' and num2 == 0:
        return("14+0 = 14")
    if num1 == 14 and sign == '+' and num2 == 1:
        return("14+1 = 15")
    if num1 == 14 and sign == '+' and num2 == 2:
        return("14+2 = 16")
    if num1 == 14 and sign == '+' and num2 == 3:
        return("14+3 = 17")
    if num1 == 14 and sign == '+' and num2 == 4:
        return("14+4 = 18")
    if num1 == 14 and sign == '+' and num2 == 5:
        return("14+5 = 19")
    if num1 == 14 and sign == '+' and num2 == 6:
        return("14+6 = 20")
    if num1 == 14 and sign == '+' and num2 == 7:
        return("14+7 = 21")
    if num1 == 14 and sign == '+' and num2 == 8:
        return("14+8 = 22")
    if num1 == 14 and sign == '+' and num2 == 9:
        return("14+9 = 23")
    if num1 == 14 and sign == '+' and num2 == 10:
        return("14+10 = 24")
    if num1 == 14 and sign == '+' and num2 == 11:
        return("14+11 = 25")
    if num1 == 14 and sign == '+' and num2 == 12:
        return("14+12 = 26")
    if num1 == 14 and sign == '+' and num2 == 13:
        return("14+13 = 27")
    if num1 == 14 and sign == '+' and num2 == 14:
        return("14+14 = 28")
    if num1 == 14 and sign == '+' and num2 == 15:
        return("14+15 = 29")
    if num1 == 14 and sign == '+' and num2 == 16:
        return("14+16 = 30")
    if num1 == 14 and sign == '+' and num2 == 17:
        return("14+17 = 31")
    if num1 == 14 and sign == '+' and num2 == 18:
        return("14+18 = 32")
    if num1 == 14 and sign == '+' and num2 == 19:
        return("14+19 = 33")
    if num1 == 14 and sign == '+' and num2 == 20:
        return("14+20 = 34")
    if num1 == 14 and sign == '+' and num2 == 21:
        return("14+21 = 35")
    if num1 == 14 and sign == '+' and num2 == 22:
        return("14+22 = 36")
    if num1 == 14 and sign == '+' and num2 == 23:
        return("14+23 = 37")
    if num1 == 14 and sign == '+' and num2 == 24:
        return("14+24 = 38")
    if num1 == 14 and sign == '+' and num2 == 25:
        return("14+25 = 39")
    if num1 == 14 and sign == '+' and num2 == 26:
        return("14+26 = 40")
    if num1 == 14 and sign == '+' and num2 == 27:
        return("14+27 = 41")
    if num1 == 14 and sign == '+' and num2 == 28:
        return("14+28 = 42")
    if num1 == 14 and sign == '+' and num2 == 29:
        return("14+29 = 43")
    if num1 == 14 and sign == '+' and num2 == 30:
        return("14+30 = 44")
    if num1 == 14 and sign == '+' and num2 == 31:
        return("14+31 = 45")
    if num1 == 14 and sign == '+' and num2 == 32:
        return("14+32 = 46")
    if num1 == 14 and sign == '+' and num2 == 33:
        return("14+33 = 47")
    if num1 == 14 and sign == '+' and num2 == 34:
        return("14+34 = 48")
    if num1 == 14 and sign == '+' and num2 == 35:
        return("14+35 = 49")
    if num1 == 14 and sign == '+' and num2 == 36:
        return("14+36 = 50")
    if num1 == 14 and sign == '+' and num2 == 37:
        return("14+37 = 51")
    if num1 == 14 and sign == '+' and num2 == 38:
        return("14+38 = 52")
    if num1 == 14 and sign == '+' and num2 == 39:
        return("14+39 = 53")
    if num1 == 14 and sign == '+' and num2 == 40:
        return("14+40 = 54")
    if num1 == 14 and sign == '+' and num2 == 41:
        return("14+41 = 55")
    if num1 == 14 and sign == '+' and num2 == 42:
        return("14+42 = 56")
    if num1 == 14 and sign == '+' and num2 == 43:
        return("14+43 = 57")
    if num1 == 14 and sign == '+' and num2 == 44:
        return("14+44 = 58")
    if num1 == 14 and sign == '+' and num2 == 45:
        return("14+45 = 59")
    if num1 == 14 and sign == '+' and num2 == 46:
        return("14+46 = 60")
    if num1 == 14 and sign == '+' and num2 == 47:
        return("14+47 = 61")
    if num1 == 14 and sign == '+' and num2 == 48:
        return("14+48 = 62")
    if num1 == 14 and sign == '+' and num2 == 49:
        return("14+49 = 63")
    if num1 == 14 and sign == '+' and num2 == 50:
        return("14+50 = 64")
    if num1 == 15 and sign == '+' and num2 == 0:
        return("15+0 = 15")
    if num1 == 15 and sign == '+' and num2 == 1:
        return("15+1 = 16")
    if num1 == 15 and sign == '+' and num2 == 2:
        return("15+2 = 17")
    if num1 == 15 and sign == '+' and num2 == 3:
        return("15+3 = 18")
    if num1 == 15 and sign == '+' and num2 == 4:
        return("15+4 = 19")
    if num1 == 15 and sign == '+' and num2 == 5:
        return("15+5 = 20")
    if num1 == 15 and sign == '+' and num2 == 6:
        return("15+6 = 21")
    if num1 == 15 and sign == '+' and num2 == 7:
        return("15+7 = 22")
    if num1 == 15 and sign == '+' and num2 == 8:
        return("15+8 = 23")
    if num1 == 15 and sign == '+' and num2 == 9:
        return("15+9 = 24")
    if num1 == 15 and sign == '+' and num2 == 10:
        return("15+10 = 25")
    if num1 == 15 and sign == '+' and num2 == 11:
        return("15+11 = 26")
    if num1 == 15 and sign == '+' and num2 == 12:
        return("15+12 = 27")
    if num1 == 15 and sign == '+' and num2 == 13:
        return("15+13 = 28")
    if num1 == 15 and sign == '+' and num2 == 14:
        return("15+14 = 29")
    if num1 == 15 and sign == '+' and num2 == 15:
        return("15+15 = 30")
    if num1 == 15 and sign == '+' and num2 == 16:
        return("15+16 = 31")
    if num1 == 15 and sign == '+' and num2 == 17:
        return("15+17 = 32")
    if num1 == 15 and sign == '+' and num2 == 18:
        return("15+18 = 33")
    if num1 == 15 and sign == '+' and num2 == 19:
        return("15+19 = 34")
    if num1 == 15 and sign == '+' and num2 == 20:
        return("15+20 = 35")
    if num1 == 15 and sign == '+' and num2 == 21:
        return("15+21 = 36")
    if num1 == 15 and sign == '+' and num2 == 22:
        return("15+22 = 37")
    if num1 == 15 and sign == '+' and num2 == 23:
        return("15+23 = 38")
    if num1 == 15 and sign == '+' and num2 == 24:
        return("15+24 = 39")
    if num1 == 15 and sign == '+' and num2 == 25:
        return("15+25 = 40")
    if num1 == 15 and sign == '+' and num2 == 26:
        return("15+26 = 41")
    if num1 == 15 and sign == '+' and num2 == 27:
        return("15+27 = 42")
    if num1 == 15 and sign == '+' and num2 == 28:
        return("15+28 = 43")
    if num1 == 15 and sign == '+' and num2 == 29:
        return("15+29 = 44")
    if num1 == 15 and sign == '+' and num2 == 30:
        return("15+30 = 45")
    if num1 == 15 and sign == '+' and num2 == 31:
        return("15+31 = 46")
    if num1 == 15 and sign == '+' and num2 == 32:
        return("15+32 = 47")
    if num1 == 15 and sign == '+' and num2 == 33:
        return("15+33 = 48")
    if num1 == 15 and sign == '+' and num2 == 34:
        return("15+34 = 49")
    if num1 == 15 and sign == '+' and num2 == 35:
        return("15+35 = 50")
    if num1 == 15 and sign == '+' and num2 == 36:
        return("15+36 = 51")
    if num1 == 15 and sign == '+' and num2 == 37:
        return("15+37 = 52")
    if num1 == 15 and sign == '+' and num2 == 38:
        return("15+38 = 53")
    if num1 == 15 and sign == '+' and num2 == 39:
        return("15+39 = 54")
    if num1 == 15 and sign == '+' and num2 == 40:
        return("15+40 = 55")
    if num1 == 15 and sign == '+' and num2 == 41:
        return("15+41 = 56")
    if num1 == 15 and sign == '+' and num2 == 42:
        return("15+42 = 57")
    if num1 == 15 and sign == '+' and num2 == 43:
        return("15+43 = 58")
    if num1 == 15 and sign == '+' and num2 == 44:
        return("15+44 = 59")
    if num1 == 15 and sign == '+' and num2 == 45:
        return("15+45 = 60")
    if num1 == 15 and sign == '+' and num2 == 46:
        return("15+46 = 61")
    if num1 == 15 and sign == '+' and num2 == 47:
        return("15+47 = 62")
    if num1 == 15 and sign == '+' and num2 == 48:
        return("15+48 = 63")
    if num1 == 15 and sign == '+' and num2 == 49:
        return("15+49 = 64")
    if num1 == 15 and sign == '+' and num2 == 50:
        return("15+50 = 65")
    if num1 == 16 and sign == '+' and num2 == 0:
        return("16+0 = 16")
    if num1 == 16 and sign == '+' and num2 == 1:
        return("16+1 = 17")
    if num1 == 16 and sign == '+' and num2 == 2:
        return("16+2 = 18")
    if num1 == 16 and sign == '+' and num2 == 3:
        return("16+3 = 19")
    if num1 == 16 and sign == '+' and num2 == 4:
        return("16+4 = 20")
    if num1 == 16 and sign == '+' and num2 == 5:
        return("16+5 = 21")
    if num1 == 16 and sign == '+' and num2 == 6:
        return("16+6 = 22")
    if num1 == 16 and sign == '+' and num2 == 7:
        return("16+7 = 23")
    if num1 == 16 and sign == '+' and num2 == 8:
        return("16+8 = 24")
    if num1 == 16 and sign == '+' and num2 == 9:
        return("16+9 = 25")
    if num1 == 16 and sign == '+' and num2 == 10:
        return("16+10 = 26")
    if num1 == 16 and sign == '+' and num2 == 11:
        return("16+11 = 27")
    if num1 == 16 and sign == '+' and num2 == 12:
        return("16+12 = 28")
    if num1 == 16 and sign == '+' and num2 == 13:
        return("16+13 = 29")
    if num1 == 16 and sign == '+' and num2 == 14:
        return("16+14 = 30")
    if num1 == 16 and sign == '+' and num2 == 15:
        return("16+15 = 31")
    if num1 == 16 and sign == '+' and num2 == 16:
        return("16+16 = 32")
    if num1 == 16 and sign == '+' and num2 == 17:
        return("16+17 = 33")
    if num1 == 16 and sign == '+' and num2 == 18:
        return("16+18 = 34")
    if num1 == 16 and sign == '+' and num2 == 19:
        return("16+19 = 35")
    if num1 == 16 and sign == '+' and num2 == 20:
        return("16+20 = 36")
    if num1 == 16 and sign == '+' and num2 == 21:
        return("16+21 = 37")
    if num1 == 16 and sign == '+' and num2 == 22:
        return("16+22 = 38")
    if num1 == 16 and sign == '+' and num2 == 23:
        return("16+23 = 39")
    if num1 == 16 and sign == '+' and num2 == 24:
        return("16+24 = 40")
    if num1 == 16 and sign == '+' and num2 == 25:
        return("16+25 = 41")
    if num1 == 16 and sign == '+' and num2 == 26:
        return("16+26 = 42")
    if num1 == 16 and sign == '+' and num2 == 27:
        return("16+27 = 43")
    if num1 == 16 and sign == '+' and num2 == 28:
        return("16+28 = 44")
    if num1 == 16 and sign == '+' and num2 == 29:
        return("16+29 = 45")
    if num1 == 16 and sign == '+' and num2 == 30:
        return("16+30 = 46")
    if num1 == 16 and sign == '+' and num2 == 31:
        return("16+31 = 47")
    if num1 == 16 and sign == '+' and num2 == 32:
        return("16+32 = 48")
    if num1 == 16 and sign == '+' and num2 == 33:
        return("16+33 = 49")
    if num1 == 16 and sign == '+' and num2 == 34:
        return("16+34 = 50")
    if num1 == 16 and sign == '+' and num2 == 35:
        return("16+35 = 51")
    if num1 == 16 and sign == '+' and num2 == 36:
        return("16+36 = 52")
    if num1 == 16 and sign == '+' and num2 == 37:
        return("16+37 = 53")
    if num1 == 16 and sign == '+' and num2 == 38:
        return("16+38 = 54")
    if num1 == 16 and sign == '+' and num2 == 39:
        return("16+39 = 55")
    if num1 == 16 and sign == '+' and num2 == 40:
        return("16+40 = 56")
    if num1 == 16 and sign == '+' and num2 == 41:
        return("16+41 = 57")
    if num1 == 16 and sign == '+' and num2 == 42:
        return("16+42 = 58")
    if num1 == 16 and sign == '+' and num2 == 43:
        return("16+43 = 59")
    if num1 == 16 and sign == '+' and num2 == 44:
        return("16+44 = 60")
    if num1 == 16 and sign == '+' and num2 == 45:
        return("16+45 = 61")
    if num1 == 16 and sign == '+' and num2 == 46:
        return("16+46 = 62")
    if num1 == 16 and sign == '+' and num2 == 47:
        return("16+47 = 63")
    if num1 == 16 and sign == '+' and num2 == 48:
        return("16+48 = 64")
    if num1 == 16 and sign == '+' and num2 == 49:
        return("16+49 = 65")
    if num1 == 16 and sign == '+' and num2 == 50:
        return("16+50 = 66")
    if num1 == 17 and sign == '+' and num2 == 0:
        return("17+0 = 17")
    if num1 == 17 and sign == '+' and num2 == 1:
        return("17+1 = 18")
    if num1 == 17 and sign == '+' and num2 == 2:
        return("17+2 = 19")
    if num1 == 17 and sign == '+' and num2 == 3:
        return("17+3 = 20")
    if num1 == 17 and sign == '+' and num2 == 4:
        return("17+4 = 21")
    if num1 == 17 and sign == '+' and num2 == 5:
        return("17+5 = 22")
    if num1 == 17 and sign == '+' and num2 == 6:
        return("17+6 = 23")
    if num1 == 17 and sign == '+' and num2 == 7:
        return("17+7 = 24")
    if num1 == 17 and sign == '+' and num2 == 8:
        return("17+8 = 25")
    if num1 == 17 and sign == '+' and num2 == 9:
        return("17+9 = 26")
    if num1 == 17 and sign == '+' and num2 == 10:
        return("17+10 = 27")
    if num1 == 17 and sign == '+' and num2 == 11:
        return("17+11 = 28")
    if num1 == 17 and sign == '+' and num2 == 12:
        return("17+12 = 29")
    if num1 == 17 and sign == '+' and num2 == 13:
        return("17+13 = 30")
    if num1 == 17 and sign == '+' and num2 == 14:
        return("17+14 = 31")
    if num1 == 17 and sign == '+' and num2 == 15:
        return("17+15 = 32")
    if num1 == 17 and sign == '+' and num2 == 16:
        return("17+16 = 33")
    if num1 == 17 and sign == '+' and num2 == 17:
        return("17+17 = 34")
    if num1 == 17 and sign == '+' and num2 == 18:
        return("17+18 = 35")
    if num1 == 17 and sign == '+' and num2 == 19:
        return("17+19 = 36")
    if num1 == 17 and sign == '+' and num2 == 20:
        return("17+20 = 37")
    if num1 == 17 and sign == '+' and num2 == 21:
        return("17+21 = 38")
    if num1 == 17 and sign == '+' and num2 == 22:
        return("17+22 = 39")
    if num1 == 17 and sign == '+' and num2 == 23:
        return("17+23 = 40")
    if num1 == 17 and sign == '+' and num2 == 24:
        return("17+24 = 41")
    if num1 == 17 and sign == '+' and num2 == 25:
        return("17+25 = 42")
    if num1 == 17 and sign == '+' and num2 == 26:
        return("17+26 = 43")
    if num1 == 17 and sign == '+' and num2 == 27:
        return("17+27 = 44")
    if num1 == 17 and sign == '+' and num2 == 28:
        return("17+28 = 45")
    if num1 == 17 and sign == '+' and num2 == 29:
        return("17+29 = 46")
    if num1 == 17 and sign == '+' and num2 == 30:
        return("17+30 = 47")
    if num1 == 17 and sign == '+' and num2 == 31:
        return("17+31 = 48")
    if num1 == 17 and sign == '+' and num2 == 32:
        return("17+32 = 49")
    if num1 == 17 and sign == '+' and num2 == 33:
        return("17+33 = 50")
    if num1 == 17 and sign == '+' and num2 == 34:
        return("17+34 = 51")
    if num1 == 17 and sign == '+' and num2 == 35:
        return("17+35 = 52")
    if num1 == 17 and sign == '+' and num2 == 36:
        return("17+36 = 53")
    if num1 == 17 and sign == '+' and num2 == 37:
        return("17+37 = 54")
    if num1 == 17 and sign == '+' and num2 == 38:
        return("17+38 = 55")
    if num1 == 17 and sign == '+' and num2 == 39:
        return("17+39 = 56")
    if num1 == 17 and sign == '+' and num2 == 40:
        return("17+40 = 57")
    if num1 == 17 and sign == '+' and num2 == 41:
        return("17+41 = 58")
    if num1 == 17 and sign == '+' and num2 == 42:
        return("17+42 = 59")
    if num1 == 17 and sign == '+' and num2 == 43:
        return("17+43 = 60")
    if num1 == 17 and sign == '+' and num2 == 44:
        return("17+44 = 61")
    if num1 == 17 and sign == '+' and num2 == 45:
        return("17+45 = 62")
    if num1 == 17 and sign == '+' and num2 == 46:
        return("17+46 = 63")
    if num1 == 17 and sign == '+' and num2 == 47:
        return("17+47 = 64")
    if num1 == 17 and sign == '+' and num2 == 48:
        return("17+48 = 65")
    if num1 == 17 and sign == '+' and num2 == 49:
        return("17+49 = 66")
    if num1 == 17 and sign == '+' and num2 == 50:
        return("17+50 = 67")
    if num1 == 18 and sign == '+' and num2 == 0:
        return("18+0 = 18")
    if num1 == 18 and sign == '+' and num2 == 1:
        return("18+1 = 19")
    if num1 == 18 and sign == '+' and num2 == 2:
        return("18+2 = 20")
    if num1 == 18 and sign == '+' and num2 == 3:
        return("18+3 = 21")
    if num1 == 18 and sign == '+' and num2 == 4:
        return("18+4 = 22")
    if num1 == 18 and sign == '+' and num2 == 5:
        return("18+5 = 23")
    if num1 == 18 and sign == '+' and num2 == 6:
        return("18+6 = 24")
    if num1 == 18 and sign == '+' and num2 == 7:
        return("18+7 = 25")
    if num1 == 18 and sign == '+' and num2 == 8:
        return("18+8 = 26")
    if num1 == 18 and sign == '+' and num2 == 9:
        return("18+9 = 27")
    if num1 == 18 and sign == '+' and num2 == 10:
        return("18+10 = 28")
    if num1 == 18 and sign == '+' and num2 == 11:
        return("18+11 = 29")
    if num1 == 18 and sign == '+' and num2 == 12:
        return("18+12 = 30")
    if num1 == 18 and sign == '+' and num2 == 13:
        return("18+13 = 31")
    if num1 == 18 and sign == '+' and num2 == 14:
        return("18+14 = 32")
    if num1 == 18 and sign == '+' and num2 == 15:
        return("18+15 = 33")
    if num1 == 18 and sign == '+' and num2 == 16:
        return("18+16 = 34")
    if num1 == 18 and sign == '+' and num2 == 17:
        return("18+17 = 35")
    if num1 == 18 and sign == '+' and num2 == 18:
        return("18+18 = 36")
    if num1 == 18 and sign == '+' and num2 == 19:
        return("18+19 = 37")
    if num1 == 18 and sign == '+' and num2 == 20:
        return("18+20 = 38")
    if num1 == 18 and sign == '+' and num2 == 21:
        return("18+21 = 39")
    if num1 == 18 and sign == '+' and num2 == 22:
        return("18+22 = 40")
    if num1 == 18 and sign == '+' and num2 == 23:
        return("18+23 = 41")
    if num1 == 18 and sign == '+' and num2 == 24:
        return("18+24 = 42")
    if num1 == 18 and sign == '+' and num2 == 25:
        return("18+25 = 43")
    if num1 == 18 and sign == '+' and num2 == 26:
        return("18+26 = 44")
    if num1 == 18 and sign == '+' and num2 == 27:
        return("18+27 = 45")
    if num1 == 18 and sign == '+' and num2 == 28:
        return("18+28 = 46")
    if num1 == 18 and sign == '+' and num2 == 29:
        return("18+29 = 47")
    if num1 == 18 and sign == '+' and num2 == 30:
        return("18+30 = 48")
    if num1 == 18 and sign == '+' and num2 == 31:
        return("18+31 = 49")
    if num1 == 18 and sign == '+' and num2 == 32:
        return("18+32 = 50")
    if num1 == 18 and sign == '+' and num2 == 33:
        return("18+33 = 51")
    if num1 == 18 and sign == '+' and num2 == 34:
        return("18+34 = 52")
    if num1 == 18 and sign == '+' and num2 == 35:
        return("18+35 = 53")
    if num1 == 18 and sign == '+' and num2 == 36:
        return("18+36 = 54")
    if num1 == 18 and sign == '+' and num2 == 37:
        return("18+37 = 55")
    if num1 == 18 and sign == '+' and num2 == 38:
        return("18+38 = 56")
    if num1 == 18 and sign == '+' and num2 == 39:
        return("18+39 = 57")
    if num1 == 18 and sign == '+' and num2 == 40:
        return("18+40 = 58")
    if num1 == 18 and sign == '+' and num2 == 41:
        return("18+41 = 59")
    if num1 == 18 and sign == '+' and num2 == 42:
        return("18+42 = 60")
    if num1 == 18 and sign == '+' and num2 == 43:
        return("18+43 = 61")
    if num1 == 18 and sign == '+' and num2 == 44:
        return("18+44 = 62")
    if num1 == 18 and sign == '+' and num2 == 45:
        return("18+45 = 63")
    if num1 == 18 and sign == '+' and num2 == 46:
        return("18+46 = 64")
    if num1 == 18 and sign == '+' and num2 == 47:
        return("18+47 = 65")
    if num1 == 18 and sign == '+' and num2 == 48:
        return("18+48 = 66")
    if num1 == 18 and sign == '+' and num2 == 49:
        return("18+49 = 67")
    if num1 == 18 and sign == '+' and num2 == 50:
        return("18+50 = 68")
    if num1 == 19 and sign == '+' and num2 == 0:
        return("19+0 = 19")
    if num1 == 19 and sign == '+' and num2 == 1:
        return("19+1 = 20")
    if num1 == 19 and sign == '+' and num2 == 2:
        return("19+2 = 21")
    if num1 == 19 and sign == '+' and num2 == 3:
        return("19+3 = 22")
    if num1 == 19 and sign == '+' and num2 == 4:
        return("19+4 = 23")
    if num1 == 19 and sign == '+' and num2 == 5:
        return("19+5 = 24")
    if num1 == 19 and sign == '+' and num2 == 6:
        return("19+6 = 25")
    if num1 == 19 and sign == '+' and num2 == 7:
        return("19+7 = 26")
    if num1 == 19 and sign == '+' and num2 == 8:
        return("19+8 = 27")
    if num1 == 19 and sign == '+' and num2 == 9:
        return("19+9 = 28")
    if num1 == 19 and sign == '+' and num2 == 10:
        return("19+10 = 29")
    if num1 == 19 and sign == '+' and num2 == 11:
        return("19+11 = 30")
    if num1 == 19 and sign == '+' and num2 == 12:
        return("19+12 = 31")
    if num1 == 19 and sign == '+' and num2 == 13:
        return("19+13 = 32")
    if num1 == 19 and sign == '+' and num2 == 14:
        return("19+14 = 33")
    if num1 == 19 and sign == '+' and num2 == 15:
        return("19+15 = 34")
    if num1 == 19 and sign == '+' and num2 == 16:
        return("19+16 = 35")
    if num1 == 19 and sign == '+' and num2 == 17:
        return("19+17 = 36")
    if num1 == 19 and sign == '+' and num2 == 18:
        return("19+18 = 37")
    if num1 == 19 and sign == '+' and num2 == 19:
        return("19+19 = 38")
    if num1 == 19 and sign == '+' and num2 == 20:
        return("19+20 = 39")
    if num1 == 19 and sign == '+' and num2 == 21:
        return("19+21 = 40")
    if num1 == 19 and sign == '+' and num2 == 22:
        return("19+22 = 41")
    if num1 == 19 and sign == '+' and num2 == 23:
        return("19+23 = 42")
    if num1 == 19 and sign == '+' and num2 == 24:
        return("19+24 = 43")
    if num1 == 19 and sign == '+' and num2 == 25:
        return("19+25 = 44")
    if num1 == 19 and sign == '+' and num2 == 26:
        return("19+26 = 45")
    if num1 == 19 and sign == '+' and num2 == 27:
        return("19+27 = 46")
    if num1 == 19 and sign == '+' and num2 == 28:
        return("19+28 = 47")
    if num1 == 19 and sign == '+' and num2 == 29:
        return("19+29 = 48")
    if num1 == 19 and sign == '+' and num2 == 30:
        return("19+30 = 49")
    if num1 == 19 and sign == '+' and num2 == 31:
        return("19+31 = 50")
    if num1 == 19 and sign == '+' and num2 == 32:
        return("19+32 = 51")
    if num1 == 19 and sign == '+' and num2 == 33:
        return("19+33 = 52")
    if num1 == 19 and sign == '+' and num2 == 34:
        return("19+34 = 53")
    if num1 == 19 and sign == '+' and num2 == 35:
        return("19+35 = 54")
    if num1 == 19 and sign == '+' and num2 == 36:
        return("19+36 = 55")
    if num1 == 19 and sign == '+' and num2 == 37:
        return("19+37 = 56")
    if num1 == 19 and sign == '+' and num2 == 38:
        return("19+38 = 57")
    if num1 == 19 and sign == '+' and num2 == 39:
        return("19+39 = 58")
    if num1 == 19 and sign == '+' and num2 == 40:
        return("19+40 = 59")
    if num1 == 19 and sign == '+' and num2 == 41:
        return("19+41 = 60")
    if num1 == 19 and sign == '+' and num2 == 42:
        return("19+42 = 61")
    if num1 == 19 and sign == '+' and num2 == 43:
        return("19+43 = 62")
    if num1 == 19 and sign == '+' and num2 == 44:
        return("19+44 = 63")
    if num1 == 19 and sign == '+' and num2 == 45:
        return("19+45 = 64")
    if num1 == 19 and sign == '+' and num2 == 46:
        return("19+46 = 65")
    if num1 == 19 and sign == '+' and num2 == 47:
        return("19+47 = 66")
    if num1 == 19 and sign == '+' and num2 == 48:
        return("19+48 = 67")
    if num1 == 19 and sign == '+' and num2 == 49:
        return("19+49 = 68")
    if num1 == 19 and sign == '+' and num2 == 50:
        return("19+50 = 69")
    if num1 == 20 and sign == '+' and num2 == 0:
        return("20+0 = 20")
    if num1 == 20 and sign == '+' and num2 == 1:
        return("20+1 = 21")
    if num1 == 20 and sign == '+' and num2 == 2:
        return("20+2 = 22")
    if num1 == 20 and sign == '+' and num2 == 3:
        return("20+3 = 23")
    if num1 == 20 and sign == '+' and num2 == 4:
        return("20+4 = 24")
    if num1 == 20 and sign == '+' and num2 == 5:
        return("20+5 = 25")
    if num1 == 20 and sign == '+' and num2 == 6:
        return("20+6 = 26")
    if num1 == 20 and sign == '+' and num2 == 7:
        return("20+7 = 27")
    if num1 == 20 and sign == '+' and num2 == 8:
        return("20+8 = 28")
    if num1 == 20 and sign == '+' and num2 == 9:
        return("20+9 = 29")
    if num1 == 20 and sign == '+' and num2 == 10:
        return("20+10 = 30")
    if num1 == 20 and sign == '+' and num2 == 11:
        return("20+11 = 31")
    if num1 == 20 and sign == '+' and num2 == 12:
        return("20+12 = 32")
    if num1 == 20 and sign == '+' and num2 == 13:
        return("20+13 = 33")
    if num1 == 20 and sign == '+' and num2 == 14:
        return("20+14 = 34")
    if num1 == 20 and sign == '+' and num2 == 15:
        return("20+15 = 35")
    if num1 == 20 and sign == '+' and num2 == 16:
        return("20+16 = 36")
    if num1 == 20 and sign == '+' and num2 == 17:
        return("20+17 = 37")
    if num1 == 20 and sign == '+' and num2 == 18:
        return("20+18 = 38")
    if num1 == 20 and sign == '+' and num2 == 19:
        return("20+19 = 39")
    if num1 == 20 and sign == '+' and num2 == 20:
        return("20+20 = 40")
    if num1 == 20 and sign == '+' and num2 == 21:
        return("20+21 = 41")
    if num1 == 20 and sign == '+' and num2 == 22:
        return("20+22 = 42")
    if num1 == 20 and sign == '+' and num2 == 23:
        return("20+23 = 43")
    if num1 == 20 and sign == '+' and num2 == 24:
        return("20+24 = 44")
    if num1 == 20 and sign == '+' and num2 == 25:
        return("20+25 = 45")
    if num1 == 20 and sign == '+' and num2 == 26:
        return("20+26 = 46")
    if num1 == 20 and sign == '+' and num2 == 27:
        return("20+27 = 47")
    if num1 == 20 and sign == '+' and num2 == 28:
        return("20+28 = 48")
    if num1 == 20 and sign == '+' and num2 == 29:
        return("20+29 = 49")
    if num1 == 20 and sign == '+' and num2 == 30:
        return("20+30 = 50")
    if num1 == 20 and sign == '+' and num2 == 31:
        return("20+31 = 51")
    if num1 == 20 and sign == '+' and num2 == 32:
        return("20+32 = 52")
    if num1 == 20 and sign == '+' and num2 == 33:
        return("20+33 = 53")
    if num1 == 20 and sign == '+' and num2 == 34:
        return("20+34 = 54")
    if num1 == 20 and sign == '+' and num2 == 35:
        return("20+35 = 55")
    if num1 == 20 and sign == '+' and num2 == 36:
        return("20+36 = 56")
    if num1 == 20 and sign == '+' and num2 == 37:
        return("20+37 = 57")
    if num1 == 20 and sign == '+' and num2 == 38:
        return("20+38 = 58")
    if num1 == 20 and sign == '+' and num2 == 39:
        return("20+39 = 59")
    if num1 == 20 and sign == '+' and num2 == 40:
        return("20+40 = 60")
    if num1 == 20 and sign == '+' and num2 == 41:
        return("20+41 = 61")
    if num1 == 20 and sign == '+' and num2 == 42:
        return("20+42 = 62")
    if num1 == 20 and sign == '+' and num2 == 43:
        return("20+43 = 63")
    if num1 == 20 and sign == '+' and num2 == 44:
        return("20+44 = 64")
    if num1 == 20 and sign == '+' and num2 == 45:
        return("20+45 = 65")
    if num1 == 20 and sign == '+' and num2 == 46:
        return("20+46 = 66")
    if num1 == 20 and sign == '+' and num2 == 47:
        return("20+47 = 67")
    if num1 == 20 and sign == '+' and num2 == 48:
        return("20+48 = 68")
    if num1 == 20 and sign == '+' and num2 == 49:
        return("20+49 = 69")
    if num1 == 20 and sign == '+' and num2 == 50:
        return("20+50 = 70")
    if num1 == 21 and sign == '+' and num2 == 0:
        return("21+0 = 21")
    if num1 == 21 and sign == '+' and num2 == 1:
        return("21+1 = 22")
    if num1 == 21 and sign == '+' and num2 == 2:
        return("21+2 = 23")
    if num1 == 21 and sign == '+' and num2 == 3:
        return("21+3 = 24")
    if num1 == 21 and sign == '+' and num2 == 4:
        return("21+4 = 25")
    if num1 == 21 and sign == '+' and num2 == 5:
        return("21+5 = 26")
    if num1 == 21 and sign == '+' and num2 == 6:
        return("21+6 = 27")
    if num1 == 21 and sign == '+' and num2 == 7:
        return("21+7 = 28")
    if num1 == 21 and sign == '+' and num2 == 8:
        return("21+8 = 29")
    if num1 == 21 and sign == '+' and num2 == 9:
        return("21+9 = 30")
    if num1 == 21 and sign == '+' and num2 == 10:
        return("21+10 = 31")
    if num1 == 21 and sign == '+' and num2 == 11:
        return("21+11 = 32")
    if num1 == 21 and sign == '+' and num2 == 12:
        return("21+12 = 33")
    if num1 == 21 and sign == '+' and num2 == 13:
        return("21+13 = 34")
    if num1 == 21 and sign == '+' and num2 == 14:
        return("21+14 = 35")
    if num1 == 21 and sign == '+' and num2 == 15:
        return("21+15 = 36")
    if num1 == 21 and sign == '+' and num2 == 16:
        return("21+16 = 37")
    if num1 == 21 and sign == '+' and num2 == 17:
        return("21+17 = 38")
    if num1 == 21 and sign == '+' and num2 == 18:
        return("21+18 = 39")
    if num1 == 21 and sign == '+' and num2 == 19:
        return("21+19 = 40")
    if num1 == 21 and sign == '+' and num2 == 20:
        return("21+20 = 41")
    if num1 == 21 and sign == '+' and num2 == 21:
        return("21+21 = 42")
    if num1 == 21 and sign == '+' and num2 == 22:
        return("21+22 = 43")
    if num1 == 21 and sign == '+' and num2 == 23:
        return("21+23 = 44")
    if num1 == 21 and sign == '+' and num2 == 24:
        return("21+24 = 45")
    if num1 == 21 and sign == '+' and num2 == 25:
        return("21+25 = 46")
    if num1 == 21 and sign == '+' and num2 == 26:
        return("21+26 = 47")
    if num1 == 21 and sign == '+' and num2 == 27:
        return("21+27 = 48")
    if num1 == 21 and sign == '+' and num2 == 28:
        return("21+28 = 49")
    if num1 == 21 and sign == '+' and num2 == 29:
        return("21+29 = 50")
    if num1 == 21 and sign == '+' and num2 == 30:
        return("21+30 = 51")
    if num1 == 21 and sign == '+' and num2 == 31:
        return("21+31 = 52")
    if num1 == 21 and sign == '+' and num2 == 32:
        return("21+32 = 53")
    if num1 == 21 and sign == '+' and num2 == 33:
        return("21+33 = 54")
    if num1 == 21 and sign == '+' and num2 == 34:
        return("21+34 = 55")
    if num1 == 21 and sign == '+' and num2 == 35:
        return("21+35 = 56")
    if num1 == 21 and sign == '+' and num2 == 36:
        return("21+36 = 57")
    if num1 == 21 and sign == '+' and num2 == 37:
        return("21+37 = 58")
    if num1 == 21 and sign == '+' and num2 == 38:
        return("21+38 = 59")
    if num1 == 21 and sign == '+' and num2 == 39:
        return("21+39 = 60")
    if num1 == 21 and sign == '+' and num2 == 40:
        return("21+40 = 61")
    if num1 == 21 and sign == '+' and num2 == 41:
        return("21+41 = 62")
    if num1 == 21 and sign == '+' and num2 == 42:
        return("21+42 = 63")
    if num1 == 21 and sign == '+' and num2 == 43:
        return("21+43 = 64")
    if num1 == 21 and sign == '+' and num2 == 44:
        return("21+44 = 65")
    if num1 == 21 and sign == '+' and num2 == 45:
        return("21+45 = 66")
    if num1 == 21 and sign == '+' and num2 == 46:
        return("21+46 = 67")
    if num1 == 21 and sign == '+' and num2 == 47:
        return("21+47 = 68")
    if num1 == 21 and sign == '+' and num2 == 48:
        return("21+48 = 69")
    if num1 == 21 and sign == '+' and num2 == 49:
        return("21+49 = 70")
    if num1 == 21 and sign == '+' and num2 == 50:
        return("21+50 = 71")
    if num1 == 22 and sign == '+' and num2 == 0:
        return("22+0 = 22")
    if num1 == 22 and sign == '+' and num2 == 1:
        return("22+1 = 23")
    if num1 == 22 and sign == '+' and num2 == 2:
        return("22+2 = 24")
    if num1 == 22 and sign == '+' and num2 == 3:
        return("22+3 = 25")
    if num1 == 22 and sign == '+' and num2 == 4:
        return("22+4 = 26")
    if num1 == 22 and sign == '+' and num2 == 5:
        return("22+5 = 27")
    if num1 == 22 and sign == '+' and num2 == 6:
        return("22+6 = 28")
    if num1 == 22 and sign == '+' and num2 == 7:
        return("22+7 = 29")
    if num1 == 22 and sign == '+' and num2 == 8:
        return("22+8 = 30")
    if num1 == 22 and sign == '+' and num2 == 9:
        return("22+9 = 31")
    if num1 == 22 and sign == '+' and num2 == 10:
        return("22+10 = 32")
    if num1 == 22 and sign == '+' and num2 == 11:
        return("22+11 = 33")
    if num1 == 22 and sign == '+' and num2 == 12:
        return("22+12 = 34")
    if num1 == 22 and sign == '+' and num2 == 13:
        return("22+13 = 35")
    if num1 == 22 and sign == '+' and num2 == 14:
        return("22+14 = 36")
    if num1 == 22 and sign == '+' and num2 == 15:
        return("22+15 = 37")
    if num1 == 22 and sign == '+' and num2 == 16:
        return("22+16 = 38")
    if num1 == 22 and sign == '+' and num2 == 17:
        return("22+17 = 39")
    if num1 == 22 and sign == '+' and num2 == 18:
        return("22+18 = 40")
    if num1 == 22 and sign == '+' and num2 == 19:
        return("22+19 = 41")
    if num1 == 22 and sign == '+' and num2 == 20:
        return("22+20 = 42")
    if num1 == 22 and sign == '+' and num2 == 21:
        return("22+21 = 43")
    if num1 == 22 and sign == '+' and num2 == 22:
        return("22+22 = 44")
    if num1 == 22 and sign == '+' and num2 == 23:
        return("22+23 = 45")
    if num1 == 22 and sign == '+' and num2 == 24:
        return("22+24 = 46")
    if num1 == 22 and sign == '+' and num2 == 25:
        return("22+25 = 47")
    if num1 == 22 and sign == '+' and num2 == 26:
        return("22+26 = 48")
    if num1 == 22 and sign == '+' and num2 == 27:
        return("22+27 = 49")
    if num1 == 22 and sign == '+' and num2 == 28:
        return("22+28 = 50")
    if num1 == 22 and sign == '+' and num2 == 29:
        return("22+29 = 51")
    if num1 == 22 and sign == '+' and num2 == 30:
        return("22+30 = 52")
    if num1 == 22 and sign == '+' and num2 == 31:
        return("22+31 = 53")
    if num1 == 22 and sign == '+' and num2 == 32:
        return("22+32 = 54")
    if num1 == 22 and sign == '+' and num2 == 33:
        return("22+33 = 55")
    if num1 == 22 and sign == '+' and num2 == 34:
        return("22+34 = 56")
    if num1 == 22 and sign == '+' and num2 == 35:
        return("22+35 = 57")
    if num1 == 22 and sign == '+' and num2 == 36:
        return("22+36 = 58")
    if num1 == 22 and sign == '+' and num2 == 37:
        return("22+37 = 59")
    if num1 == 22 and sign == '+' and num2 == 38:
        return("22+38 = 60")
    if num1 == 22 and sign == '+' and num2 == 39:
        return("22+39 = 61")
    if num1 == 22 and sign == '+' and num2 == 40:
        return("22+40 = 62")
    if num1 == 22 and sign == '+' and num2 == 41:
        return("22+41 = 63")
    if num1 == 22 and sign == '+' and num2 == 42:
        return("22+42 = 64")
    if num1 == 22 and sign == '+' and num2 == 43:
        return("22+43 = 65")
    if num1 == 22 and sign == '+' and num2 == 44:
        return("22+44 = 66")
    if num1 == 22 and sign == '+' and num2 == 45:
        return("22+45 = 67")
    if num1 == 22 and sign == '+' and num2 == 46:
        return("22+46 = 68")
    if num1 == 22 and sign == '+' and num2 == 47:
        return("22+47 = 69")
    if num1 == 22 and sign == '+' and num2 == 48:
        return("22+48 = 70")
    if num1 == 22 and sign == '+' and num2 == 49:
        return("22+49 = 71")
    if num1 == 22 and sign == '+' and num2 == 50:
        return("22+50 = 72")
    if num1 == 23 and sign == '+' and num2 == 0:
        return("23+0 = 23")
    if num1 == 23 and sign == '+' and num2 == 1:
        return("23+1 = 24")
    if num1 == 23 and sign == '+' and num2 == 2:
        return("23+2 = 25")
    if num1 == 23 and sign == '+' and num2 == 3:
        return("23+3 = 26")
    if num1 == 23 and sign == '+' and num2 == 4:
        return("23+4 = 27")
    if num1 == 23 and sign == '+' and num2 == 5:
        return("23+5 = 28")
    if num1 == 23 and sign == '+' and num2 == 6:
        return("23+6 = 29")
    if num1 == 23 and sign == '+' and num2 == 7:
        return("23+7 = 30")
    if num1 == 23 and sign == '+' and num2 == 8:
        return("23+8 = 31")
    if num1 == 23 and sign == '+' and num2 == 9:
        return("23+9 = 32")
    if num1 == 23 and sign == '+' and num2 == 10:
        return("23+10 = 33")
    if num1 == 23 and sign == '+' and num2 == 11:
        return("23+11 = 34")
    if num1 == 23 and sign == '+' and num2 == 12:
        return("23+12 = 35")
    if num1 == 23 and sign == '+' and num2 == 13:
        return("23+13 = 36")
    if num1 == 23 and sign == '+' and num2 == 14:
        return("23+14 = 37")
    if num1 == 23 and sign == '+' and num2 == 15:
        return("23+15 = 38")
    if num1 == 23 and sign == '+' and num2 == 16:
        return("23+16 = 39")
    if num1 == 23 and sign == '+' and num2 == 17:
        return("23+17 = 40")
    if num1 == 23 and sign == '+' and num2 == 18:
        return("23+18 = 41")
    if num1 == 23 and sign == '+' and num2 == 19:
        return("23+19 = 42")
    if num1 == 23 and sign == '+' and num2 == 20:
        return("23+20 = 43")
    if num1 == 23 and sign == '+' and num2 == 21:
        return("23+21 = 44")
    if num1 == 23 and sign == '+' and num2 == 22:
        return("23+22 = 45")
    if num1 == 23 and sign == '+' and num2 == 23:
        return("23+23 = 46")
    if num1 == 23 and sign == '+' and num2 == 24:
        return("23+24 = 47")
    if num1 == 23 and sign == '+' and num2 == 25:
        return("23+25 = 48")
    if num1 == 23 and sign == '+' and num2 == 26:
        return("23+26 = 49")
    if num1 == 23 and sign == '+' and num2 == 27:
        return("23+27 = 50")
    if num1 == 23 and sign == '+' and num2 == 28:
        return("23+28 = 51")
    if num1 == 23 and sign == '+' and num2 == 29:
        return("23+29 = 52")
    if num1 == 23 and sign == '+' and num2 == 30:
        return("23+30 = 53")
    if num1 == 23 and sign == '+' and num2 == 31:
        return("23+31 = 54")
    if num1 == 23 and sign == '+' and num2 == 32:
        return("23+32 = 55")
    if num1 == 23 and sign == '+' and num2 == 33:
        return("23+33 = 56")
    if num1 == 23 and sign == '+' and num2 == 34:
        return("23+34 = 57")
    if num1 == 23 and sign == '+' and num2 == 35:
        return("23+35 = 58")
    if num1 == 23 and sign == '+' and num2 == 36:
        return("23+36 = 59")
    if num1 == 23 and sign == '+' and num2 == 37:
        return("23+37 = 60")
    if num1 == 23 and sign == '+' and num2 == 38:
        return("23+38 = 61")
    if num1 == 23 and sign == '+' and num2 == 39:
        return("23+39 = 62")
    if num1 == 23 and sign == '+' and num2 == 40:
        return("23+40 = 63")
    if num1 == 23 and sign == '+' and num2 == 41:
        return("23+41 = 64")
    if num1 == 23 and sign == '+' and num2 == 42:
        return("23+42 = 65")
    if num1 == 23 and sign == '+' and num2 == 43:
        return("23+43 = 66")
    if num1 == 23 and sign == '+' and num2 == 44:
        return("23+44 = 67")
    if num1 == 23 and sign == '+' and num2 == 45:
        return("23+45 = 68")
    if num1 == 23 and sign == '+' and num2 == 46:
        return("23+46 = 69")
    if num1 == 23 and sign == '+' and num2 == 47:
        return("23+47 = 70")
    if num1 == 23 and sign == '+' and num2 == 48:
        return("23+48 = 71")
    if num1 == 23 and sign == '+' and num2 == 49:
        return("23+49 = 72")
    if num1 == 23 and sign == '+' and num2 == 50:
        return("23+50 = 73")
    if num1 == 24 and sign == '+' and num2 == 0:
        return("24+0 = 24")
    if num1 == 24 and sign == '+' and num2 == 1:
        return("24+1 = 25")
    if num1 == 24 and sign == '+' and num2 == 2:
        return("24+2 = 26")
    if num1 == 24 and sign == '+' and num2 == 3:
        return("24+3 = 27")
    if num1 == 24 and sign == '+' and num2 == 4:
        return("24+4 = 28")
    if num1 == 24 and sign == '+' and num2 == 5:
        return("24+5 = 29")
    if num1 == 24 and sign == '+' and num2 == 6:
        return("24+6 = 30")
    if num1 == 24 and sign == '+' and num2 == 7:
        return("24+7 = 31")
    if num1 == 24 and sign == '+' and num2 == 8:
        return("24+8 = 32")
    if num1 == 24 and sign == '+' and num2 == 9:
        return("24+9 = 33")
    if num1 == 24 and sign == '+' and num2 == 10:
        return("24+10 = 34")
    if num1 == 24 and sign == '+' and num2 == 11:
        return("24+11 = 35")
    if num1 == 24 and sign == '+' and num2 == 12:
        return("24+12 = 36")
    if num1 == 24 and sign == '+' and num2 == 13:
        return("24+13 = 37")
    if num1 == 24 and sign == '+' and num2 == 14:
        return("24+14 = 38")
    if num1 == 24 and sign == '+' and num2 == 15:
        return("24+15 = 39")
    if num1 == 24 and sign == '+' and num2 == 16:
        return("24+16 = 40")
    if num1 == 24 and sign == '+' and num2 == 17:
        return("24+17 = 41")
    if num1 == 24 and sign == '+' and num2 == 18:
        return("24+18 = 42")
    if num1 == 24 and sign == '+' and num2 == 19:
        return("24+19 = 43")
    if num1 == 24 and sign == '+' and num2 == 20:
        return("24+20 = 44")
    if num1 == 24 and sign == '+' and num2 == 21:
        return("24+21 = 45")
    if num1 == 24 and sign == '+' and num2 == 22:
        return("24+22 = 46")
    if num1 == 24 and sign == '+' and num2 == 23:
        return("24+23 = 47")
    if num1 == 24 and sign == '+' and num2 == 24:
        return("24+24 = 48")
    if num1 == 24 and sign == '+' and num2 == 25:
        return("24+25 = 49")
    if num1 == 24 and sign == '+' and num2 == 26:
        return("24+26 = 50")
    if num1 == 24 and sign == '+' and num2 == 27:
        return("24+27 = 51")
    if num1 == 24 and sign == '+' and num2 == 28:
        return("24+28 = 52")
    if num1 == 24 and sign == '+' and num2 == 29:
        return("24+29 = 53")
    if num1 == 24 and sign == '+' and num2 == 30:
        return("24+30 = 54")
    if num1 == 24 and sign == '+' and num2 == 31:
        return("24+31 = 55")
    if num1 == 24 and sign == '+' and num2 == 32:
        return("24+32 = 56")
    if num1 == 24 and sign == '+' and num2 == 33:
        return("24+33 = 57")
    if num1 == 24 and sign == '+' and num2 == 34:
        return("24+34 = 58")
    if num1 == 24 and sign == '+' and num2 == 35:
        return("24+35 = 59")
    if num1 == 24 and sign == '+' and num2 == 36:
        return("24+36 = 60")
    if num1 == 24 and sign == '+' and num2 == 37:
        return("24+37 = 61")
    if num1 == 24 and sign == '+' and num2 == 38:
        return("24+38 = 62")
    if num1 == 24 and sign == '+' and num2 == 39:
        return("24+39 = 63")
    if num1 == 24 and sign == '+' and num2 == 40:
        return("24+40 = 64")
    if num1 == 24 and sign == '+' and num2 == 41:
        return("24+41 = 65")
    if num1 == 24 and sign == '+' and num2 == 42:
        return("24+42 = 66")
    if num1 == 24 and sign == '+' and num2 == 43:
        return("24+43 = 67")
    if num1 == 24 and sign == '+' and num2 == 44:
        return("24+44 = 68")
    if num1 == 24 and sign == '+' and num2 == 45:
        return("24+45 = 69")
    if num1 == 24 and sign == '+' and num2 == 46:
        return("24+46 = 70")
    if num1 == 24 and sign == '+' and num2 == 47:
        return("24+47 = 71")
    if num1 == 24 and sign == '+' and num2 == 48:
        return("24+48 = 72")
    if num1 == 24 and sign == '+' and num2 == 49:
        return("24+49 = 73")
    if num1 == 24 and sign == '+' and num2 == 50:
        return("24+50 = 74")
    if num1 == 25 and sign == '+' and num2 == 0:
        return("25+0 = 25")
    if num1 == 25 and sign == '+' and num2 == 1:
        return("25+1 = 26")
    if num1 == 25 and sign == '+' and num2 == 2:
        return("25+2 = 27")
    if num1 == 25 and sign == '+' and num2 == 3:
        return("25+3 = 28")
    if num1 == 25 and sign == '+' and num2 == 4:
        return("25+4 = 29")
    if num1 == 25 and sign == '+' and num2 == 5:
        return("25+5 = 30")
    if num1 == 25 and sign == '+' and num2 == 6:
        return("25+6 = 31")
    if num1 == 25 and sign == '+' and num2 == 7:
        return("25+7 = 32")
    if num1 == 25 and sign == '+' and num2 == 8:
        return("25+8 = 33")
    if num1 == 25 and sign == '+' and num2 == 9:
        return("25+9 = 34")
    if num1 == 25 and sign == '+' and num2 == 10:
        return("25+10 = 35")
    if num1 == 25 and sign == '+' and num2 == 11:
        return("25+11 = 36")
    if num1 == 25 and sign == '+' and num2 == 12:
        return("25+12 = 37")
    if num1 == 25 and sign == '+' and num2 == 13:
        return("25+13 = 38")
    if num1 == 25 and sign == '+' and num2 == 14:
        return("25+14 = 39")
    if num1 == 25 and sign == '+' and num2 == 15:
        return("25+15 = 40")
    if num1 == 25 and sign == '+' and num2 == 16:
        return("25+16 = 41")
    if num1 == 25 and sign == '+' and num2 == 17:
        return("25+17 = 42")
    if num1 == 25 and sign == '+' and num2 == 18:
        return("25+18 = 43")
    if num1 == 25 and sign == '+' and num2 == 19:
        return("25+19 = 44")
    if num1 == 25 and sign == '+' and num2 == 20:
        return("25+20 = 45")
    if num1 == 25 and sign == '+' and num2 == 21:
        return("25+21 = 46")
    if num1 == 25 and sign == '+' and num2 == 22:
        return("25+22 = 47")
    if num1 == 25 and sign == '+' and num2 == 23:
        return("25+23 = 48")
    if num1 == 25 and sign == '+' and num2 == 24:
        return("25+24 = 49")
    if num1 == 25 and sign == '+' and num2 == 25:
        return("25+25 = 50")
    if num1 == 25 and sign == '+' and num2 == 26:
        return("25+26 = 51")
    if num1 == 25 and sign == '+' and num2 == 27:
        return("25+27 = 52")
    if num1 == 25 and sign == '+' and num2 == 28:
        return("25+28 = 53")
    if num1 == 25 and sign == '+' and num2 == 29:
        return("25+29 = 54")
    if num1 == 25 and sign == '+' and num2 == 30:
        return("25+30 = 55")
    if num1 == 25 and sign == '+' and num2 == 31:
        return("25+31 = 56")
    if num1 == 25 and sign == '+' and num2 == 32:
        return("25+32 = 57")
    if num1 == 25 and sign == '+' and num2 == 33:
        return("25+33 = 58")
    if num1 == 25 and sign == '+' and num2 == 34:
        return("25+34 = 59")
    if num1 == 25 and sign == '+' and num2 == 35:
        return("25+35 = 60")
    if num1 == 25 and sign == '+' and num2 == 36:
        return("25+36 = 61")
    if num1 == 25 and sign == '+' and num2 == 37:
        return("25+37 = 62")
    if num1 == 25 and sign == '+' and num2 == 38:
        return("25+38 = 63")
    if num1 == 25 and sign == '+' and num2 == 39:
        return("25+39 = 64")
    if num1 == 25 and sign == '+' and num2 == 40:
        return("25+40 = 65")
    if num1 == 25 and sign == '+' and num2 == 41:
        return("25+41 = 66")
    if num1 == 25 and sign == '+' and num2 == 42:
        return("25+42 = 67")
    if num1 == 25 and sign == '+' and num2 == 43:
        return("25+43 = 68")
    if num1 == 25 and sign == '+' and num2 == 44:
        return("25+44 = 69")
    if num1 == 25 and sign == '+' and num2 == 45:
        return("25+45 = 70")
    if num1 == 25 and sign == '+' and num2 == 46:
        return("25+46 = 71")
    if num1 == 25 and sign == '+' and num2 == 47:
        return("25+47 = 72")
    if num1 == 25 and sign == '+' and num2 == 48:
        return("25+48 = 73")
    if num1 == 25 and sign == '+' and num2 == 49:
        return("25+49 = 74")
    if num1 == 25 and sign == '+' and num2 == 50:
        return("25+50 = 75")
    if num1 == 26 and sign == '+' and num2 == 0:
        return("26+0 = 26")
    if num1 == 26 and sign == '+' and num2 == 1:
        return("26+1 = 27")
    if num1 == 26 and sign == '+' and num2 == 2:
        return("26+2 = 28")
    if num1 == 26 and sign == '+' and num2 == 3:
        return("26+3 = 29")
    if num1 == 26 and sign == '+' and num2 == 4:
        return("26+4 = 30")
    if num1 == 26 and sign == '+' and num2 == 5:
        return("26+5 = 31")
    if num1 == 26 and sign == '+' and num2 == 6:
        return("26+6 = 32")
    if num1 == 26 and sign == '+' and num2 == 7:
        return("26+7 = 33")
    if num1 == 26 and sign == '+' and num2 == 8:
        return("26+8 = 34")
    if num1 == 26 and sign == '+' and num2 == 9:
        return("26+9 = 35")
    if num1 == 26 and sign == '+' and num2 == 10:
        return("26+10 = 36")
    if num1 == 26 and sign == '+' and num2 == 11:
        return("26+11 = 37")
    if num1 == 26 and sign == '+' and num2 == 12:
        return("26+12 = 38")
    if num1 == 26 and sign == '+' and num2 == 13:
        return("26+13 = 39")
    if num1 == 26 and sign == '+' and num2 == 14:
        return("26+14 = 40")
    if num1 == 26 and sign == '+' and num2 == 15:
        return("26+15 = 41")
    if num1 == 26 and sign == '+' and num2 == 16:
        return("26+16 = 42")
    if num1 == 26 and sign == '+' and num2 == 17:
        return("26+17 = 43")
    if num1 == 26 and sign == '+' and num2 == 18:
        return("26+18 = 44")
    if num1 == 26 and sign == '+' and num2 == 19:
        return("26+19 = 45")
    if num1 == 26 and sign == '+' and num2 == 20:
        return("26+20 = 46")
    if num1 == 26 and sign == '+' and num2 == 21:
        return("26+21 = 47")
    if num1 == 26 and sign == '+' and num2 == 22:
        return("26+22 = 48")
    if num1 == 26 and sign == '+' and num2 == 23:
        return("26+23 = 49")
    if num1 == 26 and sign == '+' and num2 == 24:
        return("26+24 = 50")
    if num1 == 26 and sign == '+' and num2 == 25:
        return("26+25 = 51")
    if num1 == 26 and sign == '+' and num2 == 26:
        return("26+26 = 52")
    if num1 == 26 and sign == '+' and num2 == 27:
        return("26+27 = 53")
    if num1 == 26 and sign == '+' and num2 == 28:
        return("26+28 = 54")
    if num1 == 26 and sign == '+' and num2 == 29:
        return("26+29 = 55")
    if num1 == 26 and sign == '+' and num2 == 30:
        return("26+30 = 56")
    if num1 == 26 and sign == '+' and num2 == 31:
        return("26+31 = 57")
    if num1 == 26 and sign == '+' and num2 == 32:
        return("26+32 = 58")
    if num1 == 26 and sign == '+' and num2 == 33:
        return("26+33 = 59")
    if num1 == 26 and sign == '+' and num2 == 34:
        return("26+34 = 60")
    if num1 == 26 and sign == '+' and num2 == 35:
        return("26+35 = 61")
    if num1 == 26 and sign == '+' and num2 == 36:
        return("26+36 = 62")
    if num1 == 26 and sign == '+' and num2 == 37:
        return("26+37 = 63")
    if num1 == 26 and sign == '+' and num2 == 38:
        return("26+38 = 64")
    if num1 == 26 and sign == '+' and num2 == 39:
        return("26+39 = 65")
    if num1 == 26 and sign == '+' and num2 == 40:
        return("26+40 = 66")
    if num1 == 26 and sign == '+' and num2 == 41:
        return("26+41 = 67")
    if num1 == 26 and sign == '+' and num2 == 42:
        return("26+42 = 68")
    if num1 == 26 and sign == '+' and num2 == 43:
        return("26+43 = 69")
    if num1 == 26 and sign == '+' and num2 == 44:
        return("26+44 = 70")
    if num1 == 26 and sign == '+' and num2 == 45:
        return("26+45 = 71")
    if num1 == 26 and sign == '+' and num2 == 46:
        return("26+46 = 72")
    if num1 == 26 and sign == '+' and num2 == 47:
        return("26+47 = 73")
    if num1 == 26 and sign == '+' and num2 == 48:
        return("26+48 = 74")
    if num1 == 26 and sign == '+' and num2 == 49:
        return("26+49 = 75")
    if num1 == 26 and sign == '+' and num2 == 50:
        return("26+50 = 76")
    if num1 == 27 and sign == '+' and num2 == 0:
        return("27+0 = 27")
    if num1 == 27 and sign == '+' and num2 == 1:
        return("27+1 = 28")
    if num1 == 27 and sign == '+' and num2 == 2:
        return("27+2 = 29")
    if num1 == 27 and sign == '+' and num2 == 3:
        return("27+3 = 30")
    if num1 == 27 and sign == '+' and num2 == 4:
        return("27+4 = 31")
    if num1 == 27 and sign == '+' and num2 == 5:
        return("27+5 = 32")
    if num1 == 27 and sign == '+' and num2 == 6:
        return("27+6 = 33")
    if num1 == 27 and sign == '+' and num2 == 7:
        return("27+7 = 34")
    if num1 == 27 and sign == '+' and num2 == 8:
        return("27+8 = 35")
    if num1 == 27 and sign == '+' and num2 == 9:
        return("27+9 = 36")
    if num1 == 27 and sign == '+' and num2 == 10:
        return("27+10 = 37")
    if num1 == 27 and sign == '+' and num2 == 11:
        return("27+11 = 38")
    if num1 == 27 and sign == '+' and num2 == 12:
        return("27+12 = 39")
    if num1 == 27 and sign == '+' and num2 == 13:
        return("27+13 = 40")
    if num1 == 27 and sign == '+' and num2 == 14:
        return("27+14 = 41")
    if num1 == 27 and sign == '+' and num2 == 15:
        return("27+15 = 42")
    if num1 == 27 and sign == '+' and num2 == 16:
        return("27+16 = 43")
    if num1 == 27 and sign == '+' and num2 == 17:
        return("27+17 = 44")
    if num1 == 27 and sign == '+' and num2 == 18:
        return("27+18 = 45")
    if num1 == 27 and sign == '+' and num2 == 19:
        return("27+19 = 46")
    if num1 == 27 and sign == '+' and num2 == 20:
        return("27+20 = 47")
    if num1 == 27 and sign == '+' and num2 == 21:
        return("27+21 = 48")
    if num1 == 27 and sign == '+' and num2 == 22:
        return("27+22 = 49")
    if num1 == 27 and sign == '+' and num2 == 23:
        return("27+23 = 50")
    if num1 == 27 and sign == '+' and num2 == 24:
        return("27+24 = 51")
    if num1 == 27 and sign == '+' and num2 == 25:
        return("27+25 = 52")
    if num1 == 27 and sign == '+' and num2 == 26:
        return("27+26 = 53")
    if num1 == 27 and sign == '+' and num2 == 27:
        return("27+27 = 54")
    if num1 == 27 and sign == '+' and num2 == 28:
        return("27+28 = 55")
    if num1 == 27 and sign == '+' and num2 == 29:
        return("27+29 = 56")
    if num1 == 27 and sign == '+' and num2 == 30:
        return("27+30 = 57")
    if num1 == 27 and sign == '+' and num2 == 31:
        return("27+31 = 58")
    if num1 == 27 and sign == '+' and num2 == 32:
        return("27+32 = 59")
    if num1 == 27 and sign == '+' and num2 == 33:
        return("27+33 = 60")
    if num1 == 27 and sign == '+' and num2 == 34:
        return("27+34 = 61")
    if num1 == 27 and sign == '+' and num2 == 35:
        return("27+35 = 62")
    if num1 == 27 and sign == '+' and num2 == 36:
        return("27+36 = 63")
    if num1 == 27 and sign == '+' and num2 == 37:
        return("27+37 = 64")
    if num1 == 27 and sign == '+' and num2 == 38:
        return("27+38 = 65")
    if num1 == 27 and sign == '+' and num2 == 39:
        return("27+39 = 66")
    if num1 == 27 and sign == '+' and num2 == 40:
        return("27+40 = 67")
    if num1 == 27 and sign == '+' and num2 == 41:
        return("27+41 = 68")
    if num1 == 27 and sign == '+' and num2 == 42:
        return("27+42 = 69")
    if num1 == 27 and sign == '+' and num2 == 43:
        return("27+43 = 70")
    if num1 == 27 and sign == '+' and num2 == 44:
        return("27+44 = 71")
    if num1 == 27 and sign == '+' and num2 == 45:
        return("27+45 = 72")
    if num1 == 27 and sign == '+' and num2 == 46:
        return("27+46 = 73")
    if num1 == 27 and sign == '+' and num2 == 47:
        return("27+47 = 74")
    if num1 == 27 and sign == '+' and num2 == 48:
        return("27+48 = 75")
    if num1 == 27 and sign == '+' and num2 == 49:
        return("27+49 = 76")
    if num1 == 27 and sign == '+' and num2 == 50:
        return("27+50 = 77")
    if num1 == 28 and sign == '+' and num2 == 0:
        return("28+0 = 28")
    if num1 == 28 and sign == '+' and num2 == 1:
        return("28+1 = 29")
    if num1 == 28 and sign == '+' and num2 == 2:
        return("28+2 = 30")
    if num1 == 28 and sign == '+' and num2 == 3:
        return("28+3 = 31")
    if num1 == 28 and sign == '+' and num2 == 4:
        return("28+4 = 32")
    if num1 == 28 and sign == '+' and num2 == 5:
        return("28+5 = 33")
    if num1 == 28 and sign == '+' and num2 == 6:
        return("28+6 = 34")
    if num1 == 28 and sign == '+' and num2 == 7:
        return("28+7 = 35")
    if num1 == 28 and sign == '+' and num2 == 8:
        return("28+8 = 36")
    if num1 == 28 and sign == '+' and num2 == 9:
        return("28+9 = 37")
    if num1 == 28 and sign == '+' and num2 == 10:
        return("28+10 = 38")
    if num1 == 28 and sign == '+' and num2 == 11:
        return("28+11 = 39")
    if num1 == 28 and sign == '+' and num2 == 12:
        return("28+12 = 40")
    if num1 == 28 and sign == '+' and num2 == 13:
        return("28+13 = 41")
    if num1 == 28 and sign == '+' and num2 == 14:
        return("28+14 = 42")
    if num1 == 28 and sign == '+' and num2 == 15:
        return("28+15 = 43")
    if num1 == 28 and sign == '+' and num2 == 16:
        return("28+16 = 44")
    if num1 == 28 and sign == '+' and num2 == 17:
        return("28+17 = 45")
    if num1 == 28 and sign == '+' and num2 == 18:
        return("28+18 = 46")
    if num1 == 28 and sign == '+' and num2 == 19:
        return("28+19 = 47")
    if num1 == 28 and sign == '+' and num2 == 20:
        return("28+20 = 48")
    if num1 == 28 and sign == '+' and num2 == 21:
        return("28+21 = 49")
    if num1 == 28 and sign == '+' and num2 == 22:
        return("28+22 = 50")
    if num1 == 28 and sign == '+' and num2 == 23:
        return("28+23 = 51")
    if num1 == 28 and sign == '+' and num2 == 24:
        return("28+24 = 52")
    if num1 == 28 and sign == '+' and num2 == 25:
        return("28+25 = 53")
    if num1 == 28 and sign == '+' and num2 == 26:
        return("28+26 = 54")
    if num1 == 28 and sign == '+' and num2 == 27:
        return("28+27 = 55")
    if num1 == 28 and sign == '+' and num2 == 28:
        return("28+28 = 56")
    if num1 == 28 and sign == '+' and num2 == 29:
        return("28+29 = 57")
    if num1 == 28 and sign == '+' and num2 == 30:
        return("28+30 = 58")
    if num1 == 28 and sign == '+' and num2 == 31:
        return("28+31 = 59")
    if num1 == 28 and sign == '+' and num2 == 32:
        return("28+32 = 60")
    if num1 == 28 and sign == '+' and num2 == 33:
        return("28+33 = 61")
    if num1 == 28 and sign == '+' and num2 == 34:
        return("28+34 = 62")
    if num1 == 28 and sign == '+' and num2 == 35:
        return("28+35 = 63")
    if num1 == 28 and sign == '+' and num2 == 36:
        return("28+36 = 64")
    if num1 == 28 and sign == '+' and num2 == 37:
        return("28+37 = 65")
    if num1 == 28 and sign == '+' and num2 == 38:
        return("28+38 = 66")
    if num1 == 28 and sign == '+' and num2 == 39:
        return("28+39 = 67")
    if num1 == 28 and sign == '+' and num2 == 40:
        return("28+40 = 68")
    if num1 == 28 and sign == '+' and num2 == 41:
        return("28+41 = 69")
    if num1 == 28 and sign == '+' and num2 == 42:
        return("28+42 = 70")
    if num1 == 28 and sign == '+' and num2 == 43:
        return("28+43 = 71")
    if num1 == 28 and sign == '+' and num2 == 44:
        return("28+44 = 72")
    if num1 == 28 and sign == '+' and num2 == 45:
        return("28+45 = 73")
    if num1 == 28 and sign == '+' and num2 == 46:
        return("28+46 = 74")
    if num1 == 28 and sign == '+' and num2 == 47:
        return("28+47 = 75")
    if num1 == 28 and sign == '+' and num2 == 48:
        return("28+48 = 76")
    if num1 == 28 and sign == '+' and num2 == 49:
        return("28+49 = 77")
    if num1 == 28 and sign == '+' and num2 == 50:
        return("28+50 = 78")
    if num1 == 29 and sign == '+' and num2 == 0:
        return("29+0 = 29")
    if num1 == 29 and sign == '+' and num2 == 1:
        return("29+1 = 30")
    if num1 == 29 and sign == '+' and num2 == 2:
        return("29+2 = 31")
    if num1 == 29 and sign == '+' and num2 == 3:
        return("29+3 = 32")
    if num1 == 29 and sign == '+' and num2 == 4:
        return("29+4 = 33")
    if num1 == 29 and sign == '+' and num2 == 5:
        return("29+5 = 34")
    if num1 == 29 and sign == '+' and num2 == 6:
        return("29+6 = 35")
    if num1 == 29 and sign == '+' and num2 == 7:
        return("29+7 = 36")
    if num1 == 29 and sign == '+' and num2 == 8:
        return("29+8 = 37")
    if num1 == 29 and sign == '+' and num2 == 9:
        return("29+9 = 38")
    if num1 == 29 and sign == '+' and num2 == 10:
        return("29+10 = 39")
    if num1 == 29 and sign == '+' and num2 == 11:
        return("29+11 = 40")
    if num1 == 29 and sign == '+' and num2 == 12:
        return("29+12 = 41")
    if num1 == 29 and sign == '+' and num2 == 13:
        return("29+13 = 42")
    if num1 == 29 and sign == '+' and num2 == 14:
        return("29+14 = 43")
    if num1 == 29 and sign == '+' and num2 == 15:
        return("29+15 = 44")
    if num1 == 29 and sign == '+' and num2 == 16:
        return("29+16 = 45")
    if num1 == 29 and sign == '+' and num2 == 17:
        return("29+17 = 46")
    if num1 == 29 and sign == '+' and num2 == 18:
        return("29+18 = 47")
    if num1 == 29 and sign == '+' and num2 == 19:
        return("29+19 = 48")
    if num1 == 29 and sign == '+' and num2 == 20:
        return("29+20 = 49")
    if num1 == 29 and sign == '+' and num2 == 21:
        return("29+21 = 50")
    if num1 == 29 and sign == '+' and num2 == 22:
        return("29+22 = 51")
    if num1 == 29 and sign == '+' and num2 == 23:
        return("29+23 = 52")
    if num1 == 29 and sign == '+' and num2 == 24:
        return("29+24 = 53")
    if num1 == 29 and sign == '+' and num2 == 25:
        return("29+25 = 54")
    if num1 == 29 and sign == '+' and num2 == 26:
        return("29+26 = 55")
    if num1 == 29 and sign == '+' and num2 == 27:
        return("29+27 = 56")
    if num1 == 29 and sign == '+' and num2 == 28:
        return("29+28 = 57")
    if num1 == 29 and sign == '+' and num2 == 29:
        return("29+29 = 58")
    if num1 == 29 and sign == '+' and num2 == 30:
        return("29+30 = 59")
    if num1 == 29 and sign == '+' and num2 == 31:
        return("29+31 = 60")
    if num1 == 29 and sign == '+' and num2 == 32:
        return("29+32 = 61")
    if num1 == 29 and sign == '+' and num2 == 33:
        return("29+33 = 62")
    if num1 == 29 and sign == '+' and num2 == 34:
        return("29+34 = 63")
    if num1 == 29 and sign == '+' and num2 == 35:
        return("29+35 = 64")
    if num1 == 29 and sign == '+' and num2 == 36:
        return("29+36 = 65")
    if num1 == 29 and sign == '+' and num2 == 37:
        return("29+37 = 66")
    if num1 == 29 and sign == '+' and num2 == 38:
        return("29+38 = 67")
    if num1 == 29 and sign == '+' and num2 == 39:
        return("29+39 = 68")
    if num1 == 29 and sign == '+' and num2 == 40:
        return("29+40 = 69")
    if num1 == 29 and sign == '+' and num2 == 41:
        return("29+41 = 70")
    if num1 == 29 and sign == '+' and num2 == 42:
        return("29+42 = 71")
    if num1 == 29 and sign == '+' and num2 == 43:
        return("29+43 = 72")
    if num1 == 29 and sign == '+' and num2 == 44:
        return("29+44 = 73")
    if num1 == 29 and sign == '+' and num2 == 45:
        return("29+45 = 74")
    if num1 == 29 and sign == '+' and num2 == 46:
        return("29+46 = 75")
    if num1 == 29 and sign == '+' and num2 == 47:
        return("29+47 = 76")
    if num1 == 29 and sign == '+' and num2 == 48:
        return("29+48 = 77")
    if num1 == 29 and sign == '+' and num2 == 49:
        return("29+49 = 78")
    if num1 == 29 and sign == '+' and num2 == 50:
        return("29+50 = 79")
    if num1 == 30 and sign == '+' and num2 == 0:
        return("30+0 = 30")
    if num1 == 30 and sign == '+' and num2 == 1:
        return("30+1 = 31")
    if num1 == 30 and sign == '+' and num2 == 2:
        return("30+2 = 32")
    if num1 == 30 and sign == '+' and num2 == 3:
        return("30+3 = 33")
    if num1 == 30 and sign == '+' and num2 == 4:
        return("30+4 = 34")
    if num1 == 30 and sign == '+' and num2 == 5:
        return("30+5 = 35")
    if num1 == 30 and sign == '+' and num2 == 6:
        return("30+6 = 36")
    if num1 == 30 and sign == '+' and num2 == 7:
        return("30+7 = 37")
    if num1 == 30 and sign == '+' and num2 == 8:
        return("30+8 = 38")
    if num1 == 30 and sign == '+' and num2 == 9:
        return("30+9 = 39")
    if num1 == 30 and sign == '+' and num2 == 10:
        return("30+10 = 40")
    if num1 == 30 and sign == '+' and num2 == 11:
        return("30+11 = 41")
    if num1 == 30 and sign == '+' and num2 == 12:
        return("30+12 = 42")
    if num1 == 30 and sign == '+' and num2 == 13:
        return("30+13 = 43")
    if num1 == 30 and sign == '+' and num2 == 14:
        return("30+14 = 44")
    if num1 == 30 and sign == '+' and num2 == 15:
        return("30+15 = 45")
    if num1 == 30 and sign == '+' and num2 == 16:
        return("30+16 = 46")
    if num1 == 30 and sign == '+' and num2 == 17:
        return("30+17 = 47")
    if num1 == 30 and sign == '+' and num2 == 18:
        return("30+18 = 48")
    if num1 == 30 and sign == '+' and num2 == 19:
        return("30+19 = 49")
    if num1 == 30 and sign == '+' and num2 == 20:
        return("30+20 = 50")
    if num1 == 30 and sign == '+' and num2 == 21:
        return("30+21 = 51")
    if num1 == 30 and sign == '+' and num2 == 22:
        return("30+22 = 52")
    if num1 == 30 and sign == '+' and num2 == 23:
        return("30+23 = 53")
    if num1 == 30 and sign == '+' and num2 == 24:
        return("30+24 = 54")
    if num1 == 30 and sign == '+' and num2 == 25:
        return("30+25 = 55")
    if num1 == 30 and sign == '+' and num2 == 26:
        return("30+26 = 56")
    if num1 == 30 and sign == '+' and num2 == 27:
        return("30+27 = 57")
    if num1 == 30 and sign == '+' and num2 == 28:
        return("30+28 = 58")
    if num1 == 30 and sign == '+' and num2 == 29:
        return("30+29 = 59")
    if num1 == 30 and sign == '+' and num2 == 30:
        return("30+30 = 60")
    if num1 == 30 and sign == '+' and num2 == 31:
        return("30+31 = 61")
    if num1 == 30 and sign == '+' and num2 == 32:
        return("30+32 = 62")
    if num1 == 30 and sign == '+' and num2 == 33:
        return("30+33 = 63")
    if num1 == 30 and sign == '+' and num2 == 34:
        return("30+34 = 64")
    if num1 == 30 and sign == '+' and num2 == 35:
        return("30+35 = 65")
    if num1 == 30 and sign == '+' and num2 == 36:
        return("30+36 = 66")
    if num1 == 30 and sign == '+' and num2 == 37:
        return("30+37 = 67")
    if num1 == 30 and sign == '+' and num2 == 38:
        return("30+38 = 68")
    if num1 == 30 and sign == '+' and num2 == 39:
        return("30+39 = 69")
    if num1 == 30 and sign == '+' and num2 == 40:
        return("30+40 = 70")
    if num1 == 30 and sign == '+' and num2 == 41:
        return("30+41 = 71")
    if num1 == 30 and sign == '+' and num2 == 42:
        return("30+42 = 72")
    if num1 == 30 and sign == '+' and num2 == 43:
        return("30+43 = 73")
    if num1 == 30 and sign == '+' and num2 == 44:
        return("30+44 = 74")
    if num1 == 30 and sign == '+' and num2 == 45:
        return("30+45 = 75")
    if num1 == 30 and sign == '+' and num2 == 46:
        return("30+46 = 76")
    if num1 == 30 and sign == '+' and num2 == 47:
        return("30+47 = 77")
    if num1 == 30 and sign == '+' and num2 == 48:
        return("30+48 = 78")
    if num1 == 30 and sign == '+' and num2 == 49:
        return("30+49 = 79")
    if num1 == 30 and sign == '+' and num2 == 50:
        return("30+50 = 80")
    if num1 == 31 and sign == '+' and num2 == 0:
        return("31+0 = 31")
    if num1 == 31 and sign == '+' and num2 == 1:
        return("31+1 = 32")
    if num1 == 31 and sign == '+' and num2 == 2:
        return("31+2 = 33")
    if num1 == 31 and sign == '+' and num2 == 3:
        return("31+3 = 34")
    if num1 == 31 and sign == '+' and num2 == 4:
        return("31+4 = 35")
    if num1 == 31 and sign == '+' and num2 == 5:
        return("31+5 = 36")
    if num1 == 31 and sign == '+' and num2 == 6:
        return("31+6 = 37")
    if num1 == 31 and sign == '+' and num2 == 7:
        return("31+7 = 38")
    if num1 == 31 and sign == '+' and num2 == 8:
        return("31+8 = 39")
    if num1 == 31 and sign == '+' and num2 == 9:
        return("31+9 = 40")
    if num1 == 31 and sign == '+' and num2 == 10:
        return("31+10 = 41")
    if num1 == 31 and sign == '+' and num2 == 11:
        return("31+11 = 42")
    if num1 == 31 and sign == '+' and num2 == 12:
        return("31+12 = 43")
    if num1 == 31 and sign == '+' and num2 == 13:
        return("31+13 = 44")
    if num1 == 31 and sign == '+' and num2 == 14:
        return("31+14 = 45")
    if num1 == 31 and sign == '+' and num2 == 15:
        return("31+15 = 46")
    if num1 == 31 and sign == '+' and num2 == 16:
        return("31+16 = 47")
    if num1 == 31 and sign == '+' and num2 == 17:
        return("31+17 = 48")
    if num1 == 31 and sign == '+' and num2 == 18:
        return("31+18 = 49")
    if num1 == 31 and sign == '+' and num2 == 19:
        return("31+19 = 50")
    if num1 == 31 and sign == '+' and num2 == 20:
        return("31+20 = 51")
    if num1 == 31 and sign == '+' and num2 == 21:
        return("31+21 = 52")
    if num1 == 31 and sign == '+' and num2 == 22:
        return("31+22 = 53")
    if num1 == 31 and sign == '+' and num2 == 23:
        return("31+23 = 54")
    if num1 == 31 and sign == '+' and num2 == 24:
        return("31+24 = 55")
    if num1 == 31 and sign == '+' and num2 == 25:
        return("31+25 = 56")
    if num1 == 31 and sign == '+' and num2 == 26:
        return("31+26 = 57")
    if num1 == 31 and sign == '+' and num2 == 27:
        return("31+27 = 58")
    if num1 == 31 and sign == '+' and num2 == 28:
        return("31+28 = 59")
    if num1 == 31 and sign == '+' and num2 == 29:
        return("31+29 = 60")
    if num1 == 31 and sign == '+' and num2 == 30:
        return("31+30 = 61")
    if num1 == 31 and sign == '+' and num2 == 31:
        return("31+31 = 62")
    if num1 == 31 and sign == '+' and num2 == 32:
        return("31+32 = 63")
    if num1 == 31 and sign == '+' and num2 == 33:
        return("31+33 = 64")
    if num1 == 31 and sign == '+' and num2 == 34:
        return("31+34 = 65")
    if num1 == 31 and sign == '+' and num2 == 35:
        return("31+35 = 66")
    if num1 == 31 and sign == '+' and num2 == 36:
        return("31+36 = 67")
    if num1 == 31 and sign == '+' and num2 == 37:
        return("31+37 = 68")
    if num1 == 31 and sign == '+' and num2 == 38:
        return("31+38 = 69")
    if num1 == 31 and sign == '+' and num2 == 39:
        return("31+39 = 70")
    if num1 == 31 and sign == '+' and num2 == 40:
        return("31+40 = 71")
    if num1 == 31 and sign == '+' and num2 == 41:
        return("31+41 = 72")
    if num1 == 31 and sign == '+' and num2 == 42:
        return("31+42 = 73")
    if num1 == 31 and sign == '+' and num2 == 43:
        return("31+43 = 74")
    if num1 == 31 and sign == '+' and num2 == 44:
        return("31+44 = 75")
    if num1 == 31 and sign == '+' and num2 == 45:
        return("31+45 = 76")
    if num1 == 31 and sign == '+' and num2 == 46:
        return("31+46 = 77")
    if num1 == 31 and sign == '+' and num2 == 47:
        return("31+47 = 78")
    if num1 == 31 and sign == '+' and num2 == 48:
        return("31+48 = 79")
    if num1 == 31 and sign == '+' and num2 == 49:
        return("31+49 = 80")
    if num1 == 31 and sign == '+' and num2 == 50:
        return("31+50 = 81")
    if num1 == 32 and sign == '+' and num2 == 0:
        return("32+0 = 32")
    if num1 == 32 and sign == '+' and num2 == 1:
        return("32+1 = 33")
    if num1 == 32 and sign == '+' and num2 == 2:
        return("32+2 = 34")
    if num1 == 32 and sign == '+' and num2 == 3:
        return("32+3 = 35")
    if num1 == 32 and sign == '+' and num2 == 4:
        return("32+4 = 36")
    if num1 == 32 and sign == '+' and num2 == 5:
        return("32+5 = 37")
    if num1 == 32 and sign == '+' and num2 == 6:
        return("32+6 = 38")
    if num1 == 32 and sign == '+' and num2 == 7:
        return("32+7 = 39")
    if num1 == 32 and sign == '+' and num2 == 8:
        return("32+8 = 40")
    if num1 == 32 and sign == '+' and num2 == 9:
        return("32+9 = 41")
    if num1 == 32 and sign == '+' and num2 == 10:
        return("32+10 = 42")
    if num1 == 32 and sign == '+' and num2 == 11:
        return("32+11 = 43")
    if num1 == 32 and sign == '+' and num2 == 12:
        return("32+12 = 44")
    if num1 == 32 and sign == '+' and num2 == 13:
        return("32+13 = 45")
    if num1 == 32 and sign == '+' and num2 == 14:
        return("32+14 = 46")
    if num1 == 32 and sign == '+' and num2 == 15:
        return("32+15 = 47")
    if num1 == 32 and sign == '+' and num2 == 16:
        return("32+16 = 48")
    if num1 == 32 and sign == '+' and num2 == 17:
        return("32+17 = 49")
    if num1 == 32 and sign == '+' and num2 == 18:
        return("32+18 = 50")
    if num1 == 32 and sign == '+' and num2 == 19:
        return("32+19 = 51")
    if num1 == 32 and sign == '+' and num2 == 20:
        return("32+20 = 52")
    if num1 == 32 and sign == '+' and num2 == 21:
        return("32+21 = 53")
    if num1 == 32 and sign == '+' and num2 == 22:
        return("32+22 = 54")
    if num1 == 32 and sign == '+' and num2 == 23:
        return("32+23 = 55")
    if num1 == 32 and sign == '+' and num2 == 24:
        return("32+24 = 56")
    if num1 == 32 and sign == '+' and num2 == 25:
        return("32+25 = 57")
    if num1 == 32 and sign == '+' and num2 == 26:
        return("32+26 = 58")
    if num1 == 32 and sign == '+' and num2 == 27:
        return("32+27 = 59")
    if num1 == 32 and sign == '+' and num2 == 28:
        return("32+28 = 60")
    if num1 == 32 and sign == '+' and num2 == 29:
        return("32+29 = 61")
    if num1 == 32 and sign == '+' and num2 == 30:
        return("32+30 = 62")
    if num1 == 32 and sign == '+' and num2 == 31:
        return("32+31 = 63")
    if num1 == 32 and sign == '+' and num2 == 32:
        return("32+32 = 64")
    if num1 == 32 and sign == '+' and num2 == 33:
        return("32+33 = 65")
    if num1 == 32 and sign == '+' and num2 == 34:
        return("32+34 = 66")
    if num1 == 32 and sign == '+' and num2 == 35:
        return("32+35 = 67")
    if num1 == 32 and sign == '+' and num2 == 36:
        return("32+36 = 68")
    if num1 == 32 and sign == '+' and num2 == 37:
        return("32+37 = 69")
    if num1 == 32 and sign == '+' and num2 == 38:
        return("32+38 = 70")
    if num1 == 32 and sign == '+' and num2 == 39:
        return("32+39 = 71")
    if num1 == 32 and sign == '+' and num2 == 40:
        return("32+40 = 72")
    if num1 == 32 and sign == '+' and num2 == 41:
        return("32+41 = 73")
    if num1 == 32 and sign == '+' and num2 == 42:
        return("32+42 = 74")
    if num1 == 32 and sign == '+' and num2 == 43:
        return("32+43 = 75")
    if num1 == 32 and sign == '+' and num2 == 44:
        return("32+44 = 76")
    if num1 == 32 and sign == '+' and num2 == 45:
        return("32+45 = 77")
    if num1 == 32 and sign == '+' and num2 == 46:
        return("32+46 = 78")
    if num1 == 32 and sign == '+' and num2 == 47:
        return("32+47 = 79")
    if num1 == 32 and sign == '+' and num2 == 48:
        return("32+48 = 80")
    if num1 == 32 and sign == '+' and num2 == 49:
        return("32+49 = 81")
    if num1 == 32 and sign == '+' and num2 == 50:
        return("32+50 = 82")
    if num1 == 33 and sign == '+' and num2 == 0:
        return("33+0 = 33")
    if num1 == 33 and sign == '+' and num2 == 1:
        return("33+1 = 34")
    if num1 == 33 and sign == '+' and num2 == 2:
        return("33+2 = 35")
    if num1 == 33 and sign == '+' and num2 == 3:
        return("33+3 = 36")
    if num1 == 33 and sign == '+' and num2 == 4:
        return("33+4 = 37")
    if num1 == 33 and sign == '+' and num2 == 5:
        return("33+5 = 38")
    if num1 == 33 and sign == '+' and num2 == 6:
        return("33+6 = 39")
    if num1 == 33 and sign == '+' and num2 == 7:
        return("33+7 = 40")
    if num1 == 33 and sign == '+' and num2 == 8:
        return("33+8 = 41")
    if num1 == 33 and sign == '+' and num2 == 9:
        return("33+9 = 42")
    if num1 == 33 and sign == '+' and num2 == 10:
        return("33+10 = 43")
    if num1 == 33 and sign == '+' and num2 == 11:
        return("33+11 = 44")
    if num1 == 33 and sign == '+' and num2 == 12:
        return("33+12 = 45")
    if num1 == 33 and sign == '+' and num2 == 13:
        return("33+13 = 46")
    if num1 == 33 and sign == '+' and num2 == 14:
        return("33+14 = 47")
    if num1 == 33 and sign == '+' and num2 == 15:
        return("33+15 = 48")
    if num1 == 33 and sign == '+' and num2 == 16:
        return("33+16 = 49")
    if num1 == 33 and sign == '+' and num2 == 17:
        return("33+17 = 50")
    if num1 == 33 and sign == '+' and num2 == 18:
        return("33+18 = 51")
    if num1 == 33 and sign == '+' and num2 == 19:
        return("33+19 = 52")
    if num1 == 33 and sign == '+' and num2 == 20:
        return("33+20 = 53")
    if num1 == 33 and sign == '+' and num2 == 21:
        return("33+21 = 54")
    if num1 == 33 and sign == '+' and num2 == 22:
        return("33+22 = 55")
    if num1 == 33 and sign == '+' and num2 == 23:
        return("33+23 = 56")
    if num1 == 33 and sign == '+' and num2 == 24:
        return("33+24 = 57")
    if num1 == 33 and sign == '+' and num2 == 25:
        return("33+25 = 58")
    if num1 == 33 and sign == '+' and num2 == 26:
        return("33+26 = 59")
    if num1 == 33 and sign == '+' and num2 == 27:
        return("33+27 = 60")
    if num1 == 33 and sign == '+' and num2 == 28:
        return("33+28 = 61")
    if num1 == 33 and sign == '+' and num2 == 29:
        return("33+29 = 62")
    if num1 == 33 and sign == '+' and num2 == 30:
        return("33+30 = 63")
    if num1 == 33 and sign == '+' and num2 == 31:
        return("33+31 = 64")
    if num1 == 33 and sign == '+' and num2 == 32:
        return("33+32 = 65")
    if num1 == 33 and sign == '+' and num2 == 33:
        return("33+33 = 66")
    if num1 == 33 and sign == '+' and num2 == 34:
        return("33+34 = 67")
    if num1 == 33 and sign == '+' and num2 == 35:
        return("33+35 = 68")
    if num1 == 33 and sign == '+' and num2 == 36:
        return("33+36 = 69")
    if num1 == 33 and sign == '+' and num2 == 37:
        return("33+37 = 70")
    if num1 == 33 and sign == '+' and num2 == 38:
        return("33+38 = 71")
    if num1 == 33 and sign == '+' and num2 == 39:
        return("33+39 = 72")
    if num1 == 33 and sign == '+' and num2 == 40:
        return("33+40 = 73")
    if num1 == 33 and sign == '+' and num2 == 41:
        return("33+41 = 74")
    if num1 == 33 and sign == '+' and num2 == 42:
        return("33+42 = 75")
    if num1 == 33 and sign == '+' and num2 == 43:
        return("33+43 = 76")
    if num1 == 33 and sign == '+' and num2 == 44:
        return("33+44 = 77")
    if num1 == 33 and sign == '+' and num2 == 45:
        return("33+45 = 78")
    if num1 == 33 and sign == '+' and num2 == 46:
        return("33+46 = 79")
    if num1 == 33 and sign == '+' and num2 == 47:
        return("33+47 = 80")
    if num1 == 33 and sign == '+' and num2 == 48:
        return("33+48 = 81")
    if num1 == 33 and sign == '+' and num2 == 49:
        return("33+49 = 82")
    if num1 == 33 and sign == '+' and num2 == 50:
        return("33+50 = 83")
    if num1 == 34 and sign == '+' and num2 == 0:
        return("34+0 = 34")
    if num1 == 34 and sign == '+' and num2 == 1:
        return("34+1 = 35")
    if num1 == 34 and sign == '+' and num2 == 2:
        return("34+2 = 36")
    if num1 == 34 and sign == '+' and num2 == 3:
        return("34+3 = 37")
    if num1 == 34 and sign == '+' and num2 == 4:
        return("34+4 = 38")
    if num1 == 34 and sign == '+' and num2 == 5:
        return("34+5 = 39")
    if num1 == 34 and sign == '+' and num2 == 6:
        return("34+6 = 40")
    if num1 == 34 and sign == '+' and num2 == 7:
        return("34+7 = 41")
    if num1 == 34 and sign == '+' and num2 == 8:
        return("34+8 = 42")
    if num1 == 34 and sign == '+' and num2 == 9:
        return("34+9 = 43")
    if num1 == 34 and sign == '+' and num2 == 10:
        return("34+10 = 44")
    if num1 == 34 and sign == '+' and num2 == 11:
        return("34+11 = 45")
    if num1 == 34 and sign == '+' and num2 == 12:
        return("34+12 = 46")
    if num1 == 34 and sign == '+' and num2 == 13:
        return("34+13 = 47")
    if num1 == 34 and sign == '+' and num2 == 14:
        return("34+14 = 48")
    if num1 == 34 and sign == '+' and num2 == 15:
        return("34+15 = 49")
    if num1 == 34 and sign == '+' and num2 == 16:
        return("34+16 = 50")
    if num1 == 34 and sign == '+' and num2 == 17:
        return("34+17 = 51")
    if num1 == 34 and sign == '+' and num2 == 18:
        return("34+18 = 52")
    if num1 == 34 and sign == '+' and num2 == 19:
        return("34+19 = 53")
    if num1 == 34 and sign == '+' and num2 == 20:
        return("34+20 = 54")
    if num1 == 34 and sign == '+' and num2 == 21:
        return("34+21 = 55")
    if num1 == 34 and sign == '+' and num2 == 22:
        return("34+22 = 56")
    if num1 == 34 and sign == '+' and num2 == 23:
        return("34+23 = 57")
    if num1 == 34 and sign == '+' and num2 == 24:
        return("34+24 = 58")
    if num1 == 34 and sign == '+' and num2 == 25:
        return("34+25 = 59")
    if num1 == 34 and sign == '+' and num2 == 26:
        return("34+26 = 60")
    if num1 == 34 and sign == '+' and num2 == 27:
        return("34+27 = 61")
    if num1 == 34 and sign == '+' and num2 == 28:
        return("34+28 = 62")
    if num1 == 34 and sign == '+' and num2 == 29:
        return("34+29 = 63")
    if num1 == 34 and sign == '+' and num2 == 30:
        return("34+30 = 64")
    if num1 == 34 and sign == '+' and num2 == 31:
        return("34+31 = 65")
    if num1 == 34 and sign == '+' and num2 == 32:
        return("34+32 = 66")
    if num1 == 34 and sign == '+' and num2 == 33:
        return("34+33 = 67")
    if num1 == 34 and sign == '+' and num2 == 34:
        return("34+34 = 68")
    if num1 == 34 and sign == '+' and num2 == 35:
        return("34+35 = 69")
    if num1 == 34 and sign == '+' and num2 == 36:
        return("34+36 = 70")
    if num1 == 34 and sign == '+' and num2 == 37:
        return("34+37 = 71")
    if num1 == 34 and sign == '+' and num2 == 38:
        return("34+38 = 72")
    if num1 == 34 and sign == '+' and num2 == 39:
        return("34+39 = 73")
    if num1 == 34 and sign == '+' and num2 == 40:
        return("34+40 = 74")
    if num1 == 34 and sign == '+' and num2 == 41:
        return("34+41 = 75")
    if num1 == 34 and sign == '+' and num2 == 42:
        return("34+42 = 76")
    if num1 == 34 and sign == '+' and num2 == 43:
        return("34+43 = 77")
    if num1 == 34 and sign == '+' and num2 == 44:
        return("34+44 = 78")
    if num1 == 34 and sign == '+' and num2 == 45:
        return("34+45 = 79")
    if num1 == 34 and sign == '+' and num2 == 46:
        return("34+46 = 80")
    if num1 == 34 and sign == '+' and num2 == 47:
        return("34+47 = 81")
    if num1 == 34 and sign == '+' and num2 == 48:
        return("34+48 = 82")
    if num1 == 34 and sign == '+' and num2 == 49:
        return("34+49 = 83")
    if num1 == 34 and sign == '+' and num2 == 50:
        return("34+50 = 84")
    if num1 == 35 and sign == '+' and num2 == 0:
        return("35+0 = 35")
    if num1 == 35 and sign == '+' and num2 == 1:
        return("35+1 = 36")
    if num1 == 35 and sign == '+' and num2 == 2:
        return("35+2 = 37")
    if num1 == 35 and sign == '+' and num2 == 3:
        return("35+3 = 38")
    if num1 == 35 and sign == '+' and num2 == 4:
        return("35+4 = 39")
    if num1 == 35 and sign == '+' and num2 == 5:
        return("35+5 = 40")
    if num1 == 35 and sign == '+' and num2 == 6:
        return("35+6 = 41")
    if num1 == 35 and sign == '+' and num2 == 7:
        return("35+7 = 42")
    if num1 == 35 and sign == '+' and num2 == 8:
        return("35+8 = 43")
    if num1 == 35 and sign == '+' and num2 == 9:
        return("35+9 = 44")
    if num1 == 35 and sign == '+' and num2 == 10:
        return("35+10 = 45")
    if num1 == 35 and sign == '+' and num2 == 11:
        return("35+11 = 46")
    if num1 == 35 and sign == '+' and num2 == 12:
        return("35+12 = 47")
    if num1 == 35 and sign == '+' and num2 == 13:
        return("35+13 = 48")
    if num1 == 35 and sign == '+' and num2 == 14:
        return("35+14 = 49")
    if num1 == 35 and sign == '+' and num2 == 15:
        return("35+15 = 50")
    if num1 == 35 and sign == '+' and num2 == 16:
        return("35+16 = 51")
    if num1 == 35 and sign == '+' and num2 == 17:
        return("35+17 = 52")
    if num1 == 35 and sign == '+' and num2 == 18:
        return("35+18 = 53")
    if num1 == 35 and sign == '+' and num2 == 19:
        return("35+19 = 54")
    if num1 == 35 and sign == '+' and num2 == 20:
        return("35+20 = 55")
    if num1 == 35 and sign == '+' and num2 == 21:
        return("35+21 = 56")
    if num1 == 35 and sign == '+' and num2 == 22:
        return("35+22 = 57")
    if num1 == 35 and sign == '+' and num2 == 23:
        return("35+23 = 58")
    if num1 == 35 and sign == '+' and num2 == 24:
        return("35+24 = 59")
    if num1 == 35 and sign == '+' and num2 == 25:
        return("35+25 = 60")
    if num1 == 35 and sign == '+' and num2 == 26:
        return("35+26 = 61")
    if num1 == 35 and sign == '+' and num2 == 27:
        return("35+27 = 62")
    if num1 == 35 and sign == '+' and num2 == 28:
        return("35+28 = 63")
    if num1 == 35 and sign == '+' and num2 == 29:
        return("35+29 = 64")
    if num1 == 35 and sign == '+' and num2 == 30:
        return("35+30 = 65")
    if num1 == 35 and sign == '+' and num2 == 31:
        return("35+31 = 66")
    if num1 == 35 and sign == '+' and num2 == 32:
        return("35+32 = 67")
    if num1 == 35 and sign == '+' and num2 == 33:
        return("35+33 = 68")
    if num1 == 35 and sign == '+' and num2 == 34:
        return("35+34 = 69")
    if num1 == 35 and sign == '+' and num2 == 35:
        return("35+35 = 70")
    if num1 == 35 and sign == '+' and num2 == 36:
        return("35+36 = 71")
    if num1 == 35 and sign == '+' and num2 == 37:
        return("35+37 = 72")
    if num1 == 35 and sign == '+' and num2 == 38:
        return("35+38 = 73")
    if num1 == 35 and sign == '+' and num2 == 39:
        return("35+39 = 74")
    if num1 == 35 and sign == '+' and num2 == 40:
        return("35+40 = 75")
    if num1 == 35 and sign == '+' and num2 == 41:
        return("35+41 = 76")
    if num1 == 35 and sign == '+' and num2 == 42:
        return("35+42 = 77")
    if num1 == 35 and sign == '+' and num2 == 43:
        return("35+43 = 78")
    if num1 == 35 and sign == '+' and num2 == 44:
        return("35+44 = 79")
    if num1 == 35 and sign == '+' and num2 == 45:
        return("35+45 = 80")
    if num1 == 35 and sign == '+' and num2 == 46:
        return("35+46 = 81")
    if num1 == 35 and sign == '+' and num2 == 47:
        return("35+47 = 82")
    if num1 == 35 and sign == '+' and num2 == 48:
        return("35+48 = 83")
    if num1 == 35 and sign == '+' and num2 == 49:
        return("35+49 = 84")
    if num1 == 35 and sign == '+' and num2 == 50:
        return("35+50 = 85")
    if num1 == 36 and sign == '+' and num2 == 0:
        return("36+0 = 36")
    if num1 == 36 and sign == '+' and num2 == 1:
        return("36+1 = 37")
    if num1 == 36 and sign == '+' and num2 == 2:
        return("36+2 = 38")
    if num1 == 36 and sign == '+' and num2 == 3:
        return("36+3 = 39")
    if num1 == 36 and sign == '+' and num2 == 4:
        return("36+4 = 40")
    if num1 == 36 and sign == '+' and num2 == 5:
        return("36+5 = 41")
    if num1 == 36 and sign == '+' and num2 == 6:
        return("36+6 = 42")
    if num1 == 36 and sign == '+' and num2 == 7:
        return("36+7 = 43")
    if num1 == 36 and sign == '+' and num2 == 8:
        return("36+8 = 44")
    if num1 == 36 and sign == '+' and num2 == 9:
        return("36+9 = 45")
    if num1 == 36 and sign == '+' and num2 == 10:
        return("36+10 = 46")
    if num1 == 36 and sign == '+' and num2 == 11:
        return("36+11 = 47")
    if num1 == 36 and sign == '+' and num2 == 12:
        return("36+12 = 48")
    if num1 == 36 and sign == '+' and num2 == 13:
        return("36+13 = 49")
    if num1 == 36 and sign == '+' and num2 == 14:
        return("36+14 = 50")
    if num1 == 36 and sign == '+' and num2 == 15:
        return("36+15 = 51")
    if num1 == 36 and sign == '+' and num2 == 16:
        return("36+16 = 52")
    if num1 == 36 and sign == '+' and num2 == 17:
        return("36+17 = 53")
    if num1 == 36 and sign == '+' and num2 == 18:
        return("36+18 = 54")
    if num1 == 36 and sign == '+' and num2 == 19:
        return("36+19 = 55")
    if num1 == 36 and sign == '+' and num2 == 20:
        return("36+20 = 56")
    if num1 == 36 and sign == '+' and num2 == 21:
        return("36+21 = 57")
    if num1 == 36 and sign == '+' and num2 == 22:
        return("36+22 = 58")
    if num1 == 36 and sign == '+' and num2 == 23:
        return("36+23 = 59")
    if num1 == 36 and sign == '+' and num2 == 24:
        return("36+24 = 60")
    if num1 == 36 and sign == '+' and num2 == 25:
        return("36+25 = 61")
    if num1 == 36 and sign == '+' and num2 == 26:
        return("36+26 = 62")
    if num1 == 36 and sign == '+' and num2 == 27:
        return("36+27 = 63")
    if num1 == 36 and sign == '+' and num2 == 28:
        return("36+28 = 64")
    if num1 == 36 and sign == '+' and num2 == 29:
        return("36+29 = 65")
    if num1 == 36 and sign == '+' and num2 == 30:
        return("36+30 = 66")
    if num1 == 36 and sign == '+' and num2 == 31:
        return("36+31 = 67")
    if num1 == 36 and sign == '+' and num2 == 32:
        return("36+32 = 68")
    if num1 == 36 and sign == '+' and num2 == 33:
        return("36+33 = 69")
    if num1 == 36 and sign == '+' and num2 == 34:
        return("36+34 = 70")
    if num1 == 36 and sign == '+' and num2 == 35:
        return("36+35 = 71")
    if num1 == 36 and sign == '+' and num2 == 36:
        return("36+36 = 72")
    if num1 == 36 and sign == '+' and num2 == 37:
        return("36+37 = 73")
    if num1 == 36 and sign == '+' and num2 == 38:
        return("36+38 = 74")
    if num1 == 36 and sign == '+' and num2 == 39:
        return("36+39 = 75")
    if num1 == 36 and sign == '+' and num2 == 40:
        return("36+40 = 76")
    if num1 == 36 and sign == '+' and num2 == 41:
        return("36+41 = 77")
    if num1 == 36 and sign == '+' and num2 == 42:
        return("36+42 = 78")
    if num1 == 36 and sign == '+' and num2 == 43:
        return("36+43 = 79")
    if num1 == 36 and sign == '+' and num2 == 44:
        return("36+44 = 80")
    if num1 == 36 and sign == '+' and num2 == 45:
        return("36+45 = 81")
    if num1 == 36 and sign == '+' and num2 == 46:
        return("36+46 = 82")
    if num1 == 36 and sign == '+' and num2 == 47:
        return("36+47 = 83")
    if num1 == 36 and sign == '+' and num2 == 48:
        return("36+48 = 84")
    if num1 == 36 and sign == '+' and num2 == 49:
        return("36+49 = 85")
    if num1 == 36 and sign == '+' and num2 == 50:
        return("36+50 = 86")
    if num1 == 37 and sign == '+' and num2 == 0:
        return("37+0 = 37")
    if num1 == 37 and sign == '+' and num2 == 1:
        return("37+1 = 38")
    if num1 == 37 and sign == '+' and num2 == 2:
        return("37+2 = 39")
    if num1 == 37 and sign == '+' and num2 == 3:
        return("37+3 = 40")
    if num1 == 37 and sign == '+' and num2 == 4:
        return("37+4 = 41")
    if num1 == 37 and sign == '+' and num2 == 5:
        return("37+5 = 42")
    if num1 == 37 and sign == '+' and num2 == 6:
        return("37+6 = 43")
    if num1 == 37 and sign == '+' and num2 == 7:
        return("37+7 = 44")
    if num1 == 37 and sign == '+' and num2 == 8:
        return("37+8 = 45")
    if num1 == 37 and sign == '+' and num2 == 9:
        return("37+9 = 46")
    if num1 == 37 and sign == '+' and num2 == 10:
        return("37+10 = 47")
    if num1 == 37 and sign == '+' and num2 == 11:
        return("37+11 = 48")
    if num1 == 37 and sign == '+' and num2 == 12:
        return("37+12 = 49")
    if num1 == 37 and sign == '+' and num2 == 13:
        return("37+13 = 50")
    if num1 == 37 and sign == '+' and num2 == 14:
        return("37+14 = 51")
    if num1 == 37 and sign == '+' and num2 == 15:
        return("37+15 = 52")
    if num1 == 37 and sign == '+' and num2 == 16:
        return("37+16 = 53")
    if num1 == 37 and sign == '+' and num2 == 17:
        return("37+17 = 54")
    if num1 == 37 and sign == '+' and num2 == 18:
        return("37+18 = 55")
    if num1 == 37 and sign == '+' and num2 == 19:
        return("37+19 = 56")
    if num1 == 37 and sign == '+' and num2 == 20:
        return("37+20 = 57")
    if num1 == 37 and sign == '+' and num2 == 21:
        return("37+21 = 58")
    if num1 == 37 and sign == '+' and num2 == 22:
        return("37+22 = 59")
    if num1 == 37 and sign == '+' and num2 == 23:
        return("37+23 = 60")
    if num1 == 37 and sign == '+' and num2 == 24:
        return("37+24 = 61")
    if num1 == 37 and sign == '+' and num2 == 25:
        return("37+25 = 62")
    if num1 == 37 and sign == '+' and num2 == 26:
        return("37+26 = 63")
    if num1 == 37 and sign == '+' and num2 == 27:
        return("37+27 = 64")
    if num1 == 37 and sign == '+' and num2 == 28:
        return("37+28 = 65")
    if num1 == 37 and sign == '+' and num2 == 29:
        return("37+29 = 66")
    if num1 == 37 and sign == '+' and num2 == 30:
        return("37+30 = 67")
    if num1 == 37 and sign == '+' and num2 == 31:
        return("37+31 = 68")
    if num1 == 37 and sign == '+' and num2 == 32:
        return("37+32 = 69")
    if num1 == 37 and sign == '+' and num2 == 33:
        return("37+33 = 70")
    if num1 == 37 and sign == '+' and num2 == 34:
        return("37+34 = 71")
    if num1 == 37 and sign == '+' and num2 == 35:
        return("37+35 = 72")
    if num1 == 37 and sign == '+' and num2 == 36:
        return("37+36 = 73")
    if num1 == 37 and sign == '+' and num2 == 37:
        return("37+37 = 74")
    if num1 == 37 and sign == '+' and num2 == 38:
        return("37+38 = 75")
    if num1 == 37 and sign == '+' and num2 == 39:
        return("37+39 = 76")
    if num1 == 37 and sign == '+' and num2 == 40:
        return("37+40 = 77")
    if num1 == 37 and sign == '+' and num2 == 41:
        return("37+41 = 78")
    if num1 == 37 and sign == '+' and num2 == 42:
        return("37+42 = 79")
    if num1 == 37 and sign == '+' and num2 == 43:
        return("37+43 = 80")
    if num1 == 37 and sign == '+' and num2 == 44:
        return("37+44 = 81")
    if num1 == 37 and sign == '+' and num2 == 45:
        return("37+45 = 82")
    if num1 == 37 and sign == '+' and num2 == 46:
        return("37+46 = 83")
    if num1 == 37 and sign == '+' and num2 == 47:
        return("37+47 = 84")
    if num1 == 37 and sign == '+' and num2 == 48:
        return("37+48 = 85")
    if num1 == 37 and sign == '+' and num2 == 49:
        return("37+49 = 86")
    if num1 == 37 and sign == '+' and num2 == 50:
        return("37+50 = 87")
    if num1 == 38 and sign == '+' and num2 == 0:
        return("38+0 = 38")
    if num1 == 38 and sign == '+' and num2 == 1:
        return("38+1 = 39")
    if num1 == 38 and sign == '+' and num2 == 2:
        return("38+2 = 40")
    if num1 == 38 and sign == '+' and num2 == 3:
        return("38+3 = 41")
    if num1 == 38 and sign == '+' and num2 == 4:
        return("38+4 = 42")
    if num1 == 38 and sign == '+' and num2 == 5:
        return("38+5 = 43")
    if num1 == 38 and sign == '+' and num2 == 6:
        return("38+6 = 44")
    if num1 == 38 and sign == '+' and num2 == 7:
        return("38+7 = 45")
    if num1 == 38 and sign == '+' and num2 == 8:
        return("38+8 = 46")
    if num1 == 38 and sign == '+' and num2 == 9:
        return("38+9 = 47")
    if num1 == 38 and sign == '+' and num2 == 10:
        return("38+10 = 48")
    if num1 == 38 and sign == '+' and num2 == 11:
        return("38+11 = 49")
    if num1 == 38 and sign == '+' and num2 == 12:
        return("38+12 = 50")
    if num1 == 38 and sign == '+' and num2 == 13:
        return("38+13 = 51")
    if num1 == 38 and sign == '+' and num2 == 14:
        return("38+14 = 52")
    if num1 == 38 and sign == '+' and num2 == 15:
        return("38+15 = 53")
    if num1 == 38 and sign == '+' and num2 == 16:
        return("38+16 = 54")
    if num1 == 38 and sign == '+' and num2 == 17:
        return("38+17 = 55")
    if num1 == 38 and sign == '+' and num2 == 18:
        return("38+18 = 56")
    if num1 == 38 and sign == '+' and num2 == 19:
        return("38+19 = 57")
    if num1 == 38 and sign == '+' and num2 == 20:
        return("38+20 = 58")
    if num1 == 38 and sign == '+' and num2 == 21:
        return("38+21 = 59")
    if num1 == 38 and sign == '+' and num2 == 22:
        return("38+22 = 60")
    if num1 == 38 and sign == '+' and num2 == 23:
        return("38+23 = 61")
    if num1 == 38 and sign == '+' and num2 == 24:
        return("38+24 = 62")
    if num1 == 38 and sign == '+' and num2 == 25:
        return("38+25 = 63")
    if num1 == 38 and sign == '+' and num2 == 26:
        return("38+26 = 64")
    if num1 == 38 and sign == '+' and num2 == 27:
        return("38+27 = 65")
    if num1 == 38 and sign == '+' and num2 == 28:
        return("38+28 = 66")
    if num1 == 38 and sign == '+' and num2 == 29:
        return("38+29 = 67")
    if num1 == 38 and sign == '+' and num2 == 30:
        return("38+30 = 68")
    if num1 == 38 and sign == '+' and num2 == 31:
        return("38+31 = 69")
    if num1 == 38 and sign == '+' and num2 == 32:
        return("38+32 = 70")
    if num1 == 38 and sign == '+' and num2 == 33:
        return("38+33 = 71")
    if num1 == 38 and sign == '+' and num2 == 34:
        return("38+34 = 72")
    if num1 == 38 and sign == '+' and num2 == 35:
        return("38+35 = 73")
    if num1 == 38 and sign == '+' and num2 == 36:
        return("38+36 = 74")
    if num1 == 38 and sign == '+' and num2 == 37:
        return("38+37 = 75")
    if num1 == 38 and sign == '+' and num2 == 38:
        return("38+38 = 76")
    if num1 == 38 and sign == '+' and num2 == 39:
        return("38+39 = 77")
    if num1 == 38 and sign == '+' and num2 == 40:
        return("38+40 = 78")
    if num1 == 38 and sign == '+' and num2 == 41:
        return("38+41 = 79")
    if num1 == 38 and sign == '+' and num2 == 42:
        return("38+42 = 80")
    if num1 == 38 and sign == '+' and num2 == 43:
        return("38+43 = 81")
    if num1 == 38 and sign == '+' and num2 == 44:
        return("38+44 = 82")
    if num1 == 38 and sign == '+' and num2 == 45:
        return("38+45 = 83")
    if num1 == 38 and sign == '+' and num2 == 46:
        return("38+46 = 84")
    if num1 == 38 and sign == '+' and num2 == 47:
        return("38+47 = 85")
    if num1 == 38 and sign == '+' and num2 == 48:
        return("38+48 = 86")
    if num1 == 38 and sign == '+' and num2 == 49:
        return("38+49 = 87")
    if num1 == 38 and sign == '+' and num2 == 50:
        return("38+50 = 88")
    if num1 == 39 and sign == '+' and num2 == 0:
        return("39+0 = 39")
    if num1 == 39 and sign == '+' and num2 == 1:
        return("39+1 = 40")
    if num1 == 39 and sign == '+' and num2 == 2:
        return("39+2 = 41")
    if num1 == 39 and sign == '+' and num2 == 3:
        return("39+3 = 42")
    if num1 == 39 and sign == '+' and num2 == 4:
        return("39+4 = 43")
    if num1 == 39 and sign == '+' and num2 == 5:
        return("39+5 = 44")
    if num1 == 39 and sign == '+' and num2 == 6:
        return("39+6 = 45")
    if num1 == 39 and sign == '+' and num2 == 7:
        return("39+7 = 46")
    if num1 == 39 and sign == '+' and num2 == 8:
        return("39+8 = 47")
    if num1 == 39 and sign == '+' and num2 == 9:
        return("39+9 = 48")
    if num1 == 39 and sign == '+' and num2 == 10:
        return("39+10 = 49")
    if num1 == 39 and sign == '+' and num2 == 11:
        return("39+11 = 50")
    if num1 == 39 and sign == '+' and num2 == 12:
        return("39+12 = 51")
    if num1 == 39 and sign == '+' and num2 == 13:
        return("39+13 = 52")
    if num1 == 39 and sign == '+' and num2 == 14:
        return("39+14 = 53")
    if num1 == 39 and sign == '+' and num2 == 15:
        return("39+15 = 54")
    if num1 == 39 and sign == '+' and num2 == 16:
        return("39+16 = 55")
    if num1 == 39 and sign == '+' and num2 == 17:
        return("39+17 = 56")
    if num1 == 39 and sign == '+' and num2 == 18:
        return("39+18 = 57")
    if num1 == 39 and sign == '+' and num2 == 19:
        return("39+19 = 58")
    if num1 == 39 and sign == '+' and num2 == 20:
        return("39+20 = 59")
    if num1 == 39 and sign == '+' and num2 == 21:
        return("39+21 = 60")
    if num1 == 39 and sign == '+' and num2 == 22:
        return("39+22 = 61")
    if num1 == 39 and sign == '+' and num2 == 23:
        return("39+23 = 62")
    if num1 == 39 and sign == '+' and num2 == 24:
        return("39+24 = 63")
    if num1 == 39 and sign == '+' and num2 == 25:
        return("39+25 = 64")
    if num1 == 39 and sign == '+' and num2 == 26:
        return("39+26 = 65")
    if num1 == 39 and sign == '+' and num2 == 27:
        return("39+27 = 66")
    if num1 == 39 and sign == '+' and num2 == 28:
        return("39+28 = 67")
    if num1 == 39 and sign == '+' and num2 == 29:
        return("39+29 = 68")
    if num1 == 39 and sign == '+' and num2 == 30:
        return("39+30 = 69")
    if num1 == 39 and sign == '+' and num2 == 31:
        return("39+31 = 70")
    if num1 == 39 and sign == '+' and num2 == 32:
        return("39+32 = 71")
    if num1 == 39 and sign == '+' and num2 == 33:
        return("39+33 = 72")
    if num1 == 39 and sign == '+' and num2 == 34:
        return("39+34 = 73")
    if num1 == 39 and sign == '+' and num2 == 35:
        return("39+35 = 74")
    if num1 == 39 and sign == '+' and num2 == 36:
        return("39+36 = 75")
    if num1 == 39 and sign == '+' and num2 == 37:
        return("39+37 = 76")
    if num1 == 39 and sign == '+' and num2 == 38:
        return("39+38 = 77")
    if num1 == 39 and sign == '+' and num2 == 39:
        return("39+39 = 78")
    if num1 == 39 and sign == '+' and num2 == 40:
        return("39+40 = 79")
    if num1 == 39 and sign == '+' and num2 == 41:
        return("39+41 = 80")
    if num1 == 39 and sign == '+' and num2 == 42:
        return("39+42 = 81")
    if num1 == 39 and sign == '+' and num2 == 43:
        return("39+43 = 82")
    if num1 == 39 and sign == '+' and num2 == 44:
        return("39+44 = 83")
    if num1 == 39 and sign == '+' and num2 == 45:
        return("39+45 = 84")
    if num1 == 39 and sign == '+' and num2 == 46:
        return("39+46 = 85")
    if num1 == 39 and sign == '+' and num2 == 47:
        return("39+47 = 86")
    if num1 == 39 and sign == '+' and num2 == 48:
        return("39+48 = 87")
    if num1 == 39 and sign == '+' and num2 == 49:
        return("39+49 = 88")
    if num1 == 39 and sign == '+' and num2 == 50:
        return("39+50 = 89")
    if num1 == 40 and sign == '+' and num2 == 0:
        return("40+0 = 40")
    if num1 == 40 and sign == '+' and num2 == 1:
        return("40+1 = 41")
    if num1 == 40 and sign == '+' and num2 == 2:
        return("40+2 = 42")
    if num1 == 40 and sign == '+' and num2 == 3:
        return("40+3 = 43")
    if num1 == 40 and sign == '+' and num2 == 4:
        return("40+4 = 44")
    if num1 == 40 and sign == '+' and num2 == 5:
        return("40+5 = 45")
    if num1 == 40 and sign == '+' and num2 == 6:
        return("40+6 = 46")
    if num1 == 40 and sign == '+' and num2 == 7:
        return("40+7 = 47")
    if num1 == 40 and sign == '+' and num2 == 8:
        return("40+8 = 48")
    if num1 == 40 and sign == '+' and num2 == 9:
        return("40+9 = 49")
    if num1 == 40 and sign == '+' and num2 == 10:
        return("40+10 = 50")
    if num1 == 40 and sign == '+' and num2 == 11:
        return("40+11 = 51")
    if num1 == 40 and sign == '+' and num2 == 12:
        return("40+12 = 52")
    if num1 == 40 and sign == '+' and num2 == 13:
        return("40+13 = 53")
    if num1 == 40 and sign == '+' and num2 == 14:
        return("40+14 = 54")
    if num1 == 40 and sign == '+' and num2 == 15:
        return("40+15 = 55")
    if num1 == 40 and sign == '+' and num2 == 16:
        return("40+16 = 56")
    if num1 == 40 and sign == '+' and num2 == 17:
        return("40+17 = 57")
    if num1 == 40 and sign == '+' and num2 == 18:
        return("40+18 = 58")
    if num1 == 40 and sign == '+' and num2 == 19:
        return("40+19 = 59")
    if num1 == 40 and sign == '+' and num2 == 20:
        return("40+20 = 60")
    if num1 == 40 and sign == '+' and num2 == 21:
        return("40+21 = 61")
    if num1 == 40 and sign == '+' and num2 == 22:
        return("40+22 = 62")
    if num1 == 40 and sign == '+' and num2 == 23:
        return("40+23 = 63")
    if num1 == 40 and sign == '+' and num2 == 24:
        return("40+24 = 64")
    if num1 == 40 and sign == '+' and num2 == 25:
        return("40+25 = 65")
    if num1 == 40 and sign == '+' and num2 == 26:
        return("40+26 = 66")
    if num1 == 40 and sign == '+' and num2 == 27:
        return("40+27 = 67")
    if num1 == 40 and sign == '+' and num2 == 28:
        return("40+28 = 68")
    if num1 == 40 and sign == '+' and num2 == 29:
        return("40+29 = 69")
    if num1 == 40 and sign == '+' and num2 == 30:
        return("40+30 = 70")
    if num1 == 40 and sign == '+' and num2 == 31:
        return("40+31 = 71")
    if num1 == 40 and sign == '+' and num2 == 32:
        return("40+32 = 72")
    if num1 == 40 and sign == '+' and num2 == 33:
        return("40+33 = 73")
    if num1 == 40 and sign == '+' and num2 == 34:
        return("40+34 = 74")
    if num1 == 40 and sign == '+' and num2 == 35:
        return("40+35 = 75")
    if num1 == 40 and sign == '+' and num2 == 36:
        return("40+36 = 76")
    if num1 == 40 and sign == '+' and num2 == 37:
        return("40+37 = 77")
    if num1 == 40 and sign == '+' and num2 == 38:
        return("40+38 = 78")
    if num1 == 40 and sign == '+' and num2 == 39:
        return("40+39 = 79")
    if num1 == 40 and sign == '+' and num2 == 40:
        return("40+40 = 80")
    if num1 == 40 and sign == '+' and num2 == 41:
        return("40+41 = 81")
    if num1 == 40 and sign == '+' and num2 == 42:
        return("40+42 = 82")
    if num1 == 40 and sign == '+' and num2 == 43:
        return("40+43 = 83")
    if num1 == 40 and sign == '+' and num2 == 44:
        return("40+44 = 84")
    if num1 == 40 and sign == '+' and num2 == 45:
        return("40+45 = 85")
    if num1 == 40 and sign == '+' and num2 == 46:
        return("40+46 = 86")
    if num1 == 40 and sign == '+' and num2 == 47:
        return("40+47 = 87")
    if num1 == 40 and sign == '+' and num2 == 48:
        return("40+48 = 88")
    if num1 == 40 and sign == '+' and num2 == 49:
        return("40+49 = 89")
    if num1 == 40 and sign == '+' and num2 == 50:
        return("40+50 = 90")
    if num1 == 41 and sign == '+' and num2 == 0:
        return("41+0 = 41")
    if num1 == 41 and sign == '+' and num2 == 1:
        return("41+1 = 42")
    if num1 == 41 and sign == '+' and num2 == 2:
        return("41+2 = 43")
    if num1 == 41 and sign == '+' and num2 == 3:
        return("41+3 = 44")
    if num1 == 41 and sign == '+' and num2 == 4:
        return("41+4 = 45")
    if num1 == 41 and sign == '+' and num2 == 5:
        return("41+5 = 46")
    if num1 == 41 and sign == '+' and num2 == 6:
        return("41+6 = 47")
    if num1 == 41 and sign == '+' and num2 == 7:
        return("41+7 = 48")
    if num1 == 41 and sign == '+' and num2 == 8:
        return("41+8 = 49")
    if num1 == 41 and sign == '+' and num2 == 9:
        return("41+9 = 50")
    if num1 == 41 and sign == '+' and num2 == 10:
        return("41+10 = 51")
    if num1 == 41 and sign == '+' and num2 == 11:
        return("41+11 = 52")
    if num1 == 41 and sign == '+' and num2 == 12:
        return("41+12 = 53")
    if num1 == 41 and sign == '+' and num2 == 13:
        return("41+13 = 54")
    if num1 == 41 and sign == '+' and num2 == 14:
        return("41+14 = 55")
    if num1 == 41 and sign == '+' and num2 == 15:
        return("41+15 = 56")
    if num1 == 41 and sign == '+' and num2 == 16:
        return("41+16 = 57")
    if num1 == 41 and sign == '+' and num2 == 17:
        return("41+17 = 58")
    if num1 == 41 and sign == '+' and num2 == 18:
        return("41+18 = 59")
    if num1 == 41 and sign == '+' and num2 == 19:
        return("41+19 = 60")
    if num1 == 41 and sign == '+' and num2 == 20:
        return("41+20 = 61")
    if num1 == 41 and sign == '+' and num2 == 21:
        return("41+21 = 62")
    if num1 == 41 and sign == '+' and num2 == 22:
        return("41+22 = 63")
    if num1 == 41 and sign == '+' and num2 == 23:
        return("41+23 = 64")
    if num1 == 41 and sign == '+' and num2 == 24:
        return("41+24 = 65")
    if num1 == 41 and sign == '+' and num2 == 25:
        return("41+25 = 66")
    if num1 == 41 and sign == '+' and num2 == 26:
        return("41+26 = 67")
    if num1 == 41 and sign == '+' and num2 == 27:
        return("41+27 = 68")
    if num1 == 41 and sign == '+' and num2 == 28:
        return("41+28 = 69")
    if num1 == 41 and sign == '+' and num2 == 29:
        return("41+29 = 70")
    if num1 == 41 and sign == '+' and num2 == 30:
        return("41+30 = 71")
    if num1 == 41 and sign == '+' and num2 == 31:
        return("41+31 = 72")
    if num1 == 41 and sign == '+' and num2 == 32:
        return("41+32 = 73")
    if num1 == 41 and sign == '+' and num2 == 33:
        return("41+33 = 74")
    if num1 == 41 and sign == '+' and num2 == 34:
        return("41+34 = 75")
    if num1 == 41 and sign == '+' and num2 == 35:
        return("41+35 = 76")
    if num1 == 41 and sign == '+' and num2 == 36:
        return("41+36 = 77")
    if num1 == 41 and sign == '+' and num2 == 37:
        return("41+37 = 78")
    if num1 == 41 and sign == '+' and num2 == 38:
        return("41+38 = 79")
    if num1 == 41 and sign == '+' and num2 == 39:
        return("41+39 = 80")
    if num1 == 41 and sign == '+' and num2 == 40:
        return("41+40 = 81")
    if num1 == 41 and sign == '+' and num2 == 41:
        return("41+41 = 82")
    if num1 == 41 and sign == '+' and num2 == 42:
        return("41+42 = 83")
    if num1 == 41 and sign == '+' and num2 == 43:
        return("41+43 = 84")
    if num1 == 41 and sign == '+' and num2 == 44:
        return("41+44 = 85")
    if num1 == 41 and sign == '+' and num2 == 45:
        return("41+45 = 86")
    if num1 == 41 and sign == '+' and num2 == 46:
        return("41+46 = 87")
    if num1 == 41 and sign == '+' and num2 == 47:
        return("41+47 = 88")
    if num1 == 41 and sign == '+' and num2 == 48:
        return("41+48 = 89")
    if num1 == 41 and sign == '+' and num2 == 49:
        return("41+49 = 90")
    if num1 == 41 and sign == '+' and num2 == 50:
        return("41+50 = 91")
    if num1 == 42 and sign == '+' and num2 == 0:
        return("42+0 = 42")
    if num1 == 42 and sign == '+' and num2 == 1:
        return("42+1 = 43")
    if num1 == 42 and sign == '+' and num2 == 2:
        return("42+2 = 44")
    if num1 == 42 and sign == '+' and num2 == 3:
        return("42+3 = 45")
    if num1 == 42 and sign == '+' and num2 == 4:
        return("42+4 = 46")
    if num1 == 42 and sign == '+' and num2 == 5:
        return("42+5 = 47")
    if num1 == 42 and sign == '+' and num2 == 6:
        return("42+6 = 48")
    if num1 == 42 and sign == '+' and num2 == 7:
        return("42+7 = 49")
    if num1 == 42 and sign == '+' and num2 == 8:
        return("42+8 = 50")
    if num1 == 42 and sign == '+' and num2 == 9:
        return("42+9 = 51")
    if num1 == 42 and sign == '+' and num2 == 10:
        return("42+10 = 52")
    if num1 == 42 and sign == '+' and num2 == 11:
        return("42+11 = 53")
    if num1 == 42 and sign == '+' and num2 == 12:
        return("42+12 = 54")
    if num1 == 42 and sign == '+' and num2 == 13:
        return("42+13 = 55")
    if num1 == 42 and sign == '+' and num2 == 14:
        return("42+14 = 56")
    if num1 == 42 and sign == '+' and num2 == 15:
        return("42+15 = 57")
    if num1 == 42 and sign == '+' and num2 == 16:
        return("42+16 = 58")
    if num1 == 42 and sign == '+' and num2 == 17:
        return("42+17 = 59")
    if num1 == 42 and sign == '+' and num2 == 18:
        return("42+18 = 60")
    if num1 == 42 and sign == '+' and num2 == 19:
        return("42+19 = 61")
    if num1 == 42 and sign == '+' and num2 == 20:
        return("42+20 = 62")
    if num1 == 42 and sign == '+' and num2 == 21:
        return("42+21 = 63")
    if num1 == 42 and sign == '+' and num2 == 22:
        return("42+22 = 64")
    if num1 == 42 and sign == '+' and num2 == 23:
        return("42+23 = 65")
    if num1 == 42 and sign == '+' and num2 == 24:
        return("42+24 = 66")
    if num1 == 42 and sign == '+' and num2 == 25:
        return("42+25 = 67")
    if num1 == 42 and sign == '+' and num2 == 26:
        return("42+26 = 68")
    if num1 == 42 and sign == '+' and num2 == 27:
        return("42+27 = 69")
    if num1 == 42 and sign == '+' and num2 == 28:
        return("42+28 = 70")
    if num1 == 42 and sign == '+' and num2 == 29:
        return("42+29 = 71")
    if num1 == 42 and sign == '+' and num2 == 30:
        return("42+30 = 72")
    if num1 == 42 and sign == '+' and num2 == 31:
        return("42+31 = 73")
    if num1 == 42 and sign == '+' and num2 == 32:
        return("42+32 = 74")
    if num1 == 42 and sign == '+' and num2 == 33:
        return("42+33 = 75")
    if num1 == 42 and sign == '+' and num2 == 34:
        return("42+34 = 76")
    if num1 == 42 and sign == '+' and num2 == 35:
        return("42+35 = 77")
    if num1 == 42 and sign == '+' and num2 == 36:
        return("42+36 = 78")
    if num1 == 42 and sign == '+' and num2 == 37:
        return("42+37 = 79")
    if num1 == 42 and sign == '+' and num2 == 38:
        return("42+38 = 80")
    if num1 == 42 and sign == '+' and num2 == 39:
        return("42+39 = 81")
    if num1 == 42 and sign == '+' and num2 == 40:
        return("42+40 = 82")
    if num1 == 42 and sign == '+' and num2 == 41:
        return("42+41 = 83")
    if num1 == 42 and sign == '+' and num2 == 42:
        return("42+42 = 84")
    if num1 == 42 and sign == '+' and num2 == 43:
        return("42+43 = 85")
    if num1 == 42 and sign == '+' and num2 == 44:
        return("42+44 = 86")
    if num1 == 42 and sign == '+' and num2 == 45:
        return("42+45 = 87")
    if num1 == 42 and sign == '+' and num2 == 46:
        return("42+46 = 88")
    if num1 == 42 and sign == '+' and num2 == 47:
        return("42+47 = 89")
    if num1 == 42 and sign == '+' and num2 == 48:
        return("42+48 = 90")
    if num1 == 42 and sign == '+' and num2 == 49:
        return("42+49 = 91")
    if num1 == 42 and sign == '+' and num2 == 50:
        return("42+50 = 92")
    if num1 == 43 and sign == '+' and num2 == 0:
        return("43+0 = 43")
    if num1 == 43 and sign == '+' and num2 == 1:
        return("43+1 = 44")
    if num1 == 43 and sign == '+' and num2 == 2:
        return("43+2 = 45")
    if num1 == 43 and sign == '+' and num2 == 3:
        return("43+3 = 46")
    if num1 == 43 and sign == '+' and num2 == 4:
        return("43+4 = 47")
    if num1 == 43 and sign == '+' and num2 == 5:
        return("43+5 = 48")
    if num1 == 43 and sign == '+' and num2 == 6:
        return("43+6 = 49")
    if num1 == 43 and sign == '+' and num2 == 7:
        return("43+7 = 50")
    if num1 == 43 and sign == '+' and num2 == 8:
        return("43+8 = 51")
    if num1 == 43 and sign == '+' and num2 == 9:
        return("43+9 = 52")
    if num1 == 43 and sign == '+' and num2 == 10:
        return("43+10 = 53")
    if num1 == 43 and sign == '+' and num2 == 11:
        return("43+11 = 54")
    if num1 == 43 and sign == '+' and num2 == 12:
        return("43+12 = 55")
    if num1 == 43 and sign == '+' and num2 == 13:
        return("43+13 = 56")
    if num1 == 43 and sign == '+' and num2 == 14:
        return("43+14 = 57")
    if num1 == 43 and sign == '+' and num2 == 15:
        return("43+15 = 58")
    if num1 == 43 and sign == '+' and num2 == 16:
        return("43+16 = 59")
    if num1 == 43 and sign == '+' and num2 == 17:
        return("43+17 = 60")
    if num1 == 43 and sign == '+' and num2 == 18:
        return("43+18 = 61")
    if num1 == 43 and sign == '+' and num2 == 19:
        return("43+19 = 62")
    if num1 == 43 and sign == '+' and num2 == 20:
        return("43+20 = 63")
    if num1 == 43 and sign == '+' and num2 == 21:
        return("43+21 = 64")
    if num1 == 43 and sign == '+' and num2 == 22:
        return("43+22 = 65")
    if num1 == 43 and sign == '+' and num2 == 23:
        return("43+23 = 66")
    if num1 == 43 and sign == '+' and num2 == 24:
        return("43+24 = 67")
    if num1 == 43 and sign == '+' and num2 == 25:
        return("43+25 = 68")
    if num1 == 43 and sign == '+' and num2 == 26:
        return("43+26 = 69")
    if num1 == 43 and sign == '+' and num2 == 27:
        return("43+27 = 70")
    if num1 == 43 and sign == '+' and num2 == 28:
        return("43+28 = 71")
    if num1 == 43 and sign == '+' and num2 == 29:
        return("43+29 = 72")
    if num1 == 43 and sign == '+' and num2 == 30:
        return("43+30 = 73")
    if num1 == 43 and sign == '+' and num2 == 31:
        return("43+31 = 74")
    if num1 == 43 and sign == '+' and num2 == 32:
        return("43+32 = 75")
    if num1 == 43 and sign == '+' and num2 == 33:
        return("43+33 = 76")
    if num1 == 43 and sign == '+' and num2 == 34:
        return("43+34 = 77")
    if num1 == 43 and sign == '+' and num2 == 35:
        return("43+35 = 78")
    if num1 == 43 and sign == '+' and num2 == 36:
        return("43+36 = 79")
    if num1 == 43 and sign == '+' and num2 == 37:
        return("43+37 = 80")
    if num1 == 43 and sign == '+' and num2 == 38:
        return("43+38 = 81")
    if num1 == 43 and sign == '+' and num2 == 39:
        return("43+39 = 82")
    if num1 == 43 and sign == '+' and num2 == 40:
        return("43+40 = 83")
    if num1 == 43 and sign == '+' and num2 == 41:
        return("43+41 = 84")
    if num1 == 43 and sign == '+' and num2 == 42:
        return("43+42 = 85")
    if num1 == 43 and sign == '+' and num2 == 43:
        return("43+43 = 86")
    if num1 == 43 and sign == '+' and num2 == 44:
        return("43+44 = 87")
    if num1 == 43 and sign == '+' and num2 == 45:
        return("43+45 = 88")
    if num1 == 43 and sign == '+' and num2 == 46:
        return("43+46 = 89")
    if num1 == 43 and sign == '+' and num2 == 47:
        return("43+47 = 90")
    if num1 == 43 and sign == '+' and num2 == 48:
        return("43+48 = 91")
    if num1 == 43 and sign == '+' and num2 == 49:
        return("43+49 = 92")
    if num1 == 43 and sign == '+' and num2 == 50:
        return("43+50 = 93")
    if num1 == 44 and sign == '+' and num2 == 0:
        return("44+0 = 44")
    if num1 == 44 and sign == '+' and num2 == 1:
        return("44+1 = 45")
    if num1 == 44 and sign == '+' and num2 == 2:
        return("44+2 = 46")
    if num1 == 44 and sign == '+' and num2 == 3:
        return("44+3 = 47")
    if num1 == 44 and sign == '+' and num2 == 4:
        return("44+4 = 48")
    if num1 == 44 and sign == '+' and num2 == 5:
        return("44+5 = 49")
    if num1 == 44 and sign == '+' and num2 == 6:
        return("44+6 = 50")
    if num1 == 44 and sign == '+' and num2 == 7:
        return("44+7 = 51")
    if num1 == 44 and sign == '+' and num2 == 8:
        return("44+8 = 52")
    if num1 == 44 and sign == '+' and num2 == 9:
        return("44+9 = 53")
    if num1 == 44 and sign == '+' and num2 == 10:
        return("44+10 = 54")
    if num1 == 44 and sign == '+' and num2 == 11:
        return("44+11 = 55")
    if num1 == 44 and sign == '+' and num2 == 12:
        return("44+12 = 56")
    if num1 == 44 and sign == '+' and num2 == 13:
        return("44+13 = 57")
    if num1 == 44 and sign == '+' and num2 == 14:
        return("44+14 = 58")
    if num1 == 44 and sign == '+' and num2 == 15:
        return("44+15 = 59")
    if num1 == 44 and sign == '+' and num2 == 16:
        return("44+16 = 60")
    if num1 == 44 and sign == '+' and num2 == 17:
        return("44+17 = 61")
    if num1 == 44 and sign == '+' and num2 == 18:
        return("44+18 = 62")
    if num1 == 44 and sign == '+' and num2 == 19:
        return("44+19 = 63")
    if num1 == 44 and sign == '+' and num2 == 20:
        return("44+20 = 64")
    if num1 == 44 and sign == '+' and num2 == 21:
        return("44+21 = 65")
    if num1 == 44 and sign == '+' and num2 == 22:
        return("44+22 = 66")
    if num1 == 44 and sign == '+' and num2 == 23:
        return("44+23 = 67")
    if num1 == 44 and sign == '+' and num2 == 24:
        return("44+24 = 68")
    if num1 == 44 and sign == '+' and num2 == 25:
        return("44+25 = 69")
    if num1 == 44 and sign == '+' and num2 == 26:
        return("44+26 = 70")
    if num1 == 44 and sign == '+' and num2 == 27:
        return("44+27 = 71")
    if num1 == 44 and sign == '+' and num2 == 28:
        return("44+28 = 72")
    if num1 == 44 and sign == '+' and num2 == 29:
        return("44+29 = 73")
    if num1 == 44 and sign == '+' and num2 == 30:
        return("44+30 = 74")
    if num1 == 44 and sign == '+' and num2 == 31:
        return("44+31 = 75")
    if num1 == 44 and sign == '+' and num2 == 32:
        return("44+32 = 76")
    if num1 == 44 and sign == '+' and num2 == 33:
        return("44+33 = 77")
    if num1 == 44 and sign == '+' and num2 == 34:
        return("44+34 = 78")
    if num1 == 44 and sign == '+' and num2 == 35:
        return("44+35 = 79")
    if num1 == 44 and sign == '+' and num2 == 36:
        return("44+36 = 80")
    if num1 == 44 and sign == '+' and num2 == 37:
        return("44+37 = 81")
    if num1 == 44 and sign == '+' and num2 == 38:
        return("44+38 = 82")
    if num1 == 44 and sign == '+' and num2 == 39:
        return("44+39 = 83")
    if num1 == 44 and sign == '+' and num2 == 40:
        return("44+40 = 84")
    if num1 == 44 and sign == '+' and num2 == 41:
        return("44+41 = 85")
    if num1 == 44 and sign == '+' and num2 == 42:
        return("44+42 = 86")
    if num1 == 44 and sign == '+' and num2 == 43:
        return("44+43 = 87")
    if num1 == 44 and sign == '+' and num2 == 44:
        return("44+44 = 88")
    if num1 == 44 and sign == '+' and num2 == 45:
        return("44+45 = 89")
    if num1 == 44 and sign == '+' and num2 == 46:
        return("44+46 = 90")
    if num1 == 44 and sign == '+' and num2 == 47:
        return("44+47 = 91")
    if num1 == 44 and sign == '+' and num2 == 48:
        return("44+48 = 92")
    if num1 == 44 and sign == '+' and num2 == 49:
        return("44+49 = 93")
    if num1 == 44 and sign == '+' and num2 == 50:
        return("44+50 = 94")
    if num1 == 45 and sign == '+' and num2 == 0:
        return("45+0 = 45")
    if num1 == 45 and sign == '+' and num2 == 1:
        return("45+1 = 46")
    if num1 == 45 and sign == '+' and num2 == 2:
        return("45+2 = 47")
    if num1 == 45 and sign == '+' and num2 == 3:
        return("45+3 = 48")
    if num1 == 45 and sign == '+' and num2 == 4:
        return("45+4 = 49")
    if num1 == 45 and sign == '+' and num2 == 5:
        return("45+5 = 50")
    if num1 == 45 and sign == '+' and num2 == 6:
        return("45+6 = 51")
    if num1 == 45 and sign == '+' and num2 == 7:
        return("45+7 = 52")
    if num1 == 45 and sign == '+' and num2 == 8:
        return("45+8 = 53")
    if num1 == 45 and sign == '+' and num2 == 9:
        return("45+9 = 54")
    if num1 == 45 and sign == '+' and num2 == 10:
        return("45+10 = 55")
    if num1 == 45 and sign == '+' and num2 == 11:
        return("45+11 = 56")
    if num1 == 45 and sign == '+' and num2 == 12:
        return("45+12 = 57")
    if num1 == 45 and sign == '+' and num2 == 13:
        return("45+13 = 58")
    if num1 == 45 and sign == '+' and num2 == 14:
        return("45+14 = 59")
    if num1 == 45 and sign == '+' and num2 == 15:
        return("45+15 = 60")
    if num1 == 45 and sign == '+' and num2 == 16:
        return("45+16 = 61")
    if num1 == 45 and sign == '+' and num2 == 17:
        return("45+17 = 62")
    if num1 == 45 and sign == '+' and num2 == 18:
        return("45+18 = 63")
    if num1 == 45 and sign == '+' and num2 == 19:
        return("45+19 = 64")
    if num1 == 45 and sign == '+' and num2 == 20:
        return("45+20 = 65")
    if num1 == 45 and sign == '+' and num2 == 21:
        return("45+21 = 66")
    if num1 == 45 and sign == '+' and num2 == 22:
        return("45+22 = 67")
    if num1 == 45 and sign == '+' and num2 == 23:
        return("45+23 = 68")
    if num1 == 45 and sign == '+' and num2 == 24:
        return("45+24 = 69")
    if num1 == 45 and sign == '+' and num2 == 25:
        return("45+25 = 70")
    if num1 == 45 and sign == '+' and num2 == 26:
        return("45+26 = 71")
    if num1 == 45 and sign == '+' and num2 == 27:
        return("45+27 = 72")
    if num1 == 45 and sign == '+' and num2 == 28:
        return("45+28 = 73")
    if num1 == 45 and sign == '+' and num2 == 29:
        return("45+29 = 74")
    if num1 == 45 and sign == '+' and num2 == 30:
        return("45+30 = 75")
    if num1 == 45 and sign == '+' and num2 == 31:
        return("45+31 = 76")
    if num1 == 45 and sign == '+' and num2 == 32:
        return("45+32 = 77")
    if num1 == 45 and sign == '+' and num2 == 33:
        return("45+33 = 78")
    if num1 == 45 and sign == '+' and num2 == 34:
        return("45+34 = 79")
    if num1 == 45 and sign == '+' and num2 == 35:
        return("45+35 = 80")
    if num1 == 45 and sign == '+' and num2 == 36:
        return("45+36 = 81")
    if num1 == 45 and sign == '+' and num2 == 37:
        return("45+37 = 82")
    if num1 == 45 and sign == '+' and num2 == 38:
        return("45+38 = 83")
    if num1 == 45 and sign == '+' and num2 == 39:
        return("45+39 = 84")
    if num1 == 45 and sign == '+' and num2 == 40:
        return("45+40 = 85")
    if num1 == 45 and sign == '+' and num2 == 41:
        return("45+41 = 86")
    if num1 == 45 and sign == '+' and num2 == 42:
        return("45+42 = 87")
    if num1 == 45 and sign == '+' and num2 == 43:
        return("45+43 = 88")
    if num1 == 45 and sign == '+' and num2 == 44:
        return("45+44 = 89")
    if num1 == 45 and sign == '+' and num2 == 45:
        return("45+45 = 90")
    if num1 == 45 and sign == '+' and num2 == 46:
        return("45+46 = 91")
    if num1 == 45 and sign == '+' and num2 == 47:
        return("45+47 = 92")
    if num1 == 45 and sign == '+' and num2 == 48:
        return("45+48 = 93")
    if num1 == 45 and sign == '+' and num2 == 49:
        return("45+49 = 94")
    if num1 == 45 and sign == '+' and num2 == 50:
        return("45+50 = 95")
    if num1 == 46 and sign == '+' and num2 == 0:
        return("46+0 = 46")
    if num1 == 46 and sign == '+' and num2 == 1:
        return("46+1 = 47")
    if num1 == 46 and sign == '+' and num2 == 2:
        return("46+2 = 48")
    if num1 == 46 and sign == '+' and num2 == 3:
        return("46+3 = 49")
    if num1 == 46 and sign == '+' and num2 == 4:
        return("46+4 = 50")
    if num1 == 46 and sign == '+' and num2 == 5:
        return("46+5 = 51")
    if num1 == 46 and sign == '+' and num2 == 6:
        return("46+6 = 52")
    if num1 == 46 and sign == '+' and num2 == 7:
        return("46+7 = 53")
    if num1 == 46 and sign == '+' and num2 == 8:
        return("46+8 = 54")
    if num1 == 46 and sign == '+' and num2 == 9:
        return("46+9 = 55")
    if num1 == 46 and sign == '+' and num2 == 10:
        return("46+10 = 56")
    if num1 == 46 and sign == '+' and num2 == 11:
        return("46+11 = 57")
    if num1 == 46 and sign == '+' and num2 == 12:
        return("46+12 = 58")
    if num1 == 46 and sign == '+' and num2 == 13:
        return("46+13 = 59")
    if num1 == 46 and sign == '+' and num2 == 14:
        return("46+14 = 60")
    if num1 == 46 and sign == '+' and num2 == 15:
        return("46+15 = 61")
    if num1 == 46 and sign == '+' and num2 == 16:
        return("46+16 = 62")
    if num1 == 46 and sign == '+' and num2 == 17:
        return("46+17 = 63")
    if num1 == 46 and sign == '+' and num2 == 18:
        return("46+18 = 64")
    if num1 == 46 and sign == '+' and num2 == 19:
        return("46+19 = 65")
    if num1 == 46 and sign == '+' and num2 == 20:
        return("46+20 = 66")
    if num1 == 46 and sign == '+' and num2 == 21:
        return("46+21 = 67")
    if num1 == 46 and sign == '+' and num2 == 22:
        return("46+22 = 68")
    if num1 == 46 and sign == '+' and num2 == 23:
        return("46+23 = 69")
    if num1 == 46 and sign == '+' and num2 == 24:
        return("46+24 = 70")
    if num1 == 46 and sign == '+' and num2 == 25:
        return("46+25 = 71")
    if num1 == 46 and sign == '+' and num2 == 26:
        return("46+26 = 72")
    if num1 == 46 and sign == '+' and num2 == 27:
        return("46+27 = 73")
    if num1 == 46 and sign == '+' and num2 == 28:
        return("46+28 = 74")
    if num1 == 46 and sign == '+' and num2 == 29:
        return("46+29 = 75")
    if num1 == 46 and sign == '+' and num2 == 30:
        return("46+30 = 76")
    if num1 == 46 and sign == '+' and num2 == 31:
        return("46+31 = 77")
    if num1 == 46 and sign == '+' and num2 == 32:
        return("46+32 = 78")
    if num1 == 46 and sign == '+' and num2 == 33:
        return("46+33 = 79")
    if num1 == 46 and sign == '+' and num2 == 34:
        return("46+34 = 80")
    if num1 == 46 and sign == '+' and num2 == 35:
        return("46+35 = 81")
    if num1 == 46 and sign == '+' and num2 == 36:
        return("46+36 = 82")
    if num1 == 46 and sign == '+' and num2 == 37:
        return("46+37 = 83")
    if num1 == 46 and sign == '+' and num2 == 38:
        return("46+38 = 84")
    if num1 == 46 and sign == '+' and num2 == 39:
        return("46+39 = 85")
    if num1 == 46 and sign == '+' and num2 == 40:
        return("46+40 = 86")
    if num1 == 46 and sign == '+' and num2 == 41:
        return("46+41 = 87")
    if num1 == 46 and sign == '+' and num2 == 42:
        return("46+42 = 88")
    if num1 == 46 and sign == '+' and num2 == 43:
        return("46+43 = 89")
    if num1 == 46 and sign == '+' and num2 == 44:
        return("46+44 = 90")
    if num1 == 46 and sign == '+' and num2 == 45:
        return("46+45 = 91")
    if num1 == 46 and sign == '+' and num2 == 46:
        return("46+46 = 92")
    if num1 == 46 and sign == '+' and num2 == 47:
        return("46+47 = 93")
    if num1 == 46 and sign == '+' and num2 == 48:
        return("46+48 = 94")
    if num1 == 46 and sign == '+' and num2 == 49:
        return("46+49 = 95")
    if num1 == 46 and sign == '+' and num2 == 50:
        return("46+50 = 96")
    if num1 == 47 and sign == '+' and num2 == 0:
        return("47+0 = 47")
    if num1 == 47 and sign == '+' and num2 == 1:
        return("47+1 = 48")
    if num1 == 47 and sign == '+' and num2 == 2:
        return("47+2 = 49")
    if num1 == 47 and sign == '+' and num2 == 3:
        return("47+3 = 50")
    if num1 == 47 and sign == '+' and num2 == 4:
        return("47+4 = 51")
    if num1 == 47 and sign == '+' and num2 == 5:
        return("47+5 = 52")
    if num1 == 47 and sign == '+' and num2 == 6:
        return("47+6 = 53")
    if num1 == 47 and sign == '+' and num2 == 7:
        return("47+7 = 54")
    if num1 == 47 and sign == '+' and num2 == 8:
        return("47+8 = 55")
    if num1 == 47 and sign == '+' and num2 == 9:
        return("47+9 = 56")
    if num1 == 47 and sign == '+' and num2 == 10:
        return("47+10 = 57")
    if num1 == 47 and sign == '+' and num2 == 11:
        return("47+11 = 58")
    if num1 == 47 and sign == '+' and num2 == 12:
        return("47+12 = 59")
    if num1 == 47 and sign == '+' and num2 == 13:
        return("47+13 = 60")
    if num1 == 47 and sign == '+' and num2 == 14:
        return("47+14 = 61")
    if num1 == 47 and sign == '+' and num2 == 15:
        return("47+15 = 62")
    if num1 == 47 and sign == '+' and num2 == 16:
        return("47+16 = 63")
    if num1 == 47 and sign == '+' and num2 == 17:
        return("47+17 = 64")
    if num1 == 47 and sign == '+' and num2 == 18:
        return("47+18 = 65")
    if num1 == 47 and sign == '+' and num2 == 19:
        return("47+19 = 66")
    if num1 == 47 and sign == '+' and num2 == 20:
        return("47+20 = 67")
    if num1 == 47 and sign == '+' and num2 == 21:
        return("47+21 = 68")
    if num1 == 47 and sign == '+' and num2 == 22:
        return("47+22 = 69")
    if num1 == 47 and sign == '+' and num2 == 23:
        return("47+23 = 70")
    if num1 == 47 and sign == '+' and num2 == 24:
        return("47+24 = 71")
    if num1 == 47 and sign == '+' and num2 == 25:
        return("47+25 = 72")
    if num1 == 47 and sign == '+' and num2 == 26:
        return("47+26 = 73")
    if num1 == 47 and sign == '+' and num2 == 27:
        return("47+27 = 74")
    if num1 == 47 and sign == '+' and num2 == 28:
        return("47+28 = 75")
    if num1 == 47 and sign == '+' and num2 == 29:
        return("47+29 = 76")
    if num1 == 47 and sign == '+' and num2 == 30:
        return("47+30 = 77")
    if num1 == 47 and sign == '+' and num2 == 31:
        return("47+31 = 78")
    if num1 == 47 and sign == '+' and num2 == 32:
        return("47+32 = 79")
    if num1 == 47 and sign == '+' and num2 == 33:
        return("47+33 = 80")
    if num1 == 47 and sign == '+' and num2 == 34:
        return("47+34 = 81")
    if num1 == 47 and sign == '+' and num2 == 35:
        return("47+35 = 82")
    if num1 == 47 and sign == '+' and num2 == 36:
        return("47+36 = 83")
    if num1 == 47 and sign == '+' and num2 == 37:
        return("47+37 = 84")
    if num1 == 47 and sign == '+' and num2 == 38:
        return("47+38 = 85")
    if num1 == 47 and sign == '+' and num2 == 39:
        return("47+39 = 86")
    if num1 == 47 and sign == '+' and num2 == 40:
        return("47+40 = 87")
    if num1 == 47 and sign == '+' and num2 == 41:
        return("47+41 = 88")
    if num1 == 47 and sign == '+' and num2 == 42:
        return("47+42 = 89")
    if num1 == 47 and sign == '+' and num2 == 43:
        return("47+43 = 90")
    if num1 == 47 and sign == '+' and num2 == 44:
        return("47+44 = 91")
    if num1 == 47 and sign == '+' and num2 == 45:
        return("47+45 = 92")
    if num1 == 47 and sign == '+' and num2 == 46:
        return("47+46 = 93")
    if num1 == 47 and sign == '+' and num2 == 47:
        return("47+47 = 94")
    if num1 == 47 and sign == '+' and num2 == 48:
        return("47+48 = 95")
    if num1 == 47 and sign == '+' and num2 == 49:
        return("47+49 = 96")
    if num1 == 47 and sign == '+' and num2 == 50:
        return("47+50 = 97")
    if num1 == 48 and sign == '+' and num2 == 0:
        return("48+0 = 48")
    if num1 == 48 and sign == '+' and num2 == 1:
        return("48+1 = 49")
    if num1 == 48 and sign == '+' and num2 == 2:
        return("48+2 = 50")
    if num1 == 48 and sign == '+' and num2 == 3:
        return("48+3 = 51")
    if num1 == 48 and sign == '+' and num2 == 4:
        return("48+4 = 52")
    if num1 == 48 and sign == '+' and num2 == 5:
        return("48+5 = 53")
    if num1 == 48 and sign == '+' and num2 == 6:
        return("48+6 = 54")
    if num1 == 48 and sign == '+' and num2 == 7:
        return("48+7 = 55")
    if num1 == 48 and sign == '+' and num2 == 8:
        return("48+8 = 56")
    if num1 == 48 and sign == '+' and num2 == 9:
        return("48+9 = 57")
    if num1 == 48 and sign == '+' and num2 == 10:
        return("48+10 = 58")
    if num1 == 48 and sign == '+' and num2 == 11:
        return("48+11 = 59")
    if num1 == 48 and sign == '+' and num2 == 12:
        return("48+12 = 60")
    if num1 == 48 and sign == '+' and num2 == 13:
        return("48+13 = 61")
    if num1 == 48 and sign == '+' and num2 == 14:
        return("48+14 = 62")
    if num1 == 48 and sign == '+' and num2 == 15:
        return("48+15 = 63")
    if num1 == 48 and sign == '+' and num2 == 16:
        return("48+16 = 64")
    if num1 == 48 and sign == '+' and num2 == 17:
        return("48+17 = 65")
    if num1 == 48 and sign == '+' and num2 == 18:
        return("48+18 = 66")
    if num1 == 48 and sign == '+' and num2 == 19:
        return("48+19 = 67")
    if num1 == 48 and sign == '+' and num2 == 20:
        return("48+20 = 68")
    if num1 == 48 and sign == '+' and num2 == 21:
        return("48+21 = 69")
    if num1 == 48 and sign == '+' and num2 == 22:
        return("48+22 = 70")
    if num1 == 48 and sign == '+' and num2 == 23:
        return("48+23 = 71")
    if num1 == 48 and sign == '+' and num2 == 24:
        return("48+24 = 72")
    if num1 == 48 and sign == '+' and num2 == 25:
        return("48+25 = 73")
    if num1 == 48 and sign == '+' and num2 == 26:
        return("48+26 = 74")
    if num1 == 48 and sign == '+' and num2 == 27:
        return("48+27 = 75")
    if num1 == 48 and sign == '+' and num2 == 28:
        return("48+28 = 76")
    if num1 == 48 and sign == '+' and num2 == 29:
        return("48+29 = 77")
    if num1 == 48 and sign == '+' and num2 == 30:
        return("48+30 = 78")
    if num1 == 48 and sign == '+' and num2 == 31:
        return("48+31 = 79")
    if num1 == 48 and sign == '+' and num2 == 32:
        return("48+32 = 80")
    if num1 == 48 and sign == '+' and num2 == 33:
        return("48+33 = 81")
    if num1 == 48 and sign == '+' and num2 == 34:
        return("48+34 = 82")
    if num1 == 48 and sign == '+' and num2 == 35:
        return("48+35 = 83")
    if num1 == 48 and sign == '+' and num2 == 36:
        return("48+36 = 84")
    if num1 == 48 and sign == '+' and num2 == 37:
        return("48+37 = 85")
    if num1 == 48 and sign == '+' and num2 == 38:
        return("48+38 = 86")
    if num1 == 48 and sign == '+' and num2 == 39:
        return("48+39 = 87")
    if num1 == 48 and sign == '+' and num2 == 40:
        return("48+40 = 88")
    if num1 == 48 and sign == '+' and num2 == 41:
        return("48+41 = 89")
    if num1 == 48 and sign == '+' and num2 == 42:
        return("48+42 = 90")
    if num1 == 48 and sign == '+' and num2 == 43:
        return("48+43 = 91")
    if num1 == 48 and sign == '+' and num2 == 44:
        return("48+44 = 92")
    if num1 == 48 and sign == '+' and num2 == 45:
        return("48+45 = 93")
    if num1 == 48 and sign == '+' and num2 == 46:
        return("48+46 = 94")
    if num1 == 48 and sign == '+' and num2 == 47:
        return("48+47 = 95")
    if num1 == 48 and sign == '+' and num2 == 48:
        return("48+48 = 96")
    if num1 == 48 and sign == '+' and num2 == 49:
        return("48+49 = 97")
    if num1 == 48 and sign == '+' and num2 == 50:
        return("48+50 = 98")
    if num1 == 49 and sign == '+' and num2 == 0:
        return("49+0 = 49")
    if num1 == 49 and sign == '+' and num2 == 1:
        return("49+1 = 50")
    if num1 == 49 and sign == '+' and num2 == 2:
        return("49+2 = 51")
    if num1 == 49 and sign == '+' and num2 == 3:
        return("49+3 = 52")
    if num1 == 49 and sign == '+' and num2 == 4:
        return("49+4 = 53")
    if num1 == 49 and sign == '+' and num2 == 5:
        return("49+5 = 54")
    if num1 == 49 and sign == '+' and num2 == 6:
        return("49+6 = 55")
    if num1 == 49 and sign == '+' and num2 == 7:
        return("49+7 = 56")
    if num1 == 49 and sign == '+' and num2 == 8:
        return("49+8 = 57")
    if num1 == 49 and sign == '+' and num2 == 9:
        return("49+9 = 58")
    if num1 == 49 and sign == '+' and num2 == 10:
        return("49+10 = 59")
    if num1 == 49 and sign == '+' and num2 == 11:
        return("49+11 = 60")
    if num1 == 49 and sign == '+' and num2 == 12:
        return("49+12 = 61")
    if num1 == 49 and sign == '+' and num2 == 13:
        return("49+13 = 62")
    if num1 == 49 and sign == '+' and num2 == 14:
        return("49+14 = 63")
    if num1 == 49 and sign == '+' and num2 == 15:
        return("49+15 = 64")
    if num1 == 49 and sign == '+' and num2 == 16:
        return("49+16 = 65")
    if num1 == 49 and sign == '+' and num2 == 17:
        return("49+17 = 66")
    if num1 == 49 and sign == '+' and num2 == 18:
        return("49+18 = 67")
    if num1 == 49 and sign == '+' and num2 == 19:
        return("49+19 = 68")
    if num1 == 49 and sign == '+' and num2 == 20:
        return("49+20 = 69")
    if num1 == 49 and sign == '+' and num2 == 21:
        return("49+21 = 70")
    if num1 == 49 and sign == '+' and num2 == 22:
        return("49+22 = 71")
    if num1 == 49 and sign == '+' and num2 == 23:
        return("49+23 = 72")
    if num1 == 49 and sign == '+' and num2 == 24:
        return("49+24 = 73")
    if num1 == 49 and sign == '+' and num2 == 25:
        return("49+25 = 74")
    if num1 == 49 and sign == '+' and num2 == 26:
        return("49+26 = 75")
    if num1 == 49 and sign == '+' and num2 == 27:
        return("49+27 = 76")
    if num1 == 49 and sign == '+' and num2 == 28:
        return("49+28 = 77")
    if num1 == 49 and sign == '+' and num2 == 29:
        return("49+29 = 78")
    if num1 == 49 and sign == '+' and num2 == 30:
        return("49+30 = 79")
    if num1 == 49 and sign == '+' and num2 == 31:
        return("49+31 = 80")
    if num1 == 49 and sign == '+' and num2 == 32:
        return("49+32 = 81")
    if num1 == 49 and sign == '+' and num2 == 33:
        return("49+33 = 82")
    if num1 == 49 and sign == '+' and num2 == 34:
        return("49+34 = 83")
    if num1 == 49 and sign == '+' and num2 == 35:
        return("49+35 = 84")
    if num1 == 49 and sign == '+' and num2 == 36:
        return("49+36 = 85")
    if num1 == 49 and sign == '+' and num2 == 37:
        return("49+37 = 86")
    if num1 == 49 and sign == '+' and num2 == 38:
        return("49+38 = 87")
    if num1 == 49 and sign == '+' and num2 == 39:
        return("49+39 = 88")
    if num1 == 49 and sign == '+' and num2 == 40:
        return("49+40 = 89")
    if num1 == 49 and sign == '+' and num2 == 41:
        return("49+41 = 90")
    if num1 == 49 and sign == '+' and num2 == 42:
        return("49+42 = 91")
    if num1 == 49 and sign == '+' and num2 == 43:
        return("49+43 = 92")
    if num1 == 49 and sign == '+' and num2 == 44:
        return("49+44 = 93")
    if num1 == 49 and sign == '+' and num2 == 45:
        return("49+45 = 94")
    if num1 == 49 and sign == '+' and num2 == 46:
        return("49+46 = 95")
    if num1 == 49 and sign == '+' and num2 == 47:
        return("49+47 = 96")
    if num1 == 49 and sign == '+' and num2 == 48:
        return("49+48 = 97")
    if num1 == 49 and sign == '+' and num2 == 49:
        return("49+49 = 98")
    if num1 == 49 and sign == '+' and num2 == 50:
        return("49+50 = 99")
    if num1 == 50 and sign == '+' and num2 == 0:
        return("50+0 = 50")
    if num1 == 50 and sign == '+' and num2 == 1:
        return("50+1 = 51")
    if num1 == 50 and sign == '+' and num2 == 2:
        return("50+2 = 52")
    if num1 == 50 and sign == '+' and num2 == 3:
        return("50+3 = 53")
    if num1 == 50 and sign == '+' and num2 == 4:
        return("50+4 = 54")
    if num1 == 50 and sign == '+' and num2 == 5:
        return("50+5 = 55")
    if num1 == 50 and sign == '+' and num2 == 6:
        return("50+6 = 56")
    if num1 == 50 and sign == '+' and num2 == 7:
        return("50+7 = 57")
    if num1 == 50 and sign == '+' and num2 == 8:
        return("50+8 = 58")
    if num1 == 50 and sign == '+' and num2 == 9:
        return("50+9 = 59")
    if num1 == 50 and sign == '+' and num2 == 10:
        return("50+10 = 60")
    if num1 == 50 and sign == '+' and num2 == 11:
        return("50+11 = 61")
    if num1 == 50 and sign == '+' and num2 == 12:
        return("50+12 = 62")
    if num1 == 50 and sign == '+' and num2 == 13:
        return("50+13 = 63")
    if num1 == 50 and sign == '+' and num2 == 14:
        return("50+14 = 64")
    if num1 == 50 and sign == '+' and num2 == 15:
        return("50+15 = 65")
    if num1 == 50 and sign == '+' and num2 == 16:
        return("50+16 = 66")
    if num1 == 50 and sign == '+' and num2 == 17:
        return("50+17 = 67")
    if num1 == 50 and sign == '+' and num2 == 18:
        return("50+18 = 68")
    if num1 == 50 and sign == '+' and num2 == 19:
        return("50+19 = 69")
    if num1 == 50 and sign == '+' and num2 == 20:
        return("50+20 = 70")
    if num1 == 50 and sign == '+' and num2 == 21:
        return("50+21 = 71")
    if num1 == 50 and sign == '+' and num2 == 22:
        return("50+22 = 72")
    if num1 == 50 and sign == '+' and num2 == 23:
        return("50+23 = 73")
    if num1 == 50 and sign == '+' and num2 == 24:
        return("50+24 = 74")
    if num1 == 50 and sign == '+' and num2 == 25:
        return("50+25 = 75")
    if num1 == 50 and sign == '+' and num2 == 26:
        return("50+26 = 76")
    if num1 == 50 and sign == '+' and num2 == 27:
        return("50+27 = 77")
    if num1 == 50 and sign == '+' and num2 == 28:
        return("50+28 = 78")
    if num1 == 50 and sign == '+' and num2 == 29:
        return("50+29 = 79")
    if num1 == 50 and sign == '+' and num2 == 30:
        return("50+30 = 80")
    if num1 == 50 and sign == '+' and num2 == 31:
        return("50+31 = 81")
    if num1 == 50 and sign == '+' and num2 == 32:
        return("50+32 = 82")
    if num1 == 50 and sign == '+' and num2 == 33:
        return("50+33 = 83")
    if num1 == 50 and sign == '+' and num2 == 34:
        return("50+34 = 84")
    if num1 == 50 and sign == '+' and num2 == 35:
        return("50+35 = 85")
    if num1 == 50 and sign == '+' and num2 == 36:
        return("50+36 = 86")
    if num1 == 50 and sign == '+' and num2 == 37:
        return("50+37 = 87")
    if num1 == 50 and sign == '+' and num2 == 38:
        return("50+38 = 88")
    if num1 == 50 and sign == '+' and num2 == 39:
        return("50+39 = 89")
    if num1 == 50 and sign == '+' and num2 == 40:
        return("50+40 = 90")
    if num1 == 50 and sign == '+' and num2 == 41:
        return("50+41 = 91")
    if num1 == 50 and sign == '+' and num2 == 42:
        return("50+42 = 92")
    if num1 == 50 and sign == '+' and num2 == 43:
        return("50+43 = 93")
    if num1 == 50 and sign == '+' and num2 == 44:
        return("50+44 = 94")
    if num1 == 50 and sign == '+' and num2 == 45:
        return("50+45 = 95")
    if num1 == 50 and sign == '+' and num2 == 46:
        return("50+46 = 96")
    if num1 == 50 and sign == '+' and num2 == 47:
        return("50+47 = 97")
    if num1 == 50 and sign == '+' and num2 == 48:
        return("50+48 = 98")
    if num1 == 50 and sign == '+' and num2 == 49:
        return("50+49 = 99")
    if num1 == 50 and sign == '+' and num2 == 50:
        return("50+50 = 100")
    if num1 == 0 and sign == '-' and num2 == 0:
        return("0-0 = 0")
    if num1 == 0 and sign == '-' and num2 == 1:
        return("0-1 = -1")
    if num1 == 0 and sign == '-' and num2 == 2:
        return("0-2 = -2")
    if num1 == 0 and sign == '-' and num2 == 3:
        return("0-3 = -3")
    if num1 == 0 and sign == '-' and num2 == 4:
        return("0-4 = -4")
    if num1 == 0 and sign == '-' and num2 == 5:
        return("0-5 = -5")
    if num1 == 0 and sign == '-' and num2 == 6:
        return("0-6 = -6")
    if num1 == 0 and sign == '-' and num2 == 7:
        return("0-7 = -7")
    if num1 == 0 and sign == '-' and num2 == 8:
        return("0-8 = -8")
    if num1 == 0 and sign == '-' and num2 == 9:
        return("0-9 = -9")
    if num1 == 0 and sign == '-' and num2 == 10:
        return("0-10 = -10")
    if num1 == 0 and sign == '-' and num2 == 11:
        return("0-11 = -11")
    if num1 == 0 and sign == '-' and num2 == 12:
        return("0-12 = -12")
    if num1 == 0 and sign == '-' and num2 == 13:
        return("0-13 = -13")
    if num1 == 0 and sign == '-' and num2 == 14:
        return("0-14 = -14")
    if num1 == 0 and sign == '-' and num2 == 15:
        return("0-15 = -15")
    if num1 == 0 and sign == '-' and num2 == 16:
        return("0-16 = -16")
    if num1 == 0 and sign == '-' and num2 == 17:
        return("0-17 = -17")
    if num1 == 0 and sign == '-' and num2 == 18:
        return("0-18 = -18")
    if num1 == 0 and sign == '-' and num2 == 19:
        return("0-19 = -19")
    if num1 == 0 and sign == '-' and num2 == 20:
        return("0-20 = -20")
    if num1 == 0 and sign == '-' and num2 == 21:
        return("0-21 = -21")
    if num1 == 0 and sign == '-' and num2 == 22:
        return("0-22 = -22")
    if num1 == 0 and sign == '-' and num2 == 23:
        return("0-23 = -23")
    if num1 == 0 and sign == '-' and num2 == 24:
        return("0-24 = -24")
    if num1 == 0 and sign == '-' and num2 == 25:
        return("0-25 = -25")
    if num1 == 0 and sign == '-' and num2 == 26:
        return("0-26 = -26")
    if num1 == 0 and sign == '-' and num2 == 27:
        return("0-27 = -27")
    if num1 == 0 and sign == '-' and num2 == 28:
        return("0-28 = -28")
    if num1 == 0 and sign == '-' and num2 == 29:
        return("0-29 = -29")
    if num1 == 0 and sign == '-' and num2 == 30:
        return("0-30 = -30")
    if num1 == 0 and sign == '-' and num2 == 31:
        return("0-31 = -31")
    if num1 == 0 and sign == '-' and num2 == 32:
        return("0-32 = -32")
    if num1 == 0 and sign == '-' and num2 == 33:
        return("0-33 = -33")
    if num1 == 0 and sign == '-' and num2 == 34:
        return("0-34 = -34")
    if num1 == 0 and sign == '-' and num2 == 35:
        return("0-35 = -35")
    if num1 == 0 and sign == '-' and num2 == 36:
        return("0-36 = -36")
    if num1 == 0 and sign == '-' and num2 == 37:
        return("0-37 = -37")
    if num1 == 0 and sign == '-' and num2 == 38:
        return("0-38 = -38")
    if num1 == 0 and sign == '-' and num2 == 39:
        return("0-39 = -39")
    if num1 == 0 and sign == '-' and num2 == 40:
        return("0-40 = -40")
    if num1 == 0 and sign == '-' and num2 == 41:
        return("0-41 = -41")
    if num1 == 0 and sign == '-' and num2 == 42:
        return("0-42 = -42")
    if num1 == 0 and sign == '-' and num2 == 43:
        return("0-43 = -43")
    if num1 == 0 and sign == '-' and num2 == 44:
        return("0-44 = -44")
    if num1 == 0 and sign == '-' and num2 == 45:
        return("0-45 = -45")
    if num1 == 0 and sign == '-' and num2 == 46:
        return("0-46 = -46")
    if num1 == 0 and sign == '-' and num2 == 47:
        return("0-47 = -47")
    if num1 == 0 and sign == '-' and num2 == 48:
        return("0-48 = -48")
    if num1 == 0 and sign == '-' and num2 == 49:
        return("0-49 = -49")
    if num1 == 0 and sign == '-' and num2 == 50:
        return("0-50 = -50")
    if num1 == 1 and sign == '-' and num2 == 0:
        return("1-0 = 1")
    if num1 == 1 and sign == '-' and num2 == 1:
        return("1-1 = 0")
    if num1 == 1 and sign == '-' and num2 == 2:
        return("1-2 = -1")
    if num1 == 1 and sign == '-' and num2 == 3:
        return("1-3 = -2")
    if num1 == 1 and sign == '-' and num2 == 4:
        return("1-4 = -3")
    if num1 == 1 and sign == '-' and num2 == 5:
        return("1-5 = -4")
    if num1 == 1 and sign == '-' and num2 == 6:
        return("1-6 = -5")
    if num1 == 1 and sign == '-' and num2 == 7:
        return("1-7 = -6")
    if num1 == 1 and sign == '-' and num2 == 8:
        return("1-8 = -7")
    if num1 == 1 and sign == '-' and num2 == 9:
        return("1-9 = -8")
    if num1 == 1 and sign == '-' and num2 == 10:
        return("1-10 = -9")
    if num1 == 1 and sign == '-' and num2 == 11:
        return("1-11 = -10")
    if num1 == 1 and sign == '-' and num2 == 12:
        return("1-12 = -11")
    if num1 == 1 and sign == '-' and num2 == 13:
        return("1-13 = -12")
    if num1 == 1 and sign == '-' and num2 == 14:
        return("1-14 = -13")
    if num1 == 1 and sign == '-' and num2 == 15:
        return("1-15 = -14")
    if num1 == 1 and sign == '-' and num2 == 16:
        return("1-16 = -15")
    if num1 == 1 and sign == '-' and num2 == 17:
        return("1-17 = -16")
    if num1 == 1 and sign == '-' and num2 == 18:
        return("1-18 = -17")
    if num1 == 1 and sign == '-' and num2 == 19:
        return("1-19 = -18")
    if num1 == 1 and sign == '-' and num2 == 20:
        return("1-20 = -19")
    if num1 == 1 and sign == '-' and num2 == 21:
        return("1-21 = -20")
    if num1 == 1 and sign == '-' and num2 == 22:
        return("1-22 = -21")
    if num1 == 1 and sign == '-' and num2 == 23:
        return("1-23 = -22")
    if num1 == 1 and sign == '-' and num2 == 24:
        return("1-24 = -23")
    if num1 == 1 and sign == '-' and num2 == 25:
        return("1-25 = -24")
    if num1 == 1 and sign == '-' and num2 == 26:
        return("1-26 = -25")
    if num1 == 1 and sign == '-' and num2 == 27:
        return("1-27 = -26")
    if num1 == 1 and sign == '-' and num2 == 28:
        return("1-28 = -27")
    if num1 == 1 and sign == '-' and num2 == 29:
        return("1-29 = -28")
    if num1 == 1 and sign == '-' and num2 == 30:
        return("1-30 = -29")
    if num1 == 1 and sign == '-' and num2 == 31:
        return("1-31 = -30")
    if num1 == 1 and sign == '-' and num2 == 32:
        return("1-32 = -31")
    if num1 == 1 and sign == '-' and num2 == 33:
        return("1-33 = -32")
    if num1 == 1 and sign == '-' and num2 == 34:
        return("1-34 = -33")
    if num1 == 1 and sign == '-' and num2 == 35:
        return("1-35 = -34")
    if num1 == 1 and sign == '-' and num2 == 36:
        return("1-36 = -35")
    if num1 == 1 and sign == '-' and num2 == 37:
        return("1-37 = -36")
    if num1 == 1 and sign == '-' and num2 == 38:
        return("1-38 = -37")
    if num1 == 1 and sign == '-' and num2 == 39:
        return("1-39 = -38")
    if num1 == 1 and sign == '-' and num2 == 40:
        return("1-40 = -39")
    if num1 == 1 and sign == '-' and num2 == 41:
        return("1-41 = -40")
    if num1 == 1 and sign == '-' and num2 == 42:
        return("1-42 = -41")
    if num1 == 1 and sign == '-' and num2 == 43:
        return("1-43 = -42")
    if num1 == 1 and sign == '-' and num2 == 44:
        return("1-44 = -43")
    if num1 == 1 and sign == '-' and num2 == 45:
        return("1-45 = -44")
    if num1 == 1 and sign == '-' and num2 == 46:
        return("1-46 = -45")
    if num1 == 1 and sign == '-' and num2 == 47:
        return("1-47 = -46")
    if num1 == 1 and sign == '-' and num2 == 48:
        return("1-48 = -47")
    if num1 == 1 and sign == '-' and num2 == 49:
        return("1-49 = -48")
    if num1 == 1 and sign == '-' and num2 == 50:
        return("1-50 = -49")
    if num1 == 2 and sign == '-' and num2 == 0:
        return("2-0 = 2")
    if num1 == 2 and sign == '-' and num2 == 1:
        return("2-1 = 1")
    if num1 == 2 and sign == '-' and num2 == 2:
        return("2-2 = 0")
    if num1 == 2 and sign == '-' and num2 == 3:
        return("2-3 = -1")
    if num1 == 2 and sign == '-' and num2 == 4:
        return("2-4 = -2")
    if num1 == 2 and sign == '-' and num2 == 5:
        return("2-5 = -3")
    if num1 == 2 and sign == '-' and num2 == 6:
        return("2-6 = -4")
    if num1 == 2 and sign == '-' and num2 == 7:
        return("2-7 = -5")
    if num1 == 2 and sign == '-' and num2 == 8:
        return("2-8 = -6")
    if num1 == 2 and sign == '-' and num2 == 9:
        return("2-9 = -7")
    if num1 == 2 and sign == '-' and num2 == 10:
        return("2-10 = -8")
    if num1 == 2 and sign == '-' and num2 == 11:
        return("2-11 = -9")
    if num1 == 2 and sign == '-' and num2 == 12:
        return("2-12 = -10")
    if num1 == 2 and sign == '-' and num2 == 13:
        return("2-13 = -11")
    if num1 == 2 and sign == '-' and num2 == 14:
        return("2-14 = -12")
    if num1 == 2 and sign == '-' and num2 == 15:
        return("2-15 = -13")
    if num1 == 2 and sign == '-' and num2 == 16:
        return("2-16 = -14")
    if num1 == 2 and sign == '-' and num2 == 17:
        return("2-17 = -15")
    if num1 == 2 and sign == '-' and num2 == 18:
        return("2-18 = -16")
    if num1 == 2 and sign == '-' and num2 == 19:
        return("2-19 = -17")
    if num1 == 2 and sign == '-' and num2 == 20:
        return("2-20 = -18")
    if num1 == 2 and sign == '-' and num2 == 21:
        return("2-21 = -19")
    if num1 == 2 and sign == '-' and num2 == 22:
        return("2-22 = -20")
    if num1 == 2 and sign == '-' and num2 == 23:
        return("2-23 = -21")
    if num1 == 2 and sign == '-' and num2 == 24:
        return("2-24 = -22")
    if num1 == 2 and sign == '-' and num2 == 25:
        return("2-25 = -23")
    if num1 == 2 and sign == '-' and num2 == 26:
        return("2-26 = -24")
    if num1 == 2 and sign == '-' and num2 == 27:
        return("2-27 = -25")
    if num1 == 2 and sign == '-' and num2 == 28:
        return("2-28 = -26")
    if num1 == 2 and sign == '-' and num2 == 29:
        return("2-29 = -27")
    if num1 == 2 and sign == '-' and num2 == 30:
        return("2-30 = -28")
    if num1 == 2 and sign == '-' and num2 == 31:
        return("2-31 = -29")
    if num1 == 2 and sign == '-' and num2 == 32:
        return("2-32 = -30")
    if num1 == 2 and sign == '-' and num2 == 33:
        return("2-33 = -31")
    if num1 == 2 and sign == '-' and num2 == 34:
        return("2-34 = -32")
    if num1 == 2 and sign == '-' and num2 == 35:
        return("2-35 = -33")
    if num1 == 2 and sign == '-' and num2 == 36:
        return("2-36 = -34")
    if num1 == 2 and sign == '-' and num2 == 37:
        return("2-37 = -35")
    if num1 == 2 and sign == '-' and num2 == 38:
        return("2-38 = -36")
    if num1 == 2 and sign == '-' and num2 == 39:
        return("2-39 = -37")
    if num1 == 2 and sign == '-' and num2 == 40:
        return("2-40 = -38")
    if num1 == 2 and sign == '-' and num2 == 41:
        return("2-41 = -39")
    if num1 == 2 and sign == '-' and num2 == 42:
        return("2-42 = -40")
    if num1 == 2 and sign == '-' and num2 == 43:
        return("2-43 = -41")
    if num1 == 2 and sign == '-' and num2 == 44:
        return("2-44 = -42")
    if num1 == 2 and sign == '-' and num2 == 45:
        return("2-45 = -43")
    if num1 == 2 and sign == '-' and num2 == 46:
        return("2-46 = -44")
    if num1 == 2 and sign == '-' and num2 == 47:
        return("2-47 = -45")
    if num1 == 2 and sign == '-' and num2 == 48:
        return("2-48 = -46")
    if num1 == 2 and sign == '-' and num2 == 49:
        return("2-49 = -47")
    if num1 == 2 and sign == '-' and num2 == 50:
        return("2-50 = -48")
    if num1 == 3 and sign == '-' and num2 == 0:
        return("3-0 = 3")
    if num1 == 3 and sign == '-' and num2 == 1:
        return("3-1 = 2")
    if num1 == 3 and sign == '-' and num2 == 2:
        return("3-2 = 1")
    if num1 == 3 and sign == '-' and num2 == 3:
        return("3-3 = 0")
    if num1 == 3 and sign == '-' and num2 == 4:
        return("3-4 = -1")
    if num1 == 3 and sign == '-' and num2 == 5:
        return("3-5 = -2")
    if num1 == 3 and sign == '-' and num2 == 6:
        return("3-6 = -3")
    if num1 == 3 and sign == '-' and num2 == 7:
        return("3-7 = -4")
    if num1 == 3 and sign == '-' and num2 == 8:
        return("3-8 = -5")
    if num1 == 3 and sign == '-' and num2 == 9:
        return("3-9 = -6")
    if num1 == 3 and sign == '-' and num2 == 10:
        return("3-10 = -7")
    if num1 == 3 and sign == '-' and num2 == 11:
        return("3-11 = -8")
    if num1 == 3 and sign == '-' and num2 == 12:
        return("3-12 = -9")
    if num1 == 3 and sign == '-' and num2 == 13:
        return("3-13 = -10")
    if num1 == 3 and sign == '-' and num2 == 14:
        return("3-14 = -11")
    if num1 == 3 and sign == '-' and num2 == 15:
        return("3-15 = -12")
    if num1 == 3 and sign == '-' and num2 == 16:
        return("3-16 = -13")
    if num1 == 3 and sign == '-' and num2 == 17:
        return("3-17 = -14")
    if num1 == 3 and sign == '-' and num2 == 18:
        return("3-18 = -15")
    if num1 == 3 and sign == '-' and num2 == 19:
        return("3-19 = -16")
    if num1 == 3 and sign == '-' and num2 == 20:
        return("3-20 = -17")
    if num1 == 3 and sign == '-' and num2 == 21:
        return("3-21 = -18")
    if num1 == 3 and sign == '-' and num2 == 22:
        return("3-22 = -19")
    if num1 == 3 and sign == '-' and num2 == 23:
        return("3-23 = -20")
    if num1 == 3 and sign == '-' and num2 == 24:
        return("3-24 = -21")
    if num1 == 3 and sign == '-' and num2 == 25:
        return("3-25 = -22")
    if num1 == 3 and sign == '-' and num2 == 26:
        return("3-26 = -23")
    if num1 == 3 and sign == '-' and num2 == 27:
        return("3-27 = -24")
    if num1 == 3 and sign == '-' and num2 == 28:
        return("3-28 = -25")
    if num1 == 3 and sign == '-' and num2 == 29:
        return("3-29 = -26")
    if num1 == 3 and sign == '-' and num2 == 30:
        return("3-30 = -27")
    if num1 == 3 and sign == '-' and num2 == 31:
        return("3-31 = -28")
    if num1 == 3 and sign == '-' and num2 == 32:
        return("3-32 = -29")
    if num1 == 3 and sign == '-' and num2 == 33:
        return("3-33 = -30")
    if num1 == 3 and sign == '-' and num2 == 34:
        return("3-34 = -31")
    if num1 == 3 and sign == '-' and num2 == 35:
        return("3-35 = -32")
    if num1 == 3 and sign == '-' and num2 == 36:
        return("3-36 = -33")
    if num1 == 3 and sign == '-' and num2 == 37:
        return("3-37 = -34")
    if num1 == 3 and sign == '-' and num2 == 38:
        return("3-38 = -35")
    if num1 == 3 and sign == '-' and num2 == 39:
        return("3-39 = -36")
    if num1 == 3 and sign == '-' and num2 == 40:
        return("3-40 = -37")
    if num1 == 3 and sign == '-' and num2 == 41:
        return("3-41 = -38")
    if num1 == 3 and sign == '-' and num2 == 42:
        return("3-42 = -39")
    if num1 == 3 and sign == '-' and num2 == 43:
        return("3-43 = -40")
    if num1 == 3 and sign == '-' and num2 == 44:
        return("3-44 = -41")
    if num1 == 3 and sign == '-' and num2 == 45:
        return("3-45 = -42")
    if num1 == 3 and sign == '-' and num2 == 46:
        return("3-46 = -43")
    if num1 == 3 and sign == '-' and num2 == 47:
        return("3-47 = -44")
    if num1 == 3 and sign == '-' and num2 == 48:
        return("3-48 = -45")
    if num1 == 3 and sign == '-' and num2 == 49:
        return("3-49 = -46")
    if num1 == 3 and sign == '-' and num2 == 50:
        return("3-50 = -47")
    if num1 == 4 and sign == '-' and num2 == 0:
        return("4-0 = 4")
    if num1 == 4 and sign == '-' and num2 == 1:
        return("4-1 = 3")
    if num1 == 4 and sign == '-' and num2 == 2:
        return("4-2 = 2")
    if num1 == 4 and sign == '-' and num2 == 3:
        return("4-3 = 1")
    if num1 == 4 and sign == '-' and num2 == 4:
        return("4-4 = 0")
    if num1 == 4 and sign == '-' and num2 == 5:
        return("4-5 = -1")
    if num1 == 4 and sign == '-' and num2 == 6:
        return("4-6 = -2")
    if num1 == 4 and sign == '-' and num2 == 7:
        return("4-7 = -3")
    if num1 == 4 and sign == '-' and num2 == 8:
        return("4-8 = -4")
    if num1 == 4 and sign == '-' and num2 == 9:
        return("4-9 = -5")
    if num1 == 4 and sign == '-' and num2 == 10:
        return("4-10 = -6")
    if num1 == 4 and sign == '-' and num2 == 11:
        return("4-11 = -7")
    if num1 == 4 and sign == '-' and num2 == 12:
        return("4-12 = -8")
    if num1 == 4 and sign == '-' and num2 == 13:
        return("4-13 = -9")
    if num1 == 4 and sign == '-' and num2 == 14:
        return("4-14 = -10")
    if num1 == 4 and sign == '-' and num2 == 15:
        return("4-15 = -11")
    if num1 == 4 and sign == '-' and num2 == 16:
        return("4-16 = -12")
    if num1 == 4 and sign == '-' and num2 == 17:
        return("4-17 = -13")
    if num1 == 4 and sign == '-' and num2 == 18:
        return("4-18 = -14")
    if num1 == 4 and sign == '-' and num2 == 19:
        return("4-19 = -15")
    if num1 == 4 and sign == '-' and num2 == 20:
        return("4-20 = -16")
    if num1 == 4 and sign == '-' and num2 == 21:
        return("4-21 = -17")
    if num1 == 4 and sign == '-' and num2 == 22:
        return("4-22 = -18")
    if num1 == 4 and sign == '-' and num2 == 23:
        return("4-23 = -19")
    if num1 == 4 and sign == '-' and num2 == 24:
        return("4-24 = -20")
    if num1 == 4 and sign == '-' and num2 == 25:
        return("4-25 = -21")
    if num1 == 4 and sign == '-' and num2 == 26:
        return("4-26 = -22")
    if num1 == 4 and sign == '-' and num2 == 27:
        return("4-27 = -23")
    if num1 == 4 and sign == '-' and num2 == 28:
        return("4-28 = -24")
    if num1 == 4 and sign == '-' and num2 == 29:
        return("4-29 = -25")
    if num1 == 4 and sign == '-' and num2 == 30:
        return("4-30 = -26")
    if num1 == 4 and sign == '-' and num2 == 31:
        return("4-31 = -27")
    if num1 == 4 and sign == '-' and num2 == 32:
        return("4-32 = -28")
    if num1 == 4 and sign == '-' and num2 == 33:
        return("4-33 = -29")
    if num1 == 4 and sign == '-' and num2 == 34:
        return("4-34 = -30")
    if num1 == 4 and sign == '-' and num2 == 35:
        return("4-35 = -31")
    if num1 == 4 and sign == '-' and num2 == 36:
        return("4-36 = -32")
    if num1 == 4 and sign == '-' and num2 == 37:
        return("4-37 = -33")
    if num1 == 4 and sign == '-' and num2 == 38:
        return("4-38 = -34")
    if num1 == 4 and sign == '-' and num2 == 39:
        return("4-39 = -35")
    if num1 == 4 and sign == '-' and num2 == 40:
        return("4-40 = -36")
    if num1 == 4 and sign == '-' and num2 == 41:
        return("4-41 = -37")
    if num1 == 4 and sign == '-' and num2 == 42:
        return("4-42 = -38")
    if num1 == 4 and sign == '-' and num2 == 43:
        return("4-43 = -39")
    if num1 == 4 and sign == '-' and num2 == 44:
        return("4-44 = -40")
    if num1 == 4 and sign == '-' and num2 == 45:
        return("4-45 = -41")
    if num1 == 4 and sign == '-' and num2 == 46:
        return("4-46 = -42")
    if num1 == 4 and sign == '-' and num2 == 47:
        return("4-47 = -43")
    if num1 == 4 and sign == '-' and num2 == 48:
        return("4-48 = -44")
    if num1 == 4 and sign == '-' and num2 == 49:
        return("4-49 = -45")
    if num1 == 4 and sign == '-' and num2 == 50:
        return("4-50 = -46")
    if num1 == 5 and sign == '-' and num2 == 0:
        return("5-0 = 5")
    if num1 == 5 and sign == '-' and num2 == 1:
        return("5-1 = 4")
    if num1 == 5 and sign == '-' and num2 == 2:
        return("5-2 = 3")
    if num1 == 5 and sign == '-' and num2 == 3:
        return("5-3 = 2")
    if num1 == 5 and sign == '-' and num2 == 4:
        return("5-4 = 1")
    if num1 == 5 and sign == '-' and num2 == 5:
        return("5-5 = 0")
    if num1 == 5 and sign == '-' and num2 == 6:
        return("5-6 = -1")
    if num1 == 5 and sign == '-' and num2 == 7:
        return("5-7 = -2")
    if num1 == 5 and sign == '-' and num2 == 8:
        return("5-8 = -3")
    if num1 == 5 and sign == '-' and num2 == 9:
        return("5-9 = -4")
    if num1 == 5 and sign == '-' and num2 == 10:
        return("5-10 = -5")
    if num1 == 5 and sign == '-' and num2 == 11:
        return("5-11 = -6")
    if num1 == 5 and sign == '-' and num2 == 12:
        return("5-12 = -7")
    if num1 == 5 and sign == '-' and num2 == 13:
        return("5-13 = -8")
    if num1 == 5 and sign == '-' and num2 == 14:
        return("5-14 = -9")
    if num1 == 5 and sign == '-' and num2 == 15:
        return("5-15 = -10")
    if num1 == 5 and sign == '-' and num2 == 16:
        return("5-16 = -11")
    if num1 == 5 and sign == '-' and num2 == 17:
        return("5-17 = -12")
    if num1 == 5 and sign == '-' and num2 == 18:
        return("5-18 = -13")
    if num1 == 5 and sign == '-' and num2 == 19:
        return("5-19 = -14")
    if num1 == 5 and sign == '-' and num2 == 20:
        return("5-20 = -15")
    if num1 == 5 and sign == '-' and num2 == 21:
        return("5-21 = -16")
    if num1 == 5 and sign == '-' and num2 == 22:
        return("5-22 = -17")
    if num1 == 5 and sign == '-' and num2 == 23:
        return("5-23 = -18")
    if num1 == 5 and sign == '-' and num2 == 24:
        return("5-24 = -19")
    if num1 == 5 and sign == '-' and num2 == 25:
        return("5-25 = -20")
    if num1 == 5 and sign == '-' and num2 == 26:
        return("5-26 = -21")
    if num1 == 5 and sign == '-' and num2 == 27:
        return("5-27 = -22")
    if num1 == 5 and sign == '-' and num2 == 28:
        return("5-28 = -23")
    if num1 == 5 and sign == '-' and num2 == 29:
        return("5-29 = -24")
    if num1 == 5 and sign == '-' and num2 == 30:
        return("5-30 = -25")
    if num1 == 5 and sign == '-' and num2 == 31:
        return("5-31 = -26")
    if num1 == 5 and sign == '-' and num2 == 32:
        return("5-32 = -27")
    if num1 == 5 and sign == '-' and num2 == 33:
        return("5-33 = -28")
    if num1 == 5 and sign == '-' and num2 == 34:
        return("5-34 = -29")
    if num1 == 5 and sign == '-' and num2 == 35:
        return("5-35 = -30")
    if num1 == 5 and sign == '-' and num2 == 36:
        return("5-36 = -31")
    if num1 == 5 and sign == '-' and num2 == 37:
        return("5-37 = -32")
    if num1 == 5 and sign == '-' and num2 == 38:
        return("5-38 = -33")
    if num1 == 5 and sign == '-' and num2 == 39:
        return("5-39 = -34")
    if num1 == 5 and sign == '-' and num2 == 40:
        return("5-40 = -35")
    if num1 == 5 and sign == '-' and num2 == 41:
        return("5-41 = -36")
    if num1 == 5 and sign == '-' and num2 == 42:
        return("5-42 = -37")
    if num1 == 5 and sign == '-' and num2 == 43:
        return("5-43 = -38")
    if num1 == 5 and sign == '-' and num2 == 44:
        return("5-44 = -39")
    if num1 == 5 and sign == '-' and num2 == 45:
        return("5-45 = -40")
    if num1 == 5 and sign == '-' and num2 == 46:
        return("5-46 = -41")
    if num1 == 5 and sign == '-' and num2 == 47:
        return("5-47 = -42")
    if num1 == 5 and sign == '-' and num2 == 48:
        return("5-48 = -43")
    if num1 == 5 and sign == '-' and num2 == 49:
        return("5-49 = -44")
    if num1 == 5 and sign == '-' and num2 == 50:
        return("5-50 = -45")
    if num1 == 6 and sign == '-' and num2 == 0:
        return("6-0 = 6")
    if num1 == 6 and sign == '-' and num2 == 1:
        return("6-1 = 5")
    if num1 == 6 and sign == '-' and num2 == 2:
        return("6-2 = 4")
    if num1 == 6 and sign == '-' and num2 == 3:
        return("6-3 = 3")
    if num1 == 6 and sign == '-' and num2 == 4:
        return("6-4 = 2")
    if num1 == 6 and sign == '-' and num2 == 5:
        return("6-5 = 1")
    if num1 == 6 and sign == '-' and num2 == 6:
        return("6-6 = 0")
    if num1 == 6 and sign == '-' and num2 == 7:
        return("6-7 = -1")
    if num1 == 6 and sign == '-' and num2 == 8:
        return("6-8 = -2")
    if num1 == 6 and sign == '-' and num2 == 9:
        return("6-9 = -3")
    if num1 == 6 and sign == '-' and num2 == 10:
        return("6-10 = -4")
    if num1 == 6 and sign == '-' and num2 == 11:
        return("6-11 = -5")
    if num1 == 6 and sign == '-' and num2 == 12:
        return("6-12 = -6")
    if num1 == 6 and sign == '-' and num2 == 13:
        return("6-13 = -7")
    if num1 == 6 and sign == '-' and num2 == 14:
        return("6-14 = -8")
    if num1 == 6 and sign == '-' and num2 == 15:
        return("6-15 = -9")
    if num1 == 6 and sign == '-' and num2 == 16:
        return("6-16 = -10")
    if num1 == 6 and sign == '-' and num2 == 17:
        return("6-17 = -11")
    if num1 == 6 and sign == '-' and num2 == 18:
        return("6-18 = -12")
    if num1 == 6 and sign == '-' and num2 == 19:
        return("6-19 = -13")
    if num1 == 6 and sign == '-' and num2 == 20:
        return("6-20 = -14")
    if num1 == 6 and sign == '-' and num2 == 21:
        return("6-21 = -15")
    if num1 == 6 and sign == '-' and num2 == 22:
        return("6-22 = -16")
    if num1 == 6 and sign == '-' and num2 == 23:
        return("6-23 = -17")
    if num1 == 6 and sign == '-' and num2 == 24:
        return("6-24 = -18")
    if num1 == 6 and sign == '-' and num2 == 25:
        return("6-25 = -19")
    if num1 == 6 and sign == '-' and num2 == 26:
        return("6-26 = -20")
    if num1 == 6 and sign == '-' and num2 == 27:
        return("6-27 = -21")
    if num1 == 6 and sign == '-' and num2 == 28:
        return("6-28 = -22")
    if num1 == 6 and sign == '-' and num2 == 29:
        return("6-29 = -23")
    if num1 == 6 and sign == '-' and num2 == 30:
        return("6-30 = -24")
    if num1 == 6 and sign == '-' and num2 == 31:
        return("6-31 = -25")
    if num1 == 6 and sign == '-' and num2 == 32:
        return("6-32 = -26")
    if num1 == 6 and sign == '-' and num2 == 33:
        return("6-33 = -27")
    if num1 == 6 and sign == '-' and num2 == 34:
        return("6-34 = -28")
    if num1 == 6 and sign == '-' and num2 == 35:
        return("6-35 = -29")
    if num1 == 6 and sign == '-' and num2 == 36:
        return("6-36 = -30")
    if num1 == 6 and sign == '-' and num2 == 37:
        return("6-37 = -31")
    if num1 == 6 and sign == '-' and num2 == 38:
        return("6-38 = -32")
    if num1 == 6 and sign == '-' and num2 == 39:
        return("6-39 = -33")
    if num1 == 6 and sign == '-' and num2 == 40:
        return("6-40 = -34")
    if num1 == 6 and sign == '-' and num2 == 41:
        return("6-41 = -35")
    if num1 == 6 and sign == '-' and num2 == 42:
        return("6-42 = -36")
    if num1 == 6 and sign == '-' and num2 == 43:
        return("6-43 = -37")
    if num1 == 6 and sign == '-' and num2 == 44:
        return("6-44 = -38")
    if num1 == 6 and sign == '-' and num2 == 45:
        return("6-45 = -39")
    if num1 == 6 and sign == '-' and num2 == 46:
        return("6-46 = -40")
    if num1 == 6 and sign == '-' and num2 == 47:
        return("6-47 = -41")
    if num1 == 6 and sign == '-' and num2 == 48:
        return("6-48 = -42")
    if num1 == 6 and sign == '-' and num2 == 49:
        return("6-49 = -43")
    if num1 == 6 and sign == '-' and num2 == 50:
        return("6-50 = -44")
    if num1 == 7 and sign == '-' and num2 == 0:
        return("7-0 = 7")
    if num1 == 7 and sign == '-' and num2 == 1:
        return("7-1 = 6")
    if num1 == 7 and sign == '-' and num2 == 2:
        return("7-2 = 5")
    if num1 == 7 and sign == '-' and num2 == 3:
        return("7-3 = 4")
    if num1 == 7 and sign == '-' and num2 == 4:
        return("7-4 = 3")
    if num1 == 7 and sign == '-' and num2 == 5:
        return("7-5 = 2")
    if num1 == 7 and sign == '-' and num2 == 6:
        return("7-6 = 1")
    if num1 == 7 and sign == '-' and num2 == 7:
        return("7-7 = 0")
    if num1 == 7 and sign == '-' and num2 == 8:
        return("7-8 = -1")
    if num1 == 7 and sign == '-' and num2 == 9:
        return("7-9 = -2")
    if num1 == 7 and sign == '-' and num2 == 10:
        return("7-10 = -3")
    if num1 == 7 and sign == '-' and num2 == 11:
        return("7-11 = -4")
    if num1 == 7 and sign == '-' and num2 == 12:
        return("7-12 = -5")
    if num1 == 7 and sign == '-' and num2 == 13:
        return("7-13 = -6")
    if num1 == 7 and sign == '-' and num2 == 14:
        return("7-14 = -7")
    if num1 == 7 and sign == '-' and num2 == 15:
        return("7-15 = -8")
    if num1 == 7 and sign == '-' and num2 == 16:
        return("7-16 = -9")
    if num1 == 7 and sign == '-' and num2 == 17:
        return("7-17 = -10")
    if num1 == 7 and sign == '-' and num2 == 18:
        return("7-18 = -11")
    if num1 == 7 and sign == '-' and num2 == 19:
        return("7-19 = -12")
    if num1 == 7 and sign == '-' and num2 == 20:
        return("7-20 = -13")
    if num1 == 7 and sign == '-' and num2 == 21:
        return("7-21 = -14")
    if num1 == 7 and sign == '-' and num2 == 22:
        return("7-22 = -15")
    if num1 == 7 and sign == '-' and num2 == 23:
        return("7-23 = -16")
    if num1 == 7 and sign == '-' and num2 == 24:
        return("7-24 = -17")
    if num1 == 7 and sign == '-' and num2 == 25:
        return("7-25 = -18")
    if num1 == 7 and sign == '-' and num2 == 26:
        return("7-26 = -19")
    if num1 == 7 and sign == '-' and num2 == 27:
        return("7-27 = -20")
    if num1 == 7 and sign == '-' and num2 == 28:
        return("7-28 = -21")
    if num1 == 7 and sign == '-' and num2 == 29:
        return("7-29 = -22")
    if num1 == 7 and sign == '-' and num2 == 30:
        return("7-30 = -23")
    if num1 == 7 and sign == '-' and num2 == 31:
        return("7-31 = -24")
    if num1 == 7 and sign == '-' and num2 == 32:
        return("7-32 = -25")
    if num1 == 7 and sign == '-' and num2 == 33:
        return("7-33 = -26")
    if num1 == 7 and sign == '-' and num2 == 34:
        return("7-34 = -27")
    if num1 == 7 and sign == '-' and num2 == 35:
        return("7-35 = -28")
    if num1 == 7 and sign == '-' and num2 == 36:
        return("7-36 = -29")
    if num1 == 7 and sign == '-' and num2 == 37:
        return("7-37 = -30")
    if num1 == 7 and sign == '-' and num2 == 38:
        return("7-38 = -31")
    if num1 == 7 and sign == '-' and num2 == 39:
        return("7-39 = -32")
    if num1 == 7 and sign == '-' and num2 == 40:
        return("7-40 = -33")
    if num1 == 7 and sign == '-' and num2 == 41:
        return("7-41 = -34")
    if num1 == 7 and sign == '-' and num2 == 42:
        return("7-42 = -35")
    if num1 == 7 and sign == '-' and num2 == 43:
        return("7-43 = -36")
    if num1 == 7 and sign == '-' and num2 == 44:
        return("7-44 = -37")
    if num1 == 7 and sign == '-' and num2 == 45:
        return("7-45 = -38")
    if num1 == 7 and sign == '-' and num2 == 46:
        return("7-46 = -39")
    if num1 == 7 and sign == '-' and num2 == 47:
        return("7-47 = -40")
    if num1 == 7 and sign == '-' and num2 == 48:
        return("7-48 = -41")
    if num1 == 7 and sign == '-' and num2 == 49:
        return("7-49 = -42")
    if num1 == 7 and sign == '-' and num2 == 50:
        return("7-50 = -43")
    if num1 == 8 and sign == '-' and num2 == 0:
        return("8-0 = 8")
    if num1 == 8 and sign == '-' and num2 == 1:
        return("8-1 = 7")
    if num1 == 8 and sign == '-' and num2 == 2:
        return("8-2 = 6")
    if num1 == 8 and sign == '-' and num2 == 3:
        return("8-3 = 5")
    if num1 == 8 and sign == '-' and num2 == 4:
        return("8-4 = 4")
    if num1 == 8 and sign == '-' and num2 == 5:
        return("8-5 = 3")
    if num1 == 8 and sign == '-' and num2 == 6:
        return("8-6 = 2")
    if num1 == 8 and sign == '-' and num2 == 7:
        return("8-7 = 1")
    if num1 == 8 and sign == '-' and num2 == 8:
        return("8-8 = 0")
    if num1 == 8 and sign == '-' and num2 == 9:
        return("8-9 = -1")
    if num1 == 8 and sign == '-' and num2 == 10:
        return("8-10 = -2")
    if num1 == 8 and sign == '-' and num2 == 11:
        return("8-11 = -3")
    if num1 == 8 and sign == '-' and num2 == 12:
        return("8-12 = -4")
    if num1 == 8 and sign == '-' and num2 == 13:
        return("8-13 = -5")
    if num1 == 8 and sign == '-' and num2 == 14:
        return("8-14 = -6")
    if num1 == 8 and sign == '-' and num2 == 15:
        return("8-15 = -7")
    if num1 == 8 and sign == '-' and num2 == 16:
        return("8-16 = -8")
    if num1 == 8 and sign == '-' and num2 == 17:
        return("8-17 = -9")
    if num1 == 8 and sign == '-' and num2 == 18:
        return("8-18 = -10")
    if num1 == 8 and sign == '-' and num2 == 19:
        return("8-19 = -11")
    if num1 == 8 and sign == '-' and num2 == 20:
        return("8-20 = -12")
    if num1 == 8 and sign == '-' and num2 == 21:
        return("8-21 = -13")
    if num1 == 8 and sign == '-' and num2 == 22:
        return("8-22 = -14")
    if num1 == 8 and sign == '-' and num2 == 23:
        return("8-23 = -15")
    if num1 == 8 and sign == '-' and num2 == 24:
        return("8-24 = -16")
    if num1 == 8 and sign == '-' and num2 == 25:
        return("8-25 = -17")
    if num1 == 8 and sign == '-' and num2 == 26:
        return("8-26 = -18")
    if num1 == 8 and sign == '-' and num2 == 27:
        return("8-27 = -19")
    if num1 == 8 and sign == '-' and num2 == 28:
        return("8-28 = -20")
    if num1 == 8 and sign == '-' and num2 == 29:
        return("8-29 = -21")
    if num1 == 8 and sign == '-' and num2 == 30:
        return("8-30 = -22")
    if num1 == 8 and sign == '-' and num2 == 31:
        return("8-31 = -23")
    if num1 == 8 and sign == '-' and num2 == 32:
        return("8-32 = -24")
    if num1 == 8 and sign == '-' and num2 == 33:
        return("8-33 = -25")
    if num1 == 8 and sign == '-' and num2 == 34:
        return("8-34 = -26")
    if num1 == 8 and sign == '-' and num2 == 35:
        return("8-35 = -27")
    if num1 == 8 and sign == '-' and num2 == 36:
        return("8-36 = -28")
    if num1 == 8 and sign == '-' and num2 == 37:
        return("8-37 = -29")
    if num1 == 8 and sign == '-' and num2 == 38:
        return("8-38 = -30")
    if num1 == 8 and sign == '-' and num2 == 39:
        return("8-39 = -31")
    if num1 == 8 and sign == '-' and num2 == 40:
        return("8-40 = -32")
    if num1 == 8 and sign == '-' and num2 == 41:
        return("8-41 = -33")
    if num1 == 8 and sign == '-' and num2 == 42:
        return("8-42 = -34")
    if num1 == 8 and sign == '-' and num2 == 43:
        return("8-43 = -35")
    if num1 == 8 and sign == '-' and num2 == 44:
        return("8-44 = -36")
    if num1 == 8 and sign == '-' and num2 == 45:
        return("8-45 = -37")
    if num1 == 8 and sign == '-' and num2 == 46:
        return("8-46 = -38")
    if num1 == 8 and sign == '-' and num2 == 47:
        return("8-47 = -39")
    if num1 == 8 and sign == '-' and num2 == 48:
        return("8-48 = -40")
    if num1 == 8 and sign == '-' and num2 == 49:
        return("8-49 = -41")
    if num1 == 8 and sign == '-' and num2 == 50:
        return("8-50 = -42")
    if num1 == 9 and sign == '-' and num2 == 0:
        return("9-0 = 9")
    if num1 == 9 and sign == '-' and num2 == 1:
        return("9-1 = 8")
    if num1 == 9 and sign == '-' and num2 == 2:
        return("9-2 = 7")
    if num1 == 9 and sign == '-' and num2 == 3:
        return("9-3 = 6")
    if num1 == 9 and sign == '-' and num2 == 4:
        return("9-4 = 5")
    if num1 == 9 and sign == '-' and num2 == 5:
        return("9-5 = 4")
    if num1 == 9 and sign == '-' and num2 == 6:
        return("9-6 = 3")
    if num1 == 9 and sign == '-' and num2 == 7:
        return("9-7 = 2")
    if num1 == 9 and sign == '-' and num2 == 8:
        return("9-8 = 1")
    if num1 == 9 and sign == '-' and num2 == 9:
        return("9-9 = 0")
    if num1 == 9 and sign == '-' and num2 == 10:
        return("9-10 = -1")
    if num1 == 9 and sign == '-' and num2 == 11:
        return("9-11 = -2")
    if num1 == 9 and sign == '-' and num2 == 12:
        return("9-12 = -3")
    if num1 == 9 and sign == '-' and num2 == 13:
        return("9-13 = -4")
    if num1 == 9 and sign == '-' and num2 == 14:
        return("9-14 = -5")
    if num1 == 9 and sign == '-' and num2 == 15:
        return("9-15 = -6")
    if num1 == 9 and sign == '-' and num2 == 16:
        return("9-16 = -7")
    if num1 == 9 and sign == '-' and num2 == 17:
        return("9-17 = -8")
    if num1 == 9 and sign == '-' and num2 == 18:
        return("9-18 = -9")
    if num1 == 9 and sign == '-' and num2 == 19:
        return("9-19 = -10")
    if num1 == 9 and sign == '-' and num2 == 20:
        return("9-20 = -11")
    if num1 == 9 and sign == '-' and num2 == 21:
        return("9-21 = -12")
    if num1 == 9 and sign == '-' and num2 == 22:
        return("9-22 = -13")
    if num1 == 9 and sign == '-' and num2 == 23:
        return("9-23 = -14")
    if num1 == 9 and sign == '-' and num2 == 24:
        return("9-24 = -15")
    if num1 == 9 and sign == '-' and num2 == 25:
        return("9-25 = -16")
    if num1 == 9 and sign == '-' and num2 == 26:
        return("9-26 = -17")
    if num1 == 9 and sign == '-' and num2 == 27:
        return("9-27 = -18")
    if num1 == 9 and sign == '-' and num2 == 28:
        return("9-28 = -19")
    if num1 == 9 and sign == '-' and num2 == 29:
        return("9-29 = -20")
    if num1 == 9 and sign == '-' and num2 == 30:
        return("9-30 = -21")
    if num1 == 9 and sign == '-' and num2 == 31:
        return("9-31 = -22")
    if num1 == 9 and sign == '-' and num2 == 32:
        return("9-32 = -23")
    if num1 == 9 and sign == '-' and num2 == 33:
        return("9-33 = -24")
    if num1 == 9 and sign == '-' and num2 == 34:
        return("9-34 = -25")
    if num1 == 9 and sign == '-' and num2 == 35:
        return("9-35 = -26")
    if num1 == 9 and sign == '-' and num2 == 36:
        return("9-36 = -27")
    if num1 == 9 and sign == '-' and num2 == 37:
        return("9-37 = -28")
    if num1 == 9 and sign == '-' and num2 == 38:
        return("9-38 = -29")
    if num1 == 9 and sign == '-' and num2 == 39:
        return("9-39 = -30")
    if num1 == 9 and sign == '-' and num2 == 40:
        return("9-40 = -31")
    if num1 == 9 and sign == '-' and num2 == 41:
        return("9-41 = -32")
    if num1 == 9 and sign == '-' and num2 == 42:
        return("9-42 = -33")
    if num1 == 9 and sign == '-' and num2 == 43:
        return("9-43 = -34")
    if num1 == 9 and sign == '-' and num2 == 44:
        return("9-44 = -35")
    if num1 == 9 and sign == '-' and num2 == 45:
        return("9-45 = -36")
    if num1 == 9 and sign == '-' and num2 == 46:
        return("9-46 = -37")
    if num1 == 9 and sign == '-' and num2 == 47:
        return("9-47 = -38")
    if num1 == 9 and sign == '-' and num2 == 48:
        return("9-48 = -39")
    if num1 == 9 and sign == '-' and num2 == 49:
        return("9-49 = -40")
    if num1 == 9 and sign == '-' and num2 == 50:
        return("9-50 = -41")
    if num1 == 10 and sign == '-' and num2 == 0:
        return("10-0 = 10")
    if num1 == 10 and sign == '-' and num2 == 1:
        return("10-1 = 9")
    if num1 == 10 and sign == '-' and num2 == 2:
        return("10-2 = 8")
    if num1 == 10 and sign == '-' and num2 == 3:
        return("10-3 = 7")
    if num1 == 10 and sign == '-' and num2 == 4:
        return("10-4 = 6")
    if num1 == 10 and sign == '-' and num2 == 5:
        return("10-5 = 5")
    if num1 == 10 and sign == '-' and num2 == 6:
        return("10-6 = 4")
    if num1 == 10 and sign == '-' and num2 == 7:
        return("10-7 = 3")
    if num1 == 10 and sign == '-' and num2 == 8:
        return("10-8 = 2")
    if num1 == 10 and sign == '-' and num2 == 9:
        return("10-9 = 1")
    if num1 == 10 and sign == '-' and num2 == 10:
        return("10-10 = 0")
    if num1 == 10 and sign == '-' and num2 == 11:
        return("10-11 = -1")
    if num1 == 10 and sign == '-' and num2 == 12:
        return("10-12 = -2")
    if num1 == 10 and sign == '-' and num2 == 13:
        return("10-13 = -3")
    if num1 == 10 and sign == '-' and num2 == 14:
        return("10-14 = -4")
    if num1 == 10 and sign == '-' and num2 == 15:
        return("10-15 = -5")
    if num1 == 10 and sign == '-' and num2 == 16:
        return("10-16 = -6")
    if num1 == 10 and sign == '-' and num2 == 17:
        return("10-17 = -7")
    if num1 == 10 and sign == '-' and num2 == 18:
        return("10-18 = -8")
    if num1 == 10 and sign == '-' and num2 == 19:
        return("10-19 = -9")
    if num1 == 10 and sign == '-' and num2 == 20:
        return("10-20 = -10")
    if num1 == 10 and sign == '-' and num2 == 21:
        return("10-21 = -11")
    if num1 == 10 and sign == '-' and num2 == 22:
        return("10-22 = -12")
    if num1 == 10 and sign == '-' and num2 == 23:
        return("10-23 = -13")
    if num1 == 10 and sign == '-' and num2 == 24:
        return("10-24 = -14")
    if num1 == 10 and sign == '-' and num2 == 25:
        return("10-25 = -15")
    if num1 == 10 and sign == '-' and num2 == 26:
        return("10-26 = -16")
    if num1 == 10 and sign == '-' and num2 == 27:
        return("10-27 = -17")
    if num1 == 10 and sign == '-' and num2 == 28:
        return("10-28 = -18")
    if num1 == 10 and sign == '-' and num2 == 29:
        return("10-29 = -19")
    if num1 == 10 and sign == '-' and num2 == 30:
        return("10-30 = -20")
    if num1 == 10 and sign == '-' and num2 == 31:
        return("10-31 = -21")
    if num1 == 10 and sign == '-' and num2 == 32:
        return("10-32 = -22")
    if num1 == 10 and sign == '-' and num2 == 33:
        return("10-33 = -23")
    if num1 == 10 and sign == '-' and num2 == 34:
        return("10-34 = -24")
    if num1 == 10 and sign == '-' and num2 == 35:
        return("10-35 = -25")
    if num1 == 10 and sign == '-' and num2 == 36:
        return("10-36 = -26")
    if num1 == 10 and sign == '-' and num2 == 37:
        return("10-37 = -27")
    if num1 == 10 and sign == '-' and num2 == 38:
        return("10-38 = -28")
    if num1 == 10 and sign == '-' and num2 == 39:
        return("10-39 = -29")
    if num1 == 10 and sign == '-' and num2 == 40:
        return("10-40 = -30")
    if num1 == 10 and sign == '-' and num2 == 41:
        return("10-41 = -31")
    if num1 == 10 and sign == '-' and num2 == 42:
        return("10-42 = -32")
    if num1 == 10 and sign == '-' and num2 == 43:
        return("10-43 = -33")
    if num1 == 10 and sign == '-' and num2 == 44:
        return("10-44 = -34")
    if num1 == 10 and sign == '-' and num2 == 45:
        return("10-45 = -35")
    if num1 == 10 and sign == '-' and num2 == 46:
        return("10-46 = -36")
    if num1 == 10 and sign == '-' and num2 == 47:
        return("10-47 = -37")
    if num1 == 10 and sign == '-' and num2 == 48:
        return("10-48 = -38")
    if num1 == 10 and sign == '-' and num2 == 49:
        return("10-49 = -39")
    if num1 == 10 and sign == '-' and num2 == 50:
        return("10-50 = -40")
    if num1 == 11 and sign == '-' and num2 == 0:
        return("11-0 = 11")
    if num1 == 11 and sign == '-' and num2 == 1:
        return("11-1 = 10")
    if num1 == 11 and sign == '-' and num2 == 2:
        return("11-2 = 9")
    if num1 == 11 and sign == '-' and num2 == 3:
        return("11-3 = 8")
    if num1 == 11 and sign == '-' and num2 == 4:
        return("11-4 = 7")
    if num1 == 11 and sign == '-' and num2 == 5:
        return("11-5 = 6")
    if num1 == 11 and sign == '-' and num2 == 6:
        return("11-6 = 5")
    if num1 == 11 and sign == '-' and num2 == 7:
        return("11-7 = 4")
    if num1 == 11 and sign == '-' and num2 == 8:
        return("11-8 = 3")
    if num1 == 11 and sign == '-' and num2 == 9:
        return("11-9 = 2")
    if num1 == 11 and sign == '-' and num2 == 10:
        return("11-10 = 1")
    if num1 == 11 and sign == '-' and num2 == 11:
        return("11-11 = 0")
    if num1 == 11 and sign == '-' and num2 == 12:
        return("11-12 = -1")
    if num1 == 11 and sign == '-' and num2 == 13:
        return("11-13 = -2")
    if num1 == 11 and sign == '-' and num2 == 14:
        return("11-14 = -3")
    if num1 == 11 and sign == '-' and num2 == 15:
        return("11-15 = -4")
    if num1 == 11 and sign == '-' and num2 == 16:
        return("11-16 = -5")
    if num1 == 11 and sign == '-' and num2 == 17:
        return("11-17 = -6")
    if num1 == 11 and sign == '-' and num2 == 18:
        return("11-18 = -7")
    if num1 == 11 and sign == '-' and num2 == 19:
        return("11-19 = -8")
    if num1 == 11 and sign == '-' and num2 == 20:
        return("11-20 = -9")
    if num1 == 11 and sign == '-' and num2 == 21:
        return("11-21 = -10")
    if num1 == 11 and sign == '-' and num2 == 22:
        return("11-22 = -11")
    if num1 == 11 and sign == '-' and num2 == 23:
        return("11-23 = -12")
    if num1 == 11 and sign == '-' and num2 == 24:
        return("11-24 = -13")
    if num1 == 11 and sign == '-' and num2 == 25:
        return("11-25 = -14")
    if num1 == 11 and sign == '-' and num2 == 26:
        return("11-26 = -15")
    if num1 == 11 and sign == '-' and num2 == 27:
        return("11-27 = -16")
    if num1 == 11 and sign == '-' and num2 == 28:
        return("11-28 = -17")
    if num1 == 11 and sign == '-' and num2 == 29:
        return("11-29 = -18")
    if num1 == 11 and sign == '-' and num2 == 30:
        return("11-30 = -19")
    if num1 == 11 and sign == '-' and num2 == 31:
        return("11-31 = -20")
    if num1 == 11 and sign == '-' and num2 == 32:
        return("11-32 = -21")
    if num1 == 11 and sign == '-' and num2 == 33:
        return("11-33 = -22")
    if num1 == 11 and sign == '-' and num2 == 34:
        return("11-34 = -23")
    if num1 == 11 and sign == '-' and num2 == 35:
        return("11-35 = -24")
    if num1 == 11 and sign == '-' and num2 == 36:
        return("11-36 = -25")
    if num1 == 11 and sign == '-' and num2 == 37:
        return("11-37 = -26")
    if num1 == 11 and sign == '-' and num2 == 38:
        return("11-38 = -27")
    if num1 == 11 and sign == '-' and num2 == 39:
        return("11-39 = -28")
    if num1 == 11 and sign == '-' and num2 == 40:
        return("11-40 = -29")
    if num1 == 11 and sign == '-' and num2 == 41:
        return("11-41 = -30")
    if num1 == 11 and sign == '-' and num2 == 42:
        return("11-42 = -31")
    if num1 == 11 and sign == '-' and num2 == 43:
        return("11-43 = -32")
    if num1 == 11 and sign == '-' and num2 == 44:
        return("11-44 = -33")
    if num1 == 11 and sign == '-' and num2 == 45:
        return("11-45 = -34")
    if num1 == 11 and sign == '-' and num2 == 46:
        return("11-46 = -35")
    if num1 == 11 and sign == '-' and num2 == 47:
        return("11-47 = -36")
    if num1 == 11 and sign == '-' and num2 == 48:
        return("11-48 = -37")
    if num1 == 11 and sign == '-' and num2 == 49:
        return("11-49 = -38")
    if num1 == 11 and sign == '-' and num2 == 50:
        return("11-50 = -39")
    if num1 == 12 and sign == '-' and num2 == 0:
        return("12-0 = 12")
    if num1 == 12 and sign == '-' and num2 == 1:
        return("12-1 = 11")
    if num1 == 12 and sign == '-' and num2 == 2:
        return("12-2 = 10")
    if num1 == 12 and sign == '-' and num2 == 3:
        return("12-3 = 9")
    if num1 == 12 and sign == '-' and num2 == 4:
        return("12-4 = 8")
    if num1 == 12 and sign == '-' and num2 == 5:
        return("12-5 = 7")
    if num1 == 12 and sign == '-' and num2 == 6:
        return("12-6 = 6")
    if num1 == 12 and sign == '-' and num2 == 7:
        return("12-7 = 5")
    if num1 == 12 and sign == '-' and num2 == 8:
        return("12-8 = 4")
    if num1 == 12 and sign == '-' and num2 == 9:
        return("12-9 = 3")
    if num1 == 12 and sign == '-' and num2 == 10:
        return("12-10 = 2")
    if num1 == 12 and sign == '-' and num2 == 11:
        return("12-11 = 1")
    if num1 == 12 and sign == '-' and num2 == 12:
        return("12-12 = 0")
    if num1 == 12 and sign == '-' and num2 == 13:
        return("12-13 = -1")
    if num1 == 12 and sign == '-' and num2 == 14:
        return("12-14 = -2")
    if num1 == 12 and sign == '-' and num2 == 15:
        return("12-15 = -3")
    if num1 == 12 and sign == '-' and num2 == 16:
        return("12-16 = -4")
    if num1 == 12 and sign == '-' and num2 == 17:
        return("12-17 = -5")
    if num1 == 12 and sign == '-' and num2 == 18:
        return("12-18 = -6")
    if num1 == 12 and sign == '-' and num2 == 19:
        return("12-19 = -7")
    if num1 == 12 and sign == '-' and num2 == 20:
        return("12-20 = -8")
    if num1 == 12 and sign == '-' and num2 == 21:
        return("12-21 = -9")
    if num1 == 12 and sign == '-' and num2 == 22:
        return("12-22 = -10")
    if num1 == 12 and sign == '-' and num2 == 23:
        return("12-23 = -11")
    if num1 == 12 and sign == '-' and num2 == 24:
        return("12-24 = -12")
    if num1 == 12 and sign == '-' and num2 == 25:
        return("12-25 = -13")
    if num1 == 12 and sign == '-' and num2 == 26:
        return("12-26 = -14")
    if num1 == 12 and sign == '-' and num2 == 27:
        return("12-27 = -15")
    if num1 == 12 and sign == '-' and num2 == 28:
        return("12-28 = -16")
    if num1 == 12 and sign == '-' and num2 == 29:
        return("12-29 = -17")
    if num1 == 12 and sign == '-' and num2 == 30:
        return("12-30 = -18")
    if num1 == 12 and sign == '-' and num2 == 31:
        return("12-31 = -19")
    if num1 == 12 and sign == '-' and num2 == 32:
        return("12-32 = -20")
    if num1 == 12 and sign == '-' and num2 == 33:
        return("12-33 = -21")
    if num1 == 12 and sign == '-' and num2 == 34:
        return("12-34 = -22")
    if num1 == 12 and sign == '-' and num2 == 35:
        return("12-35 = -23")
    if num1 == 12 and sign == '-' and num2 == 36:
        return("12-36 = -24")
    if num1 == 12 and sign == '-' and num2 == 37:
        return("12-37 = -25")
    if num1 == 12 and sign == '-' and num2 == 38:
        return("12-38 = -26")
    if num1 == 12 and sign == '-' and num2 == 39:
        return("12-39 = -27")
    if num1 == 12 and sign == '-' and num2 == 40:
        return("12-40 = -28")
    if num1 == 12 and sign == '-' and num2 == 41:
        return("12-41 = -29")
    if num1 == 12 and sign == '-' and num2 == 42:
        return("12-42 = -30")
    if num1 == 12 and sign == '-' and num2 == 43:
        return("12-43 = -31")
    if num1 == 12 and sign == '-' and num2 == 44:
        return("12-44 = -32")
    if num1 == 12 and sign == '-' and num2 == 45:
        return("12-45 = -33")
    if num1 == 12 and sign == '-' and num2 == 46:
        return("12-46 = -34")
    if num1 == 12 and sign == '-' and num2 == 47:
        return("12-47 = -35")
    if num1 == 12 and sign == '-' and num2 == 48:
        return("12-48 = -36")
    if num1 == 12 and sign == '-' and num2 == 49:
        return("12-49 = -37")
    if num1 == 12 and sign == '-' and num2 == 50:
        return("12-50 = -38")
    if num1 == 13 and sign == '-' and num2 == 0:
        return("13-0 = 13")
    if num1 == 13 and sign == '-' and num2 == 1:
        return("13-1 = 12")
    if num1 == 13 and sign == '-' and num2 == 2:
        return("13-2 = 11")
    if num1 == 13 and sign == '-' and num2 == 3:
        return("13-3 = 10")
    if num1 == 13 and sign == '-' and num2 == 4:
        return("13-4 = 9")
    if num1 == 13 and sign == '-' and num2 == 5:
        return("13-5 = 8")
    if num1 == 13 and sign == '-' and num2 == 6:
        return("13-6 = 7")
    if num1 == 13 and sign == '-' and num2 == 7:
        return("13-7 = 6")
    if num1 == 13 and sign == '-' and num2 == 8:
        return("13-8 = 5")
    if num1 == 13 and sign == '-' and num2 == 9:
        return("13-9 = 4")
    if num1 == 13 and sign == '-' and num2 == 10:
        return("13-10 = 3")
    if num1 == 13 and sign == '-' and num2 == 11:
        return("13-11 = 2")
    if num1 == 13 and sign == '-' and num2 == 12:
        return("13-12 = 1")
    if num1 == 13 and sign == '-' and num2 == 13:
        return("13-13 = 0")
    if num1 == 13 and sign == '-' and num2 == 14:
        return("13-14 = -1")
    if num1 == 13 and sign == '-' and num2 == 15:
        return("13-15 = -2")
    if num1 == 13 and sign == '-' and num2 == 16:
        return("13-16 = -3")
    if num1 == 13 and sign == '-' and num2 == 17:
        return("13-17 = -4")
    if num1 == 13 and sign == '-' and num2 == 18:
        return("13-18 = -5")
    if num1 == 13 and sign == '-' and num2 == 19:
        return("13-19 = -6")
    if num1 == 13 and sign == '-' and num2 == 20:
        return("13-20 = -7")
    if num1 == 13 and sign == '-' and num2 == 21:
        return("13-21 = -8")
    if num1 == 13 and sign == '-' and num2 == 22:
        return("13-22 = -9")
    if num1 == 13 and sign == '-' and num2 == 23:
        return("13-23 = -10")
    if num1 == 13 and sign == '-' and num2 == 24:
        return("13-24 = -11")
    if num1 == 13 and sign == '-' and num2 == 25:
        return("13-25 = -12")
    if num1 == 13 and sign == '-' and num2 == 26:
        return("13-26 = -13")
    if num1 == 13 and sign == '-' and num2 == 27:
        return("13-27 = -14")
    if num1 == 13 and sign == '-' and num2 == 28:
        return("13-28 = -15")
    if num1 == 13 and sign == '-' and num2 == 29:
        return("13-29 = -16")
    if num1 == 13 and sign == '-' and num2 == 30:
        return("13-30 = -17")
    if num1 == 13 and sign == '-' and num2 == 31:
        return("13-31 = -18")
    if num1 == 13 and sign == '-' and num2 == 32:
        return("13-32 = -19")
    if num1 == 13 and sign == '-' and num2 == 33:
        return("13-33 = -20")
    if num1 == 13 and sign == '-' and num2 == 34:
        return("13-34 = -21")
    if num1 == 13 and sign == '-' and num2 == 35:
        return("13-35 = -22")
    if num1 == 13 and sign == '-' and num2 == 36:
        return("13-36 = -23")
    if num1 == 13 and sign == '-' and num2 == 37:
        return("13-37 = -24")
    if num1 == 13 and sign == '-' and num2 == 38:
        return("13-38 = -25")
    if num1 == 13 and sign == '-' and num2 == 39:
        return("13-39 = -26")
    if num1 == 13 and sign == '-' and num2 == 40:
        return("13-40 = -27")
    if num1 == 13 and sign == '-' and num2 == 41:
        return("13-41 = -28")
    if num1 == 13 and sign == '-' and num2 == 42:
        return("13-42 = -29")
    if num1 == 13 and sign == '-' and num2 == 43:
        return("13-43 = -30")
    if num1 == 13 and sign == '-' and num2 == 44:
        return("13-44 = -31")
    if num1 == 13 and sign == '-' and num2 == 45:
        return("13-45 = -32")
    if num1 == 13 and sign == '-' and num2 == 46:
        return("13-46 = -33")
    if num1 == 13 and sign == '-' and num2 == 47:
        return("13-47 = -34")
    if num1 == 13 and sign == '-' and num2 == 48:
        return("13-48 = -35")
    if num1 == 13 and sign == '-' and num2 == 49:
        return("13-49 = -36")
    if num1 == 13 and sign == '-' and num2 == 50:
        return("13-50 = -37")
    if num1 == 14 and sign == '-' and num2 == 0:
        return("14-0 = 14")
    if num1 == 14 and sign == '-' and num2 == 1:
        return("14-1 = 13")
    if num1 == 14 and sign == '-' and num2 == 2:
        return("14-2 = 12")
    if num1 == 14 and sign == '-' and num2 == 3:
        return("14-3 = 11")
    if num1 == 14 and sign == '-' and num2 == 4:
        return("14-4 = 10")
    if num1 == 14 and sign == '-' and num2 == 5:
        return("14-5 = 9")
    if num1 == 14 and sign == '-' and num2 == 6:
        return("14-6 = 8")
    if num1 == 14 and sign == '-' and num2 == 7:
        return("14-7 = 7")
    if num1 == 14 and sign == '-' and num2 == 8:
        return("14-8 = 6")
    if num1 == 14 and sign == '-' and num2 == 9:
        return("14-9 = 5")
    if num1 == 14 and sign == '-' and num2 == 10:
        return("14-10 = 4")
    if num1 == 14 and sign == '-' and num2 == 11:
        return("14-11 = 3")
    if num1 == 14 and sign == '-' and num2 == 12:
        return("14-12 = 2")
    if num1 == 14 and sign == '-' and num2 == 13:
        return("14-13 = 1")
    if num1 == 14 and sign == '-' and num2 == 14:
        return("14-14 = 0")
    if num1 == 14 and sign == '-' and num2 == 15:
        return("14-15 = -1")
    if num1 == 14 and sign == '-' and num2 == 16:
        return("14-16 = -2")
    if num1 == 14 and sign == '-' and num2 == 17:
        return("14-17 = -3")
    if num1 == 14 and sign == '-' and num2 == 18:
        return("14-18 = -4")
    if num1 == 14 and sign == '-' and num2 == 19:
        return("14-19 = -5")
    if num1 == 14 and sign == '-' and num2 == 20:
        return("14-20 = -6")
    if num1 == 14 and sign == '-' and num2 == 21:
        return("14-21 = -7")
    if num1 == 14 and sign == '-' and num2 == 22:
        return("14-22 = -8")
    if num1 == 14 and sign == '-' and num2 == 23:
        return("14-23 = -9")
    if num1 == 14 and sign == '-' and num2 == 24:
        return("14-24 = -10")
    if num1 == 14 and sign == '-' and num2 == 25:
        return("14-25 = -11")
    if num1 == 14 and sign == '-' and num2 == 26:
        return("14-26 = -12")
    if num1 == 14 and sign == '-' and num2 == 27:
        return("14-27 = -13")
    if num1 == 14 and sign == '-' and num2 == 28:
        return("14-28 = -14")
    if num1 == 14 and sign == '-' and num2 == 29:
        return("14-29 = -15")
    if num1 == 14 and sign == '-' and num2 == 30:
        return("14-30 = -16")
    if num1 == 14 and sign == '-' and num2 == 31:
        return("14-31 = -17")
    if num1 == 14 and sign == '-' and num2 == 32:
        return("14-32 = -18")
    if num1 == 14 and sign == '-' and num2 == 33:
        return("14-33 = -19")
    if num1 == 14 and sign == '-' and num2 == 34:
        return("14-34 = -20")
    if num1 == 14 and sign == '-' and num2 == 35:
        return("14-35 = -21")
    if num1 == 14 and sign == '-' and num2 == 36:
        return("14-36 = -22")
    if num1 == 14 and sign == '-' and num2 == 37:
        return("14-37 = -23")
    if num1 == 14 and sign == '-' and num2 == 38:
        return("14-38 = -24")
    if num1 == 14 and sign == '-' and num2 == 39:
        return("14-39 = -25")
    if num1 == 14 and sign == '-' and num2 == 40:
        return("14-40 = -26")
    if num1 == 14 and sign == '-' and num2 == 41:
        return("14-41 = -27")
    if num1 == 14 and sign == '-' and num2 == 42:
        return("14-42 = -28")
    if num1 == 14 and sign == '-' and num2 == 43:
        return("14-43 = -29")
    if num1 == 14 and sign == '-' and num2 == 44:
        return("14-44 = -30")
    if num1 == 14 and sign == '-' and num2 == 45:
        return("14-45 = -31")
    if num1 == 14 and sign == '-' and num2 == 46:
        return("14-46 = -32")
    if num1 == 14 and sign == '-' and num2 == 47:
        return("14-47 = -33")
    if num1 == 14 and sign == '-' and num2 == 48:
        return("14-48 = -34")
    if num1 == 14 and sign == '-' and num2 == 49:
        return("14-49 = -35")
    if num1 == 14 and sign == '-' and num2 == 50:
        return("14-50 = -36")
    if num1 == 15 and sign == '-' and num2 == 0:
        return("15-0 = 15")
    if num1 == 15 and sign == '-' and num2 == 1:
        return("15-1 = 14")
    if num1 == 15 and sign == '-' and num2 == 2:
        return("15-2 = 13")
    if num1 == 15 and sign == '-' and num2 == 3:
        return("15-3 = 12")
    if num1 == 15 and sign == '-' and num2 == 4:
        return("15-4 = 11")
    if num1 == 15 and sign == '-' and num2 == 5:
        return("15-5 = 10")
    if num1 == 15 and sign == '-' and num2 == 6:
        return("15-6 = 9")
    if num1 == 15 and sign == '-' and num2 == 7:
        return("15-7 = 8")
    if num1 == 15 and sign == '-' and num2 == 8:
        return("15-8 = 7")
    if num1 == 15 and sign == '-' and num2 == 9:
        return("15-9 = 6")
    if num1 == 15 and sign == '-' and num2 == 10:
        return("15-10 = 5")
    if num1 == 15 and sign == '-' and num2 == 11:
        return("15-11 = 4")
    if num1 == 15 and sign == '-' and num2 == 12:
        return("15-12 = 3")
    if num1 == 15 and sign == '-' and num2 == 13:
        return("15-13 = 2")
    if num1 == 15 and sign == '-' and num2 == 14:
        return("15-14 = 1")
    if num1 == 15 and sign == '-' and num2 == 15:
        return("15-15 = 0")
    if num1 == 15 and sign == '-' and num2 == 16:
        return("15-16 = -1")
    if num1 == 15 and sign == '-' and num2 == 17:
        return("15-17 = -2")
    if num1 == 15 and sign == '-' and num2 == 18:
        return("15-18 = -3")
    if num1 == 15 and sign == '-' and num2 == 19:
        return("15-19 = -4")
    if num1 == 15 and sign == '-' and num2 == 20:
        return("15-20 = -5")
    if num1 == 15 and sign == '-' and num2 == 21:
        return("15-21 = -6")
    if num1 == 15 and sign == '-' and num2 == 22:
        return("15-22 = -7")
    if num1 == 15 and sign == '-' and num2 == 23:
        return("15-23 = -8")
    if num1 == 15 and sign == '-' and num2 == 24:
        return("15-24 = -9")
    if num1 == 15 and sign == '-' and num2 == 25:
        return("15-25 = -10")
    if num1 == 15 and sign == '-' and num2 == 26:
        return("15-26 = -11")
    if num1 == 15 and sign == '-' and num2 == 27:
        return("15-27 = -12")
    if num1 == 15 and sign == '-' and num2 == 28:
        return("15-28 = -13")
    if num1 == 15 and sign == '-' and num2 == 29:
        return("15-29 = -14")
    if num1 == 15 and sign == '-' and num2 == 30:
        return("15-30 = -15")
    if num1 == 15 and sign == '-' and num2 == 31:
        return("15-31 = -16")
    if num1 == 15 and sign == '-' and num2 == 32:
        return("15-32 = -17")
    if num1 == 15 and sign == '-' and num2 == 33:
        return("15-33 = -18")
    if num1 == 15 and sign == '-' and num2 == 34:
        return("15-34 = -19")
    if num1 == 15 and sign == '-' and num2 == 35:
        return("15-35 = -20")
    if num1 == 15 and sign == '-' and num2 == 36:
        return("15-36 = -21")
    if num1 == 15 and sign == '-' and num2 == 37:
        return("15-37 = -22")
    if num1 == 15 and sign == '-' and num2 == 38:
        return("15-38 = -23")
    if num1 == 15 and sign == '-' and num2 == 39:
        return("15-39 = -24")
    if num1 == 15 and sign == '-' and num2 == 40:
        return("15-40 = -25")
    if num1 == 15 and sign == '-' and num2 == 41:
        return("15-41 = -26")
    if num1 == 15 and sign == '-' and num2 == 42:
        return("15-42 = -27")
    if num1 == 15 and sign == '-' and num2 == 43:
        return("15-43 = -28")
    if num1 == 15 and sign == '-' and num2 == 44:
        return("15-44 = -29")
    if num1 == 15 and sign == '-' and num2 == 45:
        return("15-45 = -30")
    if num1 == 15 and sign == '-' and num2 == 46:
        return("15-46 = -31")
    if num1 == 15 and sign == '-' and num2 == 47:
        return("15-47 = -32")
    if num1 == 15 and sign == '-' and num2 == 48:
        return("15-48 = -33")
    if num1 == 15 and sign == '-' and num2 == 49:
        return("15-49 = -34")
    if num1 == 15 and sign == '-' and num2 == 50:
        return("15-50 = -35")
    if num1 == 16 and sign == '-' and num2 == 0:
        return("16-0 = 16")
    if num1 == 16 and sign == '-' and num2 == 1:
        return("16-1 = 15")
    if num1 == 16 and sign == '-' and num2 == 2:
        return("16-2 = 14")
    if num1 == 16 and sign == '-' and num2 == 3:
        return("16-3 = 13")
    if num1 == 16 and sign == '-' and num2 == 4:
        return("16-4 = 12")
    if num1 == 16 and sign == '-' and num2 == 5:
        return("16-5 = 11")
    if num1 == 16 and sign == '-' and num2 == 6:
        return("16-6 = 10")
    if num1 == 16 and sign == '-' and num2 == 7:
        return("16-7 = 9")
    if num1 == 16 and sign == '-' and num2 == 8:
        return("16-8 = 8")
    if num1 == 16 and sign == '-' and num2 == 9:
        return("16-9 = 7")
    if num1 == 16 and sign == '-' and num2 == 10:
        return("16-10 = 6")
    if num1 == 16 and sign == '-' and num2 == 11:
        return("16-11 = 5")
    if num1 == 16 and sign == '-' and num2 == 12:
        return("16-12 = 4")
    if num1 == 16 and sign == '-' and num2 == 13:
        return("16-13 = 3")
    if num1 == 16 and sign == '-' and num2 == 14:
        return("16-14 = 2")
    if num1 == 16 and sign == '-' and num2 == 15:
        return("16-15 = 1")
    if num1 == 16 and sign == '-' and num2 == 16:
        return("16-16 = 0")
    if num1 == 16 and sign == '-' and num2 == 17:
        return("16-17 = -1")
    if num1 == 16 and sign == '-' and num2 == 18:
        return("16-18 = -2")
    if num1 == 16 and sign == '-' and num2 == 19:
        return("16-19 = -3")
    if num1 == 16 and sign == '-' and num2 == 20:
        return("16-20 = -4")
    if num1 == 16 and sign == '-' and num2 == 21:
        return("16-21 = -5")
    if num1 == 16 and sign == '-' and num2 == 22:
        return("16-22 = -6")
    if num1 == 16 and sign == '-' and num2 == 23:
        return("16-23 = -7")
    if num1 == 16 and sign == '-' and num2 == 24:
        return("16-24 = -8")
    if num1 == 16 and sign == '-' and num2 == 25:
        return("16-25 = -9")
    if num1 == 16 and sign == '-' and num2 == 26:
        return("16-26 = -10")
    if num1 == 16 and sign == '-' and num2 == 27:
        return("16-27 = -11")
    if num1 == 16 and sign == '-' and num2 == 28:
        return("16-28 = -12")
    if num1 == 16 and sign == '-' and num2 == 29:
        return("16-29 = -13")
    if num1 == 16 and sign == '-' and num2 == 30:
        return("16-30 = -14")
    if num1 == 16 and sign == '-' and num2 == 31:
        return("16-31 = -15")
    if num1 == 16 and sign == '-' and num2 == 32:
        return("16-32 = -16")
    if num1 == 16 and sign == '-' and num2 == 33:
        return("16-33 = -17")
    if num1 == 16 and sign == '-' and num2 == 34:
        return("16-34 = -18")
    if num1 == 16 and sign == '-' and num2 == 35:
        return("16-35 = -19")
    if num1 == 16 and sign == '-' and num2 == 36:
        return("16-36 = -20")
    if num1 == 16 and sign == '-' and num2 == 37:
        return("16-37 = -21")
    if num1 == 16 and sign == '-' and num2 == 38:
        return("16-38 = -22")
    if num1 == 16 and sign == '-' and num2 == 39:
        return("16-39 = -23")
    if num1 == 16 and sign == '-' and num2 == 40:
        return("16-40 = -24")
    if num1 == 16 and sign == '-' and num2 == 41:
        return("16-41 = -25")
    if num1 == 16 and sign == '-' and num2 == 42:
        return("16-42 = -26")
    if num1 == 16 and sign == '-' and num2 == 43:
        return("16-43 = -27")
    if num1 == 16 and sign == '-' and num2 == 44:
        return("16-44 = -28")
    if num1 == 16 and sign == '-' and num2 == 45:
        return("16-45 = -29")
    if num1 == 16 and sign == '-' and num2 == 46:
        return("16-46 = -30")
    if num1 == 16 and sign == '-' and num2 == 47:
        return("16-47 = -31")
    if num1 == 16 and sign == '-' and num2 == 48:
        return("16-48 = -32")
    if num1 == 16 and sign == '-' and num2 == 49:
        return("16-49 = -33")
    if num1 == 16 and sign == '-' and num2 == 50:
        return("16-50 = -34")
    if num1 == 17 and sign == '-' and num2 == 0:
        return("17-0 = 17")
    if num1 == 17 and sign == '-' and num2 == 1:
        return("17-1 = 16")
    if num1 == 17 and sign == '-' and num2 == 2:
        return("17-2 = 15")
    if num1 == 17 and sign == '-' and num2 == 3:
        return("17-3 = 14")
    if num1 == 17 and sign == '-' and num2 == 4:
        return("17-4 = 13")
    if num1 == 17 and sign == '-' and num2 == 5:
        return("17-5 = 12")
    if num1 == 17 and sign == '-' and num2 == 6:
        return("17-6 = 11")
    if num1 == 17 and sign == '-' and num2 == 7:
        return("17-7 = 10")
    if num1 == 17 and sign == '-' and num2 == 8:
        return("17-8 = 9")
    if num1 == 17 and sign == '-' and num2 == 9:
        return("17-9 = 8")
    if num1 == 17 and sign == '-' and num2 == 10:
        return("17-10 = 7")
    if num1 == 17 and sign == '-' and num2 == 11:
        return("17-11 = 6")
    if num1 == 17 and sign == '-' and num2 == 12:
        return("17-12 = 5")
    if num1 == 17 and sign == '-' and num2 == 13:
        return("17-13 = 4")
    if num1 == 17 and sign == '-' and num2 == 14:
        return("17-14 = 3")
    if num1 == 17 and sign == '-' and num2 == 15:
        return("17-15 = 2")
    if num1 == 17 and sign == '-' and num2 == 16:
        return("17-16 = 1")
    if num1 == 17 and sign == '-' and num2 == 17:
        return("17-17 = 0")
    if num1 == 17 and sign == '-' and num2 == 18:
        return("17-18 = -1")
    if num1 == 17 and sign == '-' and num2 == 19:
        return("17-19 = -2")
    if num1 == 17 and sign == '-' and num2 == 20:
        return("17-20 = -3")
    if num1 == 17 and sign == '-' and num2 == 21:
        return("17-21 = -4")
    if num1 == 17 and sign == '-' and num2 == 22:
        return("17-22 = -5")
    if num1 == 17 and sign == '-' and num2 == 23:
        return("17-23 = -6")
    if num1 == 17 and sign == '-' and num2 == 24:
        return("17-24 = -7")
    if num1 == 17 and sign == '-' and num2 == 25:
        return("17-25 = -8")
    if num1 == 17 and sign == '-' and num2 == 26:
        return("17-26 = -9")
    if num1 == 17 and sign == '-' and num2 == 27:
        return("17-27 = -10")
    if num1 == 17 and sign == '-' and num2 == 28:
        return("17-28 = -11")
    if num1 == 17 and sign == '-' and num2 == 29:
        return("17-29 = -12")
    if num1 == 17 and sign == '-' and num2 == 30:
        return("17-30 = -13")
    if num1 == 17 and sign == '-' and num2 == 31:
        return("17-31 = -14")
    if num1 == 17 and sign == '-' and num2 == 32:
        return("17-32 = -15")
    if num1 == 17 and sign == '-' and num2 == 33:
        return("17-33 = -16")
    if num1 == 17 and sign == '-' and num2 == 34:
        return("17-34 = -17")
    if num1 == 17 and sign == '-' and num2 == 35:
        return("17-35 = -18")
    if num1 == 17 and sign == '-' and num2 == 36:
        return("17-36 = -19")
    if num1 == 17 and sign == '-' and num2 == 37:
        return("17-37 = -20")
    if num1 == 17 and sign == '-' and num2 == 38:
        return("17-38 = -21")
    if num1 == 17 and sign == '-' and num2 == 39:
        return("17-39 = -22")
    if num1 == 17 and sign == '-' and num2 == 40:
        return("17-40 = -23")
    if num1 == 17 and sign == '-' and num2 == 41:
        return("17-41 = -24")
    if num1 == 17 and sign == '-' and num2 == 42:
        return("17-42 = -25")
    if num1 == 17 and sign == '-' and num2 == 43:
        return("17-43 = -26")
    if num1 == 17 and sign == '-' and num2 == 44:
        return("17-44 = -27")
    if num1 == 17 and sign == '-' and num2 == 45:
        return("17-45 = -28")
    if num1 == 17 and sign == '-' and num2 == 46:
        return("17-46 = -29")
    if num1 == 17 and sign == '-' and num2 == 47:
        return("17-47 = -30")
    if num1 == 17 and sign == '-' and num2 == 48:
        return("17-48 = -31")
    if num1 == 17 and sign == '-' and num2 == 49:
        return("17-49 = -32")
    if num1 == 17 and sign == '-' and num2 == 50:
        return("17-50 = -33")
    if num1 == 18 and sign == '-' and num2 == 0:
        return("18-0 = 18")
    if num1 == 18 and sign == '-' and num2 == 1:
        return("18-1 = 17")
    if num1 == 18 and sign == '-' and num2 == 2:
        return("18-2 = 16")
    if num1 == 18 and sign == '-' and num2 == 3:
        return("18-3 = 15")
    if num1 == 18 and sign == '-' and num2 == 4:
        return("18-4 = 14")
    if num1 == 18 and sign == '-' and num2 == 5:
        return("18-5 = 13")
    if num1 == 18 and sign == '-' and num2 == 6:
        return("18-6 = 12")
    if num1 == 18 and sign == '-' and num2 == 7:
        return("18-7 = 11")
    if num1 == 18 and sign == '-' and num2 == 8:
        return("18-8 = 10")
    if num1 == 18 and sign == '-' and num2 == 9:
        return("18-9 = 9")
    if num1 == 18 and sign == '-' and num2 == 10:
        return("18-10 = 8")
    if num1 == 18 and sign == '-' and num2 == 11:
        return("18-11 = 7")
    if num1 == 18 and sign == '-' and num2 == 12:
        return("18-12 = 6")
    if num1 == 18 and sign == '-' and num2 == 13:
        return("18-13 = 5")
    if num1 == 18 and sign == '-' and num2 == 14:
        return("18-14 = 4")
    if num1 == 18 and sign == '-' and num2 == 15:
        return("18-15 = 3")
    if num1 == 18 and sign == '-' and num2 == 16:
        return("18-16 = 2")
    if num1 == 18 and sign == '-' and num2 == 17:
        return("18-17 = 1")
    if num1 == 18 and sign == '-' and num2 == 18:
        return("18-18 = 0")
    if num1 == 18 and sign == '-' and num2 == 19:
        return("18-19 = -1")
    if num1 == 18 and sign == '-' and num2 == 20:
        return("18-20 = -2")
    if num1 == 18 and sign == '-' and num2 == 21:
        return("18-21 = -3")
    if num1 == 18 and sign == '-' and num2 == 22:
        return("18-22 = -4")
    if num1 == 18 and sign == '-' and num2 == 23:
        return("18-23 = -5")
    if num1 == 18 and sign == '-' and num2 == 24:
        return("18-24 = -6")
    if num1 == 18 and sign == '-' and num2 == 25:
        return("18-25 = -7")
    if num1 == 18 and sign == '-' and num2 == 26:
        return("18-26 = -8")
    if num1 == 18 and sign == '-' and num2 == 27:
        return("18-27 = -9")
    if num1 == 18 and sign == '-' and num2 == 28:
        return("18-28 = -10")
    if num1 == 18 and sign == '-' and num2 == 29:
        return("18-29 = -11")
    if num1 == 18 and sign == '-' and num2 == 30:
        return("18-30 = -12")
    if num1 == 18 and sign == '-' and num2 == 31:
        return("18-31 = -13")
    if num1 == 18 and sign == '-' and num2 == 32:
        return("18-32 = -14")
    if num1 == 18 and sign == '-' and num2 == 33:
        return("18-33 = -15")
    if num1 == 18 and sign == '-' and num2 == 34:
        return("18-34 = -16")
    if num1 == 18 and sign == '-' and num2 == 35:
        return("18-35 = -17")
    if num1 == 18 and sign == '-' and num2 == 36:
        return("18-36 = -18")
    if num1 == 18 and sign == '-' and num2 == 37:
        return("18-37 = -19")
    if num1 == 18 and sign == '-' and num2 == 38:
        return("18-38 = -20")
    if num1 == 18 and sign == '-' and num2 == 39:
        return("18-39 = -21")
    if num1 == 18 and sign == '-' and num2 == 40:
        return("18-40 = -22")
    if num1 == 18 and sign == '-' and num2 == 41:
        return("18-41 = -23")
    if num1 == 18 and sign == '-' and num2 == 42:
        return("18-42 = -24")
    if num1 == 18 and sign == '-' and num2 == 43:
        return("18-43 = -25")
    if num1 == 18 and sign == '-' and num2 == 44:
        return("18-44 = -26")
    if num1 == 18 and sign == '-' and num2 == 45:
        return("18-45 = -27")
    if num1 == 18 and sign == '-' and num2 == 46:
        return("18-46 = -28")
    if num1 == 18 and sign == '-' and num2 == 47:
        return("18-47 = -29")
    if num1 == 18 and sign == '-' and num2 == 48:
        return("18-48 = -30")
    if num1 == 18 and sign == '-' and num2 == 49:
        return("18-49 = -31")
    if num1 == 18 and sign == '-' and num2 == 50:
        return("18-50 = -32")
    if num1 == 19 and sign == '-' and num2 == 0:
        return("19-0 = 19")
    if num1 == 19 and sign == '-' and num2 == 1:
        return("19-1 = 18")
    if num1 == 19 and sign == '-' and num2 == 2:
        return("19-2 = 17")
    if num1 == 19 and sign == '-' and num2 == 3:
        return("19-3 = 16")
    if num1 == 19 and sign == '-' and num2 == 4:
        return("19-4 = 15")
    if num1 == 19 and sign == '-' and num2 == 5:
        return("19-5 = 14")
    if num1 == 19 and sign == '-' and num2 == 6:
        return("19-6 = 13")
    if num1 == 19 and sign == '-' and num2 == 7:
        return("19-7 = 12")
    if num1 == 19 and sign == '-' and num2 == 8:
        return("19-8 = 11")
    if num1 == 19 and sign == '-' and num2 == 9:
        return("19-9 = 10")
    if num1 == 19 and sign == '-' and num2 == 10:
        return("19-10 = 9")
    if num1 == 19 and sign == '-' and num2 == 11:
        return("19-11 = 8")
    if num1 == 19 and sign == '-' and num2 == 12:
        return("19-12 = 7")
    if num1 == 19 and sign == '-' and num2 == 13:
        return("19-13 = 6")
    if num1 == 19 and sign == '-' and num2 == 14:
        return("19-14 = 5")
    if num1 == 19 and sign == '-' and num2 == 15:
        return("19-15 = 4")
    if num1 == 19 and sign == '-' and num2 == 16:
        return("19-16 = 3")
    if num1 == 19 and sign == '-' and num2 == 17:
        return("19-17 = 2")
    if num1 == 19 and sign == '-' and num2 == 18:
        return("19-18 = 1")
    if num1 == 19 and sign == '-' and num2 == 19:
        return("19-19 = 0")
    if num1 == 19 and sign == '-' and num2 == 20:
        return("19-20 = -1")
    if num1 == 19 and sign == '-' and num2 == 21:
        return("19-21 = -2")
    if num1 == 19 and sign == '-' and num2 == 22:
        return("19-22 = -3")
    if num1 == 19 and sign == '-' and num2 == 23:
        return("19-23 = -4")
    if num1 == 19 and sign == '-' and num2 == 24:
        return("19-24 = -5")
    if num1 == 19 and sign == '-' and num2 == 25:
        return("19-25 = -6")
    if num1 == 19 and sign == '-' and num2 == 26:
        return("19-26 = -7")
    if num1 == 19 and sign == '-' and num2 == 27:
        return("19-27 = -8")
    if num1 == 19 and sign == '-' and num2 == 28:
        return("19-28 = -9")
    if num1 == 19 and sign == '-' and num2 == 29:
        return("19-29 = -10")
    if num1 == 19 and sign == '-' and num2 == 30:
        return("19-30 = -11")
    if num1 == 19 and sign == '-' and num2 == 31:
        return("19-31 = -12")
    if num1 == 19 and sign == '-' and num2 == 32:
        return("19-32 = -13")
    if num1 == 19 and sign == '-' and num2 == 33:
        return("19-33 = -14")
    if num1 == 19 and sign == '-' and num2 == 34:
        return("19-34 = -15")
    if num1 == 19 and sign == '-' and num2 == 35:
        return("19-35 = -16")
    if num1 == 19 and sign == '-' and num2 == 36:
        return("19-36 = -17")
    if num1 == 19 and sign == '-' and num2 == 37:
        return("19-37 = -18")
    if num1 == 19 and sign == '-' and num2 == 38:
        return("19-38 = -19")
    if num1 == 19 and sign == '-' and num2 == 39:
        return("19-39 = -20")
    if num1 == 19 and sign == '-' and num2 == 40:
        return("19-40 = -21")
    if num1 == 19 and sign == '-' and num2 == 41:
        return("19-41 = -22")
    if num1 == 19 and sign == '-' and num2 == 42:
        return("19-42 = -23")
    if num1 == 19 and sign == '-' and num2 == 43:
        return("19-43 = -24")
    if num1 == 19 and sign == '-' and num2 == 44:
        return("19-44 = -25")
    if num1 == 19 and sign == '-' and num2 == 45:
        return("19-45 = -26")
    if num1 == 19 and sign == '-' and num2 == 46:
        return("19-46 = -27")
    if num1 == 19 and sign == '-' and num2 == 47:
        return("19-47 = -28")
    if num1 == 19 and sign == '-' and num2 == 48:
        return("19-48 = -29")
    if num1 == 19 and sign == '-' and num2 == 49:
        return("19-49 = -30")
    if num1 == 19 and sign == '-' and num2 == 50:
        return("19-50 = -31")
    if num1 == 20 and sign == '-' and num2 == 0:
        return("20-0 = 20")
    if num1 == 20 and sign == '-' and num2 == 1:
        return("20-1 = 19")
    if num1 == 20 and sign == '-' and num2 == 2:
        return("20-2 = 18")
    if num1 == 20 and sign == '-' and num2 == 3:
        return("20-3 = 17")
    if num1 == 20 and sign == '-' and num2 == 4:
        return("20-4 = 16")
    if num1 == 20 and sign == '-' and num2 == 5:
        return("20-5 = 15")
    if num1 == 20 and sign == '-' and num2 == 6:
        return("20-6 = 14")
    if num1 == 20 and sign == '-' and num2 == 7:
        return("20-7 = 13")
    if num1 == 20 and sign == '-' and num2 == 8:
        return("20-8 = 12")
    if num1 == 20 and sign == '-' and num2 == 9:
        return("20-9 = 11")
    if num1 == 20 and sign == '-' and num2 == 10:
        return("20-10 = 10")
    if num1 == 20 and sign == '-' and num2 == 11:
        return("20-11 = 9")
    if num1 == 20 and sign == '-' and num2 == 12:
        return("20-12 = 8")
    if num1 == 20 and sign == '-' and num2 == 13:
        return("20-13 = 7")
    if num1 == 20 and sign == '-' and num2 == 14:
        return("20-14 = 6")
    if num1 == 20 and sign == '-' and num2 == 15:
        return("20-15 = 5")
    if num1 == 20 and sign == '-' and num2 == 16:
        return("20-16 = 4")
    if num1 == 20 and sign == '-' and num2 == 17:
        return("20-17 = 3")
    if num1 == 20 and sign == '-' and num2 == 18:
        return("20-18 = 2")
    if num1 == 20 and sign == '-' and num2 == 19:
        return("20-19 = 1")
    if num1 == 20 and sign == '-' and num2 == 20:
        return("20-20 = 0")
    if num1 == 20 and sign == '-' and num2 == 21:
        return("20-21 = -1")
    if num1 == 20 and sign == '-' and num2 == 22:
        return("20-22 = -2")
    if num1 == 20 and sign == '-' and num2 == 23:
        return("20-23 = -3")
    if num1 == 20 and sign == '-' and num2 == 24:
        return("20-24 = -4")
    if num1 == 20 and sign == '-' and num2 == 25:
        return("20-25 = -5")
    if num1 == 20 and sign == '-' and num2 == 26:
        return("20-26 = -6")
    if num1 == 20 and sign == '-' and num2 == 27:
        return("20-27 = -7")
    if num1 == 20 and sign == '-' and num2 == 28:
        return("20-28 = -8")
    if num1 == 20 and sign == '-' and num2 == 29:
        return("20-29 = -9")
    if num1 == 20 and sign == '-' and num2 == 30:
        return("20-30 = -10")
    if num1 == 20 and sign == '-' and num2 == 31:
        return("20-31 = -11")
    if num1 == 20 and sign == '-' and num2 == 32:
        return("20-32 = -12")
    if num1 == 20 and sign == '-' and num2 == 33:
        return("20-33 = -13")
    if num1 == 20 and sign == '-' and num2 == 34:
        return("20-34 = -14")
    if num1 == 20 and sign == '-' and num2 == 35:
        return("20-35 = -15")
    if num1 == 20 and sign == '-' and num2 == 36:
        return("20-36 = -16")
    if num1 == 20 and sign == '-' and num2 == 37:
        return("20-37 = -17")
    if num1 == 20 and sign == '-' and num2 == 38:
        return("20-38 = -18")
    if num1 == 20 and sign == '-' and num2 == 39:
        return("20-39 = -19")
    if num1 == 20 and sign == '-' and num2 == 40:
        return("20-40 = -20")
    if num1 == 20 and sign == '-' and num2 == 41:
        return("20-41 = -21")
    if num1 == 20 and sign == '-' and num2 == 42:
        return("20-42 = -22")
    if num1 == 20 and sign == '-' and num2 == 43:
        return("20-43 = -23")
    if num1 == 20 and sign == '-' and num2 == 44:
        return("20-44 = -24")
    if num1 == 20 and sign == '-' and num2 == 45:
        return("20-45 = -25")
    if num1 == 20 and sign == '-' and num2 == 46:
        return("20-46 = -26")
    if num1 == 20 and sign == '-' and num2 == 47:
        return("20-47 = -27")
    if num1 == 20 and sign == '-' and num2 == 48:
        return("20-48 = -28")
    if num1 == 20 and sign == '-' and num2 == 49:
        return("20-49 = -29")
    if num1 == 20 and sign == '-' and num2 == 50:
        return("20-50 = -30")
    if num1 == 21 and sign == '-' and num2 == 0:
        return("21-0 = 21")
    if num1 == 21 and sign == '-' and num2 == 1:
        return("21-1 = 20")
    if num1 == 21 and sign == '-' and num2 == 2:
        return("21-2 = 19")
    if num1 == 21 and sign == '-' and num2 == 3:
        return("21-3 = 18")
    if num1 == 21 and sign == '-' and num2 == 4:
        return("21-4 = 17")
    if num1 == 21 and sign == '-' and num2 == 5:
        return("21-5 = 16")
    if num1 == 21 and sign == '-' and num2 == 6:
        return("21-6 = 15")
    if num1 == 21 and sign == '-' and num2 == 7:
        return("21-7 = 14")
    if num1 == 21 and sign == '-' and num2 == 8:
        return("21-8 = 13")
    if num1 == 21 and sign == '-' and num2 == 9:
        return("21-9 = 12")
    if num1 == 21 and sign == '-' and num2 == 10:
        return("21-10 = 11")
    if num1 == 21 and sign == '-' and num2 == 11:
        return("21-11 = 10")
    if num1 == 21 and sign == '-' and num2 == 12:
        return("21-12 = 9")
    if num1 == 21 and sign == '-' and num2 == 13:
        return("21-13 = 8")
    if num1 == 21 and sign == '-' and num2 == 14:
        return("21-14 = 7")
    if num1 == 21 and sign == '-' and num2 == 15:
        return("21-15 = 6")
    if num1 == 21 and sign == '-' and num2 == 16:
        return("21-16 = 5")
    if num1 == 21 and sign == '-' and num2 == 17:
        return("21-17 = 4")
    if num1 == 21 and sign == '-' and num2 == 18:
        return("21-18 = 3")
    if num1 == 21 and sign == '-' and num2 == 19:
        return("21-19 = 2")
    if num1 == 21 and sign == '-' and num2 == 20:
        return("21-20 = 1")
    if num1 == 21 and sign == '-' and num2 == 21:
        return("21-21 = 0")
    if num1 == 21 and sign == '-' and num2 == 22:
        return("21-22 = -1")
    if num1 == 21 and sign == '-' and num2 == 23:
        return("21-23 = -2")
    if num1 == 21 and sign == '-' and num2 == 24:
        return("21-24 = -3")
    if num1 == 21 and sign == '-' and num2 == 25:
        return("21-25 = -4")
    if num1 == 21 and sign == '-' and num2 == 26:
        return("21-26 = -5")
    if num1 == 21 and sign == '-' and num2 == 27:
        return("21-27 = -6")
    if num1 == 21 and sign == '-' and num2 == 28:
        return("21-28 = -7")
    if num1 == 21 and sign == '-' and num2 == 29:
        return("21-29 = -8")
    if num1 == 21 and sign == '-' and num2 == 30:
        return("21-30 = -9")
    if num1 == 21 and sign == '-' and num2 == 31:
        return("21-31 = -10")
    if num1 == 21 and sign == '-' and num2 == 32:
        return("21-32 = -11")
    if num1 == 21 and sign == '-' and num2 == 33:
        return("21-33 = -12")
    if num1 == 21 and sign == '-' and num2 == 34:
        return("21-34 = -13")
    if num1 == 21 and sign == '-' and num2 == 35:
        return("21-35 = -14")
    if num1 == 21 and sign == '-' and num2 == 36:
        return("21-36 = -15")
    if num1 == 21 and sign == '-' and num2 == 37:
        return("21-37 = -16")
    if num1 == 21 and sign == '-' and num2 == 38:
        return("21-38 = -17")
    if num1 == 21 and sign == '-' and num2 == 39:
        return("21-39 = -18")
    if num1 == 21 and sign == '-' and num2 == 40:
        return("21-40 = -19")
    if num1 == 21 and sign == '-' and num2 == 41:
        return("21-41 = -20")
    if num1 == 21 and sign == '-' and num2 == 42:
        return("21-42 = -21")
    if num1 == 21 and sign == '-' and num2 == 43:
        return("21-43 = -22")
    if num1 == 21 and sign == '-' and num2 == 44:
        return("21-44 = -23")
    if num1 == 21 and sign == '-' and num2 == 45:
        return("21-45 = -24")
    if num1 == 21 and sign == '-' and num2 == 46:
        return("21-46 = -25")
    if num1 == 21 and sign == '-' and num2 == 47:
        return("21-47 = -26")
    if num1 == 21 and sign == '-' and num2 == 48:
        return("21-48 = -27")
    if num1 == 21 and sign == '-' and num2 == 49:
        return("21-49 = -28")
    if num1 == 21 and sign == '-' and num2 == 50:
        return("21-50 = -29")
    if num1 == 22 and sign == '-' and num2 == 0:
        return("22-0 = 22")
    if num1 == 22 and sign == '-' and num2 == 1:
        return("22-1 = 21")
    if num1 == 22 and sign == '-' and num2 == 2:
        return("22-2 = 20")
    if num1 == 22 and sign == '-' and num2 == 3:
        return("22-3 = 19")
    if num1 == 22 and sign == '-' and num2 == 4:
        return("22-4 = 18")
    if num1 == 22 and sign == '-' and num2 == 5:
        return("22-5 = 17")
    if num1 == 22 and sign == '-' and num2 == 6:
        return("22-6 = 16")
    if num1 == 22 and sign == '-' and num2 == 7:
        return("22-7 = 15")
    if num1 == 22 and sign == '-' and num2 == 8:
        return("22-8 = 14")
    if num1 == 22 and sign == '-' and num2 == 9:
        return("22-9 = 13")
    if num1 == 22 and sign == '-' and num2 == 10:
        return("22-10 = 12")
    if num1 == 22 and sign == '-' and num2 == 11:
        return("22-11 = 11")
    if num1 == 22 and sign == '-' and num2 == 12:
        return("22-12 = 10")
    if num1 == 22 and sign == '-' and num2 == 13:
        return("22-13 = 9")
    if num1 == 22 and sign == '-' and num2 == 14:
        return("22-14 = 8")
    if num1 == 22 and sign == '-' and num2 == 15:
        return("22-15 = 7")
    if num1 == 22 and sign == '-' and num2 == 16:
        return("22-16 = 6")
    if num1 == 22 and sign == '-' and num2 == 17:
        return("22-17 = 5")
    if num1 == 22 and sign == '-' and num2 == 18:
        return("22-18 = 4")
    if num1 == 22 and sign == '-' and num2 == 19:
        return("22-19 = 3")
    if num1 == 22 and sign == '-' and num2 == 20:
        return("22-20 = 2")
    if num1 == 22 and sign == '-' and num2 == 21:
        return("22-21 = 1")
    if num1 == 22 and sign == '-' and num2 == 22:
        return("22-22 = 0")
    if num1 == 22 and sign == '-' and num2 == 23:
        return("22-23 = -1")
    if num1 == 22 and sign == '-' and num2 == 24:
        return("22-24 = -2")
    if num1 == 22 and sign == '-' and num2 == 25:
        return("22-25 = -3")
    if num1 == 22 and sign == '-' and num2 == 26:
        return("22-26 = -4")
    if num1 == 22 and sign == '-' and num2 == 27:
        return("22-27 = -5")
    if num1 == 22 and sign == '-' and num2 == 28:
        return("22-28 = -6")
    if num1 == 22 and sign == '-' and num2 == 29:
        return("22-29 = -7")
    if num1 == 22 and sign == '-' and num2 == 30:
        return("22-30 = -8")
    if num1 == 22 and sign == '-' and num2 == 31:
        return("22-31 = -9")
    if num1 == 22 and sign == '-' and num2 == 32:
        return("22-32 = -10")
    if num1 == 22 and sign == '-' and num2 == 33:
        return("22-33 = -11")
    if num1 == 22 and sign == '-' and num2 == 34:
        return("22-34 = -12")
    if num1 == 22 and sign == '-' and num2 == 35:
        return("22-35 = -13")
    if num1 == 22 and sign == '-' and num2 == 36:
        return("22-36 = -14")
    if num1 == 22 and sign == '-' and num2 == 37:
        return("22-37 = -15")
    if num1 == 22 and sign == '-' and num2 == 38:
        return("22-38 = -16")
    if num1 == 22 and sign == '-' and num2 == 39:
        return("22-39 = -17")
    if num1 == 22 and sign == '-' and num2 == 40:
        return("22-40 = -18")
    if num1 == 22 and sign == '-' and num2 == 41:
        return("22-41 = -19")
    if num1 == 22 and sign == '-' and num2 == 42:
        return("22-42 = -20")
    if num1 == 22 and sign == '-' and num2 == 43:
        return("22-43 = -21")
    if num1 == 22 and sign == '-' and num2 == 44:
        return("22-44 = -22")
    if num1 == 22 and sign == '-' and num2 == 45:
        return("22-45 = -23")
    if num1 == 22 and sign == '-' and num2 == 46:
        return("22-46 = -24")
    if num1 == 22 and sign == '-' and num2 == 47:
        return("22-47 = -25")
    if num1 == 22 and sign == '-' and num2 == 48:
        return("22-48 = -26")
    if num1 == 22 and sign == '-' and num2 == 49:
        return("22-49 = -27")
    if num1 == 22 and sign == '-' and num2 == 50:
        return("22-50 = -28")
    if num1 == 23 and sign == '-' and num2 == 0:
        return("23-0 = 23")
    if num1 == 23 and sign == '-' and num2 == 1:
        return("23-1 = 22")
    if num1 == 23 and sign == '-' and num2 == 2:
        return("23-2 = 21")
    if num1 == 23 and sign == '-' and num2 == 3:
        return("23-3 = 20")
    if num1 == 23 and sign == '-' and num2 == 4:
        return("23-4 = 19")
    if num1 == 23 and sign == '-' and num2 == 5:
        return("23-5 = 18")
    if num1 == 23 and sign == '-' and num2 == 6:
        return("23-6 = 17")
    if num1 == 23 and sign == '-' and num2 == 7:
        return("23-7 = 16")
    if num1 == 23 and sign == '-' and num2 == 8:
        return("23-8 = 15")
    if num1 == 23 and sign == '-' and num2 == 9:
        return("23-9 = 14")
    if num1 == 23 and sign == '-' and num2 == 10:
        return("23-10 = 13")
    if num1 == 23 and sign == '-' and num2 == 11:
        return("23-11 = 12")
    if num1 == 23 and sign == '-' and num2 == 12:
        return("23-12 = 11")
    if num1 == 23 and sign == '-' and num2 == 13:
        return("23-13 = 10")
    if num1 == 23 and sign == '-' and num2 == 14:
        return("23-14 = 9")
    if num1 == 23 and sign == '-' and num2 == 15:
        return("23-15 = 8")
    if num1 == 23 and sign == '-' and num2 == 16:
        return("23-16 = 7")
    if num1 == 23 and sign == '-' and num2 == 17:
        return("23-17 = 6")
    if num1 == 23 and sign == '-' and num2 == 18:
        return("23-18 = 5")
    if num1 == 23 and sign == '-' and num2 == 19:
        return("23-19 = 4")
    if num1 == 23 and sign == '-' and num2 == 20:
        return("23-20 = 3")
    if num1 == 23 and sign == '-' and num2 == 21:
        return("23-21 = 2")
    if num1 == 23 and sign == '-' and num2 == 22:
        return("23-22 = 1")
    if num1 == 23 and sign == '-' and num2 == 23:
        return("23-23 = 0")
    if num1 == 23 and sign == '-' and num2 == 24:
        return("23-24 = -1")
    if num1 == 23 and sign == '-' and num2 == 25:
        return("23-25 = -2")
    if num1 == 23 and sign == '-' and num2 == 26:
        return("23-26 = -3")
    if num1 == 23 and sign == '-' and num2 == 27:
        return("23-27 = -4")
    if num1 == 23 and sign == '-' and num2 == 28:
        return("23-28 = -5")
    if num1 == 23 and sign == '-' and num2 == 29:
        return("23-29 = -6")
    if num1 == 23 and sign == '-' and num2 == 30:
        return("23-30 = -7")
    if num1 == 23 and sign == '-' and num2 == 31:
        return("23-31 = -8")
    if num1 == 23 and sign == '-' and num2 == 32:
        return("23-32 = -9")
    if num1 == 23 and sign == '-' and num2 == 33:
        return("23-33 = -10")
    if num1 == 23 and sign == '-' and num2 == 34:
        return("23-34 = -11")
    if num1 == 23 and sign == '-' and num2 == 35:
        return("23-35 = -12")
    if num1 == 23 and sign == '-' and num2 == 36:
        return("23-36 = -13")
    if num1 == 23 and sign == '-' and num2 == 37:
        return("23-37 = -14")
    if num1 == 23 and sign == '-' and num2 == 38:
        return("23-38 = -15")
    if num1 == 23 and sign == '-' and num2 == 39:
        return("23-39 = -16")
    if num1 == 23 and sign == '-' and num2 == 40:
        return("23-40 = -17")
    if num1 == 23 and sign == '-' and num2 == 41:
        return("23-41 = -18")
    if num1 == 23 and sign == '-' and num2 == 42:
        return("23-42 = -19")
    if num1 == 23 and sign == '-' and num2 == 43:
        return("23-43 = -20")
    if num1 == 23 and sign == '-' and num2 == 44:
        return("23-44 = -21")
    if num1 == 23 and sign == '-' and num2 == 45:
        return("23-45 = -22")
    if num1 == 23 and sign == '-' and num2 == 46:
        return("23-46 = -23")
    if num1 == 23 and sign == '-' and num2 == 47:
        return("23-47 = -24")
    if num1 == 23 and sign == '-' and num2 == 48:
        return("23-48 = -25")
    if num1 == 23 and sign == '-' and num2 == 49:
        return("23-49 = -26")
    if num1 == 23 and sign == '-' and num2 == 50:
        return("23-50 = -27")
    if num1 == 24 and sign == '-' and num2 == 0:
        return("24-0 = 24")
    if num1 == 24 and sign == '-' and num2 == 1:
        return("24-1 = 23")
    if num1 == 24 and sign == '-' and num2 == 2:
        return("24-2 = 22")
    if num1 == 24 and sign == '-' and num2 == 3:
        return("24-3 = 21")
    if num1 == 24 and sign == '-' and num2 == 4:
        return("24-4 = 20")
    if num1 == 24 and sign == '-' and num2 == 5:
        return("24-5 = 19")
    if num1 == 24 and sign == '-' and num2 == 6:
        return("24-6 = 18")
    if num1 == 24 and sign == '-' and num2 == 7:
        return("24-7 = 17")
    if num1 == 24 and sign == '-' and num2 == 8:
        return("24-8 = 16")
    if num1 == 24 and sign == '-' and num2 == 9:
        return("24-9 = 15")
    if num1 == 24 and sign == '-' and num2 == 10:
        return("24-10 = 14")
    if num1 == 24 and sign == '-' and num2 == 11:
        return("24-11 = 13")
    if num1 == 24 and sign == '-' and num2 == 12:
        return("24-12 = 12")
    if num1 == 24 and sign == '-' and num2 == 13:
        return("24-13 = 11")
    if num1 == 24 and sign == '-' and num2 == 14:
        return("24-14 = 10")
    if num1 == 24 and sign == '-' and num2 == 15:
        return("24-15 = 9")
    if num1 == 24 and sign == '-' and num2 == 16:
        return("24-16 = 8")
    if num1 == 24 and sign == '-' and num2 == 17:
        return("24-17 = 7")
    if num1 == 24 and sign == '-' and num2 == 18:
        return("24-18 = 6")
    if num1 == 24 and sign == '-' and num2 == 19:
        return("24-19 = 5")
    if num1 == 24 and sign == '-' and num2 == 20:
        return("24-20 = 4")
    if num1 == 24 and sign == '-' and num2 == 21:
        return("24-21 = 3")
    if num1 == 24 and sign == '-' and num2 == 22:
        return("24-22 = 2")
    if num1 == 24 and sign == '-' and num2 == 23:
        return("24-23 = 1")
    if num1 == 24 and sign == '-' and num2 == 24:
        return("24-24 = 0")
    if num1 == 24 and sign == '-' and num2 == 25:
        return("24-25 = -1")
    if num1 == 24 and sign == '-' and num2 == 26:
        return("24-26 = -2")
    if num1 == 24 and sign == '-' and num2 == 27:
        return("24-27 = -3")
    if num1 == 24 and sign == '-' and num2 == 28:
        return("24-28 = -4")
    if num1 == 24 and sign == '-' and num2 == 29:
        return("24-29 = -5")
    if num1 == 24 and sign == '-' and num2 == 30:
        return("24-30 = -6")
    if num1 == 24 and sign == '-' and num2 == 31:
        return("24-31 = -7")
    if num1 == 24 and sign == '-' and num2 == 32:
        return("24-32 = -8")
    if num1 == 24 and sign == '-' and num2 == 33:
        return("24-33 = -9")
    if num1 == 24 and sign == '-' and num2 == 34:
        return("24-34 = -10")
    if num1 == 24 and sign == '-' and num2 == 35:
        return("24-35 = -11")
    if num1 == 24 and sign == '-' and num2 == 36:
        return("24-36 = -12")
    if num1 == 24 and sign == '-' and num2 == 37:
        return("24-37 = -13")
    if num1 == 24 and sign == '-' and num2 == 38:
        return("24-38 = -14")
    if num1 == 24 and sign == '-' and num2 == 39:
        return("24-39 = -15")
    if num1 == 24 and sign == '-' and num2 == 40:
        return("24-40 = -16")
    if num1 == 24 and sign == '-' and num2 == 41:
        return("24-41 = -17")
    if num1 == 24 and sign == '-' and num2 == 42:
        return("24-42 = -18")
    if num1 == 24 and sign == '-' and num2 == 43:
        return("24-43 = -19")
    if num1 == 24 and sign == '-' and num2 == 44:
        return("24-44 = -20")
    if num1 == 24 and sign == '-' and num2 == 45:
        return("24-45 = -21")
    if num1 == 24 and sign == '-' and num2 == 46:
        return("24-46 = -22")
    if num1 == 24 and sign == '-' and num2 == 47:
        return("24-47 = -23")
    if num1 == 24 and sign == '-' and num2 == 48:
        return("24-48 = -24")
    if num1 == 24 and sign == '-' and num2 == 49:
        return("24-49 = -25")
    if num1 == 24 and sign == '-' and num2 == 50:
        return("24-50 = -26")
    if num1 == 25 and sign == '-' and num2 == 0:
        return("25-0 = 25")
    if num1 == 25 and sign == '-' and num2 == 1:
        return("25-1 = 24")
    if num1 == 25 and sign == '-' and num2 == 2:
        return("25-2 = 23")
    if num1 == 25 and sign == '-' and num2 == 3:
        return("25-3 = 22")
    if num1 == 25 and sign == '-' and num2 == 4:
        return("25-4 = 21")
    if num1 == 25 and sign == '-' and num2 == 5:
        return("25-5 = 20")
    if num1 == 25 and sign == '-' and num2 == 6:
        return("25-6 = 19")
    if num1 == 25 and sign == '-' and num2 == 7:
        return("25-7 = 18")
    if num1 == 25 and sign == '-' and num2 == 8:
        return("25-8 = 17")
    if num1 == 25 and sign == '-' and num2 == 9:
        return("25-9 = 16")
    if num1 == 25 and sign == '-' and num2 == 10:
        return("25-10 = 15")
    if num1 == 25 and sign == '-' and num2 == 11:
        return("25-11 = 14")
    if num1 == 25 and sign == '-' and num2 == 12:
        return("25-12 = 13")
    if num1 == 25 and sign == '-' and num2 == 13:
        return("25-13 = 12")
    if num1 == 25 and sign == '-' and num2 == 14:
        return("25-14 = 11")
    if num1 == 25 and sign == '-' and num2 == 15:
        return("25-15 = 10")
    if num1 == 25 and sign == '-' and num2 == 16:
        return("25-16 = 9")
    if num1 == 25 and sign == '-' and num2 == 17:
        return("25-17 = 8")
    if num1 == 25 and sign == '-' and num2 == 18:
        return("25-18 = 7")
    if num1 == 25 and sign == '-' and num2 == 19:
        return("25-19 = 6")
    if num1 == 25 and sign == '-' and num2 == 20:
        return("25-20 = 5")
    if num1 == 25 and sign == '-' and num2 == 21:
        return("25-21 = 4")
    if num1 == 25 and sign == '-' and num2 == 22:
        return("25-22 = 3")
    if num1 == 25 and sign == '-' and num2 == 23:
        return("25-23 = 2")
    if num1 == 25 and sign == '-' and num2 == 24:
        return("25-24 = 1")
    if num1 == 25 and sign == '-' and num2 == 25:
        return("25-25 = 0")
    if num1 == 25 and sign == '-' and num2 == 26:
        return("25-26 = -1")
    if num1 == 25 and sign == '-' and num2 == 27:
        return("25-27 = -2")
    if num1 == 25 and sign == '-' and num2 == 28:
        return("25-28 = -3")
    if num1 == 25 and sign == '-' and num2 == 29:
        return("25-29 = -4")
    if num1 == 25 and sign == '-' and num2 == 30:
        return("25-30 = -5")
    if num1 == 25 and sign == '-' and num2 == 31:
        return("25-31 = -6")
    if num1 == 25 and sign == '-' and num2 == 32:
        return("25-32 = -7")
    if num1 == 25 and sign == '-' and num2 == 33:
        return("25-33 = -8")
    if num1 == 25 and sign == '-' and num2 == 34:
        return("25-34 = -9")
    if num1 == 25 and sign == '-' and num2 == 35:
        return("25-35 = -10")
    if num1 == 25 and sign == '-' and num2 == 36:
        return("25-36 = -11")
    if num1 == 25 and sign == '-' and num2 == 37:
        return("25-37 = -12")
    if num1 == 25 and sign == '-' and num2 == 38:
        return("25-38 = -13")
    if num1 == 25 and sign == '-' and num2 == 39:
        return("25-39 = -14")
    if num1 == 25 and sign == '-' and num2 == 40:
        return("25-40 = -15")
    if num1 == 25 and sign == '-' and num2 == 41:
        return("25-41 = -16")
    if num1 == 25 and sign == '-' and num2 == 42:
        return("25-42 = -17")
    if num1 == 25 and sign == '-' and num2 == 43:
        return("25-43 = -18")
    if num1 == 25 and sign == '-' and num2 == 44:
        return("25-44 = -19")
    if num1 == 25 and sign == '-' and num2 == 45:
        return("25-45 = -20")
    if num1 == 25 and sign == '-' and num2 == 46:
        return("25-46 = -21")
    if num1 == 25 and sign == '-' and num2 == 47:
        return("25-47 = -22")
    if num1 == 25 and sign == '-' and num2 == 48:
        return("25-48 = -23")
    if num1 == 25 and sign == '-' and num2 == 49:
        return("25-49 = -24")
    if num1 == 25 and sign == '-' and num2 == 50:
        return("25-50 = -25")
    if num1 == 26 and sign == '-' and num2 == 0:
        return("26-0 = 26")
    if num1 == 26 and sign == '-' and num2 == 1:
        return("26-1 = 25")
    if num1 == 26 and sign == '-' and num2 == 2:
        return("26-2 = 24")
    if num1 == 26 and sign == '-' and num2 == 3:
        return("26-3 = 23")
    if num1 == 26 and sign == '-' and num2 == 4:
        return("26-4 = 22")
    if num1 == 26 and sign == '-' and num2 == 5:
        return("26-5 = 21")
    if num1 == 26 and sign == '-' and num2 == 6:
        return("26-6 = 20")
    if num1 == 26 and sign == '-' and num2 == 7:
        return("26-7 = 19")
    if num1 == 26 and sign == '-' and num2 == 8:
        return("26-8 = 18")
    if num1 == 26 and sign == '-' and num2 == 9:
        return("26-9 = 17")
    if num1 == 26 and sign == '-' and num2 == 10:
        return("26-10 = 16")
    if num1 == 26 and sign == '-' and num2 == 11:
        return("26-11 = 15")
    if num1 == 26 and sign == '-' and num2 == 12:
        return("26-12 = 14")
    if num1 == 26 and sign == '-' and num2 == 13:
        return("26-13 = 13")
    if num1 == 26 and sign == '-' and num2 == 14:
        return("26-14 = 12")
    if num1 == 26 and sign == '-' and num2 == 15:
        return("26-15 = 11")
    if num1 == 26 and sign == '-' and num2 == 16:
        return("26-16 = 10")
    if num1 == 26 and sign == '-' and num2 == 17:
        return("26-17 = 9")
    if num1 == 26 and sign == '-' and num2 == 18:
        return("26-18 = 8")
    if num1 == 26 and sign == '-' and num2 == 19:
        return("26-19 = 7")
    if num1 == 26 and sign == '-' and num2 == 20:
        return("26-20 = 6")
    if num1 == 26 and sign == '-' and num2 == 21:
        return("26-21 = 5")
    if num1 == 26 and sign == '-' and num2 == 22:
        return("26-22 = 4")
    if num1 == 26 and sign == '-' and num2 == 23:
        return("26-23 = 3")
    if num1 == 26 and sign == '-' and num2 == 24:
        return("26-24 = 2")
    if num1 == 26 and sign == '-' and num2 == 25:
        return("26-25 = 1")
    if num1 == 26 and sign == '-' and num2 == 26:
        return("26-26 = 0")
    if num1 == 26 and sign == '-' and num2 == 27:
        return("26-27 = -1")
    if num1 == 26 and sign == '-' and num2 == 28:
        return("26-28 = -2")
    if num1 == 26 and sign == '-' and num2 == 29:
        return("26-29 = -3")
    if num1 == 26 and sign == '-' and num2 == 30:
        return("26-30 = -4")
    if num1 == 26 and sign == '-' and num2 == 31:
        return("26-31 = -5")
    if num1 == 26 and sign == '-' and num2 == 32:
        return("26-32 = -6")
    if num1 == 26 and sign == '-' and num2 == 33:
        return("26-33 = -7")
    if num1 == 26 and sign == '-' and num2 == 34:
        return("26-34 = -8")
    if num1 == 26 and sign == '-' and num2 == 35:
        return("26-35 = -9")
    if num1 == 26 and sign == '-' and num2 == 36:
        return("26-36 = -10")
    if num1 == 26 and sign == '-' and num2 == 37:
        return("26-37 = -11")
    if num1 == 26 and sign == '-' and num2 == 38:
        return("26-38 = -12")
    if num1 == 26 and sign == '-' and num2 == 39:
        return("26-39 = -13")
    if num1 == 26 and sign == '-' and num2 == 40:
        return("26-40 = -14")
    if num1 == 26 and sign == '-' and num2 == 41:
        return("26-41 = -15")
    if num1 == 26 and sign == '-' and num2 == 42:
        return("26-42 = -16")
    if num1 == 26 and sign == '-' and num2 == 43:
        return("26-43 = -17")
    if num1 == 26 and sign == '-' and num2 == 44:
        return("26-44 = -18")
    if num1 == 26 and sign == '-' and num2 == 45:
        return("26-45 = -19")
    if num1 == 26 and sign == '-' and num2 == 46:
        return("26-46 = -20")
    if num1 == 26 and sign == '-' and num2 == 47:
        return("26-47 = -21")
    if num1 == 26 and sign == '-' and num2 == 48:
        return("26-48 = -22")
    if num1 == 26 and sign == '-' and num2 == 49:
        return("26-49 = -23")
    if num1 == 26 and sign == '-' and num2 == 50:
        return("26-50 = -24")
    if num1 == 27 and sign == '-' and num2 == 0:
        return("27-0 = 27")
    if num1 == 27 and sign == '-' and num2 == 1:
        return("27-1 = 26")
    if num1 == 27 and sign == '-' and num2 == 2:
        return("27-2 = 25")
    if num1 == 27 and sign == '-' and num2 == 3:
        return("27-3 = 24")
    if num1 == 27 and sign == '-' and num2 == 4:
        return("27-4 = 23")
    if num1 == 27 and sign == '-' and num2 == 5:
        return("27-5 = 22")
    if num1 == 27 and sign == '-' and num2 == 6:
        return("27-6 = 21")
    if num1 == 27 and sign == '-' and num2 == 7:
        return("27-7 = 20")
    if num1 == 27 and sign == '-' and num2 == 8:
        return("27-8 = 19")
    if num1 == 27 and sign == '-' and num2 == 9:
        return("27-9 = 18")
    if num1 == 27 and sign == '-' and num2 == 10:
        return("27-10 = 17")
    if num1 == 27 and sign == '-' and num2 == 11:
        return("27-11 = 16")
    if num1 == 27 and sign == '-' and num2 == 12:
        return("27-12 = 15")
    if num1 == 27 and sign == '-' and num2 == 13:
        return("27-13 = 14")
    if num1 == 27 and sign == '-' and num2 == 14:
        return("27-14 = 13")
    if num1 == 27 and sign == '-' and num2 == 15:
        return("27-15 = 12")
    if num1 == 27 and sign == '-' and num2 == 16:
        return("27-16 = 11")
    if num1 == 27 and sign == '-' and num2 == 17:
        return("27-17 = 10")
    if num1 == 27 and sign == '-' and num2 == 18:
        return("27-18 = 9")
    if num1 == 27 and sign == '-' and num2 == 19:
        return("27-19 = 8")
    if num1 == 27 and sign == '-' and num2 == 20:
        return("27-20 = 7")
    if num1 == 27 and sign == '-' and num2 == 21:
        return("27-21 = 6")
    if num1 == 27 and sign == '-' and num2 == 22:
        return("27-22 = 5")
    if num1 == 27 and sign == '-' and num2 == 23:
        return("27-23 = 4")
    if num1 == 27 and sign == '-' and num2 == 24:
        return("27-24 = 3")
    if num1 == 27 and sign == '-' and num2 == 25:
        return("27-25 = 2")
    if num1 == 27 and sign == '-' and num2 == 26:
        return("27-26 = 1")
    if num1 == 27 and sign == '-' and num2 == 27:
        return("27-27 = 0")
    if num1 == 27 and sign == '-' and num2 == 28:
        return("27-28 = -1")
    if num1 == 27 and sign == '-' and num2 == 29:
        return("27-29 = -2")
    if num1 == 27 and sign == '-' and num2 == 30:
        return("27-30 = -3")
    if num1 == 27 and sign == '-' and num2 == 31:
        return("27-31 = -4")
    if num1 == 27 and sign == '-' and num2 == 32:
        return("27-32 = -5")
    if num1 == 27 and sign == '-' and num2 == 33:
        return("27-33 = -6")
    if num1 == 27 and sign == '-' and num2 == 34:
        return("27-34 = -7")
    if num1 == 27 and sign == '-' and num2 == 35:
        return("27-35 = -8")
    if num1 == 27 and sign == '-' and num2 == 36:
        return("27-36 = -9")
    if num1 == 27 and sign == '-' and num2 == 37:
        return("27-37 = -10")
    if num1 == 27 and sign == '-' and num2 == 38:
        return("27-38 = -11")
    if num1 == 27 and sign == '-' and num2 == 39:
        return("27-39 = -12")
    if num1 == 27 and sign == '-' and num2 == 40:
        return("27-40 = -13")
    if num1 == 27 and sign == '-' and num2 == 41:
        return("27-41 = -14")
    if num1 == 27 and sign == '-' and num2 == 42:
        return("27-42 = -15")
    if num1 == 27 and sign == '-' and num2 == 43:
        return("27-43 = -16")
    if num1 == 27 and sign == '-' and num2 == 44:
        return("27-44 = -17")
    if num1 == 27 and sign == '-' and num2 == 45:
        return("27-45 = -18")
    if num1 == 27 and sign == '-' and num2 == 46:
        return("27-46 = -19")
    if num1 == 27 and sign == '-' and num2 == 47:
        return("27-47 = -20")
    if num1 == 27 and sign == '-' and num2 == 48:
        return("27-48 = -21")
    if num1 == 27 and sign == '-' and num2 == 49:
        return("27-49 = -22")
    if num1 == 27 and sign == '-' and num2 == 50:
        return("27-50 = -23")
    if num1 == 28 and sign == '-' and num2 == 0:
        return("28-0 = 28")
    if num1 == 28 and sign == '-' and num2 == 1:
        return("28-1 = 27")
    if num1 == 28 and sign == '-' and num2 == 2:
        return("28-2 = 26")
    if num1 == 28 and sign == '-' and num2 == 3:
        return("28-3 = 25")
    if num1 == 28 and sign == '-' and num2 == 4:
        return("28-4 = 24")
    if num1 == 28 and sign == '-' and num2 == 5:
        return("28-5 = 23")
    if num1 == 28 and sign == '-' and num2 == 6:
        return("28-6 = 22")
    if num1 == 28 and sign == '-' and num2 == 7:
        return("28-7 = 21")
    if num1 == 28 and sign == '-' and num2 == 8:
        return("28-8 = 20")
    if num1 == 28 and sign == '-' and num2 == 9:
        return("28-9 = 19")
    if num1 == 28 and sign == '-' and num2 == 10:
        return("28-10 = 18")
    if num1 == 28 and sign == '-' and num2 == 11:
        return("28-11 = 17")
    if num1 == 28 and sign == '-' and num2 == 12:
        return("28-12 = 16")
    if num1 == 28 and sign == '-' and num2 == 13:
        return("28-13 = 15")
    if num1 == 28 and sign == '-' and num2 == 14:
        return("28-14 = 14")
    if num1 == 28 and sign == '-' and num2 == 15:
        return("28-15 = 13")
    if num1 == 28 and sign == '-' and num2 == 16:
        return("28-16 = 12")
    if num1 == 28 and sign == '-' and num2 == 17:
        return("28-17 = 11")
    if num1 == 28 and sign == '-' and num2 == 18:
        return("28-18 = 10")
    if num1 == 28 and sign == '-' and num2 == 19:
        return("28-19 = 9")
    if num1 == 28 and sign == '-' and num2 == 20:
        return("28-20 = 8")
    if num1 == 28 and sign == '-' and num2 == 21:
        return("28-21 = 7")
    if num1 == 28 and sign == '-' and num2 == 22:
        return("28-22 = 6")
    if num1 == 28 and sign == '-' and num2 == 23:
        return("28-23 = 5")
    if num1 == 28 and sign == '-' and num2 == 24:
        return("28-24 = 4")
    if num1 == 28 and sign == '-' and num2 == 25:
        return("28-25 = 3")
    if num1 == 28 and sign == '-' and num2 == 26:
        return("28-26 = 2")
    if num1 == 28 and sign == '-' and num2 == 27:
        return("28-27 = 1")
    if num1 == 28 and sign == '-' and num2 == 28:
        return("28-28 = 0")
    if num1 == 28 and sign == '-' and num2 == 29:
        return("28-29 = -1")
    if num1 == 28 and sign == '-' and num2 == 30:
        return("28-30 = -2")
    if num1 == 28 and sign == '-' and num2 == 31:
        return("28-31 = -3")
    if num1 == 28 and sign == '-' and num2 == 32:
        return("28-32 = -4")
    if num1 == 28 and sign == '-' and num2 == 33:
        return("28-33 = -5")
    if num1 == 28 and sign == '-' and num2 == 34:
        return("28-34 = -6")
    if num1 == 28 and sign == '-' and num2 == 35:
        return("28-35 = -7")
    if num1 == 28 and sign == '-' and num2 == 36:
        return("28-36 = -8")
    if num1 == 28 and sign == '-' and num2 == 37:
        return("28-37 = -9")
    if num1 == 28 and sign == '-' and num2 == 38:
        return("28-38 = -10")
    if num1 == 28 and sign == '-' and num2 == 39:
        return("28-39 = -11")
    if num1 == 28 and sign == '-' and num2 == 40:
        return("28-40 = -12")
    if num1 == 28 and sign == '-' and num2 == 41:
        return("28-41 = -13")
    if num1 == 28 and sign == '-' and num2 == 42:
        return("28-42 = -14")
    if num1 == 28 and sign == '-' and num2 == 43:
        return("28-43 = -15")
    if num1 == 28 and sign == '-' and num2 == 44:
        return("28-44 = -16")
    if num1 == 28 and sign == '-' and num2 == 45:
        return("28-45 = -17")
    if num1 == 28 and sign == '-' and num2 == 46:
        return("28-46 = -18")
    if num1 == 28 and sign == '-' and num2 == 47:
        return("28-47 = -19")
    if num1 == 28 and sign == '-' and num2 == 48:
        return("28-48 = -20")
    if num1 == 28 and sign == '-' and num2 == 49:
        return("28-49 = -21")
    if num1 == 28 and sign == '-' and num2 == 50:
        return("28-50 = -22")
    if num1 == 29 and sign == '-' and num2 == 0:
        return("29-0 = 29")
    if num1 == 29 and sign == '-' and num2 == 1:
        return("29-1 = 28")
    if num1 == 29 and sign == '-' and num2 == 2:
        return("29-2 = 27")
    if num1 == 29 and sign == '-' and num2 == 3:
        return("29-3 = 26")
    if num1 == 29 and sign == '-' and num2 == 4:
        return("29-4 = 25")
    if num1 == 29 and sign == '-' and num2 == 5:
        return("29-5 = 24")
    if num1 == 29 and sign == '-' and num2 == 6:
        return("29-6 = 23")
    if num1 == 29 and sign == '-' and num2 == 7:
        return("29-7 = 22")
    if num1 == 29 and sign == '-' and num2 == 8:
        return("29-8 = 21")
    if num1 == 29 and sign == '-' and num2 == 9:
        return("29-9 = 20")
    if num1 == 29 and sign == '-' and num2 == 10:
        return("29-10 = 19")
    if num1 == 29 and sign == '-' and num2 == 11:
        return("29-11 = 18")
    if num1 == 29 and sign == '-' and num2 == 12:
        return("29-12 = 17")
    if num1 == 29 and sign == '-' and num2 == 13:
        return("29-13 = 16")
    if num1 == 29 and sign == '-' and num2 == 14:
        return("29-14 = 15")
    if num1 == 29 and sign == '-' and num2 == 15:
        return("29-15 = 14")
    if num1 == 29 and sign == '-' and num2 == 16:
        return("29-16 = 13")
    if num1 == 29 and sign == '-' and num2 == 17:
        return("29-17 = 12")
    if num1 == 29 and sign == '-' and num2 == 18:
        return("29-18 = 11")
    if num1 == 29 and sign == '-' and num2 == 19:
        return("29-19 = 10")
    if num1 == 29 and sign == '-' and num2 == 20:
        return("29-20 = 9")
    if num1 == 29 and sign == '-' and num2 == 21:
        return("29-21 = 8")
    if num1 == 29 and sign == '-' and num2 == 22:
        return("29-22 = 7")
    if num1 == 29 and sign == '-' and num2 == 23:
        return("29-23 = 6")
    if num1 == 29 and sign == '-' and num2 == 24:
        return("29-24 = 5")
    if num1 == 29 and sign == '-' and num2 == 25:
        return("29-25 = 4")
    if num1 == 29 and sign == '-' and num2 == 26:
        return("29-26 = 3")
    if num1 == 29 and sign == '-' and num2 == 27:
        return("29-27 = 2")
    if num1 == 29 and sign == '-' and num2 == 28:
        return("29-28 = 1")
    if num1 == 29 and sign == '-' and num2 == 29:
        return("29-29 = 0")
    if num1 == 29 and sign == '-' and num2 == 30:
        return("29-30 = -1")
    if num1 == 29 and sign == '-' and num2 == 31:
        return("29-31 = -2")
    if num1 == 29 and sign == '-' and num2 == 32:
        return("29-32 = -3")
    if num1 == 29 and sign == '-' and num2 == 33:
        return("29-33 = -4")
    if num1 == 29 and sign == '-' and num2 == 34:
        return("29-34 = -5")
    if num1 == 29 and sign == '-' and num2 == 35:
        return("29-35 = -6")
    if num1 == 29 and sign == '-' and num2 == 36:
        return("29-36 = -7")
    if num1 == 29 and sign == '-' and num2 == 37:
        return("29-37 = -8")
    if num1 == 29 and sign == '-' and num2 == 38:
        return("29-38 = -9")
    if num1 == 29 and sign == '-' and num2 == 39:
        return("29-39 = -10")
    if num1 == 29 and sign == '-' and num2 == 40:
        return("29-40 = -11")
    if num1 == 29 and sign == '-' and num2 == 41:
        return("29-41 = -12")
    if num1 == 29 and sign == '-' and num2 == 42:
        return("29-42 = -13")
    if num1 == 29 and sign == '-' and num2 == 43:
        return("29-43 = -14")
    if num1 == 29 and sign == '-' and num2 == 44:
        return("29-44 = -15")
    if num1 == 29 and sign == '-' and num2 == 45:
        return("29-45 = -16")
    if num1 == 29 and sign == '-' and num2 == 46:
        return("29-46 = -17")
    if num1 == 29 and sign == '-' and num2 == 47:
        return("29-47 = -18")
    if num1 == 29 and sign == '-' and num2 == 48:
        return("29-48 = -19")
    if num1 == 29 and sign == '-' and num2 == 49:
        return("29-49 = -20")
    if num1 == 29 and sign == '-' and num2 == 50:
        return("29-50 = -21")
    if num1 == 30 and sign == '-' and num2 == 0:
        return("30-0 = 30")
    if num1 == 30 and sign == '-' and num2 == 1:
        return("30-1 = 29")
    if num1 == 30 and sign == '-' and num2 == 2:
        return("30-2 = 28")
    if num1 == 30 and sign == '-' and num2 == 3:
        return("30-3 = 27")
    if num1 == 30 and sign == '-' and num2 == 4:
        return("30-4 = 26")
    if num1 == 30 and sign == '-' and num2 == 5:
        return("30-5 = 25")
    if num1 == 30 and sign == '-' and num2 == 6:
        return("30-6 = 24")
    if num1 == 30 and sign == '-' and num2 == 7:
        return("30-7 = 23")
    if num1 == 30 and sign == '-' and num2 == 8:
        return("30-8 = 22")
    if num1 == 30 and sign == '-' and num2 == 9:
        return("30-9 = 21")
    if num1 == 30 and sign == '-' and num2 == 10:
        return("30-10 = 20")
    if num1 == 30 and sign == '-' and num2 == 11:
        return("30-11 = 19")
    if num1 == 30 and sign == '-' and num2 == 12:
        return("30-12 = 18")
    if num1 == 30 and sign == '-' and num2 == 13:
        return("30-13 = 17")
    if num1 == 30 and sign == '-' and num2 == 14:
        return("30-14 = 16")
    if num1 == 30 and sign == '-' and num2 == 15:
        return("30-15 = 15")
    if num1 == 30 and sign == '-' and num2 == 16:
        return("30-16 = 14")
    if num1 == 30 and sign == '-' and num2 == 17:
        return("30-17 = 13")
    if num1 == 30 and sign == '-' and num2 == 18:
        return("30-18 = 12")
    if num1 == 30 and sign == '-' and num2 == 19:
        return("30-19 = 11")
    if num1 == 30 and sign == '-' and num2 == 20:
        return("30-20 = 10")
    if num1 == 30 and sign == '-' and num2 == 21:
        return("30-21 = 9")
    if num1 == 30 and sign == '-' and num2 == 22:
        return("30-22 = 8")
    if num1 == 30 and sign == '-' and num2 == 23:
        return("30-23 = 7")
    if num1 == 30 and sign == '-' and num2 == 24:
        return("30-24 = 6")
    if num1 == 30 and sign == '-' and num2 == 25:
        return("30-25 = 5")
    if num1 == 30 and sign == '-' and num2 == 26:
        return("30-26 = 4")
    if num1 == 30 and sign == '-' and num2 == 27:
        return("30-27 = 3")
    if num1 == 30 and sign == '-' and num2 == 28:
        return("30-28 = 2")
    if num1 == 30 and sign == '-' and num2 == 29:
        return("30-29 = 1")
    if num1 == 30 and sign == '-' and num2 == 30:
        return("30-30 = 0")
    if num1 == 30 and sign == '-' and num2 == 31:
        return("30-31 = -1")
    if num1 == 30 and sign == '-' and num2 == 32:
        return("30-32 = -2")
    if num1 == 30 and sign == '-' and num2 == 33:
        return("30-33 = -3")
    if num1 == 30 and sign == '-' and num2 == 34:
        return("30-34 = -4")
    if num1 == 30 and sign == '-' and num2 == 35:
        return("30-35 = -5")
    if num1 == 30 and sign == '-' and num2 == 36:
        return("30-36 = -6")
    if num1 == 30 and sign == '-' and num2 == 37:
        return("30-37 = -7")
    if num1 == 30 and sign == '-' and num2 == 38:
        return("30-38 = -8")
    if num1 == 30 and sign == '-' and num2 == 39:
        return("30-39 = -9")
    if num1 == 30 and sign == '-' and num2 == 40:
        return("30-40 = -10")
    if num1 == 30 and sign == '-' and num2 == 41:
        return("30-41 = -11")
    if num1 == 30 and sign == '-' and num2 == 42:
        return("30-42 = -12")
    if num1 == 30 and sign == '-' and num2 == 43:
        return("30-43 = -13")
    if num1 == 30 and sign == '-' and num2 == 44:
        return("30-44 = -14")
    if num1 == 30 and sign == '-' and num2 == 45:
        return("30-45 = -15")
    if num1 == 30 and sign == '-' and num2 == 46:
        return("30-46 = -16")
    if num1 == 30 and sign == '-' and num2 == 47:
        return("30-47 = -17")
    if num1 == 30 and sign == '-' and num2 == 48:
        return("30-48 = -18")
    if num1 == 30 and sign == '-' and num2 == 49:
        return("30-49 = -19")
    if num1 == 30 and sign == '-' and num2 == 50:
        return("30-50 = -20")
    if num1 == 31 and sign == '-' and num2 == 0:
        return("31-0 = 31")
    if num1 == 31 and sign == '-' and num2 == 1:
        return("31-1 = 30")
    if num1 == 31 and sign == '-' and num2 == 2:
        return("31-2 = 29")
    if num1 == 31 and sign == '-' and num2 == 3:
        return("31-3 = 28")
    if num1 == 31 and sign == '-' and num2 == 4:
        return("31-4 = 27")
    if num1 == 31 and sign == '-' and num2 == 5:
        return("31-5 = 26")
    if num1 == 31 and sign == '-' and num2 == 6:
        return("31-6 = 25")
    if num1 == 31 and sign == '-' and num2 == 7:
        return("31-7 = 24")
    if num1 == 31 and sign == '-' and num2 == 8:
        return("31-8 = 23")
    if num1 == 31 and sign == '-' and num2 == 9:
        return("31-9 = 22")
    if num1 == 31 and sign == '-' and num2 == 10:
        return("31-10 = 21")
    if num1 == 31 and sign == '-' and num2 == 11:
        return("31-11 = 20")
    if num1 == 31 and sign == '-' and num2 == 12:
        return("31-12 = 19")
    if num1 == 31 and sign == '-' and num2 == 13:
        return("31-13 = 18")
    if num1 == 31 and sign == '-' and num2 == 14:
        return("31-14 = 17")
    if num1 == 31 and sign == '-' and num2 == 15:
        return("31-15 = 16")
    if num1 == 31 and sign == '-' and num2 == 16:
        return("31-16 = 15")
    if num1 == 31 and sign == '-' and num2 == 17:
        return("31-17 = 14")
    if num1 == 31 and sign == '-' and num2 == 18:
        return("31-18 = 13")
    if num1 == 31 and sign == '-' and num2 == 19:
        return("31-19 = 12")
    if num1 == 31 and sign == '-' and num2 == 20:
        return("31-20 = 11")
    if num1 == 31 and sign == '-' and num2 == 21:
        return("31-21 = 10")
    if num1 == 31 and sign == '-' and num2 == 22:
        return("31-22 = 9")
    if num1 == 31 and sign == '-' and num2 == 23:
        return("31-23 = 8")
    if num1 == 31 and sign == '-' and num2 == 24:
        return("31-24 = 7")
    if num1 == 31 and sign == '-' and num2 == 25:
        return("31-25 = 6")
    if num1 == 31 and sign == '-' and num2 == 26:
        return("31-26 = 5")
    if num1 == 31 and sign == '-' and num2 == 27:
        return("31-27 = 4")
    if num1 == 31 and sign == '-' and num2 == 28:
        return("31-28 = 3")
    if num1 == 31 and sign == '-' and num2 == 29:
        return("31-29 = 2")
    if num1 == 31 and sign == '-' and num2 == 30:
        return("31-30 = 1")
    if num1 == 31 and sign == '-' and num2 == 31:
        return("31-31 = 0")
    if num1 == 31 and sign == '-' and num2 == 32:
        return("31-32 = -1")
    if num1 == 31 and sign == '-' and num2 == 33:
        return("31-33 = -2")
    if num1 == 31 and sign == '-' and num2 == 34:
        return("31-34 = -3")
    if num1 == 31 and sign == '-' and num2 == 35:
        return("31-35 = -4")
    if num1 == 31 and sign == '-' and num2 == 36:
        return("31-36 = -5")
    if num1 == 31 and sign == '-' and num2 == 37:
        return("31-37 = -6")
    if num1 == 31 and sign == '-' and num2 == 38:
        return("31-38 = -7")
    if num1 == 31 and sign == '-' and num2 == 39:
        return("31-39 = -8")
    if num1 == 31 and sign == '-' and num2 == 40:
        return("31-40 = -9")
    if num1 == 31 and sign == '-' and num2 == 41:
        return("31-41 = -10")
    if num1 == 31 and sign == '-' and num2 == 42:
        return("31-42 = -11")
    if num1 == 31 and sign == '-' and num2 == 43:
        return("31-43 = -12")
    if num1 == 31 and sign == '-' and num2 == 44:
        return("31-44 = -13")
    if num1 == 31 and sign == '-' and num2 == 45:
        return("31-45 = -14")
    if num1 == 31 and sign == '-' and num2 == 46:
        return("31-46 = -15")
    if num1 == 31 and sign == '-' and num2 == 47:
        return("31-47 = -16")
    if num1 == 31 and sign == '-' and num2 == 48:
        return("31-48 = -17")
    if num1 == 31 and sign == '-' and num2 == 49:
        return("31-49 = -18")
    if num1 == 31 and sign == '-' and num2 == 50:
        return("31-50 = -19")
    if num1 == 32 and sign == '-' and num2 == 0:
        return("32-0 = 32")
    if num1 == 32 and sign == '-' and num2 == 1:
        return("32-1 = 31")
    if num1 == 32 and sign == '-' and num2 == 2:
        return("32-2 = 30")
    if num1 == 32 and sign == '-' and num2 == 3:
        return("32-3 = 29")
    if num1 == 32 and sign == '-' and num2 == 4:
        return("32-4 = 28")
    if num1 == 32 and sign == '-' and num2 == 5:
        return("32-5 = 27")
    if num1 == 32 and sign == '-' and num2 == 6:
        return("32-6 = 26")
    if num1 == 32 and sign == '-' and num2 == 7:
        return("32-7 = 25")
    if num1 == 32 and sign == '-' and num2 == 8:
        return("32-8 = 24")
    if num1 == 32 and sign == '-' and num2 == 9:
        return("32-9 = 23")
    if num1 == 32 and sign == '-' and num2 == 10:
        return("32-10 = 22")
    if num1 == 32 and sign == '-' and num2 == 11:
        return("32-11 = 21")
    if num1 == 32 and sign == '-' and num2 == 12:
        return("32-12 = 20")
    if num1 == 32 and sign == '-' and num2 == 13:
        return("32-13 = 19")
    if num1 == 32 and sign == '-' and num2 == 14:
        return("32-14 = 18")
    if num1 == 32 and sign == '-' and num2 == 15:
        return("32-15 = 17")
    if num1 == 32 and sign == '-' and num2 == 16:
        return("32-16 = 16")
    if num1 == 32 and sign == '-' and num2 == 17:
        return("32-17 = 15")
    if num1 == 32 and sign == '-' and num2 == 18:
        return("32-18 = 14")
    if num1 == 32 and sign == '-' and num2 == 19:
        return("32-19 = 13")
    if num1 == 32 and sign == '-' and num2 == 20:
        return("32-20 = 12")
    if num1 == 32 and sign == '-' and num2 == 21:
        return("32-21 = 11")
    if num1 == 32 and sign == '-' and num2 == 22:
        return("32-22 = 10")
    if num1 == 32 and sign == '-' and num2 == 23:
        return("32-23 = 9")
    if num1 == 32 and sign == '-' and num2 == 24:
        return("32-24 = 8")
    if num1 == 32 and sign == '-' and num2 == 25:
        return("32-25 = 7")
    if num1 == 32 and sign == '-' and num2 == 26:
        return("32-26 = 6")
    if num1 == 32 and sign == '-' and num2 == 27:
        return("32-27 = 5")
    if num1 == 32 and sign == '-' and num2 == 28:
        return("32-28 = 4")
    if num1 == 32 and sign == '-' and num2 == 29:
        return("32-29 = 3")
    if num1 == 32 and sign == '-' and num2 == 30:
        return("32-30 = 2")
    if num1 == 32 and sign == '-' and num2 == 31:
        return("32-31 = 1")
    if num1 == 32 and sign == '-' and num2 == 32:
        return("32-32 = 0")
    if num1 == 32 and sign == '-' and num2 == 33:
        return("32-33 = -1")
    if num1 == 32 and sign == '-' and num2 == 34:
        return("32-34 = -2")
    if num1 == 32 and sign == '-' and num2 == 35:
        return("32-35 = -3")
    if num1 == 32 and sign == '-' and num2 == 36:
        return("32-36 = -4")
    if num1 == 32 and sign == '-' and num2 == 37:
        return("32-37 = -5")
    if num1 == 32 and sign == '-' and num2 == 38:
        return("32-38 = -6")
    if num1 == 32 and sign == '-' and num2 == 39:
        return("32-39 = -7")
    if num1 == 32 and sign == '-' and num2 == 40:
        return("32-40 = -8")
    if num1 == 32 and sign == '-' and num2 == 41:
        return("32-41 = -9")
    if num1 == 32 and sign == '-' and num2 == 42:
        return("32-42 = -10")
    if num1 == 32 and sign == '-' and num2 == 43:
        return("32-43 = -11")
    if num1 == 32 and sign == '-' and num2 == 44:
        return("32-44 = -12")
    if num1 == 32 and sign == '-' and num2 == 45:
        return("32-45 = -13")
    if num1 == 32 and sign == '-' and num2 == 46:
        return("32-46 = -14")
    if num1 == 32 and sign == '-' and num2 == 47:
        return("32-47 = -15")
    if num1 == 32 and sign == '-' and num2 == 48:
        return("32-48 = -16")
    if num1 == 32 and sign == '-' and num2 == 49:
        return("32-49 = -17")
    if num1 == 32 and sign == '-' and num2 == 50:
        return("32-50 = -18")
    if num1 == 33 and sign == '-' and num2 == 0:
        return("33-0 = 33")
    if num1 == 33 and sign == '-' and num2 == 1:
        return("33-1 = 32")
    if num1 == 33 and sign == '-' and num2 == 2:
        return("33-2 = 31")
    if num1 == 33 and sign == '-' and num2 == 3:
        return("33-3 = 30")
    if num1 == 33 and sign == '-' and num2 == 4:
        return("33-4 = 29")
    if num1 == 33 and sign == '-' and num2 == 5:
        return("33-5 = 28")
    if num1 == 33 and sign == '-' and num2 == 6:
        return("33-6 = 27")
    if num1 == 33 and sign == '-' and num2 == 7:
        return("33-7 = 26")
    if num1 == 33 and sign == '-' and num2 == 8:
        return("33-8 = 25")
    if num1 == 33 and sign == '-' and num2 == 9:
        return("33-9 = 24")
    if num1 == 33 and sign == '-' and num2 == 10:
        return("33-10 = 23")
    if num1 == 33 and sign == '-' and num2 == 11:
        return("33-11 = 22")
    if num1 == 33 and sign == '-' and num2 == 12:
        return("33-12 = 21")
    if num1 == 33 and sign == '-' and num2 == 13:
        return("33-13 = 20")
    if num1 == 33 and sign == '-' and num2 == 14:
        return("33-14 = 19")
    if num1 == 33 and sign == '-' and num2 == 15:
        return("33-15 = 18")
    if num1 == 33 and sign == '-' and num2 == 16:
        return("33-16 = 17")
    if num1 == 33 and sign == '-' and num2 == 17:
        return("33-17 = 16")
    if num1 == 33 and sign == '-' and num2 == 18:
        return("33-18 = 15")
    if num1 == 33 and sign == '-' and num2 == 19:
        return("33-19 = 14")
    if num1 == 33 and sign == '-' and num2 == 20:
        return("33-20 = 13")
    if num1 == 33 and sign == '-' and num2 == 21:
        return("33-21 = 12")
    if num1 == 33 and sign == '-' and num2 == 22:
        return("33-22 = 11")
    if num1 == 33 and sign == '-' and num2 == 23:
        return("33-23 = 10")
    if num1 == 33 and sign == '-' and num2 == 24:
        return("33-24 = 9")
    if num1 == 33 and sign == '-' and num2 == 25:
        return("33-25 = 8")
    if num1 == 33 and sign == '-' and num2 == 26:
        return("33-26 = 7")
    if num1 == 33 and sign == '-' and num2 == 27:
        return("33-27 = 6")
    if num1 == 33 and sign == '-' and num2 == 28:
        return("33-28 = 5")
    if num1 == 33 and sign == '-' and num2 == 29:
        return("33-29 = 4")
    if num1 == 33 and sign == '-' and num2 == 30:
        return("33-30 = 3")
    if num1 == 33 and sign == '-' and num2 == 31:
        return("33-31 = 2")
    if num1 == 33 and sign == '-' and num2 == 32:
        return("33-32 = 1")
    if num1 == 33 and sign == '-' and num2 == 33:
        return("33-33 = 0")
    if num1 == 33 and sign == '-' and num2 == 34:
        return("33-34 = -1")
    if num1 == 33 and sign == '-' and num2 == 35:
        return("33-35 = -2")
    if num1 == 33 and sign == '-' and num2 == 36:
        return("33-36 = -3")
    if num1 == 33 and sign == '-' and num2 == 37:
        return("33-37 = -4")
    if num1 == 33 and sign == '-' and num2 == 38:
        return("33-38 = -5")
    if num1 == 33 and sign == '-' and num2 == 39:
        return("33-39 = -6")
    if num1 == 33 and sign == '-' and num2 == 40:
        return("33-40 = -7")
    if num1 == 33 and sign == '-' and num2 == 41:
        return("33-41 = -8")
    if num1 == 33 and sign == '-' and num2 == 42:
        return("33-42 = -9")
    if num1 == 33 and sign == '-' and num2 == 43:
        return("33-43 = -10")
    if num1 == 33 and sign == '-' and num2 == 44:
        return("33-44 = -11")
    if num1 == 33 and sign == '-' and num2 == 45:
        return("33-45 = -12")
    if num1 == 33 and sign == '-' and num2 == 46:
        return("33-46 = -13")
    if num1 == 33 and sign == '-' and num2 == 47:
        return("33-47 = -14")
    if num1 == 33 and sign == '-' and num2 == 48:
        return("33-48 = -15")
    if num1 == 33 and sign == '-' and num2 == 49:
        return("33-49 = -16")
    if num1 == 33 and sign == '-' and num2 == 50:
        return("33-50 = -17")
    if num1 == 34 and sign == '-' and num2 == 0:
        return("34-0 = 34")
    if num1 == 34 and sign == '-' and num2 == 1:
        return("34-1 = 33")
    if num1 == 34 and sign == '-' and num2 == 2:
        return("34-2 = 32")
    if num1 == 34 and sign == '-' and num2 == 3:
        return("34-3 = 31")
    if num1 == 34 and sign == '-' and num2 == 4:
        return("34-4 = 30")
    if num1 == 34 and sign == '-' and num2 == 5:
        return("34-5 = 29")
    if num1 == 34 and sign == '-' and num2 == 6:
        return("34-6 = 28")
    if num1 == 34 and sign == '-' and num2 == 7:
        return("34-7 = 27")
    if num1 == 34 and sign == '-' and num2 == 8:
        return("34-8 = 26")
    if num1 == 34 and sign == '-' and num2 == 9:
        return("34-9 = 25")
    if num1 == 34 and sign == '-' and num2 == 10:
        return("34-10 = 24")
    if num1 == 34 and sign == '-' and num2 == 11:
        return("34-11 = 23")
    if num1 == 34 and sign == '-' and num2 == 12:
        return("34-12 = 22")
    if num1 == 34 and sign == '-' and num2 == 13:
        return("34-13 = 21")
    if num1 == 34 and sign == '-' and num2 == 14:
        return("34-14 = 20")
    if num1 == 34 and sign == '-' and num2 == 15:
        return("34-15 = 19")
    if num1 == 34 and sign == '-' and num2 == 16:
        return("34-16 = 18")
    if num1 == 34 and sign == '-' and num2 == 17:
        return("34-17 = 17")
    if num1 == 34 and sign == '-' and num2 == 18:
        return("34-18 = 16")
    if num1 == 34 and sign == '-' and num2 == 19:
        return("34-19 = 15")
    if num1 == 34 and sign == '-' and num2 == 20:
        return("34-20 = 14")
    if num1 == 34 and sign == '-' and num2 == 21:
        return("34-21 = 13")
    if num1 == 34 and sign == '-' and num2 == 22:
        return("34-22 = 12")
    if num1 == 34 and sign == '-' and num2 == 23:
        return("34-23 = 11")
    if num1 == 34 and sign == '-' and num2 == 24:
        return("34-24 = 10")
    if num1 == 34 and sign == '-' and num2 == 25:
        return("34-25 = 9")
    if num1 == 34 and sign == '-' and num2 == 26:
        return("34-26 = 8")
    if num1 == 34 and sign == '-' and num2 == 27:
        return("34-27 = 7")
    if num1 == 34 and sign == '-' and num2 == 28:
        return("34-28 = 6")
    if num1 == 34 and sign == '-' and num2 == 29:
        return("34-29 = 5")
    if num1 == 34 and sign == '-' and num2 == 30:
        return("34-30 = 4")
    if num1 == 34 and sign == '-' and num2 == 31:
        return("34-31 = 3")
    if num1 == 34 and sign == '-' and num2 == 32:
        return("34-32 = 2")
    if num1 == 34 and sign == '-' and num2 == 33:
        return("34-33 = 1")
    if num1 == 34 and sign == '-' and num2 == 34:
        return("34-34 = 0")
    if num1 == 34 and sign == '-' and num2 == 35:
        return("34-35 = -1")
    if num1 == 34 and sign == '-' and num2 == 36:
        return("34-36 = -2")
    if num1 == 34 and sign == '-' and num2 == 37:
        return("34-37 = -3")
    if num1 == 34 and sign == '-' and num2 == 38:
        return("34-38 = -4")
    if num1 == 34 and sign == '-' and num2 == 39:
        return("34-39 = -5")
    if num1 == 34 and sign == '-' and num2 == 40:
        return("34-40 = -6")
    if num1 == 34 and sign == '-' and num2 == 41:
        return("34-41 = -7")
    if num1 == 34 and sign == '-' and num2 == 42:
        return("34-42 = -8")
    if num1 == 34 and sign == '-' and num2 == 43:
        return("34-43 = -9")
    if num1 == 34 and sign == '-' and num2 == 44:
        return("34-44 = -10")
    if num1 == 34 and sign == '-' and num2 == 45:
        return("34-45 = -11")
    if num1 == 34 and sign == '-' and num2 == 46:
        return("34-46 = -12")
    if num1 == 34 and sign == '-' and num2 == 47:
        return("34-47 = -13")
    if num1 == 34 and sign == '-' and num2 == 48:
        return("34-48 = -14")
    if num1 == 34 and sign == '-' and num2 == 49:
        return("34-49 = -15")
    if num1 == 34 and sign == '-' and num2 == 50:
        return("34-50 = -16")
    if num1 == 35 and sign == '-' and num2 == 0:
        return("35-0 = 35")
    if num1 == 35 and sign == '-' and num2 == 1:
        return("35-1 = 34")
    if num1 == 35 and sign == '-' and num2 == 2:
        return("35-2 = 33")
    if num1 == 35 and sign == '-' and num2 == 3:
        return("35-3 = 32")
    if num1 == 35 and sign == '-' and num2 == 4:
        return("35-4 = 31")
    if num1 == 35 and sign == '-' and num2 == 5:
        return("35-5 = 30")
    if num1 == 35 and sign == '-' and num2 == 6:
        return("35-6 = 29")
    if num1 == 35 and sign == '-' and num2 == 7:
        return("35-7 = 28")
    if num1 == 35 and sign == '-' and num2 == 8:
        return("35-8 = 27")
    if num1 == 35 and sign == '-' and num2 == 9:
        return("35-9 = 26")
    if num1 == 35 and sign == '-' and num2 == 10:
        return("35-10 = 25")
    if num1 == 35 and sign == '-' and num2 == 11:
        return("35-11 = 24")
    if num1 == 35 and sign == '-' and num2 == 12:
        return("35-12 = 23")
    if num1 == 35 and sign == '-' and num2 == 13:
        return("35-13 = 22")
    if num1 == 35 and sign == '-' and num2 == 14:
        return("35-14 = 21")
    if num1 == 35 and sign == '-' and num2 == 15:
        return("35-15 = 20")
    if num1 == 35 and sign == '-' and num2 == 16:
        return("35-16 = 19")
    if num1 == 35 and sign == '-' and num2 == 17:
        return("35-17 = 18")
    if num1 == 35 and sign == '-' and num2 == 18:
        return("35-18 = 17")
    if num1 == 35 and sign == '-' and num2 == 19:
        return("35-19 = 16")
    if num1 == 35 and sign == '-' and num2 == 20:
        return("35-20 = 15")
    if num1 == 35 and sign == '-' and num2 == 21:
        return("35-21 = 14")
    if num1 == 35 and sign == '-' and num2 == 22:
        return("35-22 = 13")
    if num1 == 35 and sign == '-' and num2 == 23:
        return("35-23 = 12")
    if num1 == 35 and sign == '-' and num2 == 24:
        return("35-24 = 11")
    if num1 == 35 and sign == '-' and num2 == 25:
        return("35-25 = 10")
    if num1 == 35 and sign == '-' and num2 == 26:
        return("35-26 = 9")
    if num1 == 35 and sign == '-' and num2 == 27:
        return("35-27 = 8")
    if num1 == 35 and sign == '-' and num2 == 28:
        return("35-28 = 7")
    if num1 == 35 and sign == '-' and num2 == 29:
        return("35-29 = 6")
    if num1 == 35 and sign == '-' and num2 == 30:
        return("35-30 = 5")
    if num1 == 35 and sign == '-' and num2 == 31:
        return("35-31 = 4")
    if num1 == 35 and sign == '-' and num2 == 32:
        return("35-32 = 3")
    if num1 == 35 and sign == '-' and num2 == 33:
        return("35-33 = 2")
    if num1 == 35 and sign == '-' and num2 == 34:
        return("35-34 = 1")
    if num1 == 35 and sign == '-' and num2 == 35:
        return("35-35 = 0")
    if num1 == 35 and sign == '-' and num2 == 36:
        return("35-36 = -1")
    if num1 == 35 and sign == '-' and num2 == 37:
        return("35-37 = -2")
    if num1 == 35 and sign == '-' and num2 == 38:
        return("35-38 = -3")
    if num1 == 35 and sign == '-' and num2 == 39:
        return("35-39 = -4")
    if num1 == 35 and sign == '-' and num2 == 40:
        return("35-40 = -5")
    if num1 == 35 and sign == '-' and num2 == 41:
        return("35-41 = -6")
    if num1 == 35 and sign == '-' and num2 == 42:
        return("35-42 = -7")
    if num1 == 35 and sign == '-' and num2 == 43:
        return("35-43 = -8")
    if num1 == 35 and sign == '-' and num2 == 44:
        return("35-44 = -9")
    if num1 == 35 and sign == '-' and num2 == 45:
        return("35-45 = -10")
    if num1 == 35 and sign == '-' and num2 == 46:
        return("35-46 = -11")
    if num1 == 35 and sign == '-' and num2 == 47:
        return("35-47 = -12")
    if num1 == 35 and sign == '-' and num2 == 48:
        return("35-48 = -13")
    if num1 == 35 and sign == '-' and num2 == 49:
        return("35-49 = -14")
    if num1 == 35 and sign == '-' and num2 == 50:
        return("35-50 = -15")
    if num1 == 36 and sign == '-' and num2 == 0:
        return("36-0 = 36")
    if num1 == 36 and sign == '-' and num2 == 1:
        return("36-1 = 35")
    if num1 == 36 and sign == '-' and num2 == 2:
        return("36-2 = 34")
    if num1 == 36 and sign == '-' and num2 == 3:
        return("36-3 = 33")
    if num1 == 36 and sign == '-' and num2 == 4:
        return("36-4 = 32")
    if num1 == 36 and sign == '-' and num2 == 5:
        return("36-5 = 31")
    if num1 == 36 and sign == '-' and num2 == 6:
        return("36-6 = 30")
    if num1 == 36 and sign == '-' and num2 == 7:
        return("36-7 = 29")
    if num1 == 36 and sign == '-' and num2 == 8:
        return("36-8 = 28")
    if num1 == 36 and sign == '-' and num2 == 9:
        return("36-9 = 27")
    if num1 == 36 and sign == '-' and num2 == 10:
        return("36-10 = 26")
    if num1 == 36 and sign == '-' and num2 == 11:
        return("36-11 = 25")
    if num1 == 36 and sign == '-' and num2 == 12:
        return("36-12 = 24")
    if num1 == 36 and sign == '-' and num2 == 13:
        return("36-13 = 23")
    if num1 == 36 and sign == '-' and num2 == 14:
        return("36-14 = 22")
    if num1 == 36 and sign == '-' and num2 == 15:
        return("36-15 = 21")
    if num1 == 36 and sign == '-' and num2 == 16:
        return("36-16 = 20")
    if num1 == 36 and sign == '-' and num2 == 17:
        return("36-17 = 19")
    if num1 == 36 and sign == '-' and num2 == 18:
        return("36-18 = 18")
    if num1 == 36 and sign == '-' and num2 == 19:
        return("36-19 = 17")
    if num1 == 36 and sign == '-' and num2 == 20:
        return("36-20 = 16")
    if num1 == 36 and sign == '-' and num2 == 21:
        return("36-21 = 15")
    if num1 == 36 and sign == '-' and num2 == 22:
        return("36-22 = 14")
    if num1 == 36 and sign == '-' and num2 == 23:
        return("36-23 = 13")
    if num1 == 36 and sign == '-' and num2 == 24:
        return("36-24 = 12")
    if num1 == 36 and sign == '-' and num2 == 25:
        return("36-25 = 11")
    if num1 == 36 and sign == '-' and num2 == 26:
        return("36-26 = 10")
    if num1 == 36 and sign == '-' and num2 == 27:
        return("36-27 = 9")
    if num1 == 36 and sign == '-' and num2 == 28:
        return("36-28 = 8")
    if num1 == 36 and sign == '-' and num2 == 29:
        return("36-29 = 7")
    if num1 == 36 and sign == '-' and num2 == 30:
        return("36-30 = 6")
    if num1 == 36 and sign == '-' and num2 == 31:
        return("36-31 = 5")
    if num1 == 36 and sign == '-' and num2 == 32:
        return("36-32 = 4")
    if num1 == 36 and sign == '-' and num2 == 33:
        return("36-33 = 3")
    if num1 == 36 and sign == '-' and num2 == 34:
        return("36-34 = 2")
    if num1 == 36 and sign == '-' and num2 == 35:
        return("36-35 = 1")
    if num1 == 36 and sign == '-' and num2 == 36:
        return("36-36 = 0")
    if num1 == 36 and sign == '-' and num2 == 37:
        return("36-37 = -1")
    if num1 == 36 and sign == '-' and num2 == 38:
        return("36-38 = -2")
    if num1 == 36 and sign == '-' and num2 == 39:
        return("36-39 = -3")
    if num1 == 36 and sign == '-' and num2 == 40:
        return("36-40 = -4")
    if num1 == 36 and sign == '-' and num2 == 41:
        return("36-41 = -5")
    if num1 == 36 and sign == '-' and num2 == 42:
        return("36-42 = -6")
    if num1 == 36 and sign == '-' and num2 == 43:
        return("36-43 = -7")
    if num1 == 36 and sign == '-' and num2 == 44:
        return("36-44 = -8")
    if num1 == 36 and sign == '-' and num2 == 45:
        return("36-45 = -9")
    if num1 == 36 and sign == '-' and num2 == 46:
        return("36-46 = -10")
    if num1 == 36 and sign == '-' and num2 == 47:
        return("36-47 = -11")
    if num1 == 36 and sign == '-' and num2 == 48:
        return("36-48 = -12")
    if num1 == 36 and sign == '-' and num2 == 49:
        return("36-49 = -13")
    if num1 == 36 and sign == '-' and num2 == 50:
        return("36-50 = -14")
    if num1 == 37 and sign == '-' and num2 == 0:
        return("37-0 = 37")
    if num1 == 37 and sign == '-' and num2 == 1:
        return("37-1 = 36")
    if num1 == 37 and sign == '-' and num2 == 2:
        return("37-2 = 35")
    if num1 == 37 and sign == '-' and num2 == 3:
        return("37-3 = 34")
    if num1 == 37 and sign == '-' and num2 == 4:
        return("37-4 = 33")
    if num1 == 37 and sign == '-' and num2 == 5:
        return("37-5 = 32")
    if num1 == 37 and sign == '-' and num2 == 6:
        return("37-6 = 31")
    if num1 == 37 and sign == '-' and num2 == 7:
        return("37-7 = 30")
    if num1 == 37 and sign == '-' and num2 == 8:
        return("37-8 = 29")
    if num1 == 37 and sign == '-' and num2 == 9:
        return("37-9 = 28")
    if num1 == 37 and sign == '-' and num2 == 10:
        return("37-10 = 27")
    if num1 == 37 and sign == '-' and num2 == 11:
        return("37-11 = 26")
    if num1 == 37 and sign == '-' and num2 == 12:
        return("37-12 = 25")
    if num1 == 37 and sign == '-' and num2 == 13:
        return("37-13 = 24")
    if num1 == 37 and sign == '-' and num2 == 14:
        return("37-14 = 23")
    if num1 == 37 and sign == '-' and num2 == 15:
        return("37-15 = 22")
    if num1 == 37 and sign == '-' and num2 == 16:
        return("37-16 = 21")
    if num1 == 37 and sign == '-' and num2 == 17:
        return("37-17 = 20")
    if num1 == 37 and sign == '-' and num2 == 18:
        return("37-18 = 19")
    if num1 == 37 and sign == '-' and num2 == 19:
        return("37-19 = 18")
    if num1 == 37 and sign == '-' and num2 == 20:
        return("37-20 = 17")
    if num1 == 37 and sign == '-' and num2 == 21:
        return("37-21 = 16")
    if num1 == 37 and sign == '-' and num2 == 22:
        return("37-22 = 15")
    if num1 == 37 and sign == '-' and num2 == 23:
        return("37-23 = 14")
    if num1 == 37 and sign == '-' and num2 == 24:
        return("37-24 = 13")
    if num1 == 37 and sign == '-' and num2 == 25:
        return("37-25 = 12")
    if num1 == 37 and sign == '-' and num2 == 26:
        return("37-26 = 11")
    if num1 == 37 and sign == '-' and num2 == 27:
        return("37-27 = 10")
    if num1 == 37 and sign == '-' and num2 == 28:
        return("37-28 = 9")
    if num1 == 37 and sign == '-' and num2 == 29:
        return("37-29 = 8")
    if num1 == 37 and sign == '-' and num2 == 30:
        return("37-30 = 7")
    if num1 == 37 and sign == '-' and num2 == 31:
        return("37-31 = 6")
    if num1 == 37 and sign == '-' and num2 == 32:
        return("37-32 = 5")
    if num1 == 37 and sign == '-' and num2 == 33:
        return("37-33 = 4")
    if num1 == 37 and sign == '-' and num2 == 34:
        return("37-34 = 3")
    if num1 == 37 and sign == '-' and num2 == 35:
        return("37-35 = 2")
    if num1 == 37 and sign == '-' and num2 == 36:
        return("37-36 = 1")
    if num1 == 37 and sign == '-' and num2 == 37:
        return("37-37 = 0")
    if num1 == 37 and sign == '-' and num2 == 38:
        return("37-38 = -1")
    if num1 == 37 and sign == '-' and num2 == 39:
        return("37-39 = -2")
    if num1 == 37 and sign == '-' and num2 == 40:
        return("37-40 = -3")
    if num1 == 37 and sign == '-' and num2 == 41:
        return("37-41 = -4")
    if num1 == 37 and sign == '-' and num2 == 42:
        return("37-42 = -5")
    if num1 == 37 and sign == '-' and num2 == 43:
        return("37-43 = -6")
    if num1 == 37 and sign == '-' and num2 == 44:
        return("37-44 = -7")
    if num1 == 37 and sign == '-' and num2 == 45:
        return("37-45 = -8")
    if num1 == 37 and sign == '-' and num2 == 46:
        return("37-46 = -9")
    if num1 == 37 and sign == '-' and num2 == 47:
        return("37-47 = -10")
    if num1 == 37 and sign == '-' and num2 == 48:
        return("37-48 = -11")
    if num1 == 37 and sign == '-' and num2 == 49:
        return("37-49 = -12")
    if num1 == 37 and sign == '-' and num2 == 50:
        return("37-50 = -13")
    if num1 == 38 and sign == '-' and num2 == 0:
        return("38-0 = 38")
    if num1 == 38 and sign == '-' and num2 == 1:
        return("38-1 = 37")
    if num1 == 38 and sign == '-' and num2 == 2:
        return("38-2 = 36")
    if num1 == 38 and sign == '-' and num2 == 3:
        return("38-3 = 35")
    if num1 == 38 and sign == '-' and num2 == 4:
        return("38-4 = 34")
    if num1 == 38 and sign == '-' and num2 == 5:
        return("38-5 = 33")
    if num1 == 38 and sign == '-' and num2 == 6:
        return("38-6 = 32")
    if num1 == 38 and sign == '-' and num2 == 7:
        return("38-7 = 31")
    if num1 == 38 and sign == '-' and num2 == 8:
        return("38-8 = 30")
    if num1 == 38 and sign == '-' and num2 == 9:
        return("38-9 = 29")
    if num1 == 38 and sign == '-' and num2 == 10:
        return("38-10 = 28")
    if num1 == 38 and sign == '-' and num2 == 11:
        return("38-11 = 27")
    if num1 == 38 and sign == '-' and num2 == 12:
        return("38-12 = 26")
    if num1 == 38 and sign == '-' and num2 == 13:
        return("38-13 = 25")
    if num1 == 38 and sign == '-' and num2 == 14:
        return("38-14 = 24")
    if num1 == 38 and sign == '-' and num2 == 15:
        return("38-15 = 23")
    if num1 == 38 and sign == '-' and num2 == 16:
        return("38-16 = 22")
    if num1 == 38 and sign == '-' and num2 == 17:
        return("38-17 = 21")
    if num1 == 38 and sign == '-' and num2 == 18:
        return("38-18 = 20")
    if num1 == 38 and sign == '-' and num2 == 19:
        return("38-19 = 19")
    if num1 == 38 and sign == '-' and num2 == 20:
        return("38-20 = 18")
    if num1 == 38 and sign == '-' and num2 == 21:
        return("38-21 = 17")
    if num1 == 38 and sign == '-' and num2 == 22:
        return("38-22 = 16")
    if num1 == 38 and sign == '-' and num2 == 23:
        return("38-23 = 15")
    if num1 == 38 and sign == '-' and num2 == 24:
        return("38-24 = 14")
    if num1 == 38 and sign == '-' and num2 == 25:
        return("38-25 = 13")
    if num1 == 38 and sign == '-' and num2 == 26:
        return("38-26 = 12")
    if num1 == 38 and sign == '-' and num2 == 27:
        return("38-27 = 11")
    if num1 == 38 and sign == '-' and num2 == 28:
        return("38-28 = 10")
    if num1 == 38 and sign == '-' and num2 == 29:
        return("38-29 = 9")
    if num1 == 38 and sign == '-' and num2 == 30:
        return("38-30 = 8")
    if num1 == 38 and sign == '-' and num2 == 31:
        return("38-31 = 7")
    if num1 == 38 and sign == '-' and num2 == 32:
        return("38-32 = 6")
    if num1 == 38 and sign == '-' and num2 == 33:
        return("38-33 = 5")
    if num1 == 38 and sign == '-' and num2 == 34:
        return("38-34 = 4")
    if num1 == 38 and sign == '-' and num2 == 35:
        return("38-35 = 3")
    if num1 == 38 and sign == '-' and num2 == 36:
        return("38-36 = 2")
    if num1 == 38 and sign == '-' and num2 == 37:
        return("38-37 = 1")
    if num1 == 38 and sign == '-' and num2 == 38:
        return("38-38 = 0")
    if num1 == 38 and sign == '-' and num2 == 39:
        return("38-39 = -1")
    if num1 == 38 and sign == '-' and num2 == 40:
        return("38-40 = -2")
    if num1 == 38 and sign == '-' and num2 == 41:
        return("38-41 = -3")
    if num1 == 38 and sign == '-' and num2 == 42:
        return("38-42 = -4")
    if num1 == 38 and sign == '-' and num2 == 43:
        return("38-43 = -5")
    if num1 == 38 and sign == '-' and num2 == 44:
        return("38-44 = -6")
    if num1 == 38 and sign == '-' and num2 == 45:
        return("38-45 = -7")
    if num1 == 38 and sign == '-' and num2 == 46:
        return("38-46 = -8")
    if num1 == 38 and sign == '-' and num2 == 47:
        return("38-47 = -9")
    if num1 == 38 and sign == '-' and num2 == 48:
        return("38-48 = -10")
    if num1 == 38 and sign == '-' and num2 == 49:
        return("38-49 = -11")
    if num1 == 38 and sign == '-' and num2 == 50:
        return("38-50 = -12")
    if num1 == 39 and sign == '-' and num2 == 0:
        return("39-0 = 39")
    if num1 == 39 and sign == '-' and num2 == 1:
        return("39-1 = 38")
    if num1 == 39 and sign == '-' and num2 == 2:
        return("39-2 = 37")
    if num1 == 39 and sign == '-' and num2 == 3:
        return("39-3 = 36")
    if num1 == 39 and sign == '-' and num2 == 4:
        return("39-4 = 35")
    if num1 == 39 and sign == '-' and num2 == 5:
        return("39-5 = 34")
    if num1 == 39 and sign == '-' and num2 == 6:
        return("39-6 = 33")
    if num1 == 39 and sign == '-' and num2 == 7:
        return("39-7 = 32")
    if num1 == 39 and sign == '-' and num2 == 8:
        return("39-8 = 31")
    if num1 == 39 and sign == '-' and num2 == 9:
        return("39-9 = 30")
    if num1 == 39 and sign == '-' and num2 == 10:
        return("39-10 = 29")
    if num1 == 39 and sign == '-' and num2 == 11:
        return("39-11 = 28")
    if num1 == 39 and sign == '-' and num2 == 12:
        return("39-12 = 27")
    if num1 == 39 and sign == '-' and num2 == 13:
        return("39-13 = 26")
    if num1 == 39 and sign == '-' and num2 == 14:
        return("39-14 = 25")
    if num1 == 39 and sign == '-' and num2 == 15:
        return("39-15 = 24")
    if num1 == 39 and sign == '-' and num2 == 16:
        return("39-16 = 23")
    if num1 == 39 and sign == '-' and num2 == 17:
        return("39-17 = 22")
    if num1 == 39 and sign == '-' and num2 == 18:
        return("39-18 = 21")
    if num1 == 39 and sign == '-' and num2 == 19:
        return("39-19 = 20")
    if num1 == 39 and sign == '-' and num2 == 20:
        return("39-20 = 19")
    if num1 == 39 and sign == '-' and num2 == 21:
        return("39-21 = 18")
    if num1 == 39 and sign == '-' and num2 == 22:
        return("39-22 = 17")
    if num1 == 39 and sign == '-' and num2 == 23:
        return("39-23 = 16")
    if num1 == 39 and sign == '-' and num2 == 24:
        return("39-24 = 15")
    if num1 == 39 and sign == '-' and num2 == 25:
        return("39-25 = 14")
    if num1 == 39 and sign == '-' and num2 == 26:
        return("39-26 = 13")
    if num1 == 39 and sign == '-' and num2 == 27:
        return("39-27 = 12")
    if num1 == 39 and sign == '-' and num2 == 28:
        return("39-28 = 11")
    if num1 == 39 and sign == '-' and num2 == 29:
        return("39-29 = 10")
    if num1 == 39 and sign == '-' and num2 == 30:
        return("39-30 = 9")
    if num1 == 39 and sign == '-' and num2 == 31:
        return("39-31 = 8")
    if num1 == 39 and sign == '-' and num2 == 32:
        return("39-32 = 7")
    if num1 == 39 and sign == '-' and num2 == 33:
        return("39-33 = 6")
    if num1 == 39 and sign == '-' and num2 == 34:
        return("39-34 = 5")
    if num1 == 39 and sign == '-' and num2 == 35:
        return("39-35 = 4")
    if num1 == 39 and sign == '-' and num2 == 36:
        return("39-36 = 3")
    if num1 == 39 and sign == '-' and num2 == 37:
        return("39-37 = 2")
    if num1 == 39 and sign == '-' and num2 == 38:
        return("39-38 = 1")
    if num1 == 39 and sign == '-' and num2 == 39:
        return("39-39 = 0")
    if num1 == 39 and sign == '-' and num2 == 40:
        return("39-40 = -1")
    if num1 == 39 and sign == '-' and num2 == 41:
        return("39-41 = -2")
    if num1 == 39 and sign == '-' and num2 == 42:
        return("39-42 = -3")
    if num1 == 39 and sign == '-' and num2 == 43:
        return("39-43 = -4")
    if num1 == 39 and sign == '-' and num2 == 44:
        return("39-44 = -5")
    if num1 == 39 and sign == '-' and num2 == 45:
        return("39-45 = -6")
    if num1 == 39 and sign == '-' and num2 == 46:
        return("39-46 = -7")
    if num1 == 39 and sign == '-' and num2 == 47:
        return("39-47 = -8")
    if num1 == 39 and sign == '-' and num2 == 48:
        return("39-48 = -9")
    if num1 == 39 and sign == '-' and num2 == 49:
        return("39-49 = -10")
    if num1 == 39 and sign == '-' and num2 == 50:
        return("39-50 = -11")
    if num1 == 40 and sign == '-' and num2 == 0:
        return("40-0 = 40")
    if num1 == 40 and sign == '-' and num2 == 1:
        return("40-1 = 39")
    if num1 == 40 and sign == '-' and num2 == 2:
        return("40-2 = 38")
    if num1 == 40 and sign == '-' and num2 == 3:
        return("40-3 = 37")
    if num1 == 40 and sign == '-' and num2 == 4:
        return("40-4 = 36")
    if num1 == 40 and sign == '-' and num2 == 5:
        return("40-5 = 35")
    if num1 == 40 and sign == '-' and num2 == 6:
        return("40-6 = 34")
    if num1 == 40 and sign == '-' and num2 == 7:
        return("40-7 = 33")
    if num1 == 40 and sign == '-' and num2 == 8:
        return("40-8 = 32")
    if num1 == 40 and sign == '-' and num2 == 9:
        return("40-9 = 31")
    if num1 == 40 and sign == '-' and num2 == 10:
        return("40-10 = 30")
    if num1 == 40 and sign == '-' and num2 == 11:
        return("40-11 = 29")
    if num1 == 40 and sign == '-' and num2 == 12:
        return("40-12 = 28")
    if num1 == 40 and sign == '-' and num2 == 13:
        return("40-13 = 27")
    if num1 == 40 and sign == '-' and num2 == 14:
        return("40-14 = 26")
    if num1 == 40 and sign == '-' and num2 == 15:
        return("40-15 = 25")
    if num1 == 40 and sign == '-' and num2 == 16:
        return("40-16 = 24")
    if num1 == 40 and sign == '-' and num2 == 17:
        return("40-17 = 23")
    if num1 == 40 and sign == '-' and num2 == 18:
        return("40-18 = 22")
    if num1 == 40 and sign == '-' and num2 == 19:
        return("40-19 = 21")
    if num1 == 40 and sign == '-' and num2 == 20:
        return("40-20 = 20")
    if num1 == 40 and sign == '-' and num2 == 21:
        return("40-21 = 19")
    if num1 == 40 and sign == '-' and num2 == 22:
        return("40-22 = 18")
    if num1 == 40 and sign == '-' and num2 == 23:
        return("40-23 = 17")
    if num1 == 40 and sign == '-' and num2 == 24:
        return("40-24 = 16")
    if num1 == 40 and sign == '-' and num2 == 25:
        return("40-25 = 15")
    if num1 == 40 and sign == '-' and num2 == 26:
        return("40-26 = 14")
    if num1 == 40 and sign == '-' and num2 == 27:
        return("40-27 = 13")
    if num1 == 40 and sign == '-' and num2 == 28:
        return("40-28 = 12")
    if num1 == 40 and sign == '-' and num2 == 29:
        return("40-29 = 11")
    if num1 == 40 and sign == '-' and num2 == 30:
        return("40-30 = 10")
    if num1 == 40 and sign == '-' and num2 == 31:
        return("40-31 = 9")
    if num1 == 40 and sign == '-' and num2 == 32:
        return("40-32 = 8")
    if num1 == 40 and sign == '-' and num2 == 33:
        return("40-33 = 7")
    if num1 == 40 and sign == '-' and num2 == 34:
        return("40-34 = 6")
    if num1 == 40 and sign == '-' and num2 == 35:
        return("40-35 = 5")
    if num1 == 40 and sign == '-' and num2 == 36:
        return("40-36 = 4")
    if num1 == 40 and sign == '-' and num2 == 37:
        return("40-37 = 3")
    if num1 == 40 and sign == '-' and num2 == 38:
        return("40-38 = 2")
    if num1 == 40 and sign == '-' and num2 == 39:
        return("40-39 = 1")
    if num1 == 40 and sign == '-' and num2 == 40:
        return("40-40 = 0")
    if num1 == 40 and sign == '-' and num2 == 41:
        return("40-41 = -1")
    if num1 == 40 and sign == '-' and num2 == 42:
        return("40-42 = -2")
    if num1 == 40 and sign == '-' and num2 == 43:
        return("40-43 = -3")
    if num1 == 40 and sign == '-' and num2 == 44:
        return("40-44 = -4")
    if num1 == 40 and sign == '-' and num2 == 45:
        return("40-45 = -5")
    if num1 == 40 and sign == '-' and num2 == 46:
        return("40-46 = -6")
    if num1 == 40 and sign == '-' and num2 == 47:
        return("40-47 = -7")
    if num1 == 40 and sign == '-' and num2 == 48:
        return("40-48 = -8")
    if num1 == 40 and sign == '-' and num2 == 49:
        return("40-49 = -9")
    if num1 == 40 and sign == '-' and num2 == 50:
        return("40-50 = -10")
    if num1 == 41 and sign == '-' and num2 == 0:
        return("41-0 = 41")
    if num1 == 41 and sign == '-' and num2 == 1:
        return("41-1 = 40")
    if num1 == 41 and sign == '-' and num2 == 2:
        return("41-2 = 39")
    if num1 == 41 and sign == '-' and num2 == 3:
        return("41-3 = 38")
    if num1 == 41 and sign == '-' and num2 == 4:
        return("41-4 = 37")
    if num1 == 41 and sign == '-' and num2 == 5:
        return("41-5 = 36")
    if num1 == 41 and sign == '-' and num2 == 6:
        return("41-6 = 35")
    if num1 == 41 and sign == '-' and num2 == 7:
        return("41-7 = 34")
    if num1 == 41 and sign == '-' and num2 == 8:
        return("41-8 = 33")
    if num1 == 41 and sign == '-' and num2 == 9:
        return("41-9 = 32")
    if num1 == 41 and sign == '-' and num2 == 10:
        return("41-10 = 31")
    if num1 == 41 and sign == '-' and num2 == 11:
        return("41-11 = 30")
    if num1 == 41 and sign == '-' and num2 == 12:
        return("41-12 = 29")
    if num1 == 41 and sign == '-' and num2 == 13:
        return("41-13 = 28")
    if num1 == 41 and sign == '-' and num2 == 14:
        return("41-14 = 27")
    if num1 == 41 and sign == '-' and num2 == 15:
        return("41-15 = 26")
    if num1 == 41 and sign == '-' and num2 == 16:
        return("41-16 = 25")
    if num1 == 41 and sign == '-' and num2 == 17:
        return("41-17 = 24")
    if num1 == 41 and sign == '-' and num2 == 18:
        return("41-18 = 23")
    if num1 == 41 and sign == '-' and num2 == 19:
        return("41-19 = 22")
    if num1 == 41 and sign == '-' and num2 == 20:
        return("41-20 = 21")
    if num1 == 41 and sign == '-' and num2 == 21:
        return("41-21 = 20")
    if num1 == 41 and sign == '-' and num2 == 22:
        return("41-22 = 19")
    if num1 == 41 and sign == '-' and num2 == 23:
        return("41-23 = 18")
    if num1 == 41 and sign == '-' and num2 == 24:
        return("41-24 = 17")
    if num1 == 41 and sign == '-' and num2 == 25:
        return("41-25 = 16")
    if num1 == 41 and sign == '-' and num2 == 26:
        return("41-26 = 15")
    if num1 == 41 and sign == '-' and num2 == 27:
        return("41-27 = 14")
    if num1 == 41 and sign == '-' and num2 == 28:
        return("41-28 = 13")
    if num1 == 41 and sign == '-' and num2 == 29:
        return("41-29 = 12")
    if num1 == 41 and sign == '-' and num2 == 30:
        return("41-30 = 11")
    if num1 == 41 and sign == '-' and num2 == 31:
        return("41-31 = 10")
    if num1 == 41 and sign == '-' and num2 == 32:
        return("41-32 = 9")
    if num1 == 41 and sign == '-' and num2 == 33:
        return("41-33 = 8")
    if num1 == 41 and sign == '-' and num2 == 34:
        return("41-34 = 7")
    if num1 == 41 and sign == '-' and num2 == 35:
        return("41-35 = 6")
    if num1 == 41 and sign == '-' and num2 == 36:
        return("41-36 = 5")
    if num1 == 41 and sign == '-' and num2 == 37:
        return("41-37 = 4")
    if num1 == 41 and sign == '-' and num2 == 38:
        return("41-38 = 3")
    if num1 == 41 and sign == '-' and num2 == 39:
        return("41-39 = 2")
    if num1 == 41 and sign == '-' and num2 == 40:
        return("41-40 = 1")
    if num1 == 41 and sign == '-' and num2 == 41:
        return("41-41 = 0")
    if num1 == 41 and sign == '-' and num2 == 42:
        return("41-42 = -1")
    if num1 == 41 and sign == '-' and num2 == 43:
        return("41-43 = -2")
    if num1 == 41 and sign == '-' and num2 == 44:
        return("41-44 = -3")
    if num1 == 41 and sign == '-' and num2 == 45:
        return("41-45 = -4")
    if num1 == 41 and sign == '-' and num2 == 46:
        return("41-46 = -5")
    if num1 == 41 and sign == '-' and num2 == 47:
        return("41-47 = -6")
    if num1 == 41 and sign == '-' and num2 == 48:
        return("41-48 = -7")
    if num1 == 41 and sign == '-' and num2 == 49:
        return("41-49 = -8")
    if num1 == 41 and sign == '-' and num2 == 50:
        return("41-50 = -9")
    if num1 == 42 and sign == '-' and num2 == 0:
        return("42-0 = 42")
    if num1 == 42 and sign == '-' and num2 == 1:
        return("42-1 = 41")
    if num1 == 42 and sign == '-' and num2 == 2:
        return("42-2 = 40")
    if num1 == 42 and sign == '-' and num2 == 3:
        return("42-3 = 39")
    if num1 == 42 and sign == '-' and num2 == 4:
        return("42-4 = 38")
    if num1 == 42 and sign == '-' and num2 == 5:
        return("42-5 = 37")
    if num1 == 42 and sign == '-' and num2 == 6:
        return("42-6 = 36")
    if num1 == 42 and sign == '-' and num2 == 7:
        return("42-7 = 35")
    if num1 == 42 and sign == '-' and num2 == 8:
        return("42-8 = 34")
    if num1 == 42 and sign == '-' and num2 == 9:
        return("42-9 = 33")
    if num1 == 42 and sign == '-' and num2 == 10:
        return("42-10 = 32")
    if num1 == 42 and sign == '-' and num2 == 11:
        return("42-11 = 31")
    if num1 == 42 and sign == '-' and num2 == 12:
        return("42-12 = 30")
    if num1 == 42 and sign == '-' and num2 == 13:
        return("42-13 = 29")
    if num1 == 42 and sign == '-' and num2 == 14:
        return("42-14 = 28")
    if num1 == 42 and sign == '-' and num2 == 15:
        return("42-15 = 27")
    if num1 == 42 and sign == '-' and num2 == 16:
        return("42-16 = 26")
    if num1 == 42 and sign == '-' and num2 == 17:
        return("42-17 = 25")
    if num1 == 42 and sign == '-' and num2 == 18:
        return("42-18 = 24")
    if num1 == 42 and sign == '-' and num2 == 19:
        return("42-19 = 23")
    if num1 == 42 and sign == '-' and num2 == 20:
        return("42-20 = 22")
    if num1 == 42 and sign == '-' and num2 == 21:
        return("42-21 = 21")
    if num1 == 42 and sign == '-' and num2 == 22:
        return("42-22 = 20")
    if num1 == 42 and sign == '-' and num2 == 23:
        return("42-23 = 19")
    if num1 == 42 and sign == '-' and num2 == 24:
        return("42-24 = 18")
    if num1 == 42 and sign == '-' and num2 == 25:
        return("42-25 = 17")
    if num1 == 42 and sign == '-' and num2 == 26:
        return("42-26 = 16")
    if num1 == 42 and sign == '-' and num2 == 27:
        return("42-27 = 15")
    if num1 == 42 and sign == '-' and num2 == 28:
        return("42-28 = 14")
    if num1 == 42 and sign == '-' and num2 == 29:
        return("42-29 = 13")
    if num1 == 42 and sign == '-' and num2 == 30:
        return("42-30 = 12")
    if num1 == 42 and sign == '-' and num2 == 31:
        return("42-31 = 11")
    if num1 == 42 and sign == '-' and num2 == 32:
        return("42-32 = 10")
    if num1 == 42 and sign == '-' and num2 == 33:
        return("42-33 = 9")
    if num1 == 42 and sign == '-' and num2 == 34:
        return("42-34 = 8")
    if num1 == 42 and sign == '-' and num2 == 35:
        return("42-35 = 7")
    if num1 == 42 and sign == '-' and num2 == 36:
        return("42-36 = 6")
    if num1 == 42 and sign == '-' and num2 == 37:
        return("42-37 = 5")
    if num1 == 42 and sign == '-' and num2 == 38:
        return("42-38 = 4")
    if num1 == 42 and sign == '-' and num2 == 39:
        return("42-39 = 3")
    if num1 == 42 and sign == '-' and num2 == 40:
        return("42-40 = 2")
    if num1 == 42 and sign == '-' and num2 == 41:
        return("42-41 = 1")
    if num1 == 42 and sign == '-' and num2 == 42:
        return("42-42 = 0")
    if num1 == 42 and sign == '-' and num2 == 43:
        return("42-43 = -1")
    if num1 == 42 and sign == '-' and num2 == 44:
        return("42-44 = -2")
    if num1 == 42 and sign == '-' and num2 == 45:
        return("42-45 = -3")
    if num1 == 42 and sign == '-' and num2 == 46:
        return("42-46 = -4")
    if num1 == 42 and sign == '-' and num2 == 47:
        return("42-47 = -5")
    if num1 == 42 and sign == '-' and num2 == 48:
        return("42-48 = -6")
    if num1 == 42 and sign == '-' and num2 == 49:
        return("42-49 = -7")
    if num1 == 42 and sign == '-' and num2 == 50:
        return("42-50 = -8")
    if num1 == 43 and sign == '-' and num2 == 0:
        return("43-0 = 43")
    if num1 == 43 and sign == '-' and num2 == 1:
        return("43-1 = 42")
    if num1 == 43 and sign == '-' and num2 == 2:
        return("43-2 = 41")
    if num1 == 43 and sign == '-' and num2 == 3:
        return("43-3 = 40")
    if num1 == 43 and sign == '-' and num2 == 4:
        return("43-4 = 39")
    if num1 == 43 and sign == '-' and num2 == 5:
        return("43-5 = 38")
    if num1 == 43 and sign == '-' and num2 == 6:
        return("43-6 = 37")
    if num1 == 43 and sign == '-' and num2 == 7:
        return("43-7 = 36")
    if num1 == 43 and sign == '-' and num2 == 8:
        return("43-8 = 35")
    if num1 == 43 and sign == '-' and num2 == 9:
        return("43-9 = 34")
    if num1 == 43 and sign == '-' and num2 == 10:
        return("43-10 = 33")
    if num1 == 43 and sign == '-' and num2 == 11:
        return("43-11 = 32")
    if num1 == 43 and sign == '-' and num2 == 12:
        return("43-12 = 31")
    if num1 == 43 and sign == '-' and num2 == 13:
        return("43-13 = 30")
    if num1 == 43 and sign == '-' and num2 == 14:
        return("43-14 = 29")
    if num1 == 43 and sign == '-' and num2 == 15:
        return("43-15 = 28")
    if num1 == 43 and sign == '-' and num2 == 16:
        return("43-16 = 27")
    if num1 == 43 and sign == '-' and num2 == 17:
        return("43-17 = 26")
    if num1 == 43 and sign == '-' and num2 == 18:
        return("43-18 = 25")
    if num1 == 43 and sign == '-' and num2 == 19:
        return("43-19 = 24")
    if num1 == 43 and sign == '-' and num2 == 20:
        return("43-20 = 23")
    if num1 == 43 and sign == '-' and num2 == 21:
        return("43-21 = 22")
    if num1 == 43 and sign == '-' and num2 == 22:
        return("43-22 = 21")
    if num1 == 43 and sign == '-' and num2 == 23:
        return("43-23 = 20")
    if num1 == 43 and sign == '-' and num2 == 24:
        return("43-24 = 19")
    if num1 == 43 and sign == '-' and num2 == 25:
        return("43-25 = 18")
    if num1 == 43 and sign == '-' and num2 == 26:
        return("43-26 = 17")
    if num1 == 43 and sign == '-' and num2 == 27:
        return("43-27 = 16")
    if num1 == 43 and sign == '-' and num2 == 28:
        return("43-28 = 15")
    if num1 == 43 and sign == '-' and num2 == 29:
        return("43-29 = 14")
    if num1 == 43 and sign == '-' and num2 == 30:
        return("43-30 = 13")
    if num1 == 43 and sign == '-' and num2 == 31:
        return("43-31 = 12")
    if num1 == 43 and sign == '-' and num2 == 32:
        return("43-32 = 11")
    if num1 == 43 and sign == '-' and num2 == 33:
        return("43-33 = 10")
    if num1 == 43 and sign == '-' and num2 == 34:
        return("43-34 = 9")
    if num1 == 43 and sign == '-' and num2 == 35:
        return("43-35 = 8")
    if num1 == 43 and sign == '-' and num2 == 36:
        return("43-36 = 7")
    if num1 == 43 and sign == '-' and num2 == 37:
        return("43-37 = 6")
    if num1 == 43 and sign == '-' and num2 == 38:
        return("43-38 = 5")
    if num1 == 43 and sign == '-' and num2 == 39:
        return("43-39 = 4")
    if num1 == 43 and sign == '-' and num2 == 40:
        return("43-40 = 3")
    if num1 == 43 and sign == '-' and num2 == 41:
        return("43-41 = 2")
    if num1 == 43 and sign == '-' and num2 == 42:
        return("43-42 = 1")
    if num1 == 43 and sign == '-' and num2 == 43:
        return("43-43 = 0")
    if num1 == 43 and sign == '-' and num2 == 44:
        return("43-44 = -1")
    if num1 == 43 and sign == '-' and num2 == 45:
        return("43-45 = -2")
    if num1 == 43 and sign == '-' and num2 == 46:
        return("43-46 = -3")
    if num1 == 43 and sign == '-' and num2 == 47:
        return("43-47 = -4")
    if num1 == 43 and sign == '-' and num2 == 48:
        return("43-48 = -5")
    if num1 == 43 and sign == '-' and num2 == 49:
        return("43-49 = -6")
    if num1 == 43 and sign == '-' and num2 == 50:
        return("43-50 = -7")
    if num1 == 44 and sign == '-' and num2 == 0:
        return("44-0 = 44")
    if num1 == 44 and sign == '-' and num2 == 1:
        return("44-1 = 43")
    if num1 == 44 and sign == '-' and num2 == 2:
        return("44-2 = 42")
    if num1 == 44 and sign == '-' and num2 == 3:
        return("44-3 = 41")
    if num1 == 44 and sign == '-' and num2 == 4:
        return("44-4 = 40")
    if num1 == 44 and sign == '-' and num2 == 5:
        return("44-5 = 39")
    if num1 == 44 and sign == '-' and num2 == 6:
        return("44-6 = 38")
    if num1 == 44 and sign == '-' and num2 == 7:
        return("44-7 = 37")
    if num1 == 44 and sign == '-' and num2 == 8:
        return("44-8 = 36")
    if num1 == 44 and sign == '-' and num2 == 9:
        return("44-9 = 35")
    if num1 == 44 and sign == '-' and num2 == 10:
        return("44-10 = 34")
    if num1 == 44 and sign == '-' and num2 == 11:
        return("44-11 = 33")
    if num1 == 44 and sign == '-' and num2 == 12:
        return("44-12 = 32")
    if num1 == 44 and sign == '-' and num2 == 13:
        return("44-13 = 31")
    if num1 == 44 and sign == '-' and num2 == 14:
        return("44-14 = 30")
    if num1 == 44 and sign == '-' and num2 == 15:
        return("44-15 = 29")
    if num1 == 44 and sign == '-' and num2 == 16:
        return("44-16 = 28")
    if num1 == 44 and sign == '-' and num2 == 17:
        return("44-17 = 27")
    if num1 == 44 and sign == '-' and num2 == 18:
        return("44-18 = 26")
    if num1 == 44 and sign == '-' and num2 == 19:
        return("44-19 = 25")
    if num1 == 44 and sign == '-' and num2 == 20:
        return("44-20 = 24")
    if num1 == 44 and sign == '-' and num2 == 21:
        return("44-21 = 23")
    if num1 == 44 and sign == '-' and num2 == 22:
        return("44-22 = 22")
    if num1 == 44 and sign == '-' and num2 == 23:
        return("44-23 = 21")
    if num1 == 44 and sign == '-' and num2 == 24:
        return("44-24 = 20")
    if num1 == 44 and sign == '-' and num2 == 25:
        return("44-25 = 19")
    if num1 == 44 and sign == '-' and num2 == 26:
        return("44-26 = 18")
    if num1 == 44 and sign == '-' and num2 == 27:
        return("44-27 = 17")
    if num1 == 44 and sign == '-' and num2 == 28:
        return("44-28 = 16")
    if num1 == 44 and sign == '-' and num2 == 29:
        return("44-29 = 15")
    if num1 == 44 and sign == '-' and num2 == 30:
        return("44-30 = 14")
    if num1 == 44 and sign == '-' and num2 == 31:
        return("44-31 = 13")
    if num1 == 44 and sign == '-' and num2 == 32:
        return("44-32 = 12")
    if num1 == 44 and sign == '-' and num2 == 33:
        return("44-33 = 11")
    if num1 == 44 and sign == '-' and num2 == 34:
        return("44-34 = 10")
    if num1 == 44 and sign == '-' and num2 == 35:
        return("44-35 = 9")
    if num1 == 44 and sign == '-' and num2 == 36:
        return("44-36 = 8")
    if num1 == 44 and sign == '-' and num2 == 37:
        return("44-37 = 7")
    if num1 == 44 and sign == '-' and num2 == 38:
        return("44-38 = 6")
    if num1 == 44 and sign == '-' and num2 == 39:
        return("44-39 = 5")
    if num1 == 44 and sign == '-' and num2 == 40:
        return("44-40 = 4")
    if num1 == 44 and sign == '-' and num2 == 41:
        return("44-41 = 3")
    if num1 == 44 and sign == '-' and num2 == 42:
        return("44-42 = 2")
    if num1 == 44 and sign == '-' and num2 == 43:
        return("44-43 = 1")
    if num1 == 44 and sign == '-' and num2 == 44:
        return("44-44 = 0")
    if num1 == 44 and sign == '-' and num2 == 45:
        return("44-45 = -1")
    if num1 == 44 and sign == '-' and num2 == 46:
        return("44-46 = -2")
    if num1 == 44 and sign == '-' and num2 == 47:
        return("44-47 = -3")
    if num1 == 44 and sign == '-' and num2 == 48:
        return("44-48 = -4")
    if num1 == 44 and sign == '-' and num2 == 49:
        return("44-49 = -5")
    if num1 == 44 and sign == '-' and num2 == 50:
        return("44-50 = -6")
    if num1 == 45 and sign == '-' and num2 == 0:
        return("45-0 = 45")
    if num1 == 45 and sign == '-' and num2 == 1:
        return("45-1 = 44")
    if num1 == 45 and sign == '-' and num2 == 2:
        return("45-2 = 43")
    if num1 == 45 and sign == '-' and num2 == 3:
        return("45-3 = 42")
    if num1 == 45 and sign == '-' and num2 == 4:
        return("45-4 = 41")
    if num1 == 45 and sign == '-' and num2 == 5:
        return("45-5 = 40")
    if num1 == 45 and sign == '-' and num2 == 6:
        return("45-6 = 39")
    if num1 == 45 and sign == '-' and num2 == 7:
        return("45-7 = 38")
    if num1 == 45 and sign == '-' and num2 == 8:
        return("45-8 = 37")
    if num1 == 45 and sign == '-' and num2 == 9:
        return("45-9 = 36")
    if num1 == 45 and sign == '-' and num2 == 10:
        return("45-10 = 35")
    if num1 == 45 and sign == '-' and num2 == 11:
        return("45-11 = 34")
    if num1 == 45 and sign == '-' and num2 == 12:
        return("45-12 = 33")
    if num1 == 45 and sign == '-' and num2 == 13:
        return("45-13 = 32")
    if num1 == 45 and sign == '-' and num2 == 14:
        return("45-14 = 31")
    if num1 == 45 and sign == '-' and num2 == 15:
        return("45-15 = 30")
    if num1 == 45 and sign == '-' and num2 == 16:
        return("45-16 = 29")
    if num1 == 45 and sign == '-' and num2 == 17:
        return("45-17 = 28")
    if num1 == 45 and sign == '-' and num2 == 18:
        return("45-18 = 27")
    if num1 == 45 and sign == '-' and num2 == 19:
        return("45-19 = 26")
    if num1 == 45 and sign == '-' and num2 == 20:
        return("45-20 = 25")
    if num1 == 45 and sign == '-' and num2 == 21:
        return("45-21 = 24")
    if num1 == 45 and sign == '-' and num2 == 22:
        return("45-22 = 23")
    if num1 == 45 and sign == '-' and num2 == 23:
        return("45-23 = 22")
    if num1 == 45 and sign == '-' and num2 == 24:
        return("45-24 = 21")
    if num1 == 45 and sign == '-' and num2 == 25:
        return("45-25 = 20")
    if num1 == 45 and sign == '-' and num2 == 26:
        return("45-26 = 19")
    if num1 == 45 and sign == '-' and num2 == 27:
        return("45-27 = 18")
    if num1 == 45 and sign == '-' and num2 == 28:
        return("45-28 = 17")
    if num1 == 45 and sign == '-' and num2 == 29:
        return("45-29 = 16")
    if num1 == 45 and sign == '-' and num2 == 30:
        return("45-30 = 15")
    if num1 == 45 and sign == '-' and num2 == 31:
        return("45-31 = 14")
    if num1 == 45 and sign == '-' and num2 == 32:
        return("45-32 = 13")
    if num1 == 45 and sign == '-' and num2 == 33:
        return("45-33 = 12")
    if num1 == 45 and sign == '-' and num2 == 34:
        return("45-34 = 11")
    if num1 == 45 and sign == '-' and num2 == 35:
        return("45-35 = 10")
    if num1 == 45 and sign == '-' and num2 == 36:
        return("45-36 = 9")
    if num1 == 45 and sign == '-' and num2 == 37:
        return("45-37 = 8")
    if num1 == 45 and sign == '-' and num2 == 38:
        return("45-38 = 7")
    if num1 == 45 and sign == '-' and num2 == 39:
        return("45-39 = 6")
    if num1 == 45 and sign == '-' and num2 == 40:
        return("45-40 = 5")
    if num1 == 45 and sign == '-' and num2 == 41:
        return("45-41 = 4")
    if num1 == 45 and sign == '-' and num2 == 42:
        return("45-42 = 3")
    if num1 == 45 and sign == '-' and num2 == 43:
        return("45-43 = 2")
    if num1 == 45 and sign == '-' and num2 == 44:
        return("45-44 = 1")
    if num1 == 45 and sign == '-' and num2 == 45:
        return("45-45 = 0")
    if num1 == 45 and sign == '-' and num2 == 46:
        return("45-46 = -1")
    if num1 == 45 and sign == '-' and num2 == 47:
        return("45-47 = -2")
    if num1 == 45 and sign == '-' and num2 == 48:
        return("45-48 = -3")
    if num1 == 45 and sign == '-' and num2 == 49:
        return("45-49 = -4")
    if num1 == 45 and sign == '-' and num2 == 50:
        return("45-50 = -5")
    if num1 == 46 and sign == '-' and num2 == 0:
        return("46-0 = 46")
    if num1 == 46 and sign == '-' and num2 == 1:
        return("46-1 = 45")
    if num1 == 46 and sign == '-' and num2 == 2:
        return("46-2 = 44")
    if num1 == 46 and sign == '-' and num2 == 3:
        return("46-3 = 43")
    if num1 == 46 and sign == '-' and num2 == 4:
        return("46-4 = 42")
    if num1 == 46 and sign == '-' and num2 == 5:
        return("46-5 = 41")
    if num1 == 46 and sign == '-' and num2 == 6:
        return("46-6 = 40")
    if num1 == 46 and sign == '-' and num2 == 7:
        return("46-7 = 39")
    if num1 == 46 and sign == '-' and num2 == 8:
        return("46-8 = 38")
    if num1 == 46 and sign == '-' and num2 == 9:
        return("46-9 = 37")
    if num1 == 46 and sign == '-' and num2 == 10:
        return("46-10 = 36")
    if num1 == 46 and sign == '-' and num2 == 11:
        return("46-11 = 35")
    if num1 == 46 and sign == '-' and num2 == 12:
        return("46-12 = 34")
    if num1 == 46 and sign == '-' and num2 == 13:
        return("46-13 = 33")
    if num1 == 46 and sign == '-' and num2 == 14:
        return("46-14 = 32")
    if num1 == 46 and sign == '-' and num2 == 15:
        return("46-15 = 31")
    if num1 == 46 and sign == '-' and num2 == 16:
        return("46-16 = 30")
    if num1 == 46 and sign == '-' and num2 == 17:
        return("46-17 = 29")
    if num1 == 46 and sign == '-' and num2 == 18:
        return("46-18 = 28")
    if num1 == 46 and sign == '-' and num2 == 19:
        return("46-19 = 27")
    if num1 == 46 and sign == '-' and num2 == 20:
        return("46-20 = 26")
    if num1 == 46 and sign == '-' and num2 == 21:
        return("46-21 = 25")
    if num1 == 46 and sign == '-' and num2 == 22:
        return("46-22 = 24")
    if num1 == 46 and sign == '-' and num2 == 23:
        return("46-23 = 23")
    if num1 == 46 and sign == '-' and num2 == 24:
        return("46-24 = 22")
    if num1 == 46 and sign == '-' and num2 == 25:
        return("46-25 = 21")
    if num1 == 46 and sign == '-' and num2 == 26:
        return("46-26 = 20")
    if num1 == 46 and sign == '-' and num2 == 27:
        return("46-27 = 19")
    if num1 == 46 and sign == '-' and num2 == 28:
        return("46-28 = 18")
    if num1 == 46 and sign == '-' and num2 == 29:
        return("46-29 = 17")
    if num1 == 46 and sign == '-' and num2 == 30:
        return("46-30 = 16")
    if num1 == 46 and sign == '-' and num2 == 31:
        return("46-31 = 15")
    if num1 == 46 and sign == '-' and num2 == 32:
        return("46-32 = 14")
    if num1 == 46 and sign == '-' and num2 == 33:
        return("46-33 = 13")
    if num1 == 46 and sign == '-' and num2 == 34:
        return("46-34 = 12")
    if num1 == 46 and sign == '-' and num2 == 35:
        return("46-35 = 11")
    if num1 == 46 and sign == '-' and num2 == 36:
        return("46-36 = 10")
    if num1 == 46 and sign == '-' and num2 == 37:
        return("46-37 = 9")
    if num1 == 46 and sign == '-' and num2 == 38:
        return("46-38 = 8")
    if num1 == 46 and sign == '-' and num2 == 39:
        return("46-39 = 7")
    if num1 == 46 and sign == '-' and num2 == 40:
        return("46-40 = 6")
    if num1 == 46 and sign == '-' and num2 == 41:
        return("46-41 = 5")
    if num1 == 46 and sign == '-' and num2 == 42:
        return("46-42 = 4")
    if num1 == 46 and sign == '-' and num2 == 43:
        return("46-43 = 3")
    if num1 == 46 and sign == '-' and num2 == 44:
        return("46-44 = 2")
    if num1 == 46 and sign == '-' and num2 == 45:
        return("46-45 = 1")
    if num1 == 46 and sign == '-' and num2 == 46:
        return("46-46 = 0")
    if num1 == 46 and sign == '-' and num2 == 47:
        return("46-47 = -1")
    if num1 == 46 and sign == '-' and num2 == 48:
        return("46-48 = -2")
    if num1 == 46 and sign == '-' and num2 == 49:
        return("46-49 = -3")
    if num1 == 46 and sign == '-' and num2 == 50:
        return("46-50 = -4")
    if num1 == 47 and sign == '-' and num2 == 0:
        return("47-0 = 47")
    if num1 == 47 and sign == '-' and num2 == 1:
        return("47-1 = 46")
    if num1 == 47 and sign == '-' and num2 == 2:
        return("47-2 = 45")
    if num1 == 47 and sign == '-' and num2 == 3:
        return("47-3 = 44")
    if num1 == 47 and sign == '-' and num2 == 4:
        return("47-4 = 43")
    if num1 == 47 and sign == '-' and num2 == 5:
        return("47-5 = 42")
    if num1 == 47 and sign == '-' and num2 == 6:
        return("47-6 = 41")
    if num1 == 47 and sign == '-' and num2 == 7:
        return("47-7 = 40")
    if num1 == 47 and sign == '-' and num2 == 8:
        return("47-8 = 39")
    if num1 == 47 and sign == '-' and num2 == 9:
        return("47-9 = 38")
    if num1 == 47 and sign == '-' and num2 == 10:
        return("47-10 = 37")
    if num1 == 47 and sign == '-' and num2 == 11:
        return("47-11 = 36")
    if num1 == 47 and sign == '-' and num2 == 12:
        return("47-12 = 35")
    if num1 == 47 and sign == '-' and num2 == 13:
        return("47-13 = 34")
    if num1 == 47 and sign == '-' and num2 == 14:
        return("47-14 = 33")
    if num1 == 47 and sign == '-' and num2 == 15:
        return("47-15 = 32")
    if num1 == 47 and sign == '-' and num2 == 16:
        return("47-16 = 31")
    if num1 == 47 and sign == '-' and num2 == 17:
        return("47-17 = 30")
    if num1 == 47 and sign == '-' and num2 == 18:
        return("47-18 = 29")
    if num1 == 47 and sign == '-' and num2 == 19:
        return("47-19 = 28")
    if num1 == 47 and sign == '-' and num2 == 20:
        return("47-20 = 27")
    if num1 == 47 and sign == '-' and num2 == 21:
        return("47-21 = 26")
    if num1 == 47 and sign == '-' and num2 == 22:
        return("47-22 = 25")
    if num1 == 47 and sign == '-' and num2 == 23:
        return("47-23 = 24")
    if num1 == 47 and sign == '-' and num2 == 24:
        return("47-24 = 23")
    if num1 == 47 and sign == '-' and num2 == 25:
        return("47-25 = 22")
    if num1 == 47 and sign == '-' and num2 == 26:
        return("47-26 = 21")
    if num1 == 47 and sign == '-' and num2 == 27:
        return("47-27 = 20")
    if num1 == 47 and sign == '-' and num2 == 28:
        return("47-28 = 19")
    if num1 == 47 and sign == '-' and num2 == 29:
        return("47-29 = 18")
    if num1 == 47 and sign == '-' and num2 == 30:
        return("47-30 = 17")
    if num1 == 47 and sign == '-' and num2 == 31:
        return("47-31 = 16")
    if num1 == 47 and sign == '-' and num2 == 32:
        return("47-32 = 15")
    if num1 == 47 and sign == '-' and num2 == 33:
        return("47-33 = 14")
    if num1 == 47 and sign == '-' and num2 == 34:
        return("47-34 = 13")
    if num1 == 47 and sign == '-' and num2 == 35:
        return("47-35 = 12")
    if num1 == 47 and sign == '-' and num2 == 36:
        return("47-36 = 11")
    if num1 == 47 and sign == '-' and num2 == 37:
        return("47-37 = 10")
    if num1 == 47 and sign == '-' and num2 == 38:
        return("47-38 = 9")
    if num1 == 47 and sign == '-' and num2 == 39:
        return("47-39 = 8")
    if num1 == 47 and sign == '-' and num2 == 40:
        return("47-40 = 7")
    if num1 == 47 and sign == '-' and num2 == 41:
        return("47-41 = 6")
    if num1 == 47 and sign == '-' and num2 == 42:
        return("47-42 = 5")
    if num1 == 47 and sign == '-' and num2 == 43:
        return("47-43 = 4")
    if num1 == 47 and sign == '-' and num2 == 44:
        return("47-44 = 3")
    if num1 == 47 and sign == '-' and num2 == 45:
        return("47-45 = 2")
    if num1 == 47 and sign == '-' and num2 == 46:
        return("47-46 = 1")
    if num1 == 47 and sign == '-' and num2 == 47:
        return("47-47 = 0")
    if num1 == 47 and sign == '-' and num2 == 48:
        return("47-48 = -1")
    if num1 == 47 and sign == '-' and num2 == 49:
        return("47-49 = -2")
    if num1 == 47 and sign == '-' and num2 == 50:
        return("47-50 = -3")
    if num1 == 48 and sign == '-' and num2 == 0:
        return("48-0 = 48")
    if num1 == 48 and sign == '-' and num2 == 1:
        return("48-1 = 47")
    if num1 == 48 and sign == '-' and num2 == 2:
        return("48-2 = 46")
    if num1 == 48 and sign == '-' and num2 == 3:
        return("48-3 = 45")
    if num1 == 48 and sign == '-' and num2 == 4:
        return("48-4 = 44")
    if num1 == 48 and sign == '-' and num2 == 5:
        return("48-5 = 43")
    if num1 == 48 and sign == '-' and num2 == 6:
        return("48-6 = 42")
    if num1 == 48 and sign == '-' and num2 == 7:
        return("48-7 = 41")
    if num1 == 48 and sign == '-' and num2 == 8:
        return("48-8 = 40")
    if num1 == 48 and sign == '-' and num2 == 9:
        return("48-9 = 39")
    if num1 == 48 and sign == '-' and num2 == 10:
        return("48-10 = 38")
    if num1 == 48 and sign == '-' and num2 == 11:
        return("48-11 = 37")
    if num1 == 48 and sign == '-' and num2 == 12:
        return("48-12 = 36")
    if num1 == 48 and sign == '-' and num2 == 13:
        return("48-13 = 35")
    if num1 == 48 and sign == '-' and num2 == 14:
        return("48-14 = 34")
    if num1 == 48 and sign == '-' and num2 == 15:
        return("48-15 = 33")
    if num1 == 48 and sign == '-' and num2 == 16:
        return("48-16 = 32")
    if num1 == 48 and sign == '-' and num2 == 17:
        return("48-17 = 31")
    if num1 == 48 and sign == '-' and num2 == 18:
        return("48-18 = 30")
    if num1 == 48 and sign == '-' and num2 == 19:
        return("48-19 = 29")
    if num1 == 48 and sign == '-' and num2 == 20:
        return("48-20 = 28")
    if num1 == 48 and sign == '-' and num2 == 21:
        return("48-21 = 27")
    if num1 == 48 and sign == '-' and num2 == 22:
        return("48-22 = 26")
    if num1 == 48 and sign == '-' and num2 == 23:
        return("48-23 = 25")
    if num1 == 48 and sign == '-' and num2 == 24:
        return("48-24 = 24")
    if num1 == 48 and sign == '-' and num2 == 25:
        return("48-25 = 23")
    if num1 == 48 and sign == '-' and num2 == 26:
        return("48-26 = 22")
    if num1 == 48 and sign == '-' and num2 == 27:
        return("48-27 = 21")
    if num1 == 48 and sign == '-' and num2 == 28:
        return("48-28 = 20")
    if num1 == 48 and sign == '-' and num2 == 29:
        return("48-29 = 19")
    if num1 == 48 and sign == '-' and num2 == 30:
        return("48-30 = 18")
    if num1 == 48 and sign == '-' and num2 == 31:
        return("48-31 = 17")
    if num1 == 48 and sign == '-' and num2 == 32:
        return("48-32 = 16")
    if num1 == 48 and sign == '-' and num2 == 33:
        return("48-33 = 15")
    if num1 == 48 and sign == '-' and num2 == 34:
        return("48-34 = 14")
    if num1 == 48 and sign == '-' and num2 == 35:
        return("48-35 = 13")
    if num1 == 48 and sign == '-' and num2 == 36:
        return("48-36 = 12")
    if num1 == 48 and sign == '-' and num2 == 37:
        return("48-37 = 11")
    if num1 == 48 and sign == '-' and num2 == 38:
        return("48-38 = 10")
    if num1 == 48 and sign == '-' and num2 == 39:
        return("48-39 = 9")
    if num1 == 48 and sign == '-' and num2 == 40:
        return("48-40 = 8")
    if num1 == 48 and sign == '-' and num2 == 41:
        return("48-41 = 7")
    if num1 == 48 and sign == '-' and num2 == 42:
        return("48-42 = 6")
    if num1 == 48 and sign == '-' and num2 == 43:
        return("48-43 = 5")
    if num1 == 48 and sign == '-' and num2 == 44:
        return("48-44 = 4")
    if num1 == 48 and sign == '-' and num2 == 45:
        return("48-45 = 3")
    if num1 == 48 and sign == '-' and num2 == 46:
        return("48-46 = 2")
    if num1 == 48 and sign == '-' and num2 == 47:
        return("48-47 = 1")
    if num1 == 48 and sign == '-' and num2 == 48:
        return("48-48 = 0")
    if num1 == 48 and sign == '-' and num2 == 49:
        return("48-49 = -1")
    if num1 == 48 and sign == '-' and num2 == 50:
        return("48-50 = -2")
    if num1 == 49 and sign == '-' and num2 == 0:
        return("49-0 = 49")
    if num1 == 49 and sign == '-' and num2 == 1:
        return("49-1 = 48")
    if num1 == 49 and sign == '-' and num2 == 2:
        return("49-2 = 47")
    if num1 == 49 and sign == '-' and num2 == 3:
        return("49-3 = 46")
    if num1 == 49 and sign == '-' and num2 == 4:
        return("49-4 = 45")
    if num1 == 49 and sign == '-' and num2 == 5:
        return("49-5 = 44")
    if num1 == 49 and sign == '-' and num2 == 6:
        return("49-6 = 43")
    if num1 == 49 and sign == '-' and num2 == 7:
        return("49-7 = 42")
    if num1 == 49 and sign == '-' and num2 == 8:
        return("49-8 = 41")
    if num1 == 49 and sign == '-' and num2 == 9:
        return("49-9 = 40")
    if num1 == 49 and sign == '-' and num2 == 10:
        return("49-10 = 39")
    if num1 == 49 and sign == '-' and num2 == 11:
        return("49-11 = 38")
    if num1 == 49 and sign == '-' and num2 == 12:
        return("49-12 = 37")
    if num1 == 49 and sign == '-' and num2 == 13:
        return("49-13 = 36")
    if num1 == 49 and sign == '-' and num2 == 14:
        return("49-14 = 35")
    if num1 == 49 and sign == '-' and num2 == 15:
        return("49-15 = 34")
    if num1 == 49 and sign == '-' and num2 == 16:
        return("49-16 = 33")
    if num1 == 49 and sign == '-' and num2 == 17:
        return("49-17 = 32")
    if num1 == 49 and sign == '-' and num2 == 18:
        return("49-18 = 31")
    if num1 == 49 and sign == '-' and num2 == 19:
        return("49-19 = 30")
    if num1 == 49 and sign == '-' and num2 == 20:
        return("49-20 = 29")
    if num1 == 49 and sign == '-' and num2 == 21:
        return("49-21 = 28")
    if num1 == 49 and sign == '-' and num2 == 22:
        return("49-22 = 27")
    if num1 == 49 and sign == '-' and num2 == 23:
        return("49-23 = 26")
    if num1 == 49 and sign == '-' and num2 == 24:
        return("49-24 = 25")
    if num1 == 49 and sign == '-' and num2 == 25:
        return("49-25 = 24")
    if num1 == 49 and sign == '-' and num2 == 26:
        return("49-26 = 23")
    if num1 == 49 and sign == '-' and num2 == 27:
        return("49-27 = 22")
    if num1 == 49 and sign == '-' and num2 == 28:
        return("49-28 = 21")
    if num1 == 49 and sign == '-' and num2 == 29:
        return("49-29 = 20")
    if num1 == 49 and sign == '-' and num2 == 30:
        return("49-30 = 19")
    if num1 == 49 and sign == '-' and num2 == 31:
        return("49-31 = 18")
    if num1 == 49 and sign == '-' and num2 == 32:
        return("49-32 = 17")
    if num1 == 49 and sign == '-' and num2 == 33:
        return("49-33 = 16")
    if num1 == 49 and sign == '-' and num2 == 34:
        return("49-34 = 15")
    if num1 == 49 and sign == '-' and num2 == 35:
        return("49-35 = 14")
    if num1 == 49 and sign == '-' and num2 == 36:
        return("49-36 = 13")
    if num1 == 49 and sign == '-' and num2 == 37:
        return("49-37 = 12")
    if num1 == 49 and sign == '-' and num2 == 38:
        return("49-38 = 11")
    if num1 == 49 and sign == '-' and num2 == 39:
        return("49-39 = 10")
    if num1 == 49 and sign == '-' and num2 == 40:
        return("49-40 = 9")
    if num1 == 49 and sign == '-' and num2 == 41:
        return("49-41 = 8")
    if num1 == 49 and sign == '-' and num2 == 42:
        return("49-42 = 7")
    if num1 == 49 and sign == '-' and num2 == 43:
        return("49-43 = 6")
    if num1 == 49 and sign == '-' and num2 == 44:
        return("49-44 = 5")
    if num1 == 49 and sign == '-' and num2 == 45:
        return("49-45 = 4")
    if num1 == 49 and sign == '-' and num2 == 46:
        return("49-46 = 3")
    if num1 == 49 and sign == '-' and num2 == 47:
        return("49-47 = 2")
    if num1 == 49 and sign == '-' and num2 == 48:
        return("49-48 = 1")
    if num1 == 49 and sign == '-' and num2 == 49:
        return("49-49 = 0")
    if num1 == 49 and sign == '-' and num2 == 50:
        return("49-50 = -1")
    if num1 == 50 and sign == '-' and num2 == 0:
        return("50-0 = 50")
    if num1 == 50 and sign == '-' and num2 == 1:
        return("50-1 = 49")
    if num1 == 50 and sign == '-' and num2 == 2:
        return("50-2 = 48")
    if num1 == 50 and sign == '-' and num2 == 3:
        return("50-3 = 47")
    if num1 == 50 and sign == '-' and num2 == 4:
        return("50-4 = 46")
    if num1 == 50 and sign == '-' and num2 == 5:
        return("50-5 = 45")
    if num1 == 50 and sign == '-' and num2 == 6:
        return("50-6 = 44")
    if num1 == 50 and sign == '-' and num2 == 7:
        return("50-7 = 43")
    if num1 == 50 and sign == '-' and num2 == 8:
        return("50-8 = 42")
    if num1 == 50 and sign == '-' and num2 == 9:
        return("50-9 = 41")
    if num1 == 50 and sign == '-' and num2 == 10:
        return("50-10 = 40")
    if num1 == 50 and sign == '-' and num2 == 11:
        return("50-11 = 39")
    if num1 == 50 and sign == '-' and num2 == 12:
        return("50-12 = 38")
    if num1 == 50 and sign == '-' and num2 == 13:
        return("50-13 = 37")
    if num1 == 50 and sign == '-' and num2 == 14:
        return("50-14 = 36")
    if num1 == 50 and sign == '-' and num2 == 15:
        return("50-15 = 35")
    if num1 == 50 and sign == '-' and num2 == 16:
        return("50-16 = 34")
    if num1 == 50 and sign == '-' and num2 == 17:
        return("50-17 = 33")
    if num1 == 50 and sign == '-' and num2 == 18:
        return("50-18 = 32")
    if num1 == 50 and sign == '-' and num2 == 19:
        return("50-19 = 31")
    if num1 == 50 and sign == '-' and num2 == 20:
        return("50-20 = 30")
    if num1 == 50 and sign == '-' and num2 == 21:
        return("50-21 = 29")
    if num1 == 50 and sign == '-' and num2 == 22:
        return("50-22 = 28")
    if num1 == 50 and sign == '-' and num2 == 23:
        return("50-23 = 27")
    if num1 == 50 and sign == '-' and num2 == 24:
        return("50-24 = 26")
    if num1 == 50 and sign == '-' and num2 == 25:
        return("50-25 = 25")
    if num1 == 50 and sign == '-' and num2 == 26:
        return("50-26 = 24")
    if num1 == 50 and sign == '-' and num2 == 27:
        return("50-27 = 23")
    if num1 == 50 and sign == '-' and num2 == 28:
        return("50-28 = 22")
    if num1 == 50 and sign == '-' and num2 == 29:
        return("50-29 = 21")
    if num1 == 50 and sign == '-' and num2 == 30:
        return("50-30 = 20")
    if num1 == 50 and sign == '-' and num2 == 31:
        return("50-31 = 19")
    if num1 == 50 and sign == '-' and num2 == 32:
        return("50-32 = 18")
    if num1 == 50 and sign == '-' and num2 == 33:
        return("50-33 = 17")
    if num1 == 50 and sign == '-' and num2 == 34:
        return("50-34 = 16")
    if num1 == 50 and sign == '-' and num2 == 35:
        return("50-35 = 15")
    if num1 == 50 and sign == '-' and num2 == 36:
        return("50-36 = 14")
    if num1 == 50 and sign == '-' and num2 == 37:
        return("50-37 = 13")
    if num1 == 50 and sign == '-' and num2 == 38:
        return("50-38 = 12")
    if num1 == 50 and sign == '-' and num2 == 39:
        return("50-39 = 11")
    if num1 == 50 and sign == '-' and num2 == 40:
        return("50-40 = 10")
    if num1 == 50 and sign == '-' and num2 == 41:
        return("50-41 = 9")
    if num1 == 50 and sign == '-' and num2 == 42:
        return("50-42 = 8")
    if num1 == 50 and sign == '-' and num2 == 43:
        return("50-43 = 7")
    if num1 == 50 and sign == '-' and num2 == 44:
        return("50-44 = 6")
    if num1 == 50 and sign == '-' and num2 == 45:
        return("50-45 = 5")
    if num1 == 50 and sign == '-' and num2 == 46:
        return("50-46 = 4")
    if num1 == 50 and sign == '-' and num2 == 47:
        return("50-47 = 3")
    if num1 == 50 and sign == '-' and num2 == 48:
        return("50-48 = 2")
    if num1 == 50 and sign == '-' and num2 == 49:
        return("50-49 = 1")
    if num1 == 50 and sign == '-' and num2 == 50:
        return("50-50 = 0")
    if num1 == 0 and sign == '/' and num2 == 0:
        return("0/0 = Undefined")
    if num1 == 0 and sign == '/' and num2 == 1:
        return("0/1 = 0")
    if num1 == 0 and sign == '/' and num2 == 2:
        return("0/2 = 0")
    if num1 == 0 and sign == '/' and num2 == 3:
        return("0/3 = 0")
    if num1 == 0 and sign == '/' and num2 == 4:
        return("0/4 = 0")
    if num1 == 0 and sign == '/' and num2 == 5:
        return("0/5 = 0")
    if num1 == 0 and sign == '/' and num2 == 6:
        return("0/6 = 0")
    if num1 == 0 and sign == '/' and num2 == 7:
        return("0/7 = 0")
    if num1 == 0 and sign == '/' and num2 == 8:
        return("0/8 = 0")
    if num1 == 0 and sign == '/' and num2 == 9:
        return("0/9 = 0")
    if num1 == 0 and sign == '/' and num2 == 10:
        return("0/10 = 0")
    if num1 == 0 and sign == '/' and num2 == 11:
        return("0/11 = 0")
    if num1 == 0 and sign == '/' and num2 == 12:
        return("0/12 = 0")
    if num1 == 0 and sign == '/' and num2 == 13:
        return("0/13 = 0")
    if num1 == 0 and sign == '/' and num2 == 14:
        return("0/14 = 0")
    if num1 == 0 and sign == '/' and num2 == 15:
        return("0/15 = 0")
    if num1 == 0 and sign == '/' and num2 == 16:
        return("0/16 = 0")
    if num1 == 0 and sign == '/' and num2 == 17:
        return("0/17 = 0")
    if num1 == 0 and sign == '/' and num2 == 18:
        return("0/18 = 0")
    if num1 == 0 and sign == '/' and num2 == 19:
        return("0/19 = 0")
    if num1 == 0 and sign == '/' and num2 == 20:
        return("0/20 = 0")
    if num1 == 0 and sign == '/' and num2 == 21:
        return("0/21 = 0")
    if num1 == 0 and sign == '/' and num2 == 22:
        return("0/22 = 0")
    if num1 == 0 and sign == '/' and num2 == 23:
        return("0/23 = 0")
    if num1 == 0 and sign == '/' and num2 == 24:
        return("0/24 = 0")
    if num1 == 0 and sign == '/' and num2 == 25:
        return("0/25 = 0")
    if num1 == 0 and sign == '/' and num2 == 26:
        return("0/26 = 0")
    if num1 == 0 and sign == '/' and num2 == 27:
        return("0/27 = 0")
    if num1 == 0 and sign == '/' and num2 == 28:
        return("0/28 = 0")
    if num1 == 0 and sign == '/' and num2 == 29:
        return("0/29 = 0")
    if num1 == 0 and sign == '/' and num2 == 30:
        return("0/30 = 0")
    if num1 == 0 and sign == '/' and num2 == 31:
        return("0/31 = 0")
    if num1 == 0 and sign == '/' and num2 == 32:
        return("0/32 = 0")
    if num1 == 0 and sign == '/' and num2 == 33:
        return("0/33 = 0")
    if num1 == 0 and sign == '/' and num2 == 34:
        return("0/34 = 0")
    if num1 == 0 and sign == '/' and num2 == 35:
        return("0/35 = 0")
    if num1 == 0 and sign == '/' and num2 == 36:
        return("0/36 = 0")
    if num1 == 0 and sign == '/' and num2 == 37:
        return("0/37 = 0")
    if num1 == 0 and sign == '/' and num2 == 38:
        return("0/38 = 0")
    if num1 == 0 and sign == '/' and num2 == 39:
        return("0/39 = 0")
    if num1 == 0 and sign == '/' and num2 == 40:
        return("0/40 = 0")
    if num1 == 0 and sign == '/' and num2 == 41:
        return("0/41 = 0")
    if num1 == 0 and sign == '/' and num2 == 42:
        return("0/42 = 0")
    if num1 == 0 and sign == '/' and num2 == 43:
        return("0/43 = 0")
    if num1 == 0 and sign == '/' and num2 == 44:
        return("0/44 = 0")
    if num1 == 0 and sign == '/' and num2 == 45:
        return("0/45 = 0")
    if num1 == 0 and sign == '/' and num2 == 46:
        return("0/46 = 0")
    if num1 == 0 and sign == '/' and num2 == 47:
        return("0/47 = 0")
    if num1 == 0 and sign == '/' and num2 == 48:
        return("0/48 = 0")
    if num1 == 0 and sign == '/' and num2 == 49:
        return("0/49 = 0")
    if num1 == 0 and sign == '/' and num2 == 50:
        return("0/50 = 0")
    if num1 == 1 and sign == '/' and num2 == 0:
        return("1/0 = Inf")
    if num1 == 1 and sign == '/' and num2 == 1:
        return("1/1 = 1")
    if num1 == 1 and sign == '/' and num2 == 2:
        return("1/2 = 0.5")
    if num1 == 1 and sign == '/' and num2 == 3:
        return("1/3 = 0.3333333333333333333333333333")
    if num1 == 1 and sign == '/' and num2 == 4:
        return("1/4 = 0.25")
    if num1 == 1 and sign == '/' and num2 == 5:
        return("1/5 = 0.2")
    if num1 == 1 and sign == '/' and num2 == 6:
        return("1/6 = 0.1666666666666666666666666667")
    if num1 == 1 and sign == '/' and num2 == 7:
        return("1/7 = 0.1428571428571428571428571429")
    if num1 == 1 and sign == '/' and num2 == 8:
        return("1/8 = 0.125")
    if num1 == 1 and sign == '/' and num2 == 9:
        return("1/9 = 0.1111111111111111111111111111")
    if num1 == 1 and sign == '/' and num2 == 10:
        return("1/10 = 0.1")
    if num1 == 1 and sign == '/' and num2 == 11:
        return("1/11 = 0.09090909090909090909090909091")
    if num1 == 1 and sign == '/' and num2 == 12:
        return("1/12 = 0.08333333333333333333333333333")
    if num1 == 1 and sign == '/' and num2 == 13:
        return("1/13 = 0.07692307692307692307692307692")
    if num1 == 1 and sign == '/' and num2 == 14:
        return("1/14 = 0.07142857142857142857142857143")
    if num1 == 1 and sign == '/' and num2 == 15:
        return("1/15 = 0.06666666666666666666666666667")
    if num1 == 1 and sign == '/' and num2 == 16:
        return("1/16 = 0.0625")
    if num1 == 1 and sign == '/' and num2 == 17:
        return("1/17 = 0.05882352941176470588235294118")
    if num1 == 1 and sign == '/' and num2 == 18:
        return("1/18 = 0.05555555555555555555555555556")
    if num1 == 1 and sign == '/' and num2 == 19:
        return("1/19 = 0.05263157894736842105263157895")
    if num1 == 1 and sign == '/' and num2 == 20:
        return("1/20 = 0.05")
    if num1 == 1 and sign == '/' and num2 == 21:
        return("1/21 = 0.04761904761904761904761904762")
    if num1 == 1 and sign == '/' and num2 == 22:
        return("1/22 = 0.04545454545454545454545454545")
    if num1 == 1 and sign == '/' and num2 == 23:
        return("1/23 = 0.04347826086956521739130434783")
    if num1 == 1 and sign == '/' and num2 == 24:
        return("1/24 = 0.04166666666666666666666666667")
    if num1 == 1 and sign == '/' and num2 == 25:
        return("1/25 = 0.04")
    if num1 == 1 and sign == '/' and num2 == 26:
        return("1/26 = 0.03846153846153846153846153846")
    if num1 == 1 and sign == '/' and num2 == 27:
        return("1/27 = 0.03703703703703703703703703704")
    if num1 == 1 and sign == '/' and num2 == 28:
        return("1/28 = 0.03571428571428571428571428571")
    if num1 == 1 and sign == '/' and num2 == 29:
        return("1/29 = 0.03448275862068965517241379310")
    if num1 == 1 and sign == '/' and num2 == 30:
        return("1/30 = 0.03333333333333333333333333333")
    if num1 == 1 and sign == '/' and num2 == 31:
        return("1/31 = 0.03225806451612903225806451613")
    if num1 == 1 and sign == '/' and num2 == 32:
        return("1/32 = 0.03125")
    if num1 == 1 and sign == '/' and num2 == 33:
        return("1/33 = 0.03030303030303030303030303030")
    if num1 == 1 and sign == '/' and num2 == 34:
        return("1/34 = 0.02941176470588235294117647059")
    if num1 == 1 and sign == '/' and num2 == 35:
        return("1/35 = 0.02857142857142857142857142857")
    if num1 == 1 and sign == '/' and num2 == 36:
        return("1/36 = 0.02777777777777777777777777778")
    if num1 == 1 and sign == '/' and num2 == 37:
        return("1/37 = 0.02702702702702702702702702703")
    if num1 == 1 and sign == '/' and num2 == 38:
        return("1/38 = 0.02631578947368421052631578947")
    if num1 == 1 and sign == '/' and num2 == 39:
        return("1/39 = 0.02564102564102564102564102564")
    if num1 == 1 and sign == '/' and num2 == 40:
        return("1/40 = 0.025")
    if num1 == 1 and sign == '/' and num2 == 41:
        return("1/41 = 0.02439024390243902439024390244")
    if num1 == 1 and sign == '/' and num2 == 42:
        return("1/42 = 0.02380952380952380952380952381")
    if num1 == 1 and sign == '/' and num2 == 43:
        return("1/43 = 0.02325581395348837209302325581")
    if num1 == 1 and sign == '/' and num2 == 44:
        return("1/44 = 0.02272727272727272727272727273")
    if num1 == 1 and sign == '/' and num2 == 45:
        return("1/45 = 0.02222222222222222222222222222")
    if num1 == 1 and sign == '/' and num2 == 46:
        return("1/46 = 0.02173913043478260869565217391")
    if num1 == 1 and sign == '/' and num2 == 47:
        return("1/47 = 0.02127659574468085106382978723")
    if num1 == 1 and sign == '/' and num2 == 48:
        return("1/48 = 0.02083333333333333333333333333")
    if num1 == 1 and sign == '/' and num2 == 49:
        return("1/49 = 0.02040816326530612244897959184")
    if num1 == 1 and sign == '/' and num2 == 50:
        return("1/50 = 0.02")
    if num1 == 2 and sign == '/' and num2 == 0:
        return("2/0 = Inf")
    if num1 == 2 and sign == '/' and num2 == 1:
        return("2/1 = 2")
    if num1 == 2 and sign == '/' and num2 == 2:
        return("2/2 = 1")
    if num1 == 2 and sign == '/' and num2 == 3:
        return("2/3 = 0.6666666666666666666666666667")
    if num1 == 2 and sign == '/' and num2 == 4:
        return("2/4 = 0.5")
    if num1 == 2 and sign == '/' and num2 == 5:
        return("2/5 = 0.4")
    if num1 == 2 and sign == '/' and num2 == 6:
        return("2/6 = 0.3333333333333333333333333333")
    if num1 == 2 and sign == '/' and num2 == 7:
        return("2/7 = 0.2857142857142857142857142857")
    if num1 == 2 and sign == '/' and num2 == 8:
        return("2/8 = 0.25")
    if num1 == 2 and sign == '/' and num2 == 9:
        return("2/9 = 0.2222222222222222222222222222")
    if num1 == 2 and sign == '/' and num2 == 10:
        return("2/10 = 0.2")
    if num1 == 2 and sign == '/' and num2 == 11:
        return("2/11 = 0.1818181818181818181818181818")
    if num1 == 2 and sign == '/' and num2 == 12:
        return("2/12 = 0.1666666666666666666666666667")
    if num1 == 2 and sign == '/' and num2 == 13:
        return("2/13 = 0.1538461538461538461538461538")
    if num1 == 2 and sign == '/' and num2 == 14:
        return("2/14 = 0.1428571428571428571428571429")
    if num1 == 2 and sign == '/' and num2 == 15:
        return("2/15 = 0.1333333333333333333333333333")
    if num1 == 2 and sign == '/' and num2 == 16:
        return("2/16 = 0.125")
    if num1 == 2 and sign == '/' and num2 == 17:
        return("2/17 = 0.1176470588235294117647058824")
    if num1 == 2 and sign == '/' and num2 == 18:
        return("2/18 = 0.1111111111111111111111111111")
    if num1 == 2 and sign == '/' and num2 == 19:
        return("2/19 = 0.1052631578947368421052631579")
    if num1 == 2 and sign == '/' and num2 == 20:
        return("2/20 = 0.1")
    if num1 == 2 and sign == '/' and num2 == 21:
        return("2/21 = 0.09523809523809523809523809524")
    if num1 == 2 and sign == '/' and num2 == 22:
        return("2/22 = 0.09090909090909090909090909091")
    if num1 == 2 and sign == '/' and num2 == 23:
        return("2/23 = 0.08695652173913043478260869565")
    if num1 == 2 and sign == '/' and num2 == 24:
        return("2/24 = 0.08333333333333333333333333333")
    if num1 == 2 and sign == '/' and num2 == 25:
        return("2/25 = 0.08")
    if num1 == 2 and sign == '/' and num2 == 26:
        return("2/26 = 0.07692307692307692307692307692")
    if num1 == 2 and sign == '/' and num2 == 27:
        return("2/27 = 0.07407407407407407407407407407")
    if num1 == 2 and sign == '/' and num2 == 28:
        return("2/28 = 0.07142857142857142857142857143")
    if num1 == 2 and sign == '/' and num2 == 29:
        return("2/29 = 0.06896551724137931034482758621")
    if num1 == 2 and sign == '/' and num2 == 30:
        return("2/30 = 0.06666666666666666666666666667")
    if num1 == 2 and sign == '/' and num2 == 31:
        return("2/31 = 0.06451612903225806451612903226")
    if num1 == 2 and sign == '/' and num2 == 32:
        return("2/32 = 0.0625")
    if num1 == 2 and sign == '/' and num2 == 33:
        return("2/33 = 0.06060606060606060606060606061")
    if num1 == 2 and sign == '/' and num2 == 34:
        return("2/34 = 0.05882352941176470588235294118")
    if num1 == 2 and sign == '/' and num2 == 35:
        return("2/35 = 0.05714285714285714285714285714")
    if num1 == 2 and sign == '/' and num2 == 36:
        return("2/36 = 0.05555555555555555555555555556")
    if num1 == 2 and sign == '/' and num2 == 37:
        return("2/37 = 0.05405405405405405405405405405")
    if num1 == 2 and sign == '/' and num2 == 38:
        return("2/38 = 0.05263157894736842105263157895")
    if num1 == 2 and sign == '/' and num2 == 39:
        return("2/39 = 0.05128205128205128205128205128")
    if num1 == 2 and sign == '/' and num2 == 40:
        return("2/40 = 0.05")
    if num1 == 2 and sign == '/' and num2 == 41:
        return("2/41 = 0.04878048780487804878048780488")
    if num1 == 2 and sign == '/' and num2 == 42:
        return("2/42 = 0.04761904761904761904761904762")
    if num1 == 2 and sign == '/' and num2 == 43:
        return("2/43 = 0.04651162790697674418604651163")
    if num1 == 2 and sign == '/' and num2 == 44:
        return("2/44 = 0.04545454545454545454545454545")
    if num1 == 2 and sign == '/' and num2 == 45:
        return("2/45 = 0.04444444444444444444444444444")
    if num1 == 2 and sign == '/' and num2 == 46:
        return("2/46 = 0.04347826086956521739130434783")
    if num1 == 2 and sign == '/' and num2 == 47:
        return("2/47 = 0.04255319148936170212765957447")
    if num1 == 2 and sign == '/' and num2 == 48:
        return("2/48 = 0.04166666666666666666666666667")
    if num1 == 2 and sign == '/' and num2 == 49:
        return("2/49 = 0.04081632653061224489795918367")
    if num1 == 2 and sign == '/' and num2 == 50:
        return("2/50 = 0.04")
    if num1 == 3 and sign == '/' and num2 == 0:
        return("3/0 = Inf")
    if num1 == 3 and sign == '/' and num2 == 1:
        return("3/1 = 3")
    if num1 == 3 and sign == '/' and num2 == 2:
        return("3/2 = 1.5")
    if num1 == 3 and sign == '/' and num2 == 3:
        return("3/3 = 1")
    if num1 == 3 and sign == '/' and num2 == 4:
        return("3/4 = 0.75")
    if num1 == 3 and sign == '/' and num2 == 5:
        return("3/5 = 0.6")
    if num1 == 3 and sign == '/' and num2 == 6:
        return("3/6 = 0.5")
    if num1 == 3 and sign == '/' and num2 == 7:
        return("3/7 = 0.4285714285714285714285714286")
    if num1 == 3 and sign == '/' and num2 == 8:
        return("3/8 = 0.375")
    if num1 == 3 and sign == '/' and num2 == 9:
        return("3/9 = 0.3333333333333333333333333333")
    if num1 == 3 and sign == '/' and num2 == 10:
        return("3/10 = 0.3")
    if num1 == 3 and sign == '/' and num2 == 11:
        return("3/11 = 0.2727272727272727272727272727")
    if num1 == 3 and sign == '/' and num2 == 12:
        return("3/12 = 0.25")
    if num1 == 3 and sign == '/' and num2 == 13:
        return("3/13 = 0.2307692307692307692307692308")
    if num1 == 3 and sign == '/' and num2 == 14:
        return("3/14 = 0.2142857142857142857142857143")
    if num1 == 3 and sign == '/' and num2 == 15:
        return("3/15 = 0.2")
    if num1 == 3 and sign == '/' and num2 == 16:
        return("3/16 = 0.1875")
    if num1 == 3 and sign == '/' and num2 == 17:
        return("3/17 = 0.1764705882352941176470588235")
    if num1 == 3 and sign == '/' and num2 == 18:
        return("3/18 = 0.1666666666666666666666666667")
    if num1 == 3 and sign == '/' and num2 == 19:
        return("3/19 = 0.1578947368421052631578947368")
    if num1 == 3 and sign == '/' and num2 == 20:
        return("3/20 = 0.15")
    if num1 == 3 and sign == '/' and num2 == 21:
        return("3/21 = 0.1428571428571428571428571429")
    if num1 == 3 and sign == '/' and num2 == 22:
        return("3/22 = 0.1363636363636363636363636364")
    if num1 == 3 and sign == '/' and num2 == 23:
        return("3/23 = 0.1304347826086956521739130435")
    if num1 == 3 and sign == '/' and num2 == 24:
        return("3/24 = 0.125")
    if num1 == 3 and sign == '/' and num2 == 25:
        return("3/25 = 0.12")
    if num1 == 3 and sign == '/' and num2 == 26:
        return("3/26 = 0.1153846153846153846153846154")
    if num1 == 3 and sign == '/' and num2 == 27:
        return("3/27 = 0.1111111111111111111111111111")
    if num1 == 3 and sign == '/' and num2 == 28:
        return("3/28 = 0.1071428571428571428571428571")
    if num1 == 3 and sign == '/' and num2 == 29:
        return("3/29 = 0.1034482758620689655172413793")
    if num1 == 3 and sign == '/' and num2 == 30:
        return("3/30 = 0.1")
    if num1 == 3 and sign == '/' and num2 == 31:
        return("3/31 = 0.09677419354838709677419354839")
    if num1 == 3 and sign == '/' and num2 == 32:
        return("3/32 = 0.09375")
    if num1 == 3 and sign == '/' and num2 == 33:
        return("3/33 = 0.09090909090909090909090909091")
    if num1 == 3 and sign == '/' and num2 == 34:
        return("3/34 = 0.08823529411764705882352941176")
    if num1 == 3 and sign == '/' and num2 == 35:
        return("3/35 = 0.08571428571428571428571428571")
    if num1 == 3 and sign == '/' and num2 == 36:
        return("3/36 = 0.08333333333333333333333333333")
    if num1 == 3 and sign == '/' and num2 == 37:
        return("3/37 = 0.08108108108108108108108108108")
    if num1 == 3 and sign == '/' and num2 == 38:
        return("3/38 = 0.07894736842105263157894736842")
    if num1 == 3 and sign == '/' and num2 == 39:
        return("3/39 = 0.07692307692307692307692307692")
    if num1 == 3 and sign == '/' and num2 == 40:
        return("3/40 = 0.075")
    if num1 == 3 and sign == '/' and num2 == 41:
        return("3/41 = 0.07317073170731707317073170732")
    if num1 == 3 and sign == '/' and num2 == 42:
        return("3/42 = 0.07142857142857142857142857143")
    if num1 == 3 and sign == '/' and num2 == 43:
        return("3/43 = 0.06976744186046511627906976744")
    if num1 == 3 and sign == '/' and num2 == 44:
        return("3/44 = 0.06818181818181818181818181818")
    if num1 == 3 and sign == '/' and num2 == 45:
        return("3/45 = 0.06666666666666666666666666667")
    if num1 == 3 and sign == '/' and num2 == 46:
        return("3/46 = 0.06521739130434782608695652174")
    if num1 == 3 and sign == '/' and num2 == 47:
        return("3/47 = 0.06382978723404255319148936170")
    if num1 == 3 and sign == '/' and num2 == 48:
        return("3/48 = 0.0625")
    if num1 == 3 and sign == '/' and num2 == 49:
        return("3/49 = 0.06122448979591836734693877551")
    if num1 == 3 and sign == '/' and num2 == 50:
        return("3/50 = 0.06")
    if num1 == 4 and sign == '/' and num2 == 0:
        return("4/0 = Inf")
    if num1 == 4 and sign == '/' and num2 == 1:
        return("4/1 = 4")
    if num1 == 4 and sign == '/' and num2 == 2:
        return("4/2 = 2")
    if num1 == 4 and sign == '/' and num2 == 3:
        return("4/3 = 1.333333333333333333333333333")
    if num1 == 4 and sign == '/' and num2 == 4:
        return("4/4 = 1")
    if num1 == 4 and sign == '/' and num2 == 5:
        return("4/5 = 0.8")
    if num1 == 4 and sign == '/' and num2 == 6:
        return("4/6 = 0.6666666666666666666666666667")
    if num1 == 4 and sign == '/' and num2 == 7:
        return("4/7 = 0.5714285714285714285714285714")
    if num1 == 4 and sign == '/' and num2 == 8:
        return("4/8 = 0.5")
    if num1 == 4 and sign == '/' and num2 == 9:
        return("4/9 = 0.4444444444444444444444444444")
    if num1 == 4 and sign == '/' and num2 == 10:
        return("4/10 = 0.4")
    if num1 == 4 and sign == '/' and num2 == 11:
        return("4/11 = 0.3636363636363636363636363636")
    if num1 == 4 and sign == '/' and num2 == 12:
        return("4/12 = 0.3333333333333333333333333333")
    if num1 == 4 and sign == '/' and num2 == 13:
        return("4/13 = 0.3076923076923076923076923077")
    if num1 == 4 and sign == '/' and num2 == 14:
        return("4/14 = 0.2857142857142857142857142857")
    if num1 == 4 and sign == '/' and num2 == 15:
        return("4/15 = 0.2666666666666666666666666667")
    if num1 == 4 and sign == '/' and num2 == 16:
        return("4/16 = 0.25")
    if num1 == 4 and sign == '/' and num2 == 17:
        return("4/17 = 0.2352941176470588235294117647")
    if num1 == 4 and sign == '/' and num2 == 18:
        return("4/18 = 0.2222222222222222222222222222")
    if num1 == 4 and sign == '/' and num2 == 19:
        return("4/19 = 0.2105263157894736842105263158")
    if num1 == 4 and sign == '/' and num2 == 20:
        return("4/20 = 0.2")
    if num1 == 4 and sign == '/' and num2 == 21:
        return("4/21 = 0.1904761904761904761904761905")
    if num1 == 4 and sign == '/' and num2 == 22:
        return("4/22 = 0.1818181818181818181818181818")
    if num1 == 4 and sign == '/' and num2 == 23:
        return("4/23 = 0.1739130434782608695652173913")
    if num1 == 4 and sign == '/' and num2 == 24:
        return("4/24 = 0.1666666666666666666666666667")
    if num1 == 4 and sign == '/' and num2 == 25:
        return("4/25 = 0.16")
    if num1 == 4 and sign == '/' and num2 == 26:
        return("4/26 = 0.1538461538461538461538461538")
    if num1 == 4 and sign == '/' and num2 == 27:
        return("4/27 = 0.1481481481481481481481481481")
    if num1 == 4 and sign == '/' and num2 == 28:
        return("4/28 = 0.1428571428571428571428571429")
    if num1 == 4 and sign == '/' and num2 == 29:
        return("4/29 = 0.1379310344827586206896551724")
    if num1 == 4 and sign == '/' and num2 == 30:
        return("4/30 = 0.1333333333333333333333333333")
    if num1 == 4 and sign == '/' and num2 == 31:
        return("4/31 = 0.1290322580645161290322580645")
    if num1 == 4 and sign == '/' and num2 == 32:
        return("4/32 = 0.125")
    if num1 == 4 and sign == '/' and num2 == 33:
        return("4/33 = 0.1212121212121212121212121212")
    if num1 == 4 and sign == '/' and num2 == 34:
        return("4/34 = 0.1176470588235294117647058824")
    if num1 == 4 and sign == '/' and num2 == 35:
        return("4/35 = 0.1142857142857142857142857143")
    if num1 == 4 and sign == '/' and num2 == 36:
        return("4/36 = 0.1111111111111111111111111111")
    if num1 == 4 and sign == '/' and num2 == 37:
        return("4/37 = 0.1081081081081081081081081081")
    if num1 == 4 and sign == '/' and num2 == 38:
        return("4/38 = 0.1052631578947368421052631579")
    if num1 == 4 and sign == '/' and num2 == 39:
        return("4/39 = 0.1025641025641025641025641026")
    if num1 == 4 and sign == '/' and num2 == 40:
        return("4/40 = 0.1")
    if num1 == 4 and sign == '/' and num2 == 41:
        return("4/41 = 0.09756097560975609756097560976")
    if num1 == 4 and sign == '/' and num2 == 42:
        return("4/42 = 0.09523809523809523809523809524")
    if num1 == 4 and sign == '/' and num2 == 43:
        return("4/43 = 0.09302325581395348837209302326")
    if num1 == 4 and sign == '/' and num2 == 44:
        return("4/44 = 0.09090909090909090909090909091")
    if num1 == 4 and sign == '/' and num2 == 45:
        return("4/45 = 0.08888888888888888888888888889")
    if num1 == 4 and sign == '/' and num2 == 46:
        return("4/46 = 0.08695652173913043478260869565")
    if num1 == 4 and sign == '/' and num2 == 47:
        return("4/47 = 0.08510638297872340425531914894")
    if num1 == 4 and sign == '/' and num2 == 48:
        return("4/48 = 0.08333333333333333333333333333")
    if num1 == 4 and sign == '/' and num2 == 49:
        return("4/49 = 0.08163265306122448979591836735")
    if num1 == 4 and sign == '/' and num2 == 50:
        return("4/50 = 0.08")
    if num1 == 5 and sign == '/' and num2 == 0:
        return("5/0 = Inf")
    if num1 == 5 and sign == '/' and num2 == 1:
        return("5/1 = 5")
    if num1 == 5 and sign == '/' and num2 == 2:
        return("5/2 = 2.5")
    if num1 == 5 and sign == '/' and num2 == 3:
        return("5/3 = 1.666666666666666666666666667")
    if num1 == 5 and sign == '/' and num2 == 4:
        return("5/4 = 1.25")
    if num1 == 5 and sign == '/' and num2 == 5:
        return("5/5 = 1")
    if num1 == 5 and sign == '/' and num2 == 6:
        return("5/6 = 0.8333333333333333333333333333")
    if num1 == 5 and sign == '/' and num2 == 7:
        return("5/7 = 0.7142857142857142857142857143")
    if num1 == 5 and sign == '/' and num2 == 8:
        return("5/8 = 0.625")
    if num1 == 5 and sign == '/' and num2 == 9:
        return("5/9 = 0.5555555555555555555555555556")
    if num1 == 5 and sign == '/' and num2 == 10:
        return("5/10 = 0.5")
    if num1 == 5 and sign == '/' and num2 == 11:
        return("5/11 = 0.4545454545454545454545454545")
    if num1 == 5 and sign == '/' and num2 == 12:
        return("5/12 = 0.4166666666666666666666666667")
    if num1 == 5 and sign == '/' and num2 == 13:
        return("5/13 = 0.3846153846153846153846153846")
    if num1 == 5 and sign == '/' and num2 == 14:
        return("5/14 = 0.3571428571428571428571428571")
    if num1 == 5 and sign == '/' and num2 == 15:
        return("5/15 = 0.3333333333333333333333333333")
    if num1 == 5 and sign == '/' and num2 == 16:
        return("5/16 = 0.3125")
    if num1 == 5 and sign == '/' and num2 == 17:
        return("5/17 = 0.2941176470588235294117647059")
    if num1 == 5 and sign == '/' and num2 == 18:
        return("5/18 = 0.2777777777777777777777777778")
    if num1 == 5 and sign == '/' and num2 == 19:
        return("5/19 = 0.2631578947368421052631578947")
    if num1 == 5 and sign == '/' and num2 == 20:
        return("5/20 = 0.25")
    if num1 == 5 and sign == '/' and num2 == 21:
        return("5/21 = 0.2380952380952380952380952381")
    if num1 == 5 and sign == '/' and num2 == 22:
        return("5/22 = 0.2272727272727272727272727273")
    if num1 == 5 and sign == '/' and num2 == 23:
        return("5/23 = 0.2173913043478260869565217391")
    if num1 == 5 and sign == '/' and num2 == 24:
        return("5/24 = 0.2083333333333333333333333333")
    if num1 == 5 and sign == '/' and num2 == 25:
        return("5/25 = 0.2")
    if num1 == 5 and sign == '/' and num2 == 26:
        return("5/26 = 0.1923076923076923076923076923")
    if num1 == 5 and sign == '/' and num2 == 27:
        return("5/27 = 0.1851851851851851851851851852")
    if num1 == 5 and sign == '/' and num2 == 28:
        return("5/28 = 0.1785714285714285714285714286")
    if num1 == 5 and sign == '/' and num2 == 29:
        return("5/29 = 0.1724137931034482758620689655")
    if num1 == 5 and sign == '/' and num2 == 30:
        return("5/30 = 0.1666666666666666666666666667")
    if num1 == 5 and sign == '/' and num2 == 31:
        return("5/31 = 0.1612903225806451612903225806")
    if num1 == 5 and sign == '/' and num2 == 32:
        return("5/32 = 0.15625")
    if num1 == 5 and sign == '/' and num2 == 33:
        return("5/33 = 0.1515151515151515151515151515")
    if num1 == 5 and sign == '/' and num2 == 34:
        return("5/34 = 0.1470588235294117647058823529")
    if num1 == 5 and sign == '/' and num2 == 35:
        return("5/35 = 0.1428571428571428571428571429")
    if num1 == 5 and sign == '/' and num2 == 36:
        return("5/36 = 0.1388888888888888888888888889")
    if num1 == 5 and sign == '/' and num2 == 37:
        return("5/37 = 0.1351351351351351351351351351")
    if num1 == 5 and sign == '/' and num2 == 38:
        return("5/38 = 0.1315789473684210526315789474")
    if num1 == 5 and sign == '/' and num2 == 39:
        return("5/39 = 0.1282051282051282051282051282")
    if num1 == 5 and sign == '/' and num2 == 40:
        return("5/40 = 0.125")
    if num1 == 5 and sign == '/' and num2 == 41:
        return("5/41 = 0.1219512195121951219512195122")
    if num1 == 5 and sign == '/' and num2 == 42:
        return("5/42 = 0.1190476190476190476190476190")
    if num1 == 5 and sign == '/' and num2 == 43:
        return("5/43 = 0.1162790697674418604651162791")
    if num1 == 5 and sign == '/' and num2 == 44:
        return("5/44 = 0.1136363636363636363636363636")
    if num1 == 5 and sign == '/' and num2 == 45:
        return("5/45 = 0.1111111111111111111111111111")
    if num1 == 5 and sign == '/' and num2 == 46:
        return("5/46 = 0.1086956521739130434782608696")
    if num1 == 5 and sign == '/' and num2 == 47:
        return("5/47 = 0.1063829787234042553191489362")
    if num1 == 5 and sign == '/' and num2 == 48:
        return("5/48 = 0.1041666666666666666666666667")
    if num1 == 5 and sign == '/' and num2 == 49:
        return("5/49 = 0.1020408163265306122448979592")
    if num1 == 5 and sign == '/' and num2 == 50:
        return("5/50 = 0.1")
    if num1 == 6 and sign == '/' and num2 == 0:
        return("6/0 = Inf")
    if num1 == 6 and sign == '/' and num2 == 1:
        return("6/1 = 6")
    if num1 == 6 and sign == '/' and num2 == 2:
        return("6/2 = 3")
    if num1 == 6 and sign == '/' and num2 == 3:
        return("6/3 = 2")
    if num1 == 6 and sign == '/' and num2 == 4:
        return("6/4 = 1.5")
    if num1 == 6 and sign == '/' and num2 == 5:
        return("6/5 = 1.2")
    if num1 == 6 and sign == '/' and num2 == 6:
        return("6/6 = 1")
    if num1 == 6 and sign == '/' and num2 == 7:
        return("6/7 = 0.8571428571428571428571428571")
    if num1 == 6 and sign == '/' and num2 == 8:
        return("6/8 = 0.75")
    if num1 == 6 and sign == '/' and num2 == 9:
        return("6/9 = 0.6666666666666666666666666667")
    if num1 == 6 and sign == '/' and num2 == 10:
        return("6/10 = 0.6")
    if num1 == 6 and sign == '/' and num2 == 11:
        return("6/11 = 0.5454545454545454545454545455")
    if num1 == 6 and sign == '/' and num2 == 12:
        return("6/12 = 0.5")
    if num1 == 6 and sign == '/' and num2 == 13:
        return("6/13 = 0.4615384615384615384615384615")
    if num1 == 6 and sign == '/' and num2 == 14:
        return("6/14 = 0.4285714285714285714285714286")
    if num1 == 6 and sign == '/' and num2 == 15:
        return("6/15 = 0.4")
    if num1 == 6 and sign == '/' and num2 == 16:
        return("6/16 = 0.375")
    if num1 == 6 and sign == '/' and num2 == 17:
        return("6/17 = 0.3529411764705882352941176471")
    if num1 == 6 and sign == '/' and num2 == 18:
        return("6/18 = 0.3333333333333333333333333333")
    if num1 == 6 and sign == '/' and num2 == 19:
        return("6/19 = 0.3157894736842105263157894737")
    if num1 == 6 and sign == '/' and num2 == 20:
        return("6/20 = 0.3")
    if num1 == 6 and sign == '/' and num2 == 21:
        return("6/21 = 0.2857142857142857142857142857")
    if num1 == 6 and sign == '/' and num2 == 22:
        return("6/22 = 0.2727272727272727272727272727")
    if num1 == 6 and sign == '/' and num2 == 23:
        return("6/23 = 0.2608695652173913043478260870")
    if num1 == 6 and sign == '/' and num2 == 24:
        return("6/24 = 0.25")
    if num1 == 6 and sign == '/' and num2 == 25:
        return("6/25 = 0.24")
    if num1 == 6 and sign == '/' and num2 == 26:
        return("6/26 = 0.2307692307692307692307692308")
    if num1 == 6 and sign == '/' and num2 == 27:
        return("6/27 = 0.2222222222222222222222222222")
    if num1 == 6 and sign == '/' and num2 == 28:
        return("6/28 = 0.2142857142857142857142857143")
    if num1 == 6 and sign == '/' and num2 == 29:
        return("6/29 = 0.2068965517241379310344827586")
    if num1 == 6 and sign == '/' and num2 == 30:
        return("6/30 = 0.2")
    if num1 == 6 and sign == '/' and num2 == 31:
        return("6/31 = 0.1935483870967741935483870968")
    if num1 == 6 and sign == '/' and num2 == 32:
        return("6/32 = 0.1875")
    if num1 == 6 and sign == '/' and num2 == 33:
        return("6/33 = 0.1818181818181818181818181818")
    if num1 == 6 and sign == '/' and num2 == 34:
        return("6/34 = 0.1764705882352941176470588235")
    if num1 == 6 and sign == '/' and num2 == 35:
        return("6/35 = 0.1714285714285714285714285714")
    if num1 == 6 and sign == '/' and num2 == 36:
        return("6/36 = 0.1666666666666666666666666667")
    if num1 == 6 and sign == '/' and num2 == 37:
        return("6/37 = 0.1621621621621621621621621622")
    if num1 == 6 and sign == '/' and num2 == 38:
        return("6/38 = 0.1578947368421052631578947368")
    if num1 == 6 and sign == '/' and num2 == 39:
        return("6/39 = 0.1538461538461538461538461538")
    if num1 == 6 and sign == '/' and num2 == 40:
        return("6/40 = 0.15")
    if num1 == 6 and sign == '/' and num2 == 41:
        return("6/41 = 0.1463414634146341463414634146")
    if num1 == 6 and sign == '/' and num2 == 42:
        return("6/42 = 0.1428571428571428571428571429")
    if num1 == 6 and sign == '/' and num2 == 43:
        return("6/43 = 0.1395348837209302325581395349")
    if num1 == 6 and sign == '/' and num2 == 44:
        return("6/44 = 0.1363636363636363636363636364")
    if num1 == 6 and sign == '/' and num2 == 45:
        return("6/45 = 0.1333333333333333333333333333")
    if num1 == 6 and sign == '/' and num2 == 46:
        return("6/46 = 0.1304347826086956521739130435")
    if num1 == 6 and sign == '/' and num2 == 47:
        return("6/47 = 0.1276595744680851063829787234")
    if num1 == 6 and sign == '/' and num2 == 48:
        return("6/48 = 0.125")
    if num1 == 6 and sign == '/' and num2 == 49:
        return("6/49 = 0.1224489795918367346938775510")
    if num1 == 6 and sign == '/' and num2 == 50:
        return("6/50 = 0.12")
    if num1 == 7 and sign == '/' and num2 == 0:
        return("7/0 = Inf")
    if num1 == 7 and sign == '/' and num2 == 1:
        return("7/1 = 7")
    if num1 == 7 and sign == '/' and num2 == 2:
        return("7/2 = 3.5")
    if num1 == 7 and sign == '/' and num2 == 3:
        return("7/3 = 2.333333333333333333333333333")
    if num1 == 7 and sign == '/' and num2 == 4:
        return("7/4 = 1.75")
    if num1 == 7 and sign == '/' and num2 == 5:
        return("7/5 = 1.4")
    if num1 == 7 and sign == '/' and num2 == 6:
        return("7/6 = 1.166666666666666666666666667")
    if num1 == 7 and sign == '/' and num2 == 7:
        return("7/7 = 1")
    if num1 == 7 and sign == '/' and num2 == 8:
        return("7/8 = 0.875")
    if num1 == 7 and sign == '/' and num2 == 9:
        return("7/9 = 0.7777777777777777777777777778")
    if num1 == 7 and sign == '/' and num2 == 10:
        return("7/10 = 0.7")
    if num1 == 7 and sign == '/' and num2 == 11:
        return("7/11 = 0.6363636363636363636363636364")
    if num1 == 7 and sign == '/' and num2 == 12:
        return("7/12 = 0.5833333333333333333333333333")
    if num1 == 7 and sign == '/' and num2 == 13:
        return("7/13 = 0.5384615384615384615384615385")
    if num1 == 7 and sign == '/' and num2 == 14:
        return("7/14 = 0.5")
    if num1 == 7 and sign == '/' and num2 == 15:
        return("7/15 = 0.4666666666666666666666666667")
    if num1 == 7 and sign == '/' and num2 == 16:
        return("7/16 = 0.4375")
    if num1 == 7 and sign == '/' and num2 == 17:
        return("7/17 = 0.4117647058823529411764705882")
    if num1 == 7 and sign == '/' and num2 == 18:
        return("7/18 = 0.3888888888888888888888888889")
    if num1 == 7 and sign == '/' and num2 == 19:
        return("7/19 = 0.3684210526315789473684210526")
    if num1 == 7 and sign == '/' and num2 == 20:
        return("7/20 = 0.35")
    if num1 == 7 and sign == '/' and num2 == 21:
        return("7/21 = 0.3333333333333333333333333333")
    if num1 == 7 and sign == '/' and num2 == 22:
        return("7/22 = 0.3181818181818181818181818182")
    if num1 == 7 and sign == '/' and num2 == 23:
        return("7/23 = 0.3043478260869565217391304348")
    if num1 == 7 and sign == '/' and num2 == 24:
        return("7/24 = 0.2916666666666666666666666667")
    if num1 == 7 and sign == '/' and num2 == 25:
        return("7/25 = 0.28")
    if num1 == 7 and sign == '/' and num2 == 26:
        return("7/26 = 0.2692307692307692307692307692")
    if num1 == 7 and sign == '/' and num2 == 27:
        return("7/27 = 0.2592592592592592592592592593")
    if num1 == 7 and sign == '/' and num2 == 28:
        return("7/28 = 0.25")
    if num1 == 7 and sign == '/' and num2 == 29:
        return("7/29 = 0.2413793103448275862068965517")
    if num1 == 7 and sign == '/' and num2 == 30:
        return("7/30 = 0.2333333333333333333333333333")
    if num1 == 7 and sign == '/' and num2 == 31:
        return("7/31 = 0.2258064516129032258064516129")
    if num1 == 7 and sign == '/' and num2 == 32:
        return("7/32 = 0.21875")
    if num1 == 7 and sign == '/' and num2 == 33:
        return("7/33 = 0.2121212121212121212121212121")
    if num1 == 7 and sign == '/' and num2 == 34:
        return("7/34 = 0.2058823529411764705882352941")
    if num1 == 7 and sign == '/' and num2 == 35:
        return("7/35 = 0.2")
    if num1 == 7 and sign == '/' and num2 == 36:
        return("7/36 = 0.1944444444444444444444444444")
    if num1 == 7 and sign == '/' and num2 == 37:
        return("7/37 = 0.1891891891891891891891891892")
    if num1 == 7 and sign == '/' and num2 == 38:
        return("7/38 = 0.1842105263157894736842105263")
    if num1 == 7 and sign == '/' and num2 == 39:
        return("7/39 = 0.1794871794871794871794871795")
    if num1 == 7 and sign == '/' and num2 == 40:
        return("7/40 = 0.175")
    if num1 == 7 and sign == '/' and num2 == 41:
        return("7/41 = 0.1707317073170731707317073171")
    if num1 == 7 and sign == '/' and num2 == 42:
        return("7/42 = 0.1666666666666666666666666667")
    if num1 == 7 and sign == '/' and num2 == 43:
        return("7/43 = 0.1627906976744186046511627907")
    if num1 == 7 and sign == '/' and num2 == 44:
        return("7/44 = 0.1590909090909090909090909091")
    if num1 == 7 and sign == '/' and num2 == 45:
        return("7/45 = 0.1555555555555555555555555556")
    if num1 == 7 and sign == '/' and num2 == 46:
        return("7/46 = 0.1521739130434782608695652174")
    if num1 == 7 and sign == '/' and num2 == 47:
        return("7/47 = 0.1489361702127659574468085106")
    if num1 == 7 and sign == '/' and num2 == 48:
        return("7/48 = 0.1458333333333333333333333333")
    if num1 == 7 and sign == '/' and num2 == 49:
        return("7/49 = 0.1428571428571428571428571429")
    if num1 == 7 and sign == '/' and num2 == 50:
        return("7/50 = 0.14")
    if num1 == 8 and sign == '/' and num2 == 0:
        return("8/0 = Inf")
    if num1 == 8 and sign == '/' and num2 == 1:
        return("8/1 = 8")
    if num1 == 8 and sign == '/' and num2 == 2:
        return("8/2 = 4")
    if num1 == 8 and sign == '/' and num2 == 3:
        return("8/3 = 2.666666666666666666666666667")
    if num1 == 8 and sign == '/' and num2 == 4:
        return("8/4 = 2")
    if num1 == 8 and sign == '/' and num2 == 5:
        return("8/5 = 1.6")
    if num1 == 8 and sign == '/' and num2 == 6:
        return("8/6 = 1.333333333333333333333333333")
    if num1 == 8 and sign == '/' and num2 == 7:
        return("8/7 = 1.142857142857142857142857143")
    if num1 == 8 and sign == '/' and num2 == 8:
        return("8/8 = 1")
    if num1 == 8 and sign == '/' and num2 == 9:
        return("8/9 = 0.8888888888888888888888888889")
    if num1 == 8 and sign == '/' and num2 == 10:
        return("8/10 = 0.8")
    if num1 == 8 and sign == '/' and num2 == 11:
        return("8/11 = 0.7272727272727272727272727273")
    if num1 == 8 and sign == '/' and num2 == 12:
        return("8/12 = 0.6666666666666666666666666667")
    if num1 == 8 and sign == '/' and num2 == 13:
        return("8/13 = 0.6153846153846153846153846154")
    if num1 == 8 and sign == '/' and num2 == 14:
        return("8/14 = 0.5714285714285714285714285714")
    if num1 == 8 and sign == '/' and num2 == 15:
        return("8/15 = 0.5333333333333333333333333333")
    if num1 == 8 and sign == '/' and num2 == 16:
        return("8/16 = 0.5")
    if num1 == 8 and sign == '/' and num2 == 17:
        return("8/17 = 0.4705882352941176470588235294")
    if num1 == 8 and sign == '/' and num2 == 18:
        return("8/18 = 0.4444444444444444444444444444")
    if num1 == 8 and sign == '/' and num2 == 19:
        return("8/19 = 0.4210526315789473684210526316")
    if num1 == 8 and sign == '/' and num2 == 20:
        return("8/20 = 0.4")
    if num1 == 8 and sign == '/' and num2 == 21:
        return("8/21 = 0.3809523809523809523809523810")
    if num1 == 8 and sign == '/' and num2 == 22:
        return("8/22 = 0.3636363636363636363636363636")
    if num1 == 8 and sign == '/' and num2 == 23:
        return("8/23 = 0.3478260869565217391304347826")
    if num1 == 8 and sign == '/' and num2 == 24:
        return("8/24 = 0.3333333333333333333333333333")
    if num1 == 8 and sign == '/' and num2 == 25:
        return("8/25 = 0.32")
    if num1 == 8 and sign == '/' and num2 == 26:
        return("8/26 = 0.3076923076923076923076923077")
    if num1 == 8 and sign == '/' and num2 == 27:
        return("8/27 = 0.2962962962962962962962962963")
    if num1 == 8 and sign == '/' and num2 == 28:
        return("8/28 = 0.2857142857142857142857142857")
    if num1 == 8 and sign == '/' and num2 == 29:
        return("8/29 = 0.2758620689655172413793103448")
    if num1 == 8 and sign == '/' and num2 == 30:
        return("8/30 = 0.2666666666666666666666666667")
    if num1 == 8 and sign == '/' and num2 == 31:
        return("8/31 = 0.2580645161290322580645161290")
    if num1 == 8 and sign == '/' and num2 == 32:
        return("8/32 = 0.25")
    if num1 == 8 and sign == '/' and num2 == 33:
        return("8/33 = 0.2424242424242424242424242424")
    if num1 == 8 and sign == '/' and num2 == 34:
        return("8/34 = 0.2352941176470588235294117647")
    if num1 == 8 and sign == '/' and num2 == 35:
        return("8/35 = 0.2285714285714285714285714286")
    if num1 == 8 and sign == '/' and num2 == 36:
        return("8/36 = 0.2222222222222222222222222222")
    if num1 == 8 and sign == '/' and num2 == 37:
        return("8/37 = 0.2162162162162162162162162162")
    if num1 == 8 and sign == '/' and num2 == 38:
        return("8/38 = 0.2105263157894736842105263158")
    if num1 == 8 and sign == '/' and num2 == 39:
        return("8/39 = 0.2051282051282051282051282051")
    if num1 == 8 and sign == '/' and num2 == 40:
        return("8/40 = 0.2")
    if num1 == 8 and sign == '/' and num2 == 41:
        return("8/41 = 0.1951219512195121951219512195")
    if num1 == 8 and sign == '/' and num2 == 42:
        return("8/42 = 0.1904761904761904761904761905")
    if num1 == 8 and sign == '/' and num2 == 43:
        return("8/43 = 0.1860465116279069767441860465")
    if num1 == 8 and sign == '/' and num2 == 44:
        return("8/44 = 0.1818181818181818181818181818")
    if num1 == 8 and sign == '/' and num2 == 45:
        return("8/45 = 0.1777777777777777777777777778")
    if num1 == 8 and sign == '/' and num2 == 46:
        return("8/46 = 0.1739130434782608695652173913")
    if num1 == 8 and sign == '/' and num2 == 47:
        return("8/47 = 0.1702127659574468085106382979")
    if num1 == 8 and sign == '/' and num2 == 48:
        return("8/48 = 0.1666666666666666666666666667")
    if num1 == 8 and sign == '/' and num2 == 49:
        return("8/49 = 0.1632653061224489795918367347")
    if num1 == 8 and sign == '/' and num2 == 50:
        return("8/50 = 0.16")
    if num1 == 9 and sign == '/' and num2 == 0:
        return("9/0 = Inf")
    if num1 == 9 and sign == '/' and num2 == 1:
        return("9/1 = 9")
    if num1 == 9 and sign == '/' and num2 == 2:
        return("9/2 = 4.5")
    if num1 == 9 and sign == '/' and num2 == 3:
        return("9/3 = 3")
    if num1 == 9 and sign == '/' and num2 == 4:
        return("9/4 = 2.25")
    if num1 == 9 and sign == '/' and num2 == 5:
        return("9/5 = 1.8")
    if num1 == 9 and sign == '/' and num2 == 6:
        return("9/6 = 1.5")
    if num1 == 9 and sign == '/' and num2 == 7:
        return("9/7 = 1.285714285714285714285714286")
    if num1 == 9 and sign == '/' and num2 == 8:
        return("9/8 = 1.125")
    if num1 == 9 and sign == '/' and num2 == 9:
        return("9/9 = 1")
    if num1 == 9 and sign == '/' and num2 == 10:
        return("9/10 = 0.9")
    if num1 == 9 and sign == '/' and num2 == 11:
        return("9/11 = 0.8181818181818181818181818182")
    if num1 == 9 and sign == '/' and num2 == 12:
        return("9/12 = 0.75")
    if num1 == 9 and sign == '/' and num2 == 13:
        return("9/13 = 0.6923076923076923076923076923")
    if num1 == 9 and sign == '/' and num2 == 14:
        return("9/14 = 0.6428571428571428571428571429")
    if num1 == 9 and sign == '/' and num2 == 15:
        return("9/15 = 0.6")
    if num1 == 9 and sign == '/' and num2 == 16:
        return("9/16 = 0.5625")
    if num1 == 9 and sign == '/' and num2 == 17:
        return("9/17 = 0.5294117647058823529411764706")
    if num1 == 9 and sign == '/' and num2 == 18:
        return("9/18 = 0.5")
    if num1 == 9 and sign == '/' and num2 == 19:
        return("9/19 = 0.4736842105263157894736842105")
    if num1 == 9 and sign == '/' and num2 == 20:
        return("9/20 = 0.45")
    if num1 == 9 and sign == '/' and num2 == 21:
        return("9/21 = 0.4285714285714285714285714286")
    if num1 == 9 and sign == '/' and num2 == 22:
        return("9/22 = 0.4090909090909090909090909091")
    if num1 == 9 and sign == '/' and num2 == 23:
        return("9/23 = 0.3913043478260869565217391304")
    if num1 == 9 and sign == '/' and num2 == 24:
        return("9/24 = 0.375")
    if num1 == 9 and sign == '/' and num2 == 25:
        return("9/25 = 0.36")
    if num1 == 9 and sign == '/' and num2 == 26:
        return("9/26 = 0.3461538461538461538461538462")
    if num1 == 9 and sign == '/' and num2 == 27:
        return("9/27 = 0.3333333333333333333333333333")
    if num1 == 9 and sign == '/' and num2 == 28:
        return("9/28 = 0.3214285714285714285714285714")
    if num1 == 9 and sign == '/' and num2 == 29:
        return("9/29 = 0.3103448275862068965517241379")
    if num1 == 9 and sign == '/' and num2 == 30:
        return("9/30 = 0.3")
    if num1 == 9 and sign == '/' and num2 == 31:
        return("9/31 = 0.2903225806451612903225806452")
    if num1 == 9 and sign == '/' and num2 == 32:
        return("9/32 = 0.28125")
    if num1 == 9 and sign == '/' and num2 == 33:
        return("9/33 = 0.2727272727272727272727272727")
    if num1 == 9 and sign == '/' and num2 == 34:
        return("9/34 = 0.2647058823529411764705882353")
    if num1 == 9 and sign == '/' and num2 == 35:
        return("9/35 = 0.2571428571428571428571428571")
    if num1 == 9 and sign == '/' and num2 == 36:
        return("9/36 = 0.25")
    if num1 == 9 and sign == '/' and num2 == 37:
        return("9/37 = 0.2432432432432432432432432432")
    if num1 == 9 and sign == '/' and num2 == 38:
        return("9/38 = 0.2368421052631578947368421053")
    if num1 == 9 and sign == '/' and num2 == 39:
        return("9/39 = 0.2307692307692307692307692308")
    if num1 == 9 and sign == '/' and num2 == 40:
        return("9/40 = 0.225")
    if num1 == 9 and sign == '/' and num2 == 41:
        return("9/41 = 0.2195121951219512195121951220")
    if num1 == 9 and sign == '/' and num2 == 42:
        return("9/42 = 0.2142857142857142857142857143")
    if num1 == 9 and sign == '/' and num2 == 43:
        return("9/43 = 0.2093023255813953488372093023")
    if num1 == 9 and sign == '/' and num2 == 44:
        return("9/44 = 0.2045454545454545454545454545")
    if num1 == 9 and sign == '/' and num2 == 45:
        return("9/45 = 0.2")
    if num1 == 9 and sign == '/' and num2 == 46:
        return("9/46 = 0.1956521739130434782608695652")
    if num1 == 9 and sign == '/' and num2 == 47:
        return("9/47 = 0.1914893617021276595744680851")
    if num1 == 9 and sign == '/' and num2 == 48:
        return("9/48 = 0.1875")
    if num1 == 9 and sign == '/' and num2 == 49:
        return("9/49 = 0.1836734693877551020408163265")
    if num1 == 9 and sign == '/' and num2 == 50:
        return("9/50 = 0.18")
    if num1 == 10 and sign == '/' and num2 == 0:
        return("10/0 = Inf")
    if num1 == 10 and sign == '/' and num2 == 1:
        return("10/1 = 10")
    if num1 == 10 and sign == '/' and num2 == 2:
        return("10/2 = 5")
    if num1 == 10 and sign == '/' and num2 == 3:
        return("10/3 = 3.333333333333333333333333333")
    if num1 == 10 and sign == '/' and num2 == 4:
        return("10/4 = 2.5")
    if num1 == 10 and sign == '/' and num2 == 5:
        return("10/5 = 2")
    if num1 == 10 and sign == '/' and num2 == 6:
        return("10/6 = 1.666666666666666666666666667")
    if num1 == 10 and sign == '/' and num2 == 7:
        return("10/7 = 1.428571428571428571428571429")
    if num1 == 10 and sign == '/' and num2 == 8:
        return("10/8 = 1.25")
    if num1 == 10 and sign == '/' and num2 == 9:
        return("10/9 = 1.111111111111111111111111111")
    if num1 == 10 and sign == '/' and num2 == 10:
        return("10/10 = 1")
    if num1 == 10 and sign == '/' and num2 == 11:
        return("10/11 = 0.9090909090909090909090909091")
    if num1 == 10 and sign == '/' and num2 == 12:
        return("10/12 = 0.8333333333333333333333333333")
    if num1 == 10 and sign == '/' and num2 == 13:
        return("10/13 = 0.7692307692307692307692307692")
    if num1 == 10 and sign == '/' and num2 == 14:
        return("10/14 = 0.7142857142857142857142857143")
    if num1 == 10 and sign == '/' and num2 == 15:
        return("10/15 = 0.6666666666666666666666666667")
    if num1 == 10 and sign == '/' and num2 == 16:
        return("10/16 = 0.625")
    if num1 == 10 and sign == '/' and num2 == 17:
        return("10/17 = 0.5882352941176470588235294118")
    if num1 == 10 and sign == '/' and num2 == 18:
        return("10/18 = 0.5555555555555555555555555556")
    if num1 == 10 and sign == '/' and num2 == 19:
        return("10/19 = 0.5263157894736842105263157895")
    if num1 == 10 and sign == '/' and num2 == 20:
        return("10/20 = 0.5")
    if num1 == 10 and sign == '/' and num2 == 21:
        return("10/21 = 0.4761904761904761904761904762")
    if num1 == 10 and sign == '/' and num2 == 22:
        return("10/22 = 0.4545454545454545454545454545")
    if num1 == 10 and sign == '/' and num2 == 23:
        return("10/23 = 0.4347826086956521739130434783")
    if num1 == 10 and sign == '/' and num2 == 24:
        return("10/24 = 0.4166666666666666666666666667")
    if num1 == 10 and sign == '/' and num2 == 25:
        return("10/25 = 0.4")
    if num1 == 10 and sign == '/' and num2 == 26:
        return("10/26 = 0.3846153846153846153846153846")
    if num1 == 10 and sign == '/' and num2 == 27:
        return("10/27 = 0.3703703703703703703703703704")
    if num1 == 10 and sign == '/' and num2 == 28:
        return("10/28 = 0.3571428571428571428571428571")
    if num1 == 10 and sign == '/' and num2 == 29:
        return("10/29 = 0.3448275862068965517241379310")
    if num1 == 10 and sign == '/' and num2 == 30:
        return("10/30 = 0.3333333333333333333333333333")
    if num1 == 10 and sign == '/' and num2 == 31:
        return("10/31 = 0.3225806451612903225806451613")
    if num1 == 10 and sign == '/' and num2 == 32:
        return("10/32 = 0.3125")
    if num1 == 10 and sign == '/' and num2 == 33:
        return("10/33 = 0.3030303030303030303030303030")
    if num1 == 10 and sign == '/' and num2 == 34:
        return("10/34 = 0.2941176470588235294117647059")
    if num1 == 10 and sign == '/' and num2 == 35:
        return("10/35 = 0.2857142857142857142857142857")
    if num1 == 10 and sign == '/' and num2 == 36:
        return("10/36 = 0.2777777777777777777777777778")
    if num1 == 10 and sign == '/' and num2 == 37:
        return("10/37 = 0.2702702702702702702702702703")
    if num1 == 10 and sign == '/' and num2 == 38:
        return("10/38 = 0.2631578947368421052631578947")
    if num1 == 10 and sign == '/' and num2 == 39:
        return("10/39 = 0.2564102564102564102564102564")
    if num1 == 10 and sign == '/' and num2 == 40:
        return("10/40 = 0.25")
    if num1 == 10 and sign == '/' and num2 == 41:
        return("10/41 = 0.2439024390243902439024390244")
    if num1 == 10 and sign == '/' and num2 == 42:
        return("10/42 = 0.2380952380952380952380952381")
    if num1 == 10 and sign == '/' and num2 == 43:
        return("10/43 = 0.2325581395348837209302325581")
    if num1 == 10 and sign == '/' and num2 == 44:
        return("10/44 = 0.2272727272727272727272727273")
    if num1 == 10 and sign == '/' and num2 == 45:
        return("10/45 = 0.2222222222222222222222222222")
    if num1 == 10 and sign == '/' and num2 == 46:
        return("10/46 = 0.2173913043478260869565217391")
    if num1 == 10 and sign == '/' and num2 == 47:
        return("10/47 = 0.2127659574468085106382978723")
    if num1 == 10 and sign == '/' and num2 == 48:
        return("10/48 = 0.2083333333333333333333333333")
    if num1 == 10 and sign == '/' and num2 == 49:
        return("10/49 = 0.2040816326530612244897959184")
    if num1 == 10 and sign == '/' and num2 == 50:
        return("10/50 = 0.2")
    if num1 == 11 and sign == '/' and num2 == 0:
        return("11/0 = Inf")
    if num1 == 11 and sign == '/' and num2 == 1:
        return("11/1 = 11")
    if num1 == 11 and sign == '/' and num2 == 2:
        return("11/2 = 5.5")
    if num1 == 11 and sign == '/' and num2 == 3:
        return("11/3 = 3.666666666666666666666666667")
    if num1 == 11 and sign == '/' and num2 == 4:
        return("11/4 = 2.75")
    if num1 == 11 and sign == '/' and num2 == 5:
        return("11/5 = 2.2")
    if num1 == 11 and sign == '/' and num2 == 6:
        return("11/6 = 1.833333333333333333333333333")
    if num1 == 11 and sign == '/' and num2 == 7:
        return("11/7 = 1.571428571428571428571428571")
    if num1 == 11 and sign == '/' and num2 == 8:
        return("11/8 = 1.375")
    if num1 == 11 and sign == '/' and num2 == 9:
        return("11/9 = 1.222222222222222222222222222")
    if num1 == 11 and sign == '/' and num2 == 10:
        return("11/10 = 1.1")
    if num1 == 11 and sign == '/' and num2 == 11:
        return("11/11 = 1")
    if num1 == 11 and sign == '/' and num2 == 12:
        return("11/12 = 0.9166666666666666666666666667")
    if num1 == 11 and sign == '/' and num2 == 13:
        return("11/13 = 0.8461538461538461538461538462")
    if num1 == 11 and sign == '/' and num2 == 14:
        return("11/14 = 0.7857142857142857142857142857")
    if num1 == 11 and sign == '/' and num2 == 15:
        return("11/15 = 0.7333333333333333333333333333")
    if num1 == 11 and sign == '/' and num2 == 16:
        return("11/16 = 0.6875")
    if num1 == 11 and sign == '/' and num2 == 17:
        return("11/17 = 0.6470588235294117647058823529")
    if num1 == 11 and sign == '/' and num2 == 18:
        return("11/18 = 0.6111111111111111111111111111")
    if num1 == 11 and sign == '/' and num2 == 19:
        return("11/19 = 0.5789473684210526315789473684")
    if num1 == 11 and sign == '/' and num2 == 20:
        return("11/20 = 0.55")
    if num1 == 11 and sign == '/' and num2 == 21:
        return("11/21 = 0.5238095238095238095238095238")
    if num1 == 11 and sign == '/' and num2 == 22:
        return("11/22 = 0.5")
    if num1 == 11 and sign == '/' and num2 == 23:
        return("11/23 = 0.4782608695652173913043478261")
    if num1 == 11 and sign == '/' and num2 == 24:
        return("11/24 = 0.4583333333333333333333333333")
    if num1 == 11 and sign == '/' and num2 == 25:
        return("11/25 = 0.44")
    if num1 == 11 and sign == '/' and num2 == 26:
        return("11/26 = 0.4230769230769230769230769231")
    if num1 == 11 and sign == '/' and num2 == 27:
        return("11/27 = 0.4074074074074074074074074074")
    if num1 == 11 and sign == '/' and num2 == 28:
        return("11/28 = 0.3928571428571428571428571429")
    if num1 == 11 and sign == '/' and num2 == 29:
        return("11/29 = 0.3793103448275862068965517241")
    if num1 == 11 and sign == '/' and num2 == 30:
        return("11/30 = 0.3666666666666666666666666667")
    if num1 == 11 and sign == '/' and num2 == 31:
        return("11/31 = 0.3548387096774193548387096774")
    if num1 == 11 and sign == '/' and num2 == 32:
        return("11/32 = 0.34375")
    if num1 == 11 and sign == '/' and num2 == 33:
        return("11/33 = 0.3333333333333333333333333333")
    if num1 == 11 and sign == '/' and num2 == 34:
        return("11/34 = 0.3235294117647058823529411765")
    if num1 == 11 and sign == '/' and num2 == 35:
        return("11/35 = 0.3142857142857142857142857143")
    if num1 == 11 and sign == '/' and num2 == 36:
        return("11/36 = 0.3055555555555555555555555556")
    if num1 == 11 and sign == '/' and num2 == 37:
        return("11/37 = 0.2972972972972972972972972973")
    if num1 == 11 and sign == '/' and num2 == 38:
        return("11/38 = 0.2894736842105263157894736842")
    if num1 == 11 and sign == '/' and num2 == 39:
        return("11/39 = 0.2820512820512820512820512821")
    if num1 == 11 and sign == '/' and num2 == 40:
        return("11/40 = 0.275")
    if num1 == 11 and sign == '/' and num2 == 41:
        return("11/41 = 0.2682926829268292682926829268")
    if num1 == 11 and sign == '/' and num2 == 42:
        return("11/42 = 0.2619047619047619047619047619")
    if num1 == 11 and sign == '/' and num2 == 43:
        return("11/43 = 0.2558139534883720930232558140")
    if num1 == 11 and sign == '/' and num2 == 44:
        return("11/44 = 0.25")
    if num1 == 11 and sign == '/' and num2 == 45:
        return("11/45 = 0.2444444444444444444444444444")
    if num1 == 11 and sign == '/' and num2 == 46:
        return("11/46 = 0.2391304347826086956521739130")
    if num1 == 11 and sign == '/' and num2 == 47:
        return("11/47 = 0.2340425531914893617021276596")
    if num1 == 11 and sign == '/' and num2 == 48:
        return("11/48 = 0.2291666666666666666666666667")
    if num1 == 11 and sign == '/' and num2 == 49:
        return("11/49 = 0.2244897959183673469387755102")
    if num1 == 11 and sign == '/' and num2 == 50:
        return("11/50 = 0.22")
    if num1 == 12 and sign == '/' and num2 == 0:
        return("12/0 = Inf")
    if num1 == 12 and sign == '/' and num2 == 1:
        return("12/1 = 12")
    if num1 == 12 and sign == '/' and num2 == 2:
        return("12/2 = 6")
    if num1 == 12 and sign == '/' and num2 == 3:
        return("12/3 = 4")
    if num1 == 12 and sign == '/' and num2 == 4:
        return("12/4 = 3")
    if num1 == 12 and sign == '/' and num2 == 5:
        return("12/5 = 2.4")
    if num1 == 12 and sign == '/' and num2 == 6:
        return("12/6 = 2")
    if num1 == 12 and sign == '/' and num2 == 7:
        return("12/7 = 1.714285714285714285714285714")
    if num1 == 12 and sign == '/' and num2 == 8:
        return("12/8 = 1.5")
    if num1 == 12 and sign == '/' and num2 == 9:
        return("12/9 = 1.333333333333333333333333333")
    if num1 == 12 and sign == '/' and num2 == 10:
        return("12/10 = 1.2")
    if num1 == 12 and sign == '/' and num2 == 11:
        return("12/11 = 1.090909090909090909090909091")
    if num1 == 12 and sign == '/' and num2 == 12:
        return("12/12 = 1")
    if num1 == 12 and sign == '/' and num2 == 13:
        return("12/13 = 0.9230769230769230769230769231")
    if num1 == 12 and sign == '/' and num2 == 14:
        return("12/14 = 0.8571428571428571428571428571")
    if num1 == 12 and sign == '/' and num2 == 15:
        return("12/15 = 0.8")
    if num1 == 12 and sign == '/' and num2 == 16:
        return("12/16 = 0.75")
    if num1 == 12 and sign == '/' and num2 == 17:
        return("12/17 = 0.7058823529411764705882352941")
    if num1 == 12 and sign == '/' and num2 == 18:
        return("12/18 = 0.6666666666666666666666666667")
    if num1 == 12 and sign == '/' and num2 == 19:
        return("12/19 = 0.6315789473684210526315789474")
    if num1 == 12 and sign == '/' and num2 == 20:
        return("12/20 = 0.6")
    if num1 == 12 and sign == '/' and num2 == 21:
        return("12/21 = 0.5714285714285714285714285714")
    if num1 == 12 and sign == '/' and num2 == 22:
        return("12/22 = 0.5454545454545454545454545455")
    if num1 == 12 and sign == '/' and num2 == 23:
        return("12/23 = 0.5217391304347826086956521739")
    if num1 == 12 and sign == '/' and num2 == 24:
        return("12/24 = 0.5")
    if num1 == 12 and sign == '/' and num2 == 25:
        return("12/25 = 0.48")
    if num1 == 12 and sign == '/' and num2 == 26:
        return("12/26 = 0.4615384615384615384615384615")
    if num1 == 12 and sign == '/' and num2 == 27:
        return("12/27 = 0.4444444444444444444444444444")
    if num1 == 12 and sign == '/' and num2 == 28:
        return("12/28 = 0.4285714285714285714285714286")
    if num1 == 12 and sign == '/' and num2 == 29:
        return("12/29 = 0.4137931034482758620689655172")
    if num1 == 12 and sign == '/' and num2 == 30:
        return("12/30 = 0.4")
    if num1 == 12 and sign == '/' and num2 == 31:
        return("12/31 = 0.3870967741935483870967741935")
    if num1 == 12 and sign == '/' and num2 == 32:
        return("12/32 = 0.375")
    if num1 == 12 and sign == '/' and num2 == 33:
        return("12/33 = 0.3636363636363636363636363636")
    if num1 == 12 and sign == '/' and num2 == 34:
        return("12/34 = 0.3529411764705882352941176471")
    if num1 == 12 and sign == '/' and num2 == 35:
        return("12/35 = 0.3428571428571428571428571429")
    if num1 == 12 and sign == '/' and num2 == 36:
        return("12/36 = 0.3333333333333333333333333333")
    if num1 == 12 and sign == '/' and num2 == 37:
        return("12/37 = 0.3243243243243243243243243243")
    if num1 == 12 and sign == '/' and num2 == 38:
        return("12/38 = 0.3157894736842105263157894737")
    if num1 == 12 and sign == '/' and num2 == 39:
        return("12/39 = 0.3076923076923076923076923077")
    if num1 == 12 and sign == '/' and num2 == 40:
        return("12/40 = 0.3")
    if num1 == 12 and sign == '/' and num2 == 41:
        return("12/41 = 0.2926829268292682926829268293")
    if num1 == 12 and sign == '/' and num2 == 42:
        return("12/42 = 0.2857142857142857142857142857")
    if num1 == 12 and sign == '/' and num2 == 43:
        return("12/43 = 0.2790697674418604651162790698")
    if num1 == 12 and sign == '/' and num2 == 44:
        return("12/44 = 0.2727272727272727272727272727")
    if num1 == 12 and sign == '/' and num2 == 45:
        return("12/45 = 0.2666666666666666666666666667")
    if num1 == 12 and sign == '/' and num2 == 46:
        return("12/46 = 0.2608695652173913043478260870")
    if num1 == 12 and sign == '/' and num2 == 47:
        return("12/47 = 0.2553191489361702127659574468")
    if num1 == 12 and sign == '/' and num2 == 48:
        return("12/48 = 0.25")
    if num1 == 12 and sign == '/' and num2 == 49:
        return("12/49 = 0.2448979591836734693877551020")
    if num1 == 12 and sign == '/' and num2 == 50:
        return("12/50 = 0.24")
    if num1 == 13 and sign == '/' and num2 == 0:
        return("13/0 = Inf")
    if num1 == 13 and sign == '/' and num2 == 1:
        return("13/1 = 13")
    if num1 == 13 and sign == '/' and num2 == 2:
        return("13/2 = 6.5")
    if num1 == 13 and sign == '/' and num2 == 3:
        return("13/3 = 4.333333333333333333333333333")
    if num1 == 13 and sign == '/' and num2 == 4:
        return("13/4 = 3.25")
    if num1 == 13 and sign == '/' and num2 == 5:
        return("13/5 = 2.6")
    if num1 == 13 and sign == '/' and num2 == 6:
        return("13/6 = 2.166666666666666666666666667")
    if num1 == 13 and sign == '/' and num2 == 7:
        return("13/7 = 1.857142857142857142857142857")
    if num1 == 13 and sign == '/' and num2 == 8:
        return("13/8 = 1.625")
    if num1 == 13 and sign == '/' and num2 == 9:
        return("13/9 = 1.444444444444444444444444444")
    if num1 == 13 and sign == '/' and num2 == 10:
        return("13/10 = 1.3")
    if num1 == 13 and sign == '/' and num2 == 11:
        return("13/11 = 1.181818181818181818181818182")
    if num1 == 13 and sign == '/' and num2 == 12:
        return("13/12 = 1.083333333333333333333333333")
    if num1 == 13 and sign == '/' and num2 == 13:
        return("13/13 = 1")
    if num1 == 13 and sign == '/' and num2 == 14:
        return("13/14 = 0.9285714285714285714285714286")
    if num1 == 13 and sign == '/' and num2 == 15:
        return("13/15 = 0.8666666666666666666666666667")
    if num1 == 13 and sign == '/' and num2 == 16:
        return("13/16 = 0.8125")
    if num1 == 13 and sign == '/' and num2 == 17:
        return("13/17 = 0.7647058823529411764705882353")
    if num1 == 13 and sign == '/' and num2 == 18:
        return("13/18 = 0.7222222222222222222222222222")
    if num1 == 13 and sign == '/' and num2 == 19:
        return("13/19 = 0.6842105263157894736842105263")
    if num1 == 13 and sign == '/' and num2 == 20:
        return("13/20 = 0.65")
    if num1 == 13 and sign == '/' and num2 == 21:
        return("13/21 = 0.6190476190476190476190476190")
    if num1 == 13 and sign == '/' and num2 == 22:
        return("13/22 = 0.5909090909090909090909090909")
    if num1 == 13 and sign == '/' and num2 == 23:
        return("13/23 = 0.5652173913043478260869565217")
    if num1 == 13 and sign == '/' and num2 == 24:
        return("13/24 = 0.5416666666666666666666666667")
    if num1 == 13 and sign == '/' and num2 == 25:
        return("13/25 = 0.52")
    if num1 == 13 and sign == '/' and num2 == 26:
        return("13/26 = 0.5")
    if num1 == 13 and sign == '/' and num2 == 27:
        return("13/27 = 0.4814814814814814814814814815")
    if num1 == 13 and sign == '/' and num2 == 28:
        return("13/28 = 0.4642857142857142857142857143")
    if num1 == 13 and sign == '/' and num2 == 29:
        return("13/29 = 0.4482758620689655172413793103")
    if num1 == 13 and sign == '/' and num2 == 30:
        return("13/30 = 0.4333333333333333333333333333")
    if num1 == 13 and sign == '/' and num2 == 31:
        return("13/31 = 0.4193548387096774193548387097")
    if num1 == 13 and sign == '/' and num2 == 32:
        return("13/32 = 0.40625")
    if num1 == 13 and sign == '/' and num2 == 33:
        return("13/33 = 0.3939393939393939393939393939")
    if num1 == 13 and sign == '/' and num2 == 34:
        return("13/34 = 0.3823529411764705882352941176")
    if num1 == 13 and sign == '/' and num2 == 35:
        return("13/35 = 0.3714285714285714285714285714")
    if num1 == 13 and sign == '/' and num2 == 36:
        return("13/36 = 0.3611111111111111111111111111")
    if num1 == 13 and sign == '/' and num2 == 37:
        return("13/37 = 0.3513513513513513513513513514")
    if num1 == 13 and sign == '/' and num2 == 38:
        return("13/38 = 0.3421052631578947368421052632")
    if num1 == 13 and sign == '/' and num2 == 39:
        return("13/39 = 0.3333333333333333333333333333")
    if num1 == 13 and sign == '/' and num2 == 40:
        return("13/40 = 0.325")
    if num1 == 13 and sign == '/' and num2 == 41:
        return("13/41 = 0.3170731707317073170731707317")
    if num1 == 13 and sign == '/' and num2 == 42:
        return("13/42 = 0.3095238095238095238095238095")
    if num1 == 13 and sign == '/' and num2 == 43:
        return("13/43 = 0.3023255813953488372093023256")
    if num1 == 13 and sign == '/' and num2 == 44:
        return("13/44 = 0.2954545454545454545454545455")
    if num1 == 13 and sign == '/' and num2 == 45:
        return("13/45 = 0.2888888888888888888888888889")
    if num1 == 13 and sign == '/' and num2 == 46:
        return("13/46 = 0.2826086956521739130434782609")
    if num1 == 13 and sign == '/' and num2 == 47:
        return("13/47 = 0.2765957446808510638297872340")
    if num1 == 13 and sign == '/' and num2 == 48:
        return("13/48 = 0.2708333333333333333333333333")
    if num1 == 13 and sign == '/' and num2 == 49:
        return("13/49 = 0.2653061224489795918367346939")
    if num1 == 13 and sign == '/' and num2 == 50:
        return("13/50 = 0.26")
    if num1 == 14 and sign == '/' and num2 == 0:
        return("14/0 = Inf")
    if num1 == 14 and sign == '/' and num2 == 1:
        return("14/1 = 14")
    if num1 == 14 and sign == '/' and num2 == 2:
        return("14/2 = 7")
    if num1 == 14 and sign == '/' and num2 == 3:
        return("14/3 = 4.666666666666666666666666667")
    if num1 == 14 and sign == '/' and num2 == 4:
        return("14/4 = 3.5")
    if num1 == 14 and sign == '/' and num2 == 5:
        return("14/5 = 2.8")
    if num1 == 14 and sign == '/' and num2 == 6:
        return("14/6 = 2.333333333333333333333333333")
    if num1 == 14 and sign == '/' and num2 == 7:
        return("14/7 = 2")
    if num1 == 14 and sign == '/' and num2 == 8:
        return("14/8 = 1.75")
    if num1 == 14 and sign == '/' and num2 == 9:
        return("14/9 = 1.555555555555555555555555556")
    if num1 == 14 and sign == '/' and num2 == 10:
        return("14/10 = 1.4")
    if num1 == 14 and sign == '/' and num2 == 11:
        return("14/11 = 1.272727272727272727272727273")
    if num1 == 14 and sign == '/' and num2 == 12:
        return("14/12 = 1.166666666666666666666666667")
    if num1 == 14 and sign == '/' and num2 == 13:
        return("14/13 = 1.076923076923076923076923077")
    if num1 == 14 and sign == '/' and num2 == 14:
        return("14/14 = 1")
    if num1 == 14 and sign == '/' and num2 == 15:
        return("14/15 = 0.9333333333333333333333333333")
    if num1 == 14 and sign == '/' and num2 == 16:
        return("14/16 = 0.875")
    if num1 == 14 and sign == '/' and num2 == 17:
        return("14/17 = 0.8235294117647058823529411765")
    if num1 == 14 and sign == '/' and num2 == 18:
        return("14/18 = 0.7777777777777777777777777778")
    if num1 == 14 and sign == '/' and num2 == 19:
        return("14/19 = 0.7368421052631578947368421053")
    if num1 == 14 and sign == '/' and num2 == 20:
        return("14/20 = 0.7")
    if num1 == 14 and sign == '/' and num2 == 21:
        return("14/21 = 0.6666666666666666666666666667")
    if num1 == 14 and sign == '/' and num2 == 22:
        return("14/22 = 0.6363636363636363636363636364")
    if num1 == 14 and sign == '/' and num2 == 23:
        return("14/23 = 0.6086956521739130434782608696")
    if num1 == 14 and sign == '/' and num2 == 24:
        return("14/24 = 0.5833333333333333333333333333")
    if num1 == 14 and sign == '/' and num2 == 25:
        return("14/25 = 0.56")
    if num1 == 14 and sign == '/' and num2 == 26:
        return("14/26 = 0.5384615384615384615384615385")
    if num1 == 14 and sign == '/' and num2 == 27:
        return("14/27 = 0.5185185185185185185185185185")
    if num1 == 14 and sign == '/' and num2 == 28:
        return("14/28 = 0.5")
    if num1 == 14 and sign == '/' and num2 == 29:
        return("14/29 = 0.4827586206896551724137931034")
    if num1 == 14 and sign == '/' and num2 == 30:
        return("14/30 = 0.4666666666666666666666666667")
    if num1 == 14 and sign == '/' and num2 == 31:
        return("14/31 = 0.4516129032258064516129032258")
    if num1 == 14 and sign == '/' and num2 == 32:
        return("14/32 = 0.4375")
    if num1 == 14 and sign == '/' and num2 == 33:
        return("14/33 = 0.4242424242424242424242424242")
    if num1 == 14 and sign == '/' and num2 == 34:
        return("14/34 = 0.4117647058823529411764705882")
    if num1 == 14 and sign == '/' and num2 == 35:
        return("14/35 = 0.4")
    if num1 == 14 and sign == '/' and num2 == 36:
        return("14/36 = 0.3888888888888888888888888889")
    if num1 == 14 and sign == '/' and num2 == 37:
        return("14/37 = 0.3783783783783783783783783784")
    if num1 == 14 and sign == '/' and num2 == 38:
        return("14/38 = 0.3684210526315789473684210526")
    if num1 == 14 and sign == '/' and num2 == 39:
        return("14/39 = 0.3589743589743589743589743590")
    if num1 == 14 and sign == '/' and num2 == 40:
        return("14/40 = 0.35")
    if num1 == 14 and sign == '/' and num2 == 41:
        return("14/41 = 0.3414634146341463414634146341")
    if num1 == 14 and sign == '/' and num2 == 42:
        return("14/42 = 0.3333333333333333333333333333")
    if num1 == 14 and sign == '/' and num2 == 43:
        return("14/43 = 0.3255813953488372093023255814")
    if num1 == 14 and sign == '/' and num2 == 44:
        return("14/44 = 0.3181818181818181818181818182")
    if num1 == 14 and sign == '/' and num2 == 45:
        return("14/45 = 0.3111111111111111111111111111")
    if num1 == 14 and sign == '/' and num2 == 46:
        return("14/46 = 0.3043478260869565217391304348")
    if num1 == 14 and sign == '/' and num2 == 47:
        return("14/47 = 0.2978723404255319148936170213")
    if num1 == 14 and sign == '/' and num2 == 48:
        return("14/48 = 0.2916666666666666666666666667")
    if num1 == 14 and sign == '/' and num2 == 49:
        return("14/49 = 0.2857142857142857142857142857")
    if num1 == 14 and sign == '/' and num2 == 50:
        return("14/50 = 0.28")
    if num1 == 15 and sign == '/' and num2 == 0:
        return("15/0 = Inf")
    if num1 == 15 and sign == '/' and num2 == 1:
        return("15/1 = 15")
    if num1 == 15 and sign == '/' and num2 == 2:
        return("15/2 = 7.5")
    if num1 == 15 and sign == '/' and num2 == 3:
        return("15/3 = 5")
    if num1 == 15 and sign == '/' and num2 == 4:
        return("15/4 = 3.75")
    if num1 == 15 and sign == '/' and num2 == 5:
        return("15/5 = 3")
    if num1 == 15 and sign == '/' and num2 == 6:
        return("15/6 = 2.5")
    if num1 == 15 and sign == '/' and num2 == 7:
        return("15/7 = 2.142857142857142857142857143")
    if num1 == 15 and sign == '/' and num2 == 8:
        return("15/8 = 1.875")
    if num1 == 15 and sign == '/' and num2 == 9:
        return("15/9 = 1.666666666666666666666666667")
    if num1 == 15 and sign == '/' and num2 == 10:
        return("15/10 = 1.5")
    if num1 == 15 and sign == '/' and num2 == 11:
        return("15/11 = 1.363636363636363636363636364")
    if num1 == 15 and sign == '/' and num2 == 12:
        return("15/12 = 1.25")
    if num1 == 15 and sign == '/' and num2 == 13:
        return("15/13 = 1.153846153846153846153846154")
    if num1 == 15 and sign == '/' and num2 == 14:
        return("15/14 = 1.071428571428571428571428571")
    if num1 == 15 and sign == '/' and num2 == 15:
        return("15/15 = 1")
    if num1 == 15 and sign == '/' and num2 == 16:
        return("15/16 = 0.9375")
    if num1 == 15 and sign == '/' and num2 == 17:
        return("15/17 = 0.8823529411764705882352941176")
    if num1 == 15 and sign == '/' and num2 == 18:
        return("15/18 = 0.8333333333333333333333333333")
    if num1 == 15 and sign == '/' and num2 == 19:
        return("15/19 = 0.7894736842105263157894736842")
    if num1 == 15 and sign == '/' and num2 == 20:
        return("15/20 = 0.75")
    if num1 == 15 and sign == '/' and num2 == 21:
        return("15/21 = 0.7142857142857142857142857143")
    if num1 == 15 and sign == '/' and num2 == 22:
        return("15/22 = 0.6818181818181818181818181818")
    if num1 == 15 and sign == '/' and num2 == 23:
        return("15/23 = 0.6521739130434782608695652174")
    if num1 == 15 and sign == '/' and num2 == 24:
        return("15/24 = 0.625")
    if num1 == 15 and sign == '/' and num2 == 25:
        return("15/25 = 0.6")
    if num1 == 15 and sign == '/' and num2 == 26:
        return("15/26 = 0.5769230769230769230769230769")
    if num1 == 15 and sign == '/' and num2 == 27:
        return("15/27 = 0.5555555555555555555555555556")
    if num1 == 15 and sign == '/' and num2 == 28:
        return("15/28 = 0.5357142857142857142857142857")
    if num1 == 15 and sign == '/' and num2 == 29:
        return("15/29 = 0.5172413793103448275862068966")
    if num1 == 15 and sign == '/' and num2 == 30:
        return("15/30 = 0.5")
    if num1 == 15 and sign == '/' and num2 == 31:
        return("15/31 = 0.4838709677419354838709677419")
    if num1 == 15 and sign == '/' and num2 == 32:
        return("15/32 = 0.46875")
    if num1 == 15 and sign == '/' and num2 == 33:
        return("15/33 = 0.4545454545454545454545454545")
    if num1 == 15 and sign == '/' and num2 == 34:
        return("15/34 = 0.4411764705882352941176470588")
    if num1 == 15 and sign == '/' and num2 == 35:
        return("15/35 = 0.4285714285714285714285714286")
    if num1 == 15 and sign == '/' and num2 == 36:
        return("15/36 = 0.4166666666666666666666666667")
    if num1 == 15 and sign == '/' and num2 == 37:
        return("15/37 = 0.4054054054054054054054054054")
    if num1 == 15 and sign == '/' and num2 == 38:
        return("15/38 = 0.3947368421052631578947368421")
    if num1 == 15 and sign == '/' and num2 == 39:
        return("15/39 = 0.3846153846153846153846153846")
    if num1 == 15 and sign == '/' and num2 == 40:
        return("15/40 = 0.375")
    if num1 == 15 and sign == '/' and num2 == 41:
        return("15/41 = 0.3658536585365853658536585366")
    if num1 == 15 and sign == '/' and num2 == 42:
        return("15/42 = 0.3571428571428571428571428571")
    if num1 == 15 and sign == '/' and num2 == 43:
        return("15/43 = 0.3488372093023255813953488372")
    if num1 == 15 and sign == '/' and num2 == 44:
        return("15/44 = 0.3409090909090909090909090909")
    if num1 == 15 and sign == '/' and num2 == 45:
        return("15/45 = 0.3333333333333333333333333333")
    if num1 == 15 and sign == '/' and num2 == 46:
        return("15/46 = 0.3260869565217391304347826087")
    if num1 == 15 and sign == '/' and num2 == 47:
        return("15/47 = 0.3191489361702127659574468085")
    if num1 == 15 and sign == '/' and num2 == 48:
        return("15/48 = 0.3125")
    if num1 == 15 and sign == '/' and num2 == 49:
        return("15/49 = 0.3061224489795918367346938776")
    if num1 == 15 and sign == '/' and num2 == 50:
        return("15/50 = 0.3")
    if num1 == 16 and sign == '/' and num2 == 0:
        return("16/0 = Inf")
    if num1 == 16 and sign == '/' and num2 == 1:
        return("16/1 = 16")
    if num1 == 16 and sign == '/' and num2 == 2:
        return("16/2 = 8")
    if num1 == 16 and sign == '/' and num2 == 3:
        return("16/3 = 5.333333333333333333333333333")
    if num1 == 16 and sign == '/' and num2 == 4:
        return("16/4 = 4")
    if num1 == 16 and sign == '/' and num2 == 5:
        return("16/5 = 3.2")
    if num1 == 16 and sign == '/' and num2 == 6:
        return("16/6 = 2.666666666666666666666666667")
    if num1 == 16 and sign == '/' and num2 == 7:
        return("16/7 = 2.285714285714285714285714286")
    if num1 == 16 and sign == '/' and num2 == 8:
        return("16/8 = 2")
    if num1 == 16 and sign == '/' and num2 == 9:
        return("16/9 = 1.777777777777777777777777778")
    if num1 == 16 and sign == '/' and num2 == 10:
        return("16/10 = 1.6")
    if num1 == 16 and sign == '/' and num2 == 11:
        return("16/11 = 1.454545454545454545454545455")
    if num1 == 16 and sign == '/' and num2 == 12:
        return("16/12 = 1.333333333333333333333333333")
    if num1 == 16 and sign == '/' and num2 == 13:
        return("16/13 = 1.230769230769230769230769231")
    if num1 == 16 and sign == '/' and num2 == 14:
        return("16/14 = 1.142857142857142857142857143")
    if num1 == 16 and sign == '/' and num2 == 15:
        return("16/15 = 1.066666666666666666666666667")
    if num1 == 16 and sign == '/' and num2 == 16:
        return("16/16 = 1")
    if num1 == 16 and sign == '/' and num2 == 17:
        return("16/17 = 0.9411764705882352941176470588")
    if num1 == 16 and sign == '/' and num2 == 18:
        return("16/18 = 0.8888888888888888888888888889")
    if num1 == 16 and sign == '/' and num2 == 19:
        return("16/19 = 0.8421052631578947368421052632")
    if num1 == 16 and sign == '/' and num2 == 20:
        return("16/20 = 0.8")
    if num1 == 16 and sign == '/' and num2 == 21:
        return("16/21 = 0.7619047619047619047619047619")
    if num1 == 16 and sign == '/' and num2 == 22:
        return("16/22 = 0.7272727272727272727272727273")
    if num1 == 16 and sign == '/' and num2 == 23:
        return("16/23 = 0.6956521739130434782608695652")
    if num1 == 16 and sign == '/' and num2 == 24:
        return("16/24 = 0.6666666666666666666666666667")
    if num1 == 16 and sign == '/' and num2 == 25:
        return("16/25 = 0.64")
    if num1 == 16 and sign == '/' and num2 == 26:
        return("16/26 = 0.6153846153846153846153846154")
    if num1 == 16 and sign == '/' and num2 == 27:
        return("16/27 = 0.5925925925925925925925925926")
    if num1 == 16 and sign == '/' and num2 == 28:
        return("16/28 = 0.5714285714285714285714285714")
    if num1 == 16 and sign == '/' and num2 == 29:
        return("16/29 = 0.5517241379310344827586206897")
    if num1 == 16 and sign == '/' and num2 == 30:
        return("16/30 = 0.5333333333333333333333333333")
    if num1 == 16 and sign == '/' and num2 == 31:
        return("16/31 = 0.5161290322580645161290322581")
    if num1 == 16 and sign == '/' and num2 == 32:
        return("16/32 = 0.5")
    if num1 == 16 and sign == '/' and num2 == 33:
        return("16/33 = 0.4848484848484848484848484848")
    if num1 == 16 and sign == '/' and num2 == 34:
        return("16/34 = 0.4705882352941176470588235294")
    if num1 == 16 and sign == '/' and num2 == 35:
        return("16/35 = 0.4571428571428571428571428571")
    if num1 == 16 and sign == '/' and num2 == 36:
        return("16/36 = 0.4444444444444444444444444444")
    if num1 == 16 and sign == '/' and num2 == 37:
        return("16/37 = 0.4324324324324324324324324324")
    if num1 == 16 and sign == '/' and num2 == 38:
        return("16/38 = 0.4210526315789473684210526316")
    if num1 == 16 and sign == '/' and num2 == 39:
        return("16/39 = 0.4102564102564102564102564103")
    if num1 == 16 and sign == '/' and num2 == 40:
        return("16/40 = 0.4")
    if num1 == 16 and sign == '/' and num2 == 41:
        return("16/41 = 0.3902439024390243902439024390")
    if num1 == 16 and sign == '/' and num2 == 42:
        return("16/42 = 0.3809523809523809523809523810")
    if num1 == 16 and sign == '/' and num2 == 43:
        return("16/43 = 0.3720930232558139534883720930")
    if num1 == 16 and sign == '/' and num2 == 44:
        return("16/44 = 0.3636363636363636363636363636")
    if num1 == 16 and sign == '/' and num2 == 45:
        return("16/45 = 0.3555555555555555555555555556")
    if num1 == 16 and sign == '/' and num2 == 46:
        return("16/46 = 0.3478260869565217391304347826")
    if num1 == 16 and sign == '/' and num2 == 47:
        return("16/47 = 0.3404255319148936170212765957")
    if num1 == 16 and sign == '/' and num2 == 48:
        return("16/48 = 0.3333333333333333333333333333")
    if num1 == 16 and sign == '/' and num2 == 49:
        return("16/49 = 0.3265306122448979591836734694")
    if num1 == 16 and sign == '/' and num2 == 50:
        return("16/50 = 0.32")
    if num1 == 17 and sign == '/' and num2 == 0:
        return("17/0 = Inf")
    if num1 == 17 and sign == '/' and num2 == 1:
        return("17/1 = 17")
    if num1 == 17 and sign == '/' and num2 == 2:
        return("17/2 = 8.5")
    if num1 == 17 and sign == '/' and num2 == 3:
        return("17/3 = 5.666666666666666666666666667")
    if num1 == 17 and sign == '/' and num2 == 4:
        return("17/4 = 4.25")
    if num1 == 17 and sign == '/' and num2 == 5:
        return("17/5 = 3.4")
    if num1 == 17 and sign == '/' and num2 == 6:
        return("17/6 = 2.833333333333333333333333333")
    if num1 == 17 and sign == '/' and num2 == 7:
        return("17/7 = 2.428571428571428571428571429")
    if num1 == 17 and sign == '/' and num2 == 8:
        return("17/8 = 2.125")
    if num1 == 17 and sign == '/' and num2 == 9:
        return("17/9 = 1.888888888888888888888888889")
    if num1 == 17 and sign == '/' and num2 == 10:
        return("17/10 = 1.7")
    if num1 == 17 and sign == '/' and num2 == 11:
        return("17/11 = 1.545454545454545454545454545")
    if num1 == 17 and sign == '/' and num2 == 12:
        return("17/12 = 1.416666666666666666666666667")
    if num1 == 17 and sign == '/' and num2 == 13:
        return("17/13 = 1.307692307692307692307692308")
    if num1 == 17 and sign == '/' and num2 == 14:
        return("17/14 = 1.214285714285714285714285714")
    if num1 == 17 and sign == '/' and num2 == 15:
        return("17/15 = 1.133333333333333333333333333")
    if num1 == 17 and sign == '/' and num2 == 16:
        return("17/16 = 1.0625")
    if num1 == 17 and sign == '/' and num2 == 17:
        return("17/17 = 1")
    if num1 == 17 and sign == '/' and num2 == 18:
        return("17/18 = 0.9444444444444444444444444444")
    if num1 == 17 and sign == '/' and num2 == 19:
        return("17/19 = 0.8947368421052631578947368421")
    if num1 == 17 and sign == '/' and num2 == 20:
        return("17/20 = 0.85")
    if num1 == 17 and sign == '/' and num2 == 21:
        return("17/21 = 0.8095238095238095238095238095")
    if num1 == 17 and sign == '/' and num2 == 22:
        return("17/22 = 0.7727272727272727272727272727")
    if num1 == 17 and sign == '/' and num2 == 23:
        return("17/23 = 0.7391304347826086956521739130")
    if num1 == 17 and sign == '/' and num2 == 24:
        return("17/24 = 0.7083333333333333333333333333")
    if num1 == 17 and sign == '/' and num2 == 25:
        return("17/25 = 0.68")
    if num1 == 17 and sign == '/' and num2 == 26:
        return("17/26 = 0.6538461538461538461538461538")
    if num1 == 17 and sign == '/' and num2 == 27:
        return("17/27 = 0.6296296296296296296296296296")
    if num1 == 17 and sign == '/' and num2 == 28:
        return("17/28 = 0.6071428571428571428571428571")
    if num1 == 17 and sign == '/' and num2 == 29:
        return("17/29 = 0.5862068965517241379310344828")
    if num1 == 17 and sign == '/' and num2 == 30:
        return("17/30 = 0.5666666666666666666666666667")
    if num1 == 17 and sign == '/' and num2 == 31:
        return("17/31 = 0.5483870967741935483870967742")
    if num1 == 17 and sign == '/' and num2 == 32:
        return("17/32 = 0.53125")
    if num1 == 17 and sign == '/' and num2 == 33:
        return("17/33 = 0.5151515151515151515151515152")
    if num1 == 17 and sign == '/' and num2 == 34:
        return("17/34 = 0.5")
    if num1 == 17 and sign == '/' and num2 == 35:
        return("17/35 = 0.4857142857142857142857142857")
    if num1 == 17 and sign == '/' and num2 == 36:
        return("17/36 = 0.4722222222222222222222222222")
    if num1 == 17 and sign == '/' and num2 == 37:
        return("17/37 = 0.4594594594594594594594594595")
    if num1 == 17 and sign == '/' and num2 == 38:
        return("17/38 = 0.4473684210526315789473684211")
    if num1 == 17 and sign == '/' and num2 == 39:
        return("17/39 = 0.4358974358974358974358974359")
    if num1 == 17 and sign == '/' and num2 == 40:
        return("17/40 = 0.425")
    if num1 == 17 and sign == '/' and num2 == 41:
        return("17/41 = 0.4146341463414634146341463415")
    if num1 == 17 and sign == '/' and num2 == 42:
        return("17/42 = 0.4047619047619047619047619048")
    if num1 == 17 and sign == '/' and num2 == 43:
        return("17/43 = 0.3953488372093023255813953488")
    if num1 == 17 and sign == '/' and num2 == 44:
        return("17/44 = 0.3863636363636363636363636364")
    if num1 == 17 and sign == '/' and num2 == 45:
        return("17/45 = 0.3777777777777777777777777778")
    if num1 == 17 and sign == '/' and num2 == 46:
        return("17/46 = 0.3695652173913043478260869565")
    if num1 == 17 and sign == '/' and num2 == 47:
        return("17/47 = 0.3617021276595744680851063830")
    if num1 == 17 and sign == '/' and num2 == 48:
        return("17/48 = 0.3541666666666666666666666667")
    if num1 == 17 and sign == '/' and num2 == 49:
        return("17/49 = 0.3469387755102040816326530612")
    if num1 == 17 and sign == '/' and num2 == 50:
        return("17/50 = 0.34")
    if num1 == 18 and sign == '/' and num2 == 0:
        return("18/0 = Inf")
    if num1 == 18 and sign == '/' and num2 == 1:
        return("18/1 = 18")
    if num1 == 18 and sign == '/' and num2 == 2:
        return("18/2 = 9")
    if num1 == 18 and sign == '/' and num2 == 3:
        return("18/3 = 6")
    if num1 == 18 and sign == '/' and num2 == 4:
        return("18/4 = 4.5")
    if num1 == 18 and sign == '/' and num2 == 5:
        return("18/5 = 3.6")
    if num1 == 18 and sign == '/' and num2 == 6:
        return("18/6 = 3")
    if num1 == 18 and sign == '/' and num2 == 7:
        return("18/7 = 2.571428571428571428571428571")
    if num1 == 18 and sign == '/' and num2 == 8:
        return("18/8 = 2.25")
    if num1 == 18 and sign == '/' and num2 == 9:
        return("18/9 = 2")
    if num1 == 18 and sign == '/' and num2 == 10:
        return("18/10 = 1.8")
    if num1 == 18 and sign == '/' and num2 == 11:
        return("18/11 = 1.636363636363636363636363636")
    if num1 == 18 and sign == '/' and num2 == 12:
        return("18/12 = 1.5")
    if num1 == 18 and sign == '/' and num2 == 13:
        return("18/13 = 1.384615384615384615384615385")
    if num1 == 18 and sign == '/' and num2 == 14:
        return("18/14 = 1.285714285714285714285714286")
    if num1 == 18 and sign == '/' and num2 == 15:
        return("18/15 = 1.2")
    if num1 == 18 and sign == '/' and num2 == 16:
        return("18/16 = 1.125")
    if num1 == 18 and sign == '/' and num2 == 17:
        return("18/17 = 1.058823529411764705882352941")
    if num1 == 18 and sign == '/' and num2 == 18:
        return("18/18 = 1")
    if num1 == 18 and sign == '/' and num2 == 19:
        return("18/19 = 0.9473684210526315789473684211")
    if num1 == 18 and sign == '/' and num2 == 20:
        return("18/20 = 0.9")
    if num1 == 18 and sign == '/' and num2 == 21:
        return("18/21 = 0.8571428571428571428571428571")
    if num1 == 18 and sign == '/' and num2 == 22:
        return("18/22 = 0.8181818181818181818181818182")
    if num1 == 18 and sign == '/' and num2 == 23:
        return("18/23 = 0.7826086956521739130434782609")
    if num1 == 18 and sign == '/' and num2 == 24:
        return("18/24 = 0.75")
    if num1 == 18 and sign == '/' and num2 == 25:
        return("18/25 = 0.72")
    if num1 == 18 and sign == '/' and num2 == 26:
        return("18/26 = 0.6923076923076923076923076923")
    if num1 == 18 and sign == '/' and num2 == 27:
        return("18/27 = 0.6666666666666666666666666667")
    if num1 == 18 and sign == '/' and num2 == 28:
        return("18/28 = 0.6428571428571428571428571429")
    if num1 == 18 and sign == '/' and num2 == 29:
        return("18/29 = 0.6206896551724137931034482759")
    if num1 == 18 and sign == '/' and num2 == 30:
        return("18/30 = 0.6")
    if num1 == 18 and sign == '/' and num2 == 31:
        return("18/31 = 0.5806451612903225806451612903")
    if num1 == 18 and sign == '/' and num2 == 32:
        return("18/32 = 0.5625")
    if num1 == 18 and sign == '/' and num2 == 33:
        return("18/33 = 0.5454545454545454545454545455")
    if num1 == 18 and sign == '/' and num2 == 34:
        return("18/34 = 0.5294117647058823529411764706")
    if num1 == 18 and sign == '/' and num2 == 35:
        return("18/35 = 0.5142857142857142857142857143")
    if num1 == 18 and sign == '/' and num2 == 36:
        return("18/36 = 0.5")
    if num1 == 18 and sign == '/' and num2 == 37:
        return("18/37 = 0.4864864864864864864864864865")
    if num1 == 18 and sign == '/' and num2 == 38:
        return("18/38 = 0.4736842105263157894736842105")
    if num1 == 18 and sign == '/' and num2 == 39:
        return("18/39 = 0.4615384615384615384615384615")
    if num1 == 18 and sign == '/' and num2 == 40:
        return("18/40 = 0.45")
    if num1 == 18 and sign == '/' and num2 == 41:
        return("18/41 = 0.4390243902439024390243902439")
    if num1 == 18 and sign == '/' and num2 == 42:
        return("18/42 = 0.4285714285714285714285714286")
    if num1 == 18 and sign == '/' and num2 == 43:
        return("18/43 = 0.4186046511627906976744186047")
    if num1 == 18 and sign == '/' and num2 == 44:
        return("18/44 = 0.4090909090909090909090909091")
    if num1 == 18 and sign == '/' and num2 == 45:
        return("18/45 = 0.4")
    if num1 == 18 and sign == '/' and num2 == 46:
        return("18/46 = 0.3913043478260869565217391304")
    if num1 == 18 and sign == '/' and num2 == 47:
        return("18/47 = 0.3829787234042553191489361702")
    if num1 == 18 and sign == '/' and num2 == 48:
        return("18/48 = 0.375")
    if num1 == 18 and sign == '/' and num2 == 49:
        return("18/49 = 0.3673469387755102040816326531")
    if num1 == 18 and sign == '/' and num2 == 50:
        return("18/50 = 0.36")
    if num1 == 19 and sign == '/' and num2 == 0:
        return("19/0 = Inf")
    if num1 == 19 and sign == '/' and num2 == 1:
        return("19/1 = 19")
    if num1 == 19 and sign == '/' and num2 == 2:
        return("19/2 = 9.5")
    if num1 == 19 and sign == '/' and num2 == 3:
        return("19/3 = 6.333333333333333333333333333")
    if num1 == 19 and sign == '/' and num2 == 4:
        return("19/4 = 4.75")
    if num1 == 19 and sign == '/' and num2 == 5:
        return("19/5 = 3.8")
    if num1 == 19 and sign == '/' and num2 == 6:
        return("19/6 = 3.166666666666666666666666667")
    if num1 == 19 and sign == '/' and num2 == 7:
        return("19/7 = 2.714285714285714285714285714")
    if num1 == 19 and sign == '/' and num2 == 8:
        return("19/8 = 2.375")
    if num1 == 19 and sign == '/' and num2 == 9:
        return("19/9 = 2.111111111111111111111111111")
    if num1 == 19 and sign == '/' and num2 == 10:
        return("19/10 = 1.9")
    if num1 == 19 and sign == '/' and num2 == 11:
        return("19/11 = 1.727272727272727272727272727")
    if num1 == 19 and sign == '/' and num2 == 12:
        return("19/12 = 1.583333333333333333333333333")
    if num1 == 19 and sign == '/' and num2 == 13:
        return("19/13 = 1.461538461538461538461538462")
    if num1 == 19 and sign == '/' and num2 == 14:
        return("19/14 = 1.357142857142857142857142857")
    if num1 == 19 and sign == '/' and num2 == 15:
        return("19/15 = 1.266666666666666666666666667")
    if num1 == 19 and sign == '/' and num2 == 16:
        return("19/16 = 1.1875")
    if num1 == 19 and sign == '/' and num2 == 17:
        return("19/17 = 1.117647058823529411764705882")
    if num1 == 19 and sign == '/' and num2 == 18:
        return("19/18 = 1.055555555555555555555555556")
    if num1 == 19 and sign == '/' and num2 == 19:
        return("19/19 = 1")
    if num1 == 19 and sign == '/' and num2 == 20:
        return("19/20 = 0.95")
    if num1 == 19 and sign == '/' and num2 == 21:
        return("19/21 = 0.9047619047619047619047619048")
    if num1 == 19 and sign == '/' and num2 == 22:
        return("19/22 = 0.8636363636363636363636363636")
    if num1 == 19 and sign == '/' and num2 == 23:
        return("19/23 = 0.8260869565217391304347826087")
    if num1 == 19 and sign == '/' and num2 == 24:
        return("19/24 = 0.7916666666666666666666666667")
    if num1 == 19 and sign == '/' and num2 == 25:
        return("19/25 = 0.76")
    if num1 == 19 and sign == '/' and num2 == 26:
        return("19/26 = 0.7307692307692307692307692308")
    if num1 == 19 and sign == '/' and num2 == 27:
        return("19/27 = 0.7037037037037037037037037037")
    if num1 == 19 and sign == '/' and num2 == 28:
        return("19/28 = 0.6785714285714285714285714286")
    if num1 == 19 and sign == '/' and num2 == 29:
        return("19/29 = 0.6551724137931034482758620690")
    if num1 == 19 and sign == '/' and num2 == 30:
        return("19/30 = 0.6333333333333333333333333333")
    if num1 == 19 and sign == '/' and num2 == 31:
        return("19/31 = 0.6129032258064516129032258065")
    if num1 == 19 and sign == '/' and num2 == 32:
        return("19/32 = 0.59375")
    if num1 == 19 and sign == '/' and num2 == 33:
        return("19/33 = 0.5757575757575757575757575758")
    if num1 == 19 and sign == '/' and num2 == 34:
        return("19/34 = 0.5588235294117647058823529412")
    if num1 == 19 and sign == '/' and num2 == 35:
        return("19/35 = 0.5428571428571428571428571429")
    if num1 == 19 and sign == '/' and num2 == 36:
        return("19/36 = 0.5277777777777777777777777778")
    if num1 == 19 and sign == '/' and num2 == 37:
        return("19/37 = 0.5135135135135135135135135135")
    if num1 == 19 and sign == '/' and num2 == 38:
        return("19/38 = 0.5")
    if num1 == 19 and sign == '/' and num2 == 39:
        return("19/39 = 0.4871794871794871794871794872")
    if num1 == 19 and sign == '/' and num2 == 40:
        return("19/40 = 0.475")
    if num1 == 19 and sign == '/' and num2 == 41:
        return("19/41 = 0.4634146341463414634146341463")
    if num1 == 19 and sign == '/' and num2 == 42:
        return("19/42 = 0.4523809523809523809523809524")
    if num1 == 19 and sign == '/' and num2 == 43:
        return("19/43 = 0.4418604651162790697674418605")
    if num1 == 19 and sign == '/' and num2 == 44:
        return("19/44 = 0.4318181818181818181818181818")
    if num1 == 19 and sign == '/' and num2 == 45:
        return("19/45 = 0.4222222222222222222222222222")
    if num1 == 19 and sign == '/' and num2 == 46:
        return("19/46 = 0.4130434782608695652173913043")
    if num1 == 19 and sign == '/' and num2 == 47:
        return("19/47 = 0.4042553191489361702127659574")
    if num1 == 19 and sign == '/' and num2 == 48:
        return("19/48 = 0.3958333333333333333333333333")
    if num1 == 19 and sign == '/' and num2 == 49:
        return("19/49 = 0.3877551020408163265306122449")
    if num1 == 19 and sign == '/' and num2 == 50:
        return("19/50 = 0.38")
    if num1 == 20 and sign == '/' and num2 == 0:
        return("20/0 = Inf")
    if num1 == 20 and sign == '/' and num2 == 1:
        return("20/1 = 20")
    if num1 == 20 and sign == '/' and num2 == 2:
        return("20/2 = 10")
    if num1 == 20 and sign == '/' and num2 == 3:
        return("20/3 = 6.666666666666666666666666667")
    if num1 == 20 and sign == '/' and num2 == 4:
        return("20/4 = 5")
    if num1 == 20 and sign == '/' and num2 == 5:
        return("20/5 = 4")
    if num1 == 20 and sign == '/' and num2 == 6:
        return("20/6 = 3.333333333333333333333333333")
    if num1 == 20 and sign == '/' and num2 == 7:
        return("20/7 = 2.857142857142857142857142857")
    if num1 == 20 and sign == '/' and num2 == 8:
        return("20/8 = 2.5")
    if num1 == 20 and sign == '/' and num2 == 9:
        return("20/9 = 2.222222222222222222222222222")
    if num1 == 20 and sign == '/' and num2 == 10:
        return("20/10 = 2")
    if num1 == 20 and sign == '/' and num2 == 11:
        return("20/11 = 1.818181818181818181818181818")
    if num1 == 20 and sign == '/' and num2 == 12:
        return("20/12 = 1.666666666666666666666666667")
    if num1 == 20 and sign == '/' and num2 == 13:
        return("20/13 = 1.538461538461538461538461538")
    if num1 == 20 and sign == '/' and num2 == 14:
        return("20/14 = 1.428571428571428571428571429")
    if num1 == 20 and sign == '/' and num2 == 15:
        return("20/15 = 1.333333333333333333333333333")
    if num1 == 20 and sign == '/' and num2 == 16:
        return("20/16 = 1.25")
    if num1 == 20 and sign == '/' and num2 == 17:
        return("20/17 = 1.176470588235294117647058824")
    if num1 == 20 and sign == '/' and num2 == 18:
        return("20/18 = 1.111111111111111111111111111")
    if num1 == 20 and sign == '/' and num2 == 19:
        return("20/19 = 1.052631578947368421052631579")
    if num1 == 20 and sign == '/' and num2 == 20:
        return("20/20 = 1")
    if num1 == 20 and sign == '/' and num2 == 21:
        return("20/21 = 0.9523809523809523809523809524")
    if num1 == 20 and sign == '/' and num2 == 22:
        return("20/22 = 0.9090909090909090909090909091")
    if num1 == 20 and sign == '/' and num2 == 23:
        return("20/23 = 0.8695652173913043478260869565")
    if num1 == 20 and sign == '/' and num2 == 24:
        return("20/24 = 0.8333333333333333333333333333")
    if num1 == 20 and sign == '/' and num2 == 25:
        return("20/25 = 0.8")
    if num1 == 20 and sign == '/' and num2 == 26:
        return("20/26 = 0.7692307692307692307692307692")
    if num1 == 20 and sign == '/' and num2 == 27:
        return("20/27 = 0.7407407407407407407407407407")
    if num1 == 20 and sign == '/' and num2 == 28:
        return("20/28 = 0.7142857142857142857142857143")
    if num1 == 20 and sign == '/' and num2 == 29:
        return("20/29 = 0.6896551724137931034482758621")
    if num1 == 20 and sign == '/' and num2 == 30:
        return("20/30 = 0.6666666666666666666666666667")
    if num1 == 20 and sign == '/' and num2 == 31:
        return("20/31 = 0.6451612903225806451612903226")
    if num1 == 20 and sign == '/' and num2 == 32:
        return("20/32 = 0.625")
    if num1 == 20 and sign == '/' and num2 == 33:
        return("20/33 = 0.6060606060606060606060606061")
    if num1 == 20 and sign == '/' and num2 == 34:
        return("20/34 = 0.5882352941176470588235294118")
    if num1 == 20 and sign == '/' and num2 == 35:
        return("20/35 = 0.5714285714285714285714285714")
    if num1 == 20 and sign == '/' and num2 == 36:
        return("20/36 = 0.5555555555555555555555555556")
    if num1 == 20 and sign == '/' and num2 == 37:
        return("20/37 = 0.5405405405405405405405405405")
    if num1 == 20 and sign == '/' and num2 == 38:
        return("20/38 = 0.5263157894736842105263157895")
    if num1 == 20 and sign == '/' and num2 == 39:
        return("20/39 = 0.5128205128205128205128205128")
    if num1 == 20 and sign == '/' and num2 == 40:
        return("20/40 = 0.5")
    if num1 == 20 and sign == '/' and num2 == 41:
        return("20/41 = 0.4878048780487804878048780488")
    if num1 == 20 and sign == '/' and num2 == 42:
        return("20/42 = 0.4761904761904761904761904762")
    if num1 == 20 and sign == '/' and num2 == 43:
        return("20/43 = 0.4651162790697674418604651163")
    if num1 == 20 and sign == '/' and num2 == 44:
        return("20/44 = 0.4545454545454545454545454545")
    if num1 == 20 and sign == '/' and num2 == 45:
        return("20/45 = 0.4444444444444444444444444444")
    if num1 == 20 and sign == '/' and num2 == 46:
        return("20/46 = 0.4347826086956521739130434783")
    if num1 == 20 and sign == '/' and num2 == 47:
        return("20/47 = 0.4255319148936170212765957447")
    if num1 == 20 and sign == '/' and num2 == 48:
        return("20/48 = 0.4166666666666666666666666667")
    if num1 == 20 and sign == '/' and num2 == 49:
        return("20/49 = 0.4081632653061224489795918367")
    if num1 == 20 and sign == '/' and num2 == 50:
        return("20/50 = 0.4")
    if num1 == 21 and sign == '/' and num2 == 0:
        return("21/0 = Inf")
    if num1 == 21 and sign == '/' and num2 == 1:
        return("21/1 = 21")
    if num1 == 21 and sign == '/' and num2 == 2:
        return("21/2 = 10.5")
    if num1 == 21 and sign == '/' and num2 == 3:
        return("21/3 = 7")
    if num1 == 21 and sign == '/' and num2 == 4:
        return("21/4 = 5.25")
    if num1 == 21 and sign == '/' and num2 == 5:
        return("21/5 = 4.2")
    if num1 == 21 and sign == '/' and num2 == 6:
        return("21/6 = 3.5")
    if num1 == 21 and sign == '/' and num2 == 7:
        return("21/7 = 3")
    if num1 == 21 and sign == '/' and num2 == 8:
        return("21/8 = 2.625")
    if num1 == 21 and sign == '/' and num2 == 9:
        return("21/9 = 2.333333333333333333333333333")
    if num1 == 21 and sign == '/' and num2 == 10:
        return("21/10 = 2.1")
    if num1 == 21 and sign == '/' and num2 == 11:
        return("21/11 = 1.909090909090909090909090909")
    if num1 == 21 and sign == '/' and num2 == 12:
        return("21/12 = 1.75")
    if num1 == 21 and sign == '/' and num2 == 13:
        return("21/13 = 1.615384615384615384615384615")
    if num1 == 21 and sign == '/' and num2 == 14:
        return("21/14 = 1.5")
    if num1 == 21 and sign == '/' and num2 == 15:
        return("21/15 = 1.4")
    if num1 == 21 and sign == '/' and num2 == 16:
        return("21/16 = 1.3125")
    if num1 == 21 and sign == '/' and num2 == 17:
        return("21/17 = 1.235294117647058823529411765")
    if num1 == 21 and sign == '/' and num2 == 18:
        return("21/18 = 1.166666666666666666666666667")
    if num1 == 21 and sign == '/' and num2 == 19:
        return("21/19 = 1.105263157894736842105263158")
    if num1 == 21 and sign == '/' and num2 == 20:
        return("21/20 = 1.05")
    if num1 == 21 and sign == '/' and num2 == 21:
        return("21/21 = 1")
    if num1 == 21 and sign == '/' and num2 == 22:
        return("21/22 = 0.9545454545454545454545454545")
    if num1 == 21 and sign == '/' and num2 == 23:
        return("21/23 = 0.9130434782608695652173913043")
    if num1 == 21 and sign == '/' and num2 == 24:
        return("21/24 = 0.875")
    if num1 == 21 and sign == '/' and num2 == 25:
        return("21/25 = 0.84")
    if num1 == 21 and sign == '/' and num2 == 26:
        return("21/26 = 0.8076923076923076923076923077")
    if num1 == 21 and sign == '/' and num2 == 27:
        return("21/27 = 0.7777777777777777777777777778")
    if num1 == 21 and sign == '/' and num2 == 28:
        return("21/28 = 0.75")
    if num1 == 21 and sign == '/' and num2 == 29:
        return("21/29 = 0.7241379310344827586206896552")
    if num1 == 21 and sign == '/' and num2 == 30:
        return("21/30 = 0.7")
    if num1 == 21 and sign == '/' and num2 == 31:
        return("21/31 = 0.6774193548387096774193548387")
    if num1 == 21 and sign == '/' and num2 == 32:
        return("21/32 = 0.65625")
    if num1 == 21 and sign == '/' and num2 == 33:
        return("21/33 = 0.6363636363636363636363636364")
    if num1 == 21 and sign == '/' and num2 == 34:
        return("21/34 = 0.6176470588235294117647058824")
    if num1 == 21 and sign == '/' and num2 == 35:
        return("21/35 = 0.6")
    if num1 == 21 and sign == '/' and num2 == 36:
        return("21/36 = 0.5833333333333333333333333333")
    if num1 == 21 and sign == '/' and num2 == 37:
        return("21/37 = 0.5675675675675675675675675676")
    if num1 == 21 and sign == '/' and num2 == 38:
        return("21/38 = 0.5526315789473684210526315789")
    if num1 == 21 and sign == '/' and num2 == 39:
        return("21/39 = 0.5384615384615384615384615385")
    if num1 == 21 and sign == '/' and num2 == 40:
        return("21/40 = 0.525")
    if num1 == 21 and sign == '/' and num2 == 41:
        return("21/41 = 0.5121951219512195121951219512")
    if num1 == 21 and sign == '/' and num2 == 42:
        return("21/42 = 0.5")
    if num1 == 21 and sign == '/' and num2 == 43:
        return("21/43 = 0.4883720930232558139534883721")
    if num1 == 21 and sign == '/' and num2 == 44:
        return("21/44 = 0.4772727272727272727272727273")
    if num1 == 21 and sign == '/' and num2 == 45:
        return("21/45 = 0.4666666666666666666666666667")
    if num1 == 21 and sign == '/' and num2 == 46:
        return("21/46 = 0.4565217391304347826086956522")
    if num1 == 21 and sign == '/' and num2 == 47:
        return("21/47 = 0.4468085106382978723404255319")
    if num1 == 21 and sign == '/' and num2 == 48:
        return("21/48 = 0.4375")
    if num1 == 21 and sign == '/' and num2 == 49:
        return("21/49 = 0.4285714285714285714285714286")
    if num1 == 21 and sign == '/' and num2 == 50:
        return("21/50 = 0.42")
    if num1 == 22 and sign == '/' and num2 == 0:
        return("22/0 = Inf")
    if num1 == 22 and sign == '/' and num2 == 1:
        return("22/1 = 22")
    if num1 == 22 and sign == '/' and num2 == 2:
        return("22/2 = 11")
    if num1 == 22 and sign == '/' and num2 == 3:
        return("22/3 = 7.333333333333333333333333333")
    if num1 == 22 and sign == '/' and num2 == 4:
        return("22/4 = 5.5")
    if num1 == 22 and sign == '/' and num2 == 5:
        return("22/5 = 4.4")
    if num1 == 22 and sign == '/' and num2 == 6:
        return("22/6 = 3.666666666666666666666666667")
    if num1 == 22 and sign == '/' and num2 == 7:
        return("22/7 = 3.142857142857142857142857143")
    if num1 == 22 and sign == '/' and num2 == 8:
        return("22/8 = 2.75")
    if num1 == 22 and sign == '/' and num2 == 9:
        return("22/9 = 2.444444444444444444444444444")
    if num1 == 22 and sign == '/' and num2 == 10:
        return("22/10 = 2.2")
    if num1 == 22 and sign == '/' and num2 == 11:
        return("22/11 = 2")
    if num1 == 22 and sign == '/' and num2 == 12:
        return("22/12 = 1.833333333333333333333333333")
    if num1 == 22 and sign == '/' and num2 == 13:
        return("22/13 = 1.692307692307692307692307692")
    if num1 == 22 and sign == '/' and num2 == 14:
        return("22/14 = 1.571428571428571428571428571")
    if num1 == 22 and sign == '/' and num2 == 15:
        return("22/15 = 1.466666666666666666666666667")
    if num1 == 22 and sign == '/' and num2 == 16:
        return("22/16 = 1.375")
    if num1 == 22 and sign == '/' and num2 == 17:
        return("22/17 = 1.294117647058823529411764706")
    if num1 == 22 and sign == '/' and num2 == 18:
        return("22/18 = 1.222222222222222222222222222")
    if num1 == 22 and sign == '/' and num2 == 19:
        return("22/19 = 1.157894736842105263157894737")
    if num1 == 22 and sign == '/' and num2 == 20:
        return("22/20 = 1.1")
    if num1 == 22 and sign == '/' and num2 == 21:
        return("22/21 = 1.047619047619047619047619048")
    if num1 == 22 and sign == '/' and num2 == 22:
        return("22/22 = 1")
    if num1 == 22 and sign == '/' and num2 == 23:
        return("22/23 = 0.9565217391304347826086956522")
    if num1 == 22 and sign == '/' and num2 == 24:
        return("22/24 = 0.9166666666666666666666666667")
    if num1 == 22 and sign == '/' and num2 == 25:
        return("22/25 = 0.88")
    if num1 == 22 and sign == '/' and num2 == 26:
        return("22/26 = 0.8461538461538461538461538462")
    if num1 == 22 and sign == '/' and num2 == 27:
        return("22/27 = 0.8148148148148148148148148148")
    if num1 == 22 and sign == '/' and num2 == 28:
        return("22/28 = 0.7857142857142857142857142857")
    if num1 == 22 and sign == '/' and num2 == 29:
        return("22/29 = 0.7586206896551724137931034483")
    if num1 == 22 and sign == '/' and num2 == 30:
        return("22/30 = 0.7333333333333333333333333333")
    if num1 == 22 and sign == '/' and num2 == 31:
        return("22/31 = 0.7096774193548387096774193548")
    if num1 == 22 and sign == '/' and num2 == 32:
        return("22/32 = 0.6875")
    if num1 == 22 and sign == '/' and num2 == 33:
        return("22/33 = 0.6666666666666666666666666667")
    if num1 == 22 and sign == '/' and num2 == 34:
        return("22/34 = 0.6470588235294117647058823529")
    if num1 == 22 and sign == '/' and num2 == 35:
        return("22/35 = 0.6285714285714285714285714286")
    if num1 == 22 and sign == '/' and num2 == 36:
        return("22/36 = 0.6111111111111111111111111111")
    if num1 == 22 and sign == '/' and num2 == 37:
        return("22/37 = 0.5945945945945945945945945946")
    if num1 == 22 and sign == '/' and num2 == 38:
        return("22/38 = 0.5789473684210526315789473684")
    if num1 == 22 and sign == '/' and num2 == 39:
        return("22/39 = 0.5641025641025641025641025641")
    if num1 == 22 and sign == '/' and num2 == 40:
        return("22/40 = 0.55")
    if num1 == 22 and sign == '/' and num2 == 41:
        return("22/41 = 0.5365853658536585365853658537")
    if num1 == 22 and sign == '/' and num2 == 42:
        return("22/42 = 0.5238095238095238095238095238")
    if num1 == 22 and sign == '/' and num2 == 43:
        return("22/43 = 0.5116279069767441860465116279")
    if num1 == 22 and sign == '/' and num2 == 44:
        return("22/44 = 0.5")
    if num1 == 22 and sign == '/' and num2 == 45:
        return("22/45 = 0.4888888888888888888888888889")
    if num1 == 22 and sign == '/' and num2 == 46:
        return("22/46 = 0.4782608695652173913043478261")
    if num1 == 22 and sign == '/' and num2 == 47:
        return("22/47 = 0.4680851063829787234042553191")
    if num1 == 22 and sign == '/' and num2 == 48:
        return("22/48 = 0.4583333333333333333333333333")
    if num1 == 22 and sign == '/' and num2 == 49:
        return("22/49 = 0.4489795918367346938775510204")
    if num1 == 22 and sign == '/' and num2 == 50:
        return("22/50 = 0.44")
    if num1 == 23 and sign == '/' and num2 == 0:
        return("23/0 = Inf")
    if num1 == 23 and sign == '/' and num2 == 1:
        return("23/1 = 23")
    if num1 == 23 and sign == '/' and num2 == 2:
        return("23/2 = 11.5")
    if num1 == 23 and sign == '/' and num2 == 3:
        return("23/3 = 7.666666666666666666666666667")
    if num1 == 23 and sign == '/' and num2 == 4:
        return("23/4 = 5.75")
    if num1 == 23 and sign == '/' and num2 == 5:
        return("23/5 = 4.6")
    if num1 == 23 and sign == '/' and num2 == 6:
        return("23/6 = 3.833333333333333333333333333")
    if num1 == 23 and sign == '/' and num2 == 7:
        return("23/7 = 3.285714285714285714285714286")
    if num1 == 23 and sign == '/' and num2 == 8:
        return("23/8 = 2.875")
    if num1 == 23 and sign == '/' and num2 == 9:
        return("23/9 = 2.555555555555555555555555556")
    if num1 == 23 and sign == '/' and num2 == 10:
        return("23/10 = 2.3")
    if num1 == 23 and sign == '/' and num2 == 11:
        return("23/11 = 2.090909090909090909090909091")
    if num1 == 23 and sign == '/' and num2 == 12:
        return("23/12 = 1.916666666666666666666666667")
    if num1 == 23 and sign == '/' and num2 == 13:
        return("23/13 = 1.769230769230769230769230769")
    if num1 == 23 and sign == '/' and num2 == 14:
        return("23/14 = 1.642857142857142857142857143")
    if num1 == 23 and sign == '/' and num2 == 15:
        return("23/15 = 1.533333333333333333333333333")
    if num1 == 23 and sign == '/' and num2 == 16:
        return("23/16 = 1.4375")
    if num1 == 23 and sign == '/' and num2 == 17:
        return("23/17 = 1.352941176470588235294117647")
    if num1 == 23 and sign == '/' and num2 == 18:
        return("23/18 = 1.277777777777777777777777778")
    if num1 == 23 and sign == '/' and num2 == 19:
        return("23/19 = 1.210526315789473684210526316")
    if num1 == 23 and sign == '/' and num2 == 20:
        return("23/20 = 1.15")
    if num1 == 23 and sign == '/' and num2 == 21:
        return("23/21 = 1.095238095238095238095238095")
    if num1 == 23 and sign == '/' and num2 == 22:
        return("23/22 = 1.045454545454545454545454545")
    if num1 == 23 and sign == '/' and num2 == 23:
        return("23/23 = 1")
    if num1 == 23 and sign == '/' and num2 == 24:
        return("23/24 = 0.9583333333333333333333333333")
    if num1 == 23 and sign == '/' and num2 == 25:
        return("23/25 = 0.92")
    if num1 == 23 and sign == '/' and num2 == 26:
        return("23/26 = 0.8846153846153846153846153846")
    if num1 == 23 and sign == '/' and num2 == 27:
        return("23/27 = 0.8518518518518518518518518519")
    if num1 == 23 and sign == '/' and num2 == 28:
        return("23/28 = 0.8214285714285714285714285714")
    if num1 == 23 and sign == '/' and num2 == 29:
        return("23/29 = 0.7931034482758620689655172414")
    if num1 == 23 and sign == '/' and num2 == 30:
        return("23/30 = 0.7666666666666666666666666667")
    if num1 == 23 and sign == '/' and num2 == 31:
        return("23/31 = 0.7419354838709677419354838710")
    if num1 == 23 and sign == '/' and num2 == 32:
        return("23/32 = 0.71875")
    if num1 == 23 and sign == '/' and num2 == 33:
        return("23/33 = 0.6969696969696969696969696970")
    if num1 == 23 and sign == '/' and num2 == 34:
        return("23/34 = 0.6764705882352941176470588235")
    if num1 == 23 and sign == '/' and num2 == 35:
        return("23/35 = 0.6571428571428571428571428571")
    if num1 == 23 and sign == '/' and num2 == 36:
        return("23/36 = 0.6388888888888888888888888889")
    if num1 == 23 and sign == '/' and num2 == 37:
        return("23/37 = 0.6216216216216216216216216216")
    if num1 == 23 and sign == '/' and num2 == 38:
        return("23/38 = 0.6052631578947368421052631579")
    if num1 == 23 and sign == '/' and num2 == 39:
        return("23/39 = 0.5897435897435897435897435897")
    if num1 == 23 and sign == '/' and num2 == 40:
        return("23/40 = 0.575")
    if num1 == 23 and sign == '/' and num2 == 41:
        return("23/41 = 0.5609756097560975609756097561")
    if num1 == 23 and sign == '/' and num2 == 42:
        return("23/42 = 0.5476190476190476190476190476")
    if num1 == 23 and sign == '/' and num2 == 43:
        return("23/43 = 0.5348837209302325581395348837")
    if num1 == 23 and sign == '/' and num2 == 44:
        return("23/44 = 0.5227272727272727272727272727")
    if num1 == 23 and sign == '/' and num2 == 45:
        return("23/45 = 0.5111111111111111111111111111")
    if num1 == 23 and sign == '/' and num2 == 46:
        return("23/46 = 0.5")
    if num1 == 23 and sign == '/' and num2 == 47:
        return("23/47 = 0.4893617021276595744680851064")
    if num1 == 23 and sign == '/' and num2 == 48:
        return("23/48 = 0.4791666666666666666666666667")
    if num1 == 23 and sign == '/' and num2 == 49:
        return("23/49 = 0.4693877551020408163265306122")
    if num1 == 23 and sign == '/' and num2 == 50:
        return("23/50 = 0.46")
    if num1 == 24 and sign == '/' and num2 == 0:
        return("24/0 = Inf")
    if num1 == 24 and sign == '/' and num2 == 1:
        return("24/1 = 24")
    if num1 == 24 and sign == '/' and num2 == 2:
        return("24/2 = 12")
    if num1 == 24 and sign == '/' and num2 == 3:
        return("24/3 = 8")
    if num1 == 24 and sign == '/' and num2 == 4:
        return("24/4 = 6")
    if num1 == 24 and sign == '/' and num2 == 5:
        return("24/5 = 4.8")
    if num1 == 24 and sign == '/' and num2 == 6:
        return("24/6 = 4")
    if num1 == 24 and sign == '/' and num2 == 7:
        return("24/7 = 3.428571428571428571428571429")
    if num1 == 24 and sign == '/' and num2 == 8:
        return("24/8 = 3")
    if num1 == 24 and sign == '/' and num2 == 9:
        return("24/9 = 2.666666666666666666666666667")
    if num1 == 24 and sign == '/' and num2 == 10:
        return("24/10 = 2.4")
    if num1 == 24 and sign == '/' and num2 == 11:
        return("24/11 = 2.181818181818181818181818182")
    if num1 == 24 and sign == '/' and num2 == 12:
        return("24/12 = 2")
    if num1 == 24 and sign == '/' and num2 == 13:
        return("24/13 = 1.846153846153846153846153846")
    if num1 == 24 and sign == '/' and num2 == 14:
        return("24/14 = 1.714285714285714285714285714")
    if num1 == 24 and sign == '/' and num2 == 15:
        return("24/15 = 1.6")
    if num1 == 24 and sign == '/' and num2 == 16:
        return("24/16 = 1.5")
    if num1 == 24 and sign == '/' and num2 == 17:
        return("24/17 = 1.411764705882352941176470588")
    if num1 == 24 and sign == '/' and num2 == 18:
        return("24/18 = 1.333333333333333333333333333")
    if num1 == 24 and sign == '/' and num2 == 19:
        return("24/19 = 1.263157894736842105263157895")
    if num1 == 24 and sign == '/' and num2 == 20:
        return("24/20 = 1.2")
    if num1 == 24 and sign == '/' and num2 == 21:
        return("24/21 = 1.142857142857142857142857143")
    if num1 == 24 and sign == '/' and num2 == 22:
        return("24/22 = 1.090909090909090909090909091")
    if num1 == 24 and sign == '/' and num2 == 23:
        return("24/23 = 1.043478260869565217391304348")
    if num1 == 24 and sign == '/' and num2 == 24:
        return("24/24 = 1")
    if num1 == 24 and sign == '/' and num2 == 25:
        return("24/25 = 0.96")
    if num1 == 24 and sign == '/' and num2 == 26:
        return("24/26 = 0.9230769230769230769230769231")
    if num1 == 24 and sign == '/' and num2 == 27:
        return("24/27 = 0.8888888888888888888888888889")
    if num1 == 24 and sign == '/' and num2 == 28:
        return("24/28 = 0.8571428571428571428571428571")
    if num1 == 24 and sign == '/' and num2 == 29:
        return("24/29 = 0.8275862068965517241379310345")
    if num1 == 24 and sign == '/' and num2 == 30:
        return("24/30 = 0.8")
    if num1 == 24 and sign == '/' and num2 == 31:
        return("24/31 = 0.7741935483870967741935483871")
    if num1 == 24 and sign == '/' and num2 == 32:
        return("24/32 = 0.75")
    if num1 == 24 and sign == '/' and num2 == 33:
        return("24/33 = 0.7272727272727272727272727273")
    if num1 == 24 and sign == '/' and num2 == 34:
        return("24/34 = 0.7058823529411764705882352941")
    if num1 == 24 and sign == '/' and num2 == 35:
        return("24/35 = 0.6857142857142857142857142857")
    if num1 == 24 and sign == '/' and num2 == 36:
        return("24/36 = 0.6666666666666666666666666667")
    if num1 == 24 and sign == '/' and num2 == 37:
        return("24/37 = 0.6486486486486486486486486486")
    if num1 == 24 and sign == '/' and num2 == 38:
        return("24/38 = 0.6315789473684210526315789474")
    if num1 == 24 and sign == '/' and num2 == 39:
        return("24/39 = 0.6153846153846153846153846154")
    if num1 == 24 and sign == '/' and num2 == 40:
        return("24/40 = 0.6")
    if num1 == 24 and sign == '/' and num2 == 41:
        return("24/41 = 0.5853658536585365853658536585")
    if num1 == 24 and sign == '/' and num2 == 42:
        return("24/42 = 0.5714285714285714285714285714")
    if num1 == 24 and sign == '/' and num2 == 43:
        return("24/43 = 0.5581395348837209302325581395")
    if num1 == 24 and sign == '/' and num2 == 44:
        return("24/44 = 0.5454545454545454545454545455")
    if num1 == 24 and sign == '/' and num2 == 45:
        return("24/45 = 0.5333333333333333333333333333")
    if num1 == 24 and sign == '/' and num2 == 46:
        return("24/46 = 0.5217391304347826086956521739")
    if num1 == 24 and sign == '/' and num2 == 47:
        return("24/47 = 0.5106382978723404255319148936")
    if num1 == 24 and sign == '/' and num2 == 48:
        return("24/48 = 0.5")
    if num1 == 24 and sign == '/' and num2 == 49:
        return("24/49 = 0.4897959183673469387755102041")
    if num1 == 24 and sign == '/' and num2 == 50:
        return("24/50 = 0.48")
    if num1 == 25 and sign == '/' and num2 == 0:
        return("25/0 = Inf")
    if num1 == 25 and sign == '/' and num2 == 1:
        return("25/1 = 25")
    if num1 == 25 and sign == '/' and num2 == 2:
        return("25/2 = 12.5")
    if num1 == 25 and sign == '/' and num2 == 3:
        return("25/3 = 8.333333333333333333333333333")
    if num1 == 25 and sign == '/' and num2 == 4:
        return("25/4 = 6.25")
    if num1 == 25 and sign == '/' and num2 == 5:
        return("25/5 = 5")
    if num1 == 25 and sign == '/' and num2 == 6:
        return("25/6 = 4.166666666666666666666666667")
    if num1 == 25 and sign == '/' and num2 == 7:
        return("25/7 = 3.571428571428571428571428571")
    if num1 == 25 and sign == '/' and num2 == 8:
        return("25/8 = 3.125")
    if num1 == 25 and sign == '/' and num2 == 9:
        return("25/9 = 2.777777777777777777777777778")
    if num1 == 25 and sign == '/' and num2 == 10:
        return("25/10 = 2.5")
    if num1 == 25 and sign == '/' and num2 == 11:
        return("25/11 = 2.272727272727272727272727273")
    if num1 == 25 and sign == '/' and num2 == 12:
        return("25/12 = 2.083333333333333333333333333")
    if num1 == 25 and sign == '/' and num2 == 13:
        return("25/13 = 1.923076923076923076923076923")
    if num1 == 25 and sign == '/' and num2 == 14:
        return("25/14 = 1.785714285714285714285714286")
    if num1 == 25 and sign == '/' and num2 == 15:
        return("25/15 = 1.666666666666666666666666667")
    if num1 == 25 and sign == '/' and num2 == 16:
        return("25/16 = 1.5625")
    if num1 == 25 and sign == '/' and num2 == 17:
        return("25/17 = 1.470588235294117647058823529")
    if num1 == 25 and sign == '/' and num2 == 18:
        return("25/18 = 1.388888888888888888888888889")
    if num1 == 25 and sign == '/' and num2 == 19:
        return("25/19 = 1.315789473684210526315789474")
    if num1 == 25 and sign == '/' and num2 == 20:
        return("25/20 = 1.25")
    if num1 == 25 and sign == '/' and num2 == 21:
        return("25/21 = 1.190476190476190476190476190")
    if num1 == 25 and sign == '/' and num2 == 22:
        return("25/22 = 1.136363636363636363636363636")
    if num1 == 25 and sign == '/' and num2 == 23:
        return("25/23 = 1.086956521739130434782608696")
    if num1 == 25 and sign == '/' and num2 == 24:
        return("25/24 = 1.041666666666666666666666667")
    if num1 == 25 and sign == '/' and num2 == 25:
        return("25/25 = 1")
    if num1 == 25 and sign == '/' and num2 == 26:
        return("25/26 = 0.9615384615384615384615384615")
    if num1 == 25 and sign == '/' and num2 == 27:
        return("25/27 = 0.9259259259259259259259259259")
    if num1 == 25 and sign == '/' and num2 == 28:
        return("25/28 = 0.8928571428571428571428571429")
    if num1 == 25 and sign == '/' and num2 == 29:
        return("25/29 = 0.8620689655172413793103448276")
    if num1 == 25 and sign == '/' and num2 == 30:
        return("25/30 = 0.8333333333333333333333333333")
    if num1 == 25 and sign == '/' and num2 == 31:
        return("25/31 = 0.8064516129032258064516129032")
    if num1 == 25 and sign == '/' and num2 == 32:
        return("25/32 = 0.78125")
    if num1 == 25 and sign == '/' and num2 == 33:
        return("25/33 = 0.7575757575757575757575757576")
    if num1 == 25 and sign == '/' and num2 == 34:
        return("25/34 = 0.7352941176470588235294117647")
    if num1 == 25 and sign == '/' and num2 == 35:
        return("25/35 = 0.7142857142857142857142857143")
    if num1 == 25 and sign == '/' and num2 == 36:
        return("25/36 = 0.6944444444444444444444444444")
    if num1 == 25 and sign == '/' and num2 == 37:
        return("25/37 = 0.6756756756756756756756756757")
    if num1 == 25 and sign == '/' and num2 == 38:
        return("25/38 = 0.6578947368421052631578947368")
    if num1 == 25 and sign == '/' and num2 == 39:
        return("25/39 = 0.6410256410256410256410256410")
    if num1 == 25 and sign == '/' and num2 == 40:
        return("25/40 = 0.625")
    if num1 == 25 and sign == '/' and num2 == 41:
        return("25/41 = 0.6097560975609756097560975610")
    if num1 == 25 and sign == '/' and num2 == 42:
        return("25/42 = 0.5952380952380952380952380952")
    if num1 == 25 and sign == '/' and num2 == 43:
        return("25/43 = 0.5813953488372093023255813953")
    if num1 == 25 and sign == '/' and num2 == 44:
        return("25/44 = 0.5681818181818181818181818182")
    if num1 == 25 and sign == '/' and num2 == 45:
        return("25/45 = 0.5555555555555555555555555556")
    if num1 == 25 and sign == '/' and num2 == 46:
        return("25/46 = 0.5434782608695652173913043478")
    if num1 == 25 and sign == '/' and num2 == 47:
        return("25/47 = 0.5319148936170212765957446809")
    if num1 == 25 and sign == '/' and num2 == 48:
        return("25/48 = 0.5208333333333333333333333333")
    if num1 == 25 and sign == '/' and num2 == 49:
        return("25/49 = 0.5102040816326530612244897959")
    if num1 == 25 and sign == '/' and num2 == 50:
        return("25/50 = 0.5")
    if num1 == 26 and sign == '/' and num2 == 0:
        return("26/0 = Inf")
    if num1 == 26 and sign == '/' and num2 == 1:
        return("26/1 = 26")
    if num1 == 26 and sign == '/' and num2 == 2:
        return("26/2 = 13")
    if num1 == 26 and sign == '/' and num2 == 3:
        return("26/3 = 8.666666666666666666666666667")
    if num1 == 26 and sign == '/' and num2 == 4:
        return("26/4 = 6.5")
    if num1 == 26 and sign == '/' and num2 == 5:
        return("26/5 = 5.2")
    if num1 == 26 and sign == '/' and num2 == 6:
        return("26/6 = 4.333333333333333333333333333")
    if num1 == 26 and sign == '/' and num2 == 7:
        return("26/7 = 3.714285714285714285714285714")
    if num1 == 26 and sign == '/' and num2 == 8:
        return("26/8 = 3.25")
    if num1 == 26 and sign == '/' and num2 == 9:
        return("26/9 = 2.888888888888888888888888889")
    if num1 == 26 and sign == '/' and num2 == 10:
        return("26/10 = 2.6")
    if num1 == 26 and sign == '/' and num2 == 11:
        return("26/11 = 2.363636363636363636363636364")
    if num1 == 26 and sign == '/' and num2 == 12:
        return("26/12 = 2.166666666666666666666666667")
    if num1 == 26 and sign == '/' and num2 == 13:
        return("26/13 = 2")
    if num1 == 26 and sign == '/' and num2 == 14:
        return("26/14 = 1.857142857142857142857142857")
    if num1 == 26 and sign == '/' and num2 == 15:
        return("26/15 = 1.733333333333333333333333333")
    if num1 == 26 and sign == '/' and num2 == 16:
        return("26/16 = 1.625")
    if num1 == 26 and sign == '/' and num2 == 17:
        return("26/17 = 1.529411764705882352941176471")
    if num1 == 26 and sign == '/' and num2 == 18:
        return("26/18 = 1.444444444444444444444444444")
    if num1 == 26 and sign == '/' and num2 == 19:
        return("26/19 = 1.368421052631578947368421053")
    if num1 == 26 and sign == '/' and num2 == 20:
        return("26/20 = 1.3")
    if num1 == 26 and sign == '/' and num2 == 21:
        return("26/21 = 1.238095238095238095238095238")
    if num1 == 26 and sign == '/' and num2 == 22:
        return("26/22 = 1.181818181818181818181818182")
    if num1 == 26 and sign == '/' and num2 == 23:
        return("26/23 = 1.130434782608695652173913043")
    if num1 == 26 and sign == '/' and num2 == 24:
        return("26/24 = 1.083333333333333333333333333")
    if num1 == 26 and sign == '/' and num2 == 25:
        return("26/25 = 1.04")
    if num1 == 26 and sign == '/' and num2 == 26:
        return("26/26 = 1")
    if num1 == 26 and sign == '/' and num2 == 27:
        return("26/27 = 0.9629629629629629629629629630")
    if num1 == 26 and sign == '/' and num2 == 28:
        return("26/28 = 0.9285714285714285714285714286")
    if num1 == 26 and sign == '/' and num2 == 29:
        return("26/29 = 0.8965517241379310344827586207")
    if num1 == 26 and sign == '/' and num2 == 30:
        return("26/30 = 0.8666666666666666666666666667")
    if num1 == 26 and sign == '/' and num2 == 31:
        return("26/31 = 0.8387096774193548387096774194")
    if num1 == 26 and sign == '/' and num2 == 32:
        return("26/32 = 0.8125")
    if num1 == 26 and sign == '/' and num2 == 33:
        return("26/33 = 0.7878787878787878787878787879")
    if num1 == 26 and sign == '/' and num2 == 34:
        return("26/34 = 0.7647058823529411764705882353")
    if num1 == 26 and sign == '/' and num2 == 35:
        return("26/35 = 0.7428571428571428571428571429")
    if num1 == 26 and sign == '/' and num2 == 36:
        return("26/36 = 0.7222222222222222222222222222")
    if num1 == 26 and sign == '/' and num2 == 37:
        return("26/37 = 0.7027027027027027027027027027")
    if num1 == 26 and sign == '/' and num2 == 38:
        return("26/38 = 0.6842105263157894736842105263")
    if num1 == 26 and sign == '/' and num2 == 39:
        return("26/39 = 0.6666666666666666666666666667")
    if num1 == 26 and sign == '/' and num2 == 40:
        return("26/40 = 0.65")
    if num1 == 26 and sign == '/' and num2 == 41:
        return("26/41 = 0.6341463414634146341463414634")
    if num1 == 26 and sign == '/' and num2 == 42:
        return("26/42 = 0.6190476190476190476190476190")
    if num1 == 26 and sign == '/' and num2 == 43:
        return("26/43 = 0.6046511627906976744186046512")
    if num1 == 26 and sign == '/' and num2 == 44:
        return("26/44 = 0.5909090909090909090909090909")
    if num1 == 26 and sign == '/' and num2 == 45:
        return("26/45 = 0.5777777777777777777777777778")
    if num1 == 26 and sign == '/' and num2 == 46:
        return("26/46 = 0.5652173913043478260869565217")
    if num1 == 26 and sign == '/' and num2 == 47:
        return("26/47 = 0.5531914893617021276595744681")
    if num1 == 26 and sign == '/' and num2 == 48:
        return("26/48 = 0.5416666666666666666666666667")
    if num1 == 26 and sign == '/' and num2 == 49:
        return("26/49 = 0.5306122448979591836734693878")
    if num1 == 26 and sign == '/' and num2 == 50:
        return("26/50 = 0.52")
    if num1 == 27 and sign == '/' and num2 == 0:
        return("27/0 = Inf")
    if num1 == 27 and sign == '/' and num2 == 1:
        return("27/1 = 27")
    if num1 == 27 and sign == '/' and num2 == 2:
        return("27/2 = 13.5")
    if num1 == 27 and sign == '/' and num2 == 3:
        return("27/3 = 9")
    if num1 == 27 and sign == '/' and num2 == 4:
        return("27/4 = 6.75")
    if num1 == 27 and sign == '/' and num2 == 5:
        return("27/5 = 5.4")
    if num1 == 27 and sign == '/' and num2 == 6:
        return("27/6 = 4.5")
    if num1 == 27 and sign == '/' and num2 == 7:
        return("27/7 = 3.857142857142857142857142857")
    if num1 == 27 and sign == '/' and num2 == 8:
        return("27/8 = 3.375")
    if num1 == 27 and sign == '/' and num2 == 9:
        return("27/9 = 3")
    if num1 == 27 and sign == '/' and num2 == 10:
        return("27/10 = 2.7")
    if num1 == 27 and sign == '/' and num2 == 11:
        return("27/11 = 2.454545454545454545454545455")
    if num1 == 27 and sign == '/' and num2 == 12:
        return("27/12 = 2.25")
    if num1 == 27 and sign == '/' and num2 == 13:
        return("27/13 = 2.076923076923076923076923077")
    if num1 == 27 and sign == '/' and num2 == 14:
        return("27/14 = 1.928571428571428571428571429")
    if num1 == 27 and sign == '/' and num2 == 15:
        return("27/15 = 1.8")
    if num1 == 27 and sign == '/' and num2 == 16:
        return("27/16 = 1.6875")
    if num1 == 27 and sign == '/' and num2 == 17:
        return("27/17 = 1.588235294117647058823529412")
    if num1 == 27 and sign == '/' and num2 == 18:
        return("27/18 = 1.5")
    if num1 == 27 and sign == '/' and num2 == 19:
        return("27/19 = 1.421052631578947368421052632")
    if num1 == 27 and sign == '/' and num2 == 20:
        return("27/20 = 1.35")
    if num1 == 27 and sign == '/' and num2 == 21:
        return("27/21 = 1.285714285714285714285714286")
    if num1 == 27 and sign == '/' and num2 == 22:
        return("27/22 = 1.227272727272727272727272727")
    if num1 == 27 and sign == '/' and num2 == 23:
        return("27/23 = 1.173913043478260869565217391")
    if num1 == 27 and sign == '/' and num2 == 24:
        return("27/24 = 1.125")
    if num1 == 27 and sign == '/' and num2 == 25:
        return("27/25 = 1.08")
    if num1 == 27 and sign == '/' and num2 == 26:
        return("27/26 = 1.038461538461538461538461538")
    if num1 == 27 and sign == '/' and num2 == 27:
        return("27/27 = 1")
    if num1 == 27 and sign == '/' and num2 == 28:
        return("27/28 = 0.9642857142857142857142857143")
    if num1 == 27 and sign == '/' and num2 == 29:
        return("27/29 = 0.9310344827586206896551724138")
    if num1 == 27 and sign == '/' and num2 == 30:
        return("27/30 = 0.9")
    if num1 == 27 and sign == '/' and num2 == 31:
        return("27/31 = 0.8709677419354838709677419355")
    if num1 == 27 and sign == '/' and num2 == 32:
        return("27/32 = 0.84375")
    if num1 == 27 and sign == '/' and num2 == 33:
        return("27/33 = 0.8181818181818181818181818182")
    if num1 == 27 and sign == '/' and num2 == 34:
        return("27/34 = 0.7941176470588235294117647059")
    if num1 == 27 and sign == '/' and num2 == 35:
        return("27/35 = 0.7714285714285714285714285714")
    if num1 == 27 and sign == '/' and num2 == 36:
        return("27/36 = 0.75")
    if num1 == 27 and sign == '/' and num2 == 37:
        return("27/37 = 0.7297297297297297297297297297")
    if num1 == 27 and sign == '/' and num2 == 38:
        return("27/38 = 0.7105263157894736842105263158")
    if num1 == 27 and sign == '/' and num2 == 39:
        return("27/39 = 0.6923076923076923076923076923")
    if num1 == 27 and sign == '/' and num2 == 40:
        return("27/40 = 0.675")
    if num1 == 27 and sign == '/' and num2 == 41:
        return("27/41 = 0.6585365853658536585365853659")
    if num1 == 27 and sign == '/' and num2 == 42:
        return("27/42 = 0.6428571428571428571428571429")
    if num1 == 27 and sign == '/' and num2 == 43:
        return("27/43 = 0.6279069767441860465116279070")
    if num1 == 27 and sign == '/' and num2 == 44:
        return("27/44 = 0.6136363636363636363636363636")
    if num1 == 27 and sign == '/' and num2 == 45:
        return("27/45 = 0.6")
    if num1 == 27 and sign == '/' and num2 == 46:
        return("27/46 = 0.5869565217391304347826086957")
    if num1 == 27 and sign == '/' and num2 == 47:
        return("27/47 = 0.5744680851063829787234042553")
    if num1 == 27 and sign == '/' and num2 == 48:
        return("27/48 = 0.5625")
    if num1 == 27 and sign == '/' and num2 == 49:
        return("27/49 = 0.5510204081632653061224489796")
    if num1 == 27 and sign == '/' and num2 == 50:
        return("27/50 = 0.54")
    if num1 == 28 and sign == '/' and num2 == 0:
        return("28/0 = Inf")
    if num1 == 28 and sign == '/' and num2 == 1:
        return("28/1 = 28")
    if num1 == 28 and sign == '/' and num2 == 2:
        return("28/2 = 14")
    if num1 == 28 and sign == '/' and num2 == 3:
        return("28/3 = 9.333333333333333333333333333")
    if num1 == 28 and sign == '/' and num2 == 4:
        return("28/4 = 7")
    if num1 == 28 and sign == '/' and num2 == 5:
        return("28/5 = 5.6")
    if num1 == 28 and sign == '/' and num2 == 6:
        return("28/6 = 4.666666666666666666666666667")
    if num1 == 28 and sign == '/' and num2 == 7:
        return("28/7 = 4")
    if num1 == 28 and sign == '/' and num2 == 8:
        return("28/8 = 3.5")
    if num1 == 28 and sign == '/' and num2 == 9:
        return("28/9 = 3.111111111111111111111111111")
    if num1 == 28 and sign == '/' and num2 == 10:
        return("28/10 = 2.8")
    if num1 == 28 and sign == '/' and num2 == 11:
        return("28/11 = 2.545454545454545454545454545")
    if num1 == 28 and sign == '/' and num2 == 12:
        return("28/12 = 2.333333333333333333333333333")
    if num1 == 28 and sign == '/' and num2 == 13:
        return("28/13 = 2.153846153846153846153846154")
    if num1 == 28 and sign == '/' and num2 == 14:
        return("28/14 = 2")
    if num1 == 28 and sign == '/' and num2 == 15:
        return("28/15 = 1.866666666666666666666666667")
    if num1 == 28 and sign == '/' and num2 == 16:
        return("28/16 = 1.75")
    if num1 == 28 and sign == '/' and num2 == 17:
        return("28/17 = 1.647058823529411764705882353")
    if num1 == 28 and sign == '/' and num2 == 18:
        return("28/18 = 1.555555555555555555555555556")
    if num1 == 28 and sign == '/' and num2 == 19:
        return("28/19 = 1.473684210526315789473684211")
    if num1 == 28 and sign == '/' and num2 == 20:
        return("28/20 = 1.4")
    if num1 == 28 and sign == '/' and num2 == 21:
        return("28/21 = 1.333333333333333333333333333")
    if num1 == 28 and sign == '/' and num2 == 22:
        return("28/22 = 1.272727272727272727272727273")
    if num1 == 28 and sign == '/' and num2 == 23:
        return("28/23 = 1.217391304347826086956521739")
    if num1 == 28 and sign == '/' and num2 == 24:
        return("28/24 = 1.166666666666666666666666667")
    if num1 == 28 and sign == '/' and num2 == 25:
        return("28/25 = 1.12")
    if num1 == 28 and sign == '/' and num2 == 26:
        return("28/26 = 1.076923076923076923076923077")
    if num1 == 28 and sign == '/' and num2 == 27:
        return("28/27 = 1.037037037037037037037037037")
    if num1 == 28 and sign == '/' and num2 == 28:
        return("28/28 = 1")
    if num1 == 28 and sign == '/' and num2 == 29:
        return("28/29 = 0.9655172413793103448275862069")
    if num1 == 28 and sign == '/' and num2 == 30:
        return("28/30 = 0.9333333333333333333333333333")
    if num1 == 28 and sign == '/' and num2 == 31:
        return("28/31 = 0.9032258064516129032258064516")
    if num1 == 28 and sign == '/' and num2 == 32:
        return("28/32 = 0.875")
    if num1 == 28 and sign == '/' and num2 == 33:
        return("28/33 = 0.8484848484848484848484848485")
    if num1 == 28 and sign == '/' and num2 == 34:
        return("28/34 = 0.8235294117647058823529411765")
    if num1 == 28 and sign == '/' and num2 == 35:
        return("28/35 = 0.8")
    if num1 == 28 and sign == '/' and num2 == 36:
        return("28/36 = 0.7777777777777777777777777778")
    if num1 == 28 and sign == '/' and num2 == 37:
        return("28/37 = 0.7567567567567567567567567568")
    if num1 == 28 and sign == '/' and num2 == 38:
        return("28/38 = 0.7368421052631578947368421053")
    if num1 == 28 and sign == '/' and num2 == 39:
        return("28/39 = 0.7179487179487179487179487179")
    if num1 == 28 and sign == '/' and num2 == 40:
        return("28/40 = 0.7")
    if num1 == 28 and sign == '/' and num2 == 41:
        return("28/41 = 0.6829268292682926829268292683")
    if num1 == 28 and sign == '/' and num2 == 42:
        return("28/42 = 0.6666666666666666666666666667")
    if num1 == 28 and sign == '/' and num2 == 43:
        return("28/43 = 0.6511627906976744186046511628")
    if num1 == 28 and sign == '/' and num2 == 44:
        return("28/44 = 0.6363636363636363636363636364")
    if num1 == 28 and sign == '/' and num2 == 45:
        return("28/45 = 0.6222222222222222222222222222")
    if num1 == 28 and sign == '/' and num2 == 46:
        return("28/46 = 0.6086956521739130434782608696")
    if num1 == 28 and sign == '/' and num2 == 47:
        return("28/47 = 0.5957446808510638297872340426")
    if num1 == 28 and sign == '/' and num2 == 48:
        return("28/48 = 0.5833333333333333333333333333")
    if num1 == 28 and sign == '/' and num2 == 49:
        return("28/49 = 0.5714285714285714285714285714")
    if num1 == 28 and sign == '/' and num2 == 50:
        return("28/50 = 0.56")
    if num1 == 29 and sign == '/' and num2 == 0:
        return("29/0 = Inf")
    if num1 == 29 and sign == '/' and num2 == 1:
        return("29/1 = 29")
    if num1 == 29 and sign == '/' and num2 == 2:
        return("29/2 = 14.5")
    if num1 == 29 and sign == '/' and num2 == 3:
        return("29/3 = 9.666666666666666666666666667")
    if num1 == 29 and sign == '/' and num2 == 4:
        return("29/4 = 7.25")
    if num1 == 29 and sign == '/' and num2 == 5:
        return("29/5 = 5.8")
    if num1 == 29 and sign == '/' and num2 == 6:
        return("29/6 = 4.833333333333333333333333333")
    if num1 == 29 and sign == '/' and num2 == 7:
        return("29/7 = 4.142857142857142857142857143")
    if num1 == 29 and sign == '/' and num2 == 8:
        return("29/8 = 3.625")
    if num1 == 29 and sign == '/' and num2 == 9:
        return("29/9 = 3.222222222222222222222222222")
    if num1 == 29 and sign == '/' and num2 == 10:
        return("29/10 = 2.9")
    if num1 == 29 and sign == '/' and num2 == 11:
        return("29/11 = 2.636363636363636363636363636")
    if num1 == 29 and sign == '/' and num2 == 12:
        return("29/12 = 2.416666666666666666666666667")
    if num1 == 29 and sign == '/' and num2 == 13:
        return("29/13 = 2.230769230769230769230769231")
    if num1 == 29 and sign == '/' and num2 == 14:
        return("29/14 = 2.071428571428571428571428571")
    if num1 == 29 and sign == '/' and num2 == 15:
        return("29/15 = 1.933333333333333333333333333")
    if num1 == 29 and sign == '/' and num2 == 16:
        return("29/16 = 1.8125")
    if num1 == 29 and sign == '/' and num2 == 17:
        return("29/17 = 1.705882352941176470588235294")
    if num1 == 29 and sign == '/' and num2 == 18:
        return("29/18 = 1.611111111111111111111111111")
    if num1 == 29 and sign == '/' and num2 == 19:
        return("29/19 = 1.526315789473684210526315789")
    if num1 == 29 and sign == '/' and num2 == 20:
        return("29/20 = 1.45")
    if num1 == 29 and sign == '/' and num2 == 21:
        return("29/21 = 1.380952380952380952380952381")
    if num1 == 29 and sign == '/' and num2 == 22:
        return("29/22 = 1.318181818181818181818181818")
    if num1 == 29 and sign == '/' and num2 == 23:
        return("29/23 = 1.260869565217391304347826087")
    if num1 == 29 and sign == '/' and num2 == 24:
        return("29/24 = 1.208333333333333333333333333")
    if num1 == 29 and sign == '/' and num2 == 25:
        return("29/25 = 1.16")
    if num1 == 29 and sign == '/' and num2 == 26:
        return("29/26 = 1.115384615384615384615384615")
    if num1 == 29 and sign == '/' and num2 == 27:
        return("29/27 = 1.074074074074074074074074074")
    if num1 == 29 and sign == '/' and num2 == 28:
        return("29/28 = 1.035714285714285714285714286")
    if num1 == 29 and sign == '/' and num2 == 29:
        return("29/29 = 1")
    if num1 == 29 and sign == '/' and num2 == 30:
        return("29/30 = 0.9666666666666666666666666667")
    if num1 == 29 and sign == '/' and num2 == 31:
        return("29/31 = 0.9354838709677419354838709677")
    if num1 == 29 and sign == '/' and num2 == 32:
        return("29/32 = 0.90625")
    if num1 == 29 and sign == '/' and num2 == 33:
        return("29/33 = 0.8787878787878787878787878788")
    if num1 == 29 and sign == '/' and num2 == 34:
        return("29/34 = 0.8529411764705882352941176471")
    if num1 == 29 and sign == '/' and num2 == 35:
        return("29/35 = 0.8285714285714285714285714286")
    if num1 == 29 and sign == '/' and num2 == 36:
        return("29/36 = 0.8055555555555555555555555556")
    if num1 == 29 and sign == '/' and num2 == 37:
        return("29/37 = 0.7837837837837837837837837838")
    if num1 == 29 and sign == '/' and num2 == 38:
        return("29/38 = 0.7631578947368421052631578947")
    if num1 == 29 and sign == '/' and num2 == 39:
        return("29/39 = 0.7435897435897435897435897436")
    if num1 == 29 and sign == '/' and num2 == 40:
        return("29/40 = 0.725")
    if num1 == 29 and sign == '/' and num2 == 41:
        return("29/41 = 0.7073170731707317073170731707")
    if num1 == 29 and sign == '/' and num2 == 42:
        return("29/42 = 0.6904761904761904761904761905")
    if num1 == 29 and sign == '/' and num2 == 43:
        return("29/43 = 0.6744186046511627906976744186")
    if num1 == 29 and sign == '/' and num2 == 44:
        return("29/44 = 0.6590909090909090909090909091")
    if num1 == 29 and sign == '/' and num2 == 45:
        return("29/45 = 0.6444444444444444444444444444")
    if num1 == 29 and sign == '/' and num2 == 46:
        return("29/46 = 0.6304347826086956521739130435")
    if num1 == 29 and sign == '/' and num2 == 47:
        return("29/47 = 0.6170212765957446808510638298")
    if num1 == 29 and sign == '/' and num2 == 48:
        return("29/48 = 0.6041666666666666666666666667")
    if num1 == 29 and sign == '/' and num2 == 49:
        return("29/49 = 0.5918367346938775510204081633")
    if num1 == 29 and sign == '/' and num2 == 50:
        return("29/50 = 0.58")
    if num1 == 30 and sign == '/' and num2 == 0:
        return("30/0 = Inf")
    if num1 == 30 and sign == '/' and num2 == 1:
        return("30/1 = 30")
    if num1 == 30 and sign == '/' and num2 == 2:
        return("30/2 = 15")
    if num1 == 30 and sign == '/' and num2 == 3:
        return("30/3 = 10")
    if num1 == 30 and sign == '/' and num2 == 4:
        return("30/4 = 7.5")
    if num1 == 30 and sign == '/' and num2 == 5:
        return("30/5 = 6")
    if num1 == 30 and sign == '/' and num2 == 6:
        return("30/6 = 5")
    if num1 == 30 and sign == '/' and num2 == 7:
        return("30/7 = 4.285714285714285714285714286")
    if num1 == 30 and sign == '/' and num2 == 8:
        return("30/8 = 3.75")
    if num1 == 30 and sign == '/' and num2 == 9:
        return("30/9 = 3.333333333333333333333333333")
    if num1 == 30 and sign == '/' and num2 == 10:
        return("30/10 = 3")
    if num1 == 30 and sign == '/' and num2 == 11:
        return("30/11 = 2.727272727272727272727272727")
    if num1 == 30 and sign == '/' and num2 == 12:
        return("30/12 = 2.5")
    if num1 == 30 and sign == '/' and num2 == 13:
        return("30/13 = 2.307692307692307692307692308")
    if num1 == 30 and sign == '/' and num2 == 14:
        return("30/14 = 2.142857142857142857142857143")
    if num1 == 30 and sign == '/' and num2 == 15:
        return("30/15 = 2")
    if num1 == 30 and sign == '/' and num2 == 16:
        return("30/16 = 1.875")
    if num1 == 30 and sign == '/' and num2 == 17:
        return("30/17 = 1.764705882352941176470588235")
    if num1 == 30 and sign == '/' and num2 == 18:
        return("30/18 = 1.666666666666666666666666667")
    if num1 == 30 and sign == '/' and num2 == 19:
        return("30/19 = 1.578947368421052631578947368")
    if num1 == 30 and sign == '/' and num2 == 20:
        return("30/20 = 1.5")
    if num1 == 30 and sign == '/' and num2 == 21:
        return("30/21 = 1.428571428571428571428571429")
    if num1 == 30 and sign == '/' and num2 == 22:
        return("30/22 = 1.363636363636363636363636364")
    if num1 == 30 and sign == '/' and num2 == 23:
        return("30/23 = 1.304347826086956521739130435")
    if num1 == 30 and sign == '/' and num2 == 24:
        return("30/24 = 1.25")
    if num1 == 30 and sign == '/' and num2 == 25:
        return("30/25 = 1.2")
    if num1 == 30 and sign == '/' and num2 == 26:
        return("30/26 = 1.153846153846153846153846154")
    if num1 == 30 and sign == '/' and num2 == 27:
        return("30/27 = 1.111111111111111111111111111")
    if num1 == 30 and sign == '/' and num2 == 28:
        return("30/28 = 1.071428571428571428571428571")
    if num1 == 30 and sign == '/' and num2 == 29:
        return("30/29 = 1.034482758620689655172413793")
    if num1 == 30 and sign == '/' and num2 == 30:
        return("30/30 = 1")
    if num1 == 30 and sign == '/' and num2 == 31:
        return("30/31 = 0.9677419354838709677419354839")
    if num1 == 30 and sign == '/' and num2 == 32:
        return("30/32 = 0.9375")
    if num1 == 30 and sign == '/' and num2 == 33:
        return("30/33 = 0.9090909090909090909090909091")
    if num1 == 30 and sign == '/' and num2 == 34:
        return("30/34 = 0.8823529411764705882352941176")
    if num1 == 30 and sign == '/' and num2 == 35:
        return("30/35 = 0.8571428571428571428571428571")
    if num1 == 30 and sign == '/' and num2 == 36:
        return("30/36 = 0.8333333333333333333333333333")
    if num1 == 30 and sign == '/' and num2 == 37:
        return("30/37 = 0.8108108108108108108108108108")
    if num1 == 30 and sign == '/' and num2 == 38:
        return("30/38 = 0.7894736842105263157894736842")
    if num1 == 30 and sign == '/' and num2 == 39:
        return("30/39 = 0.7692307692307692307692307692")
    if num1 == 30 and sign == '/' and num2 == 40:
        return("30/40 = 0.75")
    if num1 == 30 and sign == '/' and num2 == 41:
        return("30/41 = 0.7317073170731707317073170732")
    if num1 == 30 and sign == '/' and num2 == 42:
        return("30/42 = 0.7142857142857142857142857143")
    if num1 == 30 and sign == '/' and num2 == 43:
        return("30/43 = 0.6976744186046511627906976744")
    if num1 == 30 and sign == '/' and num2 == 44:
        return("30/44 = 0.6818181818181818181818181818")
    if num1 == 30 and sign == '/' and num2 == 45:
        return("30/45 = 0.6666666666666666666666666667")
    if num1 == 30 and sign == '/' and num2 == 46:
        return("30/46 = 0.6521739130434782608695652174")
    if num1 == 30 and sign == '/' and num2 == 47:
        return("30/47 = 0.6382978723404255319148936170")
    if num1 == 30 and sign == '/' and num2 == 48:
        return("30/48 = 0.625")
    if num1 == 30 and sign == '/' and num2 == 49:
        return("30/49 = 0.6122448979591836734693877551")
    if num1 == 30 and sign == '/' and num2 == 50:
        return("30/50 = 0.6")
    if num1 == 31 and sign == '/' and num2 == 0:
        return("31/0 = Inf")
    if num1 == 31 and sign == '/' and num2 == 1:
        return("31/1 = 31")
    if num1 == 31 and sign == '/' and num2 == 2:
        return("31/2 = 15.5")
    if num1 == 31 and sign == '/' and num2 == 3:
        return("31/3 = 10.33333333333333333333333333")
    if num1 == 31 and sign == '/' and num2 == 4:
        return("31/4 = 7.75")
    if num1 == 31 and sign == '/' and num2 == 5:
        return("31/5 = 6.2")
    if num1 == 31 and sign == '/' and num2 == 6:
        return("31/6 = 5.166666666666666666666666667")
    if num1 == 31 and sign == '/' and num2 == 7:
        return("31/7 = 4.428571428571428571428571429")
    if num1 == 31 and sign == '/' and num2 == 8:
        return("31/8 = 3.875")
    if num1 == 31 and sign == '/' and num2 == 9:
        return("31/9 = 3.444444444444444444444444444")
    if num1 == 31 and sign == '/' and num2 == 10:
        return("31/10 = 3.1")
    if num1 == 31 and sign == '/' and num2 == 11:
        return("31/11 = 2.818181818181818181818181818")
    if num1 == 31 and sign == '/' and num2 == 12:
        return("31/12 = 2.583333333333333333333333333")
    if num1 == 31 and sign == '/' and num2 == 13:
        return("31/13 = 2.384615384615384615384615385")
    if num1 == 31 and sign == '/' and num2 == 14:
        return("31/14 = 2.214285714285714285714285714")
    if num1 == 31 and sign == '/' and num2 == 15:
        return("31/15 = 2.066666666666666666666666667")
    if num1 == 31 and sign == '/' and num2 == 16:
        return("31/16 = 1.9375")
    if num1 == 31 and sign == '/' and num2 == 17:
        return("31/17 = 1.823529411764705882352941176")
    if num1 == 31 and sign == '/' and num2 == 18:
        return("31/18 = 1.722222222222222222222222222")
    if num1 == 31 and sign == '/' and num2 == 19:
        return("31/19 = 1.631578947368421052631578947")
    if num1 == 31 and sign == '/' and num2 == 20:
        return("31/20 = 1.55")
    if num1 == 31 and sign == '/' and num2 == 21:
        return("31/21 = 1.476190476190476190476190476")
    if num1 == 31 and sign == '/' and num2 == 22:
        return("31/22 = 1.409090909090909090909090909")
    if num1 == 31 and sign == '/' and num2 == 23:
        return("31/23 = 1.347826086956521739130434783")
    if num1 == 31 and sign == '/' and num2 == 24:
        return("31/24 = 1.291666666666666666666666667")
    if num1 == 31 and sign == '/' and num2 == 25:
        return("31/25 = 1.24")
    if num1 == 31 and sign == '/' and num2 == 26:
        return("31/26 = 1.192307692307692307692307692")
    if num1 == 31 and sign == '/' and num2 == 27:
        return("31/27 = 1.148148148148148148148148148")
    if num1 == 31 and sign == '/' and num2 == 28:
        return("31/28 = 1.107142857142857142857142857")
    if num1 == 31 and sign == '/' and num2 == 29:
        return("31/29 = 1.068965517241379310344827586")
    if num1 == 31 and sign == '/' and num2 == 30:
        return("31/30 = 1.033333333333333333333333333")
    if num1 == 31 and sign == '/' and num2 == 31:
        return("31/31 = 1")
    if num1 == 31 and sign == '/' and num2 == 32:
        return("31/32 = 0.96875")
    if num1 == 31 and sign == '/' and num2 == 33:
        return("31/33 = 0.9393939393939393939393939394")
    if num1 == 31 and sign == '/' and num2 == 34:
        return("31/34 = 0.9117647058823529411764705882")
    if num1 == 31 and sign == '/' and num2 == 35:
        return("31/35 = 0.8857142857142857142857142857")
    if num1 == 31 and sign == '/' and num2 == 36:
        return("31/36 = 0.8611111111111111111111111111")
    if num1 == 31 and sign == '/' and num2 == 37:
        return("31/37 = 0.8378378378378378378378378378")
    if num1 == 31 and sign == '/' and num2 == 38:
        return("31/38 = 0.8157894736842105263157894737")
    if num1 == 31 and sign == '/' and num2 == 39:
        return("31/39 = 0.7948717948717948717948717949")
    if num1 == 31 and sign == '/' and num2 == 40:
        return("31/40 = 0.775")
    if num1 == 31 and sign == '/' and num2 == 41:
        return("31/41 = 0.7560975609756097560975609756")
    if num1 == 31 and sign == '/' and num2 == 42:
        return("31/42 = 0.7380952380952380952380952381")
    if num1 == 31 and sign == '/' and num2 == 43:
        return("31/43 = 0.7209302325581395348837209302")
    if num1 == 31 and sign == '/' and num2 == 44:
        return("31/44 = 0.7045454545454545454545454545")
    if num1 == 31 and sign == '/' and num2 == 45:
        return("31/45 = 0.6888888888888888888888888889")
    if num1 == 31 and sign == '/' and num2 == 46:
        return("31/46 = 0.6739130434782608695652173913")
    if num1 == 31 and sign == '/' and num2 == 47:
        return("31/47 = 0.6595744680851063829787234043")
    if num1 == 31 and sign == '/' and num2 == 48:
        return("31/48 = 0.6458333333333333333333333333")
    if num1 == 31 and sign == '/' and num2 == 49:
        return("31/49 = 0.6326530612244897959183673469")
    if num1 == 31 and sign == '/' and num2 == 50:
        return("31/50 = 0.62")
    if num1 == 32 and sign == '/' and num2 == 0:
        return("32/0 = Inf")
    if num1 == 32 and sign == '/' and num2 == 1:
        return("32/1 = 32")
    if num1 == 32 and sign == '/' and num2 == 2:
        return("32/2 = 16")
    if num1 == 32 and sign == '/' and num2 == 3:
        return("32/3 = 10.66666666666666666666666667")
    if num1 == 32 and sign == '/' and num2 == 4:
        return("32/4 = 8")
    if num1 == 32 and sign == '/' and num2 == 5:
        return("32/5 = 6.4")
    if num1 == 32 and sign == '/' and num2 == 6:
        return("32/6 = 5.333333333333333333333333333")
    if num1 == 32 and sign == '/' and num2 == 7:
        return("32/7 = 4.571428571428571428571428571")
    if num1 == 32 and sign == '/' and num2 == 8:
        return("32/8 = 4")
    if num1 == 32 and sign == '/' and num2 == 9:
        return("32/9 = 3.555555555555555555555555556")
    if num1 == 32 and sign == '/' and num2 == 10:
        return("32/10 = 3.2")
    if num1 == 32 and sign == '/' and num2 == 11:
        return("32/11 = 2.909090909090909090909090909")
    if num1 == 32 and sign == '/' and num2 == 12:
        return("32/12 = 2.666666666666666666666666667")
    if num1 == 32 and sign == '/' and num2 == 13:
        return("32/13 = 2.461538461538461538461538462")
    if num1 == 32 and sign == '/' and num2 == 14:
        return("32/14 = 2.285714285714285714285714286")
    if num1 == 32 and sign == '/' and num2 == 15:
        return("32/15 = 2.133333333333333333333333333")
    if num1 == 32 and sign == '/' and num2 == 16:
        return("32/16 = 2")
    if num1 == 32 and sign == '/' and num2 == 17:
        return("32/17 = 1.882352941176470588235294118")
    if num1 == 32 and sign == '/' and num2 == 18:
        return("32/18 = 1.777777777777777777777777778")
    if num1 == 32 and sign == '/' and num2 == 19:
        return("32/19 = 1.684210526315789473684210526")
    if num1 == 32 and sign == '/' and num2 == 20:
        return("32/20 = 1.6")
    if num1 == 32 and sign == '/' and num2 == 21:
        return("32/21 = 1.523809523809523809523809524")
    if num1 == 32 and sign == '/' and num2 == 22:
        return("32/22 = 1.454545454545454545454545455")
    if num1 == 32 and sign == '/' and num2 == 23:
        return("32/23 = 1.391304347826086956521739130")
    if num1 == 32 and sign == '/' and num2 == 24:
        return("32/24 = 1.333333333333333333333333333")
    if num1 == 32 and sign == '/' and num2 == 25:
        return("32/25 = 1.28")
    if num1 == 32 and sign == '/' and num2 == 26:
        return("32/26 = 1.230769230769230769230769231")
    if num1 == 32 and sign == '/' and num2 == 27:
        return("32/27 = 1.185185185185185185185185185")
    if num1 == 32 and sign == '/' and num2 == 28:
        return("32/28 = 1.142857142857142857142857143")
    if num1 == 32 and sign == '/' and num2 == 29:
        return("32/29 = 1.103448275862068965517241379")
    if num1 == 32 and sign == '/' and num2 == 30:
        return("32/30 = 1.066666666666666666666666667")
    if num1 == 32 and sign == '/' and num2 == 31:
        return("32/31 = 1.032258064516129032258064516")
    if num1 == 32 and sign == '/' and num2 == 32:
        return("32/32 = 1")
    if num1 == 32 and sign == '/' and num2 == 33:
        return("32/33 = 0.9696969696969696969696969697")
    if num1 == 32 and sign == '/' and num2 == 34:
        return("32/34 = 0.9411764705882352941176470588")
    if num1 == 32 and sign == '/' and num2 == 35:
        return("32/35 = 0.9142857142857142857142857143")
    if num1 == 32 and sign == '/' and num2 == 36:
        return("32/36 = 0.8888888888888888888888888889")
    if num1 == 32 and sign == '/' and num2 == 37:
        return("32/37 = 0.8648648648648648648648648649")
    if num1 == 32 and sign == '/' and num2 == 38:
        return("32/38 = 0.8421052631578947368421052632")
    if num1 == 32 and sign == '/' and num2 == 39:
        return("32/39 = 0.8205128205128205128205128205")
    if num1 == 32 and sign == '/' and num2 == 40:
        return("32/40 = 0.8")
    if num1 == 32 and sign == '/' and num2 == 41:
        return("32/41 = 0.7804878048780487804878048780")
    if num1 == 32 and sign == '/' and num2 == 42:
        return("32/42 = 0.7619047619047619047619047619")
    if num1 == 32 and sign == '/' and num2 == 43:
        return("32/43 = 0.7441860465116279069767441860")
    if num1 == 32 and sign == '/' and num2 == 44:
        return("32/44 = 0.7272727272727272727272727273")
    if num1 == 32 and sign == '/' and num2 == 45:
        return("32/45 = 0.7111111111111111111111111111")
    if num1 == 32 and sign == '/' and num2 == 46:
        return("32/46 = 0.6956521739130434782608695652")
    if num1 == 32 and sign == '/' and num2 == 47:
        return("32/47 = 0.6808510638297872340425531915")
    if num1 == 32 and sign == '/' and num2 == 48:
        return("32/48 = 0.6666666666666666666666666667")
    if num1 == 32 and sign == '/' and num2 == 49:
        return("32/49 = 0.6530612244897959183673469388")
    if num1 == 32 and sign == '/' and num2 == 50:
        return("32/50 = 0.64")
    if num1 == 33 and sign == '/' and num2 == 0:
        return("33/0 = Inf")
    if num1 == 33 and sign == '/' and num2 == 1:
        return("33/1 = 33")
    if num1 == 33 and sign == '/' and num2 == 2:
        return("33/2 = 16.5")
    if num1 == 33 and sign == '/' and num2 == 3:
        return("33/3 = 11")
    if num1 == 33 and sign == '/' and num2 == 4:
        return("33/4 = 8.25")
    if num1 == 33 and sign == '/' and num2 == 5:
        return("33/5 = 6.6")
    if num1 == 33 and sign == '/' and num2 == 6:
        return("33/6 = 5.5")
    if num1 == 33 and sign == '/' and num2 == 7:
        return("33/7 = 4.714285714285714285714285714")
    if num1 == 33 and sign == '/' and num2 == 8:
        return("33/8 = 4.125")
    if num1 == 33 and sign == '/' and num2 == 9:
        return("33/9 = 3.666666666666666666666666667")
    if num1 == 33 and sign == '/' and num2 == 10:
        return("33/10 = 3.3")
    if num1 == 33 and sign == '/' and num2 == 11:
        return("33/11 = 3")
    if num1 == 33 and sign == '/' and num2 == 12:
        return("33/12 = 2.75")
    if num1 == 33 and sign == '/' and num2 == 13:
        return("33/13 = 2.538461538461538461538461538")
    if num1 == 33 and sign == '/' and num2 == 14:
        return("33/14 = 2.357142857142857142857142857")
    if num1 == 33 and sign == '/' and num2 == 15:
        return("33/15 = 2.2")
    if num1 == 33 and sign == '/' and num2 == 16:
        return("33/16 = 2.0625")
    if num1 == 33 and sign == '/' and num2 == 17:
        return("33/17 = 1.941176470588235294117647059")
    if num1 == 33 and sign == '/' and num2 == 18:
        return("33/18 = 1.833333333333333333333333333")
    if num1 == 33 and sign == '/' and num2 == 19:
        return("33/19 = 1.736842105263157894736842105")
    if num1 == 33 and sign == '/' and num2 == 20:
        return("33/20 = 1.65")
    if num1 == 33 and sign == '/' and num2 == 21:
        return("33/21 = 1.571428571428571428571428571")
    if num1 == 33 and sign == '/' and num2 == 22:
        return("33/22 = 1.5")
    if num1 == 33 and sign == '/' and num2 == 23:
        return("33/23 = 1.434782608695652173913043478")
    if num1 == 33 and sign == '/' and num2 == 24:
        return("33/24 = 1.375")
    if num1 == 33 and sign == '/' and num2 == 25:
        return("33/25 = 1.32")
    if num1 == 33 and sign == '/' and num2 == 26:
        return("33/26 = 1.269230769230769230769230769")
    if num1 == 33 and sign == '/' and num2 == 27:
        return("33/27 = 1.222222222222222222222222222")
    if num1 == 33 and sign == '/' and num2 == 28:
        return("33/28 = 1.178571428571428571428571429")
    if num1 == 33 and sign == '/' and num2 == 29:
        return("33/29 = 1.137931034482758620689655172")
    if num1 == 33 and sign == '/' and num2 == 30:
        return("33/30 = 1.1")
    if num1 == 33 and sign == '/' and num2 == 31:
        return("33/31 = 1.064516129032258064516129032")
    if num1 == 33 and sign == '/' and num2 == 32:
        return("33/32 = 1.03125")
    if num1 == 33 and sign == '/' and num2 == 33:
        return("33/33 = 1")
    if num1 == 33 and sign == '/' and num2 == 34:
        return("33/34 = 0.9705882352941176470588235294")
    if num1 == 33 and sign == '/' and num2 == 35:
        return("33/35 = 0.9428571428571428571428571429")
    if num1 == 33 and sign == '/' and num2 == 36:
        return("33/36 = 0.9166666666666666666666666667")
    if num1 == 33 and sign == '/' and num2 == 37:
        return("33/37 = 0.8918918918918918918918918919")
    if num1 == 33 and sign == '/' and num2 == 38:
        return("33/38 = 0.8684210526315789473684210526")
    if num1 == 33 and sign == '/' and num2 == 39:
        return("33/39 = 0.8461538461538461538461538462")
    if num1 == 33 and sign == '/' and num2 == 40:
        return("33/40 = 0.825")
    if num1 == 33 and sign == '/' and num2 == 41:
        return("33/41 = 0.8048780487804878048780487805")
    if num1 == 33 and sign == '/' and num2 == 42:
        return("33/42 = 0.7857142857142857142857142857")
    if num1 == 33 and sign == '/' and num2 == 43:
        return("33/43 = 0.7674418604651162790697674419")
    if num1 == 33 and sign == '/' and num2 == 44:
        return("33/44 = 0.75")
    if num1 == 33 and sign == '/' and num2 == 45:
        return("33/45 = 0.7333333333333333333333333333")
    if num1 == 33 and sign == '/' and num2 == 46:
        return("33/46 = 0.7173913043478260869565217391")
    if num1 == 33 and sign == '/' and num2 == 47:
        return("33/47 = 0.7021276595744680851063829787")
    if num1 == 33 and sign == '/' and num2 == 48:
        return("33/48 = 0.6875")
    if num1 == 33 and sign == '/' and num2 == 49:
        return("33/49 = 0.6734693877551020408163265306")
    if num1 == 33 and sign == '/' and num2 == 50:
        return("33/50 = 0.66")
    if num1 == 34 and sign == '/' and num2 == 0:
        return("34/0 = Inf")
    if num1 == 34 and sign == '/' and num2 == 1:
        return("34/1 = 34")
    if num1 == 34 and sign == '/' and num2 == 2:
        return("34/2 = 17")
    if num1 == 34 and sign == '/' and num2 == 3:
        return("34/3 = 11.33333333333333333333333333")
    if num1 == 34 and sign == '/' and num2 == 4:
        return("34/4 = 8.5")
    if num1 == 34 and sign == '/' and num2 == 5:
        return("34/5 = 6.8")
    if num1 == 34 and sign == '/' and num2 == 6:
        return("34/6 = 5.666666666666666666666666667")
    if num1 == 34 and sign == '/' and num2 == 7:
        return("34/7 = 4.857142857142857142857142857")
    if num1 == 34 and sign == '/' and num2 == 8:
        return("34/8 = 4.25")
    if num1 == 34 and sign == '/' and num2 == 9:
        return("34/9 = 3.777777777777777777777777778")
    if num1 == 34 and sign == '/' and num2 == 10:
        return("34/10 = 3.4")
    if num1 == 34 and sign == '/' and num2 == 11:
        return("34/11 = 3.090909090909090909090909091")
    if num1 == 34 and sign == '/' and num2 == 12:
        return("34/12 = 2.833333333333333333333333333")
    if num1 == 34 and sign == '/' and num2 == 13:
        return("34/13 = 2.615384615384615384615384615")
    if num1 == 34 and sign == '/' and num2 == 14:
        return("34/14 = 2.428571428571428571428571429")
    if num1 == 34 and sign == '/' and num2 == 15:
        return("34/15 = 2.266666666666666666666666667")
    if num1 == 34 and sign == '/' and num2 == 16:
        return("34/16 = 2.125")
    if num1 == 34 and sign == '/' and num2 == 17:
        return("34/17 = 2")
    if num1 == 34 and sign == '/' and num2 == 18:
        return("34/18 = 1.888888888888888888888888889")
    if num1 == 34 and sign == '/' and num2 == 19:
        return("34/19 = 1.789473684210526315789473684")
    if num1 == 34 and sign == '/' and num2 == 20:
        return("34/20 = 1.7")
    if num1 == 34 and sign == '/' and num2 == 21:
        return("34/21 = 1.619047619047619047619047619")
    if num1 == 34 and sign == '/' and num2 == 22:
        return("34/22 = 1.545454545454545454545454545")
    if num1 == 34 and sign == '/' and num2 == 23:
        return("34/23 = 1.478260869565217391304347826")
    if num1 == 34 and sign == '/' and num2 == 24:
        return("34/24 = 1.416666666666666666666666667")
    if num1 == 34 and sign == '/' and num2 == 25:
        return("34/25 = 1.36")
    if num1 == 34 and sign == '/' and num2 == 26:
        return("34/26 = 1.307692307692307692307692308")
    if num1 == 34 and sign == '/' and num2 == 27:
        return("34/27 = 1.259259259259259259259259259")
    if num1 == 34 and sign == '/' and num2 == 28:
        return("34/28 = 1.214285714285714285714285714")
    if num1 == 34 and sign == '/' and num2 == 29:
        return("34/29 = 1.172413793103448275862068966")
    if num1 == 34 and sign == '/' and num2 == 30:
        return("34/30 = 1.133333333333333333333333333")
    if num1 == 34 and sign == '/' and num2 == 31:
        return("34/31 = 1.096774193548387096774193548")
    if num1 == 34 and sign == '/' and num2 == 32:
        return("34/32 = 1.0625")
    if num1 == 34 and sign == '/' and num2 == 33:
        return("34/33 = 1.030303030303030303030303030")
    if num1 == 34 and sign == '/' and num2 == 34:
        return("34/34 = 1")
    if num1 == 34 and sign == '/' and num2 == 35:
        return("34/35 = 0.9714285714285714285714285714")
    if num1 == 34 and sign == '/' and num2 == 36:
        return("34/36 = 0.9444444444444444444444444444")
    if num1 == 34 and sign == '/' and num2 == 37:
        return("34/37 = 0.9189189189189189189189189189")
    if num1 == 34 and sign == '/' and num2 == 38:
        return("34/38 = 0.8947368421052631578947368421")
    if num1 == 34 and sign == '/' and num2 == 39:
        return("34/39 = 0.8717948717948717948717948718")
    if num1 == 34 and sign == '/' and num2 == 40:
        return("34/40 = 0.85")
    if num1 == 34 and sign == '/' and num2 == 41:
        return("34/41 = 0.8292682926829268292682926829")
    if num1 == 34 and sign == '/' and num2 == 42:
        return("34/42 = 0.8095238095238095238095238095")
    if num1 == 34 and sign == '/' and num2 == 43:
        return("34/43 = 0.7906976744186046511627906977")
    if num1 == 34 and sign == '/' and num2 == 44:
        return("34/44 = 0.7727272727272727272727272727")
    if num1 == 34 and sign == '/' and num2 == 45:
        return("34/45 = 0.7555555555555555555555555556")
    if num1 == 34 and sign == '/' and num2 == 46:
        return("34/46 = 0.7391304347826086956521739130")
    if num1 == 34 and sign == '/' and num2 == 47:
        return("34/47 = 0.7234042553191489361702127660")
    if num1 == 34 and sign == '/' and num2 == 48:
        return("34/48 = 0.7083333333333333333333333333")
    if num1 == 34 and sign == '/' and num2 == 49:
        return("34/49 = 0.6938775510204081632653061224")
    if num1 == 34 and sign == '/' and num2 == 50:
        return("34/50 = 0.68")
    if num1 == 35 and sign == '/' and num2 == 0:
        return("35/0 = Inf")
    if num1 == 35 and sign == '/' and num2 == 1:
        return("35/1 = 35")
    if num1 == 35 and sign == '/' and num2 == 2:
        return("35/2 = 17.5")
    if num1 == 35 and sign == '/' and num2 == 3:
        return("35/3 = 11.66666666666666666666666667")
    if num1 == 35 and sign == '/' and num2 == 4:
        return("35/4 = 8.75")
    if num1 == 35 and sign == '/' and num2 == 5:
        return("35/5 = 7")
    if num1 == 35 and sign == '/' and num2 == 6:
        return("35/6 = 5.833333333333333333333333333")
    if num1 == 35 and sign == '/' and num2 == 7:
        return("35/7 = 5")
    if num1 == 35 and sign == '/' and num2 == 8:
        return("35/8 = 4.375")
    if num1 == 35 and sign == '/' and num2 == 9:
        return("35/9 = 3.888888888888888888888888889")
    if num1 == 35 and sign == '/' and num2 == 10:
        return("35/10 = 3.5")
    if num1 == 35 and sign == '/' and num2 == 11:
        return("35/11 = 3.181818181818181818181818182")
    if num1 == 35 and sign == '/' and num2 == 12:
        return("35/12 = 2.916666666666666666666666667")
    if num1 == 35 and sign == '/' and num2 == 13:
        return("35/13 = 2.692307692307692307692307692")
    if num1 == 35 and sign == '/' and num2 == 14:
        return("35/14 = 2.5")
    if num1 == 35 and sign == '/' and num2 == 15:
        return("35/15 = 2.333333333333333333333333333")
    if num1 == 35 and sign == '/' and num2 == 16:
        return("35/16 = 2.1875")
    if num1 == 35 and sign == '/' and num2 == 17:
        return("35/17 = 2.058823529411764705882352941")
    if num1 == 35 and sign == '/' and num2 == 18:
        return("35/18 = 1.944444444444444444444444444")
    if num1 == 35 and sign == '/' and num2 == 19:
        return("35/19 = 1.842105263157894736842105263")
    if num1 == 35 and sign == '/' and num2 == 20:
        return("35/20 = 1.75")
    if num1 == 35 and sign == '/' and num2 == 21:
        return("35/21 = 1.666666666666666666666666667")
    if num1 == 35 and sign == '/' and num2 == 22:
        return("35/22 = 1.590909090909090909090909091")
    if num1 == 35 and sign == '/' and num2 == 23:
        return("35/23 = 1.521739130434782608695652174")
    if num1 == 35 and sign == '/' and num2 == 24:
        return("35/24 = 1.458333333333333333333333333")
    if num1 == 35 and sign == '/' and num2 == 25:
        return("35/25 = 1.4")
    if num1 == 35 and sign == '/' and num2 == 26:
        return("35/26 = 1.346153846153846153846153846")
    if num1 == 35 and sign == '/' and num2 == 27:
        return("35/27 = 1.296296296296296296296296296")
    if num1 == 35 and sign == '/' and num2 == 28:
        return("35/28 = 1.25")
    if num1 == 35 and sign == '/' and num2 == 29:
        return("35/29 = 1.206896551724137931034482759")
    if num1 == 35 and sign == '/' and num2 == 30:
        return("35/30 = 1.166666666666666666666666667")
    if num1 == 35 and sign == '/' and num2 == 31:
        return("35/31 = 1.129032258064516129032258065")
    if num1 == 35 and sign == '/' and num2 == 32:
        return("35/32 = 1.09375")
    if num1 == 35 and sign == '/' and num2 == 33:
        return("35/33 = 1.060606060606060606060606061")
    if num1 == 35 and sign == '/' and num2 == 34:
        return("35/34 = 1.029411764705882352941176471")
    if num1 == 35 and sign == '/' and num2 == 35:
        return("35/35 = 1")
    if num1 == 35 and sign == '/' and num2 == 36:
        return("35/36 = 0.9722222222222222222222222222")
    if num1 == 35 and sign == '/' and num2 == 37:
        return("35/37 = 0.9459459459459459459459459459")
    if num1 == 35 and sign == '/' and num2 == 38:
        return("35/38 = 0.9210526315789473684210526316")
    if num1 == 35 and sign == '/' and num2 == 39:
        return("35/39 = 0.8974358974358974358974358974")
    if num1 == 35 and sign == '/' and num2 == 40:
        return("35/40 = 0.875")
    if num1 == 35 and sign == '/' and num2 == 41:
        return("35/41 = 0.8536585365853658536585365854")
    if num1 == 35 and sign == '/' and num2 == 42:
        return("35/42 = 0.8333333333333333333333333333")
    if num1 == 35 and sign == '/' and num2 == 43:
        return("35/43 = 0.8139534883720930232558139535")
    if num1 == 35 and sign == '/' and num2 == 44:
        return("35/44 = 0.7954545454545454545454545455")
    if num1 == 35 and sign == '/' and num2 == 45:
        return("35/45 = 0.7777777777777777777777777778")
    if num1 == 35 and sign == '/' and num2 == 46:
        return("35/46 = 0.7608695652173913043478260870")
    if num1 == 35 and sign == '/' and num2 == 47:
        return("35/47 = 0.7446808510638297872340425532")
    if num1 == 35 and sign == '/' and num2 == 48:
        return("35/48 = 0.7291666666666666666666666667")
    if num1 == 35 and sign == '/' and num2 == 49:
        return("35/49 = 0.7142857142857142857142857143")
    if num1 == 35 and sign == '/' and num2 == 50:
        return("35/50 = 0.7")
    if num1 == 36 and sign == '/' and num2 == 0:
        return("36/0 = Inf")
    if num1 == 36 and sign == '/' and num2 == 1:
        return("36/1 = 36")
    if num1 == 36 and sign == '/' and num2 == 2:
        return("36/2 = 18")
    if num1 == 36 and sign == '/' and num2 == 3:
        return("36/3 = 12")
    if num1 == 36 and sign == '/' and num2 == 4:
        return("36/4 = 9")
    if num1 == 36 and sign == '/' and num2 == 5:
        return("36/5 = 7.2")
    if num1 == 36 and sign == '/' and num2 == 6:
        return("36/6 = 6")
    if num1 == 36 and sign == '/' and num2 == 7:
        return("36/7 = 5.142857142857142857142857143")
    if num1 == 36 and sign == '/' and num2 == 8:
        return("36/8 = 4.5")
    if num1 == 36 and sign == '/' and num2 == 9:
        return("36/9 = 4")
    if num1 == 36 and sign == '/' and num2 == 10:
        return("36/10 = 3.6")
    if num1 == 36 and sign == '/' and num2 == 11:
        return("36/11 = 3.272727272727272727272727273")
    if num1 == 36 and sign == '/' and num2 == 12:
        return("36/12 = 3")
    if num1 == 36 and sign == '/' and num2 == 13:
        return("36/13 = 2.769230769230769230769230769")
    if num1 == 36 and sign == '/' and num2 == 14:
        return("36/14 = 2.571428571428571428571428571")
    if num1 == 36 and sign == '/' and num2 == 15:
        return("36/15 = 2.4")
    if num1 == 36 and sign == '/' and num2 == 16:
        return("36/16 = 2.25")
    if num1 == 36 and sign == '/' and num2 == 17:
        return("36/17 = 2.117647058823529411764705882")
    if num1 == 36 and sign == '/' and num2 == 18:
        return("36/18 = 2")
    if num1 == 36 and sign == '/' and num2 == 19:
        return("36/19 = 1.894736842105263157894736842")
    if num1 == 36 and sign == '/' and num2 == 20:
        return("36/20 = 1.8")
    if num1 == 36 and sign == '/' and num2 == 21:
        return("36/21 = 1.714285714285714285714285714")
    if num1 == 36 and sign == '/' and num2 == 22:
        return("36/22 = 1.636363636363636363636363636")
    if num1 == 36 and sign == '/' and num2 == 23:
        return("36/23 = 1.565217391304347826086956522")
    if num1 == 36 and sign == '/' and num2 == 24:
        return("36/24 = 1.5")
    if num1 == 36 and sign == '/' and num2 == 25:
        return("36/25 = 1.44")
    if num1 == 36 and sign == '/' and num2 == 26:
        return("36/26 = 1.384615384615384615384615385")
    if num1 == 36 and sign == '/' and num2 == 27:
        return("36/27 = 1.333333333333333333333333333")
    if num1 == 36 and sign == '/' and num2 == 28:
        return("36/28 = 1.285714285714285714285714286")
    if num1 == 36 and sign == '/' and num2 == 29:
        return("36/29 = 1.241379310344827586206896552")
    if num1 == 36 and sign == '/' and num2 == 30:
        return("36/30 = 1.2")
    if num1 == 36 and sign == '/' and num2 == 31:
        return("36/31 = 1.161290322580645161290322581")
    if num1 == 36 and sign == '/' and num2 == 32:
        return("36/32 = 1.125")
    if num1 == 36 and sign == '/' and num2 == 33:
        return("36/33 = 1.090909090909090909090909091")
    if num1 == 36 and sign == '/' and num2 == 34:
        return("36/34 = 1.058823529411764705882352941")
    if num1 == 36 and sign == '/' and num2 == 35:
        return("36/35 = 1.028571428571428571428571429")
    if num1 == 36 and sign == '/' and num2 == 36:
        return("36/36 = 1")
    if num1 == 36 and sign == '/' and num2 == 37:
        return("36/37 = 0.9729729729729729729729729730")
    if num1 == 36 and sign == '/' and num2 == 38:
        return("36/38 = 0.9473684210526315789473684211")
    if num1 == 36 and sign == '/' and num2 == 39:
        return("36/39 = 0.9230769230769230769230769231")
    if num1 == 36 and sign == '/' and num2 == 40:
        return("36/40 = 0.9")
    if num1 == 36 and sign == '/' and num2 == 41:
        return("36/41 = 0.8780487804878048780487804878")
    if num1 == 36 and sign == '/' and num2 == 42:
        return("36/42 = 0.8571428571428571428571428571")
    if num1 == 36 and sign == '/' and num2 == 43:
        return("36/43 = 0.8372093023255813953488372093")
    if num1 == 36 and sign == '/' and num2 == 44:
        return("36/44 = 0.8181818181818181818181818182")
    if num1 == 36 and sign == '/' and num2 == 45:
        return("36/45 = 0.8")
    if num1 == 36 and sign == '/' and num2 == 46:
        return("36/46 = 0.7826086956521739130434782609")
    if num1 == 36 and sign == '/' and num2 == 47:
        return("36/47 = 0.7659574468085106382978723404")
    if num1 == 36 and sign == '/' and num2 == 48:
        return("36/48 = 0.75")
    if num1 == 36 and sign == '/' and num2 == 49:
        return("36/49 = 0.7346938775510204081632653061")
    if num1 == 36 and sign == '/' and num2 == 50:
        return("36/50 = 0.72")
    if num1 == 37 and sign == '/' and num2 == 0:
        return("37/0 = Inf")
    if num1 == 37 and sign == '/' and num2 == 1:
        return("37/1 = 37")
    if num1 == 37 and sign == '/' and num2 == 2:
        return("37/2 = 18.5")
    if num1 == 37 and sign == '/' and num2 == 3:
        return("37/3 = 12.33333333333333333333333333")
    if num1 == 37 and sign == '/' and num2 == 4:
        return("37/4 = 9.25")
    if num1 == 37 and sign == '/' and num2 == 5:
        return("37/5 = 7.4")
    if num1 == 37 and sign == '/' and num2 == 6:
        return("37/6 = 6.166666666666666666666666667")
    if num1 == 37 and sign == '/' and num2 == 7:
        return("37/7 = 5.285714285714285714285714286")
    if num1 == 37 and sign == '/' and num2 == 8:
        return("37/8 = 4.625")
    if num1 == 37 and sign == '/' and num2 == 9:
        return("37/9 = 4.111111111111111111111111111")
    if num1 == 37 and sign == '/' and num2 == 10:
        return("37/10 = 3.7")
    if num1 == 37 and sign == '/' and num2 == 11:
        return("37/11 = 3.363636363636363636363636364")
    if num1 == 37 and sign == '/' and num2 == 12:
        return("37/12 = 3.083333333333333333333333333")
    if num1 == 37 and sign == '/' and num2 == 13:
        return("37/13 = 2.846153846153846153846153846")
    if num1 == 37 and sign == '/' and num2 == 14:
        return("37/14 = 2.642857142857142857142857143")
    if num1 == 37 and sign == '/' and num2 == 15:
        return("37/15 = 2.466666666666666666666666667")
    if num1 == 37 and sign == '/' and num2 == 16:
        return("37/16 = 2.3125")
    if num1 == 37 and sign == '/' and num2 == 17:
        return("37/17 = 2.176470588235294117647058824")
    if num1 == 37 and sign == '/' and num2 == 18:
        return("37/18 = 2.055555555555555555555555556")
    if num1 == 37 and sign == '/' and num2 == 19:
        return("37/19 = 1.947368421052631578947368421")
    if num1 == 37 and sign == '/' and num2 == 20:
        return("37/20 = 1.85")
    if num1 == 37 and sign == '/' and num2 == 21:
        return("37/21 = 1.761904761904761904761904762")
    if num1 == 37 and sign == '/' and num2 == 22:
        return("37/22 = 1.681818181818181818181818182")
    if num1 == 37 and sign == '/' and num2 == 23:
        return("37/23 = 1.608695652173913043478260870")
    if num1 == 37 and sign == '/' and num2 == 24:
        return("37/24 = 1.541666666666666666666666667")
    if num1 == 37 and sign == '/' and num2 == 25:
        return("37/25 = 1.48")
    if num1 == 37 and sign == '/' and num2 == 26:
        return("37/26 = 1.423076923076923076923076923")
    if num1 == 37 and sign == '/' and num2 == 27:
        return("37/27 = 1.370370370370370370370370370")
    if num1 == 37 and sign == '/' and num2 == 28:
        return("37/28 = 1.321428571428571428571428571")
    if num1 == 37 and sign == '/' and num2 == 29:
        return("37/29 = 1.275862068965517241379310345")
    if num1 == 37 and sign == '/' and num2 == 30:
        return("37/30 = 1.233333333333333333333333333")
    if num1 == 37 and sign == '/' and num2 == 31:
        return("37/31 = 1.193548387096774193548387097")
    if num1 == 37 and sign == '/' and num2 == 32:
        return("37/32 = 1.15625")
    if num1 == 37 and sign == '/' and num2 == 33:
        return("37/33 = 1.121212121212121212121212121")
    if num1 == 37 and sign == '/' and num2 == 34:
        return("37/34 = 1.088235294117647058823529412")
    if num1 == 37 and sign == '/' and num2 == 35:
        return("37/35 = 1.057142857142857142857142857")
    if num1 == 37 and sign == '/' and num2 == 36:
        return("37/36 = 1.027777777777777777777777778")
    if num1 == 37 and sign == '/' and num2 == 37:
        return("37/37 = 1")
    if num1 == 37 and sign == '/' and num2 == 38:
        return("37/38 = 0.9736842105263157894736842105")
    if num1 == 37 and sign == '/' and num2 == 39:
        return("37/39 = 0.9487179487179487179487179487")
    if num1 == 37 and sign == '/' and num2 == 40:
        return("37/40 = 0.925")
    if num1 == 37 and sign == '/' and num2 == 41:
        return("37/41 = 0.9024390243902439024390243902")
    if num1 == 37 and sign == '/' and num2 == 42:
        return("37/42 = 0.8809523809523809523809523810")
    if num1 == 37 and sign == '/' and num2 == 43:
        return("37/43 = 0.8604651162790697674418604651")
    if num1 == 37 and sign == '/' and num2 == 44:
        return("37/44 = 0.8409090909090909090909090909")
    if num1 == 37 and sign == '/' and num2 == 45:
        return("37/45 = 0.8222222222222222222222222222")
    if num1 == 37 and sign == '/' and num2 == 46:
        return("37/46 = 0.8043478260869565217391304348")
    if num1 == 37 and sign == '/' and num2 == 47:
        return("37/47 = 0.7872340425531914893617021277")
    if num1 == 37 and sign == '/' and num2 == 48:
        return("37/48 = 0.7708333333333333333333333333")
    if num1 == 37 and sign == '/' and num2 == 49:
        return("37/49 = 0.7551020408163265306122448980")
    if num1 == 37 and sign == '/' and num2 == 50:
        return("37/50 = 0.74")
    if num1 == 38 and sign == '/' and num2 == 0:
        return("38/0 = Inf")
    if num1 == 38 and sign == '/' and num2 == 1:
        return("38/1 = 38")
    if num1 == 38 and sign == '/' and num2 == 2:
        return("38/2 = 19")
    if num1 == 38 and sign == '/' and num2 == 3:
        return("38/3 = 12.66666666666666666666666667")
    if num1 == 38 and sign == '/' and num2 == 4:
        return("38/4 = 9.5")
    if num1 == 38 and sign == '/' and num2 == 5:
        return("38/5 = 7.6")
    if num1 == 38 and sign == '/' and num2 == 6:
        return("38/6 = 6.333333333333333333333333333")
    if num1 == 38 and sign == '/' and num2 == 7:
        return("38/7 = 5.428571428571428571428571429")
    if num1 == 38 and sign == '/' and num2 == 8:
        return("38/8 = 4.75")
    if num1 == 38 and sign == '/' and num2 == 9:
        return("38/9 = 4.222222222222222222222222222")
    if num1 == 38 and sign == '/' and num2 == 10:
        return("38/10 = 3.8")
    if num1 == 38 and sign == '/' and num2 == 11:
        return("38/11 = 3.454545454545454545454545455")
    if num1 == 38 and sign == '/' and num2 == 12:
        return("38/12 = 3.166666666666666666666666667")
    if num1 == 38 and sign == '/' and num2 == 13:
        return("38/13 = 2.923076923076923076923076923")
    if num1 == 38 and sign == '/' and num2 == 14:
        return("38/14 = 2.714285714285714285714285714")
    if num1 == 38 and sign == '/' and num2 == 15:
        return("38/15 = 2.533333333333333333333333333")
    if num1 == 38 and sign == '/' and num2 == 16:
        return("38/16 = 2.375")
    if num1 == 38 and sign == '/' and num2 == 17:
        return("38/17 = 2.235294117647058823529411765")
    if num1 == 38 and sign == '/' and num2 == 18:
        return("38/18 = 2.111111111111111111111111111")
    if num1 == 38 and sign == '/' and num2 == 19:
        return("38/19 = 2")
    if num1 == 38 and sign == '/' and num2 == 20:
        return("38/20 = 1.9")
    if num1 == 38 and sign == '/' and num2 == 21:
        return("38/21 = 1.809523809523809523809523810")
    if num1 == 38 and sign == '/' and num2 == 22:
        return("38/22 = 1.727272727272727272727272727")
    if num1 == 38 and sign == '/' and num2 == 23:
        return("38/23 = 1.652173913043478260869565217")
    if num1 == 38 and sign == '/' and num2 == 24:
        return("38/24 = 1.583333333333333333333333333")
    if num1 == 38 and sign == '/' and num2 == 25:
        return("38/25 = 1.52")
    if num1 == 38 and sign == '/' and num2 == 26:
        return("38/26 = 1.461538461538461538461538462")
    if num1 == 38 and sign == '/' and num2 == 27:
        return("38/27 = 1.407407407407407407407407407")
    if num1 == 38 and sign == '/' and num2 == 28:
        return("38/28 = 1.357142857142857142857142857")
    if num1 == 38 and sign == '/' and num2 == 29:
        return("38/29 = 1.310344827586206896551724138")
    if num1 == 38 and sign == '/' and num2 == 30:
        return("38/30 = 1.266666666666666666666666667")
    if num1 == 38 and sign == '/' and num2 == 31:
        return("38/31 = 1.225806451612903225806451613")
    if num1 == 38 and sign == '/' and num2 == 32:
        return("38/32 = 1.1875")
    if num1 == 38 and sign == '/' and num2 == 33:
        return("38/33 = 1.151515151515151515151515152")
    if num1 == 38 and sign == '/' and num2 == 34:
        return("38/34 = 1.117647058823529411764705882")
    if num1 == 38 and sign == '/' and num2 == 35:
        return("38/35 = 1.085714285714285714285714286")
    if num1 == 38 and sign == '/' and num2 == 36:
        return("38/36 = 1.055555555555555555555555556")
    if num1 == 38 and sign == '/' and num2 == 37:
        return("38/37 = 1.027027027027027027027027027")
    if num1 == 38 and sign == '/' and num2 == 38:
        return("38/38 = 1")
    if num1 == 38 and sign == '/' and num2 == 39:
        return("38/39 = 0.9743589743589743589743589744")
    if num1 == 38 and sign == '/' and num2 == 40:
        return("38/40 = 0.95")
    if num1 == 38 and sign == '/' and num2 == 41:
        return("38/41 = 0.9268292682926829268292682927")
    if num1 == 38 and sign == '/' and num2 == 42:
        return("38/42 = 0.9047619047619047619047619048")
    if num1 == 38 and sign == '/' and num2 == 43:
        return("38/43 = 0.8837209302325581395348837209")
    if num1 == 38 and sign == '/' and num2 == 44:
        return("38/44 = 0.8636363636363636363636363636")
    if num1 == 38 and sign == '/' and num2 == 45:
        return("38/45 = 0.8444444444444444444444444444")
    if num1 == 38 and sign == '/' and num2 == 46:
        return("38/46 = 0.8260869565217391304347826087")
    if num1 == 38 and sign == '/' and num2 == 47:
        return("38/47 = 0.8085106382978723404255319149")
    if num1 == 38 and sign == '/' and num2 == 48:
        return("38/48 = 0.7916666666666666666666666667")
    if num1 == 38 and sign == '/' and num2 == 49:
        return("38/49 = 0.7755102040816326530612244898")
    if num1 == 38 and sign == '/' and num2 == 50:
        return("38/50 = 0.76")
    if num1 == 39 and sign == '/' and num2 == 0:
        return("39/0 = Inf")
    if num1 == 39 and sign == '/' and num2 == 1:
        return("39/1 = 39")
    if num1 == 39 and sign == '/' and num2 == 2:
        return("39/2 = 19.5")
    if num1 == 39 and sign == '/' and num2 == 3:
        return("39/3 = 13")
    if num1 == 39 and sign == '/' and num2 == 4:
        return("39/4 = 9.75")
    if num1 == 39 and sign == '/' and num2 == 5:
        return("39/5 = 7.8")
    if num1 == 39 and sign == '/' and num2 == 6:
        return("39/6 = 6.5")
    if num1 == 39 and sign == '/' and num2 == 7:
        return("39/7 = 5.571428571428571428571428571")
    if num1 == 39 and sign == '/' and num2 == 8:
        return("39/8 = 4.875")
    if num1 == 39 and sign == '/' and num2 == 9:
        return("39/9 = 4.333333333333333333333333333")
    if num1 == 39 and sign == '/' and num2 == 10:
        return("39/10 = 3.9")
    if num1 == 39 and sign == '/' and num2 == 11:
        return("39/11 = 3.545454545454545454545454545")
    if num1 == 39 and sign == '/' and num2 == 12:
        return("39/12 = 3.25")
    if num1 == 39 and sign == '/' and num2 == 13:
        return("39/13 = 3")
    if num1 == 39 and sign == '/' and num2 == 14:
        return("39/14 = 2.785714285714285714285714286")
    if num1 == 39 and sign == '/' and num2 == 15:
        return("39/15 = 2.6")
    if num1 == 39 and sign == '/' and num2 == 16:
        return("39/16 = 2.4375")
    if num1 == 39 and sign == '/' and num2 == 17:
        return("39/17 = 2.294117647058823529411764706")
    if num1 == 39 and sign == '/' and num2 == 18:
        return("39/18 = 2.166666666666666666666666667")
    if num1 == 39 and sign == '/' and num2 == 19:
        return("39/19 = 2.052631578947368421052631579")
    if num1 == 39 and sign == '/' and num2 == 20:
        return("39/20 = 1.95")
    if num1 == 39 and sign == '/' and num2 == 21:
        return("39/21 = 1.857142857142857142857142857")
    if num1 == 39 and sign == '/' and num2 == 22:
        return("39/22 = 1.772727272727272727272727273")
    if num1 == 39 and sign == '/' and num2 == 23:
        return("39/23 = 1.695652173913043478260869565")
    if num1 == 39 and sign == '/' and num2 == 24:
        return("39/24 = 1.625")
    if num1 == 39 and sign == '/' and num2 == 25:
        return("39/25 = 1.56")
    if num1 == 39 and sign == '/' and num2 == 26:
        return("39/26 = 1.5")
    if num1 == 39 and sign == '/' and num2 == 27:
        return("39/27 = 1.444444444444444444444444444")
    if num1 == 39 and sign == '/' and num2 == 28:
        return("39/28 = 1.392857142857142857142857143")
    if num1 == 39 and sign == '/' and num2 == 29:
        return("39/29 = 1.344827586206896551724137931")
    if num1 == 39 and sign == '/' and num2 == 30:
        return("39/30 = 1.3")
    if num1 == 39 and sign == '/' and num2 == 31:
        return("39/31 = 1.258064516129032258064516129")
    if num1 == 39 and sign == '/' and num2 == 32:
        return("39/32 = 1.21875")
    if num1 == 39 and sign == '/' and num2 == 33:
        return("39/33 = 1.181818181818181818181818182")
    if num1 == 39 and sign == '/' and num2 == 34:
        return("39/34 = 1.147058823529411764705882353")
    if num1 == 39 and sign == '/' and num2 == 35:
        return("39/35 = 1.114285714285714285714285714")
    if num1 == 39 and sign == '/' and num2 == 36:
        return("39/36 = 1.083333333333333333333333333")
    if num1 == 39 and sign == '/' and num2 == 37:
        return("39/37 = 1.054054054054054054054054054")
    if num1 == 39 and sign == '/' and num2 == 38:
        return("39/38 = 1.026315789473684210526315789")
    if num1 == 39 and sign == '/' and num2 == 39:
        return("39/39 = 1")
    if num1 == 39 and sign == '/' and num2 == 40:
        return("39/40 = 0.975")
    if num1 == 39 and sign == '/' and num2 == 41:
        return("39/41 = 0.9512195121951219512195121951")
    if num1 == 39 and sign == '/' and num2 == 42:
        return("39/42 = 0.9285714285714285714285714286")
    if num1 == 39 and sign == '/' and num2 == 43:
        return("39/43 = 0.9069767441860465116279069767")
    if num1 == 39 and sign == '/' and num2 == 44:
        return("39/44 = 0.8863636363636363636363636364")
    if num1 == 39 and sign == '/' and num2 == 45:
        return("39/45 = 0.8666666666666666666666666667")
    if num1 == 39 and sign == '/' and num2 == 46:
        return("39/46 = 0.8478260869565217391304347826")
    if num1 == 39 and sign == '/' and num2 == 47:
        return("39/47 = 0.8297872340425531914893617021")
    if num1 == 39 and sign == '/' and num2 == 48:
        return("39/48 = 0.8125")
    if num1 == 39 and sign == '/' and num2 == 49:
        return("39/49 = 0.7959183673469387755102040816")
    if num1 == 39 and sign == '/' and num2 == 50:
        return("39/50 = 0.78")
    if num1 == 40 and sign == '/' and num2 == 0:
        return("40/0 = Inf")
    if num1 == 40 and sign == '/' and num2 == 1:
        return("40/1 = 40")
    if num1 == 40 and sign == '/' and num2 == 2:
        return("40/2 = 20")
    if num1 == 40 and sign == '/' and num2 == 3:
        return("40/3 = 13.33333333333333333333333333")
    if num1 == 40 and sign == '/' and num2 == 4:
        return("40/4 = 10")
    if num1 == 40 and sign == '/' and num2 == 5:
        return("40/5 = 8")
    if num1 == 40 and sign == '/' and num2 == 6:
        return("40/6 = 6.666666666666666666666666667")
    if num1 == 40 and sign == '/' and num2 == 7:
        return("40/7 = 5.714285714285714285714285714")
    if num1 == 40 and sign == '/' and num2 == 8:
        return("40/8 = 5")
    if num1 == 40 and sign == '/' and num2 == 9:
        return("40/9 = 4.444444444444444444444444444")
    if num1 == 40 and sign == '/' and num2 == 10:
        return("40/10 = 4")
    if num1 == 40 and sign == '/' and num2 == 11:
        return("40/11 = 3.636363636363636363636363636")
    if num1 == 40 and sign == '/' and num2 == 12:
        return("40/12 = 3.333333333333333333333333333")
    if num1 == 40 and sign == '/' and num2 == 13:
        return("40/13 = 3.076923076923076923076923077")
    if num1 == 40 and sign == '/' and num2 == 14:
        return("40/14 = 2.857142857142857142857142857")
    if num1 == 40 and sign == '/' and num2 == 15:
        return("40/15 = 2.666666666666666666666666667")
    if num1 == 40 and sign == '/' and num2 == 16:
        return("40/16 = 2.5")
    if num1 == 40 and sign == '/' and num2 == 17:
        return("40/17 = 2.352941176470588235294117647")
    if num1 == 40 and sign == '/' and num2 == 18:
        return("40/18 = 2.222222222222222222222222222")
    if num1 == 40 and sign == '/' and num2 == 19:
        return("40/19 = 2.105263157894736842105263158")
    if num1 == 40 and sign == '/' and num2 == 20:
        return("40/20 = 2")
    if num1 == 40 and sign == '/' and num2 == 21:
        return("40/21 = 1.904761904761904761904761905")
    if num1 == 40 and sign == '/' and num2 == 22:
        return("40/22 = 1.818181818181818181818181818")
    if num1 == 40 and sign == '/' and num2 == 23:
        return("40/23 = 1.739130434782608695652173913")
    if num1 == 40 and sign == '/' and num2 == 24:
        return("40/24 = 1.666666666666666666666666667")
    if num1 == 40 and sign == '/' and num2 == 25:
        return("40/25 = 1.6")
    if num1 == 40 and sign == '/' and num2 == 26:
        return("40/26 = 1.538461538461538461538461538")
    if num1 == 40 and sign == '/' and num2 == 27:
        return("40/27 = 1.481481481481481481481481481")
    if num1 == 40 and sign == '/' and num2 == 28:
        return("40/28 = 1.428571428571428571428571429")
    if num1 == 40 and sign == '/' and num2 == 29:
        return("40/29 = 1.379310344827586206896551724")
    if num1 == 40 and sign == '/' and num2 == 30:
        return("40/30 = 1.333333333333333333333333333")
    if num1 == 40 and sign == '/' and num2 == 31:
        return("40/31 = 1.290322580645161290322580645")
    if num1 == 40 and sign == '/' and num2 == 32:
        return("40/32 = 1.25")
    if num1 == 40 and sign == '/' and num2 == 33:
        return("40/33 = 1.212121212121212121212121212")
    if num1 == 40 and sign == '/' and num2 == 34:
        return("40/34 = 1.176470588235294117647058824")
    if num1 == 40 and sign == '/' and num2 == 35:
        return("40/35 = 1.142857142857142857142857143")
    if num1 == 40 and sign == '/' and num2 == 36:
        return("40/36 = 1.111111111111111111111111111")
    if num1 == 40 and sign == '/' and num2 == 37:
        return("40/37 = 1.081081081081081081081081081")
    if num1 == 40 and sign == '/' and num2 == 38:
        return("40/38 = 1.052631578947368421052631579")
    if num1 == 40 and sign == '/' and num2 == 39:
        return("40/39 = 1.025641025641025641025641026")
    if num1 == 40 and sign == '/' and num2 == 40:
        return("40/40 = 1")
    if num1 == 40 and sign == '/' and num2 == 41:
        return("40/41 = 0.9756097560975609756097560976")
    if num1 == 40 and sign == '/' and num2 == 42:
        return("40/42 = 0.9523809523809523809523809524")
    if num1 == 40 and sign == '/' and num2 == 43:
        return("40/43 = 0.9302325581395348837209302326")
    if num1 == 40 and sign == '/' and num2 == 44:
        return("40/44 = 0.9090909090909090909090909091")
    if num1 == 40 and sign == '/' and num2 == 45:
        return("40/45 = 0.8888888888888888888888888889")
    if num1 == 40 and sign == '/' and num2 == 46:
        return("40/46 = 0.8695652173913043478260869565")
    if num1 == 40 and sign == '/' and num2 == 47:
        return("40/47 = 0.8510638297872340425531914894")
    if num1 == 40 and sign == '/' and num2 == 48:
        return("40/48 = 0.8333333333333333333333333333")
    if num1 == 40 and sign == '/' and num2 == 49:
        return("40/49 = 0.8163265306122448979591836735")
    if num1 == 40 and sign == '/' and num2 == 50:
        return("40/50 = 0.8")
    if num1 == 41 and sign == '/' and num2 == 0:
        return("41/0 = Inf")
    if num1 == 41 and sign == '/' and num2 == 1:
        return("41/1 = 41")
    if num1 == 41 and sign == '/' and num2 == 2:
        return("41/2 = 20.5")
    if num1 == 41 and sign == '/' and num2 == 3:
        return("41/3 = 13.66666666666666666666666667")
    if num1 == 41 and sign == '/' and num2 == 4:
        return("41/4 = 10.25")
    if num1 == 41 and sign == '/' and num2 == 5:
        return("41/5 = 8.2")
    if num1 == 41 and sign == '/' and num2 == 6:
        return("41/6 = 6.833333333333333333333333333")
    if num1 == 41 and sign == '/' and num2 == 7:
        return("41/7 = 5.857142857142857142857142857")
    if num1 == 41 and sign == '/' and num2 == 8:
        return("41/8 = 5.125")
    if num1 == 41 and sign == '/' and num2 == 9:
        return("41/9 = 4.555555555555555555555555556")
    if num1 == 41 and sign == '/' and num2 == 10:
        return("41/10 = 4.1")
    if num1 == 41 and sign == '/' and num2 == 11:
        return("41/11 = 3.727272727272727272727272727")
    if num1 == 41 and sign == '/' and num2 == 12:
        return("41/12 = 3.416666666666666666666666667")
    if num1 == 41 and sign == '/' and num2 == 13:
        return("41/13 = 3.153846153846153846153846154")
    if num1 == 41 and sign == '/' and num2 == 14:
        return("41/14 = 2.928571428571428571428571429")
    if num1 == 41 and sign == '/' and num2 == 15:
        return("41/15 = 2.733333333333333333333333333")
    if num1 == 41 and sign == '/' and num2 == 16:
        return("41/16 = 2.5625")
    if num1 == 41 and sign == '/' and num2 == 17:
        return("41/17 = 2.411764705882352941176470588")
    if num1 == 41 and sign == '/' and num2 == 18:
        return("41/18 = 2.277777777777777777777777778")
    if num1 == 41 and sign == '/' and num2 == 19:
        return("41/19 = 2.157894736842105263157894737")
    if num1 == 41 and sign == '/' and num2 == 20:
        return("41/20 = 2.05")
    if num1 == 41 and sign == '/' and num2 == 21:
        return("41/21 = 1.952380952380952380952380952")
    if num1 == 41 and sign == '/' and num2 == 22:
        return("41/22 = 1.863636363636363636363636364")
    if num1 == 41 and sign == '/' and num2 == 23:
        return("41/23 = 1.782608695652173913043478261")
    if num1 == 41 and sign == '/' and num2 == 24:
        return("41/24 = 1.708333333333333333333333333")
    if num1 == 41 and sign == '/' and num2 == 25:
        return("41/25 = 1.64")
    if num1 == 41 and sign == '/' and num2 == 26:
        return("41/26 = 1.576923076923076923076923077")
    if num1 == 41 and sign == '/' and num2 == 27:
        return("41/27 = 1.518518518518518518518518519")
    if num1 == 41 and sign == '/' and num2 == 28:
        return("41/28 = 1.464285714285714285714285714")
    if num1 == 41 and sign == '/' and num2 == 29:
        return("41/29 = 1.413793103448275862068965517")
    if num1 == 41 and sign == '/' and num2 == 30:
        return("41/30 = 1.366666666666666666666666667")
    if num1 == 41 and sign == '/' and num2 == 31:
        return("41/31 = 1.322580645161290322580645161")
    if num1 == 41 and sign == '/' and num2 == 32:
        return("41/32 = 1.28125")
    if num1 == 41 and sign == '/' and num2 == 33:
        return("41/33 = 1.242424242424242424242424242")
    if num1 == 41 and sign == '/' and num2 == 34:
        return("41/34 = 1.205882352941176470588235294")
    if num1 == 41 and sign == '/' and num2 == 35:
        return("41/35 = 1.171428571428571428571428571")
    if num1 == 41 and sign == '/' and num2 == 36:
        return("41/36 = 1.138888888888888888888888889")
    if num1 == 41 and sign == '/' and num2 == 37:
        return("41/37 = 1.108108108108108108108108108")
    if num1 == 41 and sign == '/' and num2 == 38:
        return("41/38 = 1.078947368421052631578947368")
    if num1 == 41 and sign == '/' and num2 == 39:
        return("41/39 = 1.051282051282051282051282051")
    if num1 == 41 and sign == '/' and num2 == 40:
        return("41/40 = 1.025")
    if num1 == 41 and sign == '/' and num2 == 41:
        return("41/41 = 1")
    if num1 == 41 and sign == '/' and num2 == 42:
        return("41/42 = 0.9761904761904761904761904762")
    if num1 == 41 and sign == '/' and num2 == 43:
        return("41/43 = 0.9534883720930232558139534884")
    if num1 == 41 and sign == '/' and num2 == 44:
        return("41/44 = 0.9318181818181818181818181818")
    if num1 == 41 and sign == '/' and num2 == 45:
        return("41/45 = 0.9111111111111111111111111111")
    if num1 == 41 and sign == '/' and num2 == 46:
        return("41/46 = 0.8913043478260869565217391304")
    if num1 == 41 and sign == '/' and num2 == 47:
        return("41/47 = 0.8723404255319148936170212766")
    if num1 == 41 and sign == '/' and num2 == 48:
        return("41/48 = 0.8541666666666666666666666667")
    if num1 == 41 and sign == '/' and num2 == 49:
        return("41/49 = 0.8367346938775510204081632653")
    if num1 == 41 and sign == '/' and num2 == 50:
        return("41/50 = 0.82")
    if num1 == 42 and sign == '/' and num2 == 0:
        return("42/0 = Inf")
    if num1 == 42 and sign == '/' and num2 == 1:
        return("42/1 = 42")
    if num1 == 42 and sign == '/' and num2 == 2:
        return("42/2 = 21")
    if num1 == 42 and sign == '/' and num2 == 3:
        return("42/3 = 14")
    if num1 == 42 and sign == '/' and num2 == 4:
        return("42/4 = 10.5")
    if num1 == 42 and sign == '/' and num2 == 5:
        return("42/5 = 8.4")
    if num1 == 42 and sign == '/' and num2 == 6:
        return("42/6 = 7")
    if num1 == 42 and sign == '/' and num2 == 7:
        return("42/7 = 6")
    if num1 == 42 and sign == '/' and num2 == 8:
        return("42/8 = 5.25")
    if num1 == 42 and sign == '/' and num2 == 9:
        return("42/9 = 4.666666666666666666666666667")
    if num1 == 42 and sign == '/' and num2 == 10:
        return("42/10 = 4.2")
    if num1 == 42 and sign == '/' and num2 == 11:
        return("42/11 = 3.818181818181818181818181818")
    if num1 == 42 and sign == '/' and num2 == 12:
        return("42/12 = 3.5")
    if num1 == 42 and sign == '/' and num2 == 13:
        return("42/13 = 3.230769230769230769230769231")
    if num1 == 42 and sign == '/' and num2 == 14:
        return("42/14 = 3")
    if num1 == 42 and sign == '/' and num2 == 15:
        return("42/15 = 2.8")
    if num1 == 42 and sign == '/' and num2 == 16:
        return("42/16 = 2.625")
    if num1 == 42 and sign == '/' and num2 == 17:
        return("42/17 = 2.470588235294117647058823529")
    if num1 == 42 and sign == '/' and num2 == 18:
        return("42/18 = 2.333333333333333333333333333")
    if num1 == 42 and sign == '/' and num2 == 19:
        return("42/19 = 2.210526315789473684210526316")
    if num1 == 42 and sign == '/' and num2 == 20:
        return("42/20 = 2.1")
    if num1 == 42 and sign == '/' and num2 == 21:
        return("42/21 = 2")
    if num1 == 42 and sign == '/' and num2 == 22:
        return("42/22 = 1.909090909090909090909090909")
    if num1 == 42 and sign == '/' and num2 == 23:
        return("42/23 = 1.826086956521739130434782609")
    if num1 == 42 and sign == '/' and num2 == 24:
        return("42/24 = 1.75")
    if num1 == 42 and sign == '/' and num2 == 25:
        return("42/25 = 1.68")
    if num1 == 42 and sign == '/' and num2 == 26:
        return("42/26 = 1.615384615384615384615384615")
    if num1 == 42 and sign == '/' and num2 == 27:
        return("42/27 = 1.555555555555555555555555556")
    if num1 == 42 and sign == '/' and num2 == 28:
        return("42/28 = 1.5")
    if num1 == 42 and sign == '/' and num2 == 29:
        return("42/29 = 1.448275862068965517241379310")
    if num1 == 42 and sign == '/' and num2 == 30:
        return("42/30 = 1.4")
    if num1 == 42 and sign == '/' and num2 == 31:
        return("42/31 = 1.354838709677419354838709677")
    if num1 == 42 and sign == '/' and num2 == 32:
        return("42/32 = 1.3125")
    if num1 == 42 and sign == '/' and num2 == 33:
        return("42/33 = 1.272727272727272727272727273")
    if num1 == 42 and sign == '/' and num2 == 34:
        return("42/34 = 1.235294117647058823529411765")
    if num1 == 42 and sign == '/' and num2 == 35:
        return("42/35 = 1.2")
    if num1 == 42 and sign == '/' and num2 == 36:
        return("42/36 = 1.166666666666666666666666667")
    if num1 == 42 and sign == '/' and num2 == 37:
        return("42/37 = 1.135135135135135135135135135")
    if num1 == 42 and sign == '/' and num2 == 38:
        return("42/38 = 1.105263157894736842105263158")
    if num1 == 42 and sign == '/' and num2 == 39:
        return("42/39 = 1.076923076923076923076923077")
    if num1 == 42 and sign == '/' and num2 == 40:
        return("42/40 = 1.05")
    if num1 == 42 and sign == '/' and num2 == 41:
        return("42/41 = 1.024390243902439024390243902")
    if num1 == 42 and sign == '/' and num2 == 42:
        return("42/42 = 1")
    if num1 == 42 and sign == '/' and num2 == 43:
        return("42/43 = 0.9767441860465116279069767442")
    if num1 == 42 and sign == '/' and num2 == 44:
        return("42/44 = 0.9545454545454545454545454545")
    if num1 == 42 and sign == '/' and num2 == 45:
        return("42/45 = 0.9333333333333333333333333333")
    if num1 == 42 and sign == '/' and num2 == 46:
        return("42/46 = 0.9130434782608695652173913043")
    if num1 == 42 and sign == '/' and num2 == 47:
        return("42/47 = 0.8936170212765957446808510638")
    if num1 == 42 and sign == '/' and num2 == 48:
        return("42/48 = 0.875")
    if num1 == 42 and sign == '/' and num2 == 49:
        return("42/49 = 0.8571428571428571428571428571")
    if num1 == 42 and sign == '/' and num2 == 50:
        return("42/50 = 0.84")
    if num1 == 43 and sign == '/' and num2 == 0:
        return("43/0 = Inf")
    if num1 == 43 and sign == '/' and num2 == 1:
        return("43/1 = 43")
    if num1 == 43 and sign == '/' and num2 == 2:
        return("43/2 = 21.5")
    if num1 == 43 and sign == '/' and num2 == 3:
        return("43/3 = 14.33333333333333333333333333")
    if num1 == 43 and sign == '/' and num2 == 4:
        return("43/4 = 10.75")
    if num1 == 43 and sign == '/' and num2 == 5:
        return("43/5 = 8.6")
    if num1 == 43 and sign == '/' and num2 == 6:
        return("43/6 = 7.166666666666666666666666667")
    if num1 == 43 and sign == '/' and num2 == 7:
        return("43/7 = 6.142857142857142857142857143")
    if num1 == 43 and sign == '/' and num2 == 8:
        return("43/8 = 5.375")
    if num1 == 43 and sign == '/' and num2 == 9:
        return("43/9 = 4.777777777777777777777777778")
    if num1 == 43 and sign == '/' and num2 == 10:
        return("43/10 = 4.3")
    if num1 == 43 and sign == '/' and num2 == 11:
        return("43/11 = 3.909090909090909090909090909")
    if num1 == 43 and sign == '/' and num2 == 12:
        return("43/12 = 3.583333333333333333333333333")
    if num1 == 43 and sign == '/' and num2 == 13:
        return("43/13 = 3.307692307692307692307692308")
    if num1 == 43 and sign == '/' and num2 == 14:
        return("43/14 = 3.071428571428571428571428571")
    if num1 == 43 and sign == '/' and num2 == 15:
        return("43/15 = 2.866666666666666666666666667")
    if num1 == 43 and sign == '/' and num2 == 16:
        return("43/16 = 2.6875")
    if num1 == 43 and sign == '/' and num2 == 17:
        return("43/17 = 2.529411764705882352941176471")
    if num1 == 43 and sign == '/' and num2 == 18:
        return("43/18 = 2.388888888888888888888888889")
    if num1 == 43 and sign == '/' and num2 == 19:
        return("43/19 = 2.263157894736842105263157895")
    if num1 == 43 and sign == '/' and num2 == 20:
        return("43/20 = 2.15")
    if num1 == 43 and sign == '/' and num2 == 21:
        return("43/21 = 2.047619047619047619047619048")
    if num1 == 43 and sign == '/' and num2 == 22:
        return("43/22 = 1.954545454545454545454545455")
    if num1 == 43 and sign == '/' and num2 == 23:
        return("43/23 = 1.869565217391304347826086957")
    if num1 == 43 and sign == '/' and num2 == 24:
        return("43/24 = 1.791666666666666666666666667")
    if num1 == 43 and sign == '/' and num2 == 25:
        return("43/25 = 1.72")
    if num1 == 43 and sign == '/' and num2 == 26:
        return("43/26 = 1.653846153846153846153846154")
    if num1 == 43 and sign == '/' and num2 == 27:
        return("43/27 = 1.592592592592592592592592593")
    if num1 == 43 and sign == '/' and num2 == 28:
        return("43/28 = 1.535714285714285714285714286")
    if num1 == 43 and sign == '/' and num2 == 29:
        return("43/29 = 1.482758620689655172413793103")
    if num1 == 43 and sign == '/' and num2 == 30:
        return("43/30 = 1.433333333333333333333333333")
    if num1 == 43 and sign == '/' and num2 == 31:
        return("43/31 = 1.387096774193548387096774194")
    if num1 == 43 and sign == '/' and num2 == 32:
        return("43/32 = 1.34375")
    if num1 == 43 and sign == '/' and num2 == 33:
        return("43/33 = 1.303030303030303030303030303")
    if num1 == 43 and sign == '/' and num2 == 34:
        return("43/34 = 1.264705882352941176470588235")
    if num1 == 43 and sign == '/' and num2 == 35:
        return("43/35 = 1.228571428571428571428571429")
    if num1 == 43 and sign == '/' and num2 == 36:
        return("43/36 = 1.194444444444444444444444444")
    if num1 == 43 and sign == '/' and num2 == 37:
        return("43/37 = 1.162162162162162162162162162")
    if num1 == 43 and sign == '/' and num2 == 38:
        return("43/38 = 1.131578947368421052631578947")
    if num1 == 43 and sign == '/' and num2 == 39:
        return("43/39 = 1.102564102564102564102564103")
    if num1 == 43 and sign == '/' and num2 == 40:
        return("43/40 = 1.075")
    if num1 == 43 and sign == '/' and num2 == 41:
        return("43/41 = 1.048780487804878048780487805")
    if num1 == 43 and sign == '/' and num2 == 42:
        return("43/42 = 1.023809523809523809523809524")
    if num1 == 43 and sign == '/' and num2 == 43:
        return("43/43 = 1")
    if num1 == 43 and sign == '/' and num2 == 44:
        return("43/44 = 0.9772727272727272727272727273")
    if num1 == 43 and sign == '/' and num2 == 45:
        return("43/45 = 0.9555555555555555555555555556")
    if num1 == 43 and sign == '/' and num2 == 46:
        return("43/46 = 0.9347826086956521739130434783")
    if num1 == 43 and sign == '/' and num2 == 47:
        return("43/47 = 0.9148936170212765957446808511")
    if num1 == 43 and sign == '/' and num2 == 48:
        return("43/48 = 0.8958333333333333333333333333")
    if num1 == 43 and sign == '/' and num2 == 49:
        return("43/49 = 0.8775510204081632653061224490")
    if num1 == 43 and sign == '/' and num2 == 50:
        return("43/50 = 0.86")
    if num1 == 44 and sign == '/' and num2 == 0:
        return("44/0 = Inf")
    if num1 == 44 and sign == '/' and num2 == 1:
        return("44/1 = 44")
    if num1 == 44 and sign == '/' and num2 == 2:
        return("44/2 = 22")
    if num1 == 44 and sign == '/' and num2 == 3:
        return("44/3 = 14.66666666666666666666666667")
    if num1 == 44 and sign == '/' and num2 == 4:
        return("44/4 = 11")
    if num1 == 44 and sign == '/' and num2 == 5:
        return("44/5 = 8.8")
    if num1 == 44 and sign == '/' and num2 == 6:
        return("44/6 = 7.333333333333333333333333333")
    if num1 == 44 and sign == '/' and num2 == 7:
        return("44/7 = 6.285714285714285714285714286")
    if num1 == 44 and sign == '/' and num2 == 8:
        return("44/8 = 5.5")
    if num1 == 44 and sign == '/' and num2 == 9:
        return("44/9 = 4.888888888888888888888888889")
    if num1 == 44 and sign == '/' and num2 == 10:
        return("44/10 = 4.4")
    if num1 == 44 and sign == '/' and num2 == 11:
        return("44/11 = 4")
    if num1 == 44 and sign == '/' and num2 == 12:
        return("44/12 = 3.666666666666666666666666667")
    if num1 == 44 and sign == '/' and num2 == 13:
        return("44/13 = 3.384615384615384615384615385")
    if num1 == 44 and sign == '/' and num2 == 14:
        return("44/14 = 3.142857142857142857142857143")
    if num1 == 44 and sign == '/' and num2 == 15:
        return("44/15 = 2.933333333333333333333333333")
    if num1 == 44 and sign == '/' and num2 == 16:
        return("44/16 = 2.75")
    if num1 == 44 and sign == '/' and num2 == 17:
        return("44/17 = 2.588235294117647058823529412")
    if num1 == 44 and sign == '/' and num2 == 18:
        return("44/18 = 2.444444444444444444444444444")
    if num1 == 44 and sign == '/' and num2 == 19:
        return("44/19 = 2.315789473684210526315789474")
    if num1 == 44 and sign == '/' and num2 == 20:
        return("44/20 = 2.2")
    if num1 == 44 and sign == '/' and num2 == 21:
        return("44/21 = 2.095238095238095238095238095")
    if num1 == 44 and sign == '/' and num2 == 22:
        return("44/22 = 2")
    if num1 == 44 and sign == '/' and num2 == 23:
        return("44/23 = 1.913043478260869565217391304")
    if num1 == 44 and sign == '/' and num2 == 24:
        return("44/24 = 1.833333333333333333333333333")
    if num1 == 44 and sign == '/' and num2 == 25:
        return("44/25 = 1.76")
    if num1 == 44 and sign == '/' and num2 == 26:
        return("44/26 = 1.692307692307692307692307692")
    if num1 == 44 and sign == '/' and num2 == 27:
        return("44/27 = 1.629629629629629629629629630")
    if num1 == 44 and sign == '/' and num2 == 28:
        return("44/28 = 1.571428571428571428571428571")
    if num1 == 44 and sign == '/' and num2 == 29:
        return("44/29 = 1.517241379310344827586206897")
    if num1 == 44 and sign == '/' and num2 == 30:
        return("44/30 = 1.466666666666666666666666667")
    if num1 == 44 and sign == '/' and num2 == 31:
        return("44/31 = 1.419354838709677419354838710")
    if num1 == 44 and sign == '/' and num2 == 32:
        return("44/32 = 1.375")
    if num1 == 44 and sign == '/' and num2 == 33:
        return("44/33 = 1.333333333333333333333333333")
    if num1 == 44 and sign == '/' and num2 == 34:
        return("44/34 = 1.294117647058823529411764706")
    if num1 == 44 and sign == '/' and num2 == 35:
        return("44/35 = 1.257142857142857142857142857")
    if num1 == 44 and sign == '/' and num2 == 36:
        return("44/36 = 1.222222222222222222222222222")
    if num1 == 44 and sign == '/' and num2 == 37:
        return("44/37 = 1.189189189189189189189189189")
    if num1 == 44 and sign == '/' and num2 == 38:
        return("44/38 = 1.157894736842105263157894737")
    if num1 == 44 and sign == '/' and num2 == 39:
        return("44/39 = 1.128205128205128205128205128")
    if num1 == 44 and sign == '/' and num2 == 40:
        return("44/40 = 1.1")
    if num1 == 44 and sign == '/' and num2 == 41:
        return("44/41 = 1.073170731707317073170731707")
    if num1 == 44 and sign == '/' and num2 == 42:
        return("44/42 = 1.047619047619047619047619048")
    if num1 == 44 and sign == '/' and num2 == 43:
        return("44/43 = 1.023255813953488372093023256")
    if num1 == 44 and sign == '/' and num2 == 44:
        return("44/44 = 1")
    if num1 == 44 and sign == '/' and num2 == 45:
        return("44/45 = 0.9777777777777777777777777778")
    if num1 == 44 and sign == '/' and num2 == 46:
        return("44/46 = 0.9565217391304347826086956522")
    if num1 == 44 and sign == '/' and num2 == 47:
        return("44/47 = 0.9361702127659574468085106383")
    if num1 == 44 and sign == '/' and num2 == 48:
        return("44/48 = 0.9166666666666666666666666667")
    if num1 == 44 and sign == '/' and num2 == 49:
        return("44/49 = 0.8979591836734693877551020408")
    if num1 == 44 and sign == '/' and num2 == 50:
        return("44/50 = 0.88")
    if num1 == 45 and sign == '/' and num2 == 0:
        return("45/0 = Inf")
    if num1 == 45 and sign == '/' and num2 == 1:
        return("45/1 = 45")
    if num1 == 45 and sign == '/' and num2 == 2:
        return("45/2 = 22.5")
    if num1 == 45 and sign == '/' and num2 == 3:
        return("45/3 = 15")
    if num1 == 45 and sign == '/' and num2 == 4:
        return("45/4 = 11.25")
    if num1 == 45 and sign == '/' and num2 == 5:
        return("45/5 = 9")
    if num1 == 45 and sign == '/' and num2 == 6:
        return("45/6 = 7.5")
    if num1 == 45 and sign == '/' and num2 == 7:
        return("45/7 = 6.428571428571428571428571429")
    if num1 == 45 and sign == '/' and num2 == 8:
        return("45/8 = 5.625")
    if num1 == 45 and sign == '/' and num2 == 9:
        return("45/9 = 5")
    if num1 == 45 and sign == '/' and num2 == 10:
        return("45/10 = 4.5")
    if num1 == 45 and sign == '/' and num2 == 11:
        return("45/11 = 4.090909090909090909090909091")
    if num1 == 45 and sign == '/' and num2 == 12:
        return("45/12 = 3.75")
    if num1 == 45 and sign == '/' and num2 == 13:
        return("45/13 = 3.461538461538461538461538462")
    if num1 == 45 and sign == '/' and num2 == 14:
        return("45/14 = 3.214285714285714285714285714")
    if num1 == 45 and sign == '/' and num2 == 15:
        return("45/15 = 3")
    if num1 == 45 and sign == '/' and num2 == 16:
        return("45/16 = 2.8125")
    if num1 == 45 and sign == '/' and num2 == 17:
        return("45/17 = 2.647058823529411764705882353")
    if num1 == 45 and sign == '/' and num2 == 18:
        return("45/18 = 2.5")
    if num1 == 45 and sign == '/' and num2 == 19:
        return("45/19 = 2.368421052631578947368421053")
    if num1 == 45 and sign == '/' and num2 == 20:
        return("45/20 = 2.25")
    if num1 == 45 and sign == '/' and num2 == 21:
        return("45/21 = 2.142857142857142857142857143")
    if num1 == 45 and sign == '/' and num2 == 22:
        return("45/22 = 2.045454545454545454545454545")
    if num1 == 45 and sign == '/' and num2 == 23:
        return("45/23 = 1.956521739130434782608695652")
    if num1 == 45 and sign == '/' and num2 == 24:
        return("45/24 = 1.875")
    if num1 == 45 and sign == '/' and num2 == 25:
        return("45/25 = 1.8")
    if num1 == 45 and sign == '/' and num2 == 26:
        return("45/26 = 1.730769230769230769230769231")
    if num1 == 45 and sign == '/' and num2 == 27:
        return("45/27 = 1.666666666666666666666666667")
    if num1 == 45 and sign == '/' and num2 == 28:
        return("45/28 = 1.607142857142857142857142857")
    if num1 == 45 and sign == '/' and num2 == 29:
        return("45/29 = 1.551724137931034482758620690")
    if num1 == 45 and sign == '/' and num2 == 30:
        return("45/30 = 1.5")
    if num1 == 45 and sign == '/' and num2 == 31:
        return("45/31 = 1.451612903225806451612903226")
    if num1 == 45 and sign == '/' and num2 == 32:
        return("45/32 = 1.40625")
    if num1 == 45 and sign == '/' and num2 == 33:
        return("45/33 = 1.363636363636363636363636364")
    if num1 == 45 and sign == '/' and num2 == 34:
        return("45/34 = 1.323529411764705882352941176")
    if num1 == 45 and sign == '/' and num2 == 35:
        return("45/35 = 1.285714285714285714285714286")
    if num1 == 45 and sign == '/' and num2 == 36:
        return("45/36 = 1.25")
    if num1 == 45 and sign == '/' and num2 == 37:
        return("45/37 = 1.216216216216216216216216216")
    if num1 == 45 and sign == '/' and num2 == 38:
        return("45/38 = 1.184210526315789473684210526")
    if num1 == 45 and sign == '/' and num2 == 39:
        return("45/39 = 1.153846153846153846153846154")
    if num1 == 45 and sign == '/' and num2 == 40:
        return("45/40 = 1.125")
    if num1 == 45 and sign == '/' and num2 == 41:
        return("45/41 = 1.097560975609756097560975610")
    if num1 == 45 and sign == '/' and num2 == 42:
        return("45/42 = 1.071428571428571428571428571")
    if num1 == 45 and sign == '/' and num2 == 43:
        return("45/43 = 1.046511627906976744186046512")
    if num1 == 45 and sign == '/' and num2 == 44:
        return("45/44 = 1.022727272727272727272727273")
    if num1 == 45 and sign == '/' and num2 == 45:
        return("45/45 = 1")
    if num1 == 45 and sign == '/' and num2 == 46:
        return("45/46 = 0.9782608695652173913043478261")
    if num1 == 45 and sign == '/' and num2 == 47:
        return("45/47 = 0.9574468085106382978723404255")
    if num1 == 45 and sign == '/' and num2 == 48:
        return("45/48 = 0.9375")
    if num1 == 45 and sign == '/' and num2 == 49:
        return("45/49 = 0.9183673469387755102040816327")
    if num1 == 45 and sign == '/' and num2 == 50:
        return("45/50 = 0.9")
    if num1 == 46 and sign == '/' and num2 == 0:
        return("46/0 = Inf")
    if num1 == 46 and sign == '/' and num2 == 1:
        return("46/1 = 46")
    if num1 == 46 and sign == '/' and num2 == 2:
        return("46/2 = 23")
    if num1 == 46 and sign == '/' and num2 == 3:
        return("46/3 = 15.33333333333333333333333333")
    if num1 == 46 and sign == '/' and num2 == 4:
        return("46/4 = 11.5")
    if num1 == 46 and sign == '/' and num2 == 5:
        return("46/5 = 9.2")
    if num1 == 46 and sign == '/' and num2 == 6:
        return("46/6 = 7.666666666666666666666666667")
    if num1 == 46 and sign == '/' and num2 == 7:
        return("46/7 = 6.571428571428571428571428571")
    if num1 == 46 and sign == '/' and num2 == 8:
        return("46/8 = 5.75")
    if num1 == 46 and sign == '/' and num2 == 9:
        return("46/9 = 5.111111111111111111111111111")
    if num1 == 46 and sign == '/' and num2 == 10:
        return("46/10 = 4.6")
    if num1 == 46 and sign == '/' and num2 == 11:
        return("46/11 = 4.181818181818181818181818182")
    if num1 == 46 and sign == '/' and num2 == 12:
        return("46/12 = 3.833333333333333333333333333")
    if num1 == 46 and sign == '/' and num2 == 13:
        return("46/13 = 3.538461538461538461538461538")
    if num1 == 46 and sign == '/' and num2 == 14:
        return("46/14 = 3.285714285714285714285714286")
    if num1 == 46 and sign == '/' and num2 == 15:
        return("46/15 = 3.066666666666666666666666667")
    if num1 == 46 and sign == '/' and num2 == 16:
        return("46/16 = 2.875")
    if num1 == 46 and sign == '/' and num2 == 17:
        return("46/17 = 2.705882352941176470588235294")
    if num1 == 46 and sign == '/' and num2 == 18:
        return("46/18 = 2.555555555555555555555555556")
    if num1 == 46 and sign == '/' and num2 == 19:
        return("46/19 = 2.421052631578947368421052632")
    if num1 == 46 and sign == '/' and num2 == 20:
        return("46/20 = 2.3")
    if num1 == 46 and sign == '/' and num2 == 21:
        return("46/21 = 2.190476190476190476190476190")
    if num1 == 46 and sign == '/' and num2 == 22:
        return("46/22 = 2.090909090909090909090909091")
    if num1 == 46 and sign == '/' and num2 == 23:
        return("46/23 = 2")
    if num1 == 46 and sign == '/' and num2 == 24:
        return("46/24 = 1.916666666666666666666666667")
    if num1 == 46 and sign == '/' and num2 == 25:
        return("46/25 = 1.84")
    if num1 == 46 and sign == '/' and num2 == 26:
        return("46/26 = 1.769230769230769230769230769")
    if num1 == 46 and sign == '/' and num2 == 27:
        return("46/27 = 1.703703703703703703703703704")
    if num1 == 46 and sign == '/' and num2 == 28:
        return("46/28 = 1.642857142857142857142857143")
    if num1 == 46 and sign == '/' and num2 == 29:
        return("46/29 = 1.586206896551724137931034483")
    if num1 == 46 and sign == '/' and num2 == 30:
        return("46/30 = 1.533333333333333333333333333")
    if num1 == 46 and sign == '/' and num2 == 31:
        return("46/31 = 1.483870967741935483870967742")
    if num1 == 46 and sign == '/' and num2 == 32:
        return("46/32 = 1.4375")
    if num1 == 46 and sign == '/' and num2 == 33:
        return("46/33 = 1.393939393939393939393939394")
    if num1 == 46 and sign == '/' and num2 == 34:
        return("46/34 = 1.352941176470588235294117647")
    if num1 == 46 and sign == '/' and num2 == 35:
        return("46/35 = 1.314285714285714285714285714")
    if num1 == 46 and sign == '/' and num2 == 36:
        return("46/36 = 1.277777777777777777777777778")
    if num1 == 46 and sign == '/' and num2 == 37:
        return("46/37 = 1.243243243243243243243243243")
    if num1 == 46 and sign == '/' and num2 == 38:
        return("46/38 = 1.210526315789473684210526316")
    if num1 == 46 and sign == '/' and num2 == 39:
        return("46/39 = 1.179487179487179487179487179")
    if num1 == 46 and sign == '/' and num2 == 40:
        return("46/40 = 1.15")
    if num1 == 46 and sign == '/' and num2 == 41:
        return("46/41 = 1.121951219512195121951219512")
    if num1 == 46 and sign == '/' and num2 == 42:
        return("46/42 = 1.095238095238095238095238095")
    if num1 == 46 and sign == '/' and num2 == 43:
        return("46/43 = 1.069767441860465116279069767")
    if num1 == 46 and sign == '/' and num2 == 44:
        return("46/44 = 1.045454545454545454545454545")
    if num1 == 46 and sign == '/' and num2 == 45:
        return("46/45 = 1.022222222222222222222222222")
    if num1 == 46 and sign == '/' and num2 == 46:
        return("46/46 = 1")
    if num1 == 46 and sign == '/' and num2 == 47:
        return("46/47 = 0.9787234042553191489361702128")
    if num1 == 46 and sign == '/' and num2 == 48:
        return("46/48 = 0.9583333333333333333333333333")
    if num1 == 46 and sign == '/' and num2 == 49:
        return("46/49 = 0.9387755102040816326530612245")
    if num1 == 46 and sign == '/' and num2 == 50:
        return("46/50 = 0.92")
    if num1 == 47 and sign == '/' and num2 == 0:
        return("47/0 = Inf")
    if num1 == 47 and sign == '/' and num2 == 1:
        return("47/1 = 47")
    if num1 == 47 and sign == '/' and num2 == 2:
        return("47/2 = 23.5")
    if num1 == 47 and sign == '/' and num2 == 3:
        return("47/3 = 15.66666666666666666666666667")
    if num1 == 47 and sign == '/' and num2 == 4:
        return("47/4 = 11.75")
    if num1 == 47 and sign == '/' and num2 == 5:
        return("47/5 = 9.4")
    if num1 == 47 and sign == '/' and num2 == 6:
        return("47/6 = 7.833333333333333333333333333")
    if num1 == 47 and sign == '/' and num2 == 7:
        return("47/7 = 6.714285714285714285714285714")
    if num1 == 47 and sign == '/' and num2 == 8:
        return("47/8 = 5.875")
    if num1 == 47 and sign == '/' and num2 == 9:
        return("47/9 = 5.222222222222222222222222222")
    if num1 == 47 and sign == '/' and num2 == 10:
        return("47/10 = 4.7")
    if num1 == 47 and sign == '/' and num2 == 11:
        return("47/11 = 4.272727272727272727272727273")
    if num1 == 47 and sign == '/' and num2 == 12:
        return("47/12 = 3.916666666666666666666666667")
    if num1 == 47 and sign == '/' and num2 == 13:
        return("47/13 = 3.615384615384615384615384615")
    if num1 == 47 and sign == '/' and num2 == 14:
        return("47/14 = 3.357142857142857142857142857")
    if num1 == 47 and sign == '/' and num2 == 15:
        return("47/15 = 3.133333333333333333333333333")
    if num1 == 47 and sign == '/' and num2 == 16:
        return("47/16 = 2.9375")
    if num1 == 47 and sign == '/' and num2 == 17:
        return("47/17 = 2.764705882352941176470588235")
    if num1 == 47 and sign == '/' and num2 == 18:
        return("47/18 = 2.611111111111111111111111111")
    if num1 == 47 and sign == '/' and num2 == 19:
        return("47/19 = 2.473684210526315789473684211")
    if num1 == 47 and sign == '/' and num2 == 20:
        return("47/20 = 2.35")
    if num1 == 47 and sign == '/' and num2 == 21:
        return("47/21 = 2.238095238095238095238095238")
    if num1 == 47 and sign == '/' and num2 == 22:
        return("47/22 = 2.136363636363636363636363636")
    if num1 == 47 and sign == '/' and num2 == 23:
        return("47/23 = 2.043478260869565217391304348")
    if num1 == 47 and sign == '/' and num2 == 24:
        return("47/24 = 1.958333333333333333333333333")
    if num1 == 47 and sign == '/' and num2 == 25:
        return("47/25 = 1.88")
    if num1 == 47 and sign == '/' and num2 == 26:
        return("47/26 = 1.807692307692307692307692308")
    if num1 == 47 and sign == '/' and num2 == 27:
        return("47/27 = 1.740740740740740740740740741")
    if num1 == 47 and sign == '/' and num2 == 28:
        return("47/28 = 1.678571428571428571428571429")
    if num1 == 47 and sign == '/' and num2 == 29:
        return("47/29 = 1.620689655172413793103448276")
    if num1 == 47 and sign == '/' and num2 == 30:
        return("47/30 = 1.566666666666666666666666667")
    if num1 == 47 and sign == '/' and num2 == 31:
        return("47/31 = 1.516129032258064516129032258")
    if num1 == 47 and sign == '/' and num2 == 32:
        return("47/32 = 1.46875")
    if num1 == 47 and sign == '/' and num2 == 33:
        return("47/33 = 1.424242424242424242424242424")
    if num1 == 47 and sign == '/' and num2 == 34:
        return("47/34 = 1.382352941176470588235294118")
    if num1 == 47 and sign == '/' and num2 == 35:
        return("47/35 = 1.342857142857142857142857143")
    if num1 == 47 and sign == '/' and num2 == 36:
        return("47/36 = 1.305555555555555555555555556")
    if num1 == 47 and sign == '/' and num2 == 37:
        return("47/37 = 1.270270270270270270270270270")
    if num1 == 47 and sign == '/' and num2 == 38:
        return("47/38 = 1.236842105263157894736842105")
    if num1 == 47 and sign == '/' and num2 == 39:
        return("47/39 = 1.205128205128205128205128205")
    if num1 == 47 and sign == '/' and num2 == 40:
        return("47/40 = 1.175")
    if num1 == 47 and sign == '/' and num2 == 41:
        return("47/41 = 1.146341463414634146341463415")
    if num1 == 47 and sign == '/' and num2 == 42:
        return("47/42 = 1.119047619047619047619047619")
    if num1 == 47 and sign == '/' and num2 == 43:
        return("47/43 = 1.093023255813953488372093023")
    if num1 == 47 and sign == '/' and num2 == 44:
        return("47/44 = 1.068181818181818181818181818")
    if num1 == 47 and sign == '/' and num2 == 45:
        return("47/45 = 1.044444444444444444444444444")
    if num1 == 47 and sign == '/' and num2 == 46:
        return("47/46 = 1.021739130434782608695652174")
    if num1 == 47 and sign == '/' and num2 == 47:
        return("47/47 = 1")
    if num1 == 47 and sign == '/' and num2 == 48:
        return("47/48 = 0.9791666666666666666666666667")
    if num1 == 47 and sign == '/' and num2 == 49:
        return("47/49 = 0.9591836734693877551020408163")
    if num1 == 47 and sign == '/' and num2 == 50:
        return("47/50 = 0.94")
    if num1 == 48 and sign == '/' and num2 == 0:
        return("48/0 = Inf")
    if num1 == 48 and sign == '/' and num2 == 1:
        return("48/1 = 48")
    if num1 == 48 and sign == '/' and num2 == 2:
        return("48/2 = 24")
    if num1 == 48 and sign == '/' and num2 == 3:
        return("48/3 = 16")
    if num1 == 48 and sign == '/' and num2 == 4:
        return("48/4 = 12")
    if num1 == 48 and sign == '/' and num2 == 5:
        return("48/5 = 9.6")
    if num1 == 48 and sign == '/' and num2 == 6:
        return("48/6 = 8")
    if num1 == 48 and sign == '/' and num2 == 7:
        return("48/7 = 6.857142857142857142857142857")
    if num1 == 48 and sign == '/' and num2 == 8:
        return("48/8 = 6")
    if num1 == 48 and sign == '/' and num2 == 9:
        return("48/9 = 5.333333333333333333333333333")
    if num1 == 48 and sign == '/' and num2 == 10:
        return("48/10 = 4.8")
    if num1 == 48 and sign == '/' and num2 == 11:
        return("48/11 = 4.363636363636363636363636364")
    if num1 == 48 and sign == '/' and num2 == 12:
        return("48/12 = 4")
    if num1 == 48 and sign == '/' and num2 == 13:
        return("48/13 = 3.692307692307692307692307692")
    if num1 == 48 and sign == '/' and num2 == 14:
        return("48/14 = 3.428571428571428571428571429")
    if num1 == 48 and sign == '/' and num2 == 15:
        return("48/15 = 3.2")
    if num1 == 48 and sign == '/' and num2 == 16:
        return("48/16 = 3")
    if num1 == 48 and sign == '/' and num2 == 17:
        return("48/17 = 2.823529411764705882352941176")
    if num1 == 48 and sign == '/' and num2 == 18:
        return("48/18 = 2.666666666666666666666666667")
    if num1 == 48 and sign == '/' and num2 == 19:
        return("48/19 = 2.526315789473684210526315789")
    if num1 == 48 and sign == '/' and num2 == 20:
        return("48/20 = 2.4")
    if num1 == 48 and sign == '/' and num2 == 21:
        return("48/21 = 2.285714285714285714285714286")
    if num1 == 48 and sign == '/' and num2 == 22:
        return("48/22 = 2.181818181818181818181818182")
    if num1 == 48 and sign == '/' and num2 == 23:
        return("48/23 = 2.086956521739130434782608696")
    if num1 == 48 and sign == '/' and num2 == 24:
        return("48/24 = 2")
    if num1 == 48 and sign == '/' and num2 == 25:
        return("48/25 = 1.92")
    if num1 == 48 and sign == '/' and num2 == 26:
        return("48/26 = 1.846153846153846153846153846")
    if num1 == 48 and sign == '/' and num2 == 27:
        return("48/27 = 1.777777777777777777777777778")
    if num1 == 48 and sign == '/' and num2 == 28:
        return("48/28 = 1.714285714285714285714285714")
    if num1 == 48 and sign == '/' and num2 == 29:
        return("48/29 = 1.655172413793103448275862069")
    if num1 == 48 and sign == '/' and num2 == 30:
        return("48/30 = 1.6")
    if num1 == 48 and sign == '/' and num2 == 31:
        return("48/31 = 1.548387096774193548387096774")
    if num1 == 48 and sign == '/' and num2 == 32:
        return("48/32 = 1.5")
    if num1 == 48 and sign == '/' and num2 == 33:
        return("48/33 = 1.454545454545454545454545455")
    if num1 == 48 and sign == '/' and num2 == 34:
        return("48/34 = 1.411764705882352941176470588")
    if num1 == 48 and sign == '/' and num2 == 35:
        return("48/35 = 1.371428571428571428571428571")
    if num1 == 48 and sign == '/' and num2 == 36:
        return("48/36 = 1.333333333333333333333333333")
    if num1 == 48 and sign == '/' and num2 == 37:
        return("48/37 = 1.297297297297297297297297297")
    if num1 == 48 and sign == '/' and num2 == 38:
        return("48/38 = 1.263157894736842105263157895")
    if num1 == 48 and sign == '/' and num2 == 39:
        return("48/39 = 1.230769230769230769230769231")
    if num1 == 48 and sign == '/' and num2 == 40:
        return("48/40 = 1.2")
    if num1 == 48 and sign == '/' and num2 == 41:
        return("48/41 = 1.170731707317073170731707317")
    if num1 == 48 and sign == '/' and num2 == 42:
        return("48/42 = 1.142857142857142857142857143")
    if num1 == 48 and sign == '/' and num2 == 43:
        return("48/43 = 1.116279069767441860465116279")
    if num1 == 48 and sign == '/' and num2 == 44:
        return("48/44 = 1.090909090909090909090909091")
    if num1 == 48 and sign == '/' and num2 == 45:
        return("48/45 = 1.066666666666666666666666667")
    if num1 == 48 and sign == '/' and num2 == 46:
        return("48/46 = 1.043478260869565217391304348")
    if num1 == 48 and sign == '/' and num2 == 47:
        return("48/47 = 1.021276595744680851063829787")
    if num1 == 48 and sign == '/' and num2 == 48:
        return("48/48 = 1")
    if num1 == 48 and sign == '/' and num2 == 49:
        return("48/49 = 0.9795918367346938775510204082")
    if num1 == 48 and sign == '/' and num2 == 50:
        return("48/50 = 0.96")
    if num1 == 49 and sign == '/' and num2 == 0:
        return("49/0 = Inf")
    if num1 == 49 and sign == '/' and num2 == 1:
        return("49/1 = 49")
    if num1 == 49 and sign == '/' and num2 == 2:
        return("49/2 = 24.5")
    if num1 == 49 and sign == '/' and num2 == 3:
        return("49/3 = 16.33333333333333333333333333")
    if num1 == 49 and sign == '/' and num2 == 4:
        return("49/4 = 12.25")
    if num1 == 49 and sign == '/' and num2 == 5:
        return("49/5 = 9.8")
    if num1 == 49 and sign == '/' and num2 == 6:
        return("49/6 = 8.166666666666666666666666667")
    if num1 == 49 and sign == '/' and num2 == 7:
        return("49/7 = 7")
    if num1 == 49 and sign == '/' and num2 == 8:
        return("49/8 = 6.125")
    if num1 == 49 and sign == '/' and num2 == 9:
        return("49/9 = 5.444444444444444444444444444")
    if num1 == 49 and sign == '/' and num2 == 10:
        return("49/10 = 4.9")
    if num1 == 49 and sign == '/' and num2 == 11:
        return("49/11 = 4.454545454545454545454545455")
    if num1 == 49 and sign == '/' and num2 == 12:
        return("49/12 = 4.083333333333333333333333333")
    if num1 == 49 and sign == '/' and num2 == 13:
        return("49/13 = 3.769230769230769230769230769")
    if num1 == 49 and sign == '/' and num2 == 14:
        return("49/14 = 3.5")
    if num1 == 49 and sign == '/' and num2 == 15:
        return("49/15 = 3.266666666666666666666666667")
    if num1 == 49 and sign == '/' and num2 == 16:
        return("49/16 = 3.0625")
    if num1 == 49 and sign == '/' and num2 == 17:
        return("49/17 = 2.882352941176470588235294118")
    if num1 == 49 and sign == '/' and num2 == 18:
        return("49/18 = 2.722222222222222222222222222")
    if num1 == 49 and sign == '/' and num2 == 19:
        return("49/19 = 2.578947368421052631578947368")
    if num1 == 49 and sign == '/' and num2 == 20:
        return("49/20 = 2.45")
    if num1 == 49 and sign == '/' and num2 == 21:
        return("49/21 = 2.333333333333333333333333333")
    if num1 == 49 and sign == '/' and num2 == 22:
        return("49/22 = 2.227272727272727272727272727")
    if num1 == 49 and sign == '/' and num2 == 23:
        return("49/23 = 2.130434782608695652173913043")
    if num1 == 49 and sign == '/' and num2 == 24:
        return("49/24 = 2.041666666666666666666666667")
    if num1 == 49 and sign == '/' and num2 == 25:
        return("49/25 = 1.96")
    if num1 == 49 and sign == '/' and num2 == 26:
        return("49/26 = 1.884615384615384615384615385")
    if num1 == 49 and sign == '/' and num2 == 27:
        return("49/27 = 1.814814814814814814814814815")
    if num1 == 49 and sign == '/' and num2 == 28:
        return("49/28 = 1.75")
    if num1 == 49 and sign == '/' and num2 == 29:
        return("49/29 = 1.689655172413793103448275862")
    if num1 == 49 and sign == '/' and num2 == 30:
        return("49/30 = 1.633333333333333333333333333")
    if num1 == 49 and sign == '/' and num2 == 31:
        return("49/31 = 1.580645161290322580645161290")
    if num1 == 49 and sign == '/' and num2 == 32:
        return("49/32 = 1.53125")
    if num1 == 49 and sign == '/' and num2 == 33:
        return("49/33 = 1.484848484848484848484848485")
    if num1 == 49 and sign == '/' and num2 == 34:
        return("49/34 = 1.441176470588235294117647059")
    if num1 == 49 and sign == '/' and num2 == 35:
        return("49/35 = 1.4")
    if num1 == 49 and sign == '/' and num2 == 36:
        return("49/36 = 1.361111111111111111111111111")
    if num1 == 49 and sign == '/' and num2 == 37:
        return("49/37 = 1.324324324324324324324324324")
    if num1 == 49 and sign == '/' and num2 == 38:
        return("49/38 = 1.289473684210526315789473684")
    if num1 == 49 and sign == '/' and num2 == 39:
        return("49/39 = 1.256410256410256410256410256")
    if num1 == 49 and sign == '/' and num2 == 40:
        return("49/40 = 1.225")
    if num1 == 49 and sign == '/' and num2 == 41:
        return("49/41 = 1.195121951219512195121951220")
    if num1 == 49 and sign == '/' and num2 == 42:
        return("49/42 = 1.166666666666666666666666667")
    if num1 == 49 and sign == '/' and num2 == 43:
        return("49/43 = 1.139534883720930232558139535")
    if num1 == 49 and sign == '/' and num2 == 44:
        return("49/44 = 1.113636363636363636363636364")
    if num1 == 49 and sign == '/' and num2 == 45:
        return("49/45 = 1.088888888888888888888888889")
    if num1 == 49 and sign == '/' and num2 == 46:
        return("49/46 = 1.065217391304347826086956522")
    if num1 == 49 and sign == '/' and num2 == 47:
        return("49/47 = 1.042553191489361702127659574")
    if num1 == 49 and sign == '/' and num2 == 48:
        return("49/48 = 1.020833333333333333333333333")
    if num1 == 49 and sign == '/' and num2 == 49:
        return("49/49 = 1")
    if num1 == 49 and sign == '/' and num2 == 50:
        return("49/50 = 0.98")
    if num1 == 50 and sign == '/' and num2 == 0:
        return("50/0 = Inf")
    if num1 == 50 and sign == '/' and num2 == 1:
        return("50/1 = 50")
    if num1 == 50 and sign == '/' and num2 == 2:
        return("50/2 = 25")
    if num1 == 50 and sign == '/' and num2 == 3:
        return("50/3 = 16.66666666666666666666666667")
    if num1 == 50 and sign == '/' and num2 == 4:
        return("50/4 = 12.5")
    if num1 == 50 and sign == '/' and num2 == 5:
        return("50/5 = 10")
    if num1 == 50 and sign == '/' and num2 == 6:
        return("50/6 = 8.333333333333333333333333333")
    if num1 == 50 and sign == '/' and num2 == 7:
        return("50/7 = 7.142857142857142857142857143")
    if num1 == 50 and sign == '/' and num2 == 8:
        return("50/8 = 6.25")
    if num1 == 50 and sign == '/' and num2 == 9:
        return("50/9 = 5.555555555555555555555555556")
    if num1 == 50 and sign == '/' and num2 == 10:
        return("50/10 = 5")
    if num1 == 50 and sign == '/' and num2 == 11:
        return("50/11 = 4.545454545454545454545454545")
    if num1 == 50 and sign == '/' and num2 == 12:
        return("50/12 = 4.166666666666666666666666667")
    if num1 == 50 and sign == '/' and num2 == 13:
        return("50/13 = 3.846153846153846153846153846")
    if num1 == 50 and sign == '/' and num2 == 14:
        return("50/14 = 3.571428571428571428571428571")
    if num1 == 50 and sign == '/' and num2 == 15:
        return("50/15 = 3.333333333333333333333333333")
    if num1 == 50 and sign == '/' and num2 == 16:
        return("50/16 = 3.125")
    if num1 == 50 and sign == '/' and num2 == 17:
        return("50/17 = 2.941176470588235294117647059")
    if num1 == 50 and sign == '/' and num2 == 18:
        return("50/18 = 2.777777777777777777777777778")
    if num1 == 50 and sign == '/' and num2 == 19:
        return("50/19 = 2.631578947368421052631578947")
    if num1 == 50 and sign == '/' and num2 == 20:
        return("50/20 = 2.5")
    if num1 == 50 and sign == '/' and num2 == 21:
        return("50/21 = 2.380952380952380952380952381")
    if num1 == 50 and sign == '/' and num2 == 22:
        return("50/22 = 2.272727272727272727272727273")
    if num1 == 50 and sign == '/' and num2 == 23:
        return("50/23 = 2.173913043478260869565217391")
    if num1 == 50 and sign == '/' and num2 == 24:
        return("50/24 = 2.083333333333333333333333333")
    if num1 == 50 and sign == '/' and num2 == 25:
        return("50/25 = 2")
    if num1 == 50 and sign == '/' and num2 == 26:
        return("50/26 = 1.923076923076923076923076923")
    if num1 == 50 and sign == '/' and num2 == 27:
        return("50/27 = 1.851851851851851851851851852")
    if num1 == 50 and sign == '/' and num2 == 28:
        return("50/28 = 1.785714285714285714285714286")
    if num1 == 50 and sign == '/' and num2 == 29:
        return("50/29 = 1.724137931034482758620689655")
    if num1 == 50 and sign == '/' and num2 == 30:
        return("50/30 = 1.666666666666666666666666667")
    if num1 == 50 and sign == '/' and num2 == 31:
        return("50/31 = 1.612903225806451612903225806")
    if num1 == 50 and sign == '/' and num2 == 32:
        return("50/32 = 1.5625")
    if num1 == 50 and sign == '/' and num2 == 33:
        return("50/33 = 1.515151515151515151515151515")
    if num1 == 50 and sign == '/' and num2 == 34:
        return("50/34 = 1.470588235294117647058823529")
    if num1 == 50 and sign == '/' and num2 == 35:
        return("50/35 = 1.428571428571428571428571429")
    if num1 == 50 and sign == '/' and num2 == 36:
        return("50/36 = 1.388888888888888888888888889")
    if num1 == 50 and sign == '/' and num2 == 37:
        return("50/37 = 1.351351351351351351351351351")
    if num1 == 50 and sign == '/' and num2 == 38:
        return("50/38 = 1.315789473684210526315789474")
    if num1 == 50 and sign == '/' and num2 == 39:
        return("50/39 = 1.282051282051282051282051282")
    if num1 == 50 and sign == '/' and num2 == 40:
        return("50/40 = 1.25")
    if num1 == 50 and sign == '/' and num2 == 41:
        return("50/41 = 1.219512195121951219512195122")
    if num1 == 50 and sign == '/' and num2 == 42:
        return("50/42 = 1.190476190476190476190476190")
    if num1 == 50 and sign == '/' and num2 == 43:
        return("50/43 = 1.162790697674418604651162791")
    if num1 == 50 and sign == '/' and num2 == 44:
        return("50/44 = 1.136363636363636363636363636")
    if num1 == 50 and sign == '/' and num2 == 45:
        return("50/45 = 1.111111111111111111111111111")
    if num1 == 50 and sign == '/' and num2 == 46:
        return("50/46 = 1.086956521739130434782608696")
    if num1 == 50 and sign == '/' and num2 == 47:
        return("50/47 = 1.063829787234042553191489362")
    if num1 == 50 and sign == '/' and num2 == 48:
        return("50/48 = 1.041666666666666666666666667")
    if num1 == 50 and sign == '/' and num2 == 49:
        return("50/49 = 1.020408163265306122448979592")
    if num1 == 50 and sign == '/' and num2 == 50:
        return("50/50 = 1")
    if num1 == 0 and sign == '*' and num2 == 0:
        return("0*0 = 0")
    if num1 == 0 and sign == '*' and num2 == 1:
        return("0*1 = 0")
    if num1 == 0 and sign == '*' and num2 == 2:
        return("0*2 = 0")
    if num1 == 0 and sign == '*' and num2 == 3:
        return("0*3 = 0")
    if num1 == 0 and sign == '*' and num2 == 4:
        return("0*4 = 0")
    if num1 == 0 and sign == '*' and num2 == 5:
        return("0*5 = 0")
    if num1 == 0 and sign == '*' and num2 == 6:
        return("0*6 = 0")
    if num1 == 0 and sign == '*' and num2 == 7:
        return("0*7 = 0")
    if num1 == 0 and sign == '*' and num2 == 8:
        return("0*8 = 0")
    if num1 == 0 and sign == '*' and num2 == 9:
        return("0*9 = 0")
    if num1 == 0 and sign == '*' and num2 == 10:
        return("0*10 = 0")
    if num1 == 0 and sign == '*' and num2 == 11:
        return("0*11 = 0")
    if num1 == 0 and sign == '*' and num2 == 12:
        return("0*12 = 0")
    if num1 == 0 and sign == '*' and num2 == 13:
        return("0*13 = 0")
    if num1 == 0 and sign == '*' and num2 == 14:
        return("0*14 = 0")
    if num1 == 0 and sign == '*' and num2 == 15:
        return("0*15 = 0")
    if num1 == 0 and sign == '*' and num2 == 16:
        return("0*16 = 0")
    if num1 == 0 and sign == '*' and num2 == 17:
        return("0*17 = 0")
    if num1 == 0 and sign == '*' and num2 == 18:
        return("0*18 = 0")
    if num1 == 0 and sign == '*' and num2 == 19:
        return("0*19 = 0")
    if num1 == 0 and sign == '*' and num2 == 20:
        return("0*20 = 0")
    if num1 == 0 and sign == '*' and num2 == 21:
        return("0*21 = 0")
    if num1 == 0 and sign == '*' and num2 == 22:
        return("0*22 = 0")
    if num1 == 0 and sign == '*' and num2 == 23:
        return("0*23 = 0")
    if num1 == 0 and sign == '*' and num2 == 24:
        return("0*24 = 0")
    if num1 == 0 and sign == '*' and num2 == 25:
        return("0*25 = 0")
    if num1 == 0 and sign == '*' and num2 == 26:
        return("0*26 = 0")
    if num1 == 0 and sign == '*' and num2 == 27:
        return("0*27 = 0")
    if num1 == 0 and sign == '*' and num2 == 28:
        return("0*28 = 0")
    if num1 == 0 and sign == '*' and num2 == 29:
        return("0*29 = 0")
    if num1 == 0 and sign == '*' and num2 == 30:
        return("0*30 = 0")
    if num1 == 0 and sign == '*' and num2 == 31:
        return("0*31 = 0")
    if num1 == 0 and sign == '*' and num2 == 32:
        return("0*32 = 0")
    if num1 == 0 and sign == '*' and num2 == 33:
        return("0*33 = 0")
    if num1 == 0 and sign == '*' and num2 == 34:
        return("0*34 = 0")
    if num1 == 0 and sign == '*' and num2 == 35:
        return("0*35 = 0")
    if num1 == 0 and sign == '*' and num2 == 36:
        return("0*36 = 0")
    if num1 == 0 and sign == '*' and num2 == 37:
        return("0*37 = 0")
    if num1 == 0 and sign == '*' and num2 == 38:
        return("0*38 = 0")
    if num1 == 0 and sign == '*' and num2 == 39:
        return("0*39 = 0")
    if num1 == 0 and sign == '*' and num2 == 40:
        return("0*40 = 0")
    if num1 == 0 and sign == '*' and num2 == 41:
        return("0*41 = 0")
    if num1 == 0 and sign == '*' and num2 == 42:
        return("0*42 = 0")
    if num1 == 0 and sign == '*' and num2 == 43:
        return("0*43 = 0")
    if num1 == 0 and sign == '*' and num2 == 44:
        return("0*44 = 0")
    if num1 == 0 and sign == '*' and num2 == 45:
        return("0*45 = 0")
    if num1 == 0 and sign == '*' and num2 == 46:
        return("0*46 = 0")
    if num1 == 0 and sign == '*' and num2 == 47:
        return("0*47 = 0")
    if num1 == 0 and sign == '*' and num2 == 48:
        return("0*48 = 0")
    if num1 == 0 and sign == '*' and num2 == 49:
        return("0*49 = 0")
    if num1 == 0 and sign == '*' and num2 == 50:
        return("0*50 = 0")
    if num1 == 1 and sign == '*' and num2 == 0:
        return("1*0 = 0")
    if num1 == 1 and sign == '*' and num2 == 1:
        return("1*1 = 1")
    if num1 == 1 and sign == '*' and num2 == 2:
        return("1*2 = 2")
    if num1 == 1 and sign == '*' and num2 == 3:
        return("1*3 = 3")
    if num1 == 1 and sign == '*' and num2 == 4:
        return("1*4 = 4")
    if num1 == 1 and sign == '*' and num2 == 5:
        return("1*5 = 5")
    if num1 == 1 and sign == '*' and num2 == 6:
        return("1*6 = 6")
    if num1 == 1 and sign == '*' and num2 == 7:
        return("1*7 = 7")
    if num1 == 1 and sign == '*' and num2 == 8:
        return("1*8 = 8")
    if num1 == 1 and sign == '*' and num2 == 9:
        return("1*9 = 9")
    if num1 == 1 and sign == '*' and num2 == 10:
        return("1*10 = 10")
    if num1 == 1 and sign == '*' and num2 == 11:
        return("1*11 = 11")
    if num1 == 1 and sign == '*' and num2 == 12:
        return("1*12 = 12")
    if num1 == 1 and sign == '*' and num2 == 13:
        return("1*13 = 13")
    if num1 == 1 and sign == '*' and num2 == 14:
        return("1*14 = 14")
    if num1 == 1 and sign == '*' and num2 == 15:
        return("1*15 = 15")
    if num1 == 1 and sign == '*' and num2 == 16:
        return("1*16 = 16")
    if num1 == 1 and sign == '*' and num2 == 17:
        return("1*17 = 17")
    if num1 == 1 and sign == '*' and num2 == 18:
        return("1*18 = 18")
    if num1 == 1 and sign == '*' and num2 == 19:
        return("1*19 = 19")
    if num1 == 1 and sign == '*' and num2 == 20:
        return("1*20 = 20")
    if num1 == 1 and sign == '*' and num2 == 21:
        return("1*21 = 21")
    if num1 == 1 and sign == '*' and num2 == 22:
        return("1*22 = 22")
    if num1 == 1 and sign == '*' and num2 == 23:
        return("1*23 = 23")
    if num1 == 1 and sign == '*' and num2 == 24:
        return("1*24 = 24")
    if num1 == 1 and sign == '*' and num2 == 25:
        return("1*25 = 25")
    if num1 == 1 and sign == '*' and num2 == 26:
        return("1*26 = 26")
    if num1 == 1 and sign == '*' and num2 == 27:
        return("1*27 = 27")
    if num1 == 1 and sign == '*' and num2 == 28:
        return("1*28 = 28")
    if num1 == 1 and sign == '*' and num2 == 29:
        return("1*29 = 29")
    if num1 == 1 and sign == '*' and num2 == 30:
        return("1*30 = 30")
    if num1 == 1 and sign == '*' and num2 == 31:
        return("1*31 = 31")
    if num1 == 1 and sign == '*' and num2 == 32:
        return("1*32 = 32")
    if num1 == 1 and sign == '*' and num2 == 33:
        return("1*33 = 33")
    if num1 == 1 and sign == '*' and num2 == 34:
        return("1*34 = 34")
    if num1 == 1 and sign == '*' and num2 == 35:
        return("1*35 = 35")
    if num1 == 1 and sign == '*' and num2 == 36:
        return("1*36 = 36")
    if num1 == 1 and sign == '*' and num2 == 37:
        return("1*37 = 37")
    if num1 == 1 and sign == '*' and num2 == 38:
        return("1*38 = 38")
    if num1 == 1 and sign == '*' and num2 == 39:
        return("1*39 = 39")
    if num1 == 1 and sign == '*' and num2 == 40:
        return("1*40 = 40")
    if num1 == 1 and sign == '*' and num2 == 41:
        return("1*41 = 41")
    if num1 == 1 and sign == '*' and num2 == 42:
        return("1*42 = 42")
    if num1 == 1 and sign == '*' and num2 == 43:
        return("1*43 = 43")
    if num1 == 1 and sign == '*' and num2 == 44:
        return("1*44 = 44")
    if num1 == 1 and sign == '*' and num2 == 45:
        return("1*45 = 45")
    if num1 == 1 and sign == '*' and num2 == 46:
        return("1*46 = 46")
    if num1 == 1 and sign == '*' and num2 == 47:
        return("1*47 = 47")
    if num1 == 1 and sign == '*' and num2 == 48:
        return("1*48 = 48")
    if num1 == 1 and sign == '*' and num2 == 49:
        return("1*49 = 49")
    if num1 == 1 and sign == '*' and num2 == 50:
        return("1*50 = 50")
    if num1 == 2 and sign == '*' and num2 == 0:
        return("2*0 = 0")
    if num1 == 2 and sign == '*' and num2 == 1:
        return("2*1 = 2")
    if num1 == 2 and sign == '*' and num2 == 2:
        return("2*2 = 4")
    if num1 == 2 and sign == '*' and num2 == 3:
        return("2*3 = 6")
    if num1 == 2 and sign == '*' and num2 == 4:
        return("2*4 = 8")
    if num1 == 2 and sign == '*' and num2 == 5:
        return("2*5 = 10")
    if num1 == 2 and sign == '*' and num2 == 6:
        return("2*6 = 12")
    if num1 == 2 and sign == '*' and num2 == 7:
        return("2*7 = 14")
    if num1 == 2 and sign == '*' and num2 == 8:
        return("2*8 = 16")
    if num1 == 2 and sign == '*' and num2 == 9:
        return("2*9 = 18")
    if num1 == 2 and sign == '*' and num2 == 10:
        return("2*10 = 20")
    if num1 == 2 and sign == '*' and num2 == 11:
        return("2*11 = 22")
    if num1 == 2 and sign == '*' and num2 == 12:
        return("2*12 = 24")
    if num1 == 2 and sign == '*' and num2 == 13:
        return("2*13 = 26")
    if num1 == 2 and sign == '*' and num2 == 14:
        return("2*14 = 28")
    if num1 == 2 and sign == '*' and num2 == 15:
        return("2*15 = 30")
    if num1 == 2 and sign == '*' and num2 == 16:
        return("2*16 = 32")
    if num1 == 2 and sign == '*' and num2 == 17:
        return("2*17 = 34")
    if num1 == 2 and sign == '*' and num2 == 18:
        return("2*18 = 36")
    if num1 == 2 and sign == '*' and num2 == 19:
        return("2*19 = 38")
    if num1 == 2 and sign == '*' and num2 == 20:
        return("2*20 = 40")
    if num1 == 2 and sign == '*' and num2 == 21:
        return("2*21 = 42")
    if num1 == 2 and sign == '*' and num2 == 22:
        return("2*22 = 44")
    if num1 == 2 and sign == '*' and num2 == 23:
        return("2*23 = 46")
    if num1 == 2 and sign == '*' and num2 == 24:
        return("2*24 = 48")
    if num1 == 2 and sign == '*' and num2 == 25:
        return("2*25 = 50")
    if num1 == 2 and sign == '*' and num2 == 26:
        return("2*26 = 52")
    if num1 == 2 and sign == '*' and num2 == 27:
        return("2*27 = 54")
    if num1 == 2 and sign == '*' and num2 == 28:
        return("2*28 = 56")
    if num1 == 2 and sign == '*' and num2 == 29:
        return("2*29 = 58")
    if num1 == 2 and sign == '*' and num2 == 30:
        return("2*30 = 60")
    if num1 == 2 and sign == '*' and num2 == 31:
        return("2*31 = 62")
    if num1 == 2 and sign == '*' and num2 == 32:
        return("2*32 = 64")
    if num1 == 2 and sign == '*' and num2 == 33:
        return("2*33 = 66")
    if num1 == 2 and sign == '*' and num2 == 34:
        return("2*34 = 68")
    if num1 == 2 and sign == '*' and num2 == 35:
        return("2*35 = 70")
    if num1 == 2 and sign == '*' and num2 == 36:
        return("2*36 = 72")
    if num1 == 2 and sign == '*' and num2 == 37:
        return("2*37 = 74")
    if num1 == 2 and sign == '*' and num2 == 38:
        return("2*38 = 76")
    if num1 == 2 and sign == '*' and num2 == 39:
        return("2*39 = 78")
    if num1 == 2 and sign == '*' and num2 == 40:
        return("2*40 = 80")
    if num1 == 2 and sign == '*' and num2 == 41:
        return("2*41 = 82")
    if num1 == 2 and sign == '*' and num2 == 42:
        return("2*42 = 84")
    if num1 == 2 and sign == '*' and num2 == 43:
        return("2*43 = 86")
    if num1 == 2 and sign == '*' and num2 == 44:
        return("2*44 = 88")
    if num1 == 2 and sign == '*' and num2 == 45:
        return("2*45 = 90")
    if num1 == 2 and sign == '*' and num2 == 46:
        return("2*46 = 92")
    if num1 == 2 and sign == '*' and num2 == 47:
        return("2*47 = 94")
    if num1 == 2 and sign == '*' and num2 == 48:
        return("2*48 = 96")
    if num1 == 2 and sign == '*' and num2 == 49:
        return("2*49 = 98")
    if num1 == 2 and sign == '*' and num2 == 50:
        return("2*50 = 100")
    if num1 == 3 and sign == '*' and num2 == 0:
        return("3*0 = 0")
    if num1 == 3 and sign == '*' and num2 == 1:
        return("3*1 = 3")
    if num1 == 3 and sign == '*' and num2 == 2:
        return("3*2 = 6")
    if num1 == 3 and sign == '*' and num2 == 3:
        return("3*3 = 9")
    if num1 == 3 and sign == '*' and num2 == 4:
        return("3*4 = 12")
    if num1 == 3 and sign == '*' and num2 == 5:
        return("3*5 = 15")
    if num1 == 3 and sign == '*' and num2 == 6:
        return("3*6 = 18")
    if num1 == 3 and sign == '*' and num2 == 7:
        return("3*7 = 21")
    if num1 == 3 and sign == '*' and num2 == 8:
        return("3*8 = 24")
    if num1 == 3 and sign == '*' and num2 == 9:
        return("3*9 = 27")
    if num1 == 3 and sign == '*' and num2 == 10:
        return("3*10 = 30")
    if num1 == 3 and sign == '*' and num2 == 11:
        return("3*11 = 33")
    if num1 == 3 and sign == '*' and num2 == 12:
        return("3*12 = 36")
    if num1 == 3 and sign == '*' and num2 == 13:
        return("3*13 = 39")
    if num1 == 3 and sign == '*' and num2 == 14:
        return("3*14 = 42")
    if num1 == 3 and sign == '*' and num2 == 15:
        return("3*15 = 45")
    if num1 == 3 and sign == '*' and num2 == 16:
        return("3*16 = 48")
    if num1 == 3 and sign == '*' and num2 == 17:
        return("3*17 = 51")
    if num1 == 3 and sign == '*' and num2 == 18:
        return("3*18 = 54")
    if num1 == 3 and sign == '*' and num2 == 19:
        return("3*19 = 57")
    if num1 == 3 and sign == '*' and num2 == 20:
        return("3*20 = 60")
    if num1 == 3 and sign == '*' and num2 == 21:
        return("3*21 = 63")
    if num1 == 3 and sign == '*' and num2 == 22:
        return("3*22 = 66")
    if num1 == 3 and sign == '*' and num2 == 23:
        return("3*23 = 69")
    if num1 == 3 and sign == '*' and num2 == 24:
        return("3*24 = 72")
    if num1 == 3 and sign == '*' and num2 == 25:
        return("3*25 = 75")
    if num1 == 3 and sign == '*' and num2 == 26:
        return("3*26 = 78")
    if num1 == 3 and sign == '*' and num2 == 27:
        return("3*27 = 81")
    if num1 == 3 and sign == '*' and num2 == 28:
        return("3*28 = 84")
    if num1 == 3 and sign == '*' and num2 == 29:
        return("3*29 = 87")
    if num1 == 3 and sign == '*' and num2 == 30:
        return("3*30 = 90")
    if num1 == 3 and sign == '*' and num2 == 31:
        return("3*31 = 93")
    if num1 == 3 and sign == '*' and num2 == 32:
        return("3*32 = 96")
    if num1 == 3 and sign == '*' and num2 == 33:
        return("3*33 = 99")
    if num1 == 3 and sign == '*' and num2 == 34:
        return("3*34 = 102")
    if num1 == 3 and sign == '*' and num2 == 35:
        return("3*35 = 105")
    if num1 == 3 and sign == '*' and num2 == 36:
        return("3*36 = 108")
    if num1 == 3 and sign == '*' and num2 == 37:
        return("3*37 = 111")
    if num1 == 3 and sign == '*' and num2 == 38:
        return("3*38 = 114")
    if num1 == 3 and sign == '*' and num2 == 39:
        return("3*39 = 117")
    if num1 == 3 and sign == '*' and num2 == 40:
        return("3*40 = 120")
    if num1 == 3 and sign == '*' and num2 == 41:
        return("3*41 = 123")
    if num1 == 3 and sign == '*' and num2 == 42:
        return("3*42 = 126")
    if num1 == 3 and sign == '*' and num2 == 43:
        return("3*43 = 129")
    if num1 == 3 and sign == '*' and num2 == 44:
        return("3*44 = 132")
    if num1 == 3 and sign == '*' and num2 == 45:
        return("3*45 = 135")
    if num1 == 3 and sign == '*' and num2 == 46:
        return("3*46 = 138")
    if num1 == 3 and sign == '*' and num2 == 47:
        return("3*47 = 141")
    if num1 == 3 and sign == '*' and num2 == 48:
        return("3*48 = 144")
    if num1 == 3 and sign == '*' and num2 == 49:
        return("3*49 = 147")
    if num1 == 3 and sign == '*' and num2 == 50:
        return("3*50 = 150")
    if num1 == 4 and sign == '*' and num2 == 0:
        return("4*0 = 0")
    if num1 == 4 and sign == '*' and num2 == 1:
        return("4*1 = 4")
    if num1 == 4 and sign == '*' and num2 == 2:
        return("4*2 = 8")
    if num1 == 4 and sign == '*' and num2 == 3:
        return("4*3 = 12")
    if num1 == 4 and sign == '*' and num2 == 4:
        return("4*4 = 16")
    if num1 == 4 and sign == '*' and num2 == 5:
        return("4*5 = 20")
    if num1 == 4 and sign == '*' and num2 == 6:
        return("4*6 = 24")
    if num1 == 4 and sign == '*' and num2 == 7:
        return("4*7 = 28")
    if num1 == 4 and sign == '*' and num2 == 8:
        return("4*8 = 32")
    if num1 == 4 and sign == '*' and num2 == 9:
        return("4*9 = 36")
    if num1 == 4 and sign == '*' and num2 == 10:
        return("4*10 = 40")
    if num1 == 4 and sign == '*' and num2 == 11:
        return("4*11 = 44")
    if num1 == 4 and sign == '*' and num2 == 12:
        return("4*12 = 48")
    if num1 == 4 and sign == '*' and num2 == 13:
        return("4*13 = 52")
    if num1 == 4 and sign == '*' and num2 == 14:
        return("4*14 = 56")
    if num1 == 4 and sign == '*' and num2 == 15:
        return("4*15 = 60")
    if num1 == 4 and sign == '*' and num2 == 16:
        return("4*16 = 64")
    if num1 == 4 and sign == '*' and num2 == 17:
        return("4*17 = 68")
    if num1 == 4 and sign == '*' and num2 == 18:
        return("4*18 = 72")
    if num1 == 4 and sign == '*' and num2 == 19:
        return("4*19 = 76")
    if num1 == 4 and sign == '*' and num2 == 20:
        return("4*20 = 80")
    if num1 == 4 and sign == '*' and num2 == 21:
        return("4*21 = 84")
    if num1 == 4 and sign == '*' and num2 == 22:
        return("4*22 = 88")
    if num1 == 4 and sign == '*' and num2 == 23:
        return("4*23 = 92")
    if num1 == 4 and sign == '*' and num2 == 24:
        return("4*24 = 96")
    if num1 == 4 and sign == '*' and num2 == 25:
        return("4*25 = 100")
    if num1 == 4 and sign == '*' and num2 == 26:
        return("4*26 = 104")
    if num1 == 4 and sign == '*' and num2 == 27:
        return("4*27 = 108")
    if num1 == 4 and sign == '*' and num2 == 28:
        return("4*28 = 112")
    if num1 == 4 and sign == '*' and num2 == 29:
        return("4*29 = 116")
    if num1 == 4 and sign == '*' and num2 == 30:
        return("4*30 = 120")
    if num1 == 4 and sign == '*' and num2 == 31:
        return("4*31 = 124")
    if num1 == 4 and sign == '*' and num2 == 32:
        return("4*32 = 128")
    if num1 == 4 and sign == '*' and num2 == 33:
        return("4*33 = 132")
    if num1 == 4 and sign == '*' and num2 == 34:
        return("4*34 = 136")
    if num1 == 4 and sign == '*' and num2 == 35:
        return("4*35 = 140")
    if num1 == 4 and sign == '*' and num2 == 36:
        return("4*36 = 144")
    if num1 == 4 and sign == '*' and num2 == 37:
        return("4*37 = 148")
    if num1 == 4 and sign == '*' and num2 == 38:
        return("4*38 = 152")
    if num1 == 4 and sign == '*' and num2 == 39:
        return("4*39 = 156")
    if num1 == 4 and sign == '*' and num2 == 40:
        return("4*40 = 160")
    if num1 == 4 and sign == '*' and num2 == 41:
        return("4*41 = 164")
    if num1 == 4 and sign == '*' and num2 == 42:
        return("4*42 = 168")
    if num1 == 4 and sign == '*' and num2 == 43:
        return("4*43 = 172")
    if num1 == 4 and sign == '*' and num2 == 44:
        return("4*44 = 176")
    if num1 == 4 and sign == '*' and num2 == 45:
        return("4*45 = 180")
    if num1 == 4 and sign == '*' and num2 == 46:
        return("4*46 = 184")
    if num1 == 4 and sign == '*' and num2 == 47:
        return("4*47 = 188")
    if num1 == 4 and sign == '*' and num2 == 48:
        return("4*48 = 192")
    if num1 == 4 and sign == '*' and num2 == 49:
        return("4*49 = 196")
    if num1 == 4 and sign == '*' and num2 == 50:
        return("4*50 = 200")
    if num1 == 5 and sign == '*' and num2 == 0:
        return("5*0 = 0")
    if num1 == 5 and sign == '*' and num2 == 1:
        return("5*1 = 5")
    if num1 == 5 and sign == '*' and num2 == 2:
        return("5*2 = 10")
    if num1 == 5 and sign == '*' and num2 == 3:
        return("5*3 = 15")
    if num1 == 5 and sign == '*' and num2 == 4:
        return("5*4 = 20")
    if num1 == 5 and sign == '*' and num2 == 5:
        return("5*5 = 25")
    if num1 == 5 and sign == '*' and num2 == 6:
        return("5*6 = 30")
    if num1 == 5 and sign == '*' and num2 == 7:
        return("5*7 = 35")
    if num1 == 5 and sign == '*' and num2 == 8:
        return("5*8 = 40")
    if num1 == 5 and sign == '*' and num2 == 9:
        return("5*9 = 45")
    if num1 == 5 and sign == '*' and num2 == 10:
        return("5*10 = 50")
    if num1 == 5 and sign == '*' and num2 == 11:
        return("5*11 = 55")
    if num1 == 5 and sign == '*' and num2 == 12:
        return("5*12 = 60")
    if num1 == 5 and sign == '*' and num2 == 13:
        return("5*13 = 65")
    if num1 == 5 and sign == '*' and num2 == 14:
        return("5*14 = 70")
    if num1 == 5 and sign == '*' and num2 == 15:
        return("5*15 = 75")
    if num1 == 5 and sign == '*' and num2 == 16:
        return("5*16 = 80")
    if num1 == 5 and sign == '*' and num2 == 17:
        return("5*17 = 85")
    if num1 == 5 and sign == '*' and num2 == 18:
        return("5*18 = 90")
    if num1 == 5 and sign == '*' and num2 == 19:
        return("5*19 = 95")
    if num1 == 5 and sign == '*' and num2 == 20:
        return("5*20 = 100")
    if num1 == 5 and sign == '*' and num2 == 21:
        return("5*21 = 105")
    if num1 == 5 and sign == '*' and num2 == 22:
        return("5*22 = 110")
    if num1 == 5 and sign == '*' and num2 == 23:
        return("5*23 = 115")
    if num1 == 5 and sign == '*' and num2 == 24:
        return("5*24 = 120")
    if num1 == 5 and sign == '*' and num2 == 25:
        return("5*25 = 125")
    if num1 == 5 and sign == '*' and num2 == 26:
        return("5*26 = 130")
    if num1 == 5 and sign == '*' and num2 == 27:
        return("5*27 = 135")
    if num1 == 5 and sign == '*' and num2 == 28:
        return("5*28 = 140")
    if num1 == 5 and sign == '*' and num2 == 29:
        return("5*29 = 145")
    if num1 == 5 and sign == '*' and num2 == 30:
        return("5*30 = 150")
    if num1 == 5 and sign == '*' and num2 == 31:
        return("5*31 = 155")
    if num1 == 5 and sign == '*' and num2 == 32:
        return("5*32 = 160")
    if num1 == 5 and sign == '*' and num2 == 33:
        return("5*33 = 165")
    if num1 == 5 and sign == '*' and num2 == 34:
        return("5*34 = 170")
    if num1 == 5 and sign == '*' and num2 == 35:
        return("5*35 = 175")
    if num1 == 5 and sign == '*' and num2 == 36:
        return("5*36 = 180")
    if num1 == 5 and sign == '*' and num2 == 37:
        return("5*37 = 185")
    if num1 == 5 and sign == '*' and num2 == 38:
        return("5*38 = 190")
    if num1 == 5 and sign == '*' and num2 == 39:
        return("5*39 = 195")
    if num1 == 5 and sign == '*' and num2 == 40:
        return("5*40 = 200")
    if num1 == 5 and sign == '*' and num2 == 41:
        return("5*41 = 205")
    if num1 == 5 and sign == '*' and num2 == 42:
        return("5*42 = 210")
    if num1 == 5 and sign == '*' and num2 == 43:
        return("5*43 = 215")
    if num1 == 5 and sign == '*' and num2 == 44:
        return("5*44 = 220")
    if num1 == 5 and sign == '*' and num2 == 45:
        return("5*45 = 225")
    if num1 == 5 and sign == '*' and num2 == 46:
        return("5*46 = 230")
    if num1 == 5 and sign == '*' and num2 == 47:
        return("5*47 = 235")
    if num1 == 5 and sign == '*' and num2 == 48:
        return("5*48 = 240")
    if num1 == 5 and sign == '*' and num2 == 49:
        return("5*49 = 245")
    if num1 == 5 and sign == '*' and num2 == 50:
        return("5*50 = 250")
    if num1 == 6 and sign == '*' and num2 == 0:
        return("6*0 = 0")
    if num1 == 6 and sign == '*' and num2 == 1:
        return("6*1 = 6")
    if num1 == 6 and sign == '*' and num2 == 2:
        return("6*2 = 12")
    if num1 == 6 and sign == '*' and num2 == 3:
        return("6*3 = 18")
    if num1 == 6 and sign == '*' and num2 == 4:
        return("6*4 = 24")
    if num1 == 6 and sign == '*' and num2 == 5:
        return("6*5 = 30")
    if num1 == 6 and sign == '*' and num2 == 6:
        return("6*6 = 36")
    if num1 == 6 and sign == '*' and num2 == 7:
        return("6*7 = 42")
    if num1 == 6 and sign == '*' and num2 == 8:
        return("6*8 = 48")
    if num1 == 6 and sign == '*' and num2 == 9:
        return("6*9 = 54")
    if num1 == 6 and sign == '*' and num2 == 10:
        return("6*10 = 60")
    if num1 == 6 and sign == '*' and num2 == 11:
        return("6*11 = 66")
    if num1 == 6 and sign == '*' and num2 == 12:
        return("6*12 = 72")
    if num1 == 6 and sign == '*' and num2 == 13:
        return("6*13 = 78")
    if num1 == 6 and sign == '*' and num2 == 14:
        return("6*14 = 84")
    if num1 == 6 and sign == '*' and num2 == 15:
        return("6*15 = 90")
    if num1 == 6 and sign == '*' and num2 == 16:
        return("6*16 = 96")
    if num1 == 6 and sign == '*' and num2 == 17:
        return("6*17 = 102")
    if num1 == 6 and sign == '*' and num2 == 18:
        return("6*18 = 108")
    if num1 == 6 and sign == '*' and num2 == 19:
        return("6*19 = 114")
    if num1 == 6 and sign == '*' and num2 == 20:
        return("6*20 = 120")
    if num1 == 6 and sign == '*' and num2 == 21:
        return("6*21 = 126")
    if num1 == 6 and sign == '*' and num2 == 22:
        return("6*22 = 132")
    if num1 == 6 and sign == '*' and num2 == 23:
        return("6*23 = 138")
    if num1 == 6 and sign == '*' and num2 == 24:
        return("6*24 = 144")
    if num1 == 6 and sign == '*' and num2 == 25:
        return("6*25 = 150")
    if num1 == 6 and sign == '*' and num2 == 26:
        return("6*26 = 156")
    if num1 == 6 and sign == '*' and num2 == 27:
        return("6*27 = 162")
    if num1 == 6 and sign == '*' and num2 == 28:
        return("6*28 = 168")
    if num1 == 6 and sign == '*' and num2 == 29:
        return("6*29 = 174")
    if num1 == 6 and sign == '*' and num2 == 30:
        return("6*30 = 180")
    if num1 == 6 and sign == '*' and num2 == 31:
        return("6*31 = 186")
    if num1 == 6 and sign == '*' and num2 == 32:
        return("6*32 = 192")
    if num1 == 6 and sign == '*' and num2 == 33:
        return("6*33 = 198")
    if num1 == 6 and sign == '*' and num2 == 34:
        return("6*34 = 204")
    if num1 == 6 and sign == '*' and num2 == 35:
        return("6*35 = 210")
    if num1 == 6 and sign == '*' and num2 == 36:
        return("6*36 = 216")
    if num1 == 6 and sign == '*' and num2 == 37:
        return("6*37 = 222")
    if num1 == 6 and sign == '*' and num2 == 38:
        return("6*38 = 228")
    if num1 == 6 and sign == '*' and num2 == 39:
        return("6*39 = 234")
    if num1 == 6 and sign == '*' and num2 == 40:
        return("6*40 = 240")
    if num1 == 6 and sign == '*' and num2 == 41:
        return("6*41 = 246")
    if num1 == 6 and sign == '*' and num2 == 42:
        return("6*42 = 252")
    if num1 == 6 and sign == '*' and num2 == 43:
        return("6*43 = 258")
    if num1 == 6 and sign == '*' and num2 == 44:
        return("6*44 = 264")
    if num1 == 6 and sign == '*' and num2 == 45:
        return("6*45 = 270")
    if num1 == 6 and sign == '*' and num2 == 46:
        return("6*46 = 276")
    if num1 == 6 and sign == '*' and num2 == 47:
        return("6*47 = 282")
    if num1 == 6 and sign == '*' and num2 == 48:
        return("6*48 = 288")
    if num1 == 6 and sign == '*' and num2 == 49:
        return("6*49 = 294")
    if num1 == 6 and sign == '*' and num2 == 50:
        return("6*50 = 300")
    if num1 == 7 and sign == '*' and num2 == 0:
        return("7*0 = 0")
    if num1 == 7 and sign == '*' and num2 == 1:
        return("7*1 = 7")
    if num1 == 7 and sign == '*' and num2 == 2:
        return("7*2 = 14")
    if num1 == 7 and sign == '*' and num2 == 3:
        return("7*3 = 21")
    if num1 == 7 and sign == '*' and num2 == 4:
        return("7*4 = 28")
    if num1 == 7 and sign == '*' and num2 == 5:
        return("7*5 = 35")
    if num1 == 7 and sign == '*' and num2 == 6:
        return("7*6 = 42")
    if num1 == 7 and sign == '*' and num2 == 7:
        return("7*7 = 49")
    if num1 == 7 and sign == '*' and num2 == 8:
        return("7*8 = 56")
    if num1 == 7 and sign == '*' and num2 == 9:
        return("7*9 = 63")
    if num1 == 7 and sign == '*' and num2 == 10:
        return("7*10 = 70")
    if num1 == 7 and sign == '*' and num2 == 11:
        return("7*11 = 77")
    if num1 == 7 and sign == '*' and num2 == 12:
        return("7*12 = 84")
    if num1 == 7 and sign == '*' and num2 == 13:
        return("7*13 = 91")
    if num1 == 7 and sign == '*' and num2 == 14:
        return("7*14 = 98")
    if num1 == 7 and sign == '*' and num2 == 15:
        return("7*15 = 105")
    if num1 == 7 and sign == '*' and num2 == 16:
        return("7*16 = 112")
    if num1 == 7 and sign == '*' and num2 == 17:
        return("7*17 = 119")
    if num1 == 7 and sign == '*' and num2 == 18:
        return("7*18 = 126")
    if num1 == 7 and sign == '*' and num2 == 19:
        return("7*19 = 133")
    if num1 == 7 and sign == '*' and num2 == 20:
        return("7*20 = 140")
    if num1 == 7 and sign == '*' and num2 == 21:
        return("7*21 = 147")
    if num1 == 7 and sign == '*' and num2 == 22:
        return("7*22 = 154")
    if num1 == 7 and sign == '*' and num2 == 23:
        return("7*23 = 161")
    if num1 == 7 and sign == '*' and num2 == 24:
        return("7*24 = 168")
    if num1 == 7 and sign == '*' and num2 == 25:
        return("7*25 = 175")
    if num1 == 7 and sign == '*' and num2 == 26:
        return("7*26 = 182")
    if num1 == 7 and sign == '*' and num2 == 27:
        return("7*27 = 189")
    if num1 == 7 and sign == '*' and num2 == 28:
        return("7*28 = 196")
    if num1 == 7 and sign == '*' and num2 == 29:
        return("7*29 = 203")
    if num1 == 7 and sign == '*' and num2 == 30:
        return("7*30 = 210")
    if num1 == 7 and sign == '*' and num2 == 31:
        return("7*31 = 217")
    if num1 == 7 and sign == '*' and num2 == 32:
        return("7*32 = 224")
    if num1 == 7 and sign == '*' and num2 == 33:
        return("7*33 = 231")
    if num1 == 7 and sign == '*' and num2 == 34:
        return("7*34 = 238")
    if num1 == 7 and sign == '*' and num2 == 35:
        return("7*35 = 245")
    if num1 == 7 and sign == '*' and num2 == 36:
        return("7*36 = 252")
    if num1 == 7 and sign == '*' and num2 == 37:
        return("7*37 = 259")
    if num1 == 7 and sign == '*' and num2 == 38:
        return("7*38 = 266")
    if num1 == 7 and sign == '*' and num2 == 39:
        return("7*39 = 273")
    if num1 == 7 and sign == '*' and num2 == 40:
        return("7*40 = 280")
    if num1 == 7 and sign == '*' and num2 == 41:
        return("7*41 = 287")
    if num1 == 7 and sign == '*' and num2 == 42:
        return("7*42 = 294")
    if num1 == 7 and sign == '*' and num2 == 43:
        return("7*43 = 301")
    if num1 == 7 and sign == '*' and num2 == 44:
        return("7*44 = 308")
    if num1 == 7 and sign == '*' and num2 == 45:
        return("7*45 = 315")
    if num1 == 7 and sign == '*' and num2 == 46:
        return("7*46 = 322")
    if num1 == 7 and sign == '*' and num2 == 47:
        return("7*47 = 329")
    if num1 == 7 and sign == '*' and num2 == 48:
        return("7*48 = 336")
    if num1 == 7 and sign == '*' and num2 == 49:
        return("7*49 = 343")
    if num1 == 7 and sign == '*' and num2 == 50:
        return("7*50 = 350")
    if num1 == 8 and sign == '*' and num2 == 0:
        return("8*0 = 0")
    if num1 == 8 and sign == '*' and num2 == 1:
        return("8*1 = 8")
    if num1 == 8 and sign == '*' and num2 == 2:
        return("8*2 = 16")
    if num1 == 8 and sign == '*' and num2 == 3:
        return("8*3 = 24")
    if num1 == 8 and sign == '*' and num2 == 4:
        return("8*4 = 32")
    if num1 == 8 and sign == '*' and num2 == 5:
        return("8*5 = 40")
    if num1 == 8 and sign == '*' and num2 == 6:
        return("8*6 = 48")
    if num1 == 8 and sign == '*' and num2 == 7:
        return("8*7 = 56")
    if num1 == 8 and sign == '*' and num2 == 8:
        return("8*8 = 64")
    if num1 == 8 and sign == '*' and num2 == 9:
        return("8*9 = 72")
    if num1 == 8 and sign == '*' and num2 == 10:
        return("8*10 = 80")
    if num1 == 8 and sign == '*' and num2 == 11:
        return("8*11 = 88")
    if num1 == 8 and sign == '*' and num2 == 12:
        return("8*12 = 96")
    if num1 == 8 and sign == '*' and num2 == 13:
        return("8*13 = 104")
    if num1 == 8 and sign == '*' and num2 == 14:
        return("8*14 = 112")
    if num1 == 8 and sign == '*' and num2 == 15:
        return("8*15 = 120")
    if num1 == 8 and sign == '*' and num2 == 16:
        return("8*16 = 128")
    if num1 == 8 and sign == '*' and num2 == 17:
        return("8*17 = 136")
    if num1 == 8 and sign == '*' and num2 == 18:
        return("8*18 = 144")
    if num1 == 8 and sign == '*' and num2 == 19:
        return("8*19 = 152")
    if num1 == 8 and sign == '*' and num2 == 20:
        return("8*20 = 160")
    if num1 == 8 and sign == '*' and num2 == 21:
        return("8*21 = 168")
    if num1 == 8 and sign == '*' and num2 == 22:
        return("8*22 = 176")
    if num1 == 8 and sign == '*' and num2 == 23:
        return("8*23 = 184")
    if num1 == 8 and sign == '*' and num2 == 24:
        return("8*24 = 192")
    if num1 == 8 and sign == '*' and num2 == 25:
        return("8*25 = 200")
    if num1 == 8 and sign == '*' and num2 == 26:
        return("8*26 = 208")
    if num1 == 8 and sign == '*' and num2 == 27:
        return("8*27 = 216")
    if num1 == 8 and sign == '*' and num2 == 28:
        return("8*28 = 224")
    if num1 == 8 and sign == '*' and num2 == 29:
        return("8*29 = 232")
    if num1 == 8 and sign == '*' and num2 == 30:
        return("8*30 = 240")
    if num1 == 8 and sign == '*' and num2 == 31:
        return("8*31 = 248")
    if num1 == 8 and sign == '*' and num2 == 32:
        return("8*32 = 256")
    if num1 == 8 and sign == '*' and num2 == 33:
        return("8*33 = 264")
    if num1 == 8 and sign == '*' and num2 == 34:
        return("8*34 = 272")
    if num1 == 8 and sign == '*' and num2 == 35:
        return("8*35 = 280")
    if num1 == 8 and sign == '*' and num2 == 36:
        return("8*36 = 288")
    if num1 == 8 and sign == '*' and num2 == 37:
        return("8*37 = 296")
    if num1 == 8 and sign == '*' and num2 == 38:
        return("8*38 = 304")
    if num1 == 8 and sign == '*' and num2 == 39:
        return("8*39 = 312")
    if num1 == 8 and sign == '*' and num2 == 40:
        return("8*40 = 320")
    if num1 == 8 and sign == '*' and num2 == 41:
        return("8*41 = 328")
    if num1 == 8 and sign == '*' and num2 == 42:
        return("8*42 = 336")
    if num1 == 8 and sign == '*' and num2 == 43:
        return("8*43 = 344")
    if num1 == 8 and sign == '*' and num2 == 44:
        return("8*44 = 352")
    if num1 == 8 and sign == '*' and num2 == 45:
        return("8*45 = 360")
    if num1 == 8 and sign == '*' and num2 == 46:
        return("8*46 = 368")
    if num1 == 8 and sign == '*' and num2 == 47:
        return("8*47 = 376")
    if num1 == 8 and sign == '*' and num2 == 48:
        return("8*48 = 384")
    if num1 == 8 and sign == '*' and num2 == 49:
        return("8*49 = 392")
    if num1 == 8 and sign == '*' and num2 == 50:
        return("8*50 = 400")
    if num1 == 9 and sign == '*' and num2 == 0:
        return("9*0 = 0")
    if num1 == 9 and sign == '*' and num2 == 1:
        return("9*1 = 9")
    if num1 == 9 and sign == '*' and num2 == 2:
        return("9*2 = 18")
    if num1 == 9 and sign == '*' and num2 == 3:
        return("9*3 = 27")
    if num1 == 9 and sign == '*' and num2 == 4:
        return("9*4 = 36")
    if num1 == 9 and sign == '*' and num2 == 5:
        return("9*5 = 45")
    if num1 == 9 and sign == '*' and num2 == 6:
        return("9*6 = 54")
    if num1 == 9 and sign == '*' and num2 == 7:
        return("9*7 = 63")
    if num1 == 9 and sign == '*' and num2 == 8:
        return("9*8 = 72")
    if num1 == 9 and sign == '*' and num2 == 9:
        return("9*9 = 81")
    if num1 == 9 and sign == '*' and num2 == 10:
        return("9*10 = 90")
    if num1 == 9 and sign == '*' and num2 == 11:
        return("9*11 = 99")
    if num1 == 9 and sign == '*' and num2 == 12:
        return("9*12 = 108")
    if num1 == 9 and sign == '*' and num2 == 13:
        return("9*13 = 117")
    if num1 == 9 and sign == '*' and num2 == 14:
        return("9*14 = 126")
    if num1 == 9 and sign == '*' and num2 == 15:
        return("9*15 = 135")
    if num1 == 9 and sign == '*' and num2 == 16:
        return("9*16 = 144")
    if num1 == 9 and sign == '*' and num2 == 17:
        return("9*17 = 153")
    if num1 == 9 and sign == '*' and num2 == 18:
        return("9*18 = 162")
    if num1 == 9 and sign == '*' and num2 == 19:
        return("9*19 = 171")
    if num1 == 9 and sign == '*' and num2 == 20:
        return("9*20 = 180")
    if num1 == 9 and sign == '*' and num2 == 21:
        return("9*21 = 189")
    if num1 == 9 and sign == '*' and num2 == 22:
        return("9*22 = 198")
    if num1 == 9 and sign == '*' and num2 == 23:
        return("9*23 = 207")
    if num1 == 9 and sign == '*' and num2 == 24:
        return("9*24 = 216")
    if num1 == 9 and sign == '*' and num2 == 25:
        return("9*25 = 225")
    if num1 == 9 and sign == '*' and num2 == 26:
        return("9*26 = 234")
    if num1 == 9 and sign == '*' and num2 == 27:
        return("9*27 = 243")
    if num1 == 9 and sign == '*' and num2 == 28:
        return("9*28 = 252")
    if num1 == 9 and sign == '*' and num2 == 29:
        return("9*29 = 261")
    if num1 == 9 and sign == '*' and num2 == 30:
        return("9*30 = 270")
    if num1 == 9 and sign == '*' and num2 == 31:
        return("9*31 = 279")
    if num1 == 9 and sign == '*' and num2 == 32:
        return("9*32 = 288")
    if num1 == 9 and sign == '*' and num2 == 33:
        return("9*33 = 297")
    if num1 == 9 and sign == '*' and num2 == 34:
        return("9*34 = 306")
    if num1 == 9 and sign == '*' and num2 == 35:
        return("9*35 = 315")
    if num1 == 9 and sign == '*' and num2 == 36:
        return("9*36 = 324")
    if num1 == 9 and sign == '*' and num2 == 37:
        return("9*37 = 333")
    if num1 == 9 and sign == '*' and num2 == 38:
        return("9*38 = 342")
    if num1 == 9 and sign == '*' and num2 == 39:
        return("9*39 = 351")
    if num1 == 9 and sign == '*' and num2 == 40:
        return("9*40 = 360")
    if num1 == 9 and sign == '*' and num2 == 41:
        return("9*41 = 369")
    if num1 == 9 and sign == '*' and num2 == 42:
        return("9*42 = 378")
    if num1 == 9 and sign == '*' and num2 == 43:
        return("9*43 = 387")
    if num1 == 9 and sign == '*' and num2 == 44:
        return("9*44 = 396")
    if num1 == 9 and sign == '*' and num2 == 45:
        return("9*45 = 405")
    if num1 == 9 and sign == '*' and num2 == 46:
        return("9*46 = 414")
    if num1 == 9 and sign == '*' and num2 == 47:
        return("9*47 = 423")
    if num1 == 9 and sign == '*' and num2 == 48:
        return("9*48 = 432")
    if num1 == 9 and sign == '*' and num2 == 49:
        return("9*49 = 441")
    if num1 == 9 and sign == '*' and num2 == 50:
        return("9*50 = 450")
    if num1 == 10 and sign == '*' and num2 == 0:
        return("10*0 = 0")
    if num1 == 10 and sign == '*' and num2 == 1:
        return("10*1 = 10")
    if num1 == 10 and sign == '*' and num2 == 2:
        return("10*2 = 20")
    if num1 == 10 and sign == '*' and num2 == 3:
        return("10*3 = 30")
    if num1 == 10 and sign == '*' and num2 == 4:
        return("10*4 = 40")
    if num1 == 10 and sign == '*' and num2 == 5:
        return("10*5 = 50")
    if num1 == 10 and sign == '*' and num2 == 6:
        return("10*6 = 60")
    if num1 == 10 and sign == '*' and num2 == 7:
        return("10*7 = 70")
    if num1 == 10 and sign == '*' and num2 == 8:
        return("10*8 = 80")
    if num1 == 10 and sign == '*' and num2 == 9:
        return("10*9 = 90")
    if num1 == 10 and sign == '*' and num2 == 10:
        return("10*10 = 100")
    if num1 == 10 and sign == '*' and num2 == 11:
        return("10*11 = 110")
    if num1 == 10 and sign == '*' and num2 == 12:
        return("10*12 = 120")
    if num1 == 10 and sign == '*' and num2 == 13:
        return("10*13 = 130")
    if num1 == 10 and sign == '*' and num2 == 14:
        return("10*14 = 140")
    if num1 == 10 and sign == '*' and num2 == 15:
        return("10*15 = 150")
    if num1 == 10 and sign == '*' and num2 == 16:
        return("10*16 = 160")
    if num1 == 10 and sign == '*' and num2 == 17:
        return("10*17 = 170")
    if num1 == 10 and sign == '*' and num2 == 18:
        return("10*18 = 180")
    if num1 == 10 and sign == '*' and num2 == 19:
        return("10*19 = 190")
    if num1 == 10 and sign == '*' and num2 == 20:
        return("10*20 = 200")
    if num1 == 10 and sign == '*' and num2 == 21:
        return("10*21 = 210")
    if num1 == 10 and sign == '*' and num2 == 22:
        return("10*22 = 220")
    if num1 == 10 and sign == '*' and num2 == 23:
        return("10*23 = 230")
    if num1 == 10 and sign == '*' and num2 == 24:
        return("10*24 = 240")
    if num1 == 10 and sign == '*' and num2 == 25:
        return("10*25 = 250")
    if num1 == 10 and sign == '*' and num2 == 26:
        return("10*26 = 260")
    if num1 == 10 and sign == '*' and num2 == 27:
        return("10*27 = 270")
    if num1 == 10 and sign == '*' and num2 == 28:
        return("10*28 = 280")
    if num1 == 10 and sign == '*' and num2 == 29:
        return("10*29 = 290")
    if num1 == 10 and sign == '*' and num2 == 30:
        return("10*30 = 300")
    if num1 == 10 and sign == '*' and num2 == 31:
        return("10*31 = 310")
    if num1 == 10 and sign == '*' and num2 == 32:
        return("10*32 = 320")
    if num1 == 10 and sign == '*' and num2 == 33:
        return("10*33 = 330")
    if num1 == 10 and sign == '*' and num2 == 34:
        return("10*34 = 340")
    if num1 == 10 and sign == '*' and num2 == 35:
        return("10*35 = 350")
    if num1 == 10 and sign == '*' and num2 == 36:
        return("10*36 = 360")
    if num1 == 10 and sign == '*' and num2 == 37:
        return("10*37 = 370")
    if num1 == 10 and sign == '*' and num2 == 38:
        return("10*38 = 380")
    if num1 == 10 and sign == '*' and num2 == 39:
        return("10*39 = 390")
    if num1 == 10 and sign == '*' and num2 == 40:
        return("10*40 = 400")
    if num1 == 10 and sign == '*' and num2 == 41:
        return("10*41 = 410")
    if num1 == 10 and sign == '*' and num2 == 42:
        return("10*42 = 420")
    if num1 == 10 and sign == '*' and num2 == 43:
        return("10*43 = 430")
    if num1 == 10 and sign == '*' and num2 == 44:
        return("10*44 = 440")
    if num1 == 10 and sign == '*' and num2 == 45:
        return("10*45 = 450")
    if num1 == 10 and sign == '*' and num2 == 46:
        return("10*46 = 460")
    if num1 == 10 and sign == '*' and num2 == 47:
        return("10*47 = 470")
    if num1 == 10 and sign == '*' and num2 == 48:
        return("10*48 = 480")
    if num1 == 10 and sign == '*' and num2 == 49:
        return("10*49 = 490")
    if num1 == 10 and sign == '*' and num2 == 50:
        return("10*50 = 500")
    if num1 == 11 and sign == '*' and num2 == 0:
        return("11*0 = 0")
    if num1 == 11 and sign == '*' and num2 == 1:
        return("11*1 = 11")
    if num1 == 11 and sign == '*' and num2 == 2:
        return("11*2 = 22")
    if num1 == 11 and sign == '*' and num2 == 3:
        return("11*3 = 33")
    if num1 == 11 and sign == '*' and num2 == 4:
        return("11*4 = 44")
    if num1 == 11 and sign == '*' and num2 == 5:
        return("11*5 = 55")
    if num1 == 11 and sign == '*' and num2 == 6:
        return("11*6 = 66")
    if num1 == 11 and sign == '*' and num2 == 7:
        return("11*7 = 77")
    if num1 == 11 and sign == '*' and num2 == 8:
        return("11*8 = 88")
    if num1 == 11 and sign == '*' and num2 == 9:
        return("11*9 = 99")
    if num1 == 11 and sign == '*' and num2 == 10:
        return("11*10 = 110")
    if num1 == 11 and sign == '*' and num2 == 11:
        return("11*11 = 121")
    if num1 == 11 and sign == '*' and num2 == 12:
        return("11*12 = 132")
    if num1 == 11 and sign == '*' and num2 == 13:
        return("11*13 = 143")
    if num1 == 11 and sign == '*' and num2 == 14:
        return("11*14 = 154")
    if num1 == 11 and sign == '*' and num2 == 15:
        return("11*15 = 165")
    if num1 == 11 and sign == '*' and num2 == 16:
        return("11*16 = 176")
    if num1 == 11 and sign == '*' and num2 == 17:
        return("11*17 = 187")
    if num1 == 11 and sign == '*' and num2 == 18:
        return("11*18 = 198")
    if num1 == 11 and sign == '*' and num2 == 19:
        return("11*19 = 209")
    if num1 == 11 and sign == '*' and num2 == 20:
        return("11*20 = 220")
    if num1 == 11 and sign == '*' and num2 == 21:
        return("11*21 = 231")
    if num1 == 11 and sign == '*' and num2 == 22:
        return("11*22 = 242")
    if num1 == 11 and sign == '*' and num2 == 23:
        return("11*23 = 253")
    if num1 == 11 and sign == '*' and num2 == 24:
        return("11*24 = 264")
    if num1 == 11 and sign == '*' and num2 == 25:
        return("11*25 = 275")
    if num1 == 11 and sign == '*' and num2 == 26:
        return("11*26 = 286")
    if num1 == 11 and sign == '*' and num2 == 27:
        return("11*27 = 297")
    if num1 == 11 and sign == '*' and num2 == 28:
        return("11*28 = 308")
    if num1 == 11 and sign == '*' and num2 == 29:
        return("11*29 = 319")
    if num1 == 11 and sign == '*' and num2 == 30:
        return("11*30 = 330")
    if num1 == 11 and sign == '*' and num2 == 31:
        return("11*31 = 341")
    if num1 == 11 and sign == '*' and num2 == 32:
        return("11*32 = 352")
    if num1 == 11 and sign == '*' and num2 == 33:
        return("11*33 = 363")
    if num1 == 11 and sign == '*' and num2 == 34:
        return("11*34 = 374")
    if num1 == 11 and sign == '*' and num2 == 35:
        return("11*35 = 385")
    if num1 == 11 and sign == '*' and num2 == 36:
        return("11*36 = 396")
    if num1 == 11 and sign == '*' and num2 == 37:
        return("11*37 = 407")
    if num1 == 11 and sign == '*' and num2 == 38:
        return("11*38 = 418")
    if num1 == 11 and sign == '*' and num2 == 39:
        return("11*39 = 429")
    if num1 == 11 and sign == '*' and num2 == 40:
        return("11*40 = 440")
    if num1 == 11 and sign == '*' and num2 == 41:
        return("11*41 = 451")
    if num1 == 11 and sign == '*' and num2 == 42:
        return("11*42 = 462")
    if num1 == 11 and sign == '*' and num2 == 43:
        return("11*43 = 473")
    if num1 == 11 and sign == '*' and num2 == 44:
        return("11*44 = 484")
    if num1 == 11 and sign == '*' and num2 == 45:
        return("11*45 = 495")
    if num1 == 11 and sign == '*' and num2 == 46:
        return("11*46 = 506")
    if num1 == 11 and sign == '*' and num2 == 47:
        return("11*47 = 517")
    if num1 == 11 and sign == '*' and num2 == 48:
        return("11*48 = 528")
    if num1 == 11 and sign == '*' and num2 == 49:
        return("11*49 = 539")
    if num1 == 11 and sign == '*' and num2 == 50:
        return("11*50 = 550")
    if num1 == 12 and sign == '*' and num2 == 0:
        return("12*0 = 0")
    if num1 == 12 and sign == '*' and num2 == 1:
        return("12*1 = 12")
    if num1 == 12 and sign == '*' and num2 == 2:
        return("12*2 = 24")
    if num1 == 12 and sign == '*' and num2 == 3:
        return("12*3 = 36")
    if num1 == 12 and sign == '*' and num2 == 4:
        return("12*4 = 48")
    if num1 == 12 and sign == '*' and num2 == 5:
        return("12*5 = 60")
    if num1 == 12 and sign == '*' and num2 == 6:
        return("12*6 = 72")
    if num1 == 12 and sign == '*' and num2 == 7:
        return("12*7 = 84")
    if num1 == 12 and sign == '*' and num2 == 8:
        return("12*8 = 96")
    if num1 == 12 and sign == '*' and num2 == 9:
        return("12*9 = 108")
    if num1 == 12 and sign == '*' and num2 == 10:
        return("12*10 = 120")
    if num1 == 12 and sign == '*' and num2 == 11:
        return("12*11 = 132")
    if num1 == 12 and sign == '*' and num2 == 12:
        return("12*12 = 144")
    if num1 == 12 and sign == '*' and num2 == 13:
        return("12*13 = 156")
    if num1 == 12 and sign == '*' and num2 == 14:
        return("12*14 = 168")
    if num1 == 12 and sign == '*' and num2 == 15:
        return("12*15 = 180")
    if num1 == 12 and sign == '*' and num2 == 16:
        return("12*16 = 192")
    if num1 == 12 and sign == '*' and num2 == 17:
        return("12*17 = 204")
    if num1 == 12 and sign == '*' and num2 == 18:
        return("12*18 = 216")
    if num1 == 12 and sign == '*' and num2 == 19:
        return("12*19 = 228")
    if num1 == 12 and sign == '*' and num2 == 20:
        return("12*20 = 240")
    if num1 == 12 and sign == '*' and num2 == 21:
        return("12*21 = 252")
    if num1 == 12 and sign == '*' and num2 == 22:
        return("12*22 = 264")
    if num1 == 12 and sign == '*' and num2 == 23:
        return("12*23 = 276")
    if num1 == 12 and sign == '*' and num2 == 24:
        return("12*24 = 288")
    if num1 == 12 and sign == '*' and num2 == 25:
        return("12*25 = 300")
    if num1 == 12 and sign == '*' and num2 == 26:
        return("12*26 = 312")
    if num1 == 12 and sign == '*' and num2 == 27:
        return("12*27 = 324")
    if num1 == 12 and sign == '*' and num2 == 28:
        return("12*28 = 336")
    if num1 == 12 and sign == '*' and num2 == 29:
        return("12*29 = 348")
    if num1 == 12 and sign == '*' and num2 == 30:
        return("12*30 = 360")
    if num1 == 12 and sign == '*' and num2 == 31:
        return("12*31 = 372")
    if num1 == 12 and sign == '*' and num2 == 32:
        return("12*32 = 384")
    if num1 == 12 and sign == '*' and num2 == 33:
        return("12*33 = 396")
    if num1 == 12 and sign == '*' and num2 == 34:
        return("12*34 = 408")
    if num1 == 12 and sign == '*' and num2 == 35:
        return("12*35 = 420")
    if num1 == 12 and sign == '*' and num2 == 36:
        return("12*36 = 432")
    if num1 == 12 and sign == '*' and num2 == 37:
        return("12*37 = 444")
    if num1 == 12 and sign == '*' and num2 == 38:
        return("12*38 = 456")
    if num1 == 12 and sign == '*' and num2 == 39:
        return("12*39 = 468")
    if num1 == 12 and sign == '*' and num2 == 40:
        return("12*40 = 480")
    if num1 == 12 and sign == '*' and num2 == 41:
        return("12*41 = 492")
    if num1 == 12 and sign == '*' and num2 == 42:
        return("12*42 = 504")
    if num1 == 12 and sign == '*' and num2 == 43:
        return("12*43 = 516")
    if num1 == 12 and sign == '*' and num2 == 44:
        return("12*44 = 528")
    if num1 == 12 and sign == '*' and num2 == 45:
        return("12*45 = 540")
    if num1 == 12 and sign == '*' and num2 == 46:
        return("12*46 = 552")
    if num1 == 12 and sign == '*' and num2 == 47:
        return("12*47 = 564")
    if num1 == 12 and sign == '*' and num2 == 48:
        return("12*48 = 576")
    if num1 == 12 and sign == '*' and num2 == 49:
        return("12*49 = 588")
    if num1 == 12 and sign == '*' and num2 == 50:
        return("12*50 = 600")
    if num1 == 13 and sign == '*' and num2 == 0:
        return("13*0 = 0")
    if num1 == 13 and sign == '*' and num2 == 1:
        return("13*1 = 13")
    if num1 == 13 and sign == '*' and num2 == 2:
        return("13*2 = 26")
    if num1 == 13 and sign == '*' and num2 == 3:
        return("13*3 = 39")
    if num1 == 13 and sign == '*' and num2 == 4:
        return("13*4 = 52")
    if num1 == 13 and sign == '*' and num2 == 5:
        return("13*5 = 65")
    if num1 == 13 and sign == '*' and num2 == 6:
        return("13*6 = 78")
    if num1 == 13 and sign == '*' and num2 == 7:
        return("13*7 = 91")
    if num1 == 13 and sign == '*' and num2 == 8:
        return("13*8 = 104")
    if num1 == 13 and sign == '*' and num2 == 9:
        return("13*9 = 117")
    if num1 == 13 and sign == '*' and num2 == 10:
        return("13*10 = 130")
    if num1 == 13 and sign == '*' and num2 == 11:
        return("13*11 = 143")
    if num1 == 13 and sign == '*' and num2 == 12:
        return("13*12 = 156")
    if num1 == 13 and sign == '*' and num2 == 13:
        return("13*13 = 169")
    if num1 == 13 and sign == '*' and num2 == 14:
        return("13*14 = 182")
    if num1 == 13 and sign == '*' and num2 == 15:
        return("13*15 = 195")
    if num1 == 13 and sign == '*' and num2 == 16:
        return("13*16 = 208")
    if num1 == 13 and sign == '*' and num2 == 17:
        return("13*17 = 221")
    if num1 == 13 and sign == '*' and num2 == 18:
        return("13*18 = 234")
    if num1 == 13 and sign == '*' and num2 == 19:
        return("13*19 = 247")
    if num1 == 13 and sign == '*' and num2 == 20:
        return("13*20 = 260")
    if num1 == 13 and sign == '*' and num2 == 21:
        return("13*21 = 273")
    if num1 == 13 and sign == '*' and num2 == 22:
        return("13*22 = 286")
    if num1 == 13 and sign == '*' and num2 == 23:
        return("13*23 = 299")
    if num1 == 13 and sign == '*' and num2 == 24:
        return("13*24 = 312")
    if num1 == 13 and sign == '*' and num2 == 25:
        return("13*25 = 325")
    if num1 == 13 and sign == '*' and num2 == 26:
        return("13*26 = 338")
    if num1 == 13 and sign == '*' and num2 == 27:
        return("13*27 = 351")
    if num1 == 13 and sign == '*' and num2 == 28:
        return("13*28 = 364")
    if num1 == 13 and sign == '*' and num2 == 29:
        return("13*29 = 377")
    if num1 == 13 and sign == '*' and num2 == 30:
        return("13*30 = 390")
    if num1 == 13 and sign == '*' and num2 == 31:
        return("13*31 = 403")
    if num1 == 13 and sign == '*' and num2 == 32:
        return("13*32 = 416")
    if num1 == 13 and sign == '*' and num2 == 33:
        return("13*33 = 429")
    if num1 == 13 and sign == '*' and num2 == 34:
        return("13*34 = 442")
    if num1 == 13 and sign == '*' and num2 == 35:
        return("13*35 = 455")
    if num1 == 13 and sign == '*' and num2 == 36:
        return("13*36 = 468")
    if num1 == 13 and sign == '*' and num2 == 37:
        return("13*37 = 481")
    if num1 == 13 and sign == '*' and num2 == 38:
        return("13*38 = 494")
    if num1 == 13 and sign == '*' and num2 == 39:
        return("13*39 = 507")
    if num1 == 13 and sign == '*' and num2 == 40:
        return("13*40 = 520")
    if num1 == 13 and sign == '*' and num2 == 41:
        return("13*41 = 533")
    if num1 == 13 and sign == '*' and num2 == 42:
        return("13*42 = 546")
    if num1 == 13 and sign == '*' and num2 == 43:
        return("13*43 = 559")
    if num1 == 13 and sign == '*' and num2 == 44:
        return("13*44 = 572")
    if num1 == 13 and sign == '*' and num2 == 45:
        return("13*45 = 585")
    if num1 == 13 and sign == '*' and num2 == 46:
        return("13*46 = 598")
    if num1 == 13 and sign == '*' and num2 == 47:
        return("13*47 = 611")
    if num1 == 13 and sign == '*' and num2 == 48:
        return("13*48 = 624")
    if num1 == 13 and sign == '*' and num2 == 49:
        return("13*49 = 637")
    if num1 == 13 and sign == '*' and num2 == 50:
        return("13*50 = 650")
    if num1 == 14 and sign == '*' and num2 == 0:
        return("14*0 = 0")
    if num1 == 14 and sign == '*' and num2 == 1:
        return("14*1 = 14")
    if num1 == 14 and sign == '*' and num2 == 2:
        return("14*2 = 28")
    if num1 == 14 and sign == '*' and num2 == 3:
        return("14*3 = 42")
    if num1 == 14 and sign == '*' and num2 == 4:
        return("14*4 = 56")
    if num1 == 14 and sign == '*' and num2 == 5:
        return("14*5 = 70")
    if num1 == 14 and sign == '*' and num2 == 6:
        return("14*6 = 84")
    if num1 == 14 and sign == '*' and num2 == 7:
        return("14*7 = 98")
    if num1 == 14 and sign == '*' and num2 == 8:
        return("14*8 = 112")
    if num1 == 14 and sign == '*' and num2 == 9:
        return("14*9 = 126")
    if num1 == 14 and sign == '*' and num2 == 10:
        return("14*10 = 140")
    if num1 == 14 and sign == '*' and num2 == 11:
        return("14*11 = 154")
    if num1 == 14 and sign == '*' and num2 == 12:
        return("14*12 = 168")
    if num1 == 14 and sign == '*' and num2 == 13:
        return("14*13 = 182")
    if num1 == 14 and sign == '*' and num2 == 14:
        return("14*14 = 196")
    if num1 == 14 and sign == '*' and num2 == 15:
        return("14*15 = 210")
    if num1 == 14 and sign == '*' and num2 == 16:
        return("14*16 = 224")
    if num1 == 14 and sign == '*' and num2 == 17:
        return("14*17 = 238")
    if num1 == 14 and sign == '*' and num2 == 18:
        return("14*18 = 252")
    if num1 == 14 and sign == '*' and num2 == 19:
        return("14*19 = 266")
    if num1 == 14 and sign == '*' and num2 == 20:
        return("14*20 = 280")
    if num1 == 14 and sign == '*' and num2 == 21:
        return("14*21 = 294")
    if num1 == 14 and sign == '*' and num2 == 22:
        return("14*22 = 308")
    if num1 == 14 and sign == '*' and num2 == 23:
        return("14*23 = 322")
    if num1 == 14 and sign == '*' and num2 == 24:
        return("14*24 = 336")
    if num1 == 14 and sign == '*' and num2 == 25:
        return("14*25 = 350")
    if num1 == 14 and sign == '*' and num2 == 26:
        return("14*26 = 364")
    if num1 == 14 and sign == '*' and num2 == 27:
        return("14*27 = 378")
    if num1 == 14 and sign == '*' and num2 == 28:
        return("14*28 = 392")
    if num1 == 14 and sign == '*' and num2 == 29:
        return("14*29 = 406")
    if num1 == 14 and sign == '*' and num2 == 30:
        return("14*30 = 420")
    if num1 == 14 and sign == '*' and num2 == 31:
        return("14*31 = 434")
    if num1 == 14 and sign == '*' and num2 == 32:
        return("14*32 = 448")
    if num1 == 14 and sign == '*' and num2 == 33:
        return("14*33 = 462")
    if num1 == 14 and sign == '*' and num2 == 34:
        return("14*34 = 476")
    if num1 == 14 and sign == '*' and num2 == 35:
        return("14*35 = 490")
    if num1 == 14 and sign == '*' and num2 == 36:
        return("14*36 = 504")
    if num1 == 14 and sign == '*' and num2 == 37:
        return("14*37 = 518")
    if num1 == 14 and sign == '*' and num2 == 38:
        return("14*38 = 532")
    if num1 == 14 and sign == '*' and num2 == 39:
        return("14*39 = 546")
    if num1 == 14 and sign == '*' and num2 == 40:
        return("14*40 = 560")
    if num1 == 14 and sign == '*' and num2 == 41:
        return("14*41 = 574")
    if num1 == 14 and sign == '*' and num2 == 42:
        return("14*42 = 588")
    if num1 == 14 and sign == '*' and num2 == 43:
        return("14*43 = 602")
    if num1 == 14 and sign == '*' and num2 == 44:
        return("14*44 = 616")
    if num1 == 14 and sign == '*' and num2 == 45:
        return("14*45 = 630")
    if num1 == 14 and sign == '*' and num2 == 46:
        return("14*46 = 644")
    if num1 == 14 and sign == '*' and num2 == 47:
        return("14*47 = 658")
    if num1 == 14 and sign == '*' and num2 == 48:
        return("14*48 = 672")
    if num1 == 14 and sign == '*' and num2 == 49:
        return("14*49 = 686")
    if num1 == 14 and sign == '*' and num2 == 50:
        return("14*50 = 700")
    if num1 == 15 and sign == '*' and num2 == 0:
        return("15*0 = 0")
    if num1 == 15 and sign == '*' and num2 == 1:
        return("15*1 = 15")
    if num1 == 15 and sign == '*' and num2 == 2:
        return("15*2 = 30")
    if num1 == 15 and sign == '*' and num2 == 3:
        return("15*3 = 45")
    if num1 == 15 and sign == '*' and num2 == 4:
        return("15*4 = 60")
    if num1 == 15 and sign == '*' and num2 == 5:
        return("15*5 = 75")
    if num1 == 15 and sign == '*' and num2 == 6:
        return("15*6 = 90")
    if num1 == 15 and sign == '*' and num2 == 7:
        return("15*7 = 105")
    if num1 == 15 and sign == '*' and num2 == 8:
        return("15*8 = 120")
    if num1 == 15 and sign == '*' and num2 == 9:
        return("15*9 = 135")
    if num1 == 15 and sign == '*' and num2 == 10:
        return("15*10 = 150")
    if num1 == 15 and sign == '*' and num2 == 11:
        return("15*11 = 165")
    if num1 == 15 and sign == '*' and num2 == 12:
        return("15*12 = 180")
    if num1 == 15 and sign == '*' and num2 == 13:
        return("15*13 = 195")
    if num1 == 15 and sign == '*' and num2 == 14:
        return("15*14 = 210")
    if num1 == 15 and sign == '*' and num2 == 15:
        return("15*15 = 225")
    if num1 == 15 and sign == '*' and num2 == 16:
        return("15*16 = 240")
    if num1 == 15 and sign == '*' and num2 == 17:
        return("15*17 = 255")
    if num1 == 15 and sign == '*' and num2 == 18:
        return("15*18 = 270")
    if num1 == 15 and sign == '*' and num2 == 19:
        return("15*19 = 285")
    if num1 == 15 and sign == '*' and num2 == 20:
        return("15*20 = 300")
    if num1 == 15 and sign == '*' and num2 == 21:
        return("15*21 = 315")
    if num1 == 15 and sign == '*' and num2 == 22:
        return("15*22 = 330")
    if num1 == 15 and sign == '*' and num2 == 23:
        return("15*23 = 345")
    if num1 == 15 and sign == '*' and num2 == 24:
        return("15*24 = 360")
    if num1 == 15 and sign == '*' and num2 == 25:
        return("15*25 = 375")
    if num1 == 15 and sign == '*' and num2 == 26:
        return("15*26 = 390")
    if num1 == 15 and sign == '*' and num2 == 27:
        return("15*27 = 405")
    if num1 == 15 and sign == '*' and num2 == 28:
        return("15*28 = 420")
    if num1 == 15 and sign == '*' and num2 == 29:
        return("15*29 = 435")
    if num1 == 15 and sign == '*' and num2 == 30:
        return("15*30 = 450")
    if num1 == 15 and sign == '*' and num2 == 31:
        return("15*31 = 465")
    if num1 == 15 and sign == '*' and num2 == 32:
        return("15*32 = 480")
    if num1 == 15 and sign == '*' and num2 == 33:
        return("15*33 = 495")
    if num1 == 15 and sign == '*' and num2 == 34:
        return("15*34 = 510")
    if num1 == 15 and sign == '*' and num2 == 35:
        return("15*35 = 525")
    if num1 == 15 and sign == '*' and num2 == 36:
        return("15*36 = 540")
    if num1 == 15 and sign == '*' and num2 == 37:
        return("15*37 = 555")
    if num1 == 15 and sign == '*' and num2 == 38:
        return("15*38 = 570")
    if num1 == 15 and sign == '*' and num2 == 39:
        return("15*39 = 585")
    if num1 == 15 and sign == '*' and num2 == 40:
        return("15*40 = 600")
    if num1 == 15 and sign == '*' and num2 == 41:
        return("15*41 = 615")
    if num1 == 15 and sign == '*' and num2 == 42:
        return("15*42 = 630")
    if num1 == 15 and sign == '*' and num2 == 43:
        return("15*43 = 645")
    if num1 == 15 and sign == '*' and num2 == 44:
        return("15*44 = 660")
    if num1 == 15 and sign == '*' and num2 == 45:
        return("15*45 = 675")
    if num1 == 15 and sign == '*' and num2 == 46:
        return("15*46 = 690")
    if num1 == 15 and sign == '*' and num2 == 47:
        return("15*47 = 705")
    if num1 == 15 and sign == '*' and num2 == 48:
        return("15*48 = 720")
    if num1 == 15 and sign == '*' and num2 == 49:
        return("15*49 = 735")
    if num1 == 15 and sign == '*' and num2 == 50:
        return("15*50 = 750")
    if num1 == 16 and sign == '*' and num2 == 0:
        return("16*0 = 0")
    if num1 == 16 and sign == '*' and num2 == 1:
        return("16*1 = 16")
    if num1 == 16 and sign == '*' and num2 == 2:
        return("16*2 = 32")
    if num1 == 16 and sign == '*' and num2 == 3:
        return("16*3 = 48")
    if num1 == 16 and sign == '*' and num2 == 4:
        return("16*4 = 64")
    if num1 == 16 and sign == '*' and num2 == 5:
        return("16*5 = 80")
    if num1 == 16 and sign == '*' and num2 == 6:
        return("16*6 = 96")
    if num1 == 16 and sign == '*' and num2 == 7:
        return("16*7 = 112")
    if num1 == 16 and sign == '*' and num2 == 8:
        return("16*8 = 128")
    if num1 == 16 and sign == '*' and num2 == 9:
        return("16*9 = 144")
    if num1 == 16 and sign == '*' and num2 == 10:
        return("16*10 = 160")
    if num1 == 16 and sign == '*' and num2 == 11:
        return("16*11 = 176")
    if num1 == 16 and sign == '*' and num2 == 12:
        return("16*12 = 192")
    if num1 == 16 and sign == '*' and num2 == 13:
        return("16*13 = 208")
    if num1 == 16 and sign == '*' and num2 == 14:
        return("16*14 = 224")
    if num1 == 16 and sign == '*' and num2 == 15:
        return("16*15 = 240")
    if num1 == 16 and sign == '*' and num2 == 16:
        return("16*16 = 256")
    if num1 == 16 and sign == '*' and num2 == 17:
        return("16*17 = 272")
    if num1 == 16 and sign == '*' and num2 == 18:
        return("16*18 = 288")
    if num1 == 16 and sign == '*' and num2 == 19:
        return("16*19 = 304")
    if num1 == 16 and sign == '*' and num2 == 20:
        return("16*20 = 320")
    if num1 == 16 and sign == '*' and num2 == 21:
        return("16*21 = 336")
    if num1 == 16 and sign == '*' and num2 == 22:
        return("16*22 = 352")
    if num1 == 16 and sign == '*' and num2 == 23:
        return("16*23 = 368")
    if num1 == 16 and sign == '*' and num2 == 24:
        return("16*24 = 384")
    if num1 == 16 and sign == '*' and num2 == 25:
        return("16*25 = 400")
    if num1 == 16 and sign == '*' and num2 == 26:
        return("16*26 = 416")
    if num1 == 16 and sign == '*' and num2 == 27:
        return("16*27 = 432")
    if num1 == 16 and sign == '*' and num2 == 28:
        return("16*28 = 448")
    if num1 == 16 and sign == '*' and num2 == 29:
        return("16*29 = 464")
    if num1 == 16 and sign == '*' and num2 == 30:
        return("16*30 = 480")
    if num1 == 16 and sign == '*' and num2 == 31:
        return("16*31 = 496")
    if num1 == 16 and sign == '*' and num2 == 32:
        return("16*32 = 512")
    if num1 == 16 and sign == '*' and num2 == 33:
        return("16*33 = 528")
    if num1 == 16 and sign == '*' and num2 == 34:
        return("16*34 = 544")
    if num1 == 16 and sign == '*' and num2 == 35:
        return("16*35 = 560")
    if num1 == 16 and sign == '*' and num2 == 36:
        return("16*36 = 576")
    if num1 == 16 and sign == '*' and num2 == 37:
        return("16*37 = 592")
    if num1 == 16 and sign == '*' and num2 == 38:
        return("16*38 = 608")
    if num1 == 16 and sign == '*' and num2 == 39:
        return("16*39 = 624")
    if num1 == 16 and sign == '*' and num2 == 40:
        return("16*40 = 640")
    if num1 == 16 and sign == '*' and num2 == 41:
        return("16*41 = 656")
    if num1 == 16 and sign == '*' and num2 == 42:
        return("16*42 = 672")
    if num1 == 16 and sign == '*' and num2 == 43:
        return("16*43 = 688")
    if num1 == 16 and sign == '*' and num2 == 44:
        return("16*44 = 704")
    if num1 == 16 and sign == '*' and num2 == 45:
        return("16*45 = 720")
    if num1 == 16 and sign == '*' and num2 == 46:
        return("16*46 = 736")
    if num1 == 16 and sign == '*' and num2 == 47:
        return("16*47 = 752")
    if num1 == 16 and sign == '*' and num2 == 48:
        return("16*48 = 768")
    if num1 == 16 and sign == '*' and num2 == 49:
        return("16*49 = 784")
    if num1 == 16 and sign == '*' and num2 == 50:
        return("16*50 = 800")
    if num1 == 17 and sign == '*' and num2 == 0:
        return("17*0 = 0")
    if num1 == 17 and sign == '*' and num2 == 1:
        return("17*1 = 17")
    if num1 == 17 and sign == '*' and num2 == 2:
        return("17*2 = 34")
    if num1 == 17 and sign == '*' and num2 == 3:
        return("17*3 = 51")
    if num1 == 17 and sign == '*' and num2 == 4:
        return("17*4 = 68")
    if num1 == 17 and sign == '*' and num2 == 5:
        return("17*5 = 85")
    if num1 == 17 and sign == '*' and num2 == 6:
        return("17*6 = 102")
    if num1 == 17 and sign == '*' and num2 == 7:
        return("17*7 = 119")
    if num1 == 17 and sign == '*' and num2 == 8:
        return("17*8 = 136")
    if num1 == 17 and sign == '*' and num2 == 9:
        return("17*9 = 153")
    if num1 == 17 and sign == '*' and num2 == 10:
        return("17*10 = 170")
    if num1 == 17 and sign == '*' and num2 == 11:
        return("17*11 = 187")
    if num1 == 17 and sign == '*' and num2 == 12:
        return("17*12 = 204")
    if num1 == 17 and sign == '*' and num2 == 13:
        return("17*13 = 221")
    if num1 == 17 and sign == '*' and num2 == 14:
        return("17*14 = 238")
    if num1 == 17 and sign == '*' and num2 == 15:
        return("17*15 = 255")
    if num1 == 17 and sign == '*' and num2 == 16:
        return("17*16 = 272")
    if num1 == 17 and sign == '*' and num2 == 17:
        return("17*17 = 289")
    if num1 == 17 and sign == '*' and num2 == 18:
        return("17*18 = 306")
    if num1 == 17 and sign == '*' and num2 == 19:
        return("17*19 = 323")
    if num1 == 17 and sign == '*' and num2 == 20:
        return("17*20 = 340")
    if num1 == 17 and sign == '*' and num2 == 21:
        return("17*21 = 357")
    if num1 == 17 and sign == '*' and num2 == 22:
        return("17*22 = 374")
    if num1 == 17 and sign == '*' and num2 == 23:
        return("17*23 = 391")
    if num1 == 17 and sign == '*' and num2 == 24:
        return("17*24 = 408")
    if num1 == 17 and sign == '*' and num2 == 25:
        return("17*25 = 425")
    if num1 == 17 and sign == '*' and num2 == 26:
        return("17*26 = 442")
    if num1 == 17 and sign == '*' and num2 == 27:
        return("17*27 = 459")
    if num1 == 17 and sign == '*' and num2 == 28:
        return("17*28 = 476")
    if num1 == 17 and sign == '*' and num2 == 29:
        return("17*29 = 493")
    if num1 == 17 and sign == '*' and num2 == 30:
        return("17*30 = 510")
    if num1 == 17 and sign == '*' and num2 == 31:
        return("17*31 = 527")
    if num1 == 17 and sign == '*' and num2 == 32:
        return("17*32 = 544")
    if num1 == 17 and sign == '*' and num2 == 33:
        return("17*33 = 561")
    if num1 == 17 and sign == '*' and num2 == 34:
        return("17*34 = 578")
    if num1 == 17 and sign == '*' and num2 == 35:
        return("17*35 = 595")
    if num1 == 17 and sign == '*' and num2 == 36:
        return("17*36 = 612")
    if num1 == 17 and sign == '*' and num2 == 37:
        return("17*37 = 629")
    if num1 == 17 and sign == '*' and num2 == 38:
        return("17*38 = 646")
    if num1 == 17 and sign == '*' and num2 == 39:
        return("17*39 = 663")
    if num1 == 17 and sign == '*' and num2 == 40:
        return("17*40 = 680")
    if num1 == 17 and sign == '*' and num2 == 41:
        return("17*41 = 697")
    if num1 == 17 and sign == '*' and num2 == 42:
        return("17*42 = 714")
    if num1 == 17 and sign == '*' and num2 == 43:
        return("17*43 = 731")
    if num1 == 17 and sign == '*' and num2 == 44:
        return("17*44 = 748")
    if num1 == 17 and sign == '*' and num2 == 45:
        return("17*45 = 765")
    if num1 == 17 and sign == '*' and num2 == 46:
        return("17*46 = 782")
    if num1 == 17 and sign == '*' and num2 == 47:
        return("17*47 = 799")
    if num1 == 17 and sign == '*' and num2 == 48:
        return("17*48 = 816")
    if num1 == 17 and sign == '*' and num2 == 49:
        return("17*49 = 833")
    if num1 == 17 and sign == '*' and num2 == 50:
        return("17*50 = 850")
    if num1 == 18 and sign == '*' and num2 == 0:
        return("18*0 = 0")
    if num1 == 18 and sign == '*' and num2 == 1:
        return("18*1 = 18")
    if num1 == 18 and sign == '*' and num2 == 2:
        return("18*2 = 36")
    if num1 == 18 and sign == '*' and num2 == 3:
        return("18*3 = 54")
    if num1 == 18 and sign == '*' and num2 == 4:
        return("18*4 = 72")
    if num1 == 18 and sign == '*' and num2 == 5:
        return("18*5 = 90")
    if num1 == 18 and sign == '*' and num2 == 6:
        return("18*6 = 108")
    if num1 == 18 and sign == '*' and num2 == 7:
        return("18*7 = 126")
    if num1 == 18 and sign == '*' and num2 == 8:
        return("18*8 = 144")
    if num1 == 18 and sign == '*' and num2 == 9:
        return("18*9 = 162")
    if num1 == 18 and sign == '*' and num2 == 10:
        return("18*10 = 180")
    if num1 == 18 and sign == '*' and num2 == 11:
        return("18*11 = 198")
    if num1 == 18 and sign == '*' and num2 == 12:
        return("18*12 = 216")
    if num1 == 18 and sign == '*' and num2 == 13:
        return("18*13 = 234")
    if num1 == 18 and sign == '*' and num2 == 14:
        return("18*14 = 252")
    if num1 == 18 and sign == '*' and num2 == 15:
        return("18*15 = 270")
    if num1 == 18 and sign == '*' and num2 == 16:
        return("18*16 = 288")
    if num1 == 18 and sign == '*' and num2 == 17:
        return("18*17 = 306")
    if num1 == 18 and sign == '*' and num2 == 18:
        return("18*18 = 324")
    if num1 == 18 and sign == '*' and num2 == 19:
        return("18*19 = 342")
    if num1 == 18 and sign == '*' and num2 == 20:
        return("18*20 = 360")
    if num1 == 18 and sign == '*' and num2 == 21:
        return("18*21 = 378")
    if num1 == 18 and sign == '*' and num2 == 22:
        return("18*22 = 396")
    if num1 == 18 and sign == '*' and num2 == 23:
        return("18*23 = 414")
    if num1 == 18 and sign == '*' and num2 == 24:
        return("18*24 = 432")
    if num1 == 18 and sign == '*' and num2 == 25:
        return("18*25 = 450")
    if num1 == 18 and sign == '*' and num2 == 26:
        return("18*26 = 468")
    if num1 == 18 and sign == '*' and num2 == 27:
        return("18*27 = 486")
    if num1 == 18 and sign == '*' and num2 == 28:
        return("18*28 = 504")
    if num1 == 18 and sign == '*' and num2 == 29:
        return("18*29 = 522")
    if num1 == 18 and sign == '*' and num2 == 30:
        return("18*30 = 540")
    if num1 == 18 and sign == '*' and num2 == 31:
        return("18*31 = 558")
    if num1 == 18 and sign == '*' and num2 == 32:
        return("18*32 = 576")
    if num1 == 18 and sign == '*' and num2 == 33:
        return("18*33 = 594")
    if num1 == 18 and sign == '*' and num2 == 34:
        return("18*34 = 612")
    if num1 == 18 and sign == '*' and num2 == 35:
        return("18*35 = 630")
    if num1 == 18 and sign == '*' and num2 == 36:
        return("18*36 = 648")
    if num1 == 18 and sign == '*' and num2 == 37:
        return("18*37 = 666")
    if num1 == 18 and sign == '*' and num2 == 38:
        return("18*38 = 684")
    if num1 == 18 and sign == '*' and num2 == 39:
        return("18*39 = 702")
    if num1 == 18 and sign == '*' and num2 == 40:
        return("18*40 = 720")
    if num1 == 18 and sign == '*' and num2 == 41:
        return("18*41 = 738")
    if num1 == 18 and sign == '*' and num2 == 42:
        return("18*42 = 756")
    if num1 == 18 and sign == '*' and num2 == 43:
        return("18*43 = 774")
    if num1 == 18 and sign == '*' and num2 == 44:
        return("18*44 = 792")
    if num1 == 18 and sign == '*' and num2 == 45:
        return("18*45 = 810")
    if num1 == 18 and sign == '*' and num2 == 46:
        return("18*46 = 828")
    if num1 == 18 and sign == '*' and num2 == 47:
        return("18*47 = 846")
    if num1 == 18 and sign == '*' and num2 == 48:
        return("18*48 = 864")
    if num1 == 18 and sign == '*' and num2 == 49:
        return("18*49 = 882")
    if num1 == 18 and sign == '*' and num2 == 50:
        return("18*50 = 900")
    if num1 == 19 and sign == '*' and num2 == 0:
        return("19*0 = 0")
    if num1 == 19 and sign == '*' and num2 == 1:
        return("19*1 = 19")
    if num1 == 19 and sign == '*' and num2 == 2:
        return("19*2 = 38")
    if num1 == 19 and sign == '*' and num2 == 3:
        return("19*3 = 57")
    if num1 == 19 and sign == '*' and num2 == 4:
        return("19*4 = 76")
    if num1 == 19 and sign == '*' and num2 == 5:
        return("19*5 = 95")
    if num1 == 19 and sign == '*' and num2 == 6:
        return("19*6 = 114")
    if num1 == 19 and sign == '*' and num2 == 7:
        return("19*7 = 133")
    if num1 == 19 and sign == '*' and num2 == 8:
        return("19*8 = 152")
    if num1 == 19 and sign == '*' and num2 == 9:
        return("19*9 = 171")
    if num1 == 19 and sign == '*' and num2 == 10:
        return("19*10 = 190")
    if num1 == 19 and sign == '*' and num2 == 11:
        return("19*11 = 209")
    if num1 == 19 and sign == '*' and num2 == 12:
        return("19*12 = 228")
    if num1 == 19 and sign == '*' and num2 == 13:
        return("19*13 = 247")
    if num1 == 19 and sign == '*' and num2 == 14:
        return("19*14 = 266")
    if num1 == 19 and sign == '*' and num2 == 15:
        return("19*15 = 285")
    if num1 == 19 and sign == '*' and num2 == 16:
        return("19*16 = 304")
    if num1 == 19 and sign == '*' and num2 == 17:
        return("19*17 = 323")
    if num1 == 19 and sign == '*' and num2 == 18:
        return("19*18 = 342")
    if num1 == 19 and sign == '*' and num2 == 19:
        return("19*19 = 361")
    if num1 == 19 and sign == '*' and num2 == 20:
        return("19*20 = 380")
    if num1 == 19 and sign == '*' and num2 == 21:
        return("19*21 = 399")
    if num1 == 19 and sign == '*' and num2 == 22:
        return("19*22 = 418")
    if num1 == 19 and sign == '*' and num2 == 23:
        return("19*23 = 437")
    if num1 == 19 and sign == '*' and num2 == 24:
        return("19*24 = 456")
    if num1 == 19 and sign == '*' and num2 == 25:
        return("19*25 = 475")
    if num1 == 19 and sign == '*' and num2 == 26:
        return("19*26 = 494")
    if num1 == 19 and sign == '*' and num2 == 27:
        return("19*27 = 513")
    if num1 == 19 and sign == '*' and num2 == 28:
        return("19*28 = 532")
    if num1 == 19 and sign == '*' and num2 == 29:
        return("19*29 = 551")
    if num1 == 19 and sign == '*' and num2 == 30:
        return("19*30 = 570")
    if num1 == 19 and sign == '*' and num2 == 31:
        return("19*31 = 589")
    if num1 == 19 and sign == '*' and num2 == 32:
        return("19*32 = 608")
    if num1 == 19 and sign == '*' and num2 == 33:
        return("19*33 = 627")
    if num1 == 19 and sign == '*' and num2 == 34:
        return("19*34 = 646")
    if num1 == 19 and sign == '*' and num2 == 35:
        return("19*35 = 665")
    if num1 == 19 and sign == '*' and num2 == 36:
        return("19*36 = 684")
    if num1 == 19 and sign == '*' and num2 == 37:
        return("19*37 = 703")
    if num1 == 19 and sign == '*' and num2 == 38:
        return("19*38 = 722")
    if num1 == 19 and sign == '*' and num2 == 39:
        return("19*39 = 741")
    if num1 == 19 and sign == '*' and num2 == 40:
        return("19*40 = 760")
    if num1 == 19 and sign == '*' and num2 == 41:
        return("19*41 = 779")
    if num1 == 19 and sign == '*' and num2 == 42:
        return("19*42 = 798")
    if num1 == 19 and sign == '*' and num2 == 43:
        return("19*43 = 817")
    if num1 == 19 and sign == '*' and num2 == 44:
        return("19*44 = 836")
    if num1 == 19 and sign == '*' and num2 == 45:
        return("19*45 = 855")
    if num1 == 19 and sign == '*' and num2 == 46:
        return("19*46 = 874")
    if num1 == 19 and sign == '*' and num2 == 47:
        return("19*47 = 893")
    if num1 == 19 and sign == '*' and num2 == 48:
        return("19*48 = 912")
    if num1 == 19 and sign == '*' and num2 == 49:
        return("19*49 = 931")
    if num1 == 19 and sign == '*' and num2 == 50:
        return("19*50 = 950")
    if num1 == 20 and sign == '*' and num2 == 0:
        return("20*0 = 0")
    if num1 == 20 and sign == '*' and num2 == 1:
        return("20*1 = 20")
    if num1 == 20 and sign == '*' and num2 == 2:
        return("20*2 = 40")
    if num1 == 20 and sign == '*' and num2 == 3:
        return("20*3 = 60")
    if num1 == 20 and sign == '*' and num2 == 4:
        return("20*4 = 80")
    if num1 == 20 and sign == '*' and num2 == 5:
        return("20*5 = 100")
    if num1 == 20 and sign == '*' and num2 == 6:
        return("20*6 = 120")
    if num1 == 20 and sign == '*' and num2 == 7:
        return("20*7 = 140")
    if num1 == 20 and sign == '*' and num2 == 8:
        return("20*8 = 160")
    if num1 == 20 and sign == '*' and num2 == 9:
        return("20*9 = 180")
    if num1 == 20 and sign == '*' and num2 == 10:
        return("20*10 = 200")
    if num1 == 20 and sign == '*' and num2 == 11:
        return("20*11 = 220")
    if num1 == 20 and sign == '*' and num2 == 12:
        return("20*12 = 240")
    if num1 == 20 and sign == '*' and num2 == 13:
        return("20*13 = 260")
    if num1 == 20 and sign == '*' and num2 == 14:
        return("20*14 = 280")
    if num1 == 20 and sign == '*' and num2 == 15:
        return("20*15 = 300")
    if num1 == 20 and sign == '*' and num2 == 16:
        return("20*16 = 320")
    if num1 == 20 and sign == '*' and num2 == 17:
        return("20*17 = 340")
    if num1 == 20 and sign == '*' and num2 == 18:
        return("20*18 = 360")
    if num1 == 20 and sign == '*' and num2 == 19:
        return("20*19 = 380")
    if num1 == 20 and sign == '*' and num2 == 20:
        return("20*20 = 400")
    if num1 == 20 and sign == '*' and num2 == 21:
        return("20*21 = 420")
    if num1 == 20 and sign == '*' and num2 == 22:
        return("20*22 = 440")
    if num1 == 20 and sign == '*' and num2 == 23:
        return("20*23 = 460")
    if num1 == 20 and sign == '*' and num2 == 24:
        return("20*24 = 480")
    if num1 == 20 and sign == '*' and num2 == 25:
        return("20*25 = 500")
    if num1 == 20 and sign == '*' and num2 == 26:
        return("20*26 = 520")
    if num1 == 20 and sign == '*' and num2 == 27:
        return("20*27 = 540")
    if num1 == 20 and sign == '*' and num2 == 28:
        return("20*28 = 560")
    if num1 == 20 and sign == '*' and num2 == 29:
        return("20*29 = 580")
    if num1 == 20 and sign == '*' and num2 == 30:
        return("20*30 = 600")
    if num1 == 20 and sign == '*' and num2 == 31:
        return("20*31 = 620")
    if num1 == 20 and sign == '*' and num2 == 32:
        return("20*32 = 640")
    if num1 == 20 and sign == '*' and num2 == 33:
        return("20*33 = 660")
    if num1 == 20 and sign == '*' and num2 == 34:
        return("20*34 = 680")
    if num1 == 20 and sign == '*' and num2 == 35:
        return("20*35 = 700")
    if num1 == 20 and sign == '*' and num2 == 36:
        return("20*36 = 720")
    if num1 == 20 and sign == '*' and num2 == 37:
        return("20*37 = 740")
    if num1 == 20 and sign == '*' and num2 == 38:
        return("20*38 = 760")
    if num1 == 20 and sign == '*' and num2 == 39:
        return("20*39 = 780")
    if num1 == 20 and sign == '*' and num2 == 40:
        return("20*40 = 800")
    if num1 == 20 and sign == '*' and num2 == 41:
        return("20*41 = 820")
    if num1 == 20 and sign == '*' and num2 == 42:
        return("20*42 = 840")
    if num1 == 20 and sign == '*' and num2 == 43:
        return("20*43 = 860")
    if num1 == 20 and sign == '*' and num2 == 44:
        return("20*44 = 880")
    if num1 == 20 and sign == '*' and num2 == 45:
        return("20*45 = 900")
    if num1 == 20 and sign == '*' and num2 == 46:
        return("20*46 = 920")
    if num1 == 20 and sign == '*' and num2 == 47:
        return("20*47 = 940")
    if num1 == 20 and sign == '*' and num2 == 48:
        return("20*48 = 960")
    if num1 == 20 and sign == '*' and num2 == 49:
        return("20*49 = 980")
    if num1 == 20 and sign == '*' and num2 == 50:
        return("20*50 = 1000")
    if num1 == 21 and sign == '*' and num2 == 0:
        return("21*0 = 0")
    if num1 == 21 and sign == '*' and num2 == 1:
        return("21*1 = 21")
    if num1 == 21 and sign == '*' and num2 == 2:
        return("21*2 = 42")
    if num1 == 21 and sign == '*' and num2 == 3:
        return("21*3 = 63")
    if num1 == 21 and sign == '*' and num2 == 4:
        return("21*4 = 84")
    if num1 == 21 and sign == '*' and num2 == 5:
        return("21*5 = 105")
    if num1 == 21 and sign == '*' and num2 == 6:
        return("21*6 = 126")
    if num1 == 21 and sign == '*' and num2 == 7:
        return("21*7 = 147")
    if num1 == 21 and sign == '*' and num2 == 8:
        return("21*8 = 168")
    if num1 == 21 and sign == '*' and num2 == 9:
        return("21*9 = 189")
    if num1 == 21 and sign == '*' and num2 == 10:
        return("21*10 = 210")
    if num1 == 21 and sign == '*' and num2 == 11:
        return("21*11 = 231")
    if num1 == 21 and sign == '*' and num2 == 12:
        return("21*12 = 252")
    if num1 == 21 and sign == '*' and num2 == 13:
        return("21*13 = 273")
    if num1 == 21 and sign == '*' and num2 == 14:
        return("21*14 = 294")
    if num1 == 21 and sign == '*' and num2 == 15:
        return("21*15 = 315")
    if num1 == 21 and sign == '*' and num2 == 16:
        return("21*16 = 336")
    if num1 == 21 and sign == '*' and num2 == 17:
        return("21*17 = 357")
    if num1 == 21 and sign == '*' and num2 == 18:
        return("21*18 = 378")
    if num1 == 21 and sign == '*' and num2 == 19:
        return("21*19 = 399")
    if num1 == 21 and sign == '*' and num2 == 20:
        return("21*20 = 420")
    if num1 == 21 and sign == '*' and num2 == 21:
        return("21*21 = 441")
    if num1 == 21 and sign == '*' and num2 == 22:
        return("21*22 = 462")
    if num1 == 21 and sign == '*' and num2 == 23:
        return("21*23 = 483")
    if num1 == 21 and sign == '*' and num2 == 24:
        return("21*24 = 504")
    if num1 == 21 and sign == '*' and num2 == 25:
        return("21*25 = 525")
    if num1 == 21 and sign == '*' and num2 == 26:
        return("21*26 = 546")
    if num1 == 21 and sign == '*' and num2 == 27:
        return("21*27 = 567")
    if num1 == 21 and sign == '*' and num2 == 28:
        return("21*28 = 588")
    if num1 == 21 and sign == '*' and num2 == 29:
        return("21*29 = 609")
    if num1 == 21 and sign == '*' and num2 == 30:
        return("21*30 = 630")
    if num1 == 21 and sign == '*' and num2 == 31:
        return("21*31 = 651")
    if num1 == 21 and sign == '*' and num2 == 32:
        return("21*32 = 672")
    if num1 == 21 and sign == '*' and num2 == 33:
        return("21*33 = 693")
    if num1 == 21 and sign == '*' and num2 == 34:
        return("21*34 = 714")
    if num1 == 21 and sign == '*' and num2 == 35:
        return("21*35 = 735")
    if num1 == 21 and sign == '*' and num2 == 36:
        return("21*36 = 756")
    if num1 == 21 and sign == '*' and num2 == 37:
        return("21*37 = 777")
    if num1 == 21 and sign == '*' and num2 == 38:
        return("21*38 = 798")
    if num1 == 21 and sign == '*' and num2 == 39:
        return("21*39 = 819")
    if num1 == 21 and sign == '*' and num2 == 40:
        return("21*40 = 840")
    if num1 == 21 and sign == '*' and num2 == 41:
        return("21*41 = 861")
    if num1 == 21 and sign == '*' and num2 == 42:
        return("21*42 = 882")
    if num1 == 21 and sign == '*' and num2 == 43:
        return("21*43 = 903")
    if num1 == 21 and sign == '*' and num2 == 44:
        return("21*44 = 924")
    if num1 == 21 and sign == '*' and num2 == 45:
        return("21*45 = 945")
    if num1 == 21 and sign == '*' and num2 == 46:
        return("21*46 = 966")
    if num1 == 21 and sign == '*' and num2 == 47:
        return("21*47 = 987")
    if num1 == 21 and sign == '*' and num2 == 48:
        return("21*48 = 1008")
    if num1 == 21 and sign == '*' and num2 == 49:
        return("21*49 = 1029")
    if num1 == 21 and sign == '*' and num2 == 50:
        return("21*50 = 1050")
    if num1 == 22 and sign == '*' and num2 == 0:
        return("22*0 = 0")
    if num1 == 22 and sign == '*' and num2 == 1:
        return("22*1 = 22")
    if num1 == 22 and sign == '*' and num2 == 2:
        return("22*2 = 44")
    if num1 == 22 and sign == '*' and num2 == 3:
        return("22*3 = 66")
    if num1 == 22 and sign == '*' and num2 == 4:
        return("22*4 = 88")
    if num1 == 22 and sign == '*' and num2 == 5:
        return("22*5 = 110")
    if num1 == 22 and sign == '*' and num2 == 6:
        return("22*6 = 132")
    if num1 == 22 and sign == '*' and num2 == 7:
        return("22*7 = 154")
    if num1 == 22 and sign == '*' and num2 == 8:
        return("22*8 = 176")
    if num1 == 22 and sign == '*' and num2 == 9:
        return("22*9 = 198")
    if num1 == 22 and sign == '*' and num2 == 10:
        return("22*10 = 220")
    if num1 == 22 and sign == '*' and num2 == 11:
        return("22*11 = 242")
    if num1 == 22 and sign == '*' and num2 == 12:
        return("22*12 = 264")
    if num1 == 22 and sign == '*' and num2 == 13:
        return("22*13 = 286")
    if num1 == 22 and sign == '*' and num2 == 14:
        return("22*14 = 308")
    if num1 == 22 and sign == '*' and num2 == 15:
        return("22*15 = 330")
    if num1 == 22 and sign == '*' and num2 == 16:
        return("22*16 = 352")
    if num1 == 22 and sign == '*' and num2 == 17:
        return("22*17 = 374")
    if num1 == 22 and sign == '*' and num2 == 18:
        return("22*18 = 396")
    if num1 == 22 and sign == '*' and num2 == 19:
        return("22*19 = 418")
    if num1 == 22 and sign == '*' and num2 == 20:
        return("22*20 = 440")
    if num1 == 22 and sign == '*' and num2 == 21:
        return("22*21 = 462")
    if num1 == 22 and sign == '*' and num2 == 22:
        return("22*22 = 484")
    if num1 == 22 and sign == '*' and num2 == 23:
        return("22*23 = 506")
    if num1 == 22 and sign == '*' and num2 == 24:
        return("22*24 = 528")
    if num1 == 22 and sign == '*' and num2 == 25:
        return("22*25 = 550")
    if num1 == 22 and sign == '*' and num2 == 26:
        return("22*26 = 572")
    if num1 == 22 and sign == '*' and num2 == 27:
        return("22*27 = 594")
    if num1 == 22 and sign == '*' and num2 == 28:
        return("22*28 = 616")
    if num1 == 22 and sign == '*' and num2 == 29:
        return("22*29 = 638")
    if num1 == 22 and sign == '*' and num2 == 30:
        return("22*30 = 660")
    if num1 == 22 and sign == '*' and num2 == 31:
        return("22*31 = 682")
    if num1 == 22 and sign == '*' and num2 == 32:
        return("22*32 = 704")
    if num1 == 22 and sign == '*' and num2 == 33:
        return("22*33 = 726")
    if num1 == 22 and sign == '*' and num2 == 34:
        return("22*34 = 748")
    if num1 == 22 and sign == '*' and num2 == 35:
        return("22*35 = 770")
    if num1 == 22 and sign == '*' and num2 == 36:
        return("22*36 = 792")
    if num1 == 22 and sign == '*' and num2 == 37:
        return("22*37 = 814")
    if num1 == 22 and sign == '*' and num2 == 38:
        return("22*38 = 836")
    if num1 == 22 and sign == '*' and num2 == 39:
        return("22*39 = 858")
    if num1 == 22 and sign == '*' and num2 == 40:
        return("22*40 = 880")
    if num1 == 22 and sign == '*' and num2 == 41:
        return("22*41 = 902")
    if num1 == 22 and sign == '*' and num2 == 42:
        return("22*42 = 924")
    if num1 == 22 and sign == '*' and num2 == 43:
        return("22*43 = 946")
    if num1 == 22 and sign == '*' and num2 == 44:
        return("22*44 = 968")
    if num1 == 22 and sign == '*' and num2 == 45:
        return("22*45 = 990")
    if num1 == 22 and sign == '*' and num2 == 46:
        return("22*46 = 1012")
    if num1 == 22 and sign == '*' and num2 == 47:
        return("22*47 = 1034")
    if num1 == 22 and sign == '*' and num2 == 48:
        return("22*48 = 1056")
    if num1 == 22 and sign == '*' and num2 == 49:
        return("22*49 = 1078")
    if num1 == 22 and sign == '*' and num2 == 50:
        return("22*50 = 1100")
    if num1 == 23 and sign == '*' and num2 == 0:
        return("23*0 = 0")
    if num1 == 23 and sign == '*' and num2 == 1:
        return("23*1 = 23")
    if num1 == 23 and sign == '*' and num2 == 2:
        return("23*2 = 46")
    if num1 == 23 and sign == '*' and num2 == 3:
        return("23*3 = 69")
    if num1 == 23 and sign == '*' and num2 == 4:
        return("23*4 = 92")
    if num1 == 23 and sign == '*' and num2 == 5:
        return("23*5 = 115")
    if num1 == 23 and sign == '*' and num2 == 6:
        return("23*6 = 138")
    if num1 == 23 and sign == '*' and num2 == 7:
        return("23*7 = 161")
    if num1 == 23 and sign == '*' and num2 == 8:
        return("23*8 = 184")
    if num1 == 23 and sign == '*' and num2 == 9:
        return("23*9 = 207")
    if num1 == 23 and sign == '*' and num2 == 10:
        return("23*10 = 230")
    if num1 == 23 and sign == '*' and num2 == 11:
        return("23*11 = 253")
    if num1 == 23 and sign == '*' and num2 == 12:
        return("23*12 = 276")
    if num1 == 23 and sign == '*' and num2 == 13:
        return("23*13 = 299")
    if num1 == 23 and sign == '*' and num2 == 14:
        return("23*14 = 322")
    if num1 == 23 and sign == '*' and num2 == 15:
        return("23*15 = 345")
    if num1 == 23 and sign == '*' and num2 == 16:
        return("23*16 = 368")
    if num1 == 23 and sign == '*' and num2 == 17:
        return("23*17 = 391")
    if num1 == 23 and sign == '*' and num2 == 18:
        return("23*18 = 414")
    if num1 == 23 and sign == '*' and num2 == 19:
        return("23*19 = 437")
    if num1 == 23 and sign == '*' and num2 == 20:
        return("23*20 = 460")
    if num1 == 23 and sign == '*' and num2 == 21:
        return("23*21 = 483")
    if num1 == 23 and sign == '*' and num2 == 22:
        return("23*22 = 506")
    if num1 == 23 and sign == '*' and num2 == 23:
        return("23*23 = 529")
    if num1 == 23 and sign == '*' and num2 == 24:
        return("23*24 = 552")
    if num1 == 23 and sign == '*' and num2 == 25:
        return("23*25 = 575")
    if num1 == 23 and sign == '*' and num2 == 26:
        return("23*26 = 598")
    if num1 == 23 and sign == '*' and num2 == 27:
        return("23*27 = 621")
    if num1 == 23 and sign == '*' and num2 == 28:
        return("23*28 = 644")
    if num1 == 23 and sign == '*' and num2 == 29:
        return("23*29 = 667")
    if num1 == 23 and sign == '*' and num2 == 30:
        return("23*30 = 690")
    if num1 == 23 and sign == '*' and num2 == 31:
        return("23*31 = 713")
    if num1 == 23 and sign == '*' and num2 == 32:
        return("23*32 = 736")
    if num1 == 23 and sign == '*' and num2 == 33:
        return("23*33 = 759")
    if num1 == 23 and sign == '*' and num2 == 34:
        return("23*34 = 782")
    if num1 == 23 and sign == '*' and num2 == 35:
        return("23*35 = 805")
    if num1 == 23 and sign == '*' and num2 == 36:
        return("23*36 = 828")
    if num1 == 23 and sign == '*' and num2 == 37:
        return("23*37 = 851")
    if num1 == 23 and sign == '*' and num2 == 38:
        return("23*38 = 874")
    if num1 == 23 and sign == '*' and num2 == 39:
        return("23*39 = 897")
    if num1 == 23 and sign == '*' and num2 == 40:
        return("23*40 = 920")
    if num1 == 23 and sign == '*' and num2 == 41:
        return("23*41 = 943")
    if num1 == 23 and sign == '*' and num2 == 42:
        return("23*42 = 966")
    if num1 == 23 and sign == '*' and num2 == 43:
        return("23*43 = 989")
    if num1 == 23 and sign == '*' and num2 == 44:
        return("23*44 = 1012")
    if num1 == 23 and sign == '*' and num2 == 45:
        return("23*45 = 1035")
    if num1 == 23 and sign == '*' and num2 == 46:
        return("23*46 = 1058")
    if num1 == 23 and sign == '*' and num2 == 47:
        return("23*47 = 1081")
    if num1 == 23 and sign == '*' and num2 == 48:
        return("23*48 = 1104")
    if num1 == 23 and sign == '*' and num2 == 49:
        return("23*49 = 1127")
    if num1 == 23 and sign == '*' and num2 == 50:
        return("23*50 = 1150")
    if num1 == 24 and sign == '*' and num2 == 0:
        return("24*0 = 0")
    if num1 == 24 and sign == '*' and num2 == 1:
        return("24*1 = 24")
    if num1 == 24 and sign == '*' and num2 == 2:
        return("24*2 = 48")
    if num1 == 24 and sign == '*' and num2 == 3:
        return("24*3 = 72")
    if num1 == 24 and sign == '*' and num2 == 4:
        return("24*4 = 96")
    if num1 == 24 and sign == '*' and num2 == 5:
        return("24*5 = 120")
    if num1 == 24 and sign == '*' and num2 == 6:
        return("24*6 = 144")
    if num1 == 24 and sign == '*' and num2 == 7:
        return("24*7 = 168")
    if num1 == 24 and sign == '*' and num2 == 8:
        return("24*8 = 192")
    if num1 == 24 and sign == '*' and num2 == 9:
        return("24*9 = 216")
    if num1 == 24 and sign == '*' and num2 == 10:
        return("24*10 = 240")
    if num1 == 24 and sign == '*' and num2 == 11:
        return("24*11 = 264")
    if num1 == 24 and sign == '*' and num2 == 12:
        return("24*12 = 288")
    if num1 == 24 and sign == '*' and num2 == 13:
        return("24*13 = 312")
    if num1 == 24 and sign == '*' and num2 == 14:
        return("24*14 = 336")
    if num1 == 24 and sign == '*' and num2 == 15:
        return("24*15 = 360")
    if num1 == 24 and sign == '*' and num2 == 16:
        return("24*16 = 384")
    if num1 == 24 and sign == '*' and num2 == 17:
        return("24*17 = 408")
    if num1 == 24 and sign == '*' and num2 == 18:
        return("24*18 = 432")
    if num1 == 24 and sign == '*' and num2 == 19:
        return("24*19 = 456")
    if num1 == 24 and sign == '*' and num2 == 20:
        return("24*20 = 480")
    if num1 == 24 and sign == '*' and num2 == 21:
        return("24*21 = 504")
    if num1 == 24 and sign == '*' and num2 == 22:
        return("24*22 = 528")
    if num1 == 24 and sign == '*' and num2 == 23:
        return("24*23 = 552")
    if num1 == 24 and sign == '*' and num2 == 24:
        return("24*24 = 576")
    if num1 == 24 and sign == '*' and num2 == 25:
        return("24*25 = 600")
    if num1 == 24 and sign == '*' and num2 == 26:
        return("24*26 = 624")
    if num1 == 24 and sign == '*' and num2 == 27:
        return("24*27 = 648")
    if num1 == 24 and sign == '*' and num2 == 28:
        return("24*28 = 672")
    if num1 == 24 and sign == '*' and num2 == 29:
        return("24*29 = 696")
    if num1 == 24 and sign == '*' and num2 == 30:
        return("24*30 = 720")
    if num1 == 24 and sign == '*' and num2 == 31:
        return("24*31 = 744")
    if num1 == 24 and sign == '*' and num2 == 32:
        return("24*32 = 768")
    if num1 == 24 and sign == '*' and num2 == 33:
        return("24*33 = 792")
    if num1 == 24 and sign == '*' and num2 == 34:
        return("24*34 = 816")
    if num1 == 24 and sign == '*' and num2 == 35:
        return("24*35 = 840")
    if num1 == 24 and sign == '*' and num2 == 36:
        return("24*36 = 864")
    if num1 == 24 and sign == '*' and num2 == 37:
        return("24*37 = 888")
    if num1 == 24 and sign == '*' and num2 == 38:
        return("24*38 = 912")
    if num1 == 24 and sign == '*' and num2 == 39:
        return("24*39 = 936")
    if num1 == 24 and sign == '*' and num2 == 40:
        return("24*40 = 960")
    if num1 == 24 and sign == '*' and num2 == 41:
        return("24*41 = 984")
    if num1 == 24 and sign == '*' and num2 == 42:
        return("24*42 = 1008")
    if num1 == 24 and sign == '*' and num2 == 43:
        return("24*43 = 1032")
    if num1 == 24 and sign == '*' and num2 == 44:
        return("24*44 = 1056")
    if num1 == 24 and sign == '*' and num2 == 45:
        return("24*45 = 1080")
    if num1 == 24 and sign == '*' and num2 == 46:
        return("24*46 = 1104")
    if num1 == 24 and sign == '*' and num2 == 47:
        return("24*47 = 1128")
    if num1 == 24 and sign == '*' and num2 == 48:
        return("24*48 = 1152")
    if num1 == 24 and sign == '*' and num2 == 49:
        return("24*49 = 1176")
    if num1 == 24 and sign == '*' and num2 == 50:
        return("24*50 = 1200")
    if num1 == 25 and sign == '*' and num2 == 0:
        return("25*0 = 0")
    if num1 == 25 and sign == '*' and num2 == 1:
        return("25*1 = 25")
    if num1 == 25 and sign == '*' and num2 == 2:
        return("25*2 = 50")
    if num1 == 25 and sign == '*' and num2 == 3:
        return("25*3 = 75")
    if num1 == 25 and sign == '*' and num2 == 4:
        return("25*4 = 100")
    if num1 == 25 and sign == '*' and num2 == 5:
        return("25*5 = 125")
    if num1 == 25 and sign == '*' and num2 == 6:
        return("25*6 = 150")
    if num1 == 25 and sign == '*' and num2 == 7:
        return("25*7 = 175")
    if num1 == 25 and sign == '*' and num2 == 8:
        return("25*8 = 200")
    if num1 == 25 and sign == '*' and num2 == 9:
        return("25*9 = 225")
    if num1 == 25 and sign == '*' and num2 == 10:
        return("25*10 = 250")
    if num1 == 25 and sign == '*' and num2 == 11:
        return("25*11 = 275")
    if num1 == 25 and sign == '*' and num2 == 12:
        return("25*12 = 300")
    if num1 == 25 and sign == '*' and num2 == 13:
        return("25*13 = 325")
    if num1 == 25 and sign == '*' and num2 == 14:
        return("25*14 = 350")
    if num1 == 25 and sign == '*' and num2 == 15:
        return("25*15 = 375")
    if num1 == 25 and sign == '*' and num2 == 16:
        return("25*16 = 400")
    if num1 == 25 and sign == '*' and num2 == 17:
        return("25*17 = 425")
    if num1 == 25 and sign == '*' and num2 == 18:
        return("25*18 = 450")
    if num1 == 25 and sign == '*' and num2 == 19:
        return("25*19 = 475")
    if num1 == 25 and sign == '*' and num2 == 20:
        return("25*20 = 500")
    if num1 == 25 and sign == '*' and num2 == 21:
        return("25*21 = 525")
    if num1 == 25 and sign == '*' and num2 == 22:
        return("25*22 = 550")
    if num1 == 25 and sign == '*' and num2 == 23:
        return("25*23 = 575")
    if num1 == 25 and sign == '*' and num2 == 24:
        return("25*24 = 600")
    if num1 == 25 and sign == '*' and num2 == 25:
        return("25*25 = 625")
    if num1 == 25 and sign == '*' and num2 == 26:
        return("25*26 = 650")
    if num1 == 25 and sign == '*' and num2 == 27:
        return("25*27 = 675")
    if num1 == 25 and sign == '*' and num2 == 28:
        return("25*28 = 700")
    if num1 == 25 and sign == '*' and num2 == 29:
        return("25*29 = 725")
    if num1 == 25 and sign == '*' and num2 == 30:
        return("25*30 = 750")
    if num1 == 25 and sign == '*' and num2 == 31:
        return("25*31 = 775")
    if num1 == 25 and sign == '*' and num2 == 32:
        return("25*32 = 800")
    if num1 == 25 and sign == '*' and num2 == 33:
        return("25*33 = 825")
    if num1 == 25 and sign == '*' and num2 == 34:
        return("25*34 = 850")
    if num1 == 25 and sign == '*' and num2 == 35:
        return("25*35 = 875")
    if num1 == 25 and sign == '*' and num2 == 36:
        return("25*36 = 900")
    if num1 == 25 and sign == '*' and num2 == 37:
        return("25*37 = 925")
    if num1 == 25 and sign == '*' and num2 == 38:
        return("25*38 = 950")
    if num1 == 25 and sign == '*' and num2 == 39:
        return("25*39 = 975")
    if num1 == 25 and sign == '*' and num2 == 40:
        return("25*40 = 1000")
    if num1 == 25 and sign == '*' and num2 == 41:
        return("25*41 = 1025")
    if num1 == 25 and sign == '*' and num2 == 42:
        return("25*42 = 1050")
    if num1 == 25 and sign == '*' and num2 == 43:
        return("25*43 = 1075")
    if num1 == 25 and sign == '*' and num2 == 44:
        return("25*44 = 1100")
    if num1 == 25 and sign == '*' and num2 == 45:
        return("25*45 = 1125")
    if num1 == 25 and sign == '*' and num2 == 46:
        return("25*46 = 1150")
    if num1 == 25 and sign == '*' and num2 == 47:
        return("25*47 = 1175")
    if num1 == 25 and sign == '*' and num2 == 48:
        return("25*48 = 1200")
    if num1 == 25 and sign == '*' and num2 == 49:
        return("25*49 = 1225")
    if num1 == 25 and sign == '*' and num2 == 50:
        return("25*50 = 1250")
    if num1 == 26 and sign == '*' and num2 == 0:
        return("26*0 = 0")
    if num1 == 26 and sign == '*' and num2 == 1:
        return("26*1 = 26")
    if num1 == 26 and sign == '*' and num2 == 2:
        return("26*2 = 52")
    if num1 == 26 and sign == '*' and num2 == 3:
        return("26*3 = 78")
    if num1 == 26 and sign == '*' and num2 == 4:
        return("26*4 = 104")
    if num1 == 26 and sign == '*' and num2 == 5:
        return("26*5 = 130")
    if num1 == 26 and sign == '*' and num2 == 6:
        return("26*6 = 156")
    if num1 == 26 and sign == '*' and num2 == 7:
        return("26*7 = 182")
    if num1 == 26 and sign == '*' and num2 == 8:
        return("26*8 = 208")
    if num1 == 26 and sign == '*' and num2 == 9:
        return("26*9 = 234")
    if num1 == 26 and sign == '*' and num2 == 10:
        return("26*10 = 260")
    if num1 == 26 and sign == '*' and num2 == 11:
        return("26*11 = 286")
    if num1 == 26 and sign == '*' and num2 == 12:
        return("26*12 = 312")
    if num1 == 26 and sign == '*' and num2 == 13:
        return("26*13 = 338")
    if num1 == 26 and sign == '*' and num2 == 14:
        return("26*14 = 364")
    if num1 == 26 and sign == '*' and num2 == 15:
        return("26*15 = 390")
    if num1 == 26 and sign == '*' and num2 == 16:
        return("26*16 = 416")
    if num1 == 26 and sign == '*' and num2 == 17:
        return("26*17 = 442")
    if num1 == 26 and sign == '*' and num2 == 18:
        return("26*18 = 468")
    if num1 == 26 and sign == '*' and num2 == 19:
        return("26*19 = 494")
    if num1 == 26 and sign == '*' and num2 == 20:
        return("26*20 = 520")
    if num1 == 26 and sign == '*' and num2 == 21:
        return("26*21 = 546")
    if num1 == 26 and sign == '*' and num2 == 22:
        return("26*22 = 572")
    if num1 == 26 and sign == '*' and num2 == 23:
        return("26*23 = 598")
    if num1 == 26 and sign == '*' and num2 == 24:
        return("26*24 = 624")
    if num1 == 26 and sign == '*' and num2 == 25:
        return("26*25 = 650")
    if num1 == 26 and sign == '*' and num2 == 26:
        return("26*26 = 676")
    if num1 == 26 and sign == '*' and num2 == 27:
        return("26*27 = 702")
    if num1 == 26 and sign == '*' and num2 == 28:
        return("26*28 = 728")
    if num1 == 26 and sign == '*' and num2 == 29:
        return("26*29 = 754")
    if num1 == 26 and sign == '*' and num2 == 30:
        return("26*30 = 780")
    if num1 == 26 and sign == '*' and num2 == 31:
        return("26*31 = 806")
    if num1 == 26 and sign == '*' and num2 == 32:
        return("26*32 = 832")
    if num1 == 26 and sign == '*' and num2 == 33:
        return("26*33 = 858")
    if num1 == 26 and sign == '*' and num2 == 34:
        return("26*34 = 884")
    if num1 == 26 and sign == '*' and num2 == 35:
        return("26*35 = 910")
    if num1 == 26 and sign == '*' and num2 == 36:
        return("26*36 = 936")
    if num1 == 26 and sign == '*' and num2 == 37:
        return("26*37 = 962")
    if num1 == 26 and sign == '*' and num2 == 38:
        return("26*38 = 988")
    if num1 == 26 and sign == '*' and num2 == 39:
        return("26*39 = 1014")
    if num1 == 26 and sign == '*' and num2 == 40:
        return("26*40 = 1040")
    if num1 == 26 and sign == '*' and num2 == 41:
        return("26*41 = 1066")
    if num1 == 26 and sign == '*' and num2 == 42:
        return("26*42 = 1092")
    if num1 == 26 and sign == '*' and num2 == 43:
        return("26*43 = 1118")
    if num1 == 26 and sign == '*' and num2 == 44:
        return("26*44 = 1144")
    if num1 == 26 and sign == '*' and num2 == 45:
        return("26*45 = 1170")
    if num1 == 26 and sign == '*' and num2 == 46:
        return("26*46 = 1196")
    if num1 == 26 and sign == '*' and num2 == 47:
        return("26*47 = 1222")
    if num1 == 26 and sign == '*' and num2 == 48:
        return("26*48 = 1248")
    if num1 == 26 and sign == '*' and num2 == 49:
        return("26*49 = 1274")
    if num1 == 26 and sign == '*' and num2 == 50:
        return("26*50 = 1300")
    if num1 == 27 and sign == '*' and num2 == 0:
        return("27*0 = 0")
    if num1 == 27 and sign == '*' and num2 == 1:
        return("27*1 = 27")
    if num1 == 27 and sign == '*' and num2 == 2:
        return("27*2 = 54")
    if num1 == 27 and sign == '*' and num2 == 3:
        return("27*3 = 81")
    if num1 == 27 and sign == '*' and num2 == 4:
        return("27*4 = 108")
    if num1 == 27 and sign == '*' and num2 == 5:
        return("27*5 = 135")
    if num1 == 27 and sign == '*' and num2 == 6:
        return("27*6 = 162")
    if num1 == 27 and sign == '*' and num2 == 7:
        return("27*7 = 189")
    if num1 == 27 and sign == '*' and num2 == 8:
        return("27*8 = 216")
    if num1 == 27 and sign == '*' and num2 == 9:
        return("27*9 = 243")
    if num1 == 27 and sign == '*' and num2 == 10:
        return("27*10 = 270")
    if num1 == 27 and sign == '*' and num2 == 11:
        return("27*11 = 297")
    if num1 == 27 and sign == '*' and num2 == 12:
        return("27*12 = 324")
    if num1 == 27 and sign == '*' and num2 == 13:
        return("27*13 = 351")
    if num1 == 27 and sign == '*' and num2 == 14:
        return("27*14 = 378")
    if num1 == 27 and sign == '*' and num2 == 15:
        return("27*15 = 405")
    if num1 == 27 and sign == '*' and num2 == 16:
        return("27*16 = 432")
    if num1 == 27 and sign == '*' and num2 == 17:
        return("27*17 = 459")
    if num1 == 27 and sign == '*' and num2 == 18:
        return("27*18 = 486")
    if num1 == 27 and sign == '*' and num2 == 19:
        return("27*19 = 513")
    if num1 == 27 and sign == '*' and num2 == 20:
        return("27*20 = 540")
    if num1 == 27 and sign == '*' and num2 == 21:
        return("27*21 = 567")
    if num1 == 27 and sign == '*' and num2 == 22:
        return("27*22 = 594")
    if num1 == 27 and sign == '*' and num2 == 23:
        return("27*23 = 621")
    if num1 == 27 and sign == '*' and num2 == 24:
        return("27*24 = 648")
    if num1 == 27 and sign == '*' and num2 == 25:
        return("27*25 = 675")
    if num1 == 27 and sign == '*' and num2 == 26:
        return("27*26 = 702")
    if num1 == 27 and sign == '*' and num2 == 27:
        return("27*27 = 729")
    if num1 == 27 and sign == '*' and num2 == 28:
        return("27*28 = 756")
    if num1 == 27 and sign == '*' and num2 == 29:
        return("27*29 = 783")
    if num1 == 27 and sign == '*' and num2 == 30:
        return("27*30 = 810")
    if num1 == 27 and sign == '*' and num2 == 31:
        return("27*31 = 837")
    if num1 == 27 and sign == '*' and num2 == 32:
        return("27*32 = 864")
    if num1 == 27 and sign == '*' and num2 == 33:
        return("27*33 = 891")
    if num1 == 27 and sign == '*' and num2 == 34:
        return("27*34 = 918")
    if num1 == 27 and sign == '*' and num2 == 35:
        return("27*35 = 945")
    if num1 == 27 and sign == '*' and num2 == 36:
        return("27*36 = 972")
    if num1 == 27 and sign == '*' and num2 == 37:
        return("27*37 = 999")
    if num1 == 27 and sign == '*' and num2 == 38:
        return("27*38 = 1026")
    if num1 == 27 and sign == '*' and num2 == 39:
        return("27*39 = 1053")
    if num1 == 27 and sign == '*' and num2 == 40:
        return("27*40 = 1080")
    if num1 == 27 and sign == '*' and num2 == 41:
        return("27*41 = 1107")
    if num1 == 27 and sign == '*' and num2 == 42:
        return("27*42 = 1134")
    if num1 == 27 and sign == '*' and num2 == 43:
        return("27*43 = 1161")
    if num1 == 27 and sign == '*' and num2 == 44:
        return("27*44 = 1188")
    if num1 == 27 and sign == '*' and num2 == 45:
        return("27*45 = 1215")
    if num1 == 27 and sign == '*' and num2 == 46:
        return("27*46 = 1242")
    if num1 == 27 and sign == '*' and num2 == 47:
        return("27*47 = 1269")
    if num1 == 27 and sign == '*' and num2 == 48:
        return("27*48 = 1296")
    if num1 == 27 and sign == '*' and num2 == 49:
        return("27*49 = 1323")
    if num1 == 27 and sign == '*' and num2 == 50:
        return("27*50 = 1350")
    if num1 == 28 and sign == '*' and num2 == 0:
        return("28*0 = 0")
    if num1 == 28 and sign == '*' and num2 == 1:
        return("28*1 = 28")
    if num1 == 28 and sign == '*' and num2 == 2:
        return("28*2 = 56")
    if num1 == 28 and sign == '*' and num2 == 3:
        return("28*3 = 84")
    if num1 == 28 and sign == '*' and num2 == 4:
        return("28*4 = 112")
    if num1 == 28 and sign == '*' and num2 == 5:
        return("28*5 = 140")
    if num1 == 28 and sign == '*' and num2 == 6:
        return("28*6 = 168")
    if num1 == 28 and sign == '*' and num2 == 7:
        return("28*7 = 196")
    if num1 == 28 and sign == '*' and num2 == 8:
        return("28*8 = 224")
    if num1 == 28 and sign == '*' and num2 == 9:
        return("28*9 = 252")
    if num1 == 28 and sign == '*' and num2 == 10:
        return("28*10 = 280")
    if num1 == 28 and sign == '*' and num2 == 11:
        return("28*11 = 308")
    if num1 == 28 and sign == '*' and num2 == 12:
        return("28*12 = 336")
    if num1 == 28 and sign == '*' and num2 == 13:
        return("28*13 = 364")
    if num1 == 28 and sign == '*' and num2 == 14:
        return("28*14 = 392")
    if num1 == 28 and sign == '*' and num2 == 15:
        return("28*15 = 420")
    if num1 == 28 and sign == '*' and num2 == 16:
        return("28*16 = 448")
    if num1 == 28 and sign == '*' and num2 == 17:
        return("28*17 = 476")
    if num1 == 28 and sign == '*' and num2 == 18:
        return("28*18 = 504")
    if num1 == 28 and sign == '*' and num2 == 19:
        return("28*19 = 532")
    if num1 == 28 and sign == '*' and num2 == 20:
        return("28*20 = 560")
    if num1 == 28 and sign == '*' and num2 == 21:
        return("28*21 = 588")
    if num1 == 28 and sign == '*' and num2 == 22:
        return("28*22 = 616")
    if num1 == 28 and sign == '*' and num2 == 23:
        return("28*23 = 644")
    if num1 == 28 and sign == '*' and num2 == 24:
        return("28*24 = 672")
    if num1 == 28 and sign == '*' and num2 == 25:
        return("28*25 = 700")
    if num1 == 28 and sign == '*' and num2 == 26:
        return("28*26 = 728")
    if num1 == 28 and sign == '*' and num2 == 27:
        return("28*27 = 756")
    if num1 == 28 and sign == '*' and num2 == 28:
        return("28*28 = 784")
    if num1 == 28 and sign == '*' and num2 == 29:
        return("28*29 = 812")
    if num1 == 28 and sign == '*' and num2 == 30:
        return("28*30 = 840")
    if num1 == 28 and sign == '*' and num2 == 31:
        return("28*31 = 868")
    if num1 == 28 and sign == '*' and num2 == 32:
        return("28*32 = 896")
    if num1 == 28 and sign == '*' and num2 == 33:
        return("28*33 = 924")
    if num1 == 28 and sign == '*' and num2 == 34:
        return("28*34 = 952")
    if num1 == 28 and sign == '*' and num2 == 35:
        return("28*35 = 980")
    if num1 == 28 and sign == '*' and num2 == 36:
        return("28*36 = 1008")
    if num1 == 28 and sign == '*' and num2 == 37:
        return("28*37 = 1036")
    if num1 == 28 and sign == '*' and num2 == 38:
        return("28*38 = 1064")
    if num1 == 28 and sign == '*' and num2 == 39:
        return("28*39 = 1092")
    if num1 == 28 and sign == '*' and num2 == 40:
        return("28*40 = 1120")
    if num1 == 28 and sign == '*' and num2 == 41:
        return("28*41 = 1148")
    if num1 == 28 and sign == '*' and num2 == 42:
        return("28*42 = 1176")
    if num1 == 28 and sign == '*' and num2 == 43:
        return("28*43 = 1204")
    if num1 == 28 and sign == '*' and num2 == 44:
        return("28*44 = 1232")
    if num1 == 28 and sign == '*' and num2 == 45:
        return("28*45 = 1260")
    if num1 == 28 and sign == '*' and num2 == 46:
        return("28*46 = 1288")
    if num1 == 28 and sign == '*' and num2 == 47:
        return("28*47 = 1316")
    if num1 == 28 and sign == '*' and num2 == 48:
        return("28*48 = 1344")
    if num1 == 28 and sign == '*' and num2 == 49:
        return("28*49 = 1372")
    if num1 == 28 and sign == '*' and num2 == 50:
        return("28*50 = 1400")
    if num1 == 29 and sign == '*' and num2 == 0:
        return("29*0 = 0")
    if num1 == 29 and sign == '*' and num2 == 1:
        return("29*1 = 29")
    if num1 == 29 and sign == '*' and num2 == 2:
        return("29*2 = 58")
    if num1 == 29 and sign == '*' and num2 == 3:
        return("29*3 = 87")
    if num1 == 29 and sign == '*' and num2 == 4:
        return("29*4 = 116")
    if num1 == 29 and sign == '*' and num2 == 5:
        return("29*5 = 145")
    if num1 == 29 and sign == '*' and num2 == 6:
        return("29*6 = 174")
    if num1 == 29 and sign == '*' and num2 == 7:
        return("29*7 = 203")
    if num1 == 29 and sign == '*' and num2 == 8:
        return("29*8 = 232")
    if num1 == 29 and sign == '*' and num2 == 9:
        return("29*9 = 261")
    if num1 == 29 and sign == '*' and num2 == 10:
        return("29*10 = 290")
    if num1 == 29 and sign == '*' and num2 == 11:
        return("29*11 = 319")
    if num1 == 29 and sign == '*' and num2 == 12:
        return("29*12 = 348")
    if num1 == 29 and sign == '*' and num2 == 13:
        return("29*13 = 377")
    if num1 == 29 and sign == '*' and num2 == 14:
        return("29*14 = 406")
    if num1 == 29 and sign == '*' and num2 == 15:
        return("29*15 = 435")
    if num1 == 29 and sign == '*' and num2 == 16:
        return("29*16 = 464")
    if num1 == 29 and sign == '*' and num2 == 17:
        return("29*17 = 493")
    if num1 == 29 and sign == '*' and num2 == 18:
        return("29*18 = 522")
    if num1 == 29 and sign == '*' and num2 == 19:
        return("29*19 = 551")
    if num1 == 29 and sign == '*' and num2 == 20:
        return("29*20 = 580")
    if num1 == 29 and sign == '*' and num2 == 21:
        return("29*21 = 609")
    if num1 == 29 and sign == '*' and num2 == 22:
        return("29*22 = 638")
    if num1 == 29 and sign == '*' and num2 == 23:
        return("29*23 = 667")
    if num1 == 29 and sign == '*' and num2 == 24:
        return("29*24 = 696")
    if num1 == 29 and sign == '*' and num2 == 25:
        return("29*25 = 725")
    if num1 == 29 and sign == '*' and num2 == 26:
        return("29*26 = 754")
    if num1 == 29 and sign == '*' and num2 == 27:
        return("29*27 = 783")
    if num1 == 29 and sign == '*' and num2 == 28:
        return("29*28 = 812")
    if num1 == 29 and sign == '*' and num2 == 29:
        return("29*29 = 841")
    if num1 == 29 and sign == '*' and num2 == 30:
        return("29*30 = 870")
    if num1 == 29 and sign == '*' and num2 == 31:
        return("29*31 = 899")
    if num1 == 29 and sign == '*' and num2 == 32:
        return("29*32 = 928")
    if num1 == 29 and sign == '*' and num2 == 33:
        return("29*33 = 957")
    if num1 == 29 and sign == '*' and num2 == 34:
        return("29*34 = 986")
    if num1 == 29 and sign == '*' and num2 == 35:
        return("29*35 = 1015")
    if num1 == 29 and sign == '*' and num2 == 36:
        return("29*36 = 1044")
    if num1 == 29 and sign == '*' and num2 == 37:
        return("29*37 = 1073")
    if num1 == 29 and sign == '*' and num2 == 38:
        return("29*38 = 1102")
    if num1 == 29 and sign == '*' and num2 == 39:
        return("29*39 = 1131")
    if num1 == 29 and sign == '*' and num2 == 40:
        return("29*40 = 1160")
    if num1 == 29 and sign == '*' and num2 == 41:
        return("29*41 = 1189")
    if num1 == 29 and sign == '*' and num2 == 42:
        return("29*42 = 1218")
    if num1 == 29 and sign == '*' and num2 == 43:
        return("29*43 = 1247")
    if num1 == 29 and sign == '*' and num2 == 44:
        return("29*44 = 1276")
    if num1 == 29 and sign == '*' and num2 == 45:
        return("29*45 = 1305")
    if num1 == 29 and sign == '*' and num2 == 46:
        return("29*46 = 1334")
    if num1 == 29 and sign == '*' and num2 == 47:
        return("29*47 = 1363")
    if num1 == 29 and sign == '*' and num2 == 48:
        return("29*48 = 1392")
    if num1 == 29 and sign == '*' and num2 == 49:
        return("29*49 = 1421")
    if num1 == 29 and sign == '*' and num2 == 50:
        return("29*50 = 1450")
    if num1 == 30 and sign == '*' and num2 == 0:
        return("30*0 = 0")
    if num1 == 30 and sign == '*' and num2 == 1:
        return("30*1 = 30")
    if num1 == 30 and sign == '*' and num2 == 2:
        return("30*2 = 60")
    if num1 == 30 and sign == '*' and num2 == 3:
        return("30*3 = 90")
    if num1 == 30 and sign == '*' and num2 == 4:
        return("30*4 = 120")
    if num1 == 30 and sign == '*' and num2 == 5:
        return("30*5 = 150")
    if num1 == 30 and sign == '*' and num2 == 6:
        return("30*6 = 180")
    if num1 == 30 and sign == '*' and num2 == 7:
        return("30*7 = 210")
    if num1 == 30 and sign == '*' and num2 == 8:
        return("30*8 = 240")
    if num1 == 30 and sign == '*' and num2 == 9:
        return("30*9 = 270")
    if num1 == 30 and sign == '*' and num2 == 10:
        return("30*10 = 300")
    if num1 == 30 and sign == '*' and num2 == 11:
        return("30*11 = 330")
    if num1 == 30 and sign == '*' and num2 == 12:
        return("30*12 = 360")
    if num1 == 30 and sign == '*' and num2 == 13:
        return("30*13 = 390")
    if num1 == 30 and sign == '*' and num2 == 14:
        return("30*14 = 420")
    if num1 == 30 and sign == '*' and num2 == 15:
        return("30*15 = 450")
    if num1 == 30 and sign == '*' and num2 == 16:
        return("30*16 = 480")
    if num1 == 30 and sign == '*' and num2 == 17:
        return("30*17 = 510")
    if num1 == 30 and sign == '*' and num2 == 18:
        return("30*18 = 540")
    if num1 == 30 and sign == '*' and num2 == 19:
        return("30*19 = 570")
    if num1 == 30 and sign == '*' and num2 == 20:
        return("30*20 = 600")
    if num1 == 30 and sign == '*' and num2 == 21:
        return("30*21 = 630")
    if num1 == 30 and sign == '*' and num2 == 22:
        return("30*22 = 660")
    if num1 == 30 and sign == '*' and num2 == 23:
        return("30*23 = 690")
    if num1 == 30 and sign == '*' and num2 == 24:
        return("30*24 = 720")
    if num1 == 30 and sign == '*' and num2 == 25:
        return("30*25 = 750")
    if num1 == 30 and sign == '*' and num2 == 26:
        return("30*26 = 780")
    if num1 == 30 and sign == '*' and num2 == 27:
        return("30*27 = 810")
    if num1 == 30 and sign == '*' and num2 == 28:
        return("30*28 = 840")
    if num1 == 30 and sign == '*' and num2 == 29:
        return("30*29 = 870")
    if num1 == 30 and sign == '*' and num2 == 30:
        return("30*30 = 900")
    if num1 == 30 and sign == '*' and num2 == 31:
        return("30*31 = 930")
    if num1 == 30 and sign == '*' and num2 == 32:
        return("30*32 = 960")
    if num1 == 30 and sign == '*' and num2 == 33:
        return("30*33 = 990")
    if num1 == 30 and sign == '*' and num2 == 34:
        return("30*34 = 1020")
    if num1 == 30 and sign == '*' and num2 == 35:
        return("30*35 = 1050")
    if num1 == 30 and sign == '*' and num2 == 36:
        return("30*36 = 1080")
    if num1 == 30 and sign == '*' and num2 == 37:
        return("30*37 = 1110")
    if num1 == 30 and sign == '*' and num2 == 38:
        return("30*38 = 1140")
    if num1 == 30 and sign == '*' and num2 == 39:
        return("30*39 = 1170")
    if num1 == 30 and sign == '*' and num2 == 40:
        return("30*40 = 1200")
    if num1 == 30 and sign == '*' and num2 == 41:
        return("30*41 = 1230")
    if num1 == 30 and sign == '*' and num2 == 42:
        return("30*42 = 1260")
    if num1 == 30 and sign == '*' and num2 == 43:
        return("30*43 = 1290")
    if num1 == 30 and sign == '*' and num2 == 44:
        return("30*44 = 1320")
    if num1 == 30 and sign == '*' and num2 == 45:
        return("30*45 = 1350")
    if num1 == 30 and sign == '*' and num2 == 46:
        return("30*46 = 1380")
    if num1 == 30 and sign == '*' and num2 == 47:
        return("30*47 = 1410")
    if num1 == 30 and sign == '*' and num2 == 48:
        return("30*48 = 1440")
    if num1 == 30 and sign == '*' and num2 == 49:
        return("30*49 = 1470")
    if num1 == 30 and sign == '*' and num2 == 50:
        return("30*50 = 1500")
    if num1 == 31 and sign == '*' and num2 == 0:
        return("31*0 = 0")
    if num1 == 31 and sign == '*' and num2 == 1:
        return("31*1 = 31")
    if num1 == 31 and sign == '*' and num2 == 2:
        return("31*2 = 62")
    if num1 == 31 and sign == '*' and num2 == 3:
        return("31*3 = 93")
    if num1 == 31 and sign == '*' and num2 == 4:
        return("31*4 = 124")
    if num1 == 31 and sign == '*' and num2 == 5:
        return("31*5 = 155")
    if num1 == 31 and sign == '*' and num2 == 6:
        return("31*6 = 186")
    if num1 == 31 and sign == '*' and num2 == 7:
        return("31*7 = 217")
    if num1 == 31 and sign == '*' and num2 == 8:
        return("31*8 = 248")
    if num1 == 31 and sign == '*' and num2 == 9:
        return("31*9 = 279")
    if num1 == 31 and sign == '*' and num2 == 10:
        return("31*10 = 310")
    if num1 == 31 and sign == '*' and num2 == 11:
        return("31*11 = 341")
    if num1 == 31 and sign == '*' and num2 == 12:
        return("31*12 = 372")
    if num1 == 31 and sign == '*' and num2 == 13:
        return("31*13 = 403")
    if num1 == 31 and sign == '*' and num2 == 14:
        return("31*14 = 434")
    if num1 == 31 and sign == '*' and num2 == 15:
        return("31*15 = 465")
    if num1 == 31 and sign == '*' and num2 == 16:
        return("31*16 = 496")
    if num1 == 31 and sign == '*' and num2 == 17:
        return("31*17 = 527")
    if num1 == 31 and sign == '*' and num2 == 18:
        return("31*18 = 558")
    if num1 == 31 and sign == '*' and num2 == 19:
        return("31*19 = 589")
    if num1 == 31 and sign == '*' and num2 == 20:
        return("31*20 = 620")
    if num1 == 31 and sign == '*' and num2 == 21:
        return("31*21 = 651")
    if num1 == 31 and sign == '*' and num2 == 22:
        return("31*22 = 682")
    if num1 == 31 and sign == '*' and num2 == 23:
        return("31*23 = 713")
    if num1 == 31 and sign == '*' and num2 == 24:
        return("31*24 = 744")
    if num1 == 31 and sign == '*' and num2 == 25:
        return("31*25 = 775")
    if num1 == 31 and sign == '*' and num2 == 26:
        return("31*26 = 806")
    if num1 == 31 and sign == '*' and num2 == 27:
        return("31*27 = 837")
    if num1 == 31 and sign == '*' and num2 == 28:
        return("31*28 = 868")
    if num1 == 31 and sign == '*' and num2 == 29:
        return("31*29 = 899")
    if num1 == 31 and sign == '*' and num2 == 30:
        return("31*30 = 930")
    if num1 == 31 and sign == '*' and num2 == 31:
        return("31*31 = 961")
    if num1 == 31 and sign == '*' and num2 == 32:
        return("31*32 = 992")
    if num1 == 31 and sign == '*' and num2 == 33:
        return("31*33 = 1023")
    if num1 == 31 and sign == '*' and num2 == 34:
        return("31*34 = 1054")
    if num1 == 31 and sign == '*' and num2 == 35:
        return("31*35 = 1085")
    if num1 == 31 and sign == '*' and num2 == 36:
        return("31*36 = 1116")
    if num1 == 31 and sign == '*' and num2 == 37:
        return("31*37 = 1147")
    if num1 == 31 and sign == '*' and num2 == 38:
        return("31*38 = 1178")
    if num1 == 31 and sign == '*' and num2 == 39:
        return("31*39 = 1209")
    if num1 == 31 and sign == '*' and num2 == 40:
        return("31*40 = 1240")
    if num1 == 31 and sign == '*' and num2 == 41:
        return("31*41 = 1271")
    if num1 == 31 and sign == '*' and num2 == 42:
        return("31*42 = 1302")
    if num1 == 31 and sign == '*' and num2 == 43:
        return("31*43 = 1333")
    if num1 == 31 and sign == '*' and num2 == 44:
        return("31*44 = 1364")
    if num1 == 31 and sign == '*' and num2 == 45:
        return("31*45 = 1395")
    if num1 == 31 and sign == '*' and num2 == 46:
        return("31*46 = 1426")
    if num1 == 31 and sign == '*' and num2 == 47:
        return("31*47 = 1457")
    if num1 == 31 and sign == '*' and num2 == 48:
        return("31*48 = 1488")
    if num1 == 31 and sign == '*' and num2 == 49:
        return("31*49 = 1519")
    if num1 == 31 and sign == '*' and num2 == 50:
        return("31*50 = 1550")
    if num1 == 32 and sign == '*' and num2 == 0:
        return("32*0 = 0")
    if num1 == 32 and sign == '*' and num2 == 1:
        return("32*1 = 32")
    if num1 == 32 and sign == '*' and num2 == 2:
        return("32*2 = 64")
    if num1 == 32 and sign == '*' and num2 == 3:
        return("32*3 = 96")
    if num1 == 32 and sign == '*' and num2 == 4:
        return("32*4 = 128")
    if num1 == 32 and sign == '*' and num2 == 5:
        return("32*5 = 160")
    if num1 == 32 and sign == '*' and num2 == 6:
        return("32*6 = 192")
    if num1 == 32 and sign == '*' and num2 == 7:
        return("32*7 = 224")
    if num1 == 32 and sign == '*' and num2 == 8:
        return("32*8 = 256")
    if num1 == 32 and sign == '*' and num2 == 9:
        return("32*9 = 288")
    if num1 == 32 and sign == '*' and num2 == 10:
        return("32*10 = 320")
    if num1 == 32 and sign == '*' and num2 == 11:
        return("32*11 = 352")
    if num1 == 32 and sign == '*' and num2 == 12:
        return("32*12 = 384")
    if num1 == 32 and sign == '*' and num2 == 13:
        return("32*13 = 416")
    if num1 == 32 and sign == '*' and num2 == 14:
        return("32*14 = 448")
    if num1 == 32 and sign == '*' and num2 == 15:
        return("32*15 = 480")
    if num1 == 32 and sign == '*' and num2 == 16:
        return("32*16 = 512")
    if num1 == 32 and sign == '*' and num2 == 17:
        return("32*17 = 544")
    if num1 == 32 and sign == '*' and num2 == 18:
        return("32*18 = 576")
    if num1 == 32 and sign == '*' and num2 == 19:
        return("32*19 = 608")
    if num1 == 32 and sign == '*' and num2 == 20:
        return("32*20 = 640")
    if num1 == 32 and sign == '*' and num2 == 21:
        return("32*21 = 672")
    if num1 == 32 and sign == '*' and num2 == 22:
        return("32*22 = 704")
    if num1 == 32 and sign == '*' and num2 == 23:
        return("32*23 = 736")
    if num1 == 32 and sign == '*' and num2 == 24:
        return("32*24 = 768")
    if num1 == 32 and sign == '*' and num2 == 25:
        return("32*25 = 800")
    if num1 == 32 and sign == '*' and num2 == 26:
        return("32*26 = 832")
    if num1 == 32 and sign == '*' and num2 == 27:
        return("32*27 = 864")
    if num1 == 32 and sign == '*' and num2 == 28:
        return("32*28 = 896")
    if num1 == 32 and sign == '*' and num2 == 29:
        return("32*29 = 928")
    if num1 == 32 and sign == '*' and num2 == 30:
        return("32*30 = 960")
    if num1 == 32 and sign == '*' and num2 == 31:
        return("32*31 = 992")
    if num1 == 32 and sign == '*' and num2 == 32:
        return("32*32 = 1024")
    if num1 == 32 and sign == '*' and num2 == 33:
        return("32*33 = 1056")
    if num1 == 32 and sign == '*' and num2 == 34:
        return("32*34 = 1088")
    if num1 == 32 and sign == '*' and num2 == 35:
        return("32*35 = 1120")
    if num1 == 32 and sign == '*' and num2 == 36:
        return("32*36 = 1152")
    if num1 == 32 and sign == '*' and num2 == 37:
        return("32*37 = 1184")
    if num1 == 32 and sign == '*' and num2 == 38:
        return("32*38 = 1216")
    if num1 == 32 and sign == '*' and num2 == 39:
        return("32*39 = 1248")
    if num1 == 32 and sign == '*' and num2 == 40:
        return("32*40 = 1280")
    if num1 == 32 and sign == '*' and num2 == 41:
        return("32*41 = 1312")
    if num1 == 32 and sign == '*' and num2 == 42:
        return("32*42 = 1344")
    if num1 == 32 and sign == '*' and num2 == 43:
        return("32*43 = 1376")
    if num1 == 32 and sign == '*' and num2 == 44:
        return("32*44 = 1408")
    if num1 == 32 and sign == '*' and num2 == 45:
        return("32*45 = 1440")
    if num1 == 32 and sign == '*' and num2 == 46:
        return("32*46 = 1472")
    if num1 == 32 and sign == '*' and num2 == 47:
        return("32*47 = 1504")
    if num1 == 32 and sign == '*' and num2 == 48:
        return("32*48 = 1536")
    if num1 == 32 and sign == '*' and num2 == 49:
        return("32*49 = 1568")
    if num1 == 32 and sign == '*' and num2 == 50:
        return("32*50 = 1600")
    if num1 == 33 and sign == '*' and num2 == 0:
        return("33*0 = 0")
    if num1 == 33 and sign == '*' and num2 == 1:
        return("33*1 = 33")
    if num1 == 33 and sign == '*' and num2 == 2:
        return("33*2 = 66")
    if num1 == 33 and sign == '*' and num2 == 3:
        return("33*3 = 99")
    if num1 == 33 and sign == '*' and num2 == 4:
        return("33*4 = 132")
    if num1 == 33 and sign == '*' and num2 == 5:
        return("33*5 = 165")
    if num1 == 33 and sign == '*' and num2 == 6:
        return("33*6 = 198")
    if num1 == 33 and sign == '*' and num2 == 7:
        return("33*7 = 231")
    if num1 == 33 and sign == '*' and num2 == 8:
        return("33*8 = 264")
    if num1 == 33 and sign == '*' and num2 == 9:
        return("33*9 = 297")
    if num1 == 33 and sign == '*' and num2 == 10:
        return("33*10 = 330")
    if num1 == 33 and sign == '*' and num2 == 11:
        return("33*11 = 363")
    if num1 == 33 and sign == '*' and num2 == 12:
        return("33*12 = 396")
    if num1 == 33 and sign == '*' and num2 == 13:
        return("33*13 = 429")
    if num1 == 33 and sign == '*' and num2 == 14:
        return("33*14 = 462")
    if num1 == 33 and sign == '*' and num2 == 15:
        return("33*15 = 495")
    if num1 == 33 and sign == '*' and num2 == 16:
        return("33*16 = 528")
    if num1 == 33 and sign == '*' and num2 == 17:
        return("33*17 = 561")
    if num1 == 33 and sign == '*' and num2 == 18:
        return("33*18 = 594")
    if num1 == 33 and sign == '*' and num2 == 19:
        return("33*19 = 627")
    if num1 == 33 and sign == '*' and num2 == 20:
        return("33*20 = 660")
    if num1 == 33 and sign == '*' and num2 == 21:
        return("33*21 = 693")
    if num1 == 33 and sign == '*' and num2 == 22:
        return("33*22 = 726")
    if num1 == 33 and sign == '*' and num2 == 23:
        return("33*23 = 759")
    if num1 == 33 and sign == '*' and num2 == 24:
        return("33*24 = 792")
    if num1 == 33 and sign == '*' and num2 == 25:
        return("33*25 = 825")
    if num1 == 33 and sign == '*' and num2 == 26:
        return("33*26 = 858")
    if num1 == 33 and sign == '*' and num2 == 27:
        return("33*27 = 891")
    if num1 == 33 and sign == '*' and num2 == 28:
        return("33*28 = 924")
    if num1 == 33 and sign == '*' and num2 == 29:
        return("33*29 = 957")
    if num1 == 33 and sign == '*' and num2 == 30:
        return("33*30 = 990")
    if num1 == 33 and sign == '*' and num2 == 31:
        return("33*31 = 1023")
    if num1 == 33 and sign == '*' and num2 == 32:
        return("33*32 = 1056")
    if num1 == 33 and sign == '*' and num2 == 33:
        return("33*33 = 1089")
    if num1 == 33 and sign == '*' and num2 == 34:
        return("33*34 = 1122")
    if num1 == 33 and sign == '*' and num2 == 35:
        return("33*35 = 1155")
    if num1 == 33 and sign == '*' and num2 == 36:
        return("33*36 = 1188")
    if num1 == 33 and sign == '*' and num2 == 37:
        return("33*37 = 1221")
    if num1 == 33 and sign == '*' and num2 == 38:
        return("33*38 = 1254")
    if num1 == 33 and sign == '*' and num2 == 39:
        return("33*39 = 1287")
    if num1 == 33 and sign == '*' and num2 == 40:
        return("33*40 = 1320")
    if num1 == 33 and sign == '*' and num2 == 41:
        return("33*41 = 1353")
    if num1 == 33 and sign == '*' and num2 == 42:
        return("33*42 = 1386")
    if num1 == 33 and sign == '*' and num2 == 43:
        return("33*43 = 1419")
    if num1 == 33 and sign == '*' and num2 == 44:
        return("33*44 = 1452")
    if num1 == 33 and sign == '*' and num2 == 45:
        return("33*45 = 1485")
    if num1 == 33 and sign == '*' and num2 == 46:
        return("33*46 = 1518")
    if num1 == 33 and sign == '*' and num2 == 47:
        return("33*47 = 1551")
    if num1 == 33 and sign == '*' and num2 == 48:
        return("33*48 = 1584")
    if num1 == 33 and sign == '*' and num2 == 49:
        return("33*49 = 1617")
    if num1 == 33 and sign == '*' and num2 == 50:
        return("33*50 = 1650")
    if num1 == 34 and sign == '*' and num2 == 0:
        return("34*0 = 0")
    if num1 == 34 and sign == '*' and num2 == 1:
        return("34*1 = 34")
    if num1 == 34 and sign == '*' and num2 == 2:
        return("34*2 = 68")
    if num1 == 34 and sign == '*' and num2 == 3:
        return("34*3 = 102")
    if num1 == 34 and sign == '*' and num2 == 4:
        return("34*4 = 136")
    if num1 == 34 and sign == '*' and num2 == 5:
        return("34*5 = 170")
    if num1 == 34 and sign == '*' and num2 == 6:
        return("34*6 = 204")
    if num1 == 34 and sign == '*' and num2 == 7:
        return("34*7 = 238")
    if num1 == 34 and sign == '*' and num2 == 8:
        return("34*8 = 272")
    if num1 == 34 and sign == '*' and num2 == 9:
        return("34*9 = 306")
    if num1 == 34 and sign == '*' and num2 == 10:
        return("34*10 = 340")
    if num1 == 34 and sign == '*' and num2 == 11:
        return("34*11 = 374")
    if num1 == 34 and sign == '*' and num2 == 12:
        return("34*12 = 408")
    if num1 == 34 and sign == '*' and num2 == 13:
        return("34*13 = 442")
    if num1 == 34 and sign == '*' and num2 == 14:
        return("34*14 = 476")
    if num1 == 34 and sign == '*' and num2 == 15:
        return("34*15 = 510")
    if num1 == 34 and sign == '*' and num2 == 16:
        return("34*16 = 544")
    if num1 == 34 and sign == '*' and num2 == 17:
        return("34*17 = 578")
    if num1 == 34 and sign == '*' and num2 == 18:
        return("34*18 = 612")
    if num1 == 34 and sign == '*' and num2 == 19:
        return("34*19 = 646")
    if num1 == 34 and sign == '*' and num2 == 20:
        return("34*20 = 680")
    if num1 == 34 and sign == '*' and num2 == 21:
        return("34*21 = 714")
    if num1 == 34 and sign == '*' and num2 == 22:
        return("34*22 = 748")
    if num1 == 34 and sign == '*' and num2 == 23:
        return("34*23 = 782")
    if num1 == 34 and sign == '*' and num2 == 24:
        return("34*24 = 816")
    if num1 == 34 and sign == '*' and num2 == 25:
        return("34*25 = 850")
    if num1 == 34 and sign == '*' and num2 == 26:
        return("34*26 = 884")
    if num1 == 34 and sign == '*' and num2 == 27:
        return("34*27 = 918")
    if num1 == 34 and sign == '*' and num2 == 28:
        return("34*28 = 952")
    if num1 == 34 and sign == '*' and num2 == 29:
        return("34*29 = 986")
    if num1 == 34 and sign == '*' and num2 == 30:
        return("34*30 = 1020")
    if num1 == 34 and sign == '*' and num2 == 31:
        return("34*31 = 1054")
    if num1 == 34 and sign == '*' and num2 == 32:
        return("34*32 = 1088")
    if num1 == 34 and sign == '*' and num2 == 33:
        return("34*33 = 1122")
    if num1 == 34 and sign == '*' and num2 == 34:
        return("34*34 = 1156")
    if num1 == 34 and sign == '*' and num2 == 35:
        return("34*35 = 1190")
    if num1 == 34 and sign == '*' and num2 == 36:
        return("34*36 = 1224")
    if num1 == 34 and sign == '*' and num2 == 37:
        return("34*37 = 1258")
    if num1 == 34 and sign == '*' and num2 == 38:
        return("34*38 = 1292")
    if num1 == 34 and sign == '*' and num2 == 39:
        return("34*39 = 1326")
    if num1 == 34 and sign == '*' and num2 == 40:
        return("34*40 = 1360")
    if num1 == 34 and sign == '*' and num2 == 41:
        return("34*41 = 1394")
    if num1 == 34 and sign == '*' and num2 == 42:
        return("34*42 = 1428")
    if num1 == 34 and sign == '*' and num2 == 43:
        return("34*43 = 1462")
    if num1 == 34 and sign == '*' and num2 == 44:
        return("34*44 = 1496")
    if num1 == 34 and sign == '*' and num2 == 45:
        return("34*45 = 1530")
    if num1 == 34 and sign == '*' and num2 == 46:
        return("34*46 = 1564")
    if num1 == 34 and sign == '*' and num2 == 47:
        return("34*47 = 1598")
    if num1 == 34 and sign == '*' and num2 == 48:
        return("34*48 = 1632")
    if num1 == 34 and sign == '*' and num2 == 49:
        return("34*49 = 1666")
    if num1 == 34 and sign == '*' and num2 == 50:
        return("34*50 = 1700")
    if num1 == 35 and sign == '*' and num2 == 0:
        return("35*0 = 0")
    if num1 == 35 and sign == '*' and num2 == 1:
        return("35*1 = 35")
    if num1 == 35 and sign == '*' and num2 == 2:
        return("35*2 = 70")
    if num1 == 35 and sign == '*' and num2 == 3:
        return("35*3 = 105")
    if num1 == 35 and sign == '*' and num2 == 4:
        return("35*4 = 140")
    if num1 == 35 and sign == '*' and num2 == 5:
        return("35*5 = 175")
    if num1 == 35 and sign == '*' and num2 == 6:
        return("35*6 = 210")
    if num1 == 35 and sign == '*' and num2 == 7:
        return("35*7 = 245")
    if num1 == 35 and sign == '*' and num2 == 8:
        return("35*8 = 280")
    if num1 == 35 and sign == '*' and num2 == 9:
        return("35*9 = 315")
    if num1 == 35 and sign == '*' and num2 == 10:
        return("35*10 = 350")
    if num1 == 35 and sign == '*' and num2 == 11:
        return("35*11 = 385")
    if num1 == 35 and sign == '*' and num2 == 12:
        return("35*12 = 420")
    if num1 == 35 and sign == '*' and num2 == 13:
        return("35*13 = 455")
    if num1 == 35 and sign == '*' and num2 == 14:
        return("35*14 = 490")
    if num1 == 35 and sign == '*' and num2 == 15:
        return("35*15 = 525")
    if num1 == 35 and sign == '*' and num2 == 16:
        return("35*16 = 560")
    if num1 == 35 and sign == '*' and num2 == 17:
        return("35*17 = 595")
    if num1 == 35 and sign == '*' and num2 == 18:
        return("35*18 = 630")
    if num1 == 35 and sign == '*' and num2 == 19:
        return("35*19 = 665")
    if num1 == 35 and sign == '*' and num2 == 20:
        return("35*20 = 700")
    if num1 == 35 and sign == '*' and num2 == 21:
        return("35*21 = 735")
    if num1 == 35 and sign == '*' and num2 == 22:
        return("35*22 = 770")
    if num1 == 35 and sign == '*' and num2 == 23:
        return("35*23 = 805")
    if num1 == 35 and sign == '*' and num2 == 24:
        return("35*24 = 840")
    if num1 == 35 and sign == '*' and num2 == 25:
        return("35*25 = 875")
    if num1 == 35 and sign == '*' and num2 == 26:
        return("35*26 = 910")
    if num1 == 35 and sign == '*' and num2 == 27:
        return("35*27 = 945")
    if num1 == 35 and sign == '*' and num2 == 28:
        return("35*28 = 980")
    if num1 == 35 and sign == '*' and num2 == 29:
        return("35*29 = 1015")
    if num1 == 35 and sign == '*' and num2 == 30:
        return("35*30 = 1050")
    if num1 == 35 and sign == '*' and num2 == 31:
        return("35*31 = 1085")
    if num1 == 35 and sign == '*' and num2 == 32:
        return("35*32 = 1120")
    if num1 == 35 and sign == '*' and num2 == 33:
        return("35*33 = 1155")
    if num1 == 35 and sign == '*' and num2 == 34:
        return("35*34 = 1190")
    if num1 == 35 and sign == '*' and num2 == 35:
        return("35*35 = 1225")
    if num1 == 35 and sign == '*' and num2 == 36:
        return("35*36 = 1260")
    if num1 == 35 and sign == '*' and num2 == 37:
        return("35*37 = 1295")
    if num1 == 35 and sign == '*' and num2 == 38:
        return("35*38 = 1330")
    if num1 == 35 and sign == '*' and num2 == 39:
        return("35*39 = 1365")
    if num1 == 35 and sign == '*' and num2 == 40:
        return("35*40 = 1400")
    if num1 == 35 and sign == '*' and num2 == 41:
        return("35*41 = 1435")
    if num1 == 35 and sign == '*' and num2 == 42:
        return("35*42 = 1470")
    if num1 == 35 and sign == '*' and num2 == 43:
        return("35*43 = 1505")
    if num1 == 35 and sign == '*' and num2 == 44:
        return("35*44 = 1540")
    if num1 == 35 and sign == '*' and num2 == 45:
        return("35*45 = 1575")
    if num1 == 35 and sign == '*' and num2 == 46:
        return("35*46 = 1610")
    if num1 == 35 and sign == '*' and num2 == 47:
        return("35*47 = 1645")
    if num1 == 35 and sign == '*' and num2 == 48:
        return("35*48 = 1680")
    if num1 == 35 and sign == '*' and num2 == 49:
        return("35*49 = 1715")
    if num1 == 35 and sign == '*' and num2 == 50:
        return("35*50 = 1750")
    if num1 == 36 and sign == '*' and num2 == 0:
        return("36*0 = 0")
    if num1 == 36 and sign == '*' and num2 == 1:
        return("36*1 = 36")
    if num1 == 36 and sign == '*' and num2 == 2:
        return("36*2 = 72")
    if num1 == 36 and sign == '*' and num2 == 3:
        return("36*3 = 108")
    if num1 == 36 and sign == '*' and num2 == 4:
        return("36*4 = 144")
    if num1 == 36 and sign == '*' and num2 == 5:
        return("36*5 = 180")
    if num1 == 36 and sign == '*' and num2 == 6:
        return("36*6 = 216")
    if num1 == 36 and sign == '*' and num2 == 7:
        return("36*7 = 252")
    if num1 == 36 and sign == '*' and num2 == 8:
        return("36*8 = 288")
    if num1 == 36 and sign == '*' and num2 == 9:
        return("36*9 = 324")
    if num1 == 36 and sign == '*' and num2 == 10:
        return("36*10 = 360")
    if num1 == 36 and sign == '*' and num2 == 11:
        return("36*11 = 396")
    if num1 == 36 and sign == '*' and num2 == 12:
        return("36*12 = 432")
    if num1 == 36 and sign == '*' and num2 == 13:
        return("36*13 = 468")
    if num1 == 36 and sign == '*' and num2 == 14:
        return("36*14 = 504")
    if num1 == 36 and sign == '*' and num2 == 15:
        return("36*15 = 540")
    if num1 == 36 and sign == '*' and num2 == 16:
        return("36*16 = 576")
    if num1 == 36 and sign == '*' and num2 == 17:
        return("36*17 = 612")
    if num1 == 36 and sign == '*' and num2 == 18:
        return("36*18 = 648")
    if num1 == 36 and sign == '*' and num2 == 19:
        return("36*19 = 684")
    if num1 == 36 and sign == '*' and num2 == 20:
        return("36*20 = 720")
    if num1 == 36 and sign == '*' and num2 == 21:
        return("36*21 = 756")
    if num1 == 36 and sign == '*' and num2 == 22:
        return("36*22 = 792")
    if num1 == 36 and sign == '*' and num2 == 23:
        return("36*23 = 828")
    if num1 == 36 and sign == '*' and num2 == 24:
        return("36*24 = 864")
    if num1 == 36 and sign == '*' and num2 == 25:
        return("36*25 = 900")
    if num1 == 36 and sign == '*' and num2 == 26:
        return("36*26 = 936")
    if num1 == 36 and sign == '*' and num2 == 27:
        return("36*27 = 972")
    if num1 == 36 and sign == '*' and num2 == 28:
        return("36*28 = 1008")
    if num1 == 36 and sign == '*' and num2 == 29:
        return("36*29 = 1044")
    if num1 == 36 and sign == '*' and num2 == 30:
        return("36*30 = 1080")
    if num1 == 36 and sign == '*' and num2 == 31:
        return("36*31 = 1116")
    if num1 == 36 and sign == '*' and num2 == 32:
        return("36*32 = 1152")
    if num1 == 36 and sign == '*' and num2 == 33:
        return("36*33 = 1188")
    if num1 == 36 and sign == '*' and num2 == 34:
        return("36*34 = 1224")
    if num1 == 36 and sign == '*' and num2 == 35:
        return("36*35 = 1260")
    if num1 == 36 and sign == '*' and num2 == 36:
        return("36*36 = 1296")
    if num1 == 36 and sign == '*' and num2 == 37:
        return("36*37 = 1332")
    if num1 == 36 and sign == '*' and num2 == 38:
        return("36*38 = 1368")
    if num1 == 36 and sign == '*' and num2 == 39:
        return("36*39 = 1404")
    if num1 == 36 and sign == '*' and num2 == 40:
        return("36*40 = 1440")
    if num1 == 36 and sign == '*' and num2 == 41:
        return("36*41 = 1476")
    if num1 == 36 and sign == '*' and num2 == 42:
        return("36*42 = 1512")
    if num1 == 36 and sign == '*' and num2 == 43:
        return("36*43 = 1548")
    if num1 == 36 and sign == '*' and num2 == 44:
        return("36*44 = 1584")
    if num1 == 36 and sign == '*' and num2 == 45:
        return("36*45 = 1620")
    if num1 == 36 and sign == '*' and num2 == 46:
        return("36*46 = 1656")
    if num1 == 36 and sign == '*' and num2 == 47:
        return("36*47 = 1692")
    if num1 == 36 and sign == '*' and num2 == 48:
        return("36*48 = 1728")
    if num1 == 36 and sign == '*' and num2 == 49:
        return("36*49 = 1764")
    if num1 == 36 and sign == '*' and num2 == 50:
        return("36*50 = 1800")
    if num1 == 37 and sign == '*' and num2 == 0:
        return("37*0 = 0")
    if num1 == 37 and sign == '*' and num2 == 1:
        return("37*1 = 37")
    if num1 == 37 and sign == '*' and num2 == 2:
        return("37*2 = 74")
    if num1 == 37 and sign == '*' and num2 == 3:
        return("37*3 = 111")
    if num1 == 37 and sign == '*' and num2 == 4:
        return("37*4 = 148")
    if num1 == 37 and sign == '*' and num2 == 5:
        return("37*5 = 185")
    if num1 == 37 and sign == '*' and num2 == 6:
        return("37*6 = 222")
    if num1 == 37 and sign == '*' and num2 == 7:
        return("37*7 = 259")
    if num1 == 37 and sign == '*' and num2 == 8:
        return("37*8 = 296")
    if num1 == 37 and sign == '*' and num2 == 9:
        return("37*9 = 333")
    if num1 == 37 and sign == '*' and num2 == 10:
        return("37*10 = 370")
    if num1 == 37 and sign == '*' and num2 == 11:
        return("37*11 = 407")
    if num1 == 37 and sign == '*' and num2 == 12:
        return("37*12 = 444")
    if num1 == 37 and sign == '*' and num2 == 13:
        return("37*13 = 481")
    if num1 == 37 and sign == '*' and num2 == 14:
        return("37*14 = 518")
    if num1 == 37 and sign == '*' and num2 == 15:
        return("37*15 = 555")
    if num1 == 37 and sign == '*' and num2 == 16:
        return("37*16 = 592")
    if num1 == 37 and sign == '*' and num2 == 17:
        return("37*17 = 629")
    if num1 == 37 and sign == '*' and num2 == 18:
        return("37*18 = 666")
    if num1 == 37 and sign == '*' and num2 == 19:
        return("37*19 = 703")
    if num1 == 37 and sign == '*' and num2 == 20:
        return("37*20 = 740")
    if num1 == 37 and sign == '*' and num2 == 21:
        return("37*21 = 777")
    if num1 == 37 and sign == '*' and num2 == 22:
        return("37*22 = 814")
    if num1 == 37 and sign == '*' and num2 == 23:
        return("37*23 = 851")
    if num1 == 37 and sign == '*' and num2 == 24:
        return("37*24 = 888")
    if num1 == 37 and sign == '*' and num2 == 25:
        return("37*25 = 925")
    if num1 == 37 and sign == '*' and num2 == 26:
        return("37*26 = 962")
    if num1 == 37 and sign == '*' and num2 == 27:
        return("37*27 = 999")
    if num1 == 37 and sign == '*' and num2 == 28:
        return("37*28 = 1036")
    if num1 == 37 and sign == '*' and num2 == 29:
        return("37*29 = 1073")
    if num1 == 37 and sign == '*' and num2 == 30:
        return("37*30 = 1110")
    if num1 == 37 and sign == '*' and num2 == 31:
        return("37*31 = 1147")
    if num1 == 37 and sign == '*' and num2 == 32:
        return("37*32 = 1184")
    if num1 == 37 and sign == '*' and num2 == 33:
        return("37*33 = 1221")
    if num1 == 37 and sign == '*' and num2 == 34:
        return("37*34 = 1258")
    if num1 == 37 and sign == '*' and num2 == 35:
        return("37*35 = 1295")
    if num1 == 37 and sign == '*' and num2 == 36:
        return("37*36 = 1332")
    if num1 == 37 and sign == '*' and num2 == 37:
        return("37*37 = 1369")
    if num1 == 37 and sign == '*' and num2 == 38:
        return("37*38 = 1406")
    if num1 == 37 and sign == '*' and num2 == 39:
        return("37*39 = 1443")
    if num1 == 37 and sign == '*' and num2 == 40:
        return("37*40 = 1480")
    if num1 == 37 and sign == '*' and num2 == 41:
        return("37*41 = 1517")
    if num1 == 37 and sign == '*' and num2 == 42:
        return("37*42 = 1554")
    if num1 == 37 and sign == '*' and num2 == 43:
        return("37*43 = 1591")
    if num1 == 37 and sign == '*' and num2 == 44:
        return("37*44 = 1628")
    if num1 == 37 and sign == '*' and num2 == 45:
        return("37*45 = 1665")
    if num1 == 37 and sign == '*' and num2 == 46:
        return("37*46 = 1702")
    if num1 == 37 and sign == '*' and num2 == 47:
        return("37*47 = 1739")
    if num1 == 37 and sign == '*' and num2 == 48:
        return("37*48 = 1776")
    if num1 == 37 and sign == '*' and num2 == 49:
        return("37*49 = 1813")
    if num1 == 37 and sign == '*' and num2 == 50:
        return("37*50 = 1850")
    if num1 == 38 and sign == '*' and num2 == 0:
        return("38*0 = 0")
    if num1 == 38 and sign == '*' and num2 == 1:
        return("38*1 = 38")
    if num1 == 38 and sign == '*' and num2 == 2:
        return("38*2 = 76")
    if num1 == 38 and sign == '*' and num2 == 3:
        return("38*3 = 114")
    if num1 == 38 and sign == '*' and num2 == 4:
        return("38*4 = 152")
    if num1 == 38 and sign == '*' and num2 == 5:
        return("38*5 = 190")
    if num1 == 38 and sign == '*' and num2 == 6:
        return("38*6 = 228")
    if num1 == 38 and sign == '*' and num2 == 7:
        return("38*7 = 266")
    if num1 == 38 and sign == '*' and num2 == 8:
        return("38*8 = 304")
    if num1 == 38 and sign == '*' and num2 == 9:
        return("38*9 = 342")
    if num1 == 38 and sign == '*' and num2 == 10:
        return("38*10 = 380")
    if num1 == 38 and sign == '*' and num2 == 11:
        return("38*11 = 418")
    if num1 == 38 and sign == '*' and num2 == 12:
        return("38*12 = 456")
    if num1 == 38 and sign == '*' and num2 == 13:
        return("38*13 = 494")
    if num1 == 38 and sign == '*' and num2 == 14:
        return("38*14 = 532")
    if num1 == 38 and sign == '*' and num2 == 15:
        return("38*15 = 570")
    if num1 == 38 and sign == '*' and num2 == 16:
        return("38*16 = 608")
    if num1 == 38 and sign == '*' and num2 == 17:
        return("38*17 = 646")
    if num1 == 38 and sign == '*' and num2 == 18:
        return("38*18 = 684")
    if num1 == 38 and sign == '*' and num2 == 19:
        return("38*19 = 722")
    if num1 == 38 and sign == '*' and num2 == 20:
        return("38*20 = 760")
    if num1 == 38 and sign == '*' and num2 == 21:
        return("38*21 = 798")
    if num1 == 38 and sign == '*' and num2 == 22:
        return("38*22 = 836")
    if num1 == 38 and sign == '*' and num2 == 23:
        return("38*23 = 874")
    if num1 == 38 and sign == '*' and num2 == 24:
        return("38*24 = 912")
    if num1 == 38 and sign == '*' and num2 == 25:
        return("38*25 = 950")
    if num1 == 38 and sign == '*' and num2 == 26:
        return("38*26 = 988")
    if num1 == 38 and sign == '*' and num2 == 27:
        return("38*27 = 1026")
    if num1 == 38 and sign == '*' and num2 == 28:
        return("38*28 = 1064")
    if num1 == 38 and sign == '*' and num2 == 29:
        return("38*29 = 1102")
    if num1 == 38 and sign == '*' and num2 == 30:
        return("38*30 = 1140")
    if num1 == 38 and sign == '*' and num2 == 31:
        return("38*31 = 1178")
    if num1 == 38 and sign == '*' and num2 == 32:
        return("38*32 = 1216")
    if num1 == 38 and sign == '*' and num2 == 33:
        return("38*33 = 1254")
    if num1 == 38 and sign == '*' and num2 == 34:
        return("38*34 = 1292")
    if num1 == 38 and sign == '*' and num2 == 35:
        return("38*35 = 1330")
    if num1 == 38 and sign == '*' and num2 == 36:
        return("38*36 = 1368")
    if num1 == 38 and sign == '*' and num2 == 37:
        return("38*37 = 1406")
    if num1 == 38 and sign == '*' and num2 == 38:
        return("38*38 = 1444")
    if num1 == 38 and sign == '*' and num2 == 39:
        return("38*39 = 1482")
    if num1 == 38 and sign == '*' and num2 == 40:
        return("38*40 = 1520")
    if num1 == 38 and sign == '*' and num2 == 41:
        return("38*41 = 1558")
    if num1 == 38 and sign == '*' and num2 == 42:
        return("38*42 = 1596")
    if num1 == 38 and sign == '*' and num2 == 43:
        return("38*43 = 1634")
    if num1 == 38 and sign == '*' and num2 == 44:
        return("38*44 = 1672")
    if num1 == 38 and sign == '*' and num2 == 45:
        return("38*45 = 1710")
    if num1 == 38 and sign == '*' and num2 == 46:
        return("38*46 = 1748")
    if num1 == 38 and sign == '*' and num2 == 47:
        return("38*47 = 1786")
    if num1 == 38 and sign == '*' and num2 == 48:
        return("38*48 = 1824")
    if num1 == 38 and sign == '*' and num2 == 49:
        return("38*49 = 1862")
    if num1 == 38 and sign == '*' and num2 == 50:
        return("38*50 = 1900")
    if num1 == 39 and sign == '*' and num2 == 0:
        return("39*0 = 0")
    if num1 == 39 and sign == '*' and num2 == 1:
        return("39*1 = 39")
    if num1 == 39 and sign == '*' and num2 == 2:
        return("39*2 = 78")
    if num1 == 39 and sign == '*' and num2 == 3:
        return("39*3 = 117")
    if num1 == 39 and sign == '*' and num2 == 4:
        return("39*4 = 156")
    if num1 == 39 and sign == '*' and num2 == 5:
        return("39*5 = 195")
    if num1 == 39 and sign == '*' and num2 == 6:
        return("39*6 = 234")
    if num1 == 39 and sign == '*' and num2 == 7:
        return("39*7 = 273")
    if num1 == 39 and sign == '*' and num2 == 8:
        return("39*8 = 312")
    if num1 == 39 and sign == '*' and num2 == 9:
        return("39*9 = 351")
    if num1 == 39 and sign == '*' and num2 == 10:
        return("39*10 = 390")
    if num1 == 39 and sign == '*' and num2 == 11:
        return("39*11 = 429")
    if num1 == 39 and sign == '*' and num2 == 12:
        return("39*12 = 468")
    if num1 == 39 and sign == '*' and num2 == 13:
        return("39*13 = 507")
    if num1 == 39 and sign == '*' and num2 == 14:
        return("39*14 = 546")
    if num1 == 39 and sign == '*' and num2 == 15:
        return("39*15 = 585")
    if num1 == 39 and sign == '*' and num2 == 16:
        return("39*16 = 624")
    if num1 == 39 and sign == '*' and num2 == 17:
        return("39*17 = 663")
    if num1 == 39 and sign == '*' and num2 == 18:
        return("39*18 = 702")
    if num1 == 39 and sign == '*' and num2 == 19:
        return("39*19 = 741")
    if num1 == 39 and sign == '*' and num2 == 20:
        return("39*20 = 780")
    if num1 == 39 and sign == '*' and num2 == 21:
        return("39*21 = 819")
    if num1 == 39 and sign == '*' and num2 == 22:
        return("39*22 = 858")
    if num1 == 39 and sign == '*' and num2 == 23:
        return("39*23 = 897")
    if num1 == 39 and sign == '*' and num2 == 24:
        return("39*24 = 936")
    if num1 == 39 and sign == '*' and num2 == 25:
        return("39*25 = 975")
    if num1 == 39 and sign == '*' and num2 == 26:
        return("39*26 = 1014")
    if num1 == 39 and sign == '*' and num2 == 27:
        return("39*27 = 1053")
    if num1 == 39 and sign == '*' and num2 == 28:
        return("39*28 = 1092")
    if num1 == 39 and sign == '*' and num2 == 29:
        return("39*29 = 1131")
    if num1 == 39 and sign == '*' and num2 == 30:
        return("39*30 = 1170")
    if num1 == 39 and sign == '*' and num2 == 31:
        return("39*31 = 1209")
    if num1 == 39 and sign == '*' and num2 == 32:
        return("39*32 = 1248")
    if num1 == 39 and sign == '*' and num2 == 33:
        return("39*33 = 1287")
    if num1 == 39 and sign == '*' and num2 == 34:
        return("39*34 = 1326")
    if num1 == 39 and sign == '*' and num2 == 35:
        return("39*35 = 1365")
    if num1 == 39 and sign == '*' and num2 == 36:
        return("39*36 = 1404")
    if num1 == 39 and sign == '*' and num2 == 37:
        return("39*37 = 1443")
    if num1 == 39 and sign == '*' and num2 == 38:
        return("39*38 = 1482")
    if num1 == 39 and sign == '*' and num2 == 39:
        return("39*39 = 1521")
    if num1 == 39 and sign == '*' and num2 == 40:
        return("39*40 = 1560")
    if num1 == 39 and sign == '*' and num2 == 41:
        return("39*41 = 1599")
    if num1 == 39 and sign == '*' and num2 == 42:
        return("39*42 = 1638")
    if num1 == 39 and sign == '*' and num2 == 43:
        return("39*43 = 1677")
    if num1 == 39 and sign == '*' and num2 == 44:
        return("39*44 = 1716")
    if num1 == 39 and sign == '*' and num2 == 45:
        return("39*45 = 1755")
    if num1 == 39 and sign == '*' and num2 == 46:
        return("39*46 = 1794")
    if num1 == 39 and sign == '*' and num2 == 47:
        return("39*47 = 1833")
    if num1 == 39 and sign == '*' and num2 == 48:
        return("39*48 = 1872")
    if num1 == 39 and sign == '*' and num2 == 49:
        return("39*49 = 1911")
    if num1 == 39 and sign == '*' and num2 == 50:
        return("39*50 = 1950")
    if num1 == 40 and sign == '*' and num2 == 0:
        return("40*0 = 0")
    if num1 == 40 and sign == '*' and num2 == 1:
        return("40*1 = 40")
    if num1 == 40 and sign == '*' and num2 == 2:
        return("40*2 = 80")
    if num1 == 40 and sign == '*' and num2 == 3:
        return("40*3 = 120")
    if num1 == 40 and sign == '*' and num2 == 4:
        return("40*4 = 160")
    if num1 == 40 and sign == '*' and num2 == 5:
        return("40*5 = 200")
    if num1 == 40 and sign == '*' and num2 == 6:
        return("40*6 = 240")
    if num1 == 40 and sign == '*' and num2 == 7:
        return("40*7 = 280")
    if num1 == 40 and sign == '*' and num2 == 8:
        return("40*8 = 320")
    if num1 == 40 and sign == '*' and num2 == 9:
        return("40*9 = 360")
    if num1 == 40 and sign == '*' and num2 == 10:
        return("40*10 = 400")
    if num1 == 40 and sign == '*' and num2 == 11:
        return("40*11 = 440")
    if num1 == 40 and sign == '*' and num2 == 12:
        return("40*12 = 480")
    if num1 == 40 and sign == '*' and num2 == 13:
        return("40*13 = 520")
    if num1 == 40 and sign == '*' and num2 == 14:
        return("40*14 = 560")
    if num1 == 40 and sign == '*' and num2 == 15:
        return("40*15 = 600")
    if num1 == 40 and sign == '*' and num2 == 16:
        return("40*16 = 640")
    if num1 == 40 and sign == '*' and num2 == 17:
        return("40*17 = 680")
    if num1 == 40 and sign == '*' and num2 == 18:
        return("40*18 = 720")
    if num1 == 40 and sign == '*' and num2 == 19:
        return("40*19 = 760")
    if num1 == 40 and sign == '*' and num2 == 20:
        return("40*20 = 800")
    if num1 == 40 and sign == '*' and num2 == 21:
        return("40*21 = 840")
    if num1 == 40 and sign == '*' and num2 == 22:
        return("40*22 = 880")
    if num1 == 40 and sign == '*' and num2 == 23:
        return("40*23 = 920")
    if num1 == 40 and sign == '*' and num2 == 24:
        return("40*24 = 960")
    if num1 == 40 and sign == '*' and num2 == 25:
        return("40*25 = 1000")
    if num1 == 40 and sign == '*' and num2 == 26:
        return("40*26 = 1040")
    if num1 == 40 and sign == '*' and num2 == 27:
        return("40*27 = 1080")
    if num1 == 40 and sign == '*' and num2 == 28:
        return("40*28 = 1120")
    if num1 == 40 and sign == '*' and num2 == 29:
        return("40*29 = 1160")
    if num1 == 40 and sign == '*' and num2 == 30:
        return("40*30 = 1200")
    if num1 == 40 and sign == '*' and num2 == 31:
        return("40*31 = 1240")
    if num1 == 40 and sign == '*' and num2 == 32:
        return("40*32 = 1280")
    if num1 == 40 and sign == '*' and num2 == 33:
        return("40*33 = 1320")
    if num1 == 40 and sign == '*' and num2 == 34:
        return("40*34 = 1360")
    if num1 == 40 and sign == '*' and num2 == 35:
        return("40*35 = 1400")
    if num1 == 40 and sign == '*' and num2 == 36:
        return("40*36 = 1440")
    if num1 == 40 and sign == '*' and num2 == 37:
        return("40*37 = 1480")
    if num1 == 40 and sign == '*' and num2 == 38:
        return("40*38 = 1520")
    if num1 == 40 and sign == '*' and num2 == 39:
        return("40*39 = 1560")
    if num1 == 40 and sign == '*' and num2 == 40:
        return("40*40 = 1600")
    if num1 == 40 and sign == '*' and num2 == 41:
        return("40*41 = 1640")
    if num1 == 40 and sign == '*' and num2 == 42:
        return("40*42 = 1680")
    if num1 == 40 and sign == '*' and num2 == 43:
        return("40*43 = 1720")
    if num1 == 40 and sign == '*' and num2 == 44:
        return("40*44 = 1760")
    if num1 == 40 and sign == '*' and num2 == 45:
        return("40*45 = 1800")
    if num1 == 40 and sign == '*' and num2 == 46:
        return("40*46 = 1840")
    if num1 == 40 and sign == '*' and num2 == 47:
        return("40*47 = 1880")
    if num1 == 40 and sign == '*' and num2 == 48:
        return("40*48 = 1920")
    if num1 == 40 and sign == '*' and num2 == 49:
        return("40*49 = 1960")
    if num1 == 40 and sign == '*' and num2 == 50:
        return("40*50 = 2000")
    if num1 == 41 and sign == '*' and num2 == 0:
        return("41*0 = 0")
    if num1 == 41 and sign == '*' and num2 == 1:
        return("41*1 = 41")
    if num1 == 41 and sign == '*' and num2 == 2:
        return("41*2 = 82")
    if num1 == 41 and sign == '*' and num2 == 3:
        return("41*3 = 123")
    if num1 == 41 and sign == '*' and num2 == 4:
        return("41*4 = 164")
    if num1 == 41 and sign == '*' and num2 == 5:
        return("41*5 = 205")
    if num1 == 41 and sign == '*' and num2 == 6:
        return("41*6 = 246")
    if num1 == 41 and sign == '*' and num2 == 7:
        return("41*7 = 287")
    if num1 == 41 and sign == '*' and num2 == 8:
        return("41*8 = 328")
    if num1 == 41 and sign == '*' and num2 == 9:
        return("41*9 = 369")
    if num1 == 41 and sign == '*' and num2 == 10:
        return("41*10 = 410")
    if num1 == 41 and sign == '*' and num2 == 11:
        return("41*11 = 451")
    if num1 == 41 and sign == '*' and num2 == 12:
        return("41*12 = 492")
    if num1 == 41 and sign == '*' and num2 == 13:
        return("41*13 = 533")
    if num1 == 41 and sign == '*' and num2 == 14:
        return("41*14 = 574")
    if num1 == 41 and sign == '*' and num2 == 15:
        return("41*15 = 615")
    if num1 == 41 and sign == '*' and num2 == 16:
        return("41*16 = 656")
    if num1 == 41 and sign == '*' and num2 == 17:
        return("41*17 = 697")
    if num1 == 41 and sign == '*' and num2 == 18:
        return("41*18 = 738")
    if num1 == 41 and sign == '*' and num2 == 19:
        return("41*19 = 779")
    if num1 == 41 and sign == '*' and num2 == 20:
        return("41*20 = 820")
    if num1 == 41 and sign == '*' and num2 == 21:
        return("41*21 = 861")
    if num1 == 41 and sign == '*' and num2 == 22:
        return("41*22 = 902")
    if num1 == 41 and sign == '*' and num2 == 23:
        return("41*23 = 943")
    if num1 == 41 and sign == '*' and num2 == 24:
        return("41*24 = 984")
    if num1 == 41 and sign == '*' and num2 == 25:
        return("41*25 = 1025")
    if num1 == 41 and sign == '*' and num2 == 26:
        return("41*26 = 1066")
    if num1 == 41 and sign == '*' and num2 == 27:
        return("41*27 = 1107")
    if num1 == 41 and sign == '*' and num2 == 28:
        return("41*28 = 1148")
    if num1 == 41 and sign == '*' and num2 == 29:
        return("41*29 = 1189")
    if num1 == 41 and sign == '*' and num2 == 30:
        return("41*30 = 1230")
    if num1 == 41 and sign == '*' and num2 == 31:
        return("41*31 = 1271")
    if num1 == 41 and sign == '*' and num2 == 32:
        return("41*32 = 1312")
    if num1 == 41 and sign == '*' and num2 == 33:
        return("41*33 = 1353")
    if num1 == 41 and sign == '*' and num2 == 34:
        return("41*34 = 1394")
    if num1 == 41 and sign == '*' and num2 == 35:
        return("41*35 = 1435")
    if num1 == 41 and sign == '*' and num2 == 36:
        return("41*36 = 1476")
    if num1 == 41 and sign == '*' and num2 == 37:
        return("41*37 = 1517")
    if num1 == 41 and sign == '*' and num2 == 38:
        return("41*38 = 1558")
    if num1 == 41 and sign == '*' and num2 == 39:
        return("41*39 = 1599")
    if num1 == 41 and sign == '*' and num2 == 40:
        return("41*40 = 1640")
    if num1 == 41 and sign == '*' and num2 == 41:
        return("41*41 = 1681")
    if num1 == 41 and sign == '*' and num2 == 42:
        return("41*42 = 1722")
    if num1 == 41 and sign == '*' and num2 == 43:
        return("41*43 = 1763")
    if num1 == 41 and sign == '*' and num2 == 44:
        return("41*44 = 1804")
    if num1 == 41 and sign == '*' and num2 == 45:
        return("41*45 = 1845")
    if num1 == 41 and sign == '*' and num2 == 46:
        return("41*46 = 1886")
    if num1 == 41 and sign == '*' and num2 == 47:
        return("41*47 = 1927")
    if num1 == 41 and sign == '*' and num2 == 48:
        return("41*48 = 1968")
    if num1 == 41 and sign == '*' and num2 == 49:
        return("41*49 = 2009")
    if num1 == 41 and sign == '*' and num2 == 50:
        return("41*50 = 2050")
    if num1 == 42 and sign == '*' and num2 == 0:
        return("42*0 = 0")
    if num1 == 42 and sign == '*' and num2 == 1:
        return("42*1 = 42")
    if num1 == 42 and sign == '*' and num2 == 2:
        return("42*2 = 84")
    if num1 == 42 and sign == '*' and num2 == 3:
        return("42*3 = 126")
    if num1 == 42 and sign == '*' and num2 == 4:
        return("42*4 = 168")
    if num1 == 42 and sign == '*' and num2 == 5:
        return("42*5 = 210")
    if num1 == 42 and sign == '*' and num2 == 6:
        return("42*6 = 252")
    if num1 == 42 and sign == '*' and num2 == 7:
        return("42*7 = 294")
    if num1 == 42 and sign == '*' and num2 == 8:
        return("42*8 = 336")
    if num1 == 42 and sign == '*' and num2 == 9:
        return("42*9 = 378")
    if num1 == 42 and sign == '*' and num2 == 10:
        return("42*10 = 420")
    if num1 == 42 and sign == '*' and num2 == 11:
        return("42*11 = 462")
    if num1 == 42 and sign == '*' and num2 == 12:
        return("42*12 = 504")
    if num1 == 42 and sign == '*' and num2 == 13:
        return("42*13 = 546")
    if num1 == 42 and sign == '*' and num2 == 14:
        return("42*14 = 588")
    if num1 == 42 and sign == '*' and num2 == 15:
        return("42*15 = 630")
    if num1 == 42 and sign == '*' and num2 == 16:
        return("42*16 = 672")
    if num1 == 42 and sign == '*' and num2 == 17:
        return("42*17 = 714")
    if num1 == 42 and sign == '*' and num2 == 18:
        return("42*18 = 756")
    if num1 == 42 and sign == '*' and num2 == 19:
        return("42*19 = 798")
    if num1 == 42 and sign == '*' and num2 == 20:
        return("42*20 = 840")
    if num1 == 42 and sign == '*' and num2 == 21:
        return("42*21 = 882")
    if num1 == 42 and sign == '*' and num2 == 22:
        return("42*22 = 924")
    if num1 == 42 and sign == '*' and num2 == 23:
        return("42*23 = 966")
    if num1 == 42 and sign == '*' and num2 == 24:
        return("42*24 = 1008")
    if num1 == 42 and sign == '*' and num2 == 25:
        return("42*25 = 1050")
    if num1 == 42 and sign == '*' and num2 == 26:
        return("42*26 = 1092")
    if num1 == 42 and sign == '*' and num2 == 27:
        return("42*27 = 1134")
    if num1 == 42 and sign == '*' and num2 == 28:
        return("42*28 = 1176")
    if num1 == 42 and sign == '*' and num2 == 29:
        return("42*29 = 1218")
    if num1 == 42 and sign == '*' and num2 == 30:
        return("42*30 = 1260")
    if num1 == 42 and sign == '*' and num2 == 31:
        return("42*31 = 1302")
    if num1 == 42 and sign == '*' and num2 == 32:
        return("42*32 = 1344")
    if num1 == 42 and sign == '*' and num2 == 33:
        return("42*33 = 1386")
    if num1 == 42 and sign == '*' and num2 == 34:
        return("42*34 = 1428")
    if num1 == 42 and sign == '*' and num2 == 35:
        return("42*35 = 1470")
    if num1 == 42 and sign == '*' and num2 == 36:
        return("42*36 = 1512")
    if num1 == 42 and sign == '*' and num2 == 37:
        return("42*37 = 1554")
    if num1 == 42 and sign == '*' and num2 == 38:
        return("42*38 = 1596")
    if num1 == 42 and sign == '*' and num2 == 39:
        return("42*39 = 1638")
    if num1 == 42 and sign == '*' and num2 == 40:
        return("42*40 = 1680")
    if num1 == 42 and sign == '*' and num2 == 41:
        return("42*41 = 1722")
    if num1 == 42 and sign == '*' and num2 == 42:
        return("42*42 = 1764")
    if num1 == 42 and sign == '*' and num2 == 43:
        return("42*43 = 1806")
    if num1 == 42 and sign == '*' and num2 == 44:
        return("42*44 = 1848")
    if num1 == 42 and sign == '*' and num2 == 45:
        return("42*45 = 1890")
    if num1 == 42 and sign == '*' and num2 == 46:
        return("42*46 = 1932")
    if num1 == 42 and sign == '*' and num2 == 47:
        return("42*47 = 1974")
    if num1 == 42 and sign == '*' and num2 == 48:
        return("42*48 = 2016")
    if num1 == 42 and sign == '*' and num2 == 49:
        return("42*49 = 2058")
    if num1 == 42 and sign == '*' and num2 == 50:
        return("42*50 = 2100")
    if num1 == 43 and sign == '*' and num2 == 0:
        return("43*0 = 0")
    if num1 == 43 and sign == '*' and num2 == 1:
        return("43*1 = 43")
    if num1 == 43 and sign == '*' and num2 == 2:
        return("43*2 = 86")
    if num1 == 43 and sign == '*' and num2 == 3:
        return("43*3 = 129")
    if num1 == 43 and sign == '*' and num2 == 4:
        return("43*4 = 172")
    if num1 == 43 and sign == '*' and num2 == 5:
        return("43*5 = 215")
    if num1 == 43 and sign == '*' and num2 == 6:
        return("43*6 = 258")
    if num1 == 43 and sign == '*' and num2 == 7:
        return("43*7 = 301")
    if num1 == 43 and sign == '*' and num2 == 8:
        return("43*8 = 344")
    if num1 == 43 and sign == '*' and num2 == 9:
        return("43*9 = 387")
    if num1 == 43 and sign == '*' and num2 == 10:
        return("43*10 = 430")
    if num1 == 43 and sign == '*' and num2 == 11:
        return("43*11 = 473")
    if num1 == 43 and sign == '*' and num2 == 12:
        return("43*12 = 516")
    if num1 == 43 and sign == '*' and num2 == 13:
        return("43*13 = 559")
    if num1 == 43 and sign == '*' and num2 == 14:
        return("43*14 = 602")
    if num1 == 43 and sign == '*' and num2 == 15:
        return("43*15 = 645")
    if num1 == 43 and sign == '*' and num2 == 16:
        return("43*16 = 688")
    if num1 == 43 and sign == '*' and num2 == 17:
        return("43*17 = 731")
    if num1 == 43 and sign == '*' and num2 == 18:
        return("43*18 = 774")
    if num1 == 43 and sign == '*' and num2 == 19:
        return("43*19 = 817")
    if num1 == 43 and sign == '*' and num2 == 20:
        return("43*20 = 860")
    if num1 == 43 and sign == '*' and num2 == 21:
        return("43*21 = 903")
    if num1 == 43 and sign == '*' and num2 == 22:
        return("43*22 = 946")
    if num1 == 43 and sign == '*' and num2 == 23:
        return("43*23 = 989")
    if num1 == 43 and sign == '*' and num2 == 24:
        return("43*24 = 1032")
    if num1 == 43 and sign == '*' and num2 == 25:
        return("43*25 = 1075")
    if num1 == 43 and sign == '*' and num2 == 26:
        return("43*26 = 1118")
    if num1 == 43 and sign == '*' and num2 == 27:
        return("43*27 = 1161")
    if num1 == 43 and sign == '*' and num2 == 28:
        return("43*28 = 1204")
    if num1 == 43 and sign == '*' and num2 == 29:
        return("43*29 = 1247")
    if num1 == 43 and sign == '*' and num2 == 30:
        return("43*30 = 1290")
    if num1 == 43 and sign == '*' and num2 == 31:
        return("43*31 = 1333")
    if num1 == 43 and sign == '*' and num2 == 32:
        return("43*32 = 1376")
    if num1 == 43 and sign == '*' and num2 == 33:
        return("43*33 = 1419")
    if num1 == 43 and sign == '*' and num2 == 34:
        return("43*34 = 1462")
    if num1 == 43 and sign == '*' and num2 == 35:
        return("43*35 = 1505")
    if num1 == 43 and sign == '*' and num2 == 36:
        return("43*36 = 1548")
    if num1 == 43 and sign == '*' and num2 == 37:
        return("43*37 = 1591")
    if num1 == 43 and sign == '*' and num2 == 38:
        return("43*38 = 1634")
    if num1 == 43 and sign == '*' and num2 == 39:
        return("43*39 = 1677")
    if num1 == 43 and sign == '*' and num2 == 40:
        return("43*40 = 1720")
    if num1 == 43 and sign == '*' and num2 == 41:
        return("43*41 = 1763")
    if num1 == 43 and sign == '*' and num2 == 42:
        return("43*42 = 1806")
    if num1 == 43 and sign == '*' and num2 == 43:
        return("43*43 = 1849")
    if num1 == 43 and sign == '*' and num2 == 44:
        return("43*44 = 1892")
    if num1 == 43 and sign == '*' and num2 == 45:
        return("43*45 = 1935")
    if num1 == 43 and sign == '*' and num2 == 46:
        return("43*46 = 1978")
    if num1 == 43 and sign == '*' and num2 == 47:
        return("43*47 = 2021")
    if num1 == 43 and sign == '*' and num2 == 48:
        return("43*48 = 2064")
    if num1 == 43 and sign == '*' and num2 == 49:
        return("43*49 = 2107")
    if num1 == 43 and sign == '*' and num2 == 50:
        return("43*50 = 2150")
    if num1 == 44 and sign == '*' and num2 == 0:
        return("44*0 = 0")
    if num1 == 44 and sign == '*' and num2 == 1:
        return("44*1 = 44")
    if num1 == 44 and sign == '*' and num2 == 2:
        return("44*2 = 88")
    if num1 == 44 and sign == '*' and num2 == 3:
        return("44*3 = 132")
    if num1 == 44 and sign == '*' and num2 == 4:
        return("44*4 = 176")
    if num1 == 44 and sign == '*' and num2 == 5:
        return("44*5 = 220")
    if num1 == 44 and sign == '*' and num2 == 6:
        return("44*6 = 264")
    if num1 == 44 and sign == '*' and num2 == 7:
        return("44*7 = 308")
    if num1 == 44 and sign == '*' and num2 == 8:
        return("44*8 = 352")
    if num1 == 44 and sign == '*' and num2 == 9:
        return("44*9 = 396")
    if num1 == 44 and sign == '*' and num2 == 10:
        return("44*10 = 440")
    if num1 == 44 and sign == '*' and num2 == 11:
        return("44*11 = 484")
    if num1 == 44 and sign == '*' and num2 == 12:
        return("44*12 = 528")
    if num1 == 44 and sign == '*' and num2 == 13:
        return("44*13 = 572")
    if num1 == 44 and sign == '*' and num2 == 14:
        return("44*14 = 616")
    if num1 == 44 and sign == '*' and num2 == 15:
        return("44*15 = 660")
    if num1 == 44 and sign == '*' and num2 == 16:
        return("44*16 = 704")
    if num1 == 44 and sign == '*' and num2 == 17:
        return("44*17 = 748")
    if num1 == 44 and sign == '*' and num2 == 18:
        return("44*18 = 792")
    if num1 == 44 and sign == '*' and num2 == 19:
        return("44*19 = 836")
    if num1 == 44 and sign == '*' and num2 == 20:
        return("44*20 = 880")
    if num1 == 44 and sign == '*' and num2 == 21:
        return("44*21 = 924")
    if num1 == 44 and sign == '*' and num2 == 22:
        return("44*22 = 968")
    if num1 == 44 and sign == '*' and num2 == 23:
        return("44*23 = 1012")
    if num1 == 44 and sign == '*' and num2 == 24:
        return("44*24 = 1056")
    if num1 == 44 and sign == '*' and num2 == 25:
        return("44*25 = 1100")
    if num1 == 44 and sign == '*' and num2 == 26:
        return("44*26 = 1144")
    if num1 == 44 and sign == '*' and num2 == 27:
        return("44*27 = 1188")
    if num1 == 44 and sign == '*' and num2 == 28:
        return("44*28 = 1232")
    if num1 == 44 and sign == '*' and num2 == 29:
        return("44*29 = 1276")
    if num1 == 44 and sign == '*' and num2 == 30:
        return("44*30 = 1320")
    if num1 == 44 and sign == '*' and num2 == 31:
        return("44*31 = 1364")
    if num1 == 44 and sign == '*' and num2 == 32:
        return("44*32 = 1408")
    if num1 == 44 and sign == '*' and num2 == 33:
        return("44*33 = 1452")
    if num1 == 44 and sign == '*' and num2 == 34:
        return("44*34 = 1496")
    if num1 == 44 and sign == '*' and num2 == 35:
        return("44*35 = 1540")
    if num1 == 44 and sign == '*' and num2 == 36:
        return("44*36 = 1584")
    if num1 == 44 and sign == '*' and num2 == 37:
        return("44*37 = 1628")
    if num1 == 44 and sign == '*' and num2 == 38:
        return("44*38 = 1672")
    if num1 == 44 and sign == '*' and num2 == 39:
        return("44*39 = 1716")
    if num1 == 44 and sign == '*' and num2 == 40:
        return("44*40 = 1760")
    if num1 == 44 and sign == '*' and num2 == 41:
        return("44*41 = 1804")
    if num1 == 44 and sign == '*' and num2 == 42:
        return("44*42 = 1848")
    if num1 == 44 and sign == '*' and num2 == 43:
        return("44*43 = 1892")
    if num1 == 44 and sign == '*' and num2 == 44:
        return("44*44 = 1936")
    if num1 == 44 and sign == '*' and num2 == 45:
        return("44*45 = 1980")
    if num1 == 44 and sign == '*' and num2 == 46:
        return("44*46 = 2024")
    if num1 == 44 and sign == '*' and num2 == 47:
        return("44*47 = 2068")
    if num1 == 44 and sign == '*' and num2 == 48:
        return("44*48 = 2112")
    if num1 == 44 and sign == '*' and num2 == 49:
        return("44*49 = 2156")
    if num1 == 44 and sign == '*' and num2 == 50:
        return("44*50 = 2200")
    if num1 == 45 and sign == '*' and num2 == 0:
        return("45*0 = 0")
    if num1 == 45 and sign == '*' and num2 == 1:
        return("45*1 = 45")
    if num1 == 45 and sign == '*' and num2 == 2:
        return("45*2 = 90")
    if num1 == 45 and sign == '*' and num2 == 3:
        return("45*3 = 135")
    if num1 == 45 and sign == '*' and num2 == 4:
        return("45*4 = 180")
    if num1 == 45 and sign == '*' and num2 == 5:
        return("45*5 = 225")
    if num1 == 45 and sign == '*' and num2 == 6:
        return("45*6 = 270")
    if num1 == 45 and sign == '*' and num2 == 7:
        return("45*7 = 315")
    if num1 == 45 and sign == '*' and num2 == 8:
        return("45*8 = 360")
    if num1 == 45 and sign == '*' and num2 == 9:
        return("45*9 = 405")
    if num1 == 45 and sign == '*' and num2 == 10:
        return("45*10 = 450")
    if num1 == 45 and sign == '*' and num2 == 11:
        return("45*11 = 495")
    if num1 == 45 and sign == '*' and num2 == 12:
        return("45*12 = 540")
    if num1 == 45 and sign == '*' and num2 == 13:
        return("45*13 = 585")
    if num1 == 45 and sign == '*' and num2 == 14:
        return("45*14 = 630")
    if num1 == 45 and sign == '*' and num2 == 15:
        return("45*15 = 675")
    if num1 == 45 and sign == '*' and num2 == 16:
        return("45*16 = 720")
    if num1 == 45 and sign == '*' and num2 == 17:
        return("45*17 = 765")
    if num1 == 45 and sign == '*' and num2 == 18:
        return("45*18 = 810")
    if num1 == 45 and sign == '*' and num2 == 19:
        return("45*19 = 855")
    if num1 == 45 and sign == '*' and num2 == 20:
        return("45*20 = 900")
    if num1 == 45 and sign == '*' and num2 == 21:
        return("45*21 = 945")
    if num1 == 45 and sign == '*' and num2 == 22:
        return("45*22 = 990")
    if num1 == 45 and sign == '*' and num2 == 23:
        return("45*23 = 1035")
    if num1 == 45 and sign == '*' and num2 == 24:
        return("45*24 = 1080")
    if num1 == 45 and sign == '*' and num2 == 25:
        return("45*25 = 1125")
    if num1 == 45 and sign == '*' and num2 == 26:
        return("45*26 = 1170")
    if num1 == 45 and sign == '*' and num2 == 27:
        return("45*27 = 1215")
    if num1 == 45 and sign == '*' and num2 == 28:
        return("45*28 = 1260")
    if num1 == 45 and sign == '*' and num2 == 29:
        return("45*29 = 1305")
    if num1 == 45 and sign == '*' and num2 == 30:
        return("45*30 = 1350")
    if num1 == 45 and sign == '*' and num2 == 31:
        return("45*31 = 1395")
    if num1 == 45 and sign == '*' and num2 == 32:
        return("45*32 = 1440")
    if num1 == 45 and sign == '*' and num2 == 33:
        return("45*33 = 1485")
    if num1 == 45 and sign == '*' and num2 == 34:
        return("45*34 = 1530")
    if num1 == 45 and sign == '*' and num2 == 35:
        return("45*35 = 1575")
    if num1 == 45 and sign == '*' and num2 == 36:
        return("45*36 = 1620")
    if num1 == 45 and sign == '*' and num2 == 37:
        return("45*37 = 1665")
    if num1 == 45 and sign == '*' and num2 == 38:
        return("45*38 = 1710")
    if num1 == 45 and sign == '*' and num2 == 39:
        return("45*39 = 1755")
    if num1 == 45 and sign == '*' and num2 == 40:
        return("45*40 = 1800")
    if num1 == 45 and sign == '*' and num2 == 41:
        return("45*41 = 1845")
    if num1 == 45 and sign == '*' and num2 == 42:
        return("45*42 = 1890")
    if num1 == 45 and sign == '*' and num2 == 43:
        return("45*43 = 1935")
    if num1 == 45 and sign == '*' and num2 == 44:
        return("45*44 = 1980")
    if num1 == 45 and sign == '*' and num2 == 45:
        return("45*45 = 2025")
    if num1 == 45 and sign == '*' and num2 == 46:
        return("45*46 = 2070")
    if num1 == 45 and sign == '*' and num2 == 47:
        return("45*47 = 2115")
    if num1 == 45 and sign == '*' and num2 == 48:
        return("45*48 = 2160")
    if num1 == 45 and sign == '*' and num2 == 49:
        return("45*49 = 2205")
    if num1 == 45 and sign == '*' and num2 == 50:
        return("45*50 = 2250")
    if num1 == 46 and sign == '*' and num2 == 0:
        return("46*0 = 0")
    if num1 == 46 and sign == '*' and num2 == 1:
        return("46*1 = 46")
    if num1 == 46 and sign == '*' and num2 == 2:
        return("46*2 = 92")
    if num1 == 46 and sign == '*' and num2 == 3:
        return("46*3 = 138")
    if num1 == 46 and sign == '*' and num2 == 4:
        return("46*4 = 184")
    if num1 == 46 and sign == '*' and num2 == 5:
        return("46*5 = 230")
    if num1 == 46 and sign == '*' and num2 == 6:
        return("46*6 = 276")
    if num1 == 46 and sign == '*' and num2 == 7:
        return("46*7 = 322")
    if num1 == 46 and sign == '*' and num2 == 8:
        return("46*8 = 368")
    if num1 == 46 and sign == '*' and num2 == 9:
        return("46*9 = 414")
    if num1 == 46 and sign == '*' and num2 == 10:
        return("46*10 = 460")
    if num1 == 46 and sign == '*' and num2 == 11:
        return("46*11 = 506")
    if num1 == 46 and sign == '*' and num2 == 12:
        return("46*12 = 552")
    if num1 == 46 and sign == '*' and num2 == 13:
        return("46*13 = 598")
    if num1 == 46 and sign == '*' and num2 == 14:
        return("46*14 = 644")
    if num1 == 46 and sign == '*' and num2 == 15:
        return("46*15 = 690")
    if num1 == 46 and sign == '*' and num2 == 16:
        return("46*16 = 736")
    if num1 == 46 and sign == '*' and num2 == 17:
        return("46*17 = 782")
    if num1 == 46 and sign == '*' and num2 == 18:
        return("46*18 = 828")
    if num1 == 46 and sign == '*' and num2 == 19:
        return("46*19 = 874")
    if num1 == 46 and sign == '*' and num2 == 20:
        return("46*20 = 920")
    if num1 == 46 and sign == '*' and num2 == 21:
        return("46*21 = 966")
    if num1 == 46 and sign == '*' and num2 == 22:
        return("46*22 = 1012")
    if num1 == 46 and sign == '*' and num2 == 23:
        return("46*23 = 1058")
    if num1 == 46 and sign == '*' and num2 == 24:
        return("46*24 = 1104")
    if num1 == 46 and sign == '*' and num2 == 25:
        return("46*25 = 1150")
    if num1 == 46 and sign == '*' and num2 == 26:
        return("46*26 = 1196")
    if num1 == 46 and sign == '*' and num2 == 27:
        return("46*27 = 1242")
    if num1 == 46 and sign == '*' and num2 == 28:
        return("46*28 = 1288")
    if num1 == 46 and sign == '*' and num2 == 29:
        return("46*29 = 1334")
    if num1 == 46 and sign == '*' and num2 == 30:
        return("46*30 = 1380")
    if num1 == 46 and sign == '*' and num2 == 31:
        return("46*31 = 1426")
    if num1 == 46 and sign == '*' and num2 == 32:
        return("46*32 = 1472")
    if num1 == 46 and sign == '*' and num2 == 33:
        return("46*33 = 1518")
    if num1 == 46 and sign == '*' and num2 == 34:
        return("46*34 = 1564")
    if num1 == 46 and sign == '*' and num2 == 35:
        return("46*35 = 1610")
    if num1 == 46 and sign == '*' and num2 == 36:
        return("46*36 = 1656")
    if num1 == 46 and sign == '*' and num2 == 37:
        return("46*37 = 1702")
    if num1 == 46 and sign == '*' and num2 == 38:
        return("46*38 = 1748")
    if num1 == 46 and sign == '*' and num2 == 39:
        return("46*39 = 1794")
    if num1 == 46 and sign == '*' and num2 == 40:
        return("46*40 = 1840")
    if num1 == 46 and sign == '*' and num2 == 41:
        return("46*41 = 1886")
    if num1 == 46 and sign == '*' and num2 == 42:
        return("46*42 = 1932")
    if num1 == 46 and sign == '*' and num2 == 43:
        return("46*43 = 1978")
    if num1 == 46 and sign == '*' and num2 == 44:
        return("46*44 = 2024")
    if num1 == 46 and sign == '*' and num2 == 45:
        return("46*45 = 2070")
    if num1 == 46 and sign == '*' and num2 == 46:
        return("46*46 = 2116")
    if num1 == 46 and sign == '*' and num2 == 47:
        return("46*47 = 2162")
    if num1 == 46 and sign == '*' and num2 == 48:
        return("46*48 = 2208")
    if num1 == 46 and sign == '*' and num2 == 49:
        return("46*49 = 2254")
    if num1 == 46 and sign == '*' and num2 == 50:
        return("46*50 = 2300")
    if num1 == 47 and sign == '*' and num2 == 0:
        return("47*0 = 0")
    if num1 == 47 and sign == '*' and num2 == 1:
        return("47*1 = 47")
    if num1 == 47 and sign == '*' and num2 == 2:
        return("47*2 = 94")
    if num1 == 47 and sign == '*' and num2 == 3:
        return("47*3 = 141")
    if num1 == 47 and sign == '*' and num2 == 4:
        return("47*4 = 188")
    if num1 == 47 and sign == '*' and num2 == 5:
        return("47*5 = 235")
    if num1 == 47 and sign == '*' and num2 == 6:
        return("47*6 = 282")
    if num1 == 47 and sign == '*' and num2 == 7:
        return("47*7 = 329")
    if num1 == 47 and sign == '*' and num2 == 8:
        return("47*8 = 376")
    if num1 == 47 and sign == '*' and num2 == 9:
        return("47*9 = 423")
    if num1 == 47 and sign == '*' and num2 == 10:
        return("47*10 = 470")
    if num1 == 47 and sign == '*' and num2 == 11:
        return("47*11 = 517")
    if num1 == 47 and sign == '*' and num2 == 12:
        return("47*12 = 564")
    if num1 == 47 and sign == '*' and num2 == 13:
        return("47*13 = 611")
    if num1 == 47 and sign == '*' and num2 == 14:
        return("47*14 = 658")
    if num1 == 47 and sign == '*' and num2 == 15:
        return("47*15 = 705")
    if num1 == 47 and sign == '*' and num2 == 16:
        return("47*16 = 752")
    if num1 == 47 and sign == '*' and num2 == 17:
        return("47*17 = 799")
    if num1 == 47 and sign == '*' and num2 == 18:
        return("47*18 = 846")
    if num1 == 47 and sign == '*' and num2 == 19:
        return("47*19 = 893")
    if num1 == 47 and sign == '*' and num2 == 20:
        return("47*20 = 940")
    if num1 == 47 and sign == '*' and num2 == 21:
        return("47*21 = 987")
    if num1 == 47 and sign == '*' and num2 == 22:
        return("47*22 = 1034")
    if num1 == 47 and sign == '*' and num2 == 23:
        return("47*23 = 1081")
    if num1 == 47 and sign == '*' and num2 == 24:
        return("47*24 = 1128")
    if num1 == 47 and sign == '*' and num2 == 25:
        return("47*25 = 1175")
    if num1 == 47 and sign == '*' and num2 == 26:
        return("47*26 = 1222")
    if num1 == 47 and sign == '*' and num2 == 27:
        return("47*27 = 1269")
    if num1 == 47 and sign == '*' and num2 == 28:
        return("47*28 = 1316")
    if num1 == 47 and sign == '*' and num2 == 29:
        return("47*29 = 1363")
    if num1 == 47 and sign == '*' and num2 == 30:
        return("47*30 = 1410")
    if num1 == 47 and sign == '*' and num2 == 31:
        return("47*31 = 1457")
    if num1 == 47 and sign == '*' and num2 == 32:
        return("47*32 = 1504")
    if num1 == 47 and sign == '*' and num2 == 33:
        return("47*33 = 1551")
    if num1 == 47 and sign == '*' and num2 == 34:
        return("47*34 = 1598")
    if num1 == 47 and sign == '*' and num2 == 35:
        return("47*35 = 1645")
    if num1 == 47 and sign == '*' and num2 == 36:
        return("47*36 = 1692")
    if num1 == 47 and sign == '*' and num2 == 37:
        return("47*37 = 1739")
    if num1 == 47 and sign == '*' and num2 == 38:
        return("47*38 = 1786")
    if num1 == 47 and sign == '*' and num2 == 39:
        return("47*39 = 1833")
    if num1 == 47 and sign == '*' and num2 == 40:
        return("47*40 = 1880")
    if num1 == 47 and sign == '*' and num2 == 41:
        return("47*41 = 1927")
    if num1 == 47 and sign == '*' and num2 == 42:
        return("47*42 = 1974")
    if num1 == 47 and sign == '*' and num2 == 43:
        return("47*43 = 2021")
    if num1 == 47 and sign == '*' and num2 == 44:
        return("47*44 = 2068")
    if num1 == 47 and sign == '*' and num2 == 45:
        return("47*45 = 2115")
    if num1 == 47 and sign == '*' and num2 == 46:
        return("47*46 = 2162")
    if num1 == 47 and sign == '*' and num2 == 47:
        return("47*47 = 2209")
    if num1 == 47 and sign == '*' and num2 == 48:
        return("47*48 = 2256")
    if num1 == 47 and sign == '*' and num2 == 49:
        return("47*49 = 2303")
    if num1 == 47 and sign == '*' and num2 == 50:
        return("47*50 = 2350")
    if num1 == 48 and sign == '*' and num2 == 0:
        return("48*0 = 0")
    if num1 == 48 and sign == '*' and num2 == 1:
        return("48*1 = 48")
    if num1 == 48 and sign == '*' and num2 == 2:
        return("48*2 = 96")
    if num1 == 48 and sign == '*' and num2 == 3:
        return("48*3 = 144")
    if num1 == 48 and sign == '*' and num2 == 4:
        return("48*4 = 192")
    if num1 == 48 and sign == '*' and num2 == 5:
        return("48*5 = 240")
    if num1 == 48 and sign == '*' and num2 == 6:
        return("48*6 = 288")
    if num1 == 48 and sign == '*' and num2 == 7:
        return("48*7 = 336")
    if num1 == 48 and sign == '*' and num2 == 8:
        return("48*8 = 384")
    if num1 == 48 and sign == '*' and num2 == 9:
        return("48*9 = 432")
    if num1 == 48 and sign == '*' and num2 == 10:
        return("48*10 = 480")
    if num1 == 48 and sign == '*' and num2 == 11:
        return("48*11 = 528")
    if num1 == 48 and sign == '*' and num2 == 12:
        return("48*12 = 576")
    if num1 == 48 and sign == '*' and num2 == 13:
        return("48*13 = 624")
    if num1 == 48 and sign == '*' and num2 == 14:
        return("48*14 = 672")
    if num1 == 48 and sign == '*' and num2 == 15:
        return("48*15 = 720")
    if num1 == 48 and sign == '*' and num2 == 16:
        return("48*16 = 768")
    if num1 == 48 and sign == '*' and num2 == 17:
        return("48*17 = 816")
    if num1 == 48 and sign == '*' and num2 == 18:
        return("48*18 = 864")
    if num1 == 48 and sign == '*' and num2 == 19:
        return("48*19 = 912")
    if num1 == 48 and sign == '*' and num2 == 20:
        return("48*20 = 960")
    if num1 == 48 and sign == '*' and num2 == 21:
        return("48*21 = 1008")
    if num1 == 48 and sign == '*' and num2 == 22:
        return("48*22 = 1056")
    if num1 == 48 and sign == '*' and num2 == 23:
        return("48*23 = 1104")
    if num1 == 48 and sign == '*' and num2 == 24:
        return("48*24 = 1152")
    if num1 == 48 and sign == '*' and num2 == 25:
        return("48*25 = 1200")
    if num1 == 48 and sign == '*' and num2 == 26:
        return("48*26 = 1248")
    if num1 == 48 and sign == '*' and num2 == 27:
        return("48*27 = 1296")
    if num1 == 48 and sign == '*' and num2 == 28:
        return("48*28 = 1344")
    if num1 == 48 and sign == '*' and num2 == 29:
        return("48*29 = 1392")
    if num1 == 48 and sign == '*' and num2 == 30:
        return("48*30 = 1440")
    if num1 == 48 and sign == '*' and num2 == 31:
        return("48*31 = 1488")
    if num1 == 48 and sign == '*' and num2 == 32:
        return("48*32 = 1536")
    if num1 == 48 and sign == '*' and num2 == 33:
        return("48*33 = 1584")
    if num1 == 48 and sign == '*' and num2 == 34:
        return("48*34 = 1632")
    if num1 == 48 and sign == '*' and num2 == 35:
        return("48*35 = 1680")
    if num1 == 48 and sign == '*' and num2 == 36:
        return("48*36 = 1728")
    if num1 == 48 and sign == '*' and num2 == 37:
        return("48*37 = 1776")
    if num1 == 48 and sign == '*' and num2 == 38:
        return("48*38 = 1824")
    if num1 == 48 and sign == '*' and num2 == 39:
        return("48*39 = 1872")
    if num1 == 48 and sign == '*' and num2 == 40:
        return("48*40 = 1920")
    if num1 == 48 and sign == '*' and num2 == 41:
        return("48*41 = 1968")
    if num1 == 48 and sign == '*' and num2 == 42:
        return("48*42 = 2016")
    if num1 == 48 and sign == '*' and num2 == 43:
        return("48*43 = 2064")
    if num1 == 48 and sign == '*' and num2 == 44:
        return("48*44 = 2112")
    if num1 == 48 and sign == '*' and num2 == 45:
        return("48*45 = 2160")
    if num1 == 48 and sign == '*' and num2 == 46:
        return("48*46 = 2208")
    if num1 == 48 and sign == '*' and num2 == 47:
        return("48*47 = 2256")
    if num1 == 48 and sign == '*' and num2 == 48:
        return("48*48 = 2304")
    if num1 == 48 and sign == '*' and num2 == 49:
        return("48*49 = 2352")
    if num1 == 48 and sign == '*' and num2 == 50:
        return("48*50 = 2400")
    if num1 == 49 and sign == '*' and num2 == 0:
        return("49*0 = 0")
    if num1 == 49 and sign == '*' and num2 == 1:
        return("49*1 = 49")
    if num1 == 49 and sign == '*' and num2 == 2:
        return("49*2 = 98")
    if num1 == 49 and sign == '*' and num2 == 3:
        return("49*3 = 147")
    if num1 == 49 and sign == '*' and num2 == 4:
        return("49*4 = 196")
    if num1 == 49 and sign == '*' and num2 == 5:
        return("49*5 = 245")
    if num1 == 49 and sign == '*' and num2 == 6:
        return("49*6 = 294")
    if num1 == 49 and sign == '*' and num2 == 7:
        return("49*7 = 343")
    if num1 == 49 and sign == '*' and num2 == 8:
        return("49*8 = 392")
    if num1 == 49 and sign == '*' and num2 == 9:
        return("49*9 = 441")
    if num1 == 49 and sign == '*' and num2 == 10:
        return("49*10 = 490")
    if num1 == 49 and sign == '*' and num2 == 11:
        return("49*11 = 539")
    if num1 == 49 and sign == '*' and num2 == 12:
        return("49*12 = 588")
    if num1 == 49 and sign == '*' and num2 == 13:
        return("49*13 = 637")
    if num1 == 49 and sign == '*' and num2 == 14:
        return("49*14 = 686")
    if num1 == 49 and sign == '*' and num2 == 15:
        return("49*15 = 735")
    if num1 == 49 and sign == '*' and num2 == 16:
        return("49*16 = 784")
    if num1 == 49 and sign == '*' and num2 == 17:
        return("49*17 = 833")
    if num1 == 49 and sign == '*' and num2 == 18:
        return("49*18 = 882")
    if num1 == 49 and sign == '*' and num2 == 19:
        return("49*19 = 931")
    if num1 == 49 and sign == '*' and num2 == 20:
        return("49*20 = 980")
    if num1 == 49 and sign == '*' and num2 == 21:
        return("49*21 = 1029")
    if num1 == 49 and sign == '*' and num2 == 22:
        return("49*22 = 1078")
    if num1 == 49 and sign == '*' and num2 == 23:
        return("49*23 = 1127")
    if num1 == 49 and sign == '*' and num2 == 24:
        return("49*24 = 1176")
    if num1 == 49 and sign == '*' and num2 == 25:
        return("49*25 = 1225")
    if num1 == 49 and sign == '*' and num2 == 26:
        return("49*26 = 1274")
    if num1 == 49 and sign == '*' and num2 == 27:
        return("49*27 = 1323")
    if num1 == 49 and sign == '*' and num2 == 28:
        return("49*28 = 1372")
    if num1 == 49 and sign == '*' and num2 == 29:
        return("49*29 = 1421")
    if num1 == 49 and sign == '*' and num2 == 30:
        return("49*30 = 1470")
    if num1 == 49 and sign == '*' and num2 == 31:
        return("49*31 = 1519")
    if num1 == 49 and sign == '*' and num2 == 32:
        return("49*32 = 1568")
    if num1 == 49 and sign == '*' and num2 == 33:
        return("49*33 = 1617")
    if num1 == 49 and sign == '*' and num2 == 34:
        return("49*34 = 1666")
    if num1 == 49 and sign == '*' and num2 == 35:
        return("49*35 = 1715")
    if num1 == 49 and sign == '*' and num2 == 36:
        return("49*36 = 1764")
    if num1 == 49 and sign == '*' and num2 == 37:
        return("49*37 = 1813")
    if num1 == 49 and sign == '*' and num2 == 38:
        return("49*38 = 1862")
    if num1 == 49 and sign == '*' and num2 == 39:
        return("49*39 = 1911")
    if num1 == 49 and sign == '*' and num2 == 40:
        return("49*40 = 1960")
    if num1 == 49 and sign == '*' and num2 == 41:
        return("49*41 = 2009")
    if num1 == 49 and sign == '*' and num2 == 42:
        return("49*42 = 2058")
    if num1 == 49 and sign == '*' and num2 == 43:
        return("49*43 = 2107")
    if num1 == 49 and sign == '*' and num2 == 44:
        return("49*44 = 2156")
    if num1 == 49 and sign == '*' and num2 == 45:
        return("49*45 = 2205")
    if num1 == 49 and sign == '*' and num2 == 46:
        return("49*46 = 2254")
    if num1 == 49 and sign == '*' and num2 == 47:
        return("49*47 = 2303")
    if num1 == 49 and sign == '*' and num2 == 48:
        return("49*48 = 2352")
    if num1 == 49 and sign == '*' and num2 == 49:
        return("49*49 = 2401")
    if num1 == 49 and sign == '*' and num2 == 50:
        return("49*50 = 2450")
    if num1 == 50 and sign == '*' and num2 == 0:
        return("50*0 = 0")
    if num1 == 50 and sign == '*' and num2 == 1:
        return("50*1 = 50")
    if num1 == 50 and sign == '*' and num2 == 2:
        return("50*2 = 100")
    if num1 == 50 and sign == '*' and num2 == 3:
        return("50*3 = 150")
    if num1 == 50 and sign == '*' and num2 == 4:
        return("50*4 = 200")
    if num1 == 50 and sign == '*' and num2 == 5:
        return("50*5 = 250")
    if num1 == 50 and sign == '*' and num2 == 6:
        return("50*6 = 300")
    if num1 == 50 and sign == '*' and num2 == 7:
        return("50*7 = 350")
    if num1 == 50 and sign == '*' and num2 == 8:
        return("50*8 = 400")
    if num1 == 50 and sign == '*' and num2 == 9:
        return("50*9 = 450")
    if num1 == 50 and sign == '*' and num2 == 10:
        return("50*10 = 500")
    if num1 == 50 and sign == '*' and num2 == 11:
        return("50*11 = 550")
    if num1 == 50 and sign == '*' and num2 == 12:
        return("50*12 = 600")
    if num1 == 50 and sign == '*' and num2 == 13:
        return("50*13 = 650")
    if num1 == 50 and sign == '*' and num2 == 14:
        return("50*14 = 700")
    if num1 == 50 and sign == '*' and num2 == 15:
        return("50*15 = 750")
    if num1 == 50 and sign == '*' and num2 == 16:
        return("50*16 = 800")
    if num1 == 50 and sign == '*' and num2 == 17:
        return("50*17 = 850")
    if num1 == 50 and sign == '*' and num2 == 18:
        return("50*18 = 900")
    if num1 == 50 and sign == '*' and num2 == 19:
        return("50*19 = 950")
    if num1 == 50 and sign == '*' and num2 == 20:
        return("50*20 = 1000")
    if num1 == 50 and sign == '*' and num2 == 21:
        return("50*21 = 1050")
    if num1 == 50 and sign == '*' and num2 == 22:
        return("50*22 = 1100")
    if num1 == 50 and sign == '*' and num2 == 23:
        return("50*23 = 1150")
    if num1 == 50 and sign == '*' and num2 == 24:
        return("50*24 = 1200")
    if num1 == 50 and sign == '*' and num2 == 25:
        return("50*25 = 1250")
    if num1 == 50 and sign == '*' and num2 == 26:
        return("50*26 = 1300")
    if num1 == 50 and sign == '*' and num2 == 27:
        return("50*27 = 1350")
    if num1 == 50 and sign == '*' and num2 == 28:
        return("50*28 = 1400")
    if num1 == 50 and sign == '*' and num2 == 29:
        return("50*29 = 1450")
    if num1 == 50 and sign == '*' and num2 == 30:
        return("50*30 = 1500")
    if num1 == 50 and sign == '*' and num2 == 31:
        return("50*31 = 1550")
    if num1 == 50 and sign == '*' and num2 == 32:
        return("50*32 = 1600")
    if num1 == 50 and sign == '*' and num2 == 33:
        return("50*33 = 1650")
    if num1 == 50 and sign == '*' and num2 == 34:
        return("50*34 = 1700")
    if num1 == 50 and sign == '*' and num2 == 35:
        return("50*35 = 1750")
    if num1 == 50 and sign == '*' and num2 == 36:
        return("50*36 = 1800")
    if num1 == 50 and sign == '*' and num2 == 37:
        return("50*37 = 1850")
    if num1 == 50 and sign == '*' and num2 == 38:
        return("50*38 = 1900")
    if num1 == 50 and sign == '*' and num2 == 39:
        return("50*39 = 1950")
    if num1 == 50 and sign == '*' and num2 == 40:
        return("50*40 = 2000")
    if num1 == 50 and sign == '*' and num2 == 41:
        return("50*41 = 2050")
    if num1 == 50 and sign == '*' and num2 == 42:
        return("50*42 = 2100")
    if num1 == 50 and sign == '*' and num2 == 43:
        return("50*43 = 2150")
    if num1 == 50 and sign == '*' and num2 == 44:
        return("50*44 = 2200")
    if num1 == 50 and sign == '*' and num2 == 45:
        return("50*45 = 2250")
    if num1 == 50 and sign == '*' and num2 == 46:
        return("50*46 = 2300")
    if num1 == 50 and sign == '*' and num2 == 47:
        return("50*47 = 2350")
    if num1 == 50 and sign == '*' and num2 == 48:
        return("50*48 = 2400")
    if num1 == 50 and sign == '*' and num2 == 49:
        return("50*49 = 2450")
    if num1 == 50 and sign == '*' and num2 == 50:
        return("50*50 = 2500")

    print("Thanks for using this calculator, goodbye :)")


print(calculate(num1,sign,num2))