#Euler Problem 28: Number spiral diagonals
import numpy as np
total = 0
max=1001
for n in range(3,max+1,2):
        f1 = n**2 # upper right corner of each loop
        f2 = f1 -n+1 # upper left corner of each loop
        f3 = f2 - n + 1 # lower left corner of each loop
        f4 = f3 - n +1 # lower right corner of each loop
        looptot = f1+f2+f3+f4 # sum of each loop
        total = total + looptot # sum of all loops
print("The answer to Euler 28 is:",total+1) # add center