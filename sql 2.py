#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as conn


# In[3]:


mydb=conn.connect(host='localhost',user='root',passwd='12627@Dheeraj')


# In[4]:


cursor=mydb.cursor()


# In[5]:


cursor.execute("show databases")


# In[7]:


cursor.fetchall()


# In[8]:


cursor.execute("select *from dheeraj.basic")


# In[9]:


cursor.fetchall()


# In[10]:


cursor.execute("select *from dheeraj.glass")


# In[11]:


cursor.fetchall()


# In[10]:


cursor.execute("select col1,col3,col5,col10 from dheeraj.glass")


# In[11]:


cursor.fetchall()


# In[12]:


cursor.execute("select* from dheeraj.glass where col1=4")


# In[13]:


cursor.fetchall()


# In[14]:


cursor.execute("delete from dheeraj.glass where col1=4")


# In[15]:


mydb.commit()


# In[16]:


cursor.execute("UPDATE dheeraj.glass SET col1=5,col2=6 where col1=1")


# In[17]:


mydb.commit()


# In[18]:


cursor.execute("select* from dheeraj.glass")


# In[19]:


cursor.fetchall()


# In[13]:


cursor.execute("select col1, count(col1), col11 from dheeraj.glass group by col1")


# In[37]:


cursor.fetchall()


# In[37]:


cursor.execute("select count(*), col1, col2 from dheeraj.glass group by col1")


# In[41]:


cursor.fetchall()


# In[15]:


cursor.execute("select *from dheeraj.basic")


# In[16]:


cursor.fetchall()


# In[28]:


cursor.execute("select * from dheeraj.basic where classname='fdsd'")


# In[29]:


cursor.fetchall()


# In[32]:


cursor.execute("select count(*),classname from dheeraj.basic where classname='fdsd'")


# In[33]:


cursor.fetchall()


# In[34]:


cursor.execute("select count(*), classname from dheeraj.basic group by classname")


# In[35]:


cursor.fetchall()


# In[42]:


cursor.execute("select count(*),selfid from dheeraj.basic group by selfid")


# In[43]:


cursor.fetchall()


# In[47]:


#deleting a table
cursor.execute("drop table dheeraj.basic")


# In[48]:


mydb.commit()


# In[46]:


cursor.execute("select * from dheeraj.basic")


# In[49]:


cursor.fetchall()


# In[50]:


cursor.execute("select * from dheeraj.glass")


# In[51]:


cursor.fetchall()


# In[52]:


cursor.execute("select col1,col2,col11 from dheeraj.glass where col1=11 or col11=2")


# In[53]:


cursor.fetchall()


# In[54]:


cursor.execute("select col1,col2,col11 from dheeraj.glass where col1=11 and col11=2")


# In[55]:


cursor.fetchall()


# In[63]:


cursor.execute("select * from dheeraj.glass WHERE col2 LIKE '1.515%'")


# In[64]:


cursor.fetchall()


# In[65]:


cursor.execute("select * from dheeraj.glass")


# In[66]:


cursor.fetchall()


# In[67]:


cursor.execute("select * from dheeraj.glass order by col2")


# In[68]:


cursor.fetchall()


# In[71]:


a=cursor.execute("select * from dheeraj.glass where col1>112")


# In[72]:


cursor.fetchall()


# In[77]:


a=cursor.execute("select * from (select * from dheeraj.glass where col1>112)as a where col11=3")


# In[78]:


cursor.fetchall()


# In[ ]:




