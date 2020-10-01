def quicksort(arr):
    if len(arr)>=1:
        pivot = arr.pop(len(arr)//2)
    else:
        return arr
    items_greater = []
    items_lesser = []
    for ele in arr:
        if ele>=pivot:
            items_greater.append(ele)
        else:
            items_lesser.append(ele)

    return quicksort(items_lesser) + [pivot] + quicksort(items_greater)

arr = list(map(int,input().split()))
print(quicksort(arr))