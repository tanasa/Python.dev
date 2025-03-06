#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Python Dictionaries")


# In[2]:


# https://www.w3schools.com/python/python_dictionaries.asp
# https://www.geeksforgeeks.org/python-dictionary/
# https://www.programiz.com/python-programming/dictionary
# https://realpython.com/python-dicts/
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# In[3]:


print('''

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, mutable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

''')


# In[4]:


print('''

Dictionary items are ordered, mutable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

''')


# In[5]:


print('''

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

''')


# In[6]:


# The values in dictionary items can be of any data type:
# String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["brand"])


# In[7]:


# Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# In[8]:


print('''

   From Python 3.7 Version onward, Python dictionary are Ordered.
   Dictionary keys are case sensitive: the same name but different cases of Key will be treated distinctly.
   Keys must be immutable: This means keys can be strings, numbers, or tuples but not lists.
   Keys must be unique: Duplicate keys are not allowed and any duplicate key will overwrite the previous value.

''')


# In[9]:


# Unlike dictionary keys, there are no restrictions for dictionary values. Literally none at all. 
# A dictionary value can be any type of object, including mutable types like lists and dictionaries, as well as user-defined objects:

class Point:
     def __init__(self, x, y):
          self.x = x
          self.y = y


{
     "colors": ["red", "green", "blue"],
     "plugins": {"py_code", "dev_sugar", "fasting_py"},
     "timeout": 3,
     "position": Point(42, 21),
}


# In[10]:


places = [
     "Colorado",
     "Chicago",
     "Boston",
     "Minnesota",
     "Milwaukee",
     "Seattle",
]

teams = [
     "Rockies",
     "White Sox",
     "Red Sox",
     "Twins",
     "Brewers",
     "Mariners",
]

dict(zip(places, teams))


# In[ ]:





# In[11]:


print('''Accessing Items''')
# You can access the items of a dictionary by referring to its key name, inside square brackets:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car["model"]
print(x)

x = car.get("brand")
print(x)

print(car)


# In[12]:


print("Get Keys")

x = car.keys()
print(x)

car["year"] = "1986"
print(car.keys()) # after the change

# Get Values

x = car.values()
print(x)


# In[13]:


print('''

Populating Dictionaries Incrementally

Python dictionaries are dynamically sized data structures. This means that you can add key-value pairs to your dictionaries dynamically, 
and Python will take care of increasing the dictionary size for you. 

This characteristic is helpful because it lets you dynamically populate dictionaries with data.

When populating dictionaries, there are three common techniques that you can use. You can:

Assign keys manually
Add keys in a for loop
Build a dictionary with a comprehension

''')

# Adding Keys in a for Loop

squares = {}

for integer in range(1, 10):
     squares[integer] = integer**2

print(squares)

# Building Dictionaries With Comprehensions
# Python has dictionary comprehensions, which is another great tool for creating and populating dictionaries with concise syntax. 

squares = {integer: integer**2 for integer in range(1, 10)}
print(squares)


# In[ ]:





# In[14]:


# Add a new item to the original dictionary, and see that the values list gets updated as well

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) # before the change

car["color"] = "red"

print(x) # after the change


# In[15]:


print("Get Items")

# The items() method will return each item in a dictionary, as tuples in a list.

# Get a list of the key:value pairs

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) # before the change

car["year"] = 2020
print(x) #  after the change


# In[16]:


# Check if Key Exists

if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# In[ ]:





# In[17]:


print("Update Dictionary")

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

cars.update({"color": "red"})
print(cars)


# In[18]:


print("Change Dictionary Items")

# Python dictionaries are mutable (changeable). We can change the value of a dictionary element by referring to its key. For example,

country_capitals = {
  "Germany": "Berlin", 
  "Italy": "Naples", 
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)


# In[19]:


print('''
      del: Removes an item by key.
      pop(): Removes an item by key and returns its value.
      clear(): Empties the dictionary.
      popitem(): Removes and returns the last key-value pair.
''')


# In[20]:


print("Removing Items")

# There are several methods to remove items from a dictionary.
# The pop() method removes the item with the specified key name.

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

cars.pop("model")
print(cars)


# In[21]:


print("Popitem")

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

cars.popitem()
print(cars)


# In[22]:


print('''

pop(key, default)

Removes a specific key-value pair by specifying the key.
Returns the value associated with the key.
If the key does not exist and a default value is provided, it returns the default value instead of raising an error.

''')

print('''

popitem()

Removes and returns the last inserted key-value pair from the dictionary as a tuple (key, value).
Useful for treating a dictionary like a stack (LIFO - Last In, First Out).
Raises a KeyError if the dictionary is empty.

''')


# In[23]:


print("Del")

# The del keyword removes the item with the specified key name:

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del cars["model"]
print(cars)

# The del keyword can also delete the dictionary completely:

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del cars
# print(cars)


# In[24]:


print("Clear")

# The clear() method empties the dictionary:

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

cars.clear()
print(cars)


# In[25]:


cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in cars.keys():
   print(x)

for x in cars.values():
  print(x)

