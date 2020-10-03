# Python program to calculate the sum of n Natural Numbers

# n denotes upto which number you want to calculate the sum
# for example, if n is 5 then the sum of first 5 natural numbers
num = int(input("Enter the value of n: "))
hold = num
sum = 0

if num <= 0:
   print("Enter a whole positive number!")
else:
   while num > 0:
        sum = sum + num
        num = num - 1;
print("Sum of first", hold, "natural numbers is: ", sum)