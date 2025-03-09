#!/usr/bin/env python
# coding: utf-8

# In[1]:


# a material adapted from : Xiaoping Zhang
# School of Mathematics and Statistics, Wuhan University


# In[2]:


# Python is an object-oriented language and classes form the basis for all data types.
# Python is a dynamically typed language, as there is no advance
# declaration associating an identifier with a particular data type.


# In[3]:


# Identifiers : 33

# 33 specially reserved words that cannot be used as identifiers
# False as continue else from in not
# return yield None assert def except global
# is or try True break del finally
# if lambda pass while and class elif
# for import nonlocal raise with


# In[4]:


# Instantiation : 
# The process of creating a new instance of a class is known as instantiation

# In general, the syntax for instantiating an object is to invoke the constructor of a class.
# Given a class named Widget, we could create an instance using
# • w = Widget(), if the constructor does not require any parameters
# • w = Widget(a, b, c), if the constructor does require parameters

# Another way to indirectly create a new instance of a class is to call a function that creates and returns such an instance.
# eg : sorted()

# Python’s classes may define one or more methods (also known as member functions), which are invoked on a specific instance of 
# a class using the dot (“.”) operator.
# eg : data.sort()

# Some methods return information about the state of an object, but do not change that state. These are known as ACCESSORS.
# Other methods, such as the sort method of the list class, do change the state of an object. 
# These methods are known as MUTATORS or UPDATE methods.

# A class is immutable if each object of that class has a fixed value upon instantiation that cannot subsequently be changed.

# OBJECTS in Python :

# Int class : int()
# Float class : float()

# The list, tuple, and str classes are sequence types in Python, representing a collection of values in which the ORDER is SIGNIFICANT.
# • The LIST class is the most general, representing a sequence of arbitrary objects (akin to an “array” in other languages).
# • The TUPLE class is an immutable version of the list class, benefiting from a streamlined internal representation.
# • The STR class is specially designed for representing an immutable sequence of text characters.

# List class : list() (python uses [])
# Tuple class : tuple() (python uses ())
# String class : str()

# There is one important subtlety. To express a tuple of length one as a literal, a comma must be placed after the element, 
# but within the parentheses.
# (17 , ) # one element tuple
# (17) # a simple numeric

type(17)
type((17,))

# Set class : a collection of elements, without duplicates, and without an inherent order to those elements.
# Python uses curly braces { and } as delimiters.

# Dictionary : a mapping from a set of distinct KEYS to associated VALUES. 
# A dictionary literal also uses curly braces, and because dictionaries were introduced in Python prior to sets, 
# the literal form { } produces an empty dictionary.


# In[5]:


# BITWISE OPERATORS :

# ~ bitwise complement
# & bitwise and
# | bitwise or
# ^ bitwise exclusive-or
# << shift bits left, filling in with zeros
# >> shift bits right, filling in with sign bit

# Bitwise operators in Python are used to perform operations on the individual bits of integer types. 
# They can manipulate binary representations of integers directly. 

# AND (&):
# Compares each bit of two numbers and returns 1 if both bits are 1.

a = 5  # (binary: 0101)
b = 3  # (binary: 0011)
result = a & b  # (binary: 0001) → result is 1

# OR (|):
# Compares each bit of two numbers and returns 1 if at least one of the bits is 1.

result = a | b  # (binary: 0111) → result is 7

# XOR (^):
# Compares each bit of two numbers and returns 1 if the bits are different.

result = a ^ b  # (binary: 0110) → result is 6

# NOT (~):
# Inverts the bits of the number (0 becomes 1 and 1 becomes 0).

result = ~a  # (binary: ...11111010) → result is -6 (two's complement representation)
print(result)

# Left Shift (<<):
# Shifts the bits of the number to the left by a specified number of positions. 
result = a << 1  # (binary: 1010) → result is 10

# Right Shift (>>):
# Shifts the bits of the number to the right by a specified number of positions. 
result = a >> 1  # (binary: 0010) → result is 2

# Summary of Examples : 
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print("a & b =", a & b)  # Output: 1 (0001)
print("a | b =", a | b)  # Output: 7 (0111)
print("a ^ b =", a ^ b)  # Output: 6 (0110)
print("~a =", ~a)        # Output: -6 (two's complement representation)
print("a << 1 =", a << 1) # Output: 10 (1010)
print("a >> 1 =", a >> 1) # Output: 2 (0010)


# In[6]:


# To convert a decimal number to binary:

# Divide the number by 2.
# Record the remainder (0 or 1).
# Continue dividing the quotient by 2 until it becomes 0.
# The binary representation is the remainders read in reverse order.

# Example: Convert 13 to binary:
# 13 ÷ 2 = 6, remainder 1
# 6 ÷ 2 = 3, remainder 0
# 3 ÷ 2 = 1, remainder 1
# 1 ÷ 2 = 0, remainder 1
# Read from bottom to top: 1101

# To convert a binary number to an integer, you can use the positional value of each bit:


# In[7]:


# SEQUENCE OPERATORS

# Each of Python’s built-in sequence types (str, tuple and list) support the following operator syntaxes:

# s[j] element at index j
# s[start:stop] slice including indices [start, stop)
# s[start:stop:step] slice including indices start, start+step,
# start+2*step, ..., up to but not equal to stop
# s+t concatenation of sequences
# k*s shorthand for s+s++...(k times)
# val in s containment check
# val not in s non-containment check


# In[8]:


# Sets and frozensets support the following operators:

# key in s containment check
# key not in s non-containment check
# s1 == s2 s1 is equivalent to s2
# s1 != s2 s1 is not equivalent to s2
# s1 <= s2 s1 is subset of s2
# s1 < s2 s1 is proper subset of s2
# s1 >= s2 s1 is superset of s2
# s1 > s2 s1 is proper superset of s2
# s1 | s2 the union of s1 and s2
# s1 & s2 the intersection of s1 and s2
# s1 - s2 the set of elements in s1 but not s2
# s1 ^ s2 the set of elements in precisely one of s1 or s2


# In[9]:


# Dictionaries support the following operators:

# d[key] value associated with given key
# d[key] = value set (or reset) the value associated with given key
# del d[key] remove key and its associated value from dictionary
# key in d containment check
# key not in d non-containment check
# d1 == d2 d1 is equivalent to d2
# d1 != d2 d1 is not equivalent to d2


# In[10]:


# Extended assignment operator : 

count = 0
count = count + 5
count += 5 
print(count)

# Compound expressions :

# a chained assignment, such as : 
x = y = 0
# a chaining of comparison operators, such as :
1 <= x+y <= 10


# In[11]:


# Conditionals

# Loops 

# Python offers two distinct looping constructs.
# A while loop allows general repetition based upon the repeated testing of a Boolean condition.
# A for loop provides convenient iteration of values from a defined series.

# To loop over all possible indices of the list : python provides a built-in class named range that generates integer sequences.

data = [1,2,3,4]
big_index = 0
for j in range ( len ( data )):
    if data [j] > data [ big_index ]:
       big_index = j
       print(big_index)

# BREAK statement that immediately terminate a while or for loop when executed within its body.

found = False 
target = 2
for item in data :
    if item == target :
       found = True
       print("we have found the target", target)
       break

# CONTINUE statement that causes the current iteration of a loop body to stop, 
# but with subsequent passes of the loop proceeding as expected.

for x in range (7) :
    if (x == 3 or x ==6) :
        continue
    print (x)


# In[12]:


# FUNCTIONS
# METHODS


# FUNCTIONS : 
data = [1,2,2,3,4,5,6,9]
target = 2
def count (data , target ):
    n = 0
    for item in data :
        if item == target :
           n += 1
    return n

# In the context of a function signature, 
# the identifiers used to describe the expected parameters are known as FORMAL parameters, 
# and the objects sent by the caller when invoking the function are the ACTUAL parameters.

# Python provides means for functions to support more than one possible calling signature. 
# Such a function is said to be POLYMORPHIC. The functions can declare one or more default values for parameters, 
# thereby allowing the caller to invoke a function with varying numbers of actual parameters.

# If a default parameter value is present for one parameter, it must be present for all further parameters.

# A polymorphic function : range()
# Three calling syntax:
# • range(n)
# • range(start, stop)
# • range(start, stop, step)

for i in range(1,5,2) :
    print(i)

# POSITIONAL ARGUMENTS :
# With signature foo(a=10, b=20, c=30), parameters sent by the caller are matched, in the given order, to the formal parameters. 
# An invocation of foo(5) indicates that a=5, while b and c are assigned their default values.

# KEYWORD ARGUMENTS : 
# A keyword argument is specified by explicitly assigning an actual parameter to a formal parameter by name.
# With the above definition of function foo, a call foo(c=5) will invoke the function with parameters a=10, b=20, c=5.

