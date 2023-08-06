#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


dataframe = pd.read_csv("Zomato data .csv")
dataframe.head(5)


# In[4]:


dataframe.describe()


# In[8]:


dataframe["rate"].dtype


# In[11]:


def handleRate(value):
    value = str(value).split('/')
    value = value[0];
    return float(value)
dataframe['rate'] = dataframe['rate'].apply(handleRate)
dataframe.head()


# In[12]:


dataframe.info()


# In[17]:


dataframe.isnull().sum()


# In[18]:


sns.countplot(x = dataframe["listed_in(type)"])
plt.xlabel("Type of Restuarant")


# In[ ]:


#Conclusion: The majority of the restaurant falls into the Dining category


# In[20]:


grouped_data = dataframe.groupby("listed_in(type)")['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c = "green", marker = "o")
plt.xlabel("Type of Restaurant", c = "red", size = 20)
plt.ylabel("Votes", c= "red", size = 20)


# In[ ]:


#Conclusion: Dining restaurants are preferred by a larger number of individuals.


# In[22]:


max_votes = dataframe["votes"].max()
restaurant_with_max_votes = dataframe.loc[dataframe["votes"] == max_votes, 'name']
print(restaurant_with_max_votes)


# In[23]:


sns.countplot(x=dataframe['online_order'])


# In[ ]:


#Conclusion: This suggests that a majority of the restaurants do not accept online orders.


# In[24]:


plt.hist(dataframe["rate"],bins =5)
plt.title("Disrtibution of ratings")
plt.show()


# In[ ]:


#Conclusion: The majority of restaurants received ratings ranging from 3.5 to 4.


# In[26]:


couple_date = dataframe["approx_cost(for two people)"]
sns.countplot(x= couple_date)


# In[ ]:


#Conclusion: The majority of couples prefer restaurants with an approximate cost of 300 rupees.


# In[27]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)


# In[ ]:


#CONCLUSION: Offline orders received lower ratings in comparison to online orders, which obtained excellent ratings.


# In[28]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()


# In[29]:


#CONCLUSION: Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders.
#This suggests that clients prefer to place orders in person at restaurants, but prefer online ordering at cafes.

