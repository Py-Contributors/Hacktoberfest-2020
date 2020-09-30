#Basic Calculator in Python without any gui.

#create functions for calculations
def add(num1, num2):
	return num1 + num2

def sub(num1, num2):
	return num1 - num2

def mul(num1, num2):
	return num1 * num2

def div(num1, num2):
	if num2 == 0:
		print("Can't divide a number by 0")
		exit()
	return num1 / num2

def squ(num1):
	return num1 ** 2

def powe(num1 , num2):
	return num1 ** num2

def sqroot(num1):
	return num1 ** 0.5

print("Please Select Operations\n "\
	   "1. Addition\n " 
	   "2. Subtraction \n"
	   "3. Multiplication \n"
	   "4. Divide \n"
           "5. Square \n"
           "6. Power \n"
           "7. Square root \n")

#Take Input From Keyword
select = input("Press\n" "1 " "2 " "3 " "4 " "5 " "6 " "7 \n")

number_1 = int(input("Type Your First Number :"))
number_2 = int(input("Type Your Second Number :"))


if select == '1':
	print(number_1, "+", number_2, '=')
	print(add(number_1, number_2))

elif select == '2':
	print(number_1, '-', number_2, '=')
	print(sub(number_1, number_2))

elif select == '3':
	print(number_1, '*', number_2, '=')
	print(mul(number_1, number_2))

elif select == '4':
	print(number_1, '/', number_2, '=')
	print(div(number_1, number_2))
	
elif select == '5':
	print(number_1, '^', 2'=')
	print(squ(number_1))
	
elif select == '6':
	print(number_1, '^',number_2, '=')
	print(powe(number_1, number_2))
	
elif select == '7':
	print(number_1, 'sq root','=')
	print(sqroot(number_1))

else:
	print('Invalid Input ! Try aagian ')
	
print('Thanks for Using Calculator')
