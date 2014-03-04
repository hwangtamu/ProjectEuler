__author__ = 'Han Wang'
n = 600851475143
i = 3
while n >= i:
    if n%i == 0:
        n = n/i
    else:
        i += 2
print i
