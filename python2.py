# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:37:59 2024

@author: s_woeste22
"""

def teilbar(x, y):
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen")
    elif x == y:
        print("x und y sind gleich")
    else:
        if x%y == 0:
            print("x ist durch y teilbar")
        else: 
            print("x ist nicht durch y teilbar")
            
teilbar(10, 3)
