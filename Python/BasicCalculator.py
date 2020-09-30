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
# this power function is contributed by Ritika Jaiswal.
def power(num1, num2): 
	if(num2 == 0): return 1
	temp = power(num1, int(num2 / 2)) 
	if (num2 % 2 == 0): 
		return temp * temp 
	else: 
		if(num2 > 0): return x * temp * temp 
		else: return (temp * temp) / num1 
		

# This code is contributed by Smitha Dinesh Semwal. 
 

print("Please Select Operations\n "\
	   "1. Addition\n " 
	   "2. Subtraction \n"
	   "3. Multiplication \n"
	   "4. Divide \n"
           "5. Power \n"   
     )

#Take Input From Keyword
select = input("Press\n" "1 " "2 " "3 " "4 \n")

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
	print(number_1, '^', number_2, '=')
	print(power(number_1, number_2))

else:
	print('Invalid Input ! Try aagian ')
	
print('Thanks for Using Calculator')
