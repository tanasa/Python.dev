#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[40]:


print("Arrays:") 


# In[2]:


print('''

🔹 Python Arrays – Key Features

📦 1. Types of Arrays in Python

Built-in array module → Basic, type-restricted arrays (less common)
NumPy arrays (numpy.ndarray) → Powerful, fast, and flexible (widely used in data science)

🔹 2. array.array (from standard library)

from array import array
a = array('i', [1, 2, 3])  # 'i' = typecode for integers

Fixed-type arrays (all elements must be the same type)

Typecodes define data type: 'i' (int), 'f' (float), 'd' (double), etc.

Key methods:

append(x) → Add to end
insert(i, x) → Insert at index
pop(i) → Remove at index
remove(x) → Remove by value
a[i] → Indexing
a[i:j] → Slicing

🔹 3. numpy.ndarray (from NumPy library)

import numpy as np
a = np.array([1, 2, 3])

Supports multi-dimensional arrays, broadcasting, and vectorized operations.

Much faster and more powerful than lists or array.array for numerical work.

Key features:

Fixed data type (e.g., int32, float64)
Fast math: a + 10, a * 2, a ** 2
Slicing & indexing: a[1:3], a[:, 0]
Broadcasting: automatic alignment of shapes in operations
Matrix operations: dot products, transposes, inverses
Shape manipulation: reshape(), flatten(), transpose()

Common methods:

np.append()
np.concatenate()
np.insert()
np.delete()
np.mean()
np.sum()
np.std()
np.argmax(), etc.

🔁 4. Iteration
for x in a: ...
Works for both array.array and NumPy arrays

With NumPy: also supports vectorized operations → no loop needed!
''')


# In[3]:


print('''

What is Vectorization (or "Vectorized Operations")?

Vectorized operations refer to performing operations on entire arrays or collections of data at once, 
rather than looping through elements one by one.

This is a core concept in NumPy, and it makes your code faster and more concise.

🆚 Traditional vs Vectorized

🚫 Without vectorization (loop-based):

result = []
for x in [1, 2, 3]:
    result.append(x * 2)  # Multiply each number by 2

✅ With vectorization (NumPy):

import numpy as np
a = np.array([1, 2, 3])
result = a * 2  # Applies *2 to the whole array at once

Same result: [2, 4, 6], but much faster and cleaner with NumPy.

⚙️ Why Vectorization is Powerful

Internally, NumPy uses optimized C code for operations, avoiding slow Python loops.

It takes advantage of CPU-level parallelism (e.g., SIMD – single instruction, multiple data).

It lets you write code that’s shorter, cleaner, and often closer to math notation.

📌 Examples of Vectorized Operations

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b          # [5, 7, 9]
a * b          # [4, 10, 18]
a ** 2         # [1, 4, 9]
np.sqrt(a)     # [1.0, 1.41, 1.73]

Vectorization over Matrices

matrix = np.array([[1, 2], [3, 4]])
matrix * 10
# [[10, 20],
#  [30, 40]]

''')


# In[4]:


print("Lists")


# In[5]:


print('''

Python Lists – Key Features

Mutable

You can change, add, or remove elements after creation.

Operators

+ → Concatenate two lists: [1, 2] + [3, 4] → [1, 2, 3, 4]
* → Repeat a list: [1, 2] * 3 → [1, 2, 1, 2, 1, 2]

Slicing

Get sublist: a[1:4]
Insert: a[n:n] = [...]
Delete: a[m:n] = []
Replace: a[m:n] = [...]

List Methods

append(x) → Add to end
insert(i, x) → Insert at index
pop(i) → Remove by index (default last)
remove(x) → Remove first matching value
extend(iterable) → Add elements from another list
del a[m:n] → Delete a slice

Looping

for item in list: → Loop through elements
for i, val in enumerate(list): → Loop with index

Other Tips

Lists can hold mixed types (e.g., [1, "two", 3.0])
Can be nested (e.g., [[1, 2], [3, 4]])

Use list comprehensions for compact code:
[x**2 for x in range(5)] → [0, 1, 4, 9, 16]

''')


# In[ ]:





# In[6]:


print('''

What is a List Comprehension in Python?

A list comprehension is a short, elegant way to create a list using a single line of code. 
It’s like a compact for-loop that builds a list.

Feature	     List Comprehension	                Traditional Loop
Syntax	     Compact, one-liner	                Verbose, multiple lines
Readability	 Good for simple transformations	Better for complex logic
Performance	 Slightly faster (in general)	    Slightly slower
''')

print("Basic Syntax: [expression for item in iterable]") 

print("✅ Example 1: Square numbers: ")

squares = [x**2 for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]

squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

print("✅ Example 2: Filtering with if :")
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
# Output: [0, 2, 4, 6, 8]
# Only keeps even numbers.

