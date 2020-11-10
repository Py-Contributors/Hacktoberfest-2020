import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maxele = max(arr)
    minele = min(arr)
    s = 0
    for num in arr:
        s = s + num
        
    print(str(s-maxele)+' '+str(s-minele))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
