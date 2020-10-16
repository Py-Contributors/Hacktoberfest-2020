''' 
Python program to find factorial of given number
Factorial of n
n = n*(n-1)*(n-2)*(n-3).......3*2*1
4 = 4*3*2*1 = 24

'''
def factorial(n):
    #Line to Find Factorial
    if (n==1 or n==0):
            return 1
    else:
        return (n * factorial(n-1))

	#Driver Code
num = int(input(" Enter Number For Factorial :\n"))
answer = factorial(num)
print("Factorial of "+str(num)+" is ",answer)
