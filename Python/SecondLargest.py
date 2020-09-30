#Second Largest Element in List

num=int(input("Enter the number of elements: "))
list=[]

for i in range(1, num + 1): 
    ele = int(input("Enter elements: ")) 
    list.append(ele) 
    
list.sort()
print("Second Largest Element in List is: ",list[-2])     