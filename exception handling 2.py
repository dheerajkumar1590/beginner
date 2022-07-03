#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("fds")


# In[3]:


a=int(input())


# In[4]:


try:
    f=open("test1","r")
    f.write("this is my code with exception handling")
    print("this is the code after write ops")
except:
    print("this is my handler")
l=[1,2,3,4,5]
for i inl:
    print(i)


# In[7]:


f=open("test1","r")
f.write("this is my code with exception handling")
print("this is the code after write ops")
l=[1,2,3,4,5]
for i in l:
    print(i)


# In[1]:


try:
    d={"key1":"dhee","key2":[1,2,3,4],"key3":(4,6,7)}
    d["key4"]=int(input())
except Exception as a:
    print(a)


# In[2]:


d={"key1":"dhee","key2":[1,2,3,4],"key3":(4,6,7)}
d["key4"]=int(input())


# In[4]:


try:
    d={"key1":"dhee","key2":[1,2,3,4],"key3":(4,6,7)}
    d["key4"]=int(input())
except ValueError as a:
    print(a)


# In[7]:


try:
    d={"key1":"dhee","key2":[1,2,3,4],"key3":(4,6,7)}
    d["key4"]=int(input())
    f=open("test4.txt","r")
except ValueError as a:
    print(a)


# In[8]:


try:
    d={"key1":"dhee","key2":[1,2,3,4],"key3":(4,6,7)}
    d["key4"]=int(input())
    f=open("test4.txt","r")
except Exception as a:
    print(a)


# In[11]:


try:
    d={"key1":"dhee","key2":[1,2,3,4],"key3":(4,6,7)}
    d["key4"]=int(input())
    f=open("test4.txt","r")
except Exception as a:
    print(a)
    print("this is my exception ")
except ValueError as b:
    print (b)
except FileNotFoundError as c:
    print(c)


# In[12]:


try:
    d={"key1":"dhee","key2":[1,2,3,4],"key3":(4,6,7)}
    d["key4"]=int(input())
    f=open("test4.txt","r")
except ValueError as b:
    print (b)
except FileNotFoundError as c:
    print(c)
except Exception as a:
    print(a)
    print("this is my exception ")


# In[13]:


try:
    d={"key1":"dhee","key2":[1,2,3,4],"key3":(4,6,7)}
    d["key4"]=int(input())
    f=open("test4.txt","r")
except ValueError as a:
    print(a)


# In[16]:


try:
    f=open("test5.txt","r")
    f.write("this is my code in try")
except Exception as a:
    print("this is to handle as error",a)
else:
    print("this will execute once my try block wll br executed successfully")
    f.close()


# In[21]:


try:
    f=open("test3.txt","w")
except Exception as a:
    print("sfhshj")
else:
    print("do this on successfull excution of try block")
finally:
    print("do this for sure")


# In[23]:


try:
    f=open("test3.txt","w")
except Exception as a:
    print("sfhshj")
else:
    print("do this on successfull excution of try block")
finally:
    print("do this for sure")
    try:
        f=open("test3","w")
    except:
        print("handle this")
    finally:
        print("it will come to this block for sure")


# In[27]:


def func():
    a=int(input())
    return a


# In[28]:


func()


# In[29]:


func()


# In[30]:


def func():
    try:
        a=int(input())
        return a
    except Exception as b:
        print("this is my input error",b)


# In[31]:


func()


# In[15]:


def func():
    flag = True
    while flag:
        try:
            a=int(input("enter an integer"))
            
            if type(a)==int:
                print ("yes you have entered an integer ")
                return a
                flag= False
        except Exception as b:
            print("No,you did not enter an integer,please enter an integer,b")       


# In[16]:


func()


# In[19]:


def inte():
    """this function will check the integer and if integer is not entered it will again ask for integer"""
    while True:
        
        try:
            a=int(input())
            break
        except ValueError as a:
            print ("you didn't entered an integer pls enter again",a)
            
    
        


# In[20]:


inte()


# In[21]:


a=6/10


# In[22]:


5/0


# In[36]:


def test(a):
    if a<0:
        raise ZeroDivisionError("you have entered a negative value",a)
    return a


# In[37]:


test(-4)


# In[27]:


open("fdjfksh","r")


# In[38]:


def test(a):
    if a=="dhee":
        raise ZeroDivisionError("you have entered a negative value",a)
    return a


# In[39]:


test("dhee")


# In[42]:


try:
    """in this i am overwiting a class of ZeroDivision"""
    test("dhee")
except Exception as e:
    print("calling my raised exception",e)


# In[ ]:





# In[ ]:




