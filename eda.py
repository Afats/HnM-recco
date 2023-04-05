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
article_df = pd.read_csv('articles.csv')
# print(article_df.head())
customer_df = pd.read_csv('customers.csv')
# print(customer_df.head())

# Data pre-proccessing -------------

# ----- empty value stats -------------

# print out the number of missing values in each column
print(customer_df.isnull().sum())


print("FN Newsletter vals: ", customer_df['FN'].unique())
print("Active communication vals: ",customer_df['Active'].unique())
print("Club member status vals: ", customer_df['club_member_status'].unique())
print("Fashion News frequency vals: ", customer_df['fashion_news_frequency'].unique())
# print("Age vals: ", customer_df['age'].unique())

# ---- data cleaning -------------
customer_df['FN'] = customer_df['FN'].fillna(0.0)
customer_df['Active'] = customer_df['Active'].fillna(0)

# replace club_member_status missing values with 'PRE-CREATE' (assuming that the customer has not yet created an account)
customer_df['club_member_status'] = customer_df['club_member_status'].fillna('PRE-CREATE')
customer_df['fashion_news_frequency'] = customer_df['fashion_news_frequency'].fillna('None')
customer_df['fashion_news_frequency'] = customer_df['fashion_news_frequency'].replace('NONE', 'none')
customer_df['age'] = customer_df['age'].fillna(customer_df['age'].mean())
customer_df['age'] = customer_df['age'].astype(int)
article_df['detail_desc'] = article_df['detail_desc'].fillna('None')

print(customer_df.isnull().sum())
print(article_df.isnull().sum())





