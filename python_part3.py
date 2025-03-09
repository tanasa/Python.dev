#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Map

# The map() function in Python is a built-in function used to apply a specified function to all items 
# in an iterable (like a list, tuple, or set) and return an iterator (or map object) containing the results.

# map(function, iterable, ...)
# function: The function to apply to each item in the iterable. This function must take as many arguments as there are iterables.
# iterable: One or more iterables (e.g., lists, tuples, sets) whose elements will be processed by the function.

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the map object to a list to see the results
squared_list = list(squared_numbers)
print(squared_list)  # Output: [1, 4, 9, 16, 25]

# You can also use map() with a lambda function for concise code:

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)

squared_list = list(squared_numbers)
print(squared_list)  # Output: [1, 4, 9, 16, 25]

# map() can also accept multiple iterables. 
# The function should then take as many arguments as there are iterables. 
# It applies the function to the items of the iterables in parallel:

def add(x, y):
    return x + y

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(add, numbers1, numbers2)

result_list = list(result)
print(result_list)  # Output: [5, 7, 9]


# In[2]:


# Reduce

# The reduce() function in Python is a part of the functools module and is used to apply a specified function cumulatively 
# to the items of an iterable (like a list or tuple). It reduces the iterable to a single cumulative value.

from functools import reduce

# function: A function that takes two arguments and returns a single value. 
# This function is applied cumulatively to the items in the iterable.
# iterable: The iterable whose items will be processed by the function (lists, sets, tuples).

# reduce(function, iterable[, initializer])

# reduce() takes the first two elements of the iterable and applies the function to them.
# It then takes the result and the next item in the iterable and applies the function again.
# This process continues until all items in the iterable have been processed.
# The final result is a single cumulative value.

# You can also use a lambda function with reduce() for concise code:

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 120

# Using Initializer
# If you provide an initializer, it will be used as the starting point for the reduction:

numbers = [1, 2, 3]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result)  # Output: 16 (10 + 1 + 2 + 3)


# In[3]:


# Filter

# The filter() function in Python is a built-in function used to filter elements from an iterable (like a list, tuple, or string) 
# based on a specified condition. 
# It returns an iterator that contains only the elements for which the provided function returns True.

# filter(function, iterable)
# function: A function that tests whether each element of the iterable meets a certain condition. It should return True or False.
# iterable: The iterable (e.g., list, tuple) whose elements will be tested by the function.

# How It Works : filter() applies the specified function to each item in the iterable.
# Only the items for which the function returns True are included in the resulting iterator.

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list to see the results
even_list = list(even_numbers)
print(even_list)  # Output: [2, 4, 6]

# Using Lambda Functions
# You can also use a lambda function with filter() for more concise code:

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

even_list = list(even_numbers)
print(even_list)  # Output: [2, 4, 6]

# Filtering Strings
# You can use filter() with strings as well. For instance, you can filter out vowels from a string:

def is_consonant(char):
    return char.lower() not in 'aeiou'

string = "Hello World"
consonants = filter(is_consonant, string)
consonants
consonant_list = ''.join(consonants)
consonant_list
print(consonant_list)  # Output: "Hll Wrld"



# In[4]:


# Enumerate

# The enumerate() function in Python is a built-in function used to add a counter to an iterable (like a list, tuple, or string) 
# and return it as an enumerate object. 
# This is particularly useful when you need both the index and the value of items in the iterable during iteration.

# enumerate(iterable, start=0)
# iterable: The iterable to be enumerated (e.g., a list, tuple, or string).
# start (optional): The starting index value. The default is 0.

# enumerate() takes the iterable and returns an enumerate object.
# This object produces pairs of INDEX and VALUE for each item in the iterable.
# You can iterate through this object using a loop or convert it to a list.

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)


# In[5]:


# Zip

# The zip() function in Python is a built-in function used to combine two or more iterables (like lists, tuples, or strings) 
# into a single iterable of tuples. Each tuple contains elements from the corresponding position in the input iterables. 
# This is particularly useful for PAIRING elements from multiple sequences.

# zip(*iterables)
# *iterables: One or more iterables to be zipped together.

# How It Works
# zip() takes each iterable and pairs the elements based on their positions.
# It creates an iterator of tuples, where each tuple contains elements from the input iterables.
# If the input iterables are of different lengths, zip() stops creating tuples when the shortest input iterable is exhausted.

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

combined = zip(names, scores)

# Convert to a list to see the results
result = list(combined)
print(result)  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 95)]

# Zipping Multiple Iterables
# You can also zip more than two iterables:

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
ages = [25, 30, 35]

combined = zip(names, scores, ages)
result = list(combined)

print(result)
# Output: [('Alice', 85, 25), ('Bob', 90, 30), ('Charlie', 95, 35)]

# Handling Different Lengths
# When zipping iterables of different lengths, zip() stops at the shortest one:

names = ['Alice', 'Bob']
scores = [85, 90, 95]

combined = zip(names, scores)
result = list(combined)

print(result)  # Output: [('Alice', 85), ('Bob', 90)]


# In[6]:


# Unzip

# You can also unzip a list of tuples back into separate lists using the zip() function with the unpacking operator:

