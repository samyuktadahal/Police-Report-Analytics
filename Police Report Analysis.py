#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


print(plt.style.available)


# In[9]:


plt.style.use('ggplot')


# In[10]:


df= pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Python Data Analysis\Police Report Analysis\3. Police Data.csv")
df


# In[11]:


df.shape


# In[12]:


df.head()


# In[13]:


df.info()


# In[14]:


df.dtypes


# In[15]:


df.isnull().sum()


# In[16]:


#Removing Useless Column
df= df.drop(columns='country_name')
df= df.drop(columns= 'search_type')
df


# In[17]:


vs = df[df['violation']=='Speeding'].driver_gender.value_counts()
vs


# In[18]:


ax= vs.plot(kind= 'bar', ylabel= 'count', figsize=(10,6))
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width()/ 2., p.get_height()),
                ha= 'center', va= 'center', xytext=(0,5), textcoords= 'offset points')


# In[19]:


df[df['violation']== 'Speeding'].driver_race.value_counts()


# In[20]:


driver_race= ['White', 'Black', 'Hispanic', 'Asian', 'Other']
counts= [30186, 3658, 2062, 1173, 125]
COLORS =['blue', 'orange', 'yellow', 'silver', 'black']

plt.figure(figsize=(10,5))
plt.bar(driver_race, counts, color= COLORS)
plt.xlabel('Driver Race')
plt.title('Counts of Speeding Violations by Driver Race')


# In[21]:


df.groupby('driver_gender').search_conducted.value_counts()


# In[22]:


#Data Preparation (AA DataFrame)
data= {'driver_gender': ['F', 'F', 'M', 'M'],
      'search_conducted': [False, True, False, True],
      'counts':[15944, 366, 43051, 2113]}
AA= pd.DataFrame(data)

#Plotting [pivot_table = Reshapes the data]
AA.pivot_table(
               index='driver_gender', 
               columns= 'search_conducted', 
               values= 'counts', 
               aggfunc= 'sum'
               ).plot(kind='bar', stacked= True)  #Creates a stacked bar chart

#Labeling
plt.xlabel('Driver Gender')
plt.ylabel('Counts')
plt.title('Search Conducted By Driver Gender')
plt.legend(title= 'Search Conducted')  #Legend : shows True/ False
plt.xticks(rotation=0)  #Keeps gender label horizontal


# In[23]:


df.search_conducted.value_counts()


# In[24]:


df.head()


# In[25]:


df['stop_duration'].dtypes


# In[26]:


df['stop_duration'].value_counts()


# In[27]:


df['stop_duration']= df['stop_duration'].map({'0-15 Min':7.5, '16-30 Min':23,'30+ Min':30})


# In[28]:


df


# In[29]:


df['stop_duration'].mean()


# In[30]:


stop_duration_stats = df.groupby('stop_duration').agg({'driver_age':['mean', 'max', 'min', 'count']})
stop_duration_stats


# In[31]:


stop_outcome_distribution = df.groupby('stop_outcome').size().reset_index(name='Count')
stop_outcome_distribution


# In[34]:


sns.barplot(x='stop_outcome', y='Count', data=stop_outcome_distribution)

plt.xlabel('Stop Outcome')
plt.ylabel('Count')
plt.title('Distribution of Stop Outcomes')


# In[35]:


g= df.groupby('driver_age')


# In[36]:


g.violation.value_counts()


# In[37]:


df.groupby('violation').driver_age.describe()


# In[38]:


df['violation'].unique()


# In[39]:


df


# In[40]:


df1= df.groupby(['driver_gender', 'driver_race']).agg({'driver_age':['mean', 'median', 'count']})
df1


# In[42]:


#Search Conducted Analysis:

search_conducted_proportion = df['search_conducted'].value_counts(normalize= True)*100
search_conducted_proportion


# In[44]:


search_conducted_proportion.plot.pie(figsize=(10,6), autopct='%1.1f%%', startangle= 140)
# "autopct='%1.1f%%" - Displays percentage values on each slice with 1 decimal place
# "startangle= 140" - Rotates the pie chart to start at 140 degrees (default is 0)
#Adding Title
plt.title('Search Conducted Propotion')


# In[45]:


#drugs_related Stop Analysis
drugs_related_stop_frequency = df['drugs_related_stop'].value_counts()
drugs_related_stop_frequency


# In[46]:


drs= df.groupby(['driver_gender', 'drugs_related_stop']).agg({'drugs_related_stop':['count']})
drs


# In[48]:


df['is_arrested'].value_counts()


# In[49]:


drs= df.groupby(['driver_gender', 'is_arrested']).agg({'is_arrested':['count']})
drs


# In[ ]:




