#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="this is dheeraj"


# In[3]:


range(len(a))


# In[9]:


for i in range(1,len(a)):
    print(a[-i])


# In[23]:


j=len(a)
for i in range(len(a)):
    b=[]
    b.append(a[i-j::-1])
print(b)


# In[1]:


a=[1,2,3,"dheeraj",8,9,"hero"]


# In[13]:


for i in a:
    b=[]
    if type(i)==str:
        for j in range(len(i)):
            b.insert(j,i[j])
        print(b)


# In[16]:


a= int(input("enter the marks of the student"))
if a==45:
    print ("the name is in the list")
elif a==40:
    print("you are in the list")
else:
    print("sorry try next tym")


# In[18]:


range(6)


# In[19]:


len(range(6))


# In[20]:


a=range(6)


# In[21]:


a


# In[22]:


a=list(range(6))


# In[23]:


a


# In[49]:


for i in range(1,len(a)):
    for j in range(len(a)):
        print(a[i])


# In[50]:


a=[1,2,3,4,5]


# In[51]:


a


# In[61]:


b=[]
for i in range(len(a)):
    for j in a:
        b.insert(i,a[i])
        print(b)


# In[57]:


range(len(a))


# In[2]:


a=[1,2,3,4,5]


# In[12]:


for i in range(len(a)):
    b=[]
    for j in a:
        print (b.insert(a[i-j::]))


# In[14]:


a=[1,2,3,"dheeraj",8,9,"hero"]


# In[15]:


for i in a:
    b=[]
    if type(i)==str:
        for j in range(len(i)):
            b.insert(j,i[j])
        print(b)


# In[16]:


a=[1,2,3,4,5]


# In[17]:


for i in a:
    print (a[i])


# In[1]:


a=[1,2,3,4,5]


# In[3]:


for i in a:
    print (i)


# In[28]:


b=[]
for j in range(len(a)):
    b.insert(j,a[j])
    print(b)


# In[ ]:





# In[57]:


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end =" ")
    print()


# In[58]:


l=["name","email","phoneno","address"]
for i in l:
    print(i)


# In[59]:


d="dheeraj"
for i in d:
    print(i)


# In[60]:


l


# In[61]:


for i in l:
    print(i)
else:
    print('loop is not going to complete if it will come to else')


# In[62]:


a=1
while a<9:
    print(a)
    a=a+1


# In[65]:


a=1
while a<5:
    print(a)
    a=a+1
    if a==3:
        continue
   


# In[67]:


while a<5:
       pass


# In[68]:


range(6)


# In[69]:


list(range(6))


# In[70]:


range(0,7)


# In[71]:


list(range(4,100))


# In[73]:


list(range(3,10,2))


# In[74]:


list(range(3,10,-1))


# In[75]:


list(range(10,6,-1))


# In[77]:


list(range(10,-5,-2))


# In[79]:


for i in range(10,-5,-2):
    print (i)


# In[80]:


n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*", end = "")
    print("\r")


# In[ ]:




