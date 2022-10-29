#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ls


# In[3]:


pd.read_csv("sample.csv")


# In[4]:


type(d)


# In[7]:


pd.read_csv("sample.csv",header=None)


# In[4]:


pd.read_csv("sample.csv",names=['a','b','c','d','e','f','g','h','i'])


# In[5]:


pd.read_csv("sample.csv",names=['a','b','c','d','e','f','g','h','i','j','k'])


# In[17]:


pd.read_csv('sampletestcopy.csv')


# In[18]:


df=pd.read_csv('sampletestcopy.csv')


# In[19]:


df["name"]


# In[22]:


df1=pd.read_csv('sampletestcopy.csv',skiprows=[1,3])


# In[23]:


df1


# In[24]:


df.dtypes


# In[25]:


type(df)


# In[27]:


df.head()


# In[28]:


df.tail()


# In[29]:


df.tail(3)


# In[30]:


df.columns


# In[33]:


a=df['emailid']


# In[34]:


type(a)


# In[37]:


b=df[['emailid','name']]


# In[38]:


type(b)


# In[39]:


type(df[['name']])


# In[40]:


ls


# In[10]:


pd.read_excel('sampleex.xlsx')


# In[8]:


pip install openpyxl


# In[52]:


pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[ ]:




