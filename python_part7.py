#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python File I/O

import os
import sys


# In[2]:


# Get the current working directory

current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List all files in the specified directory
files = os.listdir(current_directory)

# Filter out only files (excluding directories)
files = [f for f in files if os.path.isfile(os.path.join(current_directory, f))]

# print("Files in the folder:", files)
# print("Files in the directory:\n" + '\n'.join(files))


# In[3]:


#    Best Practices for File Handling

#    Use Context Managers: Always use the with statement to open files, as it ensures proper resource management and file closure.

#    Handle Exceptions: Use try-except blocks to handle potential errors during file operations.

#    Work with Relative Paths: Use relative paths instead of absolute paths for better portability.

#    Validate File Paths: Always check if a file exists before performing operations to avoid runtime errors.

#    Use Appropriate File Modes: Choose the correct file mode to prevent data loss and ensure data integrity.

#    Be Mindful of File Sizes: When working with large files, consider reading and writing data in chunks to optimize memory usage.


# In[4]:


#     Python supports several file modes, each serving a different purpose:

#    'r': Read mode (default). Opens a file for reading.
#    'w': Write mode. Opens a file for writing (creates a new file or truncates an existing file).
#    'a': Append mode. Opens a file for writing (creates a new file if it doesn't exist and appends data to an existing file).
#    'b': Binary mode. Used in conjunction with other modes to handle binary files.
#    't': Text mode (default). Used in conjunction with other modes to handle text files.
#    'x': Exclusive creation mode. Creates a new file and fails if the file already exists.


# In[5]:


# When you open a file, it’s crucial to close it after you’re done to free up system resources. 
# You can do this using the close() method:

file = open('zexample.copy.txt', 'r')
file.close()

# Alternatively, you can use a with statement to open a file, which ensures the file is properly closed 
# after the block of code is executed:

with open('zexample.copy.txt', 'r') as file:
  
    # Perform file operations
    pass

# File is automatically closed here


# In[6]:


# READING from a FILE


# In[7]:


# Reading from a File

# Python provides several methods to read data from a file:

#    read(size): Reads the specified number of bytes from the file. 
#                If size is not specified, reads the entire file.
#    readline(): Reads a single line from the file.
#    readlines(): Reads all lines from the file and returns them as a list.


# In[8]:


# Read the entire file

with open('zexample.txt', 'r') as file:
    content = file.read()
    print(content)


# In[9]:


# Read the file line by line

with open('zexample.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end = '')
        line = file.readline()


# In[10]:


# Read all lines into a list

with open('zexample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')


# In[11]:


# WRITING to a FILE


# In[12]:


# Python provides several methods to write data to a file:

#    write(string): Writes the specified string to the file.
#    writelines(list): Writes a list of strings to the file.


# In[13]:


# Write a single line to a file

with open('zexample.copy.txt', 'w') as file:
    file.write("Hi, Sofia!\n")
    file.write("This is a new line.\n")
    
f1 = open("zexample.copy.txt", "rt")
f1
print(f1.read())


# In[14]:


with open('zexample.copy.txt', 'a') as file:
    file.write("Appending this line.\n")

f2 = open("zexample.copy.txt", "rt")
f2
print(f2.read())


# In[15]:


# Write multiple lines to a file

lines = ["Ce mai faci ?\n", 
         "Vom veni la tine.\n", 
         "Te asteptam cu drag.\n"]

with open('zexample.copy.txt', 'w') as file:
    file.writelines(lines)

f3 = open("zexample.copy.txt", "rt")
f3
print(f3.read())


# In[16]:


# Handle Exceptions

# Always handle exceptions to manage errors gracefully and maintain robust applications.

# try:
#    with open('zexample.txt', 'r') as file:
#        content = file.read()
#        print(content)
# except FileNotFoundError:
#    print("File not found.")
# except IOError:
#    print("An I/O error occurred.")


# In[17]:


# Handling CSV Files

# import csv
# reader = csv.reader(file)
# writer = csv.writer(file)


# In[18]:


# Handling JSON Files

# import json
# reader = json.load(file)
# writer = json.dump(file)


# In[19]:


# We can also specify the encoding : 

# with open('example_utf8.txt', 'w', encoding='utf-8')
# with open('example_utf8.txt', 'r', encoding='utf-8')

# UTF-8 (Unicode Transformation Format - 8-bit) is a character encoding standard used 
# to represent text in computers, communication equipment, and other devices that handle text. 
# It is capable of encoding all possible characters (called code points) in Unicode, which 
# encompasses characters from virtually all written languages, as well as symbols, emojis, 
# and control characters.

# Variable-Length Encoding:
#   1 to 4 Bytes: UTF-8 uses one to four bytes to represent each character.
#   ASCII Characters (U+0000 to U+007F): Represented with a single byte, identical to their ASCII encoding.
#   Extended Characters: Use two, three, or four bytes, allowing for the representation of a vast array of 
#   characters from different languages and symbol sets.