print("✅ Example 3: Nested loops (cartesian product)")
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)
# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

print("✅ Example 4: Apply a function to items :")

words = ['hello', 'world']
upper_words = [w.upper() for w in words]
print(upper_words)

# Output: ['HELLO', 'WORLD']


# In[ ]:





# In[7]:


print("List Comprehensions: ")


# In[8]:


numbers = [9, 3, 6, 1]

squared = list(map(lambda num: num ** 2, numbers))
print(squared)

squared2 = [num ** 2 for num in numbers]
print(squared2)

numbers = [0, 8, 9, 4, 1, 3]
squared_even_numbers = [num ** 2 for num in numbers if num % 2 == 0]
print(squared_even_numbers)


emails = ['alice 12@gmail.com', 'alice123', 'bob@abc.com', 'alice@gmail.com']
# use list comprehension to return a list of valid email addresses
# a valid email address does not have space and has @

valid_emails = [addr for addr in emails if ' ' not in addr and '@' in addr]
print(valid_emails)

text = 'filter() applies the given function to each element in a list'
result = ['long' if len(word) >= 6 else 'short' for word in text.split()]
print(result)


# In[ ]:





# In[9]:


print("List Comprehensions versus Traditional Loops: ")


# In[ ]:





# In[10]:


print("Operations on Lists:")
      
arr = [0] * 10
print(arr)

# repeat the reference
arr2 = [[]] * 10
print(arr2)

print(arr2[2] is arr2[3])
arr2[0].append(10)
print(arr2)

arr3 = [[] for i in range(10)]
arr3[0].append(10)
print(arr3)


# In[ ]:





# In[11]:


print("Lambda functions:")

# Lambda function that squares a number
s = lambda num: num ** 2

# Call with a single number
print(s(10))  # Output: 100

# To apply the lambda to a list, use map()

numbers = [3, 4, 5, 10]
squared = list(map(s, numbers))
print(squared)  

# Output: [9, 16, 25, 100]


# In[ ]:





# In[12]:


print('''

What is a Lambda Function?

A lambda function in Python is a small anonymous function (i.e., it has no name) used for short, simple operations.

It’s a quick way to define a function inline without using def.

🔧 Syntax: lambda arguments: expression

You can have any number of arguments but only one expression.
The result of the expression is automatically returned.

⚠️ When to Use Lambda Functions : the function is short and simple

You don't need to reuse the function elsewhere
You're passing a function as an argument (like in map(), filter(), sorted())

''')

# 1. Add two numbers:

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# 2. Square a number:

square = lambda x: x ** 2
print(square(4))  # Output: 16

# 3. Use with map():

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
# Output: [1, 4, 9, 16]

# 4. Use with filter():

even = list(filter(lambda x: x % 2 == 0, nums))
# Output: [2, 4]

# 5. Use with sorted() (custom sorting):

words = ['apple', 'banana', 'kiwi']
sorted_by_length = sorted(words, key = lambda w: len(w))
# Output: ['kiwi', 'apple', 'banana']


# In[13]:


print('''

Why is it called "lambda"?

The name "lambda" comes from lambda calculus, a formal system in mathematical logic developed in the 1930s by Alonzo Church.

🧮 Lambda calculus:

It’s a foundational concept in computer science.
It models computation using anonymous functions.

The Greek letter λ (lambda) was used to define functions.
For example, λx.x + 1 is like saying "a function that takes x and returns x + 1".

Python borrowed this terminology when it introduced anonymous functions, and used the keyword lambda to mimic that idea.

''')


# In[ ]:





# In[14]:


print("Map functions:")


# In[15]:


print('''

The map() function in Python is a built-in function that allows you to apply another function to each item in an iterable (like a list, tuple, or set), 
and returns a map object (which is an iterator).

Note: map() returns a map object (an iterator), so we usually wrap it with list() to see the result.

🧠 Basic Syntax

map(function, iterable)
function: A function to apply to each item in the iterable.

iterable: A sequence (like a list, set or tuple).

''')

# ✅ Example 1: Squaring a list of numbers

def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared = map(square, numbers)

print(list(squared))  # Output: [1, 4, 9, 16]


# ✅ Example 2: Using a lambda (anonymous function)

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# ✅ Example 3: With multiple iterables

a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))

print(summed)  # Output: [5, 7, 9]

# 🆚 map() vs List Comprehension

# Using map
list(map(str.upper, ['hello', 'world']))

# Equivalent using list comprehension
[word.upper() for word in ['hello', 'world']]

# ✅ Use map() when you already have a function to apply
# ✅ Use list comprehensions when you want flexibility and readability

# 🚨 Things to remember:
# map() is lazy – it only evaluates when iterated over (e.g., in a for loop or when converted to a list).
# It doesn’t modify the original list.
# It’s often used with built-ins like str(), int(), len(), etc.


# In[ ]:





# In[16]:


print("Filter functions:")


# In[17]:


print('''

What is filter()?

The filter() function filters elements from an iterable based on a function that returns True or False.

🔧 Syntax:

filter(function, iterable)

function: A function that takes one argument and returns True or False.
iterable: Any iterable (like a list, tuple, string, etc.)

Returns a filter object (convert to list or tuple to see results).

''')

# ✅ Example: Filter even numbers

nums = [1, 2, 3, 4, 5, 6]

# Define a function that returns True for even numbers
def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, nums))
print(evens)  # Output: [2, 4, 6]

# 🧪 Using lambda with filter()

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]

print('''

🧠 How it works:

filter() goes through each item in the list:

Applies the function to it.

Keeps the item if the result is True.

''')


# In[ ]:





# In[18]:


numbers = [0, 8, 9, 4, 1, 3]

even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
print(even_numbers)

text = 'filter() applies the given function to each element in a list'

# print all the "long words" from text, whose length is >= 6

long_words = list(
    filter(
        lambda word: len(word) >= 6,
        text.split()
    )
)
print(long_words)

# create a list with the squared values of only the even values from numbers

squared_even_numbers = list(
    map(
        lambda num: num ** 2,
        filter(
            lambda num: num % 2 == 0,
            numbers
        )
    )
)
print(squared_even_numbers) # [0, 64, 16]


# In[ ]:





# In[19]:


print("Comparisons :")


# In[20]:


print("Version 1 of the code :")


# In[21]:


# Return a new list, each value is the square of the corresponding value in arr

def square(arr):
    result = []

    for num in arr:
        result.append(num * num)

    return result

# Return a new list, each value is 10 times of the corresponding value in arr

def time10(arr):
    result = []

    for num in arr:
        result.append(num * 10)

    return result

arr = [9, 3, 6, 1]

squared = square(arr)
print(squared)

timed10 = time10(arr)
print(timed10)


# In[22]:


print("Version 2 of the code :")


# In[23]:


# def square(num):
#     return num * num
#
# def time10(num):
#     return num * 10

def process(arr, process_func):
    result = []

    for num in arr:
        result.append(process_func(num))

    return result

arr = [9, 3, 6, 1]
squared = process(arr, lambda num: num ** 2)
print(squared)

timed10 = process(arr, lambda num: num * 10)
print(timed10)


# In[24]:


print("Version 3 of the code :")


# In[25]:


arr = [9, 3, 6, 1]
squared = list(map(lambda num: num ** 2, arr))
print(squared)

timed10 = list(map(lambda num: num * 10, arr))
print(timed10)


# In[ ]:





# In[ ]:





# In[26]:


print("Another example : 1 :")

# How map() works with multiple iterables:
# map(lambda a, b, c: a**3 + b**2 + c, cubes, squares, units)
# It takes one element at a time from each list, in parallel.

cubes = [5, 12, 4, 6]
squares = [11, 2, 6, 4]
units = [9, 8, 3, 5]

# result = [
#     5**3 + 11**2 + 9,
#     12**3 + 2**2 + 8,
#     ...
# ]

result = list(map(lambda a, b, c: a**3 + b**2 + c, cubes, squares, units))
print(result)


# In[ ]:





# In[27]:


print("Another example : 2 :")


# In[28]:


# It returns a new list, the i-th value in the new list
# is the sum of 0-th value to the i-th value in arr

# example:
# arr: [10, 3, 7, 6, 5, 2]
# prefix sum of arr: [10, 13, 20, 26, 31, 33]

def prefix_sum(arr):

    result = []

    prefix_sum_so_far = 0
    for num in arr:
        prefix_sum_so_far += num
        result.append(prefix_sum_so_far)

    return result

if __name__ == '__main__':
    arr = [10, 3, 7, 6, 5, 2]
    ps = prefix_sum(arr)
    print(arr) # [10, 3, 7, 6, 5, 2]
    print(ps) # [10, 13, 20, 26, 31, 33]


# In[29]:


# a contest has 4 levels: bronze, silver, gold and platinum
# before the contest, we have
# - 30 students in bronze
# - 19 in silver
# - 33 in gold
# - 26 in platinum
# in the contest,
# - new students can enter it at the bronze (basic) level
# - existing students can be promoted to the next level
# - except that the platinum students will keep their level
# after the contest, we have
# - 40 in bronze
# - 28 in silver
# - 8 in gold
# - 53 in platinum
# tell me that in the contest
# - number of students who enter the contest at the bronze level
# - number of students who are promoted from bronze to silver
# - number of students who are promoted from silver to gold
# - number of students who are promoted from gold to platinum

from prefix_sum import prefix_sum

before = [26, 33, 19, 30] # from platinum to bronze
after = [53, 8, 28, 40]