# pow(x, y)
# it returns the value xy (as an integer if x and y are integers); equivalent to x**y


# In[13]:


# INPUT : 

# input() # displays a prompt for input values

age = int ( input ("Enter your age in years : "))
max_heart_rate = 206.9 - (0.67 * age )
target = 0.65 * max_heart_rate
print ("Your target fat - burning heat rate is ", target )

# OUTPUT :

# print()


# In[14]:


# FILES : 

# fp = open("sample.txt", access_mode)

# where access_mode is : r, w, a, rb, wb, ab

# Calling Syntax Description
# fp.read() Return the (remaining) contents of a readable file as a string.
# fp.readline() Return (remainder of) the current line of a readable file as a STRING.
# fp.readlines() Return all (remaining) lines of a readable file as a LISTS of STRINGS.

# for line in fp: Iterate all (remaining) lines of a readable file.

# fp.read(k) Return the next k bytes of a readable file as a string.
# fp.seek(k) Change the current position to be at the k-th byte of the file.

# fp.tell() Return the current position, measured as byte-offset from the start.

# fp.write(string) Write given string at current position of the writable file.
# fp.writelines(seq) Write each of the strings of the given sequence at the current position of the writable file. 
# This command does not insert any newlines, beyond those that are embedded in the strings.

# print(...,file=fp) Redirect output of print function to the file.


# In[15]:


# Exception handling : Raising an exception

# Class Description
# Exception A base class for most error types
# NameError Raised if nonexistent identifier used
# AttributeError Raised by syntax obj.foo, if obj has no member named foo
# TypeError Raised when wrong type of parameter is sent to a function
# EOFError Raised if 􀁯end of file􀁰reached for console or file input
# IOError Raised upon failure of I/O operation (e.g., opening file)
# StopIteration Raised by next(iterator) if no element
# IndexError Raised if index to sequence is out of bounds
# KeyError Raised if nonexistent key requested for set or dictionary
# KeyboardInterrupt Raised if user types ctrl-C while program is executing
# ValueError Raised when parameter has invalid value (e.g., sqrt (-5))
# ZeroDivisionError Raised when any division operator used with 0 as divisor

# Raising an Exception

# If a function for computing a square root is sent a negative value as a parameter, it can raise an exception with the command:
# raise ValueError (’x cannot be negative ’)

def sqrt (x):
    if not isinstance (x, (int , float )):
       raise TypeError ("x must be numeric")
    elif x < 0:
       raise ValueError ("x cannot be negative")

print(sqrt(5))
# print(sqrt(-5))

# A function :
def sum1 ( values ):
      total = 0
      for v in values :
          total += v
      return total

# can be rigourously written as :

import collections 
def sum2 ( values ):
    if not isinstance (values , collections.abc.Iterable):
       raise TypeError ("parameter must be an iterable type")
    total = 0
    for v in values :
        if not isinstance (v, (int , float )):
           raise TypeError ("elements must be numeric ")
    total += v
    return total

sum1([1,2,3,4])
#sum2([1,2,3,4,"a"])


# In[16]:


# Exception handling : Catching an Exception

# try :
#  fp = open (’sample .txt ’)
# except IOError as e:
#  print (’Unable to open the file :’, e)

# try :
# You do your operations here ;
# ...
# except :
# If there is any exception , then execute this block .
# ...
# else :
# If there is no exception then execute this block .

age = -1
while age <= 0:
  try :
    age = int( input ('Enter your age in years :'))
    if age <= 0:
       print ('Your age must be positive ')
  except ( ValueError , EOFError ):
    print ('Invalid response ')

# try :
# You do your operations here ;
# ...
# Due to any exception , this may be skipped .
# finally :
# This would always be executed .
# ...


# In[17]:


# Iterators and Generators


# In[18]:


# Iterators : 
# for element in iterable :
# ...

# • Basic container types, such as list, tuple, and set, qualify as iterable types.
# • Furthermore, a string can produce an iteration of its characters, a dictionary can produce an iteration of its keys, 
# and a file can produce an iteration of its lines.

# An iterator in Python is an object that allows you to traverse through a collection 
# (like a list, tuple, dictionary, or set) without exposing the underlying structure of the collection. 
# It provides a way to access the elements of a collection one at a time and is fundamental to Python's iteration protocols.

# Key Concepts : Iterator Protocol:

