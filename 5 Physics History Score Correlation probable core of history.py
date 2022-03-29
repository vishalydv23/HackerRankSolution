# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:58:09 2022

@author: Vishal
"""
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
cov = cov(physics, history)

# slope = covariance(x,y)/variance(x)
# correlation 
slope = cov/var_physics

# physics is x, variable independent
# history is y, variable dependent
# constant = mean(y) - slope * mean(x)
constant = mean(history) - slope * mean(physics)

# Y = slope * X + constant
result = slope * 10 + constant
print(round(result,1))