# Python Script to calculate the total number of digits from 1 to N, for an input N.

# T = no. of test cases
T = int(input())

for t in range(T):
  # Upper limit
  N = int(input())
  
  len_ = len(str(N))
  count = (N - 10 ** (len_ - 1) + 1)*len_
  
  for i in range(len_-1):
    count += 9*(10 ** i)*(i+1)
    
  #printing the result
  print(count)
