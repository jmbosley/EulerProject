#Euler 25: 1000-digit Fibonacci number
import numpy as np 
fiblist = [1,1,2]
newnumb = 0
for i in range(0,1000000):
    newnumb = fiblist[-1] + fiblist[-2]
    if len(str(newnumb)) == 1000:
        fiblist.append(newnumb)
        break
    fiblist.append(newnumb)
    i = i + 1
a=1
b=1
count = 2
for i in range(2,100000000):
    c = a + b
    a = b
    b = c
    count = count +1
    if len(str(b)) >= 10**4:
        break
    
print("The answer to Euler 25 is ")
print(count)