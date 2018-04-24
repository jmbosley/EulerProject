# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 16:31:11 2018

@author: Julie
"""

answer = 1

for a in range(2+1): # 100 p coin
    for b in range(int(1+(200-a*100)/50)): # 50 p coin
        for c in  range(int(1+(200-a*100-b*50)/20)): # 20 p coin
            for d in  range(int(1+(200-a*100-b*50-c*20)/10)): # 10 p coin
                for e in  range(int(1+(200-a*100-b*50-c*20-d*10)/5)): # 5 p coin
                    for f in  range(int(1+(200-a*100-b*50-c*20-d*10-e*5)/2)): # 2 p coin
                        answer = answer + 1
print(answer)