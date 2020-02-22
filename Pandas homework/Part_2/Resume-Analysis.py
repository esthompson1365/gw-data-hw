#!/usr/bin/env python
# coding: utf-8

# # Resume Analysis
# _**HARD: This is a curveball assignment. Plus, this is Python without Pandas.**_
# 
# #### The objective of this assignment is for you to explain what is happening in each cell in clear, understandable language. 
# 
# #### _There is no need to code._ The code is there for you, and it already runs. Your task is only to explain what each line in each cell does.
# 
# #### The placeholder cells should describe what happens in the cell below it.

# The cell below imports `os` as a dependency because the `os.path.join` function. Also, the `string` dependency is needed because later in the script, `string.punctuation` will be used to detect and remove punctuation symbols. Explain what the line `from collection import Counter` does.

# In[1]:


import os
import string
from collections import Counter


#  In the first line of code below we are writing a path to a .md or markdown file. We then create two constants which are defined by all capital letters. These variables cannot be changed.

# In[2]:


# Paths
resume_path = os.path.join(".", 'resume.md')

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet", "modeling"}
REQUIRED_SKILLS 


# Next we create a function called load_file by using def. In this function, we're reading a file, turning all of the text to lowercase and then splitting all the words up into a list. By deafult the split function will seperate text with spaces.

# In[3]:


def load_file(filepath):
    # Helper function to read a file and return the data.
    with open(filepath, "r") as resume_file_handler:
        resume_contents = resume_file_handler.read()
        resume_contents = resume_contents.lower()
        resume_tokens = resume_contents.split()
        return resume_tokens


# The cell below passes the path we created above into the load_file function to create a list.

# In[6]:


# Grab the text for a Resume
word_list = load_file(resume_path)


# Replace this with your clear explanation of what happens in the cell below. 
# Be sure to answer the following:
# * Why is a `set` created?
# * How are we populating the set
# * Why would it be necessary to create a `punctuation` set?
# * What does subtracting from the set do?
# * * Refer to the `resume = resume - punctuation` line
# * What does `\n` do in a string

# Sets are like lists, but unordered so the items have no index. We use a set here beacuse we can loop through the set items using a for loop. We are populating the set with every token or text speperated by spaces from our word_list using the .add function.
# 
# We create a punctuation set to identify all stop words and special characters. Substracting the punctuation from the resume, removes these stop words and special characters from the resume  set.
# 
# Note that the use of \n in a string creates a new line.

# In[12]:


# Create a set of unique words from the resume
resume = set()
resume
# HINT: Single elements in a programming language are often referred to as tokens
for token in word_list:
    resume.add(token)

print('\nWORDS BEFORE MOVING PUNCTUATION')    
print(resume)

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
# HINT: Attributes that are in `resume` that are not in `punctuation` (difference)
resume = resume - punctuation

print('\nWORDS AFTER MOVING PUNCTUATION')    
print(resume)


# In the first two paragraphs below, we use a set intersection determine which required and desired skill this resume has.
# 
# Next, we do some charachter cleaning. Unlike word cleaning, charachter cleaning removes special charachters from words.
# 
# After cleaning our words with some automated solutions, we notice there are still words thta we don't want in our word_list. So we create a variable called stop_words with additional words that we want to remove. Then we overwrite our word_list excluding these stop_words using a list comprehension.

# In[15]:


# Calculate the Required Skills Match using Set Intersection
print('REQUIRED SKILLS')
print(resume & REQUIRED_SKILLS)

# Calculate the Desired Skills Match using Set Intersection
print('DESIRED SKILLS')
print(resume & DESIRED_SKILLS)

# Word Punctuation Cleaning
word_list = [word for word in word_list if word not in string.punctuation]
print('\nWORD LIST AFTER PUNCTUATION REMOVAL')
print(word_list)

# Character Punctuation Cleaning
word_list = [''.join(char for char in word if char not in string.punctuation) for word in word_list]
print('\nWORD LIST AFTER CHARACTER PUNCTUATION REMOVAL')
print(word_list)

# Clean Stop Words
stop_words = ["and", "with", "using", "##", "working", "in", "to"]
word_list = [word for word in word_list if word not in stop_words]
print('\nWORD LIST AFTER STOP WORDS')
print(word_list)


# * Collections.counter is optional, but explain the difference between the `for loop` and using `Counter`
# 
# Below we create a dictionary named `word_count`. The keys for the dictionary are our elements in `word_list` and the values are set to 0. 
# 
# The for loop that we created looks at every word in our `word_list` and if those words mathc a word in our word_count dictionary, it adds 1 to the value of that respective key. 
# 
# You can also use counter here. Note that counter creates a series, while the for loop appends a dictionary.

# In[17]:


# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
# print(word_count)

# Bonus using collections.Counter
word_counter = Counter(word_list)
# print(word_counter)

# Comparing both word count solutions
print(word_count == word_counter)

# Top 10 Words
print("Top 10 Words")
print("=============")


# Replace this with your clear explanation of what happens in the cell below. Which column was sorted and how? How was the top ten selected? Does that explain the significance of `[:10]`?
# 
# In the for loop below, the first thing that happens is the the dictionary is sorted. By deafult the dictionary will be sorted on the values.
# 
# Then we take words from the beginning to position 10 and print their key and value.

# In[24]:


# Sort words by count and print the top 10
sorted_words = []
for word in sorted(word_count, key=word_count.get, reverse=True)[:10]:
    print(f"Token: {word:20} Count: {word_count[word]}")

