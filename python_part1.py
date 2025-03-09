#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Arrays : mutable, ordered

# Lists : mutable, ordered

# Dictionaries : mutable, ordered (they maintain the order of items based on the order of insertion.) 

# Sets : mutable, UNORDERED (can not be accessed by index), non-hashable

# Frozensets : IMMUTABLE, UNORDERED, HASHABLE (because they are immutable : it means that frozensets can be used as keys in dictionaries 
# or elements in other sets (which is not possible with mutable sets).)

# Tuples : IMMUTABLE, ordered


# In[26]:


import os 
import numpy
import array


# In[3]:


# LISTS : a sequence of elements that can be of any type.

# Lists are MUTABLE, so they can be changed after they are created.
# Lists are ORDERED, so the elements will be iterated through in the order in which they were added.
# Lists are ITERABLE, so you can iterate through a list using a for loop.
# Lists can be used as keys in dictionaries.
# Lists are efficient for operations such as checking for membership, finding the intersection or union of two lists, 
# and finding the difference between two lists.


# In[4]:


list1 = list(range(10)) # constructor
print(list1)
print(list1[0]) # access

sliced_list = list1[0:5] # slice
print(sliced_list)

list1.append(11) # adding new elements
print(list1)

list1.remove(5)  # removing elements
print(list1)

list1.sort() # sorting the list
print(list1)

index1 = list1.index(11) # searching for element 10 in the list
print(index1)

for element in list1: # iterating through the list
    print(element)


# In[5]:


# TUPLES : collection of data elements of the same type or different types

# Tuples are IMMUTABLE, meaning that they cannot be changed after they are created.

tuple1 = tuple(range(10)) # constructor
print(tuple1)
print(tuple1[0]) # accessing an element

sliced_tuple1 = tuple1[0:8] # Slicing Tuples
print(sliced_tuple1)

# Adding Elements to a Tuple : Elements can NOT be added to a tuple.
# Tuples are immutable, so they cannot be changed after they are created.
# We can simulate appending elements to tuple, by using this code :

tuple2 = (1, 2, 3)
tuple2 = tuple2 + (4,)
print("tuple2 :")
print(tuple2) # will print 1,2,3,4 ; what is going on here? Is it immutable or not?

# Removing Elements from a Tuple : Elements can NOT be removed from a tuple.
# Tuples are immutable, so they cannot be changed after they are created.

# Sorting Tuples : Tuples can NOT be sorted.
# Tuples are immutable, so they cannot be changed after they are created.

# Searching Tuples : Elements can be searched for in a tuple.
# To search for an element in a tuple, you can use the index() method.

index1 = tuple1.index(9)
print(index1)

# Check if the value exists in the tuple before trying to get its index :
value_to_search = 10  # Value to search for

# Check if the value exists in the tuple before trying to get its index
if value_to_search in tuple1:
    index1 = tuple1.index(value_to_search)
    print(index1)
else:
    print(f"Value {value_to_search} not found in tuple1.")

# Iterating Through Tuples :
for element in tuple1:
    print(element)

# We can use tuples to store a collection of elements that should not be changed. 
# For example, we could use a tuple to store the coordinates of a point on a map.
# You can use tuples to check for membership. For example, you could use a
# tuple to check if a particular point is located within a polygon.

# ● Tuples are immutable, so they cannot be changed after they are created.
# ● Tuples are ordered, so the elements will be iterated through in the order in which they were added.
# ● Tuples are iterable, so you can iterate through a tuple using a for loop.
# ● Tuples can be used as keys in dictionaries.
# ● Tuples are efficient for operations such as checking for membership, finding the intersection or union of two tuples, 
# and finding the difference between two tuples.



# In[6]:


# SETS :

# ● A set is a collection of UNIQUE elements.
# ● Sets are MUTABLE, meaning that they can be changed after they are created.
# ● Sets are UNORDERED, so there is no concept of an index. 
# ● It means that you cannot access elements in a set by their index.

# Correctly creating a set by passing a single iterable (list or tuple)
set1 = set([1, 2, 3, 4, 5, 6])  # Using a LIST, and the constructor set()
# or
set2 = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Using a TUPLE, and the constructor set()

print(set1)
print(set2)

# Accessing Set Elements
# Set elements can NOT be accessed by their index.
# Sets are UNORDERED, so there is NO concept of an INDEX.
# However, you can iterate through a set using a for loop.

set1.add(500) # Adding Elements to a Set
print(set1) 

set1.remove(2) # Removing Elements from a Set
print(set1)

# Intersection of Sets
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
intersection = set1 & set2
print(intersection) # it will print {2, 3}

# Union of Sets 
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
union = set1 | set2
print(union) # it will print {1, 2, 3, 4, 5, 6}

# Symmetric Difference of Sets
# The symmetric difference of two sets is the collection of elements that are in either set but not in both sets.
# intersection = set1 & set2 sets can be calculated using the ^ operator.

set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
symmetric_difference = set1 ^ set2 # or set2 ^ set1
print(symmetric_difference) # it will print {1, 4, 5, 6}

if 5 in symmetric_difference : # Serching a set
   print("5 is in the set")
else:
   print("5 is not in the set")

for element in symmetric_difference : # Iterating Through Sets
    print(element)

# Sets are UNORDERED, so there is no guarantee about the order in which the elements will be iterated through.

# ● You can use sets to store a collection of unique elements. For example, you could use a set to store the names of all the students in a class.
# ● You can use sets to check for membership. For example, you could use a set to check if a particular student is enrolled in a class.
# ● You can use sets to find the intersection or union of two sets. 
# For example, you could use a set to find the students who are enrolled in both English and math classes.
# ● You can use sets to find the difference between two sets. For example, you could use a set to find the students 
# who are enrolled in English but not math classes.

# A set in Python is NOT HASHABLE. This is because sets are mutable, meaning their contents can change after they are created. 
# Since the elements within a set can be modified, their hash value would not remain consistent, which is a requirement for an object to be hashable.

# FROZENSET : an IMMUTABLE version of a set, which is hashable.
    
# Because frozensets cannot be changed after they are created, they have a consistent hash value and can be used as dictionary keys
# or elements in other sets.

fs = frozenset([1, 2, 3])
print(fs)
hash(fs)  # This works because frozensets are hashable





# In[7]:


# DICTIONARIES 

# a MUTABLE data structure that stores a mapping of KEYS to VALUES.
# ● Keys are UNIQUE, and values can be of any type.
# ● Dictionaries are ORDERED, but the order is not guaranteed to be stable.
# ● Dictionaries are iterable

dict1 = {"John": 30, "Mary": 25, "Peter": 40}
print(dict1)

dict2 = dict()   # dict() constructor
dict2["name"] = "John"
dict2["age"] = 30
dict2["occupation"] = "Software Engineer"
print(dict2)

dict3 = dict([("name", "John"), ("age", 30), ("occupation", "Software Engineer")])
dict4 = dict(name="John Tanasa", age=40, occupation="Software Engineer")

print(dict3)
print(dict4)

dict5 = dict({"City": "San Jose", "State": "CA"})
print(dict5) # prints {'City': 'San Jose', 'State': 'CA'}

age = dict3.get("age") # Accessing Dictionary Elements by their Keys
print(age)

dict3.update({"Jane": 35}) # Adding Elements to a Dictionary : UPDATE
print(dict3)

name = dict3.pop("name") # Removing Elements from a Dictionary : POP (it returns its value)
print(name)
print(dict3)

del dict3["age"] # del Statement: Removes a specific key and its associated value.
print(dict3)


# In[8]:


for key, value in dict3.items():  # Iterating Through Dictionary
    print(key, value)

if "Jane" in dict3:               # Membership
    print("The name Jane is in the dictionary" )
else:
    print("The name Jane is not in the dictionary" )


# You can access the keys and values in a dictionary using the keys() and values() methods.
# ● The keys() method returns a list of the keys in the dictionary.
# ● The values() method returns a list of the values in the dictionary.

keys = dict3.keys()
values = dict3.values()
print("The keys in the dictionary are:", keys) 
print("The values in the dictionary are:", values)

dict3["occupation"] = "engineer" # Update the key with a new value
dict3["Jane"] = "interesting" # Update the key with a new value
print(dict3)

# To change a KEY in a Python dictionary, you can't directly rename the key, 
# but you can achieve it by adding a new key-value pair with the updated key and then deleting the old key. 

# Original dictionary
dict7 = {"name": "John", "age": 30, "occupation": "Software Engineer"}

# dict7.pop("occupation") removes the old key (occupation) and returns its value.
# The new key (job) is assigned that value.
dict7["job"] = dict7.pop("occupation")
print(dict7)

# Copying a dictionary :
dict8 = dict7.copy()
print(dict8)



# In[9]:


# ARRAYS 

# An array is a data structure that stores a collection of elements of the SAME TYPE
# ● Arrays are ORDERED
# ● Arrays are MUTABLE

# Library : array
# Function : array

# The array() function takes two arguments: the type of the elements (i, f, b, s, c, u) in the array and the initial values of the array.
# b Boolean
# i Integer
# f Float
# c Complex
# s String
# u Unicode string

import array
array_of_integers = array.array("i", [1, 2, 3, 4, 0, 200, 100])

third_element = array_of_integers[2] # Accessing the elements in the array
print(third_element)

array_of_integers.append(5) # The append() method takes an element as an argument and adds the element to the end of the array.
print(array_of_integers)

array_of_integers.remove(2) # The remove() method takes an element as an argument and removes the element from the array.
print(array_of_integers)

for element in array_of_integers: # Arrays can be iterated through using a for loop
    print(element)

if 3 in array_of_integers:        # Membership : You can check if an element is in an array using the in operator.
     print("The element 3 is in the array")
else:
     print("The element 3 is not in the array")

ais = sorted(array_of_integers)         # The sorted() function sorts the elements in the array in ascending order.
print(ais)

array_of_integers[2] = 10 # You can update an element in an array by accessing the element's index and assigning a new value to it.
print(array_of_integers)

# We can concatenate arrays in Python. This can be done using the + operator.

array_1 = array.array("i", [1, 2, 3])
array_2 = array.array("i", [4, 5, 6])
new_array = array_1 + array_2
print(new_array)

array_1 = array.array("i", [1, 2, 3])  # Extend : Concatenate Array with List
list_1 = [4, 5, 6]
array_1.extend(list_1)
print(array_1)

import numpy as np

# Create a 2D array using NumPy
array_of_arrays = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Nested arrays

type(array_of_arrays)

# The data type supported by array are:
# 'b': Signed integer (byte)
# 'B': Unsigned integer (byte)
# 'h': Signed short integer (2 bytes)
# 'H': Unsigned short integer (2 bytes)
# 'i': Signed integer (4 bytes)
# 'I': Unsigned integer (4 bytes)
# 'l': Signed long integer (4 bytes)
# 'L': Unsigned long integer (4 bytes)
# 'f': Floating-point number (4 bytes)
# 'd': Double-precision floating-point number (8 bytes)



# In[10]:


# Derived Data Structures in Python

# ● Arrays: An array is a linear data structure that stores data in contiguous memory locations.
# ● Linked lists: A linked list is a linear data structure that stores data in nodes that are linked together.
# ● Stacks: A stack is a LIFO (last in, first out) data structure that stores data in a last-in, first-out order.
# ● Queues: A queue is a FIFO (first in, first out) data structure that stores data in a first-in, first-out order.
# ● Trees: A tree is a hierarchical data structure that stores data in a parent-child relationship.
# ● Graphs: A graph is a non-linear data structure that stores data in a node-edge relationship.


# Some other examples of data structures ?
# a. Hash tables: A hash table is a data structure that maps keys to values.
# b. Tries: A trie is a data structure that stores data in a tree-like structure.
# c. Heaps: A heap is a data structure that stores data in a priority queue.
# d. Skip lists: A skip list is a data structure that combines the properties of linked lists and binary search trees.

# In Python, a dictionary is essentially an implementation of a hash table. 
# Both structures store key-value pairs, allowing for efficient lookups, insertions, and deletions.

# In operating systems, data structures are used to manage the memory and files on a computer. 
# For example, the file system is a data structure that stores information about the files on a computer, such as their names, sizes, and locations.
# In databases, data structures are used to store and organize data. For example, a relational
# database is a data structure that stores data in tables, which are made up of rows and columns.

