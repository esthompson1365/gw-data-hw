#!/usr/bin/env python
# coding: utf-8

# # Search For The Worst
# 
# #### The objective of this assignment is for you to explain what is happening in each cell in clear, understandable language. 
# 
# #### _There is no need to code._ The code is there for you, and it already runs. Your task is only to explain what each line in each cell does.
# 
# #### The placeholder cells should describe what happens in the cell below it.

# **Example**: The cell below imports `pandas` as a dependency because `pandas` functions will be used throughout the program, such as the Pandas `DataFrame` as well as the `read_csv` function.

# In[1]:


import pandas as pd
import numpy as np


# **Example**: The cell below creates a reference to teh csv file and stores it in a variable called `csv_path`. It then creates a DataFrame using the `pd.read_csv` function. The output of the `read_csv` function is a DataFrame.

# In[2]:


# Create reference to CSV file
csv_path = "Resources/Soccer2018Data.csv"

# Import the CSV into a pandas DataFrame
soccer_2018_df = pd.read_csv(csv_path, low_memory=False)
soccer_2018_df


# The code below returns a deduplicated array of soccer positions

# In[3]:


soccer_2018_df["Preferred Position"].unique()


# Now that we know that strikers are marked with the letters 'ST', we create a new dataframe with rows that have the value 'ST' in the `Preferred Position` column. A colon after the comma indicates that we want all columns.

# In[ ]:


strikers_2018_df = soccer_2018_df.loc[soccer_2018_df["Preferred Position"] == "ST", :]
strikers_2018_df.head()


# Below, we sort the `ST` column. The deafult is ascending. We rest the index so that the worst striker is index 0.

# In[ ]:


# Sort the DataFrame by the values in the "ST" column to find the worst
strikers_2018_df = strikers_2018_df.sort_values("ST")

# Reset the index so that the index is now based on the sorting locations
strikers_2018_df = strikers_2018_df.reset_index(drop=True)

strikers_2018_df.head()


# This last line of code takes all the columns from the worst player (index 0).

# In[ ]:


worst_striker = strikers_2018_df.loc[0, :]
worst_striker

