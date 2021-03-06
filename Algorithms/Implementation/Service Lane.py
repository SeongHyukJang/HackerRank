#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases):
    res = []
    for case in cases:
        i,j = case[0],case[1]
        
        max_size = min(width[i:j+1])
        res.append(max_size)
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
