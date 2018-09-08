#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    consecutive = 0
    maximum = 0
    
    while n > 0:
        if n % 2 == 1:
            consecutive += 1
            maximum = max(maximum, consecutive)
        
        else:
            consecutive = 0
        n //= 2
        
    print(maximum)
