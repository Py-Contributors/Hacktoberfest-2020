#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    rounded = []
    for grade in grades:
        if(grade<38):
            rounded.append(grade)
        else:
            r = math.ceil(grade/5)*5
            if(r-grade<3):
                rounded.append(math.ceil(grade/5)*5)
            else:
                rounded.append(grade)
    return rounded
        
if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
