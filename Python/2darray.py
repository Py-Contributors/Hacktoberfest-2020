#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    left = 0
    right = 0
    l = len(arr)
    for i in range(0,len(arr)):
        left += arr[i][i]
        right += arr[l-1][i]
        l = l-1
    return abs(left-right)

def main():
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
main()
