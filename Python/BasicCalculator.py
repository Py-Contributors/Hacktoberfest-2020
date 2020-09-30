#Basic Calculator in Python without any gui.
from math import *

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

def sin(val):
	return sin(val)

def cos(val):
	return cos(val)

def tan(val):
	return tan(val)

def squareroot(num):
	return sqrt(num)

print("Please Select Operations\n "\
	   "1. Addition\n " "2. Subtraction \n"
	   "3. Multiplication \n"
	   "4. Divide \n"
     	   "5. sin\n"
           "6. cos\n"
           "7. tan\n"
           "8. squareroot\n")

#Take Input From Keyword
select = input("Press\n" "1 " "2 " "3 " "4 " "5 " "6 " "7 " "8 \n")

number_1 = int(input("Type Your First Number :"))
number_2 = int(input("Type Your Second Number :"))
value = int(input("Enter your value :"))


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
	print(value)
	print("sin", value, "is", sine(value))
	
elif select == '6':
	print(value)
	print("cos", value, "is", cos(value))
	
elif select == '7':
	print(value)
	print("tan", value, "is", tan(value))
	
elif select == '8':
	print(value)
	print("Squareroot of", value, "is", squareroot(value))

else:
	print('Invalid Input ! Try aagian ')
	
print('Thanks for Using Calculator')
