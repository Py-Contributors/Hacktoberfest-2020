#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    nw = 0
    for i in range(0,(len(s)-m)+1):
        print(i)
        n = 0
        for j in range(i,i+m):
            print(i,j,s[j],n)
            n += s[j]
        if(n==d):
            nw += 1
    return nw
        
            

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')

