#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    shoes = list(set(ar))
    pairs = 0
    for shoe in shoes:
        p = math.floor(ar.count(shoe)/2)
        pairs += p
    return pairs
if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

