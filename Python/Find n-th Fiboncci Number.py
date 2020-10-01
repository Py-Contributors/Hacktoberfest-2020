'''
Fibonacci Series start from 1. it makes new number by adding previous 2 Numbers.
1,1,2,3,5

Make a array storing the series of fibonacci number
if the nth number of fibonacci is present then the answer is printed 
else it computes and stores it in the array
'''

fibArr = [0,1]

def Fibonacci(n):
	if n<0:
		print("Wrong Input ! Please Check Again")
	elif n <= len(fibArr):
		return fibArr[n-1]
	else:
		temp = Fibonacci(n-1) + Fibonacci(n-2)		
		fibArr.append(temp)		
		return temp


print(Fibonacci(9))
'''so in Fibonacci Series (9th ) number is 21'''
