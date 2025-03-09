#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DICTIONARIES


# In[2]:


my_dictionary = {"song": "Estranged", 
                 "artist": "Guns N' Roses"}

print(my_dictionary)
print(my_dictionary["song"])

my_dictionary["song"] = "Paradise City"

print(my_dictionary)
print(my_dictionary["song"])


# In[3]:


# Are dictionaries ordered : yes, starting with Python 3.7, the built-in dict type maintains insertion order.

# Merging dictionaries with the .update() 

dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}

dict1.update(dict2)
print(dict1)


# In[4]:


print(dict1.keys())


# In[5]:


print(dict1.values())


# In[6]:


print(dict1.items())


# In[7]:


print(dict1["color"])
print(dict1["shape"])


# In[8]:


# GET
# a .get() method to access a dictionary value if it exists.

dict1.get("color")
dict1.get("shape")


# In[9]:


# Merging the dictionaries
# UPDATE()

cart1 = {"dress": "multi", "jacket": "pink", "shoes": "white"}
cart2 = {"slacks": "black", "blouse": "white", "shoes": "black"}

# Using update() to combine dictionaries

cart3 = cart1.copy()  # Create a copy of cart1
cart3.update(cart2)   # Update the copy with cart2
print(cart3)

cart4 = {"blouse": "red", "purse": "red"}
cart5 = cart2.copy()
cart5.update(cart4)
print(cart5)


# In[ ]:





# In[10]:


# VIEW OBJECT :

# In Python, a view object is an object that provides a dynamic view on the underlying data of a dictionary 
# or similar collection. Instead of copying the data, it gives you a real-time view, 
# meaning if the dictionary (or collection) changes, the view object reflects those changes automatically.


# In[ ]:





# In[11]:


# Removing key-value pairs with the .pop() method. 
# .pop() Method for Dictionaries 

# .pop() takes a key as an argument and removes it from the dictionary. 
# At the same time, it also returns the value that it removes from the dictionary.

dict2.pop("number")
print(dict2)


# In[12]:


# To avoid a KeyError when using the pop() method of a dictionary, you can use one of the following approaches:

# Use the pop() Method with a Default Value
# The pop() method allows you to specify a default value that will be returned 
# if the key does not exist in the dictionary. This prevents a KeyError.

my_dict = {'a': 1, 'b': 2}

# 1
# Using pop() with a default value
value = my_dict.pop('c', 'Key not found')  # Returns 'Key not found' if 'c' doesn't exist
print(value)

# 2
# Check for the Key Before Popping
my_dict = {'a': 1, 'b': 2}

if 'c' in my_dict:
    value = my_dict.pop('c')
else:
    value = 'Key not found'
print(value)  # Output: Key not found


# In[13]:


flowers = {"white": "lily",
               "red": "rose",
               "blue": "carnation",
               "yellow": "buttercup"}

colors = list(flowers.keys())
colors.sort()
show_colors = "Colors of flowers: "
for color in colors:
      show_colors += color + " "
print(show_colors)


# In[ ]:





# In[14]:


# Another example of dictionary :


# In[15]:


MLB_team1 = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}

print(MLB_team1)


# In[16]:


MLB_team2 = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])

print(MLB_team2)


# In[17]:


MLB_team3 = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

print(MLB_team3)


# In[18]:


# The entries in the dictionary display in the order they were defined. 
# But that is irrelevant when it comes to retrieving them. 
# Dictionary elements are not accessed by numerical index.


# In[19]:


MLB_team1['Minnesota']
'Twins'
MLB_team1['Colorado']
'Rockies'


# In[20]:


# An object of any immutable type can be used as a dictionary key. 
# Accordingly, there is no reason you can’t use integers:

d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
d


# In[21]:


# A tuple can also be a dictionary key, because tuples are immutable.

d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
d[(1,1)]
d[(2,1)]


# In[22]:


'Milwaukee' in MLB_team1


# In[ ]:





# In[23]:


# Methods that apply to dictionaries

# d.clear()
# d.get(<key>)
# d.items()

# Nested dictionaries


# In[ ]:





# In[24]:


# STRINGS


# In[25]:


# Strings in Python are arrays of bytes representing unicode characters.
# Python does not have a character data type, a single character is simply a string with a length of 1.


# In[26]:


# To access elements of the string.

a = "Hello, World!"
print(a[0])
print(a[1])


# In[27]:


# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)


# In[28]:


# Checking a String

String1 = "The best things in life are free!"
if "free" in String1:
  print("Yes, 'free' is present.")


# In[29]:


# String Slicing

# Printing 3rd to 12th character
print("\nSlicing characters from 2-12: ")
print(String1[1:12])


# In[30]:


# String Reversing

gfg = "hey geeksforgeeks"
gfg = "".join(reversed(gfg))
print(gfg)


# In[31]:


# Updating a character of the String

String1 = "Hello, I'm a Geek"

## As python strings are immutable, they don't support item updation directly

### there are following two ways :

# 1
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

# 2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)


# In[32]:


# Deleting a character in a String

# Since strings in Python are immutable, you can't delete characters directly from them. 
# However, you can create a new string by excluding the characters you want to remove. 

# Here are several methods you can use to "delete" characters from a string:

# 1. Using Slicing
# You can remove a character at a specific index by slicing and joining the parts of the string 
# before and after the character:

string1 = "Hello, World!"
new_string = string1[:2] + string1[3:]
print(new_string)  

# 2. Using replace() method
# If you want to remove all occurrences of a specific character, you can use replace():

string2 = "Hello, World!"
# Remove all 'l' characters
new_string2 = string2.replace('l', '')
print(new_string2)  


# In[33]:


# REPLACE()

original_string = "hello world"
new_string = original_string.replace("o", "a")

print(new_string)  # Output: "hella warld"


# In[34]:


# To replace a character in a string in python at a specific position, there are two methods :


# In[35]:


# Method 1: Using String Slicing

# Slice the string into parts: before the character you want to replace and after it.
# Concatenate the parts with the new character.

original_string = "hello"
position = 1      # Position to replace (0-indexed)
new_char = 'a'   # New character to insert

# Replace the character at the specified position
new_string = original_string[:position] + new_char + original_string[position + 1:]

print(new_string)  # Output: "hallo"


# In[36]:


# Method 2: Using a List

# We can also convert the string to a list, replace the character, and then join it back to a string.

original_string = "hello"
position = 1      # Position to replace (0-indexed)
new_char = 'a'   # New character to insert

# Convert to a list to allow modification
string_list = list(original_string)
string_list[position] = new_char  # Replace the character at the specified position

# Join the list back into a string
new_string = ''.join(string_list)

print(new_string)  # Output: "hallo"


# In[37]:


# To replace the first occurrence of a character in a string in Python, you can use the str.replace() method 
# with an additional argument that specifies the number of occurrences to replace.

string = "Hello, World!"

# Replace the first occurrence of 'o' with 'a'
new_string = string.replace('o', 'a', 1)
print(new_string)  # Output: "Hella, World!"

original_string = "hello, world"
new_string = original_string.replace('o', 'a', 1)  # Replace the first occurrence of 'o' with 'a'

print(new_string)  # Output: "hella, world"