combined = [('Alice', 85), ('Bob', 90), ('Charlie', 95)]
names, scores = zip(*combined)

print(names)  # Output: ('Alice', 'Bob', 'Charlie')
print(scores)  # Output: (85, 90, 95)

# The unzip operator in Python is the asterisk (*). It is used to unpack elements from an iterable, typically in conjunction with the zip() function.

# When you have a list of tuples (or any iterable of iterables) and 
# you want to separate or "unzip" them into individual lists, you can use the * operator.


# In[7]:


# Problem 1: Array Manipulation
# Write a function named sum_even_numbers that accepts an array of integers as a parameter.
# • Inside the function, calculate the sum of all the even numbers in the array.
# • Return the sum.
# • Test your function by providing different arrays and verifying the outpu


# In[8]:


import os
import array as array
import numpy as np

def sum_even_numbers(input_array) :
    # my_array = array.array('i', input_array)
    my_array = np.array(input_array)
    even_array = [x for x in my_array if x % 2 == 0]
    if even_array: 
       print("Even array exists :", even_array)
       total_sum = np.sum(even_array)
       # for number in even_array:
       #    total_sum += number
       print("The sum is :", total_sum)
       return total_sum
    else: 
       print("Array does not exist. There are no even numbers.")
       return 0


array1 = [3, 2, 6, 1, 5, 4] # Unsorted version of the first array
array2 = [50, 20, 40, 10, 30] # Unsorted version of the second array
array3 = [15, 11, 19, 13, 17] # Unsorted, but still contains no even numbers

print(sum_even_numbers(array1)) # Expected Output: 12
print(sum_even_numbers(array2)) # Expected Output: 100
print(sum_even_numbers(array3)) # Expected Output: 0


# In[9]:


# Problem 2: List Manipulation
# • Write a function named long_strings that accepts a list of strings as a parameter.
# • Inside the function, iterate through the list and filter out the strings that have more than 5 characters.
# • Append the filtered strings to a new list.
# • Return the new list.
# • Test your function by providing different lists of strings and verifying the output.


# In[10]:


# Problem 2: List Manipulation

import os
import string 

def long_strings(lst):
    results = list()
    for i in lst : 
        # print(i)
        if len(i) > 5 :
           results.append(i)
    return results 
    
# Testing the function

list1 = ["apple", "banana", "watermelon", "grapes"]
list2 = ["cat", "dog", "bird"]
list3 = ["python", "java", "c++", "javascript"]

print(long_strings(list1)) # Output: ['watermelon', 'grapes']
print(long_strings(list2)) # Output: []
print(long_strings(list3)) # Output: ['python', 'javascript']


# In[11]:


# Problem 3: Tuple Manipulation
# • Write a function named reverse_tuple that accepts a tuple of integers as a parameter.
# • Inside the function, create a new tuple with the elements reversed from the input tuple.
# • Return the new tuple.
# • Test your function by providing different tuples of integers and verifying the output.


# In[12]:


# Problem 3: Tuple Manipulation
def reverse_tuple(tpl):
    tpl = list(tpl)
    tpl_length = len(tpl)
    list_reverse = list()
    for i in range(tpl_length) :
        # list_reverse.append(tpl[tpl_length-i-1])
        list_reverse.insert(i, tpl[tpl_length-i-1])
    return tuple(list_reverse)
    
# Testing the function
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (10, 20, 30, 40, 50)
tuple3 = (11, 13, 15, 17, 19)
print(reverse_tuple(tuple1)) # Output: (5, 4, 3, 2, 1)
print(reverse_tuple(tuple2)) # Output: (50, 40, 30, 20, 10)
print(reverse_tuple(tuple3)) # Output: (19, 17, 15, 13, 11)


# In[13]:


# Problem 4: Write a simple bubble sort function, and call it to sort the array and print those arrays. 

import os 
import numpy as np 

def bubble_sort(unsorted_array) : 
    
    unsorted_array = np.array(unsorted_array)
    # sorted_array = np.empty(len(unsorted_array))
    sorted_array = np.copy(unsorted_array)
    n = len(sorted_array)
    
    # Bubble sort algorithm
    for i in range(n):
        for j in range(0, n - i - 1):  # Last i elements are already sorted
            if sorted_array[j] > sorted_array[j + 1]:  # Compare adjacent elements
                # Swap if the current element is greater than the next
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
    
    return sorted_array  # Return the sorted array

# Unsorted arrays
array1 = [3, 2, 6, 1, 5, 4]
array2 = [50, 20, 40, 10, 30]
array3 = [15, 11, 19, 13, 17]

# Sorting the arrays
sorted_array1 = bubble_sort(array1)
sorted_array2 = bubble_sort(array2)
sorted_array3 = bubble_sort(array3)

# Printing the sorted arrays
print("Sorted array1:", sorted_array1)  # Output: Sorted array1: [1, 2, 5, 5, 6, 9]
print("Sorted array2:", sorted_array2)  # Output: Sorted array2: [0, 3, 4, 7, 8]
print("Sorted array3:", sorted_array3)  # Sorted array3: [11, 13, 15, 17, 19]


