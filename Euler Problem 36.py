# Euler Problem 36: Double - Base Palindromes
def dectobi(decnum):
    binum = ""
    while decnum >= 1:
        binum = binum + str(decnum%2)
        decnum = int(decnum / 2)
    return int(binum[::-1])

def bitodec(binum):
    decnum = 0
    for i in range(0,len(str(binum))):
        decnum = decnum + int(str(binum)[i])*2**i
    return int(decnum)
maxnum = 1000000
answerlist = []
for i in range(1,maxnum+1):
    if str(i) == str(i)[::-1]:
        bie = dectobi(i)
        if str(bie) == str(bie)[::-1]:
            answerlist.append(i)
answer = 0
for i in answerlist:
    answer = answer + i
print("The answer to Euler 36 is ")
print(answer)
