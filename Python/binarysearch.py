def linearSearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['z','a','c','o','r','i','u','m']
x = 'i'
print("element found at index "+str(linearsearch(arr,x)))