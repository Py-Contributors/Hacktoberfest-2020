#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    rb_mini = 0
    rb_maxi = 0
    mini=maxi = scores[0]
    for score in scores:
        if(score<mini):
            mini = score
            rb_mini += 1
        elif(score>maxi):
            maxi = score
            rb_maxi += 1
    return rb_maxi,rb_mini
if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
