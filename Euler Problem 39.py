# Euler Problem 39: Integer Right Triangles
# assumption 1: p can only be even
#   if a and b are even then so is c then so is p
#   if a and b are odd then c is even the p is even
#   if a or b is odd and the other even then c is odd then p is even
# assumption 2: a valid answer is when ( (p*(p-2*a)) % (2*(p-a)) ) == 0 
#   this comes from using a+b+c=p -> c = p-a-b plug into a**2+b**2 = c**2
#   solvig for b you get this equation
#   b must be an integer so the remainder must be zero
# assumption 3: the largest range on a is p/3
#   we know a<c and b < c and that a<=b
#   this means a<=b<c 
#   a being the smallest side has a max value of p/3
maxcount = 0
pans = 0
for p in range (2,1000,2): # p can only be even given all combinations of a b and c
    count = 0
    for a in range (2,int(p/3)): 
            if( ( (p*(p-2*a)) % (2*(p-a)) ) == 0 ):
                count = count + 1
    if count > maxcount:
        maxcount = count
        pans = p
print("The answer to Euler 39 is ")
print(pans)                
