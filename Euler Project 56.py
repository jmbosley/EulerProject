answer = 0
for a in range(100):
    for b in range(100):
        num = str(a**b)
        temp = 0
        for i in num:
            temp = temp + int(i)
        if temp > answer:
            answer = temp
print(answer)