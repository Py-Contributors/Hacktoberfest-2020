#Basic Calculator in Python without any gui.

#create functions for calculations
def add(number1, number2):
	return number1 + number2

def sub(number1, number2):
	return number1 - number2

def mul(number1, number2):
	return number1 * num2

def div(number1, number2):
	if num2 == 0:
		print("Can't divide a number by 0")
		exit()
	return number1 / number2

print("Please Select Operations\n "\
	   "1. Addition\n " 
	   "2. Subtraction \n"
	   "3. Multiplication \n"
	   "4. Divide \n" )

#Take Input From Keyword
select = input("Press\n" "1 " "2 " "3 " "4 \n")

number_1 = int(input("Type Your First Number Here:"))
number_2 = int(input("Type Your Second Number Here:"))


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

else:
	print('Invalid Input ! Try aagian ')
	
print('Thanks for Using Calculator')
