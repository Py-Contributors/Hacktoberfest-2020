# Python program to calculate x^n in O(logn) time complexity


#function which returns x^n
def func(x ,n):
	res = x
	prefix = 1

	while n != 1:
		if n % 2 == 0:
			res = res * res
		else:
			prefix = prefix * res
			res = res * res
		n = n // 2

	return res * prefix

num = int(input("Enter an integer: "))
exp = int(input("Enter desirable exponent(integer): "))

print(f'{num}^{exp} = {func(num ,exp)}') #prints output