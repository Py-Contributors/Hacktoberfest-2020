#Basic Calculator in Python without any gui.
import sys
flag=False
#create functions for calculations
def add(num1, num2):
	return num1 + num2

def sub(num1, num2):
	return num1 - num2

def mul(num1, num2):
	return num1 * num2

def div(num1, num2):
	return num1 / num2

def square(num1):
    return num1**2

def squareroot(num1):
    return num1**0.5

print("Please Select Operations\n "\
	   "1. Addition\n " 
	   "2. Subtraction \n"
	   "3. Multiplication \n"
	   "4. Divide \n"
       "5. Square \n"
       "6. Square Root \n"
     )

#Take Input From Keyword
select = input("Press\n" "1 " "2 " "3 " "4 " "5 ""6 \n")
if(int(select)<5):
    number_1 = int(input("Type Your First Number :"))
    number_2 = int(input("Type Your Second Number :"))
    try:
        re=number_1/number_2
    except ZeroDivisionError:
        print("Cannot be divided!")
        flag=True
        print("Oops!", sys.exc_info()[0], "occurred.")
        
else:
    number_1 = int(input("Type Your  Number :"))

        
        


if select == '1':
	print(number_1, "+", number_2, '=')
	print(add(number_1, number_2))

elif select == '2':
	print(number_1, '-', number_2, '=')
	print(sub(number_1, number_2))

elif select == '3':
	print(number_1, '*', number_2, '=')
	print(mul(number_1, number_2))

elif select == '4' and flag == False:
	print(number_1, '/', number_2, '=')
	print(div(number_1, number_2))

elif select == '5':
    print(number_1, '^ 2 =')
    print(square(number_1))
elif select == '6':
	print(number_1, '^ 0.5 =')
	print(squareroot(number_1))  

else:
	print('Invalid Input ! Try aagian ')
	
print('Thanks for Using Calculator')