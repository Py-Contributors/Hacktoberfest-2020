def binary_search(arr, low, high, x):

    if high >= low:
  
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x) 

        else:
            return binary_search(arr, mid + 1, high, x) 
  
    else:
        return -1


if __name__ == '__main__':
    arr = [6, 1, 2, 3, 10, 40, 9, 205]
    print(binary_search(arr, 0, len(arr)-1, 10))
