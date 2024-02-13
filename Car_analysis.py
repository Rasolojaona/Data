#!/usr/bin/env python
# coding: utf-8

# # Import the dataset cars

# In[25]:


import pandas as pd
car = pd.read_csv('file(2).csv')
car


# The fisrt five rows

# In[2]:


car.head()


# ## Statistiques de nos données

# In[3]:


car.describe()


# In[6]:


car.shape


# ## 1) Data cleaning

# In[8]:


car.isnull().sum()


# In[26]:


car[car['Cylinders'].isnull()]


# ### On peut soit choisir d'effacer tous les données manquantes

# In[15]:


car1 = car.dropna()


# In[16]:


car1.shape


# In[17]:


car1.isnull().sum()


# ### Soit de compléter les données par les valeurs manquantes

# In[27]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)


# In[28]:


car


# In[29]:


car.isnull().sum()


# In[30]:


car = car.dropna()


# In[31]:


car.isnull().sum()


# In[33]:


car[car['EngineSize'] == 1.3]


# ### 2) Question (based on value counts)

# In[34]:


car['Make'].value_counts()


# ### Show the records where the origin is Asia or Europe

# In[35]:


car[(car['Origin'] == 'Asia') | (car['Origin'] == 'Europe')]


# In[36]:


car['Origin'].value_counts()


# In[38]:


car[car['Origin'].isin(['Asia', 'Europe'])]


# ### 4) Remove rows where weigth is above 4000

# In[41]:


car[~(car['Weight'] > 4000)]


# ### 5) Increase all the values of 'MPG_City' column by 3

# In[43]:


car['MPG_City']


# In[49]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)


# In[48]:


car['MPG_City']


# In[ ]:




