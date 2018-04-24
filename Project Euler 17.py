# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 11:42:46 2018

@author: Julie
"""

tens = ["one", "two", "three","four","five","six", "seven", "eight", "nine"]
teens = ["ten","eleven", "twelve", "thirteen" , "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decades = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

megalist = [] 

megalist = megalist + tens
megalist= megalist+teens


megalist = megalist + decades

for i in range(0,len(decades)):
    for j in range(0,len(tens)):
        megalist.append(decades[i]+tens[j])
        

for i in range(0,len(tens)):
    megalist.append(tens[i]+"hundred")

for j in range(0,len(tens)):
    for k in range(0,len(tens)):
        megalist.append(tens[k]+"hundredand" +tens[j])

for j in range(0,len(teens)):
    for k in range(0,len(tens)):
        megalist.append(tens[k]+"hundredand" +teens[j])

for k in range(0,len(tens)):
    for i in range(0,len(decades)):
            megalist.append(tens[k]+"hundredand" +decades[i])

for k in range(0,len(tens)):
    for i in range(0,len(decades)):
        for j in range(0,len(tens)):
            megalist.append(tens[k]+"hundredand" +decades[i]+ tens[j])
            

      
            
megalist.append( "onethousand")
print(len("".join(megalist)))  