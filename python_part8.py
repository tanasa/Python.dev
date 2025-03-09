#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os
import sys


# In[18]:


# Get the current working directory

current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List all files in the specified directory
files = os.listdir(current_directory)

# Filter out only files (excluding directories)
files = [f for f in files if os.path.isfile(os.path.join(current_directory, f))]

# print("Files in the folder:", files)
# print("Files in the directory:\n" + '\n'.join(files))


# In[19]:


# The pickle library in Python is used for serializing and deserializing Python objects, 
# also known as "pickling" and "unpickling." 

# Serialization refers to the process of converting a Python object 
# (like a list, dictionary, or custom class instance) into a byte stream 
# that can be stored in a file or sent over a network. 

# Deserialization is the reverse process, where the byte stream is converted back into a Python object.

# Key Functions in the pickle Library:

# pickle.dump(obj, file): This function serializes (pickles) the object obj and writes it 
#                         to an open file object file.

# pickle.load(file): This function reads a pickled object from a file and 
#                    deserializes (unpickles) it, returning the original Python object.
    
# pickle.dumps(obj): Similar to dump, but instead of writing to a file, 
#                    it returns the pickled object as a byte stream.

# pickle.loads(byte_stream): Similar to load, but instead of reading from a file, 
#                    it loads the object from a byte stream.


# In[20]:


import pickle


# In[21]:


courses = [["Python", 3],
           ["Trig", 3],
           ["Physics", 4],
           ["Yoga", 2]]

with open("classes.bin", "wb") as file:
          pickle.dump(courses, file)
    
with open("classes.bin", "rb") as file:
         course_list = pickle.load(file)
        
i = 0
while i < len(course_list):
       course = course_list[i]
       print(course) 
       print(course[0], course[1], end=" ")
       print("\n") 
       i += 2


# In[22]:


print(courses)
print(course_list)
print(len(course_list))


# In[23]:


import csv

courses = [["Python", 3],
           ["Trig", 3],
           ["Physics", 4],
           ["Yoga", 2]]

with open("zcourses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(courses)

course_list = []

with open("zcourses.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            course_list.append(row)

print("the course list:")
print(course_list)

for i in range(len(course_list) - 2):
        print(i)
        course = course_list[i]
        print(course)
        print(f"{course[0]} ({course[1]})")


# In[24]:


print(course_list[0])
print(course_list[0][0])
print(course_list[0][1])

print(course_list[1])
print(course_list[1][0])
print(course_list[1][1])


# In[29]:


# EXCEPTIONS in PYTHON


# In[30]:


# In Python, exceptions are errors that occur during the execution of a program. 
# When such errors occur, Python raises an exception that can either be handled or cause the program to terminate. 


# In[31]:


# source : GPT


# In[ ]:


'''1. ArithmeticError

    Base class for all errors that occur for numeric calculations.
    Examples:
        ZeroDivisionError: Raised when dividing by zero.
        OverflowError: Raised when the result of an arithmetic operation is too large to be expressed 
                       within the range of the data type.
        FloatingPointError: Raised when a floating-point operation fails.
'''


# In[ ]:


'''
2. AttributeError

    Raised when an invalid attribute reference or assignment is attempted on an object 
    (i.e., the object does not have the specified attribute).
'''


# In[ ]:


'''
3. EOFError

    Raised when the input() function hits an end-of-file condition (EOF) without reading any data.
'''


# In[ ]:


'''
4. ImportError

    Raised when an import statement fails to import a module.
    ModuleNotFoundError: A subclass of ImportError, raised when the module cannot be found.
'''


# In[ ]:


'''
5. IndexError

    Raised when an index is out of range in a list, tuple, or other sequence.
'''


# In[ ]:


'''
6. KeyError

    Raised when a dictionary is accessed with a key that does not exist.
'''


# In[ ]:


'''
7. NameError

    Raised when a local or global name is not found.
'''


# In[ ]:


'''
8. TypeError

    Raised when an operation or function is applied to an object of inappropriate type.
'''


# In[ ]:


'''
9. ValueError

    Raised when a function receives an argument of the correct type but an inappropriate value.
'''


# In[ ]:


'''
10. FileNotFoundError

    Raised when trying to open a file that does not exist.
'''


# In[ ]:


'''
11. OSError

    Raised when a system function returns a system-related error (e.g., file-related errors).
    Examples:
        FileExistsError: Raised when trying to create a file that already exists.
        PermissionError: Raised when there is a permission issue with file operations.
'''


# In[ ]:


'''
12. RuntimeError

    Raised when an error does not fall under any other category.
'''


# In[ ]:


'''
13. StopIteration

    Raised to signal the end of an iterator.
'''


# In[ ]:


'''
14. IndentationError

    Raised when indentation is incorrect (common in Python due to its strict indentation rules).
    Examples:
        TabError: Raised when mixing tabs and spaces.
'''


# In[ ]:


'''
15. MemoryError

    Raised when an operation runs out of memory but can be recovered.
'''


# In[ ]:


'''
16. RecursionError

    Raised when the maximum recursion depth is exceeded.
'''


# In[ ]:


'''
17. AssertionError

    Raised when an assert statement fails.
'''


# In[ ]:


'''
18. SystemExit

    Raised when sys.exit() is called to exit the program.
'''


# In[ ]:


'''
19. KeyboardInterrupt

    Raised when the user interrupts program execution, usually by pressing Ctrl+C.
'''


# In[ ]:


'''
20. NotImplementedError

    Raised when an abstract method that should have been implemented in a subclass is called.
'''


# In[1]:


# Handling Exceptions:

# Exceptions can be handled using try and except blocks:

try:
    # Code that might raise an exception
    x = 1 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)


# In[16]:


# Custom Exceptions:
# https://www.programiz.com/python-programming/user-defined-exception

# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess a number
number = 18

try:
    
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")


# In[ ]:




