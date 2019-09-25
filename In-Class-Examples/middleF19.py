# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:36:39 2019

@author: David.McGinn, Michael Lewis & Yujin Yoshimura
"""

# Returns all but first and last item
def middle(t):
    L = t[1:-1]
    return L

#Returns only middle item or middle two items
def middleItem(t):
    
    if len(t) % 2 == 0:
        m = len(t)// 2
        return (t[m-1], t[m])
    else:
        m = len(t) // 2
        return t[m]
    
#Returns only middle item or middle two items
def middleItem2(t):
    m = (len(t) - 1) // 2
    L = t[m:-m]
    return L
    
t = [1]
print(middle(t))
print(middleItem(t))
print(middleItem2(t))