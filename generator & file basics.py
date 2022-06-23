#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[1,2,3,4]


# In[5]:


l=iter(l)


# In[6]:


next(l)


# In[7]:


next(l)


# In[8]:


next(l)


# In[9]:


next(l)


# In[10]:


next(l)


# In[11]:


a=56


# In[12]:


next(a)


# In[13]:


a=iter(a)


# In[14]:


b=(1,2,3,4)


# In[15]:


next(b)


# In[17]:


b=iter(b)


# In[19]:


next(b)


# In[20]:


next(b)


# In[21]:


next(b)


# In[22]:


next(b)


# In[24]:


r=range(6)


# In[26]:


next(r)


# In[28]:


r=iter(r)


# In[29]:


next(r)


# In[30]:


next(r)


# In[31]:


next(r)


# In[32]:


next(r)


# In[33]:


next(r)


# In[34]:


"""Generator : kind of object to hold the info of prevous data set which you have generated and the logic of the data set so that u can generate another data of same logic""" 
range(45)


# In[36]:


list(range(0,45,3))


# In[40]:


def cube(n):
        return n**3


# In[41]:


cube(3)


# In[42]:


cube(6)


# In[45]:


def cube1(n):
    l=[]
    for i in range(n):
        l=l.append(i**3)
    return l


# In[46]:


cube1(6)


# In[1]:


def gencube(n):
    for i in range (n):
        yield i**3
    


# In[2]:


gencube(10)


# In[3]:


gencube(9)


# In[4]:


for i in gencube(9):
    print(i)


# In[10]:


def fibo(n):
    a=1
    b=1
    for i in range(n):
        yield a,i
        a,b=b,a+b


# In[11]:


for i in fibo(10):
    print(i)


# In[12]:


def fibo1(n):
    a=1
    b=1
    output=[]
    for i in range(n):
        output.append(a)
        a,b=b,a+b
    return output


# In[13]:


fibo1(9)


# In[1]:


print("something in cosole")


# In[2]:


f=open("test.txt","w")


# In[3]:


pwd()


# In[4]:


dir()


# In[5]:


get_ipython().system('ls')


# In[6]:


pwd()


# In[7]:


get_ipython().run_line_magic('ls', '')


# In[8]:


f=open("test2","w")


# In[9]:


f.write("this is my first file operation  in my test2.text")


# In[11]:


f.close()


# In[12]:


f=open("test2","w")


# In[13]:


f.write("hi this is my first operation related to file")


# In[14]:


f.close()


# In[15]:


get_ipython().run_cell_magic('writefile', 'test2.txt', 'this is a data i would like to store\n')


# In[16]:


get_ipython().run_line_magic('ls', '')


# In[21]:


f=open("test2")


# In[22]:


f.read()


# In[23]:


f=open('test2.txt')


# In[24]:


f.read()


# In[25]:


f.read()


# In[26]:


f.read()


# In[27]:


f.seek(5)


# In[28]:


f.read()


# In[ ]:




