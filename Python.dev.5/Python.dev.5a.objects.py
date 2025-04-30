#!/usr/bin/env python
# coding: utf-8

# In[11]:


print("Object Oriented Programming")


# In[ ]:





# In[ ]:


print("code version 1:")


# In[ ]:





# In[3]:


# calculate the distance between points on the 2D space
# data structure should we use to present each point ?

import math

def move(pt, x, y):
    pt['x'] += x
    pt['y'] += y

def distance(pt):
    return math.sqrt(pt['x'] ** 2 + pt['y'] ** 2)

pt = {'x': 3, 'y': 4}
print(pt)
move(pt, 1, 2)
print(pt)

d = distance(pt) # distance between pt and (0, 0)
print(d)


# In[ ]:


print("code version 2:")


# In[8]:


print("DYNAMICALLY add ATTRIBUTES")

print('''

Even though Point() is an empty class (i.e. it has no predefined attributes or methods), 
Python allows you to dynamically add attributes to instances of a class — 
as long as you're not using __slots__.

''')


# In[9]:


import math

class Point:   # an empty class
    pass

def move(pt, x, y):
    pt.x += x
    pt.y += y

def distance(pt):
    return math.sqrt(pt.x ** 2 + pt.y ** 2)

pt = Point()
pt.x = 3
pt.y = 4

print(pt.x, pt.y)
move(pt, 1, 2)
print(pt.x, pt.y)

d = distance(pt)
print(d)

# Python's default object model supports this because every object has a built-in dictionary (__dict__) 
# where its attributes are stored. You can see it:

print(pt.__dict__)  # Output: {'x': 3, 'y': 4}


# In[10]:


print('''

But is it good practice?

Usually no — it's better practice to define your attributes explicitly in an __init__ constructor 
so they're always present and predictable.

''')


# In[ ]:


print("code version 3:")


# In[12]:


import math

class Point:
    def move(pt, x, y):
        pt.x = x
        pt.y = y

    def distance(pt):
        return math.sqrt(pt.x ** 2 + pt.y ** 2)


pt = Point()
pt.x = 3
pt.y = 4

print(pt.x, pt.y)
Point.move(pt, 1, 2)
print(pt.x, pt.y)
d = Point.distance(pt)
print(d)


# In[ ]:


print("code version 4:")


# In[15]:


import math

class Point:
    def move(self, x, y):
        self.x += x
        self.y += y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


pt = Point()
pt.x = 3
pt.y = 4

print(pt.x, pt.y)
pt.move(1, 2)      # Point.move(pt, 1, 2)
print(pt.x, pt.y)

d = pt.distance()  # d = Point.distance(pt)
print(d)


# In[ ]:


print("code version 5:")


# In[22]:


# x and y are parameters passed into the method when you create a Point object. 
# so they are external to the object at the time of creation.

# We use self. to record (or store) external variables into the object’s internal state so that they persist 
# beyond the constructor and can be accessed or modified later by other methods or code.

# 🧠 Without self:
# If you just write:

def __init__(self, x, y):
    x = x
    y = y

# It does nothing meaningful. It just creates local variables x and y that disappear after __init__ finishes. 
# The object itself stores nothing.

# ✅ With self:

def __init__(self, x, y):
    self.x = x
    self.y = y

# This assigns the external values (x, y) to attributes of the object. Now you can later access them like:

# pt = Point(3, 4)
# print(pt.x)  # → 3
# print(pt.y)  # → 4

print('''

Think of SELF as: a reference to "this object"

self.x means: "x stored inside this object"

By saving values as self.x, you're giving the object MEMORY 

— a way to remember data passed to it when it was created.

''')


# In[23]:


import math



class Point:
    # automatically called when an object is created
    # initialize the newly created object
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # automatically called when calling str(obj)
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    # for an instance method, we have to use caller (self) as the first parameter
    def move(self, x, y):
        self.x += x
        self.y += y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

# create a new blank object
# obj.__init__(3, 4)
# Point.__init__(obj, 3, 4)

pt = Point(3, 4)
# pt.x = 3
# pt.y = 4

print(pt.x, pt.y)
print(str(pt)) # print(pt) -> str(pt) provides the string representation of pt

pt.move(1, 2)  # Point.move(pt, 1, 2)
print(pt.x, pt.y)

d = pt.distance()  # d = Point.distance(pt)
print(d)

# We don’t need to pass x and y into distance(self) because they’re already stored inside the object as self.x and self.y. 
# That's the whole point of using self. — to save values so they can be reused later without needing to pass them again.

print('''

If we write:

def distance(self, x, y):
    return math.sqrt(x ** 2 + y ** 2)

You would need to call it like this:

pt.distance(3, 4)

And then what's the point of storing self.x and self.y in the object?

So it defeats the purpose of object-oriented design, 

where data lives inside the object and methods use that internal data.

''')


# In[24]:


print('''

🎯 Summary:

Use self.x, self.y when the data already lives inside the object

Use extra parameters when the method needs additional input not stored inside the object

''')


# In[25]:


print('''

Method needs extra input

Now let’s say you want to compute the distance from this point to another point. 

That other point's coordinates aren’t stored inside the object, so you need to pass them as parameters:

''')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_x, other_y):
        dx = self.x - other_x
        dy = self.y - other_y
        return (dx ** 2 + dy ** 2) ** 0.5

pt = Point(3, 4)
print(pt.distance_to(0, 0))  # Distance to origin → 5.0
print(pt.distance_to(6, 8))  # Distance to another point


# In[27]:


print("Custom equality checking in Python :")


# In[28]:


print('''

__eq__ is a special method that defines what == means for two Point objects.

It checks that the other object is a Point, and then compares x and y values.

''')


# In[30]:


import math

class Point:
    # automatically called when an object is created
    # initialize the newly created object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # automatically called when calling str(obj)
    def __str__(self):
         return '({}, {})'.format(self.x, self.y)

    # if two Point objects have the same x and y values
    # they are equal
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

# by default == equality checking is
# to check if two variables refer to same object (identical)

# In this example, we overide the default behavior of ==.
# By default, == checks object identity (i.e., same memory address).
# With __eq__, we tell Python:
# “Two Points are equal if their x and y values are equal.”
# isinstance(other, Point) ensures we're only comparing Point objects, and not something else like a Car.

p = Point(3, 4)
q = Point(3, 4)
print('p', p)
print('q', q)
print(p == q) # Point.__eq__(p, q) => p.__eq__(q)

# If Point had no __eq__, p == q would be False even with the same values, because it would fall back to:
# p is q  # identity comparison

r = p
print('r', r)
print(p == r)

class Car:
    def __eq__(self, other):
        return True

c = Car()
c.x = 3
c.y = 4
print(p == c) # False — because Point.__eq__ sees c is not a Point
print(c == q) # True — because Car.__eq__ returns True no matter what
              # == start from c and if __eq__ is not provided, try q


# In[31]:


print('''

🧠 Summary:

__eq__ lets you define what “equality” means for your class.

Default == checks identity (like is).

Overriding __eq__ is Pythonic when comparing custom objects.

You can even override __str__, __lt__, etc., for more natural behavior.

''')


# In[34]:


print('''

__hash__ — for sets and dictionary keys

By default, objects are hashable by identity (i.e., memory address). 

But if you override __eq__, Python removes the default hashability unless you also define __hash__.

def __hash__(self):
    return hash((self.x, self.y))

This makes the hash based on content — so two points with the same x and y are considered the same in sets and dicts.

''')

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 3)

points = {p1, p2, p3}
print(len(points))  # ✅ 2, because p1 == p2 and hashes match


# In[ ]:




