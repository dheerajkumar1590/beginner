#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install mysql-connector-python')


# In[1]:


import mysql.connector as conn


# In[2]:


mydb=conn.connect(host='localhost',user='root',password="12627@Dheeraj")


# In[3]:


mydb


# In[4]:


cursor=mydb.cursor()


# In[5]:


cursor.execute("show databases")


# In[6]:


cursor.fetchall()


# In[13]:


cursor=mydb.cursor()


# In[14]:


#to create a new data base
cursor.execute("create database dheeraj")


# In[15]:


cursor.execute('create table dheeraj.basic(selfid INT(10),firstname VARCHAR(30),lastname VARCHAR(30),regid INT(10),classname VARCHAR(30))')


# In[9]:


cursor.execute('use dheeraj')


# In[10]:


cursor.execute("show tables")


# In[11]:


cursor.fetchall()


# In[12]:


cursor.execute('insert into dheeraj.basic values(12345,"dheeraj","kumar",233435,"basic")')


# In[13]:


mydb.commit()


# In[14]:


cursor.execute('insert into dheeraj.basic values(232323,"dk","kumar",434443,"fdsd")')


# In[15]:


mydb.commit()


# In[16]:


cursor.execute('insert into dheeraj.basic values(77457,"dheeru","kumar",744393,"fdsd")')


# In[17]:


mydb.commit()


# In[18]:


cursor.execute("select *from dheeraj.basic")


# In[19]:


cursor.fetchall()


# In[28]:


cursor.execute("create table dheeraj.glass(col1 INT(10),col2 float(10,5),col3 float(10,5),col4 float(10,5),col5 float(10,5),col6 float(10,5),col7 float(10,5), col8 float(10,5),col9 float(10,5),col10 float(10,5),col11 INT(10))")


# In[25]:


cursor.execute("show tables")


# In[26]:


cursor.fetchall()


# In[29]:


ls


# In[7]:


file=open("glass.data","r")


# In[8]:


file.read()


# In[36]:


import csv
with open("glass.data","r")as f:
    glass_data=csv.reader(f,delimiter='\n')
    print(glass_data)


# In[27]:


import csv
with open("glass.data","r")as f:
    glass_data=csv.reader(f,delimiter='\n')
    for i in glass_data:
        print(i)


# In[10]:


import csv
with open("glass.data","r")as f:
    glass_data=csv.reader(f,delimiter='\n')
    for i in glass_data:
        print(i[0])


# In[ ]:


cursor.execute("create table dheeraj.glass(col1 INT(10),col2 float(10,5),col3 float(10,5),col4 float(10,5),col5 float(10,5),col6 float(10,5),col7 float(10,5), col8 float(10,5),col9 float(10,5),col10 float(10,5),col11 INT(10))")


# In[39]:


cursor.execute('insert into dheeraj.glass values(1,1.52101,13.64,4.49,1.10,71.78,0.06,8.75,0.00,0.00,1)')


# In[40]:


mydb.commit()


# In[41]:


cursor.execute('select * from dheeraj.glass')


# In[42]:


cursor.fetchall()


# In[37]:


with open ('glass.data','r')as f:
    glass_data=csv.reader(f,delimiter='\n')
    for i in glass_data:
        print(i)
        print('insert into glass data file({str(i[0])})')
        cursor.execute('insert into dheeraj.glass values({values})'.format(values=((i[0]))))
    mydb.commit()


# In[38]:


cursor.execute("select* from dheeraj.glass")


# In[39]:


cursor.fetchall()


# In[41]:


import pandas as pd


# In[45]:


pd.read_sql("select* from dheeraj.glass",mydb)


# In[44]:


pd.read_sql("show databases",mydb)


# In[ ]:




