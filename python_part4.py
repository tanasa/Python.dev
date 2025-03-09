#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
current_directory = os.getcwd()
print("Current Directory:", current_directory)


# In[3]:


# Use a raw string
os.chdir(r"C:\Users\user\Desktop\Desktop_old2\Python_course_data_structures_algorithms\Python-Data-Wrangling-main\data")
current_directory = os.getcwd()
print("Current Directory:", current_directory)


# In[4]:


files = os.listdir('.')
print(files)


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[6]:


# Pandas Series 


# In[7]:


# A Pandas Series is a one-dimensional array-like object in the Pandas library that can hold a variety of data types, 
# including integers, floats, strings, and Python objects. 
# It is similar to a column in a spreadsheet or a database table but operates more like a dictionary, 
# as it has both data values and an associated index.


# In[8]:


# One-dimensional: It is a single column of data, unlike a DataFrame, which is two-dimensional (rows and columns).
# Labeled Index: Each element in the Series is associated with an index, which can be either numeric (default) or custom (like a list of labels).
# Flexible Data Types: A Series can hold any data type—numbers, strings, or more complex objects.


# In[9]:


import pandas as pd

data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)


# In[10]:


# Custom index example :
data = [100, 200, 300]
index = ['a', 'b', 'c']
series = pd.Series(data, index=index)
print(series)


# In[11]:


print(series['b'])  # Output: 200 # Accessing the values


# In[12]:


series * 2 # Vectorized operations


# In[ ]:





# In[13]:


# Pandas DataFrames


# In[14]:


# A Pandas DataFrame is a two-dimensional, table-like data structure that allows you to store and manipulate data in rows and columns, 
# similar to a spreadsheet or SQL table. It is one of the most commonly used data structures in the Pandas library and is highly flexible 
# for data analysis and manipulation tasks.

# Key Characteristics of a DataFrame:

# Two-Dimensional: It has rows and columns, which makes it ideal for representing datasets where each row represents an observation and 
# each column represents a feature or variable.

# Labeled Axes (Rows and Columns): Like a Series, a DataFrame has an index for rows, but it also has column labels. 
# Both rows and columns can be accessed and modified by label or integer position.

# Heterogeneous Data: Different columns in a DataFrame can hold different data types (e.g., integers, floats, strings, or even complex data types 
# like lists or objects).


# In[15]:


# Example 1: Creating from a Dictionary

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
}
df = pd.DataFrame(data)
print(df)


# In[16]:


# Example 2: Creating from a List of Lists

data = [['Alice', 25, 'Engineer'], ['Bob', 30, 'Doctor'], ['Charlie', 35, 'Artist']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
print(df)


# In[17]:


# additional operations :
df.dropna()  # Removes rows with missing data
df.fillna(0)  # Replaces missing data with 0


# In[ ]:





# In[18]:


# Working with another dataframe


# In[19]:


unemployment = pd.read_csv('country_total.csv')
type(unemployment)


# In[20]:


unemployment.head(4)


# In[21]:


unemployment.tail(4)


# In[22]:


unemployment.shape


# In[23]:


unemployment.columns


# In[24]:


unemployment.dtypes


# In[26]:


countries_url = 'https://raw.githubusercontent.com/dlab-berkeley/Python-Data-Wrangling/main/data/countries.csv'
countries = pd.read_csv(countries_url)
countries.shape


# In[27]:


countries.head(3)


# In[28]:


countries.tail(3)


# In[29]:


countries.columns


# In[30]:


pd.set_option('display.max_rows', 10)
countries.describe()
pd.reset_option('display.max_rows')


# In[ ]:





# In[31]:


# INDEXING with .loc

# In Pandas, loc[] is primarily used for label-based indexing, 
# allowing you to access a group of rows and columns by their labels or a boolean array. 
# It provides a powerful way to select data by specifying row and column labels explicitly.
# df.loc['row_label']
# df.loc[['row_label1', 'row_label2']]
# df.loc['row_label', 'column_label']
# df.loc['start_label':'end_label'] # range of rows
# df.loc[df['column_name'] > 10]
# df.loc['row_label', ['col1', 'col2']]


# In[32]:


my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_list
my_list[:4]


# In[33]:


my_list[0]
my_list[2:]


# In[34]:


countries.loc[3, 'google_country_code']


# In[35]:


# .loc allows us to index data based on the labels of our DataFrame's index and its column names. 
countries.loc[:4, :]


# In[36]:


countries.loc[2:4, 'name_en']


# In[37]:


type(countries.loc[2:4, 'name_en'])


# In[ ]:





# In[38]:


# INDEXING with .iloc : INTEGER LOCATION 

# In Pandas, iloc is used for integer-location-based indexing, which allows you to select data by position rather than labels. 
# This is particularly useful when you want to access data by its numeric index (row/column number) rather than its name.


# In[39]:


countries.head(4)


# In[40]:


countries.iloc[0:4, 1]  # Selects the second column (index 1)


# In[41]:


countries.iloc[1:4, 0:2]  # Selects rows 1 to 3 and columns 0 to 1


# In[42]:


# Non-contiguous rows and columns
countries.iloc[[0, 3], [1, 2]]  # Selects rows 0 and 3, and columns 1 and 2


# In[43]:


# Using Negative Indexing: Like Python’s standard negative indexing, you can use negative integers in iloc to count from the end.


# In[44]:


countries.iloc[-1]  # Selects the last row


# In[45]:


countries.iloc[0:2, -2:]  # Selects the last two columns


# In[46]:


countries.iloc[ 0:2, [0,4,5] ]


# In[47]:


# Boolean Indexing

# Boolean indexing in Pandas is a powerful way to filter data in a DataFrame or Series based on conditions that return either True or False. 
# This method allows you to select specific rows or columns from your data based on logical conditions, 
# making it easier to analyze and manipulate datasets.

# filtered_df = df[condition]  # Returns rows where Age > 30
# print(filtered_df)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Score': [88, 92, 85, 90]
}

df = pd.DataFrame(data)
filtered_df = df[(df['Age'] > 30) & (df['Score'] > 85)]
print(filtered_df)


# In[48]:


# Example: find countries outside the EU


# In[49]:


test = countries.loc[20:25, :]
test.head(6)


# In[50]:


test['country_group']


# In[51]:


test['country_group'] == 'non-eu'


# In[52]:


# Use the boolean mask to index only those rows that satisfied the test: test[test['country_group'] == 'non-eu']
test[test['country_group'] == 'non-eu']


# In[53]:


countries[countries['longitude'] > 25]


# In[54]:


# Find the average longitude of countries in our data, assign it to the variable average_long
average_long =  test['longitude'].mean()
print(average_long) 

# Find countries that have "above average" longitude 
test['longitude'] > average_long


# In[ ]:





# In[55]:


# Boolean Indexing with multiple conditions

# Select the countries with longitude greater than 25 but less than 30
countries[(countries['longitude'] > 25) & (countries['longitude'] < 30)]


# In[56]:


# Boolean Indexing with multiple conditions

# Select the countries with longitude greater than 30 or less than 0
countries[(countries['longitude'] > 30) | (countries['longitude'] < 0)]


# In[ ]:





# In[57]:


# Computing Missing Values 


# In[58]:


unemployment = pd.read_csv('country_total.csv')
type(unemployment)
unemployment.shape


# In[59]:


# Missing Values


# In[60]:


unemployment.isna().sum()


# In[61]:


# Dealing with missing data. One basic approach would be to drop any row with a missing unemployment rate record.


# In[62]:


# To drop any row with a missing unemployment rate record:

unemployment = unemployment.dropna(subset=['unemployment_rate'])
unemployment.head(6)


# In[63]:


# Sorting Values
# the country with the highest unemployment rates 

unemployment.sort_values(by='unemployment_rate', ascending=False).head(1)


# In[64]:


# Merging DataFrames

unemployment.shape
countries.shape


# In[65]:


unemployment_merged = pd.merge(unemployment, countries, on='country')
unemployment_merged.head(6)


# In[66]:


# Grouping and Aggregating Data

# What if we'd like to know how many observations exist for each country? To do so, we need to group the countries, 
# then count how many times each one occurs. 
# The "group-by" operation is a fundamental technique used with tabular data.


# In[67]:


# VALUE_COUNTS


# In[68]:


# Simple Grouping with .value_counts()
# We typically run this on a single column, and it will return a table showing 
# how many observations there are for each unique value in the column. 


# In[69]:


unemployment_merged['name_en'].value_counts().tail(5)


# In[70]:


# .value_counts() on the DataFrame to find out how many observations are from EU versus non-EU records
unemployment_merged[unemployment_merged["country_group"] == "eu"].country.value_counts().head(5)


# In[71]:


# .value_counts() on the DataFrame to find out how many observations are from EU versus non-EU records
unemployment_merged[unemployment_merged["country_group"] != "eu"].country.value_counts().head(5)


# In[72]:


unemployment_merged['country_group'].value_counts()


# In[73]:


# GROUPBY()


# In[74]:


# Complex grouping with .groupby()
# What if we want to do something more complex, like find out what was the average unemployment rate for EU and non-EU countries?. 
# .value_counts() groups data then counts it, but we need a method that can group data then average it.

# .groupby() -- allows us to group data then apply any aggregate function we want -- count, average, min, max, median, etc.


# In[75]:


#  It doesn't actually return data or output -- it just groups the data
unemployment_merged.groupby('country_group')


# In[76]:


# to select a column of data and specify an aggregate function.

unemployment_merged.groupby('country_group')['unemployment_rate'].mean()


# In[77]:


unemployment_merged.groupby('country_group')['unemployment_rate'].mean()


# In[ ]:





# In[78]:


# To confirm the behavior using boolean indexing as well.

boolean_index = unemployment_merged['country_group'] == 'eu'
boolean_index.head(5)
unemployment_merged.loc[boolean_index, 'unemployment_rate'].mean()


# In[79]:


# To confirm the behavior using boolean indexing as well.

boolean_index = unemployment_merged['country_group'] != 'eu'
boolean_index.head(5)
unemployment_merged.loc[boolean_index, 'unemployment_rate'].mean()


# In[80]:


# Use .groupby() to find the maximum unemployment rate for each country. Sort your results from largest to smallest.
grouped = unemployment_merged.groupby('name_en')['unemployment_rate'].max().sort_values(ascending = False).head(5)


# In[ ]:





# In[81]:


# Data visualization in Pandas 


# In[82]:


grouped = unemployment_merged.groupby('name_en')
grouped


# In[ ]:




