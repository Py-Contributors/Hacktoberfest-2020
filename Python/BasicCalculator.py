# Basic Calculator in Python without any gui.

# create functions for calculations


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def raise_to_power(num1, num2):
    return num1 ** num2


print("Please Select Operations\n " 
      "1. Addition\n "
      "2. Subtraction \n "
      "3. Multiplication \n "
      "4. Divide \n "
      "5. EXPONENTIAL \n")

# Take Input From Keyword
select = input("Press\n" "1 " "2 " "3 " "4 ""5 \n"":")
old_operations = ['1', '2', '3', '4']

if select in old:
    number_1 = int(input("Type Your First Number :"))
    number_2 = int(input("Type YOur Second Number :"))

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

elif select == '5':
    number_1 = int(input("type Your Number :"))
    number_2 = int(input("Raised To What power :"))
    print(f"{number_1} ^ {number_2} =")
    print(raise_to_power(number_1, number_2))

else:
    print('Invalid Operation')
print('Thanks for Using Calculator')


