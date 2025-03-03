#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://www.geeksforgeeks.org/python-string/?ref=shm


# In[2]:


print("Strings")


# In[3]:


# Python String :

s = "GfG"

print(s[1])   # access 2nd char
s1 = s + s[0] # update
print(s1)     # print

# Negative indexing :

s = "GeeksforGeeks"

# Accesses 3rd character: 'k'
print(s[-10])  

# Accesses 5th character from end: 'G'
print(s[-5]) 

b = "Hello, World!"
print(b[-5:-2])


# In[4]:


# Strings are indexed starting from 0 and -1 from end. This allows us to retrieve specific characters from the string.


# In[5]:


# String Slicing :
# The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).

s = "GeeksforGeeks"

# Retrieves characters from index 1 to 3: 'eek'
print(s[1:4])  

# Retrieves characters from beginning to index 2: 'Gee'
print(s[:3])   

# Retrieves characters from index 3 to the end: 'ksforGeeks'
print(s[3:])   

# Reverse a string
print(s[::-1])


# In[6]:


print('''

String Immutability

Strings in Python are immutable. This means that they cannot be changed after they are created. 
If we need to manipulate strings then we can use methods like concatenation, slicing, or formatting to create new strings based on the original.

''')


# In[7]:


s = "geeksforGeeks"

# Trying to change the first character raises an error
# s[0] = 'I'  # Uncommenting this line will cause a TypeError

# Instead, create a new string
s = "G" + s[1:]
print(s)


# In[8]:


print('''

General Approach to Changing Characters in a String

To change characters in a string, you need to:

Convert the string into a list (since lists are mutable).
Modify the desired character(s).
Convert it back into a string.

''')


# In[9]:


print("Multiple Characters Changing :")

s = "geeksforGeeks"

# Convert string to a list
s_list = list(s)
print(s_list)

# Modify characters (example: changing 'g' to 'I' and 'G' to 'Z')
s_list[0] = 'I'   # Changing first letter
s_list[9] = 'Z'   # Changing 'G' to 'Z'

# Convert back to a string
s = "".join(s_list)
print(s)  # Output: "IeeksforZeeks"


# In[10]:


print("Alternative: Using String Slicing (One Change at a Time) :")

# If you only need to modify a single character:
s = "geeksforGeeks"

# Change first character
s = "I" + s[1:]
print(s)  # Output: "IeeksforGeeks"

# Change a character in the middle
s = s[:5] + "X" + s[6:]
print(s)  # Output: "IeeksXorGeeks"


# In[11]:


# Deleting a String

# In Python, it is not possible to delete individual characters from a string since strings are immutable. 
# However, we can delete an entire string variable using the del keyword.

s = "GfG"

# Deletes entire string
del s


# In[12]:


print('''
Updating a String :

To update a part of a string we need to create a new string since strings are immutable.

s = "hello geeks"

# Updating by creating a new string
s1 = "H" + s[1:]

# replacnig "geeks" with "GeeksforGeeks"
s2 = s.replace("geeks", "GeeksforGeeks")
print(s1)
print(s2)
''')


# In[13]:


print('''

Common String Methods :

len(s)
s.upper()
s.lower()

s.strip()
s.replace()

''')


# In[14]:


s = "   Gfg   "

# Removes spaces from both ends
print(s.strip())    

s = "Python is fun"

# Replaces 'fun' with 'awesome'
print(s.replace("fun", "awesome"))  


# In[15]:


print(''' 

Concatenating and Repeating Strings :

Strings can be combined by using + operator.
We can repeat a string multiple times using * operator.
''')


# In[16]:


print('''Formatting Strings : Using f-strings''')

name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")

print('''Formatting Strings : Using format() method.''')

s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)


# In[17]:


# Add a placeholder for the price variable. 
# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, 
# like .2f which means fixed point number with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The new price is {20 * 59} dollars"
print(txt)


# In[ ]:





# In[18]:


print(''' About r-strings : 

Raw strings, or r-strings, are prefixed with r or R (e.g., r"string"), and they treat backslashes (\) as literal characters, 
rather than escape sequences.

''')

print("Hello\nWorld")  # Output: 
# Hello
# World  (because \n is interpreted as a newline)

# But in raw strings, backslashes are treated literally:

print(r"Hello\nWorld")  # Output: Hello\nWorld  (backslash remains)

print("Applications of r-strings : Regular expressions (regex)")

# In regex, backslashes have special meanings, so using raw strings helps avoid unnecessary escaping.

import re

pattern = r"\d+\.\d+"  # Matches decimal numbers
result = re.findall(pattern, "Price: 12.50, Discount: 5.0")
print(result)  # Output: ['12.50', '5.0']

pattern = r"\d{3}-\d{2}-\d{4}"  # Matches a Social Security Number format
text = "My SSN is 123-45-6789"
match = re.search(pattern, text)
print(match)
print(match.group())  # Output: 123-45-6789


# In[19]:


print(''' 

The Common String Methods in Python :

upper(): Converts all characters in a string to uppercase.
lower(): Converts all characters in a string to lowercase.
find(substring): Returns the lowest index in the string where the substring is found.
strip(): Removes any leading and trailing characters (space is the default).
replace(old, new): Replaces occurrences of a substring within the string.
split(delimiter): Splits the string at the specified delimiter and returns a list of substrings.
join(iterable): Concatenates elements of an iterable with a specified separator.
startswith(prefix): Checks if the string starts with the specified prefix.
endswith(suffix): Checks if the string ends with the specified suffix.

''')


# In[20]:


print("Strip Method")

text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

# Removing specific characters
text = "###Hello, World!###"
stripped_text = text.strip("#")
print(stripped_text)  # Output: "Hello, World!"


# In[21]:


print("Replace Method")

# Replacing substrings
text = "Hello, World!"
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Output: Hello, Python!

# Replacing characters
text = "banana"
replaced_text = text.replace("a", "o")
print(replaced_text)  # Output: bonono

a = "Hello, World!"
print(a.replace("H", "J"))


# In[22]:


print("Split Method")

# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello, World!"
print(a.split(";")) # returns ['Hello,  World!']


# In[23]:


print('''Escape Sequences ''')

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


# In[24]:


print(''' Join Method : 

The join() method in Python is used to concatenate a sequence of strings with a specified separator.
separator.join(iterable)

separator: The string used to join elements.
iterable: A list, tuple, or any iterable containing strings.

''')


# In[25]:


words = ["Hello", "World", "Python"]
sentence = " ".join(words)  # Joins with a space
print(sentence)


# In[26]:


numbers = ["1", "2", "3", "4"]
comma_separated = ", ".join(numbers)
print(comma_separated)

tuple_strings = ("apple", "banana", "cherry")
result = " - ".join(tuple_strings)
print(result)


# In[27]:


letters = ['P', 'y', 't', 'h', 'o', 'n']
word = "".join(letters)  # Joins with an empty separator (no spaces)
print(word)

lines = ["Line 1", "Line 2", "Line 3"]
paragraph = "\n".join(lines)
print(paragraph)


# In[28]:


# Handling Non-String Elements (Convert to String First)
# If the list contains non-string elements, convert them to strings first.

mixed_list = [1, 2, 3, 4]
result = ", ".join(map(str, mixed_list))  # Convert numbers to strings before joining
print(result)


# In[ ]:




