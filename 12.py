__author__ = 'Han Wang'
def tri(n):
    return n*(n+1)/2

def fac(n):
    factor = {}
    i = 2
    while n > 1:
        if n%i == 0:
            if i>2 and i not in factor:
                factor[i] = 1
            if i == 2 and i not in factor:
                factor[i] = 2
            else:
                factor[i] += 1
            n = n/i
        else:
            i += 1
    ans = 1
    for i in factor.values():
        ans *= i
    return ans

n = 1000
while fac(tri(n))<500:
    n += 1
print tri(n)
