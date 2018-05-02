# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 10:35:25 2018

@author: jbosley
"""

size = 20
pathcount = 1;
for i in range(size):
    pathcount = pathcount * ((2*size)- i)/ (i+1) #based on wikipedia code for binomial imjplementation for coding where 2*size = n
print(pathcount)