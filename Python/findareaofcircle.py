'''
Formula for area of circle
Area = pi * r^2
 where pi is constant and r is the radius of the circle
'''
def findarea(r):
	return 3.142 *(r**2)

if __name__ == "__main__":
	print("Area is %.6f" % findarea(5))



