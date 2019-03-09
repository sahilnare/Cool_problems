# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 22:06:47 2019

@author: Sahil
"""

def move(fr,to):
    print("Move the top piece of " + fr + " to " + to)

def tower(n,fr,to,sp):
    if n == 1:
        move(fr,to)
    else:
        tower(n-1,fr,sp,to)
        tower(1,fr,to,sp)
        tower(n-1,sp,to,fr)

tower(3,"P1","P2","P3")