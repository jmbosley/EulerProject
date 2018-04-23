# Euler Problem 32: Pandigital products
threedigit = list(range(123,2000))
twodigit = list(range(1,98))
megalist = []
#This creats my lists of multipliers and products
for i in threedigit:
    for j in twodigit:
        templist = []
        multi = i * j
        if multi < 9999:
            adder = [str(i),str(j),str(multi)]
            megalist.append(adder)
            
answerlist = []
newanswerlist = []
#This splits up the numbers into a list of digits
for i in megalist:
    cycle = []
    for j in i: 
        for digit in j:
            cycle.append(int(digit))
    answerlist.append(cycle)
#This checks to make sure there are only 1 of each number    
for i in answerlist:
    for j in i:
        if j ==0:
            i.remove(j)
    if len(set(i))==9:
        newanswerlist.append(i)
        
addlist = []
#This recombines the products into actual numbers
for i in newanswerlist:
    addlist.append(int(str(i[5])+str(i[6])+str(i[7])+str(i[8])))
#This gets rid of any repeats  that made it    
addlist = list(set(addlist))

answer = 0
#This add teh products all up
for i in addlist:
    answer = answer + i
print("The answer to Euler 32 is")
print(answer)

