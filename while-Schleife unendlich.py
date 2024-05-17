# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:25:04 2024

@author: s_woeste22
"""

a = 1 
r = 0.5
s = 0
k = 0 
grenzwert = 1/(1-r)
epsilon = 0.0001
while True:
    s += a * r**k 
    k += 1
    print(s, end = " ")
    if (grenzwert - s) < epsilon:
        break
    
    