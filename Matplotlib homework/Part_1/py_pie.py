#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[4]:


pies = ["Apple", "Pumpkin", "Chocolate Creme", "Cherry", "Apple Crumb",
        "Pecan", "Lemon Meringue", "Blueberry", "Key Lime", "Peach"]
pie_votes = [47, 37, 32, 27, 25, 24, 24, 21, 18, 16]
colors = ["yellow", "green", "lightblue", "orange", "red",
          "purple", "pink", "yellowgreen", "lightskyblue", "lightcoral"]
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)


# In[8]:


# Tell matplotlib to create a pie chart based upon the above data
plt.pie(pie_votes, explode=explode, labels=pies, colors=colors,
        autopct="%1.2f%%", startangle=0)
# Create axes that are equal 
plt.axis("equal")
# Save an image of our chart and print the final product to the screen
plt.savefig('pies_pie.png')

plt.show


# In[ ]:




