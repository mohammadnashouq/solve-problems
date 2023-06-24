#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    dig = 0
    secdiag = 0
    for i in range(len(arr)):
        dig += arr[i][i]
        secdiag += arr[i][len(arr) - 1 - i ]
    res = dig - secdiag
    if res < 0:
        return -res
    else:
        return res
