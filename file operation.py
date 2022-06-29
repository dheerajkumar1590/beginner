#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open("test2.txt")


# In[2]:


f.read()


# In[3]:


f.tell()


# In[4]:


f.seek(5)


# In[6]:


f.tell()


# In[7]:


f.close()


# In[9]:


f=open("test2","r+")


# In[14]:


f.seek(0)


# In[15]:


f.readline()


# In[17]:


f.seek(0)


# In[18]:


f.readline()


# In[19]:


f.readline()


# In[20]:


f.seek(0)


# In[21]:


f.read()


# In[22]:


f.close()


# In[24]:


f=open("test2","r+")


# In[25]:


f.read()


# In[26]:


f.readline()


# In[27]:


f.seek(0)


# In[28]:


f.readline()


# In[29]:


f.readline()


# In[30]:


f.readline()


# In[32]:


f=open("google.txt","w")


# In[34]:


f.write("""Googlers are committed to exploring how artificial intelligence (AI) can accelerate the ways gender inequities are tackled across industries. From recognizing female leaders lost in historical scientific archives, to improving women patient outcomes, to identifying gender disparities on screen — this is only the beginning. The potential of what AI can achieve is promising, spanning many more sectors and other identities beyond gender.
""")


# In[35]:


f.close()


# In[36]:


f=open("google.txt","r+")


# In[37]:


f.read()


# In[38]:


f.seek(0)


# In[39]:


f.readline()


# In[40]:


f.readline()


# In[41]:


f.readline()


# In[42]:


f.close()


# In[44]:


f=open("google.txt","r+")
for line in f:
    print(line,end="")


# In[45]:


f.write("""this is extra writing in this file """)


# In[46]:


f.read()


# In[47]:


f.seek(0)


# In[48]:


f.read()


# In[49]:


f.close()


# In[51]:


f=open("google.txt","r+")


# In[52]:


f.read()


# In[53]:


f.seek(6)


# In[54]:


f.write("this is the 6th position")


# In[55]:


f.read()


# In[56]:


f.seek(0)


# In[57]:


f.read()


# In[60]:


f.close()


# In[65]:


f=open("google.txt","r+")


# In[66]:


len(f.readlines())


# In[69]:


f.seek(0)


# In[70]:


l=f.readlines()


# In[71]:


l


# In[72]:


l[0]


# In[73]:


l[0].split()


# In[76]:


l1=[]
for i in l[0].split():
    l1.append(i[0]) 


# In[77]:


l1


# In[78]:


get_ipython().system('ls')


# In[79]:


f=open("google.txt","r+")


# In[80]:


f.name


# In[81]:


l=["this is my line one","this is my line two","this is my line3","this is my line 4"]


# In[82]:


f.write("i can write lines at curent cursor")


# In[83]:


f.writelines(l)


# In[84]:


f.close


# In[85]:


f.close()


# In[1]:


f= open("google.txt","r+")


# In[3]:


f.fileno()


# In[4]:


get_ipython().run_line_magic('ls', '')


# In[5]:


import os


# In[6]:


os.remove("google.txt")


# In[7]:


get_ipython().run_line_magic('ls', '')


# In[9]:


os.getcwd()


# In[10]:


os.listdir()


# In[12]:


os.getcwd()


# In[13]:


import os
os.listdir()


# In[14]:


pwd()


# In[15]:


os.listdir(/Users/dheerajkumar)


# In[ ]:




