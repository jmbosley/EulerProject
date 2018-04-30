
def count(number):
    count = 0
    while number != 1:
        if number % 2 ==0:
            number = number / 2
            count += 1
        else:
            number = 3*number + 1
            count +=1
    return count + 1

answer = 0
match = 0
for i in range(13,1000000):
    temp = count(i)
    if temp > answer:
        answer = temp
        match = i

print(match)