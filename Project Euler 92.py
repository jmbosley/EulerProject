def recur(num):
    if num == 1:
        return 0
    elif num ==89:
        return 1
    else:
        newnum = 0
        for i in str(num):
            newnum += int(i)**2
        #return(newnum)
        return recur(newnum)
answer = 0
for i in range(1,10**7):
    answer = answer + recur(i)
print(answer)
        
