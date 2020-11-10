#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    b_cal = 0
    for i in range(0,len(bill)):
        if(i==k):
            continue
        else:
            b_cal += bill[i]        
    if(b==int(b_cal/2)):
        print("Bon Appetit")
    else:
        print (int(b-(b_cal/2)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
