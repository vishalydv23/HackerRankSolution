# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:44:39 2022

@author: Vishal
"""

from sklearn import linear_model

f, n = input().split()
f = int(f)
n = int(n)

model = linear_model.LinearRegression()
x_train = []
y_train = []

for i in range(n):
    tmp = [float(n) for n in input().split()]
    x_train.append(tmp[0:len(tmp) - 1])
    y_train.append(tmp[len(tmp) - 1])
    
model.fit(x_train, y_train)

x_test = []
n = int(input())
for i in range(n):
    tmp = [float(n) for n in input().split()]
    x_test.append(tmp)
    
y_test = model.predict(x_test)
for y in y_test:
    print(y)