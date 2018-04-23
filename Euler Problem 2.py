# Euler Problem 2
fiblist = [1,2]

newnumb = 0
i=1
while i < 100:
    newnumb = fiblist[-1] + fiblist[-2]
    if newnumb > 4000000:
        break
    fiblist.append(newnumb)
    i = i + 1
evenlist = []
for element in fiblist:
    if element%2 == 0:
        evenlist.append(element)
answer = 0
for element in evenlist:
    answer = answer + element
print(answer)
