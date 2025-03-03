#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Arrays")


# In[2]:


print('''

Unlike Python lists (can store elements of mixed types), arrays must have all elements of same type. 
Having only homogeneous elements makes it memory-efficient.

''')

# https://www.geeksforgeeks.org/python-arrays/


# In[3]:


cars = ["Ford", "Volvo", "BMW"]


# In[4]:


x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars)


# In[5]:


# Looping :
for x in cars:
  print(x)


# In[6]:


# Adding elements:
cars.append("Dacia")
print(cars) 

# Removing elements :
cars.pop(1)       # to remove an element from the array
print(cars)

cars.remove("Toyota")
print(cars)


# In[7]:


print('''

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

''')


# In[8]:


print('''

NumPy Array : These arrays are designed for high-performance operations on large volumes of data and support multi-dimensional arrays and matrices. 

This makes them ideal for complex mathematical computations and large-scale data processing.

NumPy arrays are stored more efficiently than Python lists and provide optimized performance for numerical operations.

''')


# In[9]:


import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4])
print(arr)

# Element-wise operations
print(arr * 2)  

# Multi-dimensional array
arr2d = np.array([[1, 2], [3, 4]])
print(arr2d * 2)


# In[10]:


print('''

The array module in Python provides a space-efficient way to store arrays of numeric values with a specific type constraint. 
Unlike Python lists, which can hold elements of different data types, array.array objects are more memory-efficient because 
they store only elements of a single data type.

This creates an array of type 'i', which stands for a signed integer (typically 4 bytes in size, depending on the platform).

''')


# In[11]:


import array as arr

# creating array of integers
a = arr.array('i', [1, 2, 3])

# accessing First Araay
print(a[0])

# Adding element to array
a.append(5)
print(a)  


# In[12]:


# Adding elements to the array 
# append() is also used to add the value mentioned in its arguments at the end of the Python array.

# The insert(index, value) method shifts elements to the right before inserting.
# Using *a in print() unpacks the array, displaying elements without brackets.
    
import array as arr

# Integer array example
a = arr.array('i', [1, 2, 3])
print("Integer Array before insertion:", *a) # Using *a in print() unpacks the array, displaying elements without brackets

a.append(4)
print(a)  # Output: array('i', [1, 2, 3, 4])

a.insert(1, 4)  # Insert 4 at index 1
print("Integer Array after insertion:", *a)  # Using *a in print() unpacks the array, displaying elements without brackets


# In[13]:


# Removing elements from the array 

# pop() : By default it removes only the last element of the array. To remove element from a specific position, 
# index of that item is passed as an argument to pop() method.


# In[14]:


import array
arr = array.array('i', [1, 2, 3, 1, 5])
print(arr) 

# using remove() method to remove first occurance of 1
arr.remove(1)
print(arr)

# pop() method - remove item at index 2
arr.pop(2)
print(arr)


# In[15]:


# Slicing of an Array

print('''

Elements from beginning to a range use [:Index]
Elements from end use [:-Index]
Elements from specific Index till the end use [Index:]
Elements within a range, use [Start Index:End Index]
Print complete List, use [:].
For Reverse list, use [::-1].

''')


# In[16]:


import array as arr

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)

Sliced_array = a[3:8]
print(Sliced_array)

Sliced_array = a[5:]
print(Sliced_array)

Sliced_array = a[:]
print(Sliced_array)


# In[17]:


print("Searching Element in an Array")


# In[18]:


# Searching Element in an Array

# This function returns the index of the first occurrence of value mentioned in arguments.

import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# index of 1st occurrence of 2
print(arr.index(2))

# index of 1st occurrence of 1
print(arr.index(1))


# In[19]:


print("Updating Elements in an Array")


# In[20]:


# Updating Elements in an Array
# In order to update an element in the array we simply reassign a new value to the desired index we want to update.

import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print(arr)

# update item at index 2
arr[2] = 6
print(arr)

# update item at index 4
arr[4] = 8
print(arr)


# In[21]:


print("Counting Elements in an Array")


# In[22]:


# Counting Elements in an Array
# We can use count() method to count given item in array.

import array

arr = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = arr.count(2)

print("Number of occurrences of 2:", count) 


# In[23]:


print("Reversing Elements in an Array")


# In[24]:


# Reversing Elements in an Array
# In order to reverse elements of an array we need to simply use reverse method.

import array
arr = array.array('i', [1, 2, 3, 4, 5])

arr.reverse()
print("Reversed array:", *arr)


# In[25]:


print("Extend Element from Array")


# In[26]:


# extend() is used to add an array of values to the end of a given or existing array.
# list.extend(iterable)

