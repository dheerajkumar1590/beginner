#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[2]:


url='https://api.github.com/repos/pandas-dev/pandas/issues'


# In[4]:


pd.read_json(url)


# In[5]:


import requests
url='https://api.github.com/repos/pandas-dev/pandas/issues'


# In[6]:


data=requests.get(url)


# In[7]:


data


# In[9]:


data1=data.json()


# In[10]:


data1


# In[11]:


pd.DataFrame(data1)


# In[15]:


df=pd.DataFrame(data1,columns=['url','repository_url','label_url','user'])


# In[16]:


df.to_excel('practice.xlsx')


# In[19]:


len(data1)


# In[20]:


data1[0]['user']


# In[24]:


a=[]
for i in range(len(data1)):
    a.append(data1[i]['user'])
print(a)


# In[25]:


df2=pd.DataFrame(a)


# In[26]:


df2


# In[67]:


df3=pd.DataFrame.merge(df,df2)


# In[68]:


df3.to_excel('practice.xlsx')


# In[69]:


url1='https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'


# In[3]:


df4=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[4]:


type(df4)


# In[5]:


len(df4)


# In[6]:


df4.head()


# In[7]:


df4.tail(3)


# In[8]:


df4.dtypes


# In[9]:


df4.info()


# In[10]:


df4.describe()


# In[11]:


df4.columns


# In[12]:


df4.dtypes == "object"


# In[13]:


type(df4.dtypes)


# In[15]:


df4.dtypes[df4.dtypes == "object"]


# In[17]:


col_name=df4.dtypes[df4.dtypes == "object"].index


# In[18]:


col_name


# In[20]:


df4[col_name]


# In[22]:


df4[col_name].describe()


# In[23]:


df4


# In[24]:


df4["dk club"]="dheeraj"


# In[25]:


df4


# In[26]:


df4["Name"]


# In[28]:


df4.head(15)


# In[30]:


df4["Name"][0:15]


# In[31]:


df4["Name"][0:15:2]


# In[32]:


df4["Name"][::-1]


# In[33]:


df4


# In[37]:


df4[df4["Age"].isnull()==True].index


# In[39]:


len(df4[df4["Age"].isnull()==True].index)


# In[41]:


ind=df4[df4["Age"].isnull()==True].index


# In[42]:


df4.loc[ind]


# In[46]:


df4[df4["Age"].isnull()]


# In[49]:


max(df4["Fare"])


# In[51]:


df4[df4["Fare"]==max(df4["Fare"])]["Name"]


# In[52]:


df4[df4["Fare"]== max(df4["Fare"])]


# In[53]:


df4.head()


# In[68]:


df4["Sex"]


# In[84]:


col1_name=df4.dtypes[df4.dtypes == "object"].index


# In[85]:


col1_name


# In[87]:


col1_name[1]


# In[89]:


df4[col1_name[1]]


# In[91]:





# In[ ]:




