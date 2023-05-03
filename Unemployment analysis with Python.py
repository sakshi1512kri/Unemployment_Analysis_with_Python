#!/usr/bin/env python

# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
from plotly import express as exp


# In[5]:


dataset=pd.read_csv(r"C:\Users\saksh\Downloads\archive\Unemployment_Rate_upto_11_2020.csv",engine="python")


# In[6]:


print(dataset.head())


# In[7]:


print(dataset.isnull().sum())


# In[8]:


dataset.columns= ["State","Date","Frequency",
               "Estimated Unemployment Rate(%)",
               "Estimated Employed",
               "Estimated Labour Participation Rate(%)",
               "Region","Longitude","Latitude"]


# In[9]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))
sb.heatmap(dataset.corr())
plt.show()


# In[12]:


dataset.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Region",
               "longitude","latitude"]
plt.title("Indian Unemployment")
sb.histplot(x="Estimated Employed", hue="Region", data=dataset)
plt.show()


# In[14]:


plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sb.histplot(x="Estimated Unemployment Rate", hue="Region", data=dataset)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




