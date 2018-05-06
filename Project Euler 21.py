def divisors(num):
    div = [1]
    for i in range(2,int(num**.5)):
        if num%i==0:
            div.append(i)
            temp = num/i
            div.append(temp)
    return(list(set(div)))

def amicable(num):
    mynum = sum(divisors(num))
    return mynum

def test(num):
    return amicable(amicable(num))


anslist = []
for i in range(2,10000):
    if i == test(i) and i != amicable(i):
        anslist.append(i)
        anslist.append(test(i))

print(sum(list(set(anslist))))
    