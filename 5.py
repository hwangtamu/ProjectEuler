__author__ = 'Han Wang'
multiples = []
product = 1
for i in range(1,21):
    if not multiples:
        multiples.append(i)
    else:
        for n in multiples:
            if i%n == 0:
                i = i/n
        multiples.append(i)
        product *= i
print product
