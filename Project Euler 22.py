# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:13:27 2018

@author: Julie
"""
f=open("p022_names.txt",'r')
names=sorted(f.read().replace('"','').split(','),key=str)

def ltn(letter):
    if letter == 'A':
        return 1
    if letter == 'B':
        return 2
    if letter == 'C':
        return 3
    if letter == 'D': 
        return 4
    if letter == 'E':
        return 5
    if letter == 'F':
        return 6
    if letter == 'G':
        return 7
    if letter == 'H':
        return 8
    if letter == 'I': 
        return 9
    if letter == 'J':
        return 10
    if letter == 'K':
        return 11
    if letter == 'L':
        return 12
    if letter == 'M':
        return 13
    if letter == 'N': 
        return 14
    if letter == 'O':
        return 15
    if letter == 'P':
        return 16
    if letter == 'Q':
        return 17
    if letter == 'R':
        return 18
    if letter == 'S': 
        return 19
    if letter == 'T':
        return 20
    if letter == 'U':
        return 21
    if letter == 'V':
        return 22
    if letter == 'W':
        return 23
    if letter == 'X':
        return 24
    if letter == 'Y': 
        return 25
    if letter == 'Z':
        return 26
 
 
answer = 0
count = 0
for i in names:
    count = count + 1
    namesum = 0
    for j in i:
        namesum = namesum + ltn(j)
    answer = answer + namesum * count
    
print(answer)