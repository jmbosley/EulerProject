def divsum(num):
    div = [1]
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            div.append(i)
            temp = num/i
            div.append(temp)
    return(sum(list(set(div))))

abundant = []
upper = 28123+1
for i in range(1,upper):
    if i < divsum(i) and divsum(i) <= 28123:
        abundant.append(i)
answerlist = list(range(1,28123))

for i in range(1,28123):
    for j in abundant:
        if (i-j) in abundant:
            answerlist.remove(i)
            break
print(sum(answerlist))
  

