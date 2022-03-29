# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:52:06 2022

@author: Vishal
"""

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#load the dataset
dataset = pd.read_csv('./datasets/trainingdata.txt', header=None)

#Plot the graph with the data
plt.plot(dataset.iloc[:,0], dataset.iloc[:,1], 'ro')
plt.ylabel('Laptob Battery Life')
plt.show()

# According to the chart, we must remove items with a 
# duration of time greater than eight.
dataset = dataset[dataset.iloc[:,1] < 8]

# Add bias
dataset.insert(0, len(dataset.columns), 0)

# Separe variables dependet and independent
X = dataset.iloc[:,0:2].values
Y = dataset.iloc[:,2].values

# Create the classifier model
model = linear_model.LinearRegression()
model.fit(X, Y)

# Set new value to predict
timeCharged = float(input().strip())

result = model.predict([[0, timeCharged]])
if result[0] > 8:
    print (8.0)
else:
    print (round(result[0],2))