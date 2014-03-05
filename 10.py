__author__ = 'Han Wang'
n = 2*10**6
primes = [True] * n
primes[0],primes[1] = [None] * 2
sum = 0
for ind,val in enumerate(primes):
    if val is True and ind > n ** 0.5 + 1:
        sum += ind
    elif val is True:
        primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
        sum += ind
print sum
