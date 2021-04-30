#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df = pd.read_csv('911 calls.csv')


# In[7]:


df.info()


# In[8]:


df.head()


# In[9]:


df['zip'].value_counts().head()


# In[10]:


df['twp'].value_counts().head()


# In[11]:


#df['title'].unique()
df['title'].nunique()


# In[12]:


df.head()


# In[13]:


s = "EMS: BACK PAINS/INJURY"
new_s = s.split(':')[0].replace('', '')
print(new_s)


# In[14]:


df.apply(lambda x: x.title.split(':')[0].replace('',''), axis=1) #x.title specifies the column of the data frame


# In[15]:


df['Reason'] = df.apply(lambda x: x.title.split(':')[0].replace('',''), axis=1) #specifc axis=1 to run over the rows
df.head(10)


# In[16]:


df['Reason'].value_counts()


# In[17]:


sns.set_style('whitegrid')


# In[18]:


sns.countplot(x='Reason', data=df)


# In[19]:


type(df['timeStamp'][0])


# In[20]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[21]:


time = df['timeStamp'].iloc[0]
print(time.day)
print(time.year)
print(time.date())

print(time.hour)
print(time.month_name())
print(time.day_name())


# In[22]:



time = df['timeStamp'].iloc[0]
print(time.hour)
print(time.month_name())
print(time.day_name())


# In[23]:


df['Hour'] = df.apply(lambda x: x['timeStamp'].hour, axis=1) #using DateTime objects
df['Month'] = df.apply(lambda x: x['timeStamp'].month_name(), axis=1) 
df['Day of Week'] = df.apply(lambda x: x['timeStamp'].day_name(), axis=1) 

#df.head(10)


# In[24]:


sns.countplot(x='Day of Week', data=df, hue='Reason')


# In[ ]:





# In[25]:


df['Month No'] = df.apply(lambda x: x['timeStamp'].month, axis=1)


# In[26]:


sns.countplot(x='Month No', data=df, hue='Reason')


# In[27]:


byMonth = df.groupby(['Month No'])[['lat','lng','desc','zip','title','timeStamp','twp','addr','e','Reason','Hour','Day of Week']].count()
#byMont = df.groupby('Month No')


# In[28]:


byMonth.head()


# In[29]:


byMonth['twp'].plot()


# In[30]:


byMonth = byMonth.reset_index()


# In[31]:


sns.lmplot(x='Month No', y='twp', data=byMonth)


# In[32]:


df['Date'] = df['timeStamp'].apply(lambda t: t.date()) 
df.head()


# In[33]:



byDate = df.groupby('Date').count()
byDate.head()


# In[34]:


byDate['twp'].plot(figsize=(7,5))
plt.tight_layout()


# In[35]:


byDate.head()


# In[37]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot(figsize=(7,5))
#byDate['twp'].plot(figsize=(7,5))
plt.title('Traffic')
plt.tight_layout()


# In[38]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot(figsize=(7,5))
plt.title('Fire')
plt.tight_layout()


# In[39]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot(figsize=(7,5))
plt.title('EMS')
plt.tight_layout()


# In[40]:


dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()
dayHour


# In[41]:


plt.figure(figsize=(12,6))
sns.heatmap(dayHour, cmap="viridis")


# In[42]:


plt.figure(figsize=(12,6))
sns.clustermap(dayHour, cmap="viridis")


# In[43]:


dayMonth = df.groupby(by=['Day of Week','Month No']).count()['Reason'].unstack()
dayMonth


# In[44]:


plt.figure(figsize=(12,7))
sns.heatmap(dayMonth, cmap='viridis')


# In[45]:


plt.figure(figsize=(12,7))
sns.clustermap(dayMonth, cmap="viridis")


# In[ ]:




