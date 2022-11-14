#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pip install --upgrade pip


# In[3]:


pip install lxml


# In[2]:


df=pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')


# In[3]:


type(df)


# In[4]:


type(df[0])


# In[5]:


df1=df[0]


# In[6]:


df1.columns


# In[7]:


pip install --upgrade pip setuptools wheel


# In[8]:


get_ipython().system('pip install my_package')


# In[11]:


df1.head()


# In[12]:


df1.tail(3)


# In[13]:


df1.dtypes


# In[14]:


df1[['Age','GS']]


# In[15]:


df1


# In[16]:


df1.to_csv('NBA.csv',index=False)


# In[13]:


ls


# In[16]:


l=pd.read_html('https://stats.espncricinfo.com/ci/engine/records/averages/batting.html?class=3;id=6;type=team')


# In[17]:


len(l)


# In[21]:


l[0].to_csv('cricket.csv',index=False)


# In[19]:


l[1].


# In[20]:


l[2]


# In[42]:


d="""
{"name":"dheeraj",
"email":"dk@gmail.com","tech":["ML","DL","CV"],
"platform":["technology","kids","self"]
}"""


# In[43]:


import json


# In[44]:


result=json.loads(d)


# In[45]:


result


# In[36]:


type(result)


# In[37]:


type(d)


# In[46]:


pd.DataFrame(result)


# In[49]:


result['name']


# In[50]:


#list to data frame conversion can be possible but string to dataframe conversion is not possible
pd.DataFrame(result["tech"])


# In[51]:


result['tech']


# In[17]:


url='https://api.github.com/repos/pandas-dev/pandas/issues'


# In[18]:


pd.read_json(url)


# In[19]:


"""loading a data in raw jason"""
import requests
url="https://api.github.com/repos/pandas-dev/pandas/issues"


# In[20]:


data=requests.get(url)


# In[21]:


data


# 200 is the code of success it simply means that i have requested something and it has been accepted.

# In[22]:


data1=data.json()


# In[23]:


data1


# In[24]:


len(data1)


# In[25]:


data1[0]


# In[41]:


data1[0]['user']


# In[27]:


data1[0]['user']


# In[ ]:





# In[16]:


data1[0]['user']['id']


# In[ ]:





# In[17]:


"""in this we are getting the user id """
for i in range(len(data1)):
    print(data1[i]['user']['id'])


# In[54]:


data1


# In[105]:


len(data1[0]['user'])


# In[109]:


a=[]
for i in range(len(data1)):
    a.append(data1[i]['user'])
a


# In[83]:


data1[0]['user']['login']


# In[129]:


df3=pd.DataFrame(data1,columns=['id','url','repository_url','label_url','user'])
df4=pd.DataFrame(a)


# In[137]:


pd.concat(df3,df4)


# In[138]:


df5


# In[124]:


df3.to_excel('try.xlx')


# In[132]:


df4


# In[80]:


df2=pd.DataFrame(data1,columns=['id','url','repository_url','label_url','user'])


# In[81]:


df2.to_csv('json.csv')


# In[82]:


ls


# In[ ]:




