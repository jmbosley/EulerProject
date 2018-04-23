#Euler Problem 9: Special Pythagorean triplet
ansset = set()
for a in range(1,1000): # so im doing this for all combinations of numbers
    for b in range(a,1000): # from 1 to 999 since it has to be less than 1000
        for c in range(b,1000): # to add to 1000
            if a+b+c==1000:# weird thing, I couldn't get this to work in the
                if a**2 + b**2 ==c**2: # other order
                    print("The answer to Euler Problem 9 is")
                    print(a*b*c)
                    break