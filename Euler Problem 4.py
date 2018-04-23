# Euler Problem 4
giantlist = list(range(100,999))
multis = list()
for element in giantlist:
    for part in giantlist:
        if str(element * part) == str(element*part)[::-1]:
            multis.append(element*part)
print(max(multis))
