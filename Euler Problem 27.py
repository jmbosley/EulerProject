#Euler Problem 27: Quadratic primes
def primeCheck(n):
    if n == 2: #so 2 is a prime
        return True
    if n % 2 == 0 or n <= 1: # if number is divisible by two or less than 2 then not a prime
        return False

    sqr = int(n**.5) + 1 # so root of a number plus 1 is sq

    for divisor in range(3, sqr): # so the divisor must be less than the root plus 1
        if n % divisor == 0:
            return False
    return True 
primerange = []
maxrange = 0
for number in range(0,1000+1): # cant be negative anyway
    if primeCheck(number)==True:
        primerange.append(number)
nmax = 0
ans = 0
for b in primerange: # for a=-n case b must be prime
    for a in range(-1000, 1001): # I think a can exist in full range
        n = 1
        while primeCheck(n*n + a*n + b)==True:
            n+= 1 # so we are counting unitl last prime
        if n>nmax:
            ans = a*b
            nmax = n
print("The answer to Euler 27 is:", ans)     