for x, y in cars.items():
   print(x, y)


# In[26]:


print("Copy a Dictionary")

# You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

carsss = cars.copy()
print(carsss)


# In[27]:


print('''Equality and Inequality: == and !''')

# These operators disregard element order when you use them with dictionaries, which is different from what happens with lists, for example:

[1, 2, 3] == [3, 2, 1]
# False
{1: 1, 2: 2, 3: 3} == {3: 3, 2: 2, 1: 1}
# True

[1, 2, 3] != [3, 2, 1]
# True
{1: 1, 2: 2, 3: 3} != {3: 3, 2: 2, 1: 1}
# False


# In[28]:


print('''Union of Dictionaries (| or .union())''')

# The union operator (|) creates a new dictionary by merging the keys and values of two initial dictionaries. 
# The values of the dictionary to the right of the operator take precedence when both dictionaries share keys.

# If a key exists in both, the value from the second dictionary (dict2) overrides the first (dict1).
# It works in Python 3.9+ using | or .union().

# Define dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 4}

# Union using | (Python 3.9+)
union_dict = dict1 | dict2

# Union using update() (for older versions)
union_dict_alt = dict1.copy()
union_dict_alt.update(dict2)

# Print results
print("Union using | operator:", union_dict)
print("Union using .update():", union_dict_alt)
print("Union of Key-Value Pairs Using | (Python 3.9+)")

# Get the union of keys
union_keys = dict1.keys() | dict2.keys()

# Construct a new dictionary with keys from both, keeping original values from dict1 when possible
# union_dict = {k: dict1.get(k, dict2.get(k)) for k in union_keys}

# Print the result
print("Union based on keys:", union_keys)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 4}

print("Union based on key-value pairs:", union_keys)

# Union operator (Python 3.9+)
union_dict = dict1 | dict2

print("Union:", union_dict)


# In[29]:


print("Intersection (&) on Dictionaries")

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 4}

print('''Key-Based Intersection''')
# dict1.keys() & dict2.keys(): Finds common keys.

common_keys = dict1.keys() & dict2.keys()
print(common_keys)  # Output: {'b', 'c'}

print('''Key-Value Pair Intersection''')
# {k: dict1[k] for k in dict1.keys() & dict2.keys()}

intersect_dict = {k: dict1[k] for k in dict1.keys() & dict2.keys()}
print(intersect_dict)  # Output: {'b': 2, 'c': 3}

intersect_dict = {k: dict2[k] for k in dict1.keys() & dict2.keys()}
print(intersect_dict)  # Output: {'b': 20, 'c': 30}


# In[30]:


print('''Difference (-) on Dictionaries''')

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 4}

print("Key-Based Difference")
# dict1.keys() - dict2.keys(): Returns keys in dict1 but not in dict2.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}
diff_keys = dict1.keys() - dict2.keys()
print(diff_keys)  # Output: {'a'}
# Only {'a'} remains because 'b' and 'c' are in both dictionaries.

print("Key-Value Pair Difference")
# {k: v for k, v in dict1.items() if k not in dict2}

diff_dict = {k: v for k, v in dict1.items() if k not in dict2}
print(diff_dict)  # Output: {'a': 1}


# In[31]:


print('''Symmetric Difference (^)''')

# dict1.keys() ^ dict2.keys(): Returns keys that are only in one dictionary.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 4}

print("Symmetric Difference on Keys")

symmetric_diff_keys = dict1.keys() ^ dict2.keys()
print(symmetric_diff_keys)  # Output: {'a', 'd'}

print("Symmetric Difference on Key-Value Pairs")

# Find unique keys in either dictionary
unique_keys = dict1.keys() ^ dict2.keys()
    
# Find keys that are in both but with different values
diff_values = {k for k in dict1.keys() & dict2.keys() if dict1[k] != dict2[k]}

# Find unique keys in either dictionary
unique_keys = dict1.keys() ^ dict2.keys()

# Combine both unique keys and differing value keys
sym_diff = {k: (dict1[k] if k in dict1 else dict2[k]) for k in unique_keys | diff_values}
print(sym_diff)


# In[32]:


def symmetric_difference(dict1, dict2):
    # Find keys that are only in one dictionary
    unique_keys = dict1.keys() ^ dict2.keys()

    # Find keys that exist in both but have different values
    diff_values = {k for k in dict1.keys() & dict2.keys() if dict1[k] != dict2[k]}

    # Combine both unique keys and differing value keys with correct values
    sym_diff = {k: dict1[k] if k in dict1 else dict2[k] for k in unique_keys | diff_values}

    return sym_diff

# Define dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 4}

# Symmetric Difference on Keys
print("Symmetric Difference on Keys")
symmetric_diff_keys = dict1.keys() ^ dict2.keys()
print(symmetric_diff_keys)  # Expected Output: {'a', 'd'}

# Symmetric Difference on Key-Value Pairs
print("\nSymmetric Difference on Key-Value Pairs")
result = symmetric_difference(dict1, dict2)
print(result)  # Expected Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# In[33]:


