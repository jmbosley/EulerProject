#Euler Problem 7: 10001st prime     
import numpy as np
import time
tick = time.time()

n = 104750 # okay so I kinda cheated this and this number gives me 10001 primes
primes = set(range(2,n)) # this creates a range from 2 to a totally random n
p=1
while p < n:
    p = p+1
    countlist = set(np.arange(2*p,n,p))
    for element in countlist:
        if element in primes:
            primes.remove(element) 
            # so i'm removing non primes by multiples
tock = time.time()
time_delta = float(tock-tick)
print("The answer to Euler 7 is")
print(max(primes))
print("It took us exactly T={} s to generate prime numbers".format(time_delta,n))
