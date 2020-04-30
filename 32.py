# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:47:43 2020

@author: AVANI
"""

def AddWithoutPlusOperator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
print(AddWithoutPlusOperator(5,9))
