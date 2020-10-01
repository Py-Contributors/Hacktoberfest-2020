'''
Fibonacci Series are a series of number which starts from 0 and 1, then the next number is an addition of the previous 2 numbers.
For eg: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.... is a fibonacci series.
Here 0 & 1 are the first two numbers, then we get 1 which is an addition of 0 and 1, then we get 2 i.e addition of 1 & 1,
then we get 3 i.e addition of 2 & 1 and so on.
'''

# Fibonacci Series using Recursion :-

def Fibonacci(n):
	if n<0:
		print("Wrong Input ! Please Check again")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(9))

'''so in Fibonacci Series (9th) number is 21'''
'''
Time Complexity :  T(n) = T(n-1) + T(n-2)
Space Complexity : O(N)
'''