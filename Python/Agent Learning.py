
# NAME:Oarabile Mwiya

# VectorAdd() returns a vector obtained by adding two vectors,
#which are parameters of the function
# result is a vector
def VectorAdd(a,b):
	#Check equality of the vectors
    assert len(a)==len(b)
	#Initialise an empty vector list
    newVector = []
	#Iterate with respect to the vector length and add corresponding values
    for i in range(len(a)):
            v = a[i] + b[i]
            newVector.append(v)
    
    
    return newVector
#  performs vector subtraction on two vectors and returns a 
# vector
def VectorSub(a,b):
	#check if length of vectors are equal
    assert len(a)==len(b)
	#Initialize an empty vector list
    newVector = []
	#Iterate the  indices wrt to vector length and subtract corresponding values
    for i in range(len(a)):
            v = a[i] - b[i]
            newVector.append(v)
    return newVector


# Implement this: VectorMult() performs vector multiplication and returns a scalar 
# (number)
def VectorMult(a,b):
	#compare length equality of vector a and b
    assert len(a)==len(b)
    total =  0
	#Iterate the vector indices wrt to the vector length and multiply corresponding values
    for i in range(len(a)):
            v = a[i] * b[i]
            total = total + v
    return total

# Implement this: Perceptron Learning Algorithm
def PerceptronLearning(wvector,Mp,Mn):
		weight = Mp
		newVector = []
		while len(newVector  < 0 or count < 3):
			newVector = [];
		for i in range (0, len(wvector)):
			if VectorMult(weight,Mp[i] <=0):
				weight = VectorAdd(weight, Mn[i])
				newVector.append(VectorMult,weight,wvector[i])
				count  = count + 1;
		for i in range(0, len(Mn)):
			if VectorMult(weight,Mn[i] > 0):
				weight = VectorSub(weight, Mn[i])
				newVector.append(VectorMult,(weight,wvector[i]))
				count = count + 1;
				
 
    
		return wvector


# Implement this
def PerceptronFunction(wvector,x):
    assert len (wvector)==len(x)
    sum=VectorMult(wvector,x)
    if sum > 0:
            return 1
    return 0
   

# DO NOT MODIFY THIS
def CheckPerceptron():
        w=[1,1]
    # positive examles
        Mp=[[0,1],[0,2]]
    
    # negative examples
        Mn=[[-1,1],[-2,1]]
    
        for x in Mp:
                if PerceptronFunction(w,x)==0:
                    print "Problem with Positive Vector x:",x
                else:
                    print "No problem with Positive Vector x:",x
        for x in Mn:
                if PerceptronFunction(w,x)==1:
                    print "Problem with Negative Vector x:",x
                else:
                    print "No problem with Negative Vector x:",x

print(VectorAdd([1,2],[1,4]))
print(VectorSub([1,9],[1,4]))
print(VectorMult([1,3],[1,2]))

CheckPerceptron()
