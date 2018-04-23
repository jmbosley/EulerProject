#Euler Problem 6
natnumb = list(range(1,101))
soosq = 0
filler = 0
for element in natnumb:
    soosq = soosq + element**2
for element in natnumb:
    filler  = filler + element
sqosu = filler**2
print(sqosu-soosq)
