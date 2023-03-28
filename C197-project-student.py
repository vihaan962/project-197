#!/usr/bin/env python
# coding: utf-8

# In[8]:


print('Name: ')
print('Plot a heatmap which help you visualize percentage of blood leaving the heart at each contraction of a smoking and non smoking person heart')
print('Plot a heatmap which help you visualize Percentage of blood leaving the heart at each contraction of person who died due to cardio vascular disease')


# #  Task 1 - Plot heat map to visualize percentage of blood leaving the heart at each contraction of a smoking and non smoking person

# A normal, healthy heart will never completely empty, but it will pump out 55-70 percent of the blood that’s inside it. An ejection fraction of 55-70 percent is normal; 40-55 percent is below normal. Anything less than 40 percent may indicate heart failure, and below 35 percent there’s a risk for life-threating arrhythmias

# In[1]:


#predefine code for image
from IPython.display import Image
Image(filename='heart.png') 
#predefine code end


# The right side of your heart receives oxygen-poor blood from your veins and pumps it to your lungs, where it picks up oxygen and gets rid of carbon dioxide. The left side of your heart receives oxygen-rich blood from your lungs and pumps it through your arteries to the rest of your body.

# In[3]:


# Import all the libraries and read heart_failure_clinical_records_dataset.csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataframe = pd.read_csv('heart_failure_clinical_records_dataset.csv')
dataframe


# In[4]:


#Group by age and smokers and find the average ejection_fraction rate
smoking_heart_dataframe = dataframe.groupby(['age','smoking'])['ejection_fraction'].mean().reset_index()
smoking_heart_dataframe


# In[6]:


# Plot a heatmap to show the ejection fraction rate in smokers and non smokers heart
plt.figure(figsize = (10,8))
heatmap_df = pd.pivot_table(values = 'ejection_fraction',index = 'smoking',columns = 'age',data = smoking_heart_dataframe)
sns.heatmap(heatmap_df,cmap = 'plasma')


# 0 are non smokers  and 1 are smokers
# 
# Conclusion - =

# #  Task 2 Plot a heatmap to visualize percentage of blood leaving the heart at each contraction of people who died due to cardio vascular disease

# In[8]:


#Group by death events and ejection fraction rate and find the average ejection fraction rate
death_dataframe = dataframe.groupby(['age','DEATH_EVENT'])['ejection_fraction'].mean().reset_index()
death_dataframe



# In[9]:


# Plot a heatmap to show the ejection fraction rate of people who died due to cardiovascular disease



plt.figure(figsize = (10,8))
heatmap_df = pd.pivot_table(values = 'ejection_fraction',index = 'DEATH_EVENT',columns = 'age',data = death_dataframe)
sns.heatmap(heatmap_df,cmap = 'plasma')


# 1 are people died due to cardiovascular disease
# 
# Conclusion - 

# In[ ]:




