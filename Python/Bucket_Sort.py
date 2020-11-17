# Python3 program to sort an array 
# using bucket sort 

#defining insertion sort for comparing two values
def insertionSort(b): 
	for i in range(1, len(b)): 
		up = b[i] 
		j = i - 1
		while j >= 0 and b[j] > up: 
			b[j + 1] = b[j] 
			j -= 1
		b[j + 1] = up	 
	return b	 

#bucket sort implementation
def bucketSort(x): 
	arr = [] 
	slot_num = 10 # 10 means 10 slots, each 
				# In this case slot's size is 0.1 
	for i in range(slot_num): 
		arr.append([]) 
		
	# Putting array elements in different buckets 
	for j in x: 
		index_b = int(slot_num * j) 
		arr[index_b].append(j) 
	
	# Sorting individual buckets 
	for i in range(slot_num): 
		arr[i] = insertionSort(arr[i]) 
		
	# concatenating the result 
	k = 0
	for i in range(slot_num): 
		for j in range(len(arr[i])): 
			x[k] = arr[i][j] 
			k += 1
	return x 

# Driver Code
# here list are in range 0 to 1 
x = [0.009, 0.332, 0.77, 
	0.91, 0.66, 0.3, 0.12] 
print("Sorted Array :") 
print(bucketSort(x)) 
