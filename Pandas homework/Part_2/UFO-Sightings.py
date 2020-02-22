#!/usr/bin/env python
# coding: utf-8

# # UFO Sightings
# 
# #### The objective of this assignment is for you to explain what is happening in each cell in clear, understandable language. 
# 
# #### _There is no need to code._ The code is there for you, and it already runs. Your task is only to explain what each line in each cell does.
# 
# #### The placeholder cells should describe what happens in the cell below it.

# **Example**: The cell below imports `pandas` as a dependency because `pandas` functions will be used throughout the program, such as the Pandas `DataFrame` as well as the `read_csv` function.

# In[1]:


import pandas as pd


# First, we specify the the path to our csv file and store the path in `csv_path`. Then we load the csv file to a dataframe called `ufo_df` and display the first 5 rows.

# In[2]:


csv_path = "Resources/ufoSightings.csv"

ufo_df = pd.read_csv(csv_path)

ufo_df.head()


# `ufo_df.count()` returns the number of values in each column, absent of NaNs.

# In[3]:


ufo_df.count()


# In the cell below, we drop all rows containing an 'Nan' value in any column. We use "any" rather than "all" so that if a column contains all NaNs, it will not be removed from the dataframe.

# In[4]:


clean_ufo_df = ufo_df.dropna(how="any")
clean_ufo_df.count()


# The `columns` list below holds strings which are column headers in `ufo_df`. This list is referenced in the loc function below to denote what columns we want to pull from the ufo dataframe. The syntax of the loc function before the comma indiates which rows we want. In this case we are telling the computer to pull all rows that contain the value `us` in the `country` column.

# In[5]:


columns = [
    "datetime",
    "city",
    "state",
    "country",
    "shape",
    "duration (seconds)",
    "duration (hours/min)",
    "comments",
    "date posted"
]

usa_ufo_df = clean_ufo_df.loc[clean_ufo_df["country"] == "us", columns]
usa_ufo_df.head()


# With the `usa_ufo_df["state"].value_counts()` function below, we are pulling the total number of rows (ufo sitings) per state.

# In[7]:


state_counts = usa_ufo_df["state"].value_counts()
state_counts.head()


# In the cell below we are turning the series created above `state_counts` to a dataframe.

# In[8]:


state_ufo_counts_df = pd.DataFrame(state_counts)
state_ufo_counts_df.head()


# Next, we rename the column `state` to `Sum of Sightings`.

# In[9]:


state_ufo_counts_df = state_ufo_counts_df.rename(
    columns={"state": "Sum of Sightings"})
state_ufo_counts_df.head()


# The command below returns the data types for each column in the `usa_ufo_df` dataframe

# In[10]:


usa_ufo_df.dtypes


# Here, we are turning the data type of the column `duration (seconds)` to a float so we cna perform math operations on it.

# In[11]:


usa_ufo_df.loc[:, "duration (seconds)"] = usa_ufo_df["duration (seconds)"].astype("float")
usa_ufo_df.dtypes


# Now that our `duration (seconds)` column is a float we can calculate the total duration that ufos have been seen for.

# In[12]:


# Now it is possible to find the sum of seconds
usa_ufo_df["duration (seconds)"].sum()


# We group by two columns by putting the column names in brackets to denote a list. This allows us to see the total number of sitings per city and organize the cities by state. From here we can easily identify hotspots for ufo sitings. 

# In[13]:


grouped_data = usa_ufo_df.groupby(['state', 'city'])

# Hint: If you are counting records, you can use any column and get the same result. Try it.
grouped_data['datetime'].count()

