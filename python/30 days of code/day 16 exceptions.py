#!/bin/python3

import sys

S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")



'''
Fail
'''

#!/bin/python3

import sys

S = input().strip()

try:
    is_int = int(S)
    print(is_int)
except ValueError:
    print("Bad String")
