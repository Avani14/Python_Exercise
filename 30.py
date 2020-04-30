# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:47:42 2020

@author: AVANI
"""

def permutation(lst):
    if len(lst) == 0: 
        return [] 
    if len(lst) == 1: 
        return [lst] 
    l = [] 
  for i in range(len(lst)): 
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 

       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 

data = list('Avani') 
for p in permutation(data): 
    print (p)