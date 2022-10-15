#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


db=sqlite3.connect("dheeraj.db")


# In[3]:


ls


# In[4]:


c=db.cursor()


# In[5]:


c.execute('create table hero(name text, batch int,marks real)')


# In[9]:


c.execute("insert into hero values('dheeraj',322,458.4)")


# In[11]:


c.execute("insert into hero values('dheeraj',322,458.4)")

c.execute("insert into hero values('dheeraj',322,458.4)")
c.execute("insert into hero values('dheeraj',322,458.4)")
c.execute("insert into hero values('dheeraj',322,458.4)")
c.execute("insert into hero values('dheeraj',322,458.4)")
c.execute("insert into hero values('dheeraj',322,458.4)")


# In[13]:


data=c.execute("select * from hero")


# In[14]:


for i in data:
    print(i)


# In[15]:


db.commit()


# In[16]:


db.close()


# In[19]:


db=sqlite3.connect("dheeraj.db")


# In[20]:


c=db.cursor()


# In[22]:


data=c.execute("select * from hero where marks>400")


# In[23]:


for i in data:
    print(i)


# In[24]:


data=c.execute("select * from hero where name='dheeraj'")


# In[25]:


for i in data:
    print(i)


# In[29]:


data=c.execute("select name,marks from hero")


# In[30]:


for i in data:
    print(i)


# In[33]:


d=c.execute("select name,marks from hero order by marks")


# In[34]:


for i in d:
    print(i)


# In[35]:


db.close()


# In[37]:


db=sqlite3.connect("person.db")


# In[38]:


c=db.cursor()


# In[39]:


c.execute("create table persontable(name text,mail text, age int, salary real)")


# In[40]:


ls


# In[46]:


c.execute("insert into persontable values('dheeraj','dh@gmail.com',32,3223)")
c.execute("insert into persontable values('kumar','abc@gmail.com',43,34)")
c.execute("insert into persontable values('hero','axc',323,434)")


# In[48]:


d=c.execute("select * from persontable")


# In[49]:


for i in d:
    print(i)


# In[51]:


db.commit()


# In[52]:


db.close()


# In[54]:


db=sqlite3.connect("dheeraj.db")


# In[55]:


c=db.cursor()


# In[56]:


c.execute("drop table hero")


# In[57]:


c.execute("select * from hero")


# In[58]:


db.close()


# In[64]:


db=sqlite3.connect("person.db")


# In[65]:


c=db.cursor()


# In[66]:


d=c.execute("select * from persontable limit 2")


# In[67]:


for i in d:
    print(i)


# # join opertion

# In[4]:


db=sqlite3.connect("join.db")


# In[5]:


c=db.cursor()


# In[6]:


c.execute("create table student(student_id int,student_name text, student_mailid text, marks int)")


# In[9]:


c.execute("create table address(student_id int, pincode int, location text, reference text, phone_no int)")


# In[8]:


c.execute("drop table address")


# In[12]:


c.execute("insert into student values(22,'dheeraj', 'dheeraj@123',3232)")
c.execute("insert into student values(23,'dheeraj', 'dheeraj@123',3232)")
c.execute("insert into student values(24,'dheeraj', 'dheeraj@123',3232)")
c.execute("insert into student values(25,'dheeraj', 'dheeraj@123',3232)")
c.execute("insert into student values(26,'dheeraj', 'dheeraj@123',3232)")


# In[16]:


c.execute("insert into address values(22,3434,'nehru place','lotus temple',423243)")
c.execute("insert into address values(23,3434,'nehru place','lotus temple',423243)")
c.execute("insert into address values(24,3434,'nehru place','lotus temple',423243)")
c.execute("insert into address values(25,3434,'nehru place','lotus temple',423243)")
c.execute("insert into address values(26,3434,'nehru place','lotus temple',423243)")
c.execute("insert into address values(27,3434,'nehru place','lotus temple',423243)")
c.execute("insert into address values(28,3434,'nehru place','lotus temple',423243)")


# In[23]:


d=c.execute("select * from address")


# In[18]:


for i in d:
    print(i)


# In[19]:


e=c.execute("select * from student")


# In[20]:


for i in e:
    print(i)


# In[24]:


for i in d:
    print(i)


# In[25]:


data=c.execute("select * from student s left join address a on s.student_id=a.student_id")


# In[26]:


for i in data:
    print(i)


# In[28]:


data=c.execute("select * from address s left join student a on s.student_id=a.student_id")


# In[29]:


for i in data:
    print(i)


# In[30]:


for i in c.execute("select * from student"):
    print(i)


# In[35]:


e=c.execute("delete from student where student_id>25")


# In[38]:


for i in c.execute("select * from student"):
    print(i)


# In[39]:


data=c.execute("select * from student")


# In[40]:


data.fetchall()


# In[41]:


data=c.execute("update student set student_id =1000 where student_id =24")


# In[42]:


data=c.execute("select * from student ")


# In[43]:


data.fetchall()


# In[44]:


l=[1,2,3,4,5,6]


# In[45]:


l1=[]
for i in l:
    l1.append(i+5)


# In[46]:


l1


# In[49]:


def test(a):
    return a+5


# In[48]:


[i+5 for i in l]


# In[51]:


list(map(test,l))


# In[52]:


def test1(a):
    return a*332+222


# In[53]:


list(map(test1,l))


# In[54]:


l1=['22','454','4332','7886']


# In[55]:


def test2(a):
    return int(a)


# In[56]:


list(map(test2,l1))


# In[57]:


list(map(lambda x:int(x),l1))


# In[59]:


list(map(lambda x:x+5,l))


# In[60]:


l=[34,556,33,67,44,90]


# In[74]:


[i for i in l if i %2==0]


# In[71]:


def test4(a):
    if a%2==0:
        return a


# In[72]:


list(map(test4,l))


# In[73]:


list(filter(test4,l))


# In[75]:


list(filter(lambda x:x%2==0,l))


# In[3]:


from functools import reduce


# In[4]:


l=[1,2,3,4,5]


# In[5]:


sum(l)


# In[10]:


def test5(a,b):
    return a+b


# In[11]:


reduce(test5,l)


# In[14]:


def test6(a,b,c):
    return a*b


# In[15]:


reduce(test6,l)


# In[20]:


l1=[3]


# In[21]:


reduce(test5,l1)


# In[22]:


reduce(lambda x,y:x+y,l)


# In[23]:


l=[1,2,3,4]
l1=[5,6,7,8]
l2=['dheeraj','kumar',9,10]


# In[25]:


list(zip(l,l1,l2))


# In[ ]:




