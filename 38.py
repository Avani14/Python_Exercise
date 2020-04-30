# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:37:39 2020

@author: AVANI
"""

def fact(n):
  a = n // 5
  b = a
  while a > 0:
    a /= 5
    b += int(a)
  return b
       
print(fact(11))
print(fact(54))
print(fact(98))