#!/usr/bin/env python
# coding: utf-8

# # Winning Wrestlers Entertainment
# 
# In this activity you will be taking four seperate csvs that were scraped down from a wrestling database, merging them together, and then creating charts to visualize a wrestler's wins and losses over the course of four years.
# 
# ### Part 1 - Macho Merging
# 
# * You will likely need to perform three different merges over the course of this activity, changing the names of your columns as you go along.

# In[1]:


#import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

get_ipython().run_line_magic('matplotlib', 'notebook')


# In[3]:


# Take in all of our wrestling data and read it into pandas
path_2013 = "../Resources/WWE-Data-2013.csv"
WWE_2013 = pd.read_csv(path_2013)

path_2014 = "../Resources/WWE-Data-2014.csv"
WWE_2014 = pd.read_csv(path_2014)

path_2015 = "../Resources/WWE-Data-2015.csv"
WWE_2015 = pd.read_csv(path_2015)

path_2016 = "../Resources/WWE-Data-2016.csv"
WWE_2016 = pd.read_csv(path_2016)
WWE_2016.head()


# In[4]:


# Merge
WWE_data = pd.merge(WWE_2013, WWE_2014, on='Wrestler', how='outer')
WWE_data.head()


# In[5]:


#rename columns
WWE_data = WWE_data.rename(columns={"Wins_x":"2013 Wins", "Losses_x":"2013 Losses", "Draws_x":"2013 Draws", "Wins_y":"2014 Wins","Losses_y":"2014 Losses","Draws_y":"2014 Draws"})
WWE_data.head()


# In[6]:


#merge again with 2015
WWE_data = pd.merge(WWE_data, WWE_2015, how="outer", on="Wrestler")
WWE_data.head()


# In[7]:


WWE_data = WWE_data.rename(columns={"Wins":"2015 Wins","Losses":"2015 Losses","Draws":"2015 Draws"})
WWE_data.head()


# In[8]:


WWE_data = pd.merge(WWE_data, WWE_2016, how="outer", on="Wrestler")
WWE_data.head()


# In[9]:


WWE_data = WWE_data.rename(columns={"Wins":"2016 Wins","Losses":"2016 Losses","Draws":"2016 Draws"})
WWE_data.head()


# ### Part 2 - Time to Calculate!
# 
# * When your tables have been merged together into one data frame, calculate the total number of wins, losses, and draws a wrestler has had over the course of their career. Also create a new column that will hold the total matches a wrestler has been in over the course of their career.
# 
#     * You will need to convert all NaN values to a number so that you can perform these calculations
# 
# * We are only interested in those wrestlers who have been with the WWE from 2013 to 2016. You will need to come up with some way of filtering out rows that do not meet these conditions.
#     
#     * Also set the 'Wrestler' column as your key for easier referencing later on.

# In[10]:


#NA to 0
WWE_data = WWE_data.fillna(0)

#Summary stats
WWE_data["Total Wins"] = WWE_data["2013 Wins"] + WWE_data["2014 Wins"] + WWE_data["2015 Wins"] + WWE_data["2016 Wins"]
WWE_data["Total Losses"] = WWE_data["2013 Losses"] + WWE_data["2014 Losses"] + WWE_data["2015 Losses"] + WWE_data["2016 Losses"]
WWE_data["Total Draws"] = WWE_data["2013 Draws"] + WWE_data["2014 Draws"] + WWE_data["2015 Draws"] + WWE_data["2016 Draws"]
WWE_data["Total Matches"] = WWE_data["Total Wins"] + WWE_data["Total Losses"] + WWE_data["Total Draws"]

WWE_data.head()


# In[11]:


WWE_vets = WWE_data.loc[(WWE_data["Total Matches"] >= 100) & (WWE_data["2013 Wins"] > 0) & (WWE_data["2016 Wins"] > 0)]

WWE_vets = WWE_vets.set_index("Wrestler")

WWE_vets.head()


# ### Part 3 - Charting Careers
# 
# * Store an individual wrestler's wins over time in a variable
# * Store that same wrestler's losses over time in a variable as well
# * Create a line chart that will plot this wrestler's wins and losses from 2013 to 2016

# In[14]:


wrestler = input("What wrestler are you interested in?")


# In[15]:


# Create a series that looks for a wrestler by name and then traces their wins from 2013 to 2016
wins = WWE_vets.loc[wrestler,["2013 Wins","2014 Wins", "2015 Wins", "2016 Wins"]]

# Create a series that looks for a wrestler by name and then traces their losses from 2013 to 2016
losses = WWE_vets.loc[wrestler,["2013 Losses","2014 Losses","2015 Losses", "2016 Losses"]]


# In[17]:


x = [2013,2014,2015,2016]

plt.plot(x, wins, color="green", label="W's")
plt.plot(x, losses, color="red", label="L's")

plt.legend(loc="best")

plt.xlabel("Years")
plt.ylabel("Number of Matches")

plt.show()


# In[ ]:




