import math
import os
import random
import re
import sys
from collections import Counter


# Complete the plusMinus function below.
def plusMinus(arr):
    l = len(arr)
    z = 0
    n = 0
    p = 0
    for i in arr:
        if i > 0:
            p += 1
        elif i == 0:
            z += 1
        else:
            n += 1
    print(f'{p / l:f}')
    print(f'{n / l:f}')
    print(f'{z / l:f}')


if __name__ == '__main__':
    #n = int(input())
    #arr = list(map(int, input().rstrip().split()))

    plusMinus([1, 1, 0, -1, -1])
    plusMinus([-4, 3, -9, 0, 4, 1])