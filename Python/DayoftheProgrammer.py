#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if(year==1918):
        return '26.09.1918'
    elif(year<1918):
        if(year%4==0):
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)
    else:
        if((year%400==0) or (year%4==0 and year%100!=0)):
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)
if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')

