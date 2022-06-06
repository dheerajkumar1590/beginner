#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[1,2,3,4,5,6,7]
for i in l:
    print(i)


# In[7]:


t=(1,2,3,4,5,6,7)
for i in range(len(t)):
    print(i,t[i])


# In[3]:


s="Dheeraj"
for i in s:
    print(i)


# In[8]:


t


# In[11]:


list(range(len(t),0,-1))


# In[20]:


for i in range(len(t)-1,-1,-1):
    print(t[i])


# In[21]:


d={"a":"fdss","b":"kumar","c":[1,2,3,4],"d":(7,8,9),"e":"dheeraj"}


# In[22]:


for i in d:
    print (i)


# In[24]:


for i in d:
    print(i,d[i])


# In[25]:


d.items()


# In[27]:


s={2,34,56,4,3,8,56,774,3,3,4,4}


# In[28]:


s


# In[32]:


for i in s:
    print (i)


# In[33]:


range(5)


# In[45]:


for i in range(1,6):
    for j in range(6-i,0,-1):
        print (j,end ="")
    print(" ")


# In[46]:


l=[10,20,30,40,50]


# In[51]:


len(l)


# In[54]:


for i in range (len(l)-1,-1,-1):
    print (l[i])


# In[56]:


range(len(l))


# In[63]:


a=25
b=50
for i in range(a,b+1):
    if i>1:
        for j in range(2,i,1):
            if i%j==0:
                break
        else:
            print(i)


# In[68]:


a=0
b=1
for i in range(10):
    print(a,end=" ")
    c=a+b
    a=b
    b=c


# In[90]:


print("pls enter the no. u want factorial")
a= int(input())
c=1
for i in range (1,a+1):
        c=c*i
print(c)
    


# In[80]:


range(5)


# In[ ]:




