'''heap sort has nlogn big oh complexity
n is size of array
parent is bigger than left and right child in max heap and vice versa in min heap
left child is 2*n +1
right is 2*n +2
this is max heap
to convert this to min heap just comvert < in heapify to >
'''


def heapify(arr,i,n):
	left=(2*i)+1
	right=(2*i)+2
	largest=i
	if(left<n and arr[largest]<arr[left]):
		largest=left
	if(right<n and arr[largest]<arr[right]):
		largest=right
	if(largest!=i):
		(arr[largest],arr[i])=(arr[i],arr[largest])
		heapify(arr,largest,n)


def heap(arr,n):
	for i in range(n,-1,-1):
		heapify(arr,i,n)
	for i in range(n-1,0,-1):
		(arr[0],arr[i])=(arr[i],arr[0])#transfering highest element from root to last
		heapify(arr,0,i)
def delete(arr,a):
	l=0;
	r=len(arr)
	pos=-1
	while(l<=r):
		mid=l+(r-l)/2
		if(arr[mid]<a):
			l=mid+1
		elif arr[mid]>a:
			r=mid-1
		else:
			pos=mid
	if pos>=0:
		arr[pos]=arr[-1]
		arr.pop(-1)
	heap(arr,len(arr))



s=list(map(int,input().split()));
heap(s,len(s))
print(s)
