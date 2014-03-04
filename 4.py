__author__ = 'Han Wang'
max = 0
for a in range(100,1000):
    for b in range(a,1000):
        if a*b > max and str(a*b)==str(a*b)[::-1]:
            max = a*b
print max
