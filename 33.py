# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:14:36 2020

@author: AVANI
"""

from collections import deque
import re

oprt = "+-/*"
parenthesis = "()"
priority = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

def higher_priority(opt1, opt2):
    return priority[opt1] >= priority[opt2]

print(higher_priority('*','-'))
print(higher_priority('+','-'))
print(higher_priority('+','*'))
print(higher_priority('+','/'))
print(higher_priority('*','/'))
