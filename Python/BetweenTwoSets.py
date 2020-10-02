#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 

    return x

def find_lcm(a,b): 
    return int((a*b) / find_gcd(a,b))

def getTotalX(a, b):
    # Write your code here
    count = 0
    lcm = a[0]
    gcd= b[0]
    if(len(b)>1):
        for i in range(1,len(b)): 
            gcd=find_gcd(gcd,b[i])
    if(len(a)>1):
        for i in range(1,len(a)):
            lcm = find_lcm(lcm,a[i])
    for i in range(lcm,gcd+1,lcm):
        if(gcd%i==0):
            count += 1
    return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')
