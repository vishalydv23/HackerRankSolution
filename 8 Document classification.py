# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:16:20 2022

@author: Vishal
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('trainingdata.txt')
df.columns = ['text']
df['label'] = df['text'].apply(lambda x: x.split(' ')[0])
df['text'] = df['text'].apply(lambda x: x.split(' ', 1)[1].rsplit(' ', 2)[0])

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(df['text'])
X_train_counts.shape

tf_transformer = TfidfTransformer(use_idf=True).fit(X_train_counts)
X_train_tfidf = tf_transformer.transform(X_train_counts)
X_train_tfidf.shape

clf = MultinomialNB().fit(X_train_tfidf, df['label'])
predicted = clf.predict(X_train_tfidf)
sum(predicted == df['label'])/len(df)