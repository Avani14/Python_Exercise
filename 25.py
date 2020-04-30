# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:36:30 2020

@author: AVANI
"""

def freq(str1):
    dict = {};
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1;
        else:
            dict[n]=1;
    return dict;
print(freq("Avani Trivedi"))