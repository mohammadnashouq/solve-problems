#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    current_level = 0
    next_level = 0
    previous_level = 0
    res = 0
    for i in range(n):
        if s[i] == 'D':
            previous_level = current_level
            current_level = next_level
            next_level -= 1
            
        if s[i] == 'U':
            previous_level = current_level
            current_level = next_level
            next_level += 1

        if current_level == -1  and next_level ==0:
            res += 1
    return res
