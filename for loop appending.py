#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[2,3,4,"dheeraj",7+6j,[34,22,56]]


# In[2]:


for i in l:
    if type(i)==int:
        print(i)
    


# In[3]:


for i in l:
    if type(i)==int:
        print(i)
    elif type(i)==list:
        for j in i:
            if type(j)==int:
                print(j)


# In[4]:


l=[2,45,66,12,"dheeraj",6+7j,[34,45,78,"dshd"]]


# In[6]:


for i in l:
    print(i)


# In[15]:


for i in range(len(l)):
    print("index",i,"for an element",l[i])


# In[16]:


for i in enumerate(l):
    print(i)


# In[19]:


for i in range(len(l)):
    print(i,l[i])


# In[20]:


l


# In[26]:


for i in l:
    if type(i)==str:
        print(i)
    elif type(i)==list:
        if type(i)==str:
            print (i)


# In[29]:


for i in l:
    if type(i)==str:
        l1=[]
        for j in i:
            l1.append(j)
        print(l1)


# In[34]:


for i in l:
    if type(i)==str:
        l1=[]
        for j in i:
            l1.append(j)
    elif type(i)==list:
        for k in i:
            if type(k)==str:
                l1.append(k)
print(l1)


# In[40]:


l1=[]
for i in l:
    if type(i)==int:
        l1.append(i**2)
    elif type(i)==list:
        l2=[]
        if type(i)==int:
            l2.append(i**2)
print(l2.append(l1))
        


# In[36]:


l


# In[ ]:




