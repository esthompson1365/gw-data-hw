#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[5]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "schools_complete.csv"
student_data_to_load = "students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[43]:


total_schools = school_data_complete['school_name'].unique()
total_schools = len(pd.DataFrame(total_schools))

total_students = school_data_complete['Student ID'].unique()
total_students = len(pd.DataFrame(total_students))

unique_schools = school_data_complete.drop_duplicates('school_name', keep="first")
total_budget = unique_schools['budget'].sum()

avg_math_score = round(school_data_complete['math_score'].mean(),2)

avg_reading_score = round(school_data_complete['reading_score'].mean(),2)

overall_average_score = round((avg_math_score+avg_reading_score)/2,2)

passing_math = school_data_complete[school_data_complete.math_score > 69]
passed_math = round((len(passing_math)/total_students)*100,2)

passing_reading = school_data_complete[school_data_complete.reading_score > 69]
passed_reading = round((len(passing_reading)/total_students)*100,2)

district_summary = pd.DataFrame({
    "Schools": [total_schools],
    "Students": [total_students],
    "Total Budget": [total_budget],
    "Average Math Score": [avg_math_score],
    "Average Reading Score": [avg_reading_score],
    "Average Score": [overall_average_score],
    "Passed Math": [str(passed_math)+"%"],
    "Passed Reading": [str(passed_reading)+"%"]})

district_summary


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[94]:


all_schools = school_data_complete.drop_duplicates('school_name', keep="first")
school_type = all_schools[["school_name","type"]]

schools_group = school_data_complete.groupby("school_name")
students_school = schools_group["type"].count()
students_school = students_school.reset_index()
students_school = students_school.rename(columns = {'type':'Total Students'})
students_school

school_budget = all_schools[["school_name","budget"]]

school_summary = pd.merge(school_type, students_school, on="school_name")
school_summary = pd.merge(school_summary, school_budget, on="school_name")
school_summary['Per Student Budget'] =  school_summary['budget']/school_summary['Total Students']


schools_avg_scores = schools_group[["math_score","reading_score"]].mean()
schools_avg_scores = schools_avg_scores.reset_index()

schools_pass_math =  passing_math.groupby("school_name")
schools_pass_math = schools_pass_math["type"].count()
schools_pass_math = schools_pass_math.reset_index()
schools_pass_math = schools_pass_math.rename(columns = {'type':'% Passing Math'})

schools_pass_reading =  passing_reading.groupby("school_name")
schools_pass_reading = schools_pass_reading["type"].count()
schools_pass_reading = schools_pass_reading.reset_index()
schools_pass_reading = schools_pass_reading.rename(columns = {'type':'% Passing Reading'})

school_scores = pd.merge(schools_pass_math, schools_pass_reading, on="school_name")
school_scores = pd.merge(school_scores, schools_avg_scores, on="school_name")

school_summary = pd.merge(school_summary, school_scores, on="school_name")
school_summary.head()

school_summary['% Passing Math'] = (school_summary['% Passing Math']/school_summary['Total Students'])*100

school_summary['% Passing Reading'] = (school_summary['% Passing Reading']/school_summary['Total Students'])*100

school_summary['% Overall Passing'] = (school_summary['% Passing Reading']+school_summary['% Passing Math'])/2

worst_schools = school_summary.sort_values(by=['% Overall Passing'], ascending=False)
worst_schools.head(5)


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[63]:


worst_schools = school_summary.sort_values(by=['% Overall Passing'], ascending=True)
worst_schools.head(5)


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[87]:


group_grades = school_data_complete.groupby(['school_name','grade'])
math_scores_by_grade = group_grades['math_score'].mean()
math_scores_by_grade = math_scores_by_grade.reset_index()
math_scores_by_grade

math_scores_by_grade.groupby(['school_name', 'grade'])['math_score'].aggregate('first').unstack()


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[88]:


group_grades = school_data_complete.groupby(['school_name','grade'])
reading_scores_by_grade = group_grades['reading_score'].mean()
reading_scores_by_grade = reading_scores_by_grade.reset_index()
reading_scores_by_grade

reading_scores_by_grade.groupby(['school_name', 'grade'])['reading_score'].aggregate('first').unstack()


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[89]:


school_summary.head(5)


# In[95]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]
school_summary["Spending Ranges (Per Student)"] = pd.cut(school_summary["Per Student Budget"], spending_bins, labels=group_names, right=False)
group_per_student_spend = school_summary.groupby('Spending Ranges (Per Student)')
group_per_student_spend[['% Passing Math', '% Passing Reading', 'math_score', 'reading_score', '% Overall Passing']].mean()


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[96]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
school_summary["School Size"] = pd.cut(school_summary["Total Students"], size_bins, labels=group_names, right=False)
group_school_size = school_summary.groupby("School Size")
group_school_size[['% Passing Math', '% Passing Reading', 'math_score', 'reading_score', '% Overall Passing']].mean()


# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[97]:


group_school_type = school_summary.groupby("type")
group_school_type[['% Passing Math', '% Passing Reading', 'math_score', 'reading_score', '% Overall Passing']].mean()


# In[ ]:




