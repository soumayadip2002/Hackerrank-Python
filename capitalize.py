import math
import os
import random
import re
import string
def solve(s):
    #return string.capwords(s, ' ')
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':
    s = input()

    result = solve(s)
    
    print(result)
