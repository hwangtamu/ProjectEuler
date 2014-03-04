__author__ = 'Han Wang'
a = 1
b = 1
c = 2
while c <= 4000000:
    a = b + c
    b = a + c
    c = a + b
print (b-1)/2
