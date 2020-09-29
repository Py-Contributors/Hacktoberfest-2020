import math

operation = input("Do you want to perform one or more than one operation? (1/2)\n")

if not operation.isnumeric():
    print("Please choose 1 or 2")
elif operation.isnumeric():
    try:
        operation = int(operation)
        if operation > 2:
            print ("Please choose 1 or 2")
    except:
        print ("Error")    
if operation == 1:
    sqrt_option = input("Do you want to get the square root of the final result?(Yes/no) \n")
    sqrt_option.lower()
    if not sqrt_option == "yes" or sqrt_option == "no":
        print("Either choose between yes or no.")
        exit() 
    def add(num1, num2):
	    return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def mul(num1, num2):
        return num1 * num2

    def div(num1, num2):
        return num1 / num2

    print("Please Select Operations\n "
          "1. Addition\n " 
          "2. Subtraction \n"
          "3. Multiplication \n"
          "4. Divide \n" )

    #Take Input From Keyword
    select = input("Press\n" "1 " "2 " "3 " "4 \n")
    try:
        number_1 = float(input("Type Your First Number :"))
        number_2 = float(input("Type YOur Second Number :"))
    except ValueError:
        print("Please input an integer only!")
        exit()

    if select == '1':
        print(number_1, "+", number_2, '=')
        print(add(number_1, number_2))
        answer = add(number_1, number_2)
    elif select == '2':
        print(number_1, '-', number_2, '=')
        print(sub(number_1, number_2))
        answer = sub(number_1, number_2)

    elif select == '3':
        print(number_1, '*', number_2, '=')
        print(mul(number_1, number_2))
        answer = mul(number_1, number_2)

    elif select == '4':
        print(number_1, '/', number_2, '=')
        print(div(number_1, number_2))
        answer = div(number_1, number_2)
    
    if sqrt_option == "yes":
        print(f"The square root for {answer} is {math.sqrt(answer)}")
    elif sqrt_option == "no":
        pass
elif operation == 2:
    sqrt_option = input("Do you want to get the square root of the final result?(Yes/no) \n")
    sqrt_option.lower()
    if not sqrt_option == "no" and not sqrt_option == "yes":
        print("Either choose between yes or no.")
        exit()    
    try:    
        operation_perf = input("Type in your problem to solve:\n")
        print(eval(operation_perf))
        answer = eval(operation_perf)
    except SyntaxError:
        print("Please use Integer only!")
        exit()
    except NameError:
        print("Please use Integer only!")
        exit()
    if sqrt_option == "yes":
        print(f"The square root for {answer} is {math.sqrt(answer)}")

# By Ind-Kartikey