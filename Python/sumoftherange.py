#first define the main function for the array sum.

def sumofrange(arr):
    sumarr = [0]*(len(arr))
    sumarr[0] = arr[0]
    for i in range(1,len(arr)):
        sumarr[i] = arr[i]+sumarr[i-1]
    return sumarr

print(sumofrange([1,-2,3,10,-8,0]))

# Give the query like sum in the range(2,4)
# The answer will be => sum(2,4) = sum(0,4) - sum(0,1)
# i.e., sum(i,j) = sum(0,j) - sum(0,i-1)
