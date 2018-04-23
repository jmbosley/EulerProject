#Euler Problem 5: Smallest multiple
setnum=10
i=1
rangelist = list(range(1,21))
upperlimit = 1 # so this will be a upperbound found by multiplying all number
for element in rangelist:
    upperlimit = upperlimit * element
while i < upperlimit:
    i=i+1
    if i % 20 ==0 and i%19==0 and i%18==0: # This cycles through all numbers
        if i%17==0 and i%16==0 and i%15==0: # that arn't covered by others
            if i%14==0 and i%13==0 and i%12==0: # like if it is divisible by 12
                if i%11==0: # it will the be divisible by 2, 3 ect
                    print("The answer to Euler 5 is")
                    print(i)
                    break
            
