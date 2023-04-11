import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os
import re
import warnings

from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

articles = pd.read_csv('articles.csv')
# print(articles.head())
# print("--")
customers = pd.read_csv('customers.csv')
# print(customers.head())
# print("--")
transactions = pd.read_csv("transactions_train.csv")

# combine transactions, articles and customers to find sgd (easier)
# too much data - need to modify training set
# print(customers['customer_id'])
merged_df = pd.merge(transactions, articles, on='article_id')
merged_df_final = pd.merge(merged_df, customers, on='customer_id') 

# change this
# X matrix
x = merged_df_final

# y vector
y = merged_df_final['target']
#print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=25)
sgd = SGDClassifier(alpha=0.01, max_iter=200)
sgd.fit(x_train,y_train)
