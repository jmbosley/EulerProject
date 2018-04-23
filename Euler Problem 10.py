#Euler Problem 7
import numpy as np

n = 2000000
primes = set(range(2,n))
p=1
while p < n:
    p = p+1
    countlist = set(np.arange(2*p,n,p))
    for element in countlist:
        if element in primes:
            primes.remove(element)

print("The answer to Euler 7 is")
print(max(primes))   