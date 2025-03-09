#!/usr/bin/env python
# coding: utf-8

import os
import sys


# FILE HANDLING


# Get the current working directory

current_directory = os.getcwd()
print("Current Directory:", current_directory)


# List all files in the specified directory
files = os.listdir(current_directory)

# Filter out only files (excluding directories)
files = [f for f in files if os.path.isfile(os.path.join(current_directory, f))]

# print("Files in the folder:", files)
# print("Files in the directory:\n" + '\n'.join(files))

# '\n'.join(files): This joins the list of file names into a single string, 
# with each file name separated by a newline character, effectively printing each name on a new line.

# The .join() method in Python is a string method used to concatenate the elements of an iterable 
# (such as a list or tuple) into a single string, with a specified string as a separator between each element.


# We will work with the file : zexample.txt
# The content of the file is :

# The file provides an example of how to use Python. 
# The more I learn, the more enjoyable it becomes. 
# I hope Sofia learns it soon.

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# R
# A
# W
# X

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


# READING from FILES : Python provides various methods

# Read the entire file       : f.read()
# Read the file line by line : f.readline()
# Read all lines into a list : f.readlines()


f = open("zexample.txt", "rt")
f


# The open() function returns a file object, which has a read() method for reading the content of the file:

print(f.read())

# To close the file :

f.close()


# To read the lines : you can return one line by using the readline() method:

# Read one line of the file:

f = open("zexample.txt", "r")
print(f.readline())

# Read two lines of the file:

f = open("zexample.txt", "r")
print(f.readline())
print(f.readline())


# Read the file line by line

f = open("zexample.txt", "r")

for line in f:
    print(line.strip())
f.close()


# Read all lines into a list

f = open("zexample.txt", "r")

lines = f.readlines()
print(lines)

f.close()


# Write to an Existing File :

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("zexample.copy.txt", "a")
f.write("Now the file has more content!")
f.close()

# To examine the updated file :

f = open("zexample.copy.txt", "rt")
print(f.read())


# To open the file and override the content :

f = open("zexample.copy.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# To open and read the file after the overwriting:
f = open("zexample.copy.txt", "r")
print(f.read())


# To create a New File

# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# fnew = open("zexample.new.txt", "x")


# To remove a File
# os.remove("zexample.new.txt")

# To avoid getting an error, 
# to check if the file exists before you try to delete it:

import os  

# Check if the file exists

if os.path.exists("zexample.new.txt"):
    os.remove("zexample.new.txt")      # Remove the file
    print("The file has been removed.")
else:
    print("The file does not exist.")


# WRITING to FILES

# Write data to a file using write() and writelines() methods.


# Write a single line to a file

file = open('zexample.new.txt', 'w')
file.write('Bonjour, Sofia!\n')
file.close()

# Write multiple lines to a file

file = open('zexample.new.txt', 'w')
lines = ['I am so happy.\n', 
         'Great seeing you.\n', 
         'I love you.\n']
file.writelines(lines)
file.close()


fnew = open("zexample.new.txt", "r")
print(fnew.read())
fnew.close()


# To delete a Folder

# import os
# os.rmdir("my_favourite_folder")

# We can only remove empty folders.


# To read specific lines (for example, lines 2 and 3) from a file in Python, 
# you can use a loop to iterate through the lines while keeping track of the current line number. 

# Open the file in read mode
fnew = open("zexample.copy.txt", "r")

# Read all lines into a list
lines = fnew.readlines()

# Print lines 2 and 3 (index 1 and 2 in zero-based index)
print("Line 2:", lines[0].strip())  # Strip to remove any trailing newline or spaces


#####

print(fnew.read())




