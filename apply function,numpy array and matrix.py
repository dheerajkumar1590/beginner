#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.DataFrame({'col1':[1,2,3,4,5],
             'col2':[45,66,55,43,22],
             'col3':"dheeraj kumar dheeru delhi"             })


# In[3]:


"dheeraj kumar dheeru delhi".split()


# In[4]:


df=pd.DataFrame({'col1':[1,2,3,4,5],
             'col2':[45,66,55,43,22],
             'col3':"dheeraj kumar dheeru delhi hero".split()            
             })


# In[5]:


df


# In[6]:


df['col4']=df['col1']**2


# In[7]:


df


# In[8]:


df['col5']=df['col3'].str[0]


# In[9]:


df


# # Apply function

# In[10]:


def test(a):
    return a**2


# In[11]:


df['col_4']=df['col1'].apply(test)


# In[12]:


df


# In[13]:


def change(a):
    if a=="d":
        return "s"
    else:
        return "z"


# In[14]:


df['col6']=df["col5"].apply(change)


# In[15]:


df


# In[16]:


x = lambda a, b : a * b
print(x(5, 6))


# In[17]:


df["col_6"]=df["col5"].apply(lambda a:"s"if a=="d" else "z")


# In[18]:


df


# In[ ]:





# In[19]:


df["col7"]=df["col3"].apply(lambda a:len(a))


# In[20]:


df


# In[21]:


import math


# In[22]:


df["col8"]=df["col2"].apply(math.log)


# In[23]:


df


# # Numpy package

# In[24]:


import numpy as np


# In[25]:


l=["dheeraj",1,2,3,4]


# In[26]:


type(l)


# In[27]:


np.array(l)


# In[28]:


type(np.array(l))


# In[29]:


a1=np.array([3,4,5,6,3.0])


# In[30]:


a=np.array([[1,2],[3,4]])


# In[31]:


a


# In[32]:


a[1][1]


# In[33]:


a1


# In[34]:


a1[1]


# In[35]:


a2=np.array([[[[1,2,3,4]]]])


# In[36]:


a2


# In[37]:


a2[0]


# In[38]:


a2[0][0]


# In[39]:


a2[0][0][0][0]


# In[40]:


np.asarray([1,2,3,4])


# In[41]:


np.asanyarray([1,2,3,4])


# # Matrix

# In[42]:


np.mat([1,2,3,4,5])


# In[43]:


a=[1,2,3,4,5]
np.asarray(a)


# In[44]:


np.asanyarray(a)


# In[45]:


np.mat(a)


# In[46]:


np.asanyarray(np.mat(a))


# In[47]:


np.fromfunction(lambda i,j:i==j,(3,3))


# In[48]:


np.fromfunction(lambda i,j:i*j,(4,4))


# In[49]:


#converting the above output from floating to int type
np.fromfunction(lambda i,j:i*j,(4,4),dtype=int)


# In[56]:


a=np.fromfunction(lambda i,j,z:i*j*z,(4,3,2),dtype=int)


# In[57]:


a


# In[58]:


a.ndim


# In[59]:


a.size


# In[60]:


a.dtype


# In[61]:


import pandas as pd


# In[63]:


b=np.fromfunction(lambda i,j:i*j,(4,4),dtype=int)


# In[64]:


b


# In[65]:


pd.DataFrame(b)


# In[66]:


np.random.rand(4,5)


# In[75]:


np.random.rand(4,5)


# In[76]:


np.random.randn(4,5)


# In[79]:


np.random.randint(4,100)


# In[80]:


a


# In[83]:


pd.DataFrame(a.reshape(4,6))


# In[84]:


a.reshape(12,-1)


# In[ ]:




