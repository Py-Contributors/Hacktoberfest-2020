#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for n in range(0,len(ar)):
        for m in range(n+1,len(ar)):
            if((ar[n]+ar[m])% k ==0):
                count +=1
    return count
                
    

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')
