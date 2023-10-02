#!/usr/bin/env python
# coding: utf-8

# In[111]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


#load Data
data = pd.read_excel(r'C:\Users\abdulrahman\Documents\DataBooks\New folder\SaudiPopulationData.xlsx')


# In[3]:


#Explore Data
data.head()


# In[132]:


#Check missing values
data.isnull().sum()


# In[130]:


#Explore Region Column
data.value_counts('Region')


# In[23]:


#Sum of population in each region
Population_Region = data.groupby('Region')['Population estimates'].sum().sort_values()
Population_Region


# In[133]:


Nation=data.groupby('Nationality')['Population estimates'].sum()
Nation


# In[92]:


#Summary Statistics about Population
data['Population estimates'].describe()


# In[114]:


#Population by regions visualized
sns.catplot(x ='Population estimates', y = 'Region', data=data , kind = 'bar' )


# In[ ]:





# In[103]:


#Population by regions visualized & differentiated by nationality
sns.catplot(x = 'Population estimates' , y ='Region' ,hue = 'Nationality' ,data=data , kind = 'bar')


# In[99]:


#Population by regions visualized & differentiated by Gender
sns.catplot(x = 'Population estimates' , y ='Region' ,hue = 'Gender' ,data=data , kind = 'bar')


# In[120]:


#Population size overtime
sns.lineplot(x='Year' , y='Population estimates' , data = data)


# In[123]:


#population size overtime differentiated by Gender
sns.lineplot(x='Year' , y='Population estimates' , data = data , hue = 'Gender')


# In[124]:


#Now differentiated by Nationality
sns.lineplot(x='Year' , y='Population estimates' , data = data , hue = 'Nationality')


# In[128]:


#Differentiated by both variables 
sns.lineplot(x='Year' , y='Population estimates' , data = data , hue = 'Nationality'  , style ='Gender')


# In[148]:


#Basic EDA project is done !


# In[ ]:




