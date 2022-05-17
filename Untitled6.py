#!/usr/bin/env python
# coding: utf-8

# In[1]:


d1={"key1":[1,2,3,4],"key2":[2,3,4,5],"kumar":45}


# In[2]:


d1["key1"]


# In[3]:


type(d1)


# In[4]:


d1["key1"][0]


# In[6]:


d3={"+++":"done"}


# In[7]:


d4={"name":"dheeraj","mob no":897565645,"mail id":"dheerajkumar1234.com"}


# In[8]:


d4


# In[9]:


type(d4["name"])


# In[10]:


type(d4["mob no"])


# In[11]:


d4.keys()


# In[12]:


d4.values()


# In[13]:


d4.items()


# In[15]:


d={'key1':"dhee",'key2':[1,2,3,5]}


# In[16]:


d


# In[17]:


d["key3"]="kumar"


# In[18]:


d


# In[19]:


d[4]=[2,3,4,5]


# In[20]:


d


# In[21]:


d["key1"]=1


# In[22]:


d


# In[25]:


del d["key1"]


# In[26]:


d


# In[27]:


d1={"key1":"dhee","key2":[4,5,6,7]}


# In[28]:


d1[[1,2,3,4]]="practical"


# In[30]:


d1[(1,2,3,4)]="practical"


# In[31]:


d1


# In[32]:


d1.get("key1")


# In[33]:


d1={'key1':"practice",'key2':"fsd"}


# In[34]:


d2={'key3':123,"key4":[1,2,3,4]}


# In[1]:


d1={"key1":"practice","key2":"fsd"}
d2={"key3":123,"key4":[1,2,3,4]}


# In[2]:


d1+d2


# In[3]:


l=[1,2,3,4]
l.append(l)


# In[4]:


l


# In[5]:


l[2]


# In[6]:


d2=("dheeraj",1,1+2j,3.4,True)
d2.index(True)


# In[1]:


d1={"key1":34,"key2":"dheeraj","key3":(1,2,3,4,5)}


# In[2]:


d1.fromkeys()


# In[3]:


key1=("name","mobie no", "email id")
value="dheeraj"


# In[6]:


d=d1.fromkeys(key1,value)


# In[5]:


d1


# In[7]:


d


# In[ ]:




