# Basic Calculator in Python without any gui.

def add(num_1, num_2):
	""""" This Function Adds Two Numbers """""
	return num_1 + num_2


def subtract(num_1, num_2):
	""""" This Function Subtracts Two Numbers """""
	return num_1 - num_2


def multiply(num_1, num_2):
	""""" This Function Multiplies Two Numbers """""
	return num_1 * num_2


def divide(num_1, num_2):
	""""" This Function divides Two Numbers """""
	if num_2 == 0:
		print("Not Defined / Infinite")
		exit()
	return num_1 / num_2


def power(num1, num2):
	import math
	""""" This Function gives Power """""
	return math.pow(num1, num2)


def calculator():
	print("Please Select Operations")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Power")

	# Take Input From Keyword
	print("Enter Your Choice")
	choice = input("1," " 2," " 3," " 4," " 5"" ------> ")

	num1 = int(input("Type Your First Number :"))
	num2 = int(input("Type Your Second Number :"))

	if choice == '1':
		print(num1, "+", num2, '=', add(num1, num2))

	elif choice == '2':
		print(num1, '-', num2, '=', subtract(num1, num2))

	elif choice == '3':
		print(num1, '*', num2, '=', multiply(num1, num2))

	elif choice == '4':
		print(num1, '/', num2, '=', divide(num1, num2))

	elif choice == '5':
		print(num1, "to the power", num2, power(num1, num2))

	else:
		print('Invalid Input ! Try again ')


def main():
	print('Thanks for Using Calculator')
	print("If you want to Run calculator again press Y if not press N")
	run = input("Enter your choice : ")
	if run == 'Y' or 'y':
		calculator()
		main()
	else:
		print("See you again !")


calculator()
main()