import array as arr 
a = arr.array('i', [1, 2, 3,4,5])

# using extend() method
a.extend([6,7,8,9,10])
print(a)


# In[27]:


print("1. Array of Floats")

import array

float_array = array.array('f', [1.1, 2.2, 3.3])  # 'f' stands for float (4 bytes per element)
print(float_array)                               # Output: array('f', [1.1, 2.2, 3.3])

# Why Do Floats Show Extra Decimal Places?

# Floats in Python (and in most programming languages) are represented using IEEE 754 floating-point arithmetic, which can cause small precision errors. 
# This is because some decimal numbers (like 1.1) cannot be represented exactly in binary.

# For example, 1.1 in binary is actually stored as something like: 1.10000002384185791015625


# If you want to display only a few decimal places, you can use Python's format() function or an f-string:

print([f"{num:.2f}" for num in float_array])  # Output: ['1.10', '2.20', '3.30']


# In[28]:


# if you need higher precision and less rounding error, use double ('d') instead of float ('f'):

print("2. Array of Doubles")

float_array = array.array('d', [1.1, 2.2, 3.3])  # 'd' stands for double (8 bytes per element)
print(float_array)

# This provides more precision, but will still have small floating-point errors.


# In[29]:


print('''

How Floating-Point Numbers Are Stored

A floating-point number is typically stored in three parts:

Sign bit (1 bit) → Determines positive or negative.
Exponent (8 bits for float, 11 bits for double) → Determines the scale of the number.
Mantissa (Fraction) (23 bits for float, 52 bits for double) → Stores the significant digits.

''')

print('''
A 32-bit single-precision float (float) is stored as:

SEEEEEEEE MMMMMMMMMMMMMMMMMMMMMMM
S (1 bit) → Sign bit (0 = positive, 1 = negative)
E (8 bits) → Exponent (biased by 127)
M (23 bits) → Mantissa (fraction part)

")

print("A 64-bit double-precision float (double) is stored as:

SEEEEEEEEEEE MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
S (1 bit) → Sign bit
E (11 bits) → Exponent (biased by 1023)
M (52 bits) → Mantissa"

''')

# TBC 

print('''

Exponent determines scaling (powers of 2).
Mantissa determines precision (fractional part).
Small rounding errors occur because some decimal numbers cannot be exactly represented in binary.

''')


# In[30]:


#  Array of Characters Using array library ?

# The array module in Python does not support character (char) arrays directly because it is designed for numeric types. 
# However, you can create an array of Unicode characters using the 'u' type code.
# 'u' → Stands for Unicode character (since Python 3, all strings are Unicode).

import array

# Creating an array of Unicode characters
char_array = array.array('u', ['a', 'b', 'c', 'd', 'e'])

# Printing the character array
print("Character Array:", char_array)

# Accessing elements
print("First character:", char_array[0])

# Modifying an element
char_array[1] = 'z'
print("Modified Array:", char_array)

# Appending a new character
char_array.append('f')
print("Array after appending:", char_array)


# In[31]:


print("The built-in array module only supports numeric types, so you will need to use NumPy or a list to store these complex data structures.")


# In[32]:


print('''

Python array Module :

Python array module allows us to create an array with constraint on the data types. 
There are only a few data types supported by this module.

Python Array Supported Type Code

‘b’ 
‘B’ 
‘u’ 
‘h’ 
‘H’ 
‘i’ 
‘I’ 
‘l’ 
‘L’ 
‘q’ 
‘Q’ 
‘f’ 
‘d’ 

C Type

signed char
unsigned char
Py_UNICODE
signed short
unsigned short
signed int
unsigned int
signed long
unsigned long
signed long long
unsigned long long
float
double

Python Type

int
int
Unicode character
int
int
int
int
int
int
int
int
float
float

Minimum size in bytes
1
1
2
2
2
2
2
4
4
8
8
4
8

''')


# In[33]:


print('''

The array module in Python does not support arrays of strings because it is designed for storing only numeric types (such as integers and floats) 
and Unicode characters ('u' type).

However, you can use a list to store an array of strings in Python.
''')


# In[34]:


# However, we can use Numpy. If you need an array-like structure with better performance, use NumPy:

import numpy as np

string_array = np.array(["apple", "banana", "cherry"])

print("NumPy String Array:", string_array)


# In[35]:


print('''

What is dtype=object in NumPy?

In NumPy, dtype=object means that each element in the array is stored as a generic Python object, rather than a fixed-size numerical type 
(like int32, float64, etc.). This allows NumPy to store heterogeneous (different types) or complex objects, such as:

Lists
Dictionaries
Tuples
Sets
Strings of varying lengths
Other arbitrary Python objects

''')


