#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://refactoring.guru/design-patterns

# Refactoring design patterns are pre-made blueprints that can be customized to solve recurring design problems in code. 
# Some common refactoring patterns include: 
# Extract Method: Moving a block of code into a separate method.
# Replace Magic Number with Symbolic Constant: Replacing hard-coded numeric values with named constants.
# Extract Class: Refactoring to create a new class.
# Rename Method: Changing the name of a method. 


# In[ ]:





# In[2]:


# notes taken during the class 1


# In[3]:


import os

current_path = os.getcwd()
print("Current directory path:", current_path)


# In[4]:


print("Files:")


# In[5]:


fout = open('znames.txt', 'w')

fout.write('\tAlice\n')
fout.write('Bob\n')
fout.write('\tCharles\n')
fout.write('\tXenia\n')
fout.write('\tKayak\n')
fout.write('\tkayak\n')
fout.write('\tAccept\n')
fout.write('David\n')

fout.close()

fin = open('znames.txt')

while True:
    line = fin.readline()
    if not line:
        break

    name = line.strip()
    print(name)

fin.close()


# In[6]:


# with open() is a Context Manager in Python. It returns a file object (here, assigned to fin).

with open('znames.txt') as fin:
    for line in fin:
        name = line.strip()
        print(name)


# In[7]:


with open('znames.txt') as fin, open('znames-upper.txt', 'w') as fout:
    for line in fin:
        name = line.strip()
        fout.write('{} -> {}\n'.format(name, name.upper()))

# The {} are placeholders for values to be inserted.
# .format(name, name.upper()):
# This method fills in the {} placeholders with the provided arguments.
# The first {} gets replaced by name.
# The second {} gets replaced by name.upper(), which returns the uppercase version of the string name.


# In[ ]:





# In[8]:


print("Functions: ")


# In[9]:


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def calculate(a, b, calc_func):
    return calc_func(a, b)

print(calculate(3, 4, add))
print(calculate(3, 4, subtract))
print(calculate(3, 4, multiply))


# In[10]:


def greet(name):
     print('Hello {}!'.format(name))

greet('John')
g = greet
print(type(g))
g('World')


# In[11]:


# write Python code to read all the words from names.txt
# print all the words that start with x

with open('znames.txt') as fin:
    for line in fin:
        word = line.strip()
        if word.lower().startswith('x'):
            print(word)


# In[ ]:





# In[12]:


print("Self divisors :")

# A number is a self-divisor if it is evenly divisible by all its digits
# Example: 128 is a self-divisor (128 % 1 == 0, 128 % 2 == 0, 128 % 8 == 0)
# Example: 152 is not a self-divisor (152 % 5 != 0)
# Any number that contains a 0 is not a self-divisor, since division by 0 is undefined

# Precondition: number is a positive integer
def is_self_divisor(number):
    # Convert the number to a string to iterate over its digits
    number_str = str(number)

    # Check each digit
    for digit_str in number_str:
        digit = int(digit_str)  # Convert character back to integer

        # If digit is 0 or number is not divisible by digit, it's not a self-divisor
        if digit == 0 or number % digit != 0:
            return False  # Exit early if any digit disqualifies the number

    # All digits passed the test, it's a self-divisor
    return True


# In[13]:


print("Integer (floor) division of a by b :")

# number % 10 gives the last digit of the number (units place).
# number // 10 removes the last digit, shifting the rest of the number to the right.
# it mimics how we would manually peel digits from a number, right to left.

# a // b
# Performs integer (floor) division of a by b, meaning:
# It divides the number and rounds down to the nearest whole number (toward negative infinity).

7 // 2    # → 3   (because 7 ÷ 2 = 3.5 → rounds down to 3)
-7 // 2   # → -4  (because -3.5 rounds down to -4)

# Contrast this with regular division:
- 7 / 2     # → 3.5   (returns a float)


# In[14]:


print("Self divisors :")

# Check if a number is a self-divisor
# A self-divisor is a number that is divisible by each of its digits
# For example: 128 is a self-divisor (128 % 1 == 0, 128 % 2 == 0, 128 % 8 == 0)

def is_self_divisor(number):
    target = number  # Save the original number to use later

    while number > 0:
        digit = number % 10  # Get the last digit of the number

        # If the digit is 0 or the original number is not divisible by the digit
        if digit == 0 or target % digit != 0:
            return False  # It's not a self-divisor

        number //= 10  # Remove the last digit and keep checking

    return True  # All digits were valid, so it's a self-divisor

print(is_self_divisor(128)) # True
print(is_self_divisor(26))  # False
print(is_self_divisor(152)) # False
print(is_self_divisor(101)) # False

for number in range(1, 5):
    if is_self_divisor(number):
        print(number)


# In[15]:


print("Palindromes:")

# Check if a word is a palindrome
# A palindrome reads the same forwards and backwards (like "kayak" or "madam")

def is_palindrome(word):
    return word == word[::-1]  # Reverse the word using slicing and compare with the original

print("Abecedarians:")

# Check if the letters in a word are in alphabetical order
# For example, "accept" is abecedarian (a < c < c < e < p < t)

def is_abecedarian(word):
    for index in range(len(word) - 1):   # Loop through each letter (except the last)
        curr_letter = word[index]        # Current letter
        next_letter = word[index + 1]    # Next letter in the word

        if curr_letter > next_letter:    # If letters are out of order
            return False                 # Not abecedarian, stop early

    return True  # All letters were in order

# if __name__ == '__main__':
# It is a Python idiom that allows you to write code that can be used both as:
# A standalone script, and
# An importable module.
# When a Python file is run directly, Python sets the special built-in variable __name__ to "__main__".
# But if the same file is imported as a module into another script, then __name__ is set to the module's name


if __name__ == '__main__':
    print(is_palindrome('kayak'))    # True, "kayak" is the same forward and backward
    print(is_palindrome('hello'))    # False, "hello" is not a palindrome

    print(is_abecedarian('accept'))  # True, all letters are in alphabetical order
    print(is_abecedarian('brother')) # False, "r" comes after "e"


# In[16]:


from word_checker import is_palindrome, is_abecedarian

# write Python code to read all the words from words.txt
# print all the words that are palindrome
# print(is_palindrome('kayak'))

with open('znames.txt') as fin:
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)


# In[17]:


# write the Python code to find the longest palindrome word in znames.txt

from word_checker import is_palindrome

with open('znames.txt') as fin:
    longest_so_far = ''
    for line in fin:
        word = line.strip()
        if is_palindrome(word):
            if len(word) >= len(longest_so_far):
                longest_so_far = word
    print(longest_so_far)


# In[ ]:





# In[18]:


# Import two functions from word_checker module:
# - is_palindrome: checks if a word is a palindrome
# - is_abecedarian: checks if letters in a word are in alphabetical order

from word_checker import is_palindrome, is_abecedarian

def find_longest(check_func):
    # Open the file containing words (one word per line)
    with open('znames.txt') as fin:
        longest_so_far = ''  # Keeps track of the longest matching word found so far

        for line in fin:
            word = line.strip()  # Remove any leading/trailing whitespace or newline

            if check_func(word):  # Check if the word satisfies the condition
                if len(word) >= len(longest_so_far):  # If it's as long or longer than current longest
                    longest_so_far = word  # Update the longest match

    return longest_so_far  # Return the longest matching word


# Find and print the longest palindrome in the word list
print(find_longest(is_palindrome))

# Find and print the longest abecedarian word in the word list
print(find_longest(is_abecedarian))


# In[ ]:





# In[ ]:




