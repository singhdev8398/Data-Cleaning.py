#!/usr/bin/env python
# coding: utf-8

# # Data cleaning by Delete Row & columns

# In[1]:


import numpy as np 
import matplotlib.pyplot as  plt 
import pandas as pd
import seaborn as sns 
import math


# In[2]:


df=pd.read_csv("D:\dataset\House_price_dataset.csv")
df


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.isnull()


# In[8]:


df.isnull().sum()


# In[9]:


plt.figure(figsize=(10,10))
sns.heatmap(df.isnull())


# In[10]:


df.isnull().sum()/df.shape[0]*100


# In[11]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[12]:


df.isnull().sum()


# In[13]:


null_var=df.isnull().sum()/df.shape[0]*100
null_var


# In[16]:


drop_columns= null_var[null_var>15].keys()
drop_columns


# In[17]:


df1_drop_column=df.drop(columns=drop_columns)
df1_drop_column


# In[18]:


df1_drop_column.shape


# In[19]:


df1_drop_column.isnull().sum()


# In[22]:


plt.figure(figsize=(10,10))
sns.heatmap(df1_drop_column.isnull())


# In[23]:


df2_drop_rows=df1_drop_column.dropna()
df2_drop_rows


# In[24]:


df2_drop_rows.shape


# In[25]:


df2_drop_rows.isnull().sum().sum()


# In[26]:


plt.figure(figsize=(25,25))
sns.heatmap(df2_drop_rows.isnull())


# In[29]:


df2_drop_rows.select_dtypes(include=["int64","float64"]).columns


# In[31]:


sns.distplot(df["MSSubClass"])


# In[32]:


sns.distplot(df2_drop_rows["MSSubClass"])


# In[33]:


sns.distplot(df["MSSubClass"])
sns.distplot(df2_drop_rows["MSSubClass"])


# In[34]:


num_var=[ 'MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
       'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
       'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
       'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
       'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
       'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
       'MoSold', 'YrSold']


# In[51]:


plt.figure(figsize=(25,25))
for i, var in enumerate(num_var):
    plt.subplot(9,4,i+1)
    sns.histplot(df[var],bins=20)
    sns.histplot(df2_drop_rows[var],bins=20,color="red")


# In[94]:


df2_drop_rows.select_dtypes(include=['object']).columns


# In[95]:


df['MSZoning'].value_counts()


# In[101]:


a=df[var].value_counts()/df.shape[0]*100


# In[102]:


b=df2_drop_rows[var].value_counts()/df2_drop_rows.shape[0]*100


# In[ ]:



   


# In[103]:


def cat_var_dist(var):
    return pd.concat([a,b],axis=1,keys=[var+'org',var+'clean'])


# In[104]:


cat_var_dist('BsmtCond')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




