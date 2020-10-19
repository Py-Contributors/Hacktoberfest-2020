https://github.com/coderiosity/Hacktoberfest-2022.git# Python3 program to print k-th  
# distinct element in a given array 
def printKDistinct(arr, size, KthIndex): 
    dict = {} 
    vect = [] 
    for i in range(size): 
        if(arr[i] in dict): 
            dict[arr[i]] = dict[arr[i]] + 1
        else: 
            dict[arr[i]] = 1
    for i in range(size): 
        if(dict[arr[i]] > 1): 
            continue
        else: 
            KthIndex = KthIndex - 1
        if(KthIndex == 0): 
            return arr[i] 
    return -1
  
# Driver Code 
arr = [1, 2, 1, 3, 4, 2] 
size = len(arr) 
print(printKDistinct(arr, size, 2)) 
