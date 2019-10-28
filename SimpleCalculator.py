print("""this is  a simple calcultor that accepts equations that are seperated by spaces in between operators and operands:
	for example: 2 + 3. It does not accept more than one operator """)
equation = input("").split()
res = 0
if '/' in equation:
	n = equation.index('/')
	res+=int(equation[n-1])/int(equation[n+1])
elif '*' in equation:
	n = equation.index('*')
	res+=int(equation[n-1])*int(equation[n+1])
elif '+' in equation:
	n = equation.index('+')
	res+=int(equation[n-1])+int(equation[n+1])
elif '-' in equation:
	n = equation.index('-')
	res+=int(equation[n-1])-int(equation[n+1])
else:
	print("Please give the sum in a valid format with spaces.")
print(res)