# An object is considered an iterator if it implements two methods:
# __iter__(): Returns the iterator object itself. This is called when an iterator is required.
# __next__(): Returns the next value from the iterator. If there are no more items to return, it raises the StopIteration exception.

# Iterable vs. Iterator:
# An iterable is any object that can return an iterator (e.g., lists, tuples, strings, dictionaries).
# An iterator is the object that actually implements the iterator protocol and is used to iterate over the iterable.

class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Using the custom iterator
my_iter = MyIterator(5)
for value in my_iter:
    print(value)


# Built-in Iterators : Python has several built-in iterators, such as:
# Lists: You can iterate over lists using a for loop.
# Dictionaries: Iterating over a dictionary iterates over its keys by default.
# Sets: You can iterate over sets just like lists.
# Using the iter() and next() Functions
# You can also manually use the iter() and next() functions:

my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # This would raise StopIteration

# Summary
# Iterator: An object that implements the iterator protocol (__iter__() and __next__()).
# Iterable: An object that can return an iterator (like lists and dictionaries).
# Iterators allow for efficient and lazy iteration over data structures, making them a powerful feature in Python.


# In[19]:


# Generators : 

# The most convenient technique for creating iterators in Python is through the use of generators.
# A generator is implemented with a syntax that is very similar to a function, but instead of returning values, 
# a yield statement is executed to indicate each element of the series.

def factors1 (n):
    results = []
    for k in range (1, n+1) :
        if n % k == 0 :
           results.append (k)
    return results

print(factors1(100))

# In contrast, an implementation of a generator for computing those factors could be implemented as follows:
def factors2 (n):
    for k in range (1, n+1):
        if n % k == 0 :
           yield k

factors2(100)

def factors3 (n):
    k = 1
    while k * k < n:
       if n % k == 0:
          yield k
          yield n // k
    if k*k == n:
       yield k

factors3(200)


def fibonacci ():
   a = 0
   b = 1
   while True :
      yield a
      future = a + b
      a = b
      b = future

fibonacci()


# In[20]:


# Generators :

# Generators in Python are a special type of iterable, like lists or tuples, 
# but instead of storing all values in memory, they generate values on the fly. 
# This is particularly useful for working with large datasets or streams of data because 
# they allow you to iterate through values without needing to load everything into memory at once.

# A generator is defined using a function that contains one or more yield statements. 
# When the function is called, it returns a generator object, but the code within the function does not execute until you iterate over it.

# Yield Statement:
# The yield statement is what makes a function a generator. When the function encounters a yield, it produces a value and pauses its execution, 
# maintaining its state (local variables and execution point). 
# The next time the generator is called, it resumes execution right after the yield.

# Memory Efficiency:
# Since generators yield items one at a time and only when required, they are more memory-efficient compared to lists, especially for large datasets.

def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)

for number in counter:
    print(number)


# In[21]:


# Additional Python Conveniences

# Conditional Expressions : expr1 if condition else expr2
# It is equivalent to the syntax condition ? expr1 : expr2 in C/C++.

def abs (n):
    if n >= 0:
       return n
    else :
      return -n

result2 = abs(-4)
print(result2)

# A conditional expression syntax :

def abs (n):
    return n if n >= 0 else -n

result1 = abs (-40)
print(result1)


# In[22]:


# Additional Python Conveniences

# Comprehension Syntax

# General form of list comprehension : [ expression for value in iterable if condition ]

# A traditional control structure :

# result = []
# for value in iterable :
#    if condition :
#       result.append(expression)


# Generate a list of squares of the numbers from 1 to n)

n = 10

# A traditional control structure :
squares1 = []
for k in range (1, n+1) :
    squares1.append (k*k)
print(squares1)

# List comprehension
squares2 = [k*k for k in range (1, n +1)]
print(squares2)

factors = [k for k in range (1, n+1) if n % k == 0]
print(factors)

# Python supports similar comprehension syntaxes that respectively produce a set, generator, or dictionary. 
# We compare those syntaxes using our example for producing the squares of numbers.

# list comprehension
# [k*k for k in range (1, n+1)]

# set comprehension
# {k*k for k in range (1, n+1)}

# generator comprehension
# (k*k for k in range (1, n+1))

# dictionary comprehension
# {k: k*k for k in range (1, n+1)}


# In[23]:


# Additional Python Conveniences involving the treatment of tuples and other sequence types.

# Automatic PACKING of a tuple
data = 2, 4, 6, 8
print(data) 
# results in identifier, data, being assigned to the tuple (2, 4, 6, 8).

