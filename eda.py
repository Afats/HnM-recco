# EDA replica of eda.ipynd notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import re
import warnings
warnings.filterwarnings('ignore')

# Importing data
articles = pd.read_csv('articles.csv')
# print(article_df.head())
customers = pd.read_csv('customers.csv')
# print(customer_df.head())
transactions = pd.read_csv('transactions.csv')

# ----- empty value stats -------------

print("Missing values: ")
print(customers.isnull().sum())
print("--")

print("FN Newsletter vals: ", customers['FN'].unique())
print("Active communication vals: ",customers['Active'].unique())
print("Club member status vals: ", customers['club_member_status'].unique())
print("Fashion News frequency vals: ", customers['fashion_news_frequency'].unique())
# print("Age vals: ", customers['age'].unique())
print("--")

# ---- data cleaning -------------
customers['FN'] = customers['FN'].fillna(0.0)
customers['Active'] = customers['Active'].fillna(0)

# replace club_member_status missing values with 'PRE-CREATE' (assuming that the customer has not yet created an account)
customers['club_member_status'] = customers['club_member_status'].fillna('PRE-CREATE')
customers['fashion_news_frequency'] = customers['fashion_news_frequency'].fillna('None')
customers['fashion_news_frequency'] = customers['fashion_news_frequency'].replace('NONE', 'none')
customers['age'] = customers['age'].fillna(customers['age'].mean())
customers['age'] = customers['age'].astype(int)
articles['detail_desc'] = articles['detail_desc'].fillna('None')

print("Missing values: ")
print(customers.isnull().sum())
print("--")