# In[36]:


print('''

1. Numpy Array of Lists

You can store lists inside a NumPy array, but the dtype will be object

''')

import numpy as np

# Explicitly specify dtype=object to allow lists of different lengths
array_of_lists = np.array([[1, 2, 3], [4, 5], [6, 7, 8]], dtype=object)

print("Array of Lists:", array_of_lists)
print("First list:", array_of_lists[0])

# 📌 Note: NumPy does not enforce the same size for inner lists when using dtype=object, unlike its usual behavior for numeric arrays.


# In[37]:


print('''

2. NumPy Array of Strings

Yes! NumPy supports string arrays, but unlike regular Python lists, NumPy may require fixed-size strings for efficient memory storage.

''')

import numpy as np

# Creating an array of strings
string_array = np.array(["apple", "banana", "cherry"])

print("NumPy String Array:", string_array)
print("Data Type:", string_array.dtype)

string_array = np.array(["short", "veryverylongword", "tiny123456789"], dtype="U6")
print(string_array)
print(string_array.dtype)

print('''

If you need longer strings, specify the dtype explicitly

''')

string_array = np.array(["short", "veryverylongword", "tiny"], dtype="U20")
print(string_array)
print(string_array.dtype)

print('''

dtype (UXX)	Max String Length	Use Case
U10	10 characters	Short names, product codes
U20	20 characters	Longer names, common words
U50	50 characters	Addresses, descriptions
U100	100 characters	Sentences, reviews

''')


# In[38]:


print('''

The maximum value for UXX (Unicode string length) in NumPy depends on your system's memory and NumPy's internal handling of arrays.

Technically, there is no fixed upper limit imposed by NumPy, but:

The string length XX should be reasonable based on available memory.

If XX is too large, the array may cause memory allocation errors.

''')

# What Happens with a Large UXX?
# Let's try a very large U1000000 (1 million characters per string):
#

import numpy as np

# Create a NumPy array with a massive Unicode string length
try:
    large_string_array = np.array(["hello", "world"], dtype="U100000000000000")
    print(large_string_array.dtype)
except MemoryError:
    print("Memory Error: U1000000 is too large for your system.")


# In[ ]:





# In[39]:


print('''

3. NumPy Array of Lists of Strings

''')

import numpy as np

# Creating a NumPy array of lists of strings
array_of_lists = np.array([
    ["apple", "banana", "cherry"],
    ["dog", "elephant"],
    ["fish", "giraffe", "hippo", "iguana"]
], dtype=object)

print("Array of Lists of Strings:", array_of_lists)
print("First list:", array_of_lists[0])
print("First element of first list:", array_of_lists[0][0])

print('''

dtype=object ensures that each element in the NumPy array is a list of strings rather than trying to form a uniform matrix.

Each element in the NumPy array is a Python list.
You can access elements just like a normal list (array_of_lists[0] gives the first list).

''')

print(array_of_lists[0]) 
print(array_of_lists[1][0]) 
print(array_of_lists[1][1]) 


# In[ ]:





# In[40]:


print('''

4. Array of Tuples :

# Advantage: Tuples can be stored efficiently if all elements are of the same type.

''')

array_of_tuples = np.array([(1, 2), (3, 4), (5, 6)])
print("Array of Tuples:", array_of_tuples)

print("First tuple:", array_of_tuples[0])
print("Second tuple:", array_of_tuples[1])
print("Second tuple first element:", array_of_tuples[1][0])
print("Second tuple second element:", array_of_tuples[1][1])


# In[41]:


print('''

5. Array of Dictionaries

Since dictionaries are not numeric, NumPy will store them as objects:

''')

array_of_dicts = np.array([
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
], dtype=object)


# Printing the entire array
print("Array of Dictionaries:", array_of_dicts)

# Accessing the first dictionary
print("\nFirst dictionary:", array_of_dicts[0])

# Accessing values of the first dictionary
print("Name of first person:", array_of_dicts[0]["name"])
print("Age of first person:", array_of_dicts[0]["age"])

# Accessing the second dictionary
print("\nSecond dictionary:", array_of_dicts[1])

# Accessing values of the second dictionary
print("Name of second person:", array_of_dicts[1]["name"])
print("Age of second person:", array_of_dicts[1]["age"])

# Warning: NumPy does not provide special dictionary operations; it's just storing them as generic Python objects.

print("\n")

# Get the first dictionary
first_dict = array_of_dicts[0]
print("The first dictionary:", first_dict)

print("\nthe keys:")
print(first_dict.keys())
print("\nthe values:")
print(first_dict.values())

# Get the first key dynamically
first_key = list(first_dict.keys())[0]
first_value = list(first_dict.values())[0]

print("First key in first dictionary:", first_key)
print("First value in first dictionary:", first_value)

print("\nAnother way to write the code above")

# Extract the first key and value dynamically
first_key, first_value = next(iter(first_dict.items()))

print(f"First key in first dictionary: {first_key}")
print(f"First value in first dictionary: {first_value}")

print('''

iter(dict.items()) creates an iterator over the dictionary’s key-value pairs.
next(iterator) returns the first key-value pair from the dictionary.

''')

iterator = iter(first_dict.items())
print(iterator)

first_key, first_value = next(iter(first_dict.items()))
print(first_key)   # name
print(first_value) # Alice


# In[42]:


print('''

6. Array of Sets

Since sets are unordered and mutable, NumPy treats them as generic objects (dtype=object).

''')

array_of_sets = np.array([{1, 2, 3}, {4, 5, 6}, {7, 8}])
print("Array of Sets:", array_of_sets)
print("First set:", array_of_sets[0])

# Notes about the sets 
# We cannot index sets directly like array_of_sets[0][0].
# Accessing elements of a set using indexing is incorrect

# Sets in Python are unordered collections, meaning {1, 2, 3}[0] is not valid.
# You cannot access elements of a set using indexing (set[index]).

# print("First set element:", array_of_sets[0][0])  # ❌ This will cause an error
# print("First set element:", array_of_sets[0][1])  # ❌ This will cause an error


# In[43]:


# We cannot index a set.
# If you need indexing, convert sets to lists first.
# NumPy is not the best choice for storing sets.


# In[44]:


# ✅ 1. Convert Sets to Lists Before Storing in NumPy Array
# Since sets are unordered and not indexable, you can convert them into lists:

import numpy as np

array_of_sets = np.array([list({1, 2, 3}), list({4, 5, 6}), list({7, 8})], dtype=object)
print("Array of Sets:", array_of_sets)

# dtype=object ensures NumPy treats it as an array of Python objects rather than trying to create a structured numerical array.
# Without dtype=object, NumPy attempts to construct a uniform array, which fails due to different list lengths.

print("First set:", array_of_sets[0])
print("First set element:", array_of_sets[0][0])  # ✅ Works now
print("First set element:", array_of_sets[0][1])  # ✅ Works now

# ✅ 2. Use a Python List Instead of a NumPy Array
# Since you are working with sets, you don’t need NumPy. A simple list of sets is better:

array_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8}]
print("Array of Sets:", array_of_sets)

# Get first set
first_set = array_of_sets[0]
print("First set:", first_set)

# Convert to list before accessing elements
first_list = list(first_set)
print("First set element:", first_list[0])  # ✅ Works now
print("First set element:", first_list[1])  # ✅ Works now


# In[45]:


print('''

Working with Arrays in SciPy 

In SciPy, arrays are primarily handled using NumPy arrays (numpy.ndarray), as SciPy builds on NumPy for numerical computations. 
SciPy functions generally accept and return NumPy arrays.

''')

# 1. Creating Arrays
# Since SciPy relies on NumPy, you create arrays using NumPy functions:

import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2. Using Arrays in SciPy
# Many SciPy functions operate on NumPy arrays. For example:

# Linear Algebra (scipy.linalg):

from scipy.linalg import inv

A = np.array([[1, 2], [3, 4]])
A_inv = inv(A)  # Inverse of matrix A
print(A_inv)

# Optimization (scipy.optimize):

from scipy.optimize import minimize

def func(x):
    return x**2 + 3*x + 2  # Example quadratic function

result = minimize(func, x0=0)  # Minimizing the function starting at x=0
print(result.x)

# Interpolation (scipy.interpolate):

from scipy.interpolate import interp1d

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
f = interp1d(x, y)  # Linear interpolation

print(f(2.5))  # Interpolating at x = 2.5


# In[46]:


print ('''

1. Sparse Matrices (scipy.sparse):

from scipy.sparse import csr_matrix

A = np.array([[0, 0, 1], [1, 0, 0], [0, 2, 0]])
A_sparse = csr_matrix(A)  # Compressed Sparse Row format
print(A_sparse)

2. Masked Arrays (scipy.stats.mstats) (handling missing values):

from scipy.stats.mstats import mquantiles

data = np.array([1, 2, np.nan, 4, 5])
masked_data = np.ma.masked_invalid(data)  # Mask NaN values
print(mquantiles(masked_data))  # Compute quantiles while ignoring NaNs

''')


# In[47]:


print('''The floating-point representation''')


# In[48]:


print( '''

How 5.75 is Stored in IEEE 754 Format (32-bit)

Let's break down the floating-point representation of 5.75 in IEEE 754 single-precision format.

Step 1: Convert to Binary

The decimal number 5.75 can be written as:

5.75 = 5 + 0.75

Converting both parts to binary:

5 in binary = 101
0.75 in binary = 0.11 (since 0.75 = 0.5 + 0.25 → 0.11 in binary)
So, 5.75 in binary is 101.11

Step 2: Normalize into Scientific Notation
We rewrite the number in the form:

1.xxxxx × 2^y
For 101.11, shift the decimal point left by 2 places:

1.0111 × 2^2

The mantissa is 0111
The exponent is 2 (but it needs to be biased)

Step 3: Encode the Sign, Exponent, and Mantissa

Sign Bit (S): 0 (since the number is positive)
Exponent (E): Stored with a bias of 127, so:

Actual exponent = 2
Stored exponent = 2 + 127 = 129
129 in binary = 10000001

Mantissa (M): The fractional part after 1. (drop the leading 1):

01110000000000000000000  (23 bits)

Final IEEE 754 Representation (Single Precision)

0 10000001 01110000000000000000000
0 → Positive

10000001 → Exponent (129 in decimal)
01110000000000000000000 → Mantissa

Final Hexadecimal Representation :

Converting 0100 0001 0111 0000 0000 0000 0000 0000 to hex gives :

4    1    7    0    0    0    0    0

that is : 0x41700000

Final Answer

Binary (IEEE 754 single-precision): 0 10000001 01110000000000000000000

Hexadecimal representation: 0x41700000

''')


# In[49]:


print('''

Exponent & Mantissa in Detail

Exponent (E) 

The exponent determines the range of values.
Instead of storing negative exponents, IEEE 754 uses a bias:

For 32-bit float → Bias = 127
For 64-bit double → Bias = 1023

Stored Exponent = Actual Exponent + Bias

Mantissa (Fraction) 

The mantissa stores the precision of the number.
The leading 1 is always assumed in normalized numbers (called implicit leading bit).
More bits in the mantissa → higher precision.

''')


# In[50]:


import struct

# Convert float to raw IEEE 754 binary representation
def float_to_binary(num):
    packed = struct.pack('!f', num)  # Convert to 4 bytes
    binary = ''.join(f'{byte:08b}' for byte in packed)  # Convert to bits
    return binary

print(float_to_binary(5.75))  # Output: '01000000101110000000000000000000'


# In[51]:


print('''

Breaking Down a Negative Floating-Point Number in IEEE 754

Let's analyze how -5.75 is stored in IEEE 754 single-precision format (32-bit).

1. IEEE 754 Structure Recap

A 32-bit floating-point number consists of:

Bit	Component	Purpose
1 bit	Sign bit (S)	0 = Positive, 1 = Negative
8 bits	Exponent (E)	Determines the scaling (power of 2)
23 bits	Mantissa (Fraction) (M)	Stores the significant digits

Now, let’s go step by step for -5.75.

2. Convert -5.75 to Binary

Step 1: Convert Absolute Value to Binary
We first convert 5.75 to binary (ignoring the sign):

5.75 = 5 + 0.75
5 in binary = 101
0.75 in binary = 0.11 (since 0.75 = 0.5 + 0.25 → 0.11 in binary)

Thus, 5.75 in binary is: 101.11

Step 2: Normalize into Scientific Notation
To express in binary scientific notation:

1.0111 × 2^2

The mantissa is 0111 (fractional part after 1.).
The exponent is 2.

3. Encode the Sign, Exponent, and Mantissa

Sign Bit (S)
Since the number is negative, the sign bit is:

Exponent (E) : The actual exponent is 2.

IEEE 754 biases the exponent by 127:
Stored Exponent = 2 + 127 = 129
129 in binary = 10000001

Mantissa (M)
We drop the leading 1 (implicit bit) and keep the fraction:

01110000000000000000000  (23 bits)

4. Final IEEE 754 Representation

Now we assemble the 32-bit IEEE 754 format:

S       EEEEEEEE    MMMMMMMMMMMMMMMMMMMMMMM
1       10000001    01110000000000000000000

So, the binary representation of -5.75 in IEEE 754 single-precision format is:

11000000101110000000000000000000

Step 5: Convert to Hexadecimal

Grouping into 4-bit chunks:
1100 0000 1011 1000 0000 0000 0000 0000

Convert to hex: 0xC0B80000

Final IEEE 754 Encoded Value for -5.75
Binary: 11000000101110000000000000000000

''')


# In[ ]:




