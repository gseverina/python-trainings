#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumping_on_clouds(cloud):
    i = 0
    j = 0
    while i < (len(cloud) - 2):
        if cloud[i+2] == 0:
            i += 2
        else:
            i += 1
        j += 1
    if i == (len(cloud) - 2):
        j += 1
    return j


if __name__ == '__main__':
    c = [0, 0, 1, 0, 0, 1, 0]
    result = jumping_on_clouds(c)
    print(result)

    c = [0, 0, 0, 0, 1, 0]
    result = jumping_on_clouds(c)
    print(result)
