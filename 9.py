__author__ = 'Han Wang'
import math
for a in range(1,250):
    for b in range(500-a,500):
        c = math.sqrt(a*a+b*b)
        if a+b+c==1000:
            print a*b*c
