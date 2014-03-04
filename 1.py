__author__ = 'Han Wang'
num = [i+1 for i in range(999) if (i+1)%3 == 0 or (i+1)%5 == 0]
print sum(num)
