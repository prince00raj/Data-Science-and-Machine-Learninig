#!/usr/bin/env python
# coding: utf-8

# # Introduction to numpy

# In[13]:


import numpy as np


# In[14]:


data= np.random.randn(2,3)


# In[15]:


data


# ## Shape of the data

# In[16]:


data.shape


# In[17]:


data.dtype


# In[18]:


##Pythonic list 


# In[19]:


data1 = [6,7.5,7,8,9,1]


# In[20]:


print(type(data1))


# In[21]:


arr1=np.array(data1)


# In[22]:


type(arr1)


# In[23]:


data2=[[1,2,3,4],[5,6,7,8]]


# In[24]:


arr2=np.array(data2)


# In[25]:


print(arr2)


# In[26]:


arr2.ndim


# In[27]:


arr2.shape


# In[28]:


np.eye(3)


# ## Arrange = a + range

# it is similar to python's built in range method <br>
# for (int i = start, i < stop, i = i + step)
# 
# np.arrange(start,stop,step)

# In[29]:


np.arange(3,10,1).ndim


# #### The default value of start is 0,  and step =1, it wouldn't include the last index element

# In[30]:


for i in range(4,5,1):
    print(i)


# In[31]:


np.arange(3,-10,-3)


# In[32]:


arr1=np.array([1,2,3,4,5],dtype=np.float64)


# In[33]:


print(arr1)


# In[34]:


arr1.dtype


# ## Typecasting numpy array

# In[35]:


arrr=np.array([1,2,3,4,5])


# In[36]:


print(arrr)


# In[37]:


arrr.dtype


# In[38]:


arrr.astype(np.float64)


# In[39]:


data2=np.array([[1,2,3,4],[5,6,7,8]])


# In[40]:


print(data2)


# In[41]:


data2+data2


# In[42]:


data2*data2


# In[43]:


dp=np.arange(10)


# In[44]:


dp[3]


# In[45]:


dp[5:8]


# In[46]:


dp[5:8]=12


# In[47]:


dp


# ## Two dimensional Array

# In[48]:


arr2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[49]:


print(arr2d)


# In[50]:


print(arr2d[2])


# In[51]:


print(arr2d[0][2])


# In[52]:


print(arr2d[0,2]) #either way is fine 


# ## Pandas

# In[53]:


import pandas as pd


# In[ ]:


###it can handle hetrogeneous data


# In[56]:


obj=pd.Series([4,7,-5,3])


# In[57]:


obj


# In[58]:


obj.values


# In[59]:


obj.index


# In[60]:


obj2 = pd.Series([4,7,-5,3]), index=['a','b','c','d']


# In[ ]:




