#Program to find the 2nd minimun number from  a list

numbers=input('Enter numbers')
numbers=numbers.split()
numbers=list(map(int,numbers))
maxnumber=max(numbers)
minnumber=min(numbers)
for number in numbers:
    if number<maxnumber and number>minnumber:
        secondmin=number
        break
    else:
        secondmin=number
print(secondmin)
