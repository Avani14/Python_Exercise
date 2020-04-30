# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:30:29 2020

@author: AVANI
"""

import itertools
from functools import partial
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

def check_sum(n, *nums):
  if sum(i for i in nums) == n:
    return (True, nums)
  else:
      return (False, nums)
pro = itertools.product(X,Y,Z)
func = partial(check_sum, T)
sums = list(itertools.starmap(func, pro))

result = set()
for s in sums:
    if s[0] == True and s[1] not in result:
      result.add(s[1])
      print(result)
