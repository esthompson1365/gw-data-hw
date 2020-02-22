#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[6]:


temp = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
sales = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]


# In[8]:


# Tell matplotlib to create a scatter plot based upon the above data
plt.scatter(temp, sales, marker="o", facecolors="red", edgecolors="black", alpha=0.75)


# In[9]:


# Set the upper and lower limits of our y axis
plt.ylim(175, 625)


# In[10]:


# Set the upper and lower limits of our x axis
plt.xlim(11, 26)


# In[11]:


# Create a title, x label, and y label for our chart
plt.title("Ice Cream Sales and Temperature")
plt.ylabel("Ice Cream Sales")
plt.xlabel("Temperature")


# In[12]:


# Save an image of the chart and print to screen
plt.savefig('ice_cream_sales.png')

plt.show
# NOTE: If your plot shrinks after saving an image,
# update matplotlib to 2.2 or higher,
# or simply run the above cells again.

