def binary_search(arr,left,right,x):
  if left<right:
    mid = (left + right) // 2    #find the medium value
    if arr[mid] == x:            # if element found then return index
      return mid  
    elif arr[mid] > x:      # if element is lesser than medium element then travesre the first half of the array
      return binary_search(arr,left,mid-1,x) 
    else:                   # if element is greater than medium element then travesre the second half of the array
      return binary_search(arr,mid+1,right,x)   
  else: 
    return -1

