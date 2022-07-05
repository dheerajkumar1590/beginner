#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import logging


# In[ ]:


logging.basicConfig(filename="test.log")


# In[ ]:


logging.info("this is my info log")
logging.warning("this is my warning log")
logging.error("this is my error log")


# In[ ]:


pwd()


# In[ ]:


"""DEBUG
INFO
WARNING
CRITTICAL"""


# In[ ]:


f=open("test.log","w")


# In[ ]:


f.close()


# In[ ]:


import logging


# In[ ]:


logging.basicConfig(filename="test.log",level=logging.INFO)


# In[ ]:


logging.info("dheeraj info")
logging.warning("this. is my second log")


# In[ ]:


logging.error("this is my error log")


# In[ ]:


logging.shutdown()


# In[1]:


import logging
logging.basicConfig(filename="test3.log",level=logging.INFO, format='%(asctime)s%(message)s%(levelname)s')


# In[2]:


logging.info("this is my info log")
logging.warning("this is my warning log")
logging.debug("this is my debug log")
logging.error("this is my error log")


# In[3]:


"""priority of logging
ERROR
WARNING
INFO
DEBUG

it will not log below but will log above it"""


# In[3]:


import logging


# In[2]:


logging.basicConfig(filename="test4.log",level=logging.DEBUG,format='%(asctime)s%(levelname)s%(message)s')


# In[3]:


def divbyzero(a,b):
    """this will find the divsion of two no.s"""
    logging.info("this is the start of my code and i am trying to enter %s and %s",a,b)
    try:
        div=a/b
        logging.info("executed successfully")
    except Exception as e:
        logging.error("Error has happened")
        logging.exception("Exception occured "+ str(e))


# In[4]:


divbyzero(5,4)


# In[5]:


divbyzero(5,0)


# In[7]:


logging.shutdown()


# In[4]:


logging.basicConfig(filename="dheeraj.log",level=logging.DEBUG,format='%(asctime)s%(levelname)s%(message)s')


# In[5]:


logging.info("this is my info log")
logging.debug("this is my debug log")
logging.error("this is my error log")


# In[ ]:




