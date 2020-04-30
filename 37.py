# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:22:43 2020

@author: AVANI
"""

def ndegrees(num):
  answ = True
  n, tempnum, i = 2, 2, 2
  while answ:
    if str(tempnum) in num:
      i += 1
      tempnum = pow(n, i)
    else:
      answ = False
  return i-1;
print(ndegrees("2481632"))
print(ndegrees("248163264"))