prefix_sum_before = prefix_sum(before)
prefix_sum_after = prefix_sum(after)

print(prefix_sum_before)
print(prefix_sum_after)

# promotion = []
# for index in range(len(prefix_sum_before)):
#     diff = prefix_sum_after[index] - prefix_sum_before[index]
#     promotion.append(diff)

promotion = list(map(lambda af, bf: af - bf, prefix_sum_after, prefix_sum_before))

print(promotion) # [27, 2, 11, 21]


# In[ ]:





# In[30]:


print("Another example : 3 :")


# In[31]:


# zgrades.txt

# Alice,100011,98,93,82,66
# Bob,123456,78,75,92,64
# Charles,129012,97,93,90,90
# David,123123,90,79,97,92


# In[32]:


# read the student info including the scores from grades.txt
# each line in z more zggrades.txt follows the same pattern as
# name,id,score1,score2,score3,score4
# for each student, calculate his/her average score
# print out each student's average score

# arr = '92,78,91,96'.split(',')
# list(map(int, arr))
# [92, 78, 91, 96]

import numpy as np

with open('zgrades.txt') as fin:
    for line in fin:
        line = line.strip()
        info = line.split(',')
        
        scores=[]
        for x in info[2:]:
            scores.append(int(x))
            
        # scores = list(map(int, info[2:])) # version 1 : Alice 84
        # scores = [int(x) for x in info[2:]] # version 2 : Alice : 84
        
        average = sum(scores) / len(scores)
        print('{}: {}'.format(info[0], average))


# In[ ]:





# In[33]:


print('''

Notes about range()

range(start, stop, step)
start → beginning (default is 0)
stop → end (not included!)
step → how much to increase each time (default is 1)

''')

# for i in range(1, 6):
#    print(i)

for i in range(5, 0, -1):
    print(i)

# for i in range(0, 10, 2):
#    print(i)


# In[34]:


print('''

Notes about enumerate() 

enumerate() is a built-in function that lets you loop over an iterable (like a list or tuple) and 
get both the index and the value at the same time.

enumerate(iterable, start=0)
iterable: any iterable (like a list, string, tuple, etc.)

start: the starting index (default is 0)

''')

fruits = ['apple', 'banana', 'cherry']

print("With Default Start Index:")

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("With Custom Start Index:")

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")


# In[ ]:





# In[35]:


print('''

Notes about zip() : 

zip() combines two or more iterables (like lists or tuples) element-wise into pairs or tuples.
Think of it as zipping up a jacket — it connects items side by side.

zip(iterable1, iterable2, ...)

It returns an iterator of tuples, where each tuple contains one element from each input iterable.
''')

names = ['Alice', 'Bob', 'Charlie']
grades = [85, 90, 78]

for name, grade in zip(names, grades):
    print(f"{name} got {grade}")


# Zip Stops at the Shortest Input

a = [1, 2, 3]
b = ['a', 'b']

print(list(zip(a, b)))
# Output: [(1, 'a'), (2, 'b')] → the third element of `a` is ignored


# In[36]:


print("How do we unzip ? Unzipping : You can 'unzip' with the * operator:")

pairs = [('Alice', 85), ('Bob', 90)]
names, grades = zip(*pairs)
print(names)   # ('Alice', 'Bob')
print(grades)  # (85, 90)

# When to Use zip() : Creating key-value pairs	dict(zip(keys, values))
# Combine two lists — one of keys, one of values — into a dictionary.

# List of keys (e.g., names)
keys = ['name', 'age', 'city']

# List of values
values = ['Alice', 30, 'New York']

# Create dictionary using zip()
person = dict(zip(keys, values))

print(person)


# In[37]:


print("Various : about computer science")


# In[38]:


print('''

Implement the Actor Model — very close in spirit to pi-calculus.


# Example with pykka
import pykka

class Greeter(pykka.ThreadingActor):
    def on_receive(self, message):
        return f"Hi {message['name']}"

actor_ref = Greeter.start()
response = actor_ref.ask({'name': 'Bogdan'})
print(response)  # Output: "Hi Bogdan"
actor_ref.stop()

''')


# In[39]:


print('''

The Actor Model is a powerful conceptual model for concurrent computation, especially useful in distributed systems and parallel programming.

🎭 Definition:
In the Actor Model, the basic unit of computation is an actor.

Each actor:

Is an independent "thing" (like a lightweight thread or agent)

Has a private state

Can only communicate with other actors via asynchronous message passing

Can:

Send messages to other actors

Create new actors

Change its own internal state

And that’s it.

🔄 Key Properties:

Property	Description
Isolation	Each actor manages its own state — no shared memory.
Asynchronous	Messages are sent and received non-blocking.
Decentralized	No global "manager" — actors can spawn and organize themselves.
Scalable & Parallel	Actors can run truly concurrently, making this model great for distributed systems.

''')





