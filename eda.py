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
print(article_df.head())

customer_df = pd.read_csv('customers.csv')
print(customer_df.head())

# Data preprocessing

# fill out missing values in customer_df



