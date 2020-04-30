# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:22:39 2020

@author: AVANI
"""

def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(6,7,'x'))
print(pythagoras(5,'x',7))
print(pythagoras('x',7,8))
print(pythagoras(6,7,8))