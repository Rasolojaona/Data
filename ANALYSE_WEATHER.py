#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('file.csv')


# In[3]:


# the first five rows
df.head()


# In[4]:


# information about our dataframe
df.info()


# In[5]:


# the dimension of our data
df.shape


# In[6]:


df.index


# In[7]:


df.dtypes


# In[8]:


df.columns


# In[9]:


# it can be applied in a single column
df['Temp_C'].unique()


# In[10]:


# show the count of unique in the dataframe
df.nunique()


# In[11]:


# it show the total non-null in each column
df.count()


# In[12]:


# it show the unique value with their count
df['Weather'].value_counts()


# In[13]:


# nunique() manisa ny valeur unique eo @ colonne iray
# df['Wind Speed_km/h'].nunique()
# unique() manome tableau ny unique value rehetra
# df['Wind Speed_km/h'].unique()


# df.count()

# In[14]:


# question 2: find the number of times when the weather is exactly Clear
df.columns


# In[15]:


df['Weather'].value_counts()


# In[16]:


df[df['Weather'] == "Clear"].value_counts()


# In[17]:


# selon Tommy
df[df['Weather'] == 'Clear'].value_counts().sum()


# In[18]:


# correction selon video
df.Weather.value_counts()


# In[19]:


# selon video, filtering
df[df.Weather == 'Clear']


# In[20]:


# use groupby method
# function get_group is used to take particular data from the column
df.groupby('Weather').get_group('Clear')


# df.count()

# In[21]:


# question 3: find the number of times when the Wind Speed was exactly 4 km/h
# first: let's see the different name of our column
df.columns


# In[22]:


df['Wind Speed_km/h'].value_counts()


# In[23]:


# solution selon Tommy
df[df['Wind Speed_km/h'] == 4].value_counts().sum()


# In[24]:


# selon Tommy en utilisant groupby
df.groupby('Wind Speed_km/h').get_group(4).value_counts().sum()


# In[25]:


df.columns


# In[26]:


df['Visibility_km'].value_counts()


# In[27]:


# question 4: find out all the null values in the data
df.isna().sum()


# In[28]:


# question 5: Rename column weather of the dataframe to Weather Condition
# we use the dictionnary to rename the column, selon Tommy
df = df.rename(columns={'Weather': 'Weather Condition'})


# In[29]:


df


# In[30]:


# selon video
df.rename(columns={'Weather': 'Weather Condition'}, inplace=True)


# In[31]:


# question 6 : what is the mean 'visibility'
df['Visibility_km'].mean()


# In[32]:


# question 7: what is the standard Deviation of 'Pressure in this data'
df['Press_kPa'].std()


# In[33]:


# question 8: variance of Relative Humidity in this data
df['Rel Hum_%'].var()


# In[38]:


# question 9: find all instances when snow was recorded 28:11
df[df['Weather Condition'] == 'Snow'].value_counts().sum()


# In[39]:


# 2 eme methode
df.groupby('Weather Condition').get_group('Snow')


# In[41]:


# selon la video en utilisant str.contains
df[df['Weather Condition'].str.contains('Snow')].head(30)


# In[42]:


# question 10: find all instances when 'Wind Speed is above 24' and 'Visibility is 25'
df.info()


# In[52]:





# In[57]:


# question 10 selon video, atao ao anaty entre parenthese ilay condition rehefa be condition be
df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)]


# In[54]:


# question 11 selon Tommy
df.groupby('Weather Condition').mean()


# In[58]:


# question 12 selon Tommy
df.groupby('Weather Condition').min()


# In[59]:


# selon Tommy
df.groupby('Weather Condition').max()


# In[61]:


# question 13: show all records where Weather Condition is Fog
df[df['Weather Condition'] == 'Fog']


# In[62]:


# 2 eme methode:
df.groupby('Weather Condition').get_group('Fog')


# In[66]:


# question 14: find all instances when the 'Weather is clear' or 'visibility is above 40'
df[(df['Weather Condition'] == "Clear") | (df['Visibility_km'] > 40)]


# In[67]:


# question 15: Weather Condition is Clear and relative humidity is greater than 50 or visibility is above 40
df1 = (df['Weather Condition'] == "Clear") & (df['Rel Hum_%'] > 50)


# In[70]:


df[(df1) | (df['Visibility_km'] > 40) ]


# In[ ]:




