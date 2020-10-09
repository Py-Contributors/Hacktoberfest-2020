# To heapify subtree rooted at index i.
def heap(array, array_size, i):
    # Initialize largest as root
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists and is 
    # greater than root
    if( left < array_size and array[i] < array[left]):
        largest = left

    # See if right child of root exists and is 
    # greater than root 
    if( right < array_size and array[largest] < array[right]):
        largest = right

    # Change root, if needed 
    if(largest != i):
        array[i], array[largest] = array[largest], array[i]

        # Heapify the root.
        heap(array, array_size, largest)

def sort(array):
    array_size = len(array)

    for i in range(array_size//2 - 1, -1 , -1):
        heap(array, array_size, i)

    for i in range(array_size-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap(array, i, 0)

    return array

if __name__ == "__main__":
    array = [10,50,30,20,60,90,100,80,40,70]

    print("Unsorted array:")
    print(array)

    sorted_array = sort(array)

    print("Sorted array:")
    print(sorted_array)