# If the body of a function executes the command,
# return x, y
# it will be formally returning a single object that is the tuple (x, y).


# Automatically UNPACKING a sequence
# The assignment
a, b, c, d = range (7, 11)
# has the effect of assigning a = 7, b = 8, c = 9, d = 10.

print(a)
print(b)
print(c)
print(d)

# The built-in function, divmod(a, b), returns the pair of values (a // b, a % b). 
# quotient , remainder = divmod (a, b) 
# to separately identify the two entries of the returned tuple.

quotient , remainder = divmod (100, 3)

print("quotient")
print(quotient)
print("remainder")
print(remainder)


# In[24]:


# Additional Python Conveniences

# Simultaneous Assignments

# The combination of automatic packing and unpacking forms a technique known as simultaneous assignment.
# • Explicitly assign a series of values to a series of identifiers:
# x, y, z = 6, 2, 5
# • A convenient way for swapping the values associated with two variables:
# j, k = k, j

# The use of simultaneous assignments can greatly simplify the presentation of code.

# Example (The generator producing Fibonacci series)
# With simultaneous assignements, the generator can be implemented more directly as follows:
def fibonacci ():
    a, b = 0, 1
    while True :
       yield a
       a, b = b, a+b


# In[25]:


# Scopes and Namespaces

# Whenever an identifier is assigned to a value, that definition is made with a specific scope.
# • Top-level assignments are typically made in what is known as global scope.
# • Assignments made within the body of a function typically have scope that is local to that function call.

# Each distinct scope in Python is represented using an abstraction known as a NAMESPACE. 
# A namespace manages all identifiers that are currently defined in given SCOPE.

# Python provides several ways to examine a given namespace.
# • dir()
# • vars()


# In[26]:


# What are First-Class Objects?

# A first-class object (or first-class citizen) is an entity that supports all the operations that the language provides for its values. 
# This typically includes:
# Being assigned to a variable (identifier): You can store the object in a variable.
# Being passed as an argument: You can send the object to a function as a parameter.
# Being returned from a function: You can have a function return the object as its result.

# Examples of First-Class Objects in Python :

# 1 . Functions: In languages like Python, functions are first-class objects. You can:

# a. Assign a function to a variable:

def greet():
    return "Hello!"
say_hello = greet  # Assigning the function to a variable
print(say_hello())  # Output: Hello!

# b. Pass a function as an argument:

def execute(func):
    return func()
print(execute(say_hello))  # Output: Hello!

# c. Return a function from another function:

def outer():
    def inner():
        return "Inner function!"
    return inner  # Returning the inner function

new_function = outer()
print(new_function())  # Output: Inner function!

# 2. Objects: In object-oriented programming, instances of classes are also first-class objects:

# You can create an instance of a class and store it in a variable.
# You can pass it to functions and return it from functions.


# In[27]:


# First-Class Objects: 
# These are values or entities in programming that can be treated uniformly — 
# assigned to variables, 
# passed as parameters, 
# and returned from functions.


# Second-Class Objects: 
# These are entities that have limitations in how they can be used compared to first-class objects. 
# Restrictions: Common restrictions include:
# Cannot be assigned to variables.
# Cannot be passed as arguments to functions.
# Cannot be returned from functions.


# In[28]:


# MODULES

import builtins
dir ( builtins )

import math
dir ( math )

# Python's import statement loads definitions from a module into the current namespace.

from math import pi , sqrt
angle = pi /2
v = sqrt (2)
print(angle)
print(v)

# If there are many definitions from the same module to be imported, an asterisk may be used as a wild card
from math import *

# To create a new module, one simply has to put the relevant definitions in a file named with a .py suffix. 
# Those definitions can be imported from any other .py file within the same project directory.

# in the file : utils.py
# def count (data , target ):
#    n = 0
#    for item in data :
#         if item == target :
#             n += 1
#    return n

# from utils import count
# count ([1 ,2 ,2 ,2 ,3] , 2)


# In[29]:


# Existing Modules

# array Compact array storage for primitive types.
# collections Additional data structures and abstract base classes involving collections of objects.
# copy General functions for making copies of objects.
# heapq Heap-based priority queue functions.
# math Common mathematical constants and functions.
# os Support for interactions with the operating system.
# random Random number generation.
# re Support for processing regular expressions.
# sys Additional level of interaction with the Python interpreter.
# time Support for measuring time, or delaying a program.


