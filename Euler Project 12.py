
import math
#step 1: generate triangular numbers
def triangle(a):
    return a*(a+1)/2
def numofdivisors(num):
     factors = 0
     for i in range(1,int(math.sqrt(num))):
         if num%i == 0:
             factors += 2
         else:
             continue
     return factors
n = 1
div = 0
while div < 500:
    n = n + 1
    div = numofdivisors(triangle(n))
print(triangle(n))