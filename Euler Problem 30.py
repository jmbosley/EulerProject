#Euler Problem 30: Digit fifth powers
#for an upper bound 9 is the largest single digit so. using 9^5 gets us 59049 
#which is 5 digits long. So for a max bound it should be around 5*9^5. 
answerlist = []
for i in range(10,300000):
    sums = 0
    for j in str(i):
        sums = sums + int(j)**5
    if sums == i:
        answerlist.append(sums)
answer30 = 0
for i in answerlist:
    answer30 = i + answer30
print("The answer to Euler 30 is")
print(answer30)
