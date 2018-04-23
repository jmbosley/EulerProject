## Euler Problem 26: Reciprocal cycles
##So for the approach of this one I will be using the reaminder function. So
##basically fo 1/6 we do 1%6 which is 1. For the next tens place we multiply the
##remainder by 10 then divide again. 10%6 = 4. so do that again. 40%6 = 4. I already
##I already had a remainder of 4 so that means the loop will repeat. This number has
## one repeating decimal. Which is true.
maxnum = 1000
countmax = 0
dmax = 0
for i in range(2,maxnum):
     remainderlist = []
     top = 1
     count = 0
     remainder = 1
     while top%i not in remainderlist:  
         remainder = top%i
         remainderlist.append(remainder)
         top= remainder*10 
         count = count + 1
     if count>countmax:
         countmax = count
         dmax = i
print("The answer to Euler 26 is:", dmax)   
       