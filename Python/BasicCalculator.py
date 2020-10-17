# Selection of operation
try:
	while True:
		choice = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modular\n6.Exit\nEnter choice: "))
		if(choice == 6):
			break
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
       	# Check which operation to perform 
		if choice == 1:
			print(num1, "+", num2, "=", num1+num2)
		elif choice == 2:
			print(num1, "-", num2, "=", num1-num2)
		elif choice == 3:
			print(num1, "*", num2, "=", num1*num2)
		elif choice == 4:
			print(num1, "/", num2, "=", num1/num2)
		elif choice == 5:
			print(num1, "%", num2, "=", num1%num2)
		else:
			print("Invalid Choice")
except ZeroDivisionError:
	print("Denominator cannot be 0")
except ValueError:
	print("Enter Numbers only")