#!/usr/bin/env python
# coding: utf-8

# ## Import police dataset

# In[1]:


import pandas as pd
police = pd.read_csv('file(3).csv')
police


# ## Data cleaning

# In[2]:


police.head()


# In[3]:


police.describe()


# In[4]:


police.isnull().sum()


# ## Removing the column that only contains missing values

# In[6]:


police.drop(columns = 'country_name', inplace=True)


# In[7]:


police


# ## For speeding, were Men or women stopped more often

# In[10]:


police[police['violation'] == 'Speeding'].driver_gender.value_counts()


# ## Does gender affect who gets searched during a stop?

# In[11]:


police.groupby('driver_gender').search_conducted.sum()


# ## Mean stop_duration

# In[12]:


police['stop_duration'] = police['stop_duration'].map({'0-15 Min': 7.5, '16-30 Min': 24, '30+ Min': 45})


# In[13]:


police


# In[14]:


police['stop_duration'].mean()


# In[15]:


police.groupby('violation').driver_age.describe()


# In[ ]:




