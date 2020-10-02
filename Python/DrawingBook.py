#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    p = p if(p%2==0) else p-1
    start = 1 if (p<n/2) else n
    turns =0
    print(start)
    if(start==1):
        turns = math.floor(p/2)
    else:
        turns = math.floor((start-p)/2)
    return turns
    
    

if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(str(result) + '\n')

