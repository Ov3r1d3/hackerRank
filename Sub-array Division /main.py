#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    blockCounter = 0
    for x in range(0, len(s) - m + 1):
        blockSum = 0
        for y in range(0, m):
            blockSum += s[y + x]
        if blockSum == d:
            blockCounter += 1
    return blockCounter

if __name__ == '__main__':
    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