print("Nested Dictionaries")

# A dictionary can contain dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])
print(myfamily["child3"]["year"])

for x, obj in myfamily.items():
  print(x, obj)

  for y in obj:
      print(y + ':', obj[y]) 


# In[34]:


print('''

   clear()	    Removes all the elements from the dictionary
   copy()	    Returns a copy of the dictionary
   fromkeys()	Returns a dictionary with the specified keys and value
   get()	    Returns the value of the specified key
   items()	    Returns a list containing a tuple for each key value pair
   keys()	    Returns a list containing the dictionary's keys
   pop()	    Removes the element with the specified key
   popitem()	Removes the last inserted key-value pair
   setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
   update()	    Updates the dictionary with the specified key-value pairs
   values()	    Returns a list of all the values in the dictionary

''')


# In[35]:


print('''

Exploring Existing Dictionary-Like Classes

In the Python standard library, you’ll find a few dictionary-like classes that have been adapted to perform specific tasks. 
The most notable examples are the following:

Class	Description

OrderedDict	A dictionary subclass specially designed to remember the order of items, which is defined by the insertion order of keys.
Counter	A dictionary subclass specially designed to provide efficient counting capabilities out of the box.
defaultdict	A dictionary subclass specially designed to handle missing keys in dictionaries.

''')


# In[ ]:





# In[36]:


print('''

Hashable Objects

The keys must be hashable objects like numbers, strings, or tuples. Being hashable means they can be passed to a hash function. 

A hash function takes data of arbitrary size and maps it to a fixed-size value called a hash value — or just hash — which is used for table lookup 
and comparison. In Python, the built-in immutable data types are hashable, and the mutable types are unhashable.

''')


# In[37]:


print('''

What is a Hash function?

A hash function creates a mapping from an input key to an index in hash table, this is done through the use of mathematical formulas known 
as hash functions.

For example: Consider phone numbers as keys and a hash table of size 100. A simple example hash function can be to consider the last two digits 
of phone numbers so that we have valid array indexes as output.

Types of Hash functions:

There are many hash functions that use numeric or alphanumeric keys. This article focuses on discussing different hash functions :

Division Method.
Mid Square Method
Folding Method.
Multiplication Method

''')


# In[38]:


print('''

Components of Hashing

There are majorly three components of hashing:

Key: A Key can be anything string or integer which is fed as input in the hash function the technique that determines an index or location 
for storage of an item in a data structure.

Hash Function: Receives the input key and returns the index of an element in an array called a hash table. The index is known as the hash index.

Hash Table: Hash Table is typically an array of lists. It stores values corresponding to the keys. Hash stores the data in an associative manner 
in an array where each data value has its own unique index.

''')


# In[39]:


print('''

How does Hashing work?

Suppose we have a set of strings {“ab”, “cd”, “efg”} and we would like to store it in a table.

Step 1: We know that hash functions (which is some mathematical formula) are used to calculate the hash value 
which acts as the index of the data structure where the value will be stored.

Step 2: So, let’s assign
“a” = 1,
“b”=2, .. etc, to all alphabetical characters.

Step 3: Therefore, the numerical value by summation of all characters of the string:

 “ab” = 1 + 2 = 3, 
 “cd” = 3 + 4 = 7 , 
 “efg” = 5 + 6 + 7 = 18 

Step 4: Now, assume that we have a table of size 7 to store these strings. 
The hash function that is used here is the sum of the characters in key mod Table size. 
We can compute the location of the string in the array by taking the sum(string) mod 7.

Step 5: So we will then store
“ab” in 3 mod 7 = 3,
“cd” in 7 mod 7 = 0, and
“efg” in 18 mod 7 = 4.

Mapping-Key-with-indices-of-Array

The above technique enables us to calculate the location of a given string by using a simple hash function and rapidly find the value 
that is stored in that location. Therefore the idea of hashing seems like a great way to store (key, value) pairs of the data in a table.

''')


# In[40]:


print('''

What is Collision?

For example: {“ab”, “ba”} both have the same hash value, and string {“cd”,”be”} also generate the same hash value, etc. 
This is known as collision and it creates problem in searching, insertion, deletion, and updating of value. 
The probability of a hash collision depends on the size of the algorithm, the distribution of hash values and the efficiency of Hash Function.

''')


# In[41]:


print('''

How to handle Collisions?

There are mainly two methods to handle collision:

Separate Chaining

Open Addressing

''')

print('''

What is meant by Load Factor in Hashing?

The load factor of the hash table can be defined as the number of items the hash table contains divided by the size of the hash table. 
Load factor is the decisive parameter that is used when we want to rehash the previous hash function or want to add more elements 
to the existing hash table.

''')

print('''

What is Rehashing?

As the name suggests, rehashing means hashing again. Basically, when the load factor increases to more than its predefined value 
(the default value of the load factor is 0.75), the complexity increases. 

So to overcome this, the size of the array is increased (doubled) and all the values are hashed again and stored in the new double-sized array 
to maintain a low load factor and low complexity.

''')


# In[ ]:




