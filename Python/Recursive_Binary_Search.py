'''
Title- Recursive Binary Search
'''


def binsearch(ar, key, low, high):
    mid = int((low + high) / 2)
    if low > high:
        print('Element not found')
    elif key == int(ar[mid]):
        print(key, 'found at index', mid)
    elif key < int(ar[mid]):
        high = mid - 1
        binsearch(ar, key, low, high)
    else:
        low = mid+1
        binsearch(ar, key, low, high)


arr = []
i = int(input('enter the no. of elements in the array'))
for j in range(0, i):
    arr.append(int(input('Enter the element')))

item = int(input('enter the search element: '))
arr.sort
binsearch(arr, item, 0, len(arr) - 1)
