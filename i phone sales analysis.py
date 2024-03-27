#!/usr/bin/env python
# coding: utf-8

# # i phone sales analysys

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as pg


# In[2]:


data=pd.read_csv("apple_products.csv")


# In[3]:


data


# In[4]:


print(data.isnull().sum())


# In[5]:


print(data.describe())


# # i phone sales analysys in india

# In[6]:


top_rated=data.sort_values(by=["Star Rating"],ascending=False)
top_rated=top_rated.head(10)
print(top_rated['Product Name'])


# # Rating count of the top rated iphone on flipkart 

# In[9]:


iphones=top_rated['Product Name'].value_counts()
labels=iphones.index
counts=top_rated['Number Of Ratings']
figure=px.bar(top_rated,x=labels,y=counts,title="Rating count of top rated i phone")
figure.show()


# In[29]:


iphones=top_rated['Product Name'].value_counts()
labels=iphones.index
counts=top_rated['Number Of Reviews']
figure=px.bar(top_rated,x=labels,y=counts,title="Rating count of top reviewed i phone")
figure.show()


# In[18]:


figure=px.scatter(data_frame=data,x="Number Of Ratings",y="Sale Price",trendline="ols",size="Discount Percentage",title="relationship between sales price with number of ratings with respect to discount percentage")
figure.show()


# In[21]:


figure=px.scatter(data_frame=data,x="Star Rating",y="Sale Price",trendline="ols",size="Discount Percentage",title="relationship between sales price with number of star-ratings with respect to discount percentage")
figure.show()


# In[27]:


figure=px.scatter(data_frame=data,x="Number Of Ratings",
                 y="Discount Percentage",size="Sale Price",trendline="ols",title="Relationship between discount percentage andnumber of rating")
figure.show()

# 
Steps followed - 
1.Objective - Iphone sales analysys
2.Data cleaning- used numpy and pandas library
3.Data analysys- used numpy and pandas library
4.Data visualize- used plotly library

Findings-

1.APPLE iPhone 8 Plus (Gold, 64 GB) was the most appreciated iPhone in India
2.iPhones with lower sale prices are sold more in India
3.iPhones with high discounts are sold more in India
# In[ ]:




