# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:47:05 2018

@author: Julie
"""
from math import factorial


#using recurstion
# so the way this works is we need the 1000000th number.
# we know that there are 9! posabilities or each possible first digit.
#  we divide the total possablites (1000000) by the number of posiblities for each number (9!)
# to find how mnay numbers we eat up with each possible first number. the divisor is the first number and the 
# modulus is the number that the rest of the digits need to take up
def permutation(num,listnum):
    if len(listnum) == 1:
        return listnum
    quot, mod = divmod(num, factorial(len(listnum)-1))
    return listnum[quot] + permutation(mod,listnum[:quot] + listnum[quot+1:]) # this omits the number that was just used so it isn't repeated

print(permutation(1000000-1,'0123456789'))