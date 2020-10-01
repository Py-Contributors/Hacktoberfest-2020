'''
All the differnt sorting methods at single place. 
Recursive as much as possible 
Keep it simple
'''




'''
bubble sort
Comparison sort
complexity:  О(n2)
'''
def bubble_sort(num):
    value_exchange =0
    for index,value in enumerate(num):
        if index != len(num)-1 and value > num[index+1] :
            num[index]=num[index+1]
            num[index+1]=value
            value_exchange=1
    
    if not value_exchange:
         print(num)
         return
    
    bubble_sort(num)  
    
    
    
num = [23,45,231,767,8,342,24,67,232,5,67,2]    
    
bubble_sort(num)