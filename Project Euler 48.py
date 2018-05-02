answer = 0
for i in range(1,1000+1):
    answer = answer + i**i
answer = str(answer)
print(int(answer[-10:]))