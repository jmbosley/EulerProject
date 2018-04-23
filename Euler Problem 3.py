#Euler Problem 3: Largest prime factor
num = int(600851475143)
multilist = set()
i = 2 # every thing is divisible by 1 so skip that
while i <= num: # a number larger than num won't go into it
    if num%i==0: # find every number that num is a multiple of
        num = num/i # Divide num by that number in order from least to greatest
        multilist.add(i) # add each number to multilist
    else:
        i = i+1 # if it isn't a multiple then add 1 to i
print("The answer to Euler 3 is")
print(max(multilist))
