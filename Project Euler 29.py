# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 11:26:12 2018

@author: Julie
"""
alist = []

for a in range(2,100+1):
    for b in range(2,100+1):
        alist.append(a**b)


alist = set(alist)
print(len(alist))
