answer = False
count = 99999#needs to be at least 6 digits
while answer == False:
    count +=1
    x = set(str(count))
    x2 = set(str(2*count))
    x3 = set(str(3*count))
    x4 = set(str(4*count))
    x5 = set(str(5*count))
    x6 = set(str(6*count))
    answer = (x==x2 and x==x3 and x==x4 and x==x5 and x==x6 )
print(count)
    