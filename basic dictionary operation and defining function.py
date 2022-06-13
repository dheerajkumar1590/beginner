#!/usr/bin/env python
# coding: utf-8

# In[3]:


s="this is a basic python class"
c=0
for i in s:
   c+=1
print (c)


# In[4]:


s[::-1]


# In[8]:


for i in range(len(s)-1,-1,-1):
        print(s[i])


# In[9]:


i=len(s)-1
while i>=0:
    print (s[i],end=" ")
    i=i-1


# In[10]:


s


# In[14]:


s="python"
v="AaEeIiOoUu"
for i in s:
    if i in v:
        print(i,"is a vowel")
    else :
        print(i, "is not a vowel")


# In[27]:


a=input('enter the word')
for i in range(len(a)) :
    if a[i]!=a[len(a)-i-1]:
        print("not palindrom")
        break
else:
    print("palindrom")
    


# In[29]:


a=input ("enter the word")
b=a[::-1]
if(a==b):
    print(a,"is a palindrom")
else:
    print(a,"is not a palindrom")


# In[31]:


a=input("enter the word")
b=""
i =
while len(b)<=len(a):
    b=b+a
if b==a:
    print(a,"is a palindrom")
else:
    print(a,"is not a palindrom")
    


# In[1]:


s=input("enter a word")
k=0
l=len(s)
for i in range(l):
    if s[i]==s[l-i-1]:
        continue
    else:
        print("Not palindrom")
        k=1
        break
if k==0:
    print("palindrome")


# In[2]:


d={"india":"IN","canada":"CA","china":"CH","united states":"US"}


# In[3]:


"india" in d


# In[10]:


d.keys()


# In[ ]:


a=[]
b=[]
for i in d:
    if len(i)<=5:
        a.append(i)
    else:
        b.append(i)


# In[17]:


a


# In[18]:


b


# In[31]:


d={"hi":{
    
            "a":12,
            "b":34,
            "c":45
            },
   "course":
           {
               "d":67,
               "e":55,
               "f":89
           }


  }


# In[65]:


a=d["hi"]
b=d["course"]
for i in a:
    c=0
    if c<a[i]:
        c=a[i]
print(c)
for j in b:
    l=0
    if l<b[j]:
        l=b[j]
print(l)


# In[69]:


for i in d.values():
    for j in i.values():
        c=0
        if c<j:
            c=j
    print(c)


# In[ ]:


while(i<d)


# In[1]:


d={"dheeraj":{"a":12,"b":23,"c":45},"course":{"d":67,"e":34,"f":1},"g":33,"h":[45,6,7,8,9,3],"i":[43,45,78],"k":"dheeraj"}


# In[22]:


a=0
for i in d.values():
    if type(i)==dict:  
        for j in i.values():
            if a<max(i.values()):
                a=max(i.values())
    elif type (i)==list:
        for k in i:
            if a<k:
                a=k
    elif type (i)==tuple:
        if a<d[i]:
            a=d[i]
    elif type(i)==int:
        if a<i:
            a=i
print ("maximum no. is ",a)    


# In[8]:


d.values()


# In[11]:


for i in d.values():
    for j in i.values():
        print (j)


# In[12]:


n=(1,2,3)
type (n)


# In[23]:


a={"b":"juice","c":"corn"}
a.values()


# In[24]:


a.items()


# In[25]:


a=["ten","twenty","thirty"]
b=[10,20,30]


# In[31]:


c={}
for i in range(3):
    cupdateitems()=a[i]
    c.values()=b[i]
print(c)
    


# In[32]:


m={"d":4,"l":0}
m.update(5)


# In[1]:


t=(1,2,3,(4,5,6))


# In[2]:


c=0
for i in t:
    if type(i)==int:
        if c<i:
            c=i
    elif type(i)==tuple:
        for j in i:
            if c<j:
                c=j
print ("the max value is",c)


# In[14]:


a=input("enter the word")
b=a[::-1]
if b==a:
    print("palindrome")
else:
    print("not palindrome")


# In[32]:


a=input ("enter the word")
k=0
for i in range(len(a)):
    if a[i]!=a[len(a)-i-1]:
        print("not palindrome")
        k=k+1
        break
    else:
        k=0
if k==0:
    print("palindrome")


# In[33]:


len("dheeraj")


# In[38]:


def test():
    pass


# In[39]:


def test1():
    print ("this is my first function")


# In[40]:


test1()


# In[49]:


a=test1()


# In[51]:


type(test1())


# In[52]:


a=test1()


# In[53]:


str(a)


# In[54]:


test1()+"dh"


# In[55]:


def test2():
    return "this is my first function"


# In[56]:


type(test2())


# In[57]:


test2()+"dh"


# In[58]:


def test3():
    return 34


# In[59]:


test3()


# In[60]:


type(test3())


# In[61]:


def test4():
    return 4,3,"dk",[1,2,3]


# In[62]:


test4()


# In[63]:


type (test4())


# In[1]:


def test5():
    return 1,2,3,"dk",[4,5,6]


# In[4]:


b=test5()


# In[5]:


b[1]


# In[6]:


test5()


# In[7]:


a=1
b=5
c="dhee"
d=[6262,32,13,44,89]


# In[8]:


a,b,c,d=34,45,"dhee",998


# In[10]:


x,y,u,v,w=test5()


# In[11]:


x


# In[12]:


y


# In[13]:


u


# In[14]:


v


# In[15]:


w


# In[16]:


def test6():
    a=6*7/6
    return a


# In[17]:


test6()


# In[18]:


l=[3,4,5,6,7,"dhee",[1,2,3,4,5]]
    


# In[31]:


def test7(a):
    n=[]
    if type (a)==list:
        for i in a:
            if type (i)==int:
                n.append(i)
            elif type(i)==list:
                for j in i:
                    if type (j)==int:
                        n.append(j)
    return n


# In[32]:


test7(l)


# In[33]:


a=[34,45,2,2,5566,787,"dheeraj"]


# In[34]:


test7(a)


# In[35]:


def test8(a):
    if type(a)==dict:
        return a.keys()
    else:
        return "you have not passed a dict"
            


# In[36]:


test8("dheeraj")


# In[37]:


test8({"a":23,"b":56,"c":"dheeraj"})


# In[52]:


def test9(a,b):
    if type(a)==list and type (b)==list:
        a.extend(b)
        return a
    else:
        return "it is not a list"
    


# In[53]:


test9([1,2,3,4],[5,6,7,8])


# In[49]:


a=[1,2,3,4]
b=[5,6,7,8]


# In[50]:


test9(a,b)


# In[51]:


a


# In[81]:


def pat(a):
    if type(a)==int:
        for i in range(a):
            for j in range(i+1):
                 print ("*", end=" ")
            print("\n ")


# In[82]:


pat(5)


# In[ ]:




