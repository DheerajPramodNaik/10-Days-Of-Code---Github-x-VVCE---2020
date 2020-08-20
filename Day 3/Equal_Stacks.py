#!/bin/python3

import os
import sys
import math

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)

    while not (sum_h1 == sum_h2 and sum_h2 == sum_h3):
        if sum_h1 > sum_h2 or sum_h1 > sum_h3:
            t = h1.pop()
            sum_h1 -= t
        if sum_h2 > sum_h1 or sum_h2 > sum_h3:
            t = h2.pop()
            sum_h2 -= t
        if sum_h3 > sum_h1 or sum_h3 > sum_h2:
            t = h3.pop()
            sum_h3 -= t

    return sum_h1

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    h1.reverse()
    h2.reverse()
    h3.reverse()

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
