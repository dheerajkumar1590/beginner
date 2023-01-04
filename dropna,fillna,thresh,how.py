#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


f=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[9]:


f


# In[10]:


f.dropna(axis=1)


# In[11]:


f.describe()


# In[12]:


f.isnull().sum()


# In[ ]:





# In[5]:


f.dropna()


# In[6]:


f.dropna(inplace=True)


# In[7]:


f


# In[13]:


f


# In[14]:


f.dropna(axis=1,thresh=800)


# In[15]:


f.dropna(axis=1,how='all')


# In[16]:


f.fillna('dhee')


# In[3]:


f.groupby("Survived").describe()


# In[4]:


#filtering out passenger id
f.groupby("Survived").describe()["PassengerId"]


# In[5]:


f.groupby("Survived").describe()["PassengerId"].T


# In[3]:


df=pd.read_csv('/Users/dheerajkumar/bank/bank.csv',sep=';')


# In[4]:


p=df[df["education"]=="primary"]


# In[5]:


s=df[df["education"]=="secondary"]


# In[6]:


t=df[df["education"]=="tertiary"]


# In[7]:


u=df[df["education"]=="unknown"]


# # concatanate operation

# In[11]:


pd.concat([p,s])


# In[44]:


p=p.head(5)


# In[45]:


s=s.head(5)


# In[16]:


pd.concat([p,s])


# In[17]:


pd.concat([p,s],axis=1)


# In[19]:


p.columns


# In[25]:


p=p.head(3)[['age', 'job', 'marital']]


# In[26]:


s=s.head(3)[['age', 'job', 'marital']]


# In[29]:


df2=pd.concat([p,s],axis=1)


# In[30]:


df2


# In[32]:


df2.iloc[:,3]


# In[33]:


s


# In[34]:


s.iloc[[1,2],[1,2]]


# In[35]:


p


# In[36]:


p.iloc[[1,2],[1,2]]


# # Merge operation

# In[8]:


p=p.head(5)[['age', 'job', 'marital']]


# In[9]:


s=s.head(5)[['age', 'job', 'marital']]


# In[10]:


p


# In[11]:


s


# In[12]:


pd.merge(p,s,on='age')


# In[13]:


pd.merge(p,s,on='age',how='left')


# In[14]:


pd.merge(p,s,on='age',how='right')


# In[17]:


pd.merge(p,s,on='age',how='outer')


# In[22]:


p=p.set_index('age')


# In[23]:


s=s.set_index('age')


# In[24]:


p


# In[25]:


s


# In[30]:


p.rename(columns={'job':'job1','marital':'marital1'},inplace=True)


# In[31]:


p.join(s)


# In[33]:


p


# In[34]:


p.join(s,how='inner')


# In[36]:


pd.merge(p,s,on= "age")


# In[38]:


pd.merge(p,s,left_on="job1",right_on='job')


# In[ ]:




