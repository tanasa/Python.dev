#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Tuples")


# In[2]:


print('''

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Like Lists, tuples are ordered and we can access their elements using their index values

We cannot update items to a tuple once it is created. 

Tuples cannot be appended or extended.

We cannot remove items from a tuple once it is created. 

''')


# In[3]:


thistuple = ("apple", "banana", "cherry")
print(thistuple)


# In[4]:


# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# In[5]:


# Tuple items can be of any data type:
# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")


# In[6]:


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# In[7]:


t = (1, 2, 3, 4, 5)

# Tuples are indexed
print(t[1])
print(t[4])

# Tuples contain duplicate elements
t = (1, 2, 3, 4, 2, 3)
print(t)

# updating an element
# t[1] = 100
# print(t)
# 'tuple' object does not support item assignment

# Accessing Values in Python Tuples

t = (10, 5, 20)

print("Value in t[0] = ", t[0])
print("Value in t[1] = ", t[1])

print("Value in t[-1] = ", t[-1])
print("Value in t[-2] = ", t[-2])


# In[8]:


# Concatenation of 2 Python tuples
t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')

print(t1 + t2)

# Nesting of Python Tuples
# A nested tuple in Python means a tuple inside another tuple.

t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')

t3 = (t1, t2)
print(t3)

# Slicing Tuples in Python

t = (0 ,1, 2, 3)
print(t[1:])
print(t[::-1])
print(t[2:4])


# In[9]:


# Deleting a Tuple in Python
# To remove individual tuple elements is not possible, but we can delete the whole Tuple using Del keyword.

# Code for deleting a tuple
t = ( 0, 1)

del t
# print(t) #  name 't' is not defined


# In[10]:


# Creating a tuple without brackets

t = 4, 5, 6
print(t)  # Output: (4, 5, 6)


# In[11]:


# Tuple packing

a, b, c = 11, 12, 13
t = (a, b, c)
print(t)  # Output: (11, 12, 13)


# In[12]:


# Tuple Iteration

numbers = (2, 9, 6)

for item in t:
    print(item)

tuple(int(number) for number in numbers)


# In[13]:


# Swapping Values

x, y = 5, 10
x, y = y, x
print(x, y)  # Output: 10 5


# In[14]:


tuple(x**2 for x in range(10))
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)


# In[15]:


print('''

Tuple Methods
.count(x) – Returns the number of times x appears in the tuple.
.index(x) – Returns the index of the first occurrence of x.

''')

t = (1, 2, 3, 2, 2)
print(t.count(2))  # Output: 3
print(t.index(3))  # Output: 2


# In[16]:


# Slicing operator : [start:stop:step] 


# In[17]:


days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

days[:5]
('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

days[5:]
('Saturday', 'Sunday')


# In[18]:


print("Hello, %s! You're %s years old." % ("Linda", 24))

# print("Hello, %s! You're %s years old." % "Linda", 24)

# In the first example, you use a tuple wrapped in parentheses as the right-hand operand to the % operator. 
# In this case, the interpolation works as expected. 
# In the second example, you don’t wrap the tuple in parentheses, and you get an error.


# In[ ]:





# In[19]:


# https://realpython.com/python-tuple/


# In[ ]:





# In[20]:


tuple({
    "manufacturer": "Boeing",
    "model": "747",
    "passengers": 416,
}.values())

tuple({
    "manufacturer": "Boeing",
    "model": "747",
    "passengers": 416,
}.keys())

tuple({
    "manufacturer": "Boeing",
    "model": "747",
    "passengers": 416,
}.items())


# In[ ]:





# In[21]:


print('''

Tuples can store any type of object, including mutable ones. 
This means that you can store lists, sets, dictionaries, and other mutable objects in a tuple

''')

student_info = ("Linda", 18, ["Math", "Physics", "History"])
print(student_info)
print(student_info[0])
print(student_info[2])
print(student_info[2][0])
print(student_info[2][2])

# The first two items are immutable. The third item is a list of subjects. 
# Python’s lists are mutable, and therefore, you can change their items in place. 

student_info[2][2] = "Computer science"
print(student_info)


# In[22]:


# We can change the content of mutable objects even if they’re nested in a tuple. 
# This behavior of tuples may have further implications. 
# For example, because tuples are immutable, you can use them as keys in a dictionary:

# Initialize student_courses dictionary
student_courses = {
    ("John", "Doe"): ["Physics", "Chemistry"],
    ("Jane", "Doe"): ["English", "History"]
}

# Accessing data
print("John Doe's courses:", student_courses[("John", "Doe")])
print("Jane Doe's courses:", student_courses[("Jane", "Doe")])

# Adding a new student
student_courses[("Alice", "Smith")] = ["Math", "Biology"]
print("Alice Smith's courses:", student_courses[("Alice", "Smith")])

# Adding a course for an existing student
student_courses[("John", "Doe")].append("Mathematics")
print("John Doe's updated courses:", student_courses[("John", "Doe")])

# Checking if a student exists
if ("John", "Doe") in student_courses:
    print("John Doe is enrolled.")

if ("Bob", "Brown") not in student_courses:
    print("Bob Brown is not enrolled.")

# Output the final dictionary
print("\nFinal student_courses dictionary:")
for student, courses in student_courses.items():
    print(f"{student[0]} {student[1]}: {', '.join(courses)}")


# In[23]:


# Python also has a packing and unpacking operator (*) that you can use to make your unpacking statements more flexible. 
# For example, you can use this operator to collect multiple values in a single variable when the number of variables on the left 
# doesn’t match the number of items in the tuple on the right.


# In[24]:


numbers = (1, 2, 3, 4, 5)

*head, last = numbers
print(head)
print(last)

first, *middle, last = numbers
print(first)
print(middle)
print(last)


# In[25]:


# Reversing a Tuple With reversed()
# Reversing a Tuple With the Slicing Operator : eg days[::-1]
# Sorting a Tuple With sorted()


# In[26]:


# Using a for Loop to Iterate Over a Tuple
# To illustrate how to iterate over a tuple using a Python for loop, say that you have a tuple of tuples. 
# Each nested tuple contains a month of the year and the income of a company during that month. 
# Now say that you want to know the year’s income

monthly_incomes = (
     ("January", 5000),
     ("February", 5500),
     ("March", 6000),
     ("April", 5800),
     ("May", 6200),
     ("June", 7000),
     ("July", 7500),
     ("August", 7300),
     ("September", 6800),
     ("October", 6500),
     ("November", 6000),
     ("December", 5500)
)

total_income = 0
for income in monthly_incomes:
    # print(income)
    # print(income[0])
    # print(income[1])
    total_income += income[1]

total_income


# In[ ]:





# In[27]:


print('''

Tuples With Named Fields: collections.namedtuple

A named tuple is a tuple subclass that incorporates named fields into its public interface. 
These named fields allow you to access the items in the underlying tuple using dot notation and the appropriate field name, 
which is more readable and explicit than using an index.

''')

from collections import namedtuple

Person = namedtuple("Person", "name age position")

# You create the Person class by calling the function with two arguments. 
# The first argument is the class name, while the second argument is a string that provides the field names separated by whitespaces. 
# In this specific example, your tuple-like class will have three fields: name, age, and position.

person = Person("John", 35, "Python Developer")
print(person.name)
print(person.age)
print(person.position)
print(person[0])


# In[28]:


# Database records are a good example of a typical use case of tuples. 
# In this scenario, a tuple will provide a good representation of records or rows, 
# where you have many fields containing heterogeneous values that shouldn’t change frequently.


# In[ ]:





# In[ ]:




