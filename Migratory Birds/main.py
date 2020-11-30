#!/bin/python3

import math
import os
import random
import re
import sys
import collections


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    collection = collections.Counter(arr)
    maxSum = -1
    maxBird = -1
    for bird in collection:
        if collection[bird] > maxSum:
            maxSum = collection[bird]
            maxBird = bird
        elif collection[bird] == maxSum:
            if bird < maxBird:
                maxSum = collection[bird]
                maxBird = bird
    return maxBird


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)
