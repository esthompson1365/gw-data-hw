#!/usr/bin/env python
# coding: utf-8

# # Good Reads Summary
# 
# #### The objective of this assignment is for you to explain what is happening in each cell in clear, understandable language. 
# 
# #### _There is no need to code._ The code is there for you, and it already runs. Your task is only to explain what each line in each cell does.
# 
# #### The placeholder cells should describe what happens in the cell below it.

# **Example**: The cell below imports `pandas` as a dependency because `pandas` functions will be used throughout the program, such as the Pandas `DataFrame` as well as the `read_csv` function.

# In[1]:


import pandas as pd


# First, we specify the the path to our csv file and store the path in `goodreads_path`. Then we load the csv file to a dataframe called `goodreads_df` and display the first 5 rows.

# In[2]:


goodreads_path = "Resources/books_clean.csv"

goodreads_df = pd.read_csv(goodreads_path, encoding="utf-8")
goodreads_df.head()


# The first line below counts the number of authors in the dataframe `goodreads_df["Authors"].unique()` references the column named 'Author' and returns a list of authors without duplicates. The `len()` function then counts the length of this list or, in other words, the number of unique authors in the dataframe. 
# 
# Then we write the minimum and maximum publication years to `earliest_year` and `latest_year`.
# 
# We create a new column called 'Total Reviews' which contains the sum of columns 4-8. The sum of all the rows in `goodreads_df['Total Reviews']` is taken and stored in the object `total reviews`

# In[ ]:


author_count = len(goodreads_df["Authors"].unique())

earliest_year = goodreads_df["Publication Year"].min()
latest_year = goodreads_df["Publication Year"].max()

goodreads_df['Total Reviews'] = goodreads_df.iloc[:, 4:].sum(axis=1)
total_reviews = sum(goodreads_df['Total Reviews'])


# Using the pandas function pd.DataFrame, we create a table with our summary statistics

# In[ ]:


summary_table = pd.DataFrame({"Total Unique Authors": [author_count],
                              "Earliest Year": earliest_year,
                              "Latest Year": latest_year,
                              "Total Reviews": total_reviews})
summary_table

