#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[5]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[6]:


total_players = purchase_data.SN.unique()
total_players = len(pd.DataFrame(total_players))
total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[7]:


#unique items
unique_items = purchase_data['Item ID'].unique()
unique_items = len(pd.DataFrame(unique_items))

#Average Price
avg_price = round(purchase_data.Price.mean(),2)
avg_price = str('$' + str(avg_price))
avg_price

#Number of purchases
total_purchases = len(purchase_data)
total_purchases

#Total Revenue
total_revenue = round(purchase_data.Price.sum(),2)
total_revenue = str("$" + str(total_revenue))
total_revenue

#Create df from dictionary
purchasing_analysis = pd.DataFrame({
    "Unique Items": [unique_items],
    "Average Price": [avg_price],
    "Number of Purchases": [total_purchases],
    "Total Revenue": [total_revenue]})

purchasing_analysis


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[19]:


group_df = purchase_data.groupby("Gender")
#count rows for each bootcamp name
genders = group_df.size()
#reset index
genders = genders.reset_index()
genders=genders.rename(columns = {0:'Count'})
total_count=genders['Count'].sum()
genders['Percentage of Players'] = round(((genders['Count']/total_count)*100))
genders['Percentage of Players'] = genders['Percentage of Players'].map("{:.0f}%".format)
genders


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[31]:


#Average price
avg_price = group_df['Price'].mean()
#reset index
avg_price = avg_price.reset_index()
avg_price=avg_price.rename(columns = {'Price':'Average Purchase Price'})

#Total Purchase Value
total_value = group_df['Price'].sum()
#reset index
total_value = total_value.reset_index()
total_value = total_value.rename(columns = {'Price':'Total Purchase Value'})

#Merge tables
purchasing_by_gender = pd.merge(genders, avg_price, on="Gender")
purchasing_by_gender = pd.merge(purchasing_by_gender, total_value, on="Gender")


#Remove 'Percentage of Players' column
purchasing_by_gender = purchasing_by_gender.drop(columns="Percentage of Players")
purchasing_by_gender['Avg Total Purchase per Person'] = purchasing_by_gender['Total Purchase Value']/purchasing_by_gender['Count']
purchasing_by_gender['Avg Total Purchase per Person'] = purchasing_by_gender['Avg Total Purchase per Person'].map("${:.2f}".format)
purchasing_by_gender['Average Purchase Price'] = purchasing_by_gender['Average Purchase Price'].map("${:.2f}".format)
purchasing_by_gender['Total Purchase Value'] = purchasing_by_gender['Total Purchase Value'].map("${:.2f}".format)
purchasing_by_gender


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[50]:


# Create the bins in which Data will be held   
#purchase_data["Age"].max() is 45
bins = [0, 10, 15, 20, 25, 30, 35, 40, 46]

# Create the names for the 8 bins
group_names = ["<10", "10-14", "15-19", "20-24", "25-29","30-34","35-39","40+"]

purchase_data["Age_Bin"] = pd.cut(purchase_data["Age"], bins, labels=group_names, right=False)
purchase_data.head()

group_2 = purchase_data.groupby("Age_Bin")
players_per_age = group_2.size()
#reset index
players_per_age = players_per_age.reset_index()
players_per_age = players_per_age.rename(columns = {0:'Total Count'})
players_per_age

players_per_age['Percentage of Players'] = (players_per_age['Total Count']/(players_per_age['Total Count'].sum()))*100
players_per_age['Percentage of Players'] = players_per_age['Percentage of Players'].map("{:.0f}%".format)
players_per_age


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[55]:


#Average price
age_avg_price = group_2['Price'].mean()
#reset index
age_avg_price = age_avg_price.reset_index()
age_avg_price=age_avg_price.rename(columns = {'Price':'Average Purchase Price'})

#Total Purchase Value
age_total_value = group_2['Price'].sum()
#reset index
age_total_value = age_total_value.reset_index()
age_total_value = age_total_value.rename(columns = {'Price':'Total Purchase Value'})

#Merge tables
purchasing_by_age = pd.merge(players_per_age, age_avg_price, on="Age_Bin")
purchasing_by_age = pd.merge(purchasing_by_age, age_total_value, on="Age_Bin")

#Remove 'Percentage of Players' column
purchasing_by_age = purchasing_by_age.drop(columns="Percentage of Players")
purchasing_by_age['Avg Total Purchase per Person'] = purchasing_by_age['Total Purchase Value']/purchasing_by_age['Total Count']
purchasing_by_age['Avg Total Purchase per Person'] = purchasing_by_age['Avg Total Purchase per Person'].map("${:.2f}".format)
purchasing_by_age['Average Purchase Price'] = purchasing_by_age['Average Purchase Price'].map("${:.2f}".format)
purchasing_by_age['Total Purchase Value'] = purchasing_by_age['Total Purchase Value'].map("${:.2f}".format)
purchasing_by_age


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[71]:


group_players = purchase_data.groupby("SN")
purchase_per_players = group_players.size()
#reset index
purchase_per_players = purchase_per_players.reset_index()
purchase_per_players = purchase_per_players.rename(columns = {0:'Purchase Count'})

#Average price
player_avg_price = group_players['Price'].mean()
#reset index
player_avg_price = player_avg_price.reset_index()
player_avg_price = player_avg_price.rename(columns = {'Price':'Average Purchase Price'})

#Total Purchase Value
player_total_value = group_players['Price'].sum()
#reset index
player_total_value = player_total_value.reset_index()
player_total_value = player_total_value.rename(columns = {'Price':'Total Purchase Value'})

#Merge tables
purchasing_by_player = pd.merge(purchase_per_players, player_avg_price, on="SN")
purchasing_by_player = pd.merge(purchasing_by_player, player_total_value, on="SN")

purchasing_by_player['Average Purchase Price'] = purchasing_by_player['Average Purchase Price'].map("${:.2f}".format)
purchasing_by_player['Total Purchase Value'] = purchasing_by_player['Total Purchase Value'].map("${:.2f}".format)
purchasing_by_player = purchasing_by_player.sort_values(by=['Total Purchase Value'], ascending=False)
purchasing_by_player.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[86]:


group_items = purchase_data.groupby("Item Name")
item_sales = group_items.size()
#reset index
item_sales = item_sales.reset_index()
item_sales = item_sales.rename(columns = {0:'Purchase Count'})

item_price = purchase_data[['Item Name', 'Price']]

items = pd.merge(item_sales, item_price, on="Item Name")
items = items.drop_duplicates('Item Name', keep="first")


items['Total Purchase Value'] = items['Purchase Count']*items['Price']
items['Price'] = items['Price'].map("${:.2f}".format)
items['Total Purchase Value'] = items['Total Purchase Value'].map("${:.2f}".format)
items = items.sort_values(by=['Purchase Count'], ascending=False)
items.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[89]:


items_2 = items.sort_values(by=['Total Purchase Value'], ascending=False)
items_2.head()

