#!/usr/bin/env python
# coding: utf-8

# In[1]:


def test(a,b,c,d,e):
    return a,b,c,d,e


# In[2]:


test(1,2,3,4,5)


# In[8]:


def test1(*args):
    return args


# In[9]:


test1(2,45,6,6)


# In[10]:


test1(45,"dheeraj",87)


# In[11]:


test1([1,2,3,4],(65,67,87),"gdjd",45+7j)


# In[12]:


def test2(*dk):
    return dk


# In[13]:


test2([1,2,3,4],(54,56,67))


# In[16]:


def test3(*l,a=98):
    return l,a
    


# In[17]:


test3(43,44,67)


# In[19]:


def test4(*dk,a,b,c,d):
    return dk,a,b,c,d


# In[20]:


test4(343,556,333,a="dheeraj",b=67,c="kumar",d=90)


# In[23]:


def test5(a,*dk,b,c):
       return a,dk,b,c


# In[24]:


test5(45,"dk",6483,344,334,67,99,b=90,c=70)


# In[36]:


def test6(*a):
    c=[]
    for i in a:
        if type(i)==list:
            c.append(i)
    return c


# In[37]:


test6([1,2,3,4],(5,6,7,8),"dheeraj",90+9j,[23,45,78,99])


# In[38]:


type(test6)


# In[41]:


type(test6())


# In[42]:


type(print)


# In[50]:


def test7(**a):
    if type(a)==dict:
        return a
    else:
        print ("this is not dictionary")


# In[57]:


test7(a=1,b=2,c=3)


# In[53]:


test7(a=56,b="dheeraj")


# In[55]:


def test8(**d):
    return d


# In[56]:


test8(a=10,b=90,c="dheeraj",d="kumar")


# In[58]:


def test9(**a):
    return a


# In[59]:


test9(name="dheeraj",age=27,phone=8034,adress="delhi")


# In[62]:


def test10(a,**dk):
    return dk,a


# In[64]:


test10(45,c=33,d=22,e=22)


# In[66]:


def test11(a,*ar,**args):
    return a,ar,args


# In[68]:


test11(23,(53,45,66,77,8,4,6,5),b=54,t=98)


# In[70]:


def test12(a,b):
    return a*b


# In[71]:


test12(1,4)


# In[74]:


a=lambda a,b :a*b


# In[75]:


a(56,9)


# In[77]:


a=lambda a,b:(a*b,a+b)


# In[78]:


a(2,3)


# In[79]:


a(4,5)


# In[82]:


x=lambda x:[print(i) for i in x]


# In[84]:


x([12,34,55,43])


# In[85]:


x=lambda x:[i for i in x]


# In[86]:


x([12,34,55,43])


# In[87]:


x=lambda x:[i for i in x]


# In[89]:


x([45,34,5])


# In[90]:


a=lambda **kwargs:kwargs


# In[91]:


a(a=45,b=67)


# In[102]:


a=10
def test16(c,d):
    c=5
    return c*d


# In[103]:


test16(a,50)


# In[104]:


l=[1,2,3,4,5,6,7]
l1=[]
for i in l:
    l1.append(i+2)


# In[105]:


l1


# In[107]:


def test17(a):
    l1=[]
    for i in a:
        l1.append(i+2)
    return l1


# In[108]:


test17(l)


# In[109]:


a=lambda a:[i+2 for i in a]


# In[110]:


a(l)


# In[111]:


l


# In[112]:


[i+2 for i in l]


# In[113]:


[i+2 for i in l if i<4]


# In[116]:


l1=[]
for i in l:
    if i<4:
        l1.append((i**2,i+i))    


# In[117]:


l1


# In[119]:


{i:i**2 for i in range(1,10)}


# In[121]:


d1={}
for i in range(1,10):
    d1[i]=i**2


# In[122]:


d1


# In[123]:


#tuple comprehension
(i for i in range(10))


# In[124]:


tuple(i for i in range(10))


# In[125]:


a=56
for i in a:
    print (i)


# In[126]:


d="dhee"
for i in d:
    print (i)


# In[127]:


next(d)


# In[128]:


b=iter(d)


# In[129]:


b


# In[131]:


next(b)


# In[132]:


next(b)


# In[133]:


next(b)


# In[134]:


s="ddsfsfdfsf"
for i in s:
    print(i)


# In[136]:


s=iter(d)


# In[137]:


next(s)


# In[138]:


next(s)


# In[139]:


next(s)


# In[140]:


next(s)


# In[141]:


next(s)


# In[142]:


l=[2,3,4,5]


# In[144]:


iter(45)


# In[145]:


l


# In[149]:


l=iter(l)


# In[150]:


next(l)


# In[151]:


next(l)


# In[152]:


next(l)


# In[153]:


next(l)


# In[154]:


next(l)


# In[ ]:




