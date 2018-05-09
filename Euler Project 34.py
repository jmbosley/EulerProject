import math as m

answer = 0
for i in range(3,2540161):
    factsum = 0
    for j in str(i):
        factsum += m.factorial(int(j))
    if(factsum == i):
        answer += i
print(answer)
