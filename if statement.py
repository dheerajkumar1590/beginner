#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10


# In[6]:


a


# In[9]:


if a<15:
    pass


# In[7]:


a<15


# In[10]:


if a<15:
    print ("my name is Dheeraj")


# In[11]:


if 24<15:
    print("my ")


# In[12]:


24<15


# In[3]:


if 5<10:
    print ("dheeraj")
else:
    print("the statement is wrong")
            


# In[10]:


income=int(input())
if income<50:
    print("i will buy phone")
elif income<70:
    print("buy car")
elif income<90:
    print("buy anything")
else:
    print("donot buy anything")


# In[15]:


Total_price= int(input())
if Total_price>20000:
    discount=Total_price*.20
    print("Discount will be ",discount)
elif Total_price<=7000:
    discount= Total_price*.05
    print("Discount will be ",discount)
else:
    print("wont be able to give any discount")


# In[19]:


coup= input()


# In[21]:


coup= input()
if coup== "dheeraj5":
    print("you will be able to get a discount of 5%")
    amount=5000-5000*.05
    print("you have to pay only",amount)
else:
    print("kindly use another code")


# In[26]:


print("enter the cooupen code")
coup= input()
print("enter the amount of item")
amount=int(input())
if coup== "dheeraj5":
    print("you will be able to get a discount of 5%")
    pay_amount=amount-amount*.05
    print("you have to pay only",pay_amount)
else:
    print("kindly use another code")


# In[31]:


sthr=int(input())
if sthr<1:
    print("it will take 8 mnths of time for transition")
elif sthr<4 or sthr>1:
    print ("may take 6 mnths for transition")
elif sthr>10:
    print('it will take only 3 months for transition')
else:
    print("work hard")
    


# In[ ]:




