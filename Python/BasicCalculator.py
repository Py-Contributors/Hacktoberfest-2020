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

print("Please Select Operations\n "\
	   "1. Addition\n " 
	   "2. Subtraction\n "
	   "3. Multiplication\n "
	   "4. Divide \n" )

#Take Input From Keyword
select = input("Press\n" "1 " "2 " "3 " "4 \n")

number_1 = int(input("Type Your First Number :"))
number_2 = int(input("Type Your Second Number :"))

options = {"1": ("add","+"), "2":("sub","-"), "3":("mul","*"), "4":("div","/")}
selected_op = options.get(select,False)

if not selected_op:
    print("Invalid Input! Try again")
else:
    print(f"{number_1} {selected_op[1]} {number_2} = ")
    print(eval(f'{selected_op[0]}({number_1}, {number_2})'))

print('Thanks for Using Calculator')
