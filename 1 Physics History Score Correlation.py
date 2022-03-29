# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:28:59 2022

@author: Vishal
"""
import math as m

# mean function
def mean(data):
    return sum(data)/ len(data)

def var(data):
    sum = 0
    for i in range(len(data)):
        sum = sum + (data[i] - mean(data)) ** 2
    return sum

def cov(dt1, dt2):
    sum = 0
    for i in range(len(dt1)):
        sum += (dt1[i] - mean(dt1)) * (dt2[i] - mean(dt2))
    return sum

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

var_physics = var(physics)
var_history = var(history)

cov = cov(physics, history)
std = m.sqrt(var_physics * var_history)

# correlation 
r = cov/std
print(round(r,3))
