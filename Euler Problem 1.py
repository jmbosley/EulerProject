#Euler Problem 1: Multiples of 3 and 5
rangelist = list(range(1,1000)) # Creats a range that goes from to 999
sumlist = list()
for element in rangelist:
    if element%3 == 0 or element%5==0: # so if the element is divisible by 3 or 5
        sumlist.append(element) # add it to sumlist
sumrange = sum(sumlist) # Then sum them
print("The answer to Euler 1 is")
print(sumrange)
