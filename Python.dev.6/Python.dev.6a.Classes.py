#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# The double underscores in __str__ (and other similar names like __init__, __add__, etc.) are part of Python's special method 
# naming convention, sometimes called "dunder methods" (short for "double underscore").
# dunder str" → în română: "dublă subliniere str"


# In[11]:


print("__str__ : it defines how the object appears when printed:")


# In[17]:


class Note:
    def __init__(self, content, category):
        self.content = content
        self.category = category

    def __str__(self):
        # return '{} ({})'.format(self.content, self.category)
        return f'{self.content} ({self.category})'

if __name__ == '__main__':
    n1 = Note('Drink a lot of water', 'health')
    n2 = Note('Wash hands frequently', 'health')
    n3 = Note('Always say "Thank you"', 'social')
    print(n1)
    print(n2)
    print(n3)


# In[ ]:





# In[4]:


print("Class 1")


# In[3]:


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

    # if two Point objects have the same x and y values, they are equal
    # it overrides the equality operator ==.
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    # Enables the use of the + operator between two Point objects.
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    # Enables multiplying a Point by an integer: Point * int.
    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            return NotImplemented

    # Enables reverse multiplication: int * Point.
    def __rmul__(self, other):
        return self.__mul__(other)

    # Computes the Euclidean distance between two points:
    def distance(self, other):
        if isinstance(other, Point):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        else:
            return NotImplemented



if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(5, 7)

    p3 = p1 + p2  # p1.__add__(p2)
    print(p1)
    print(p2)
    print(p3)

    p4 = p3 * 5
    print(p4)

    p5 = 10 * p4
    print(p5)


# Python uses a special method __rmul__ ("right multiplication") when the left-hand side does not know how to handle the operation, 
# and the right-hand side might.

# Without defining __rmul__, this will fail:
# 10 * Point(1, 2)
# Even though:
# Point(1, 2) * 10
# would work fine.


# In[5]:


print("Class 2")


# In[7]:


import math

class Rational:
    def __init__(self, n, d):
        gcd = math.gcd(n, d)
        self.numerator = n // gcd
        self.denominator = d // gcd

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):                 # Defines addition of two rational numbers:
        if isinstance(other, Rational):
            return Rational(
                self.numerator * other.denominator + self.denominator * other.numerator,
                self.denominator * other.denominator
            )
        else:
            return NotImplemented

    def __mul__(self, other):                 # Defines multiplication of two rational numbers:
        if isinstance(other, Rational):
            return Rational(
                self.numerator * other.numerator,
                self.denominator * other.denominator
            )
        else:
            return NotImplemented


r1 = Rational(3, 4)
r2 = Rational(2, 5)
print(r1)  # 3/4
print(r2)  # 2/5

r3 = r1 + r2
print(r3)  # 23/20
r4 = r1 * r2
print(r4)  # 6/20 -> 3/10
r5 = r1 + r1
print(r5)

r6 = Rational(10, 20)
print(r6)


# In[ ]:


print("Class 3")


# In[9]:


import math

# a Circle object has a radius and a Point object as its center

class Circle:
    def __init__(self, x, y, r):
        self.center = Point(x, y)   # a Point object at coordinates (x, y)
        self.radius = r

    def __str__(self):
        return 'Circle at {} with radius {}'.format(self.center, self.radius)

    # return False if pt is not inside Circle or on its edge
    def cover(self, pt):
        return self.center.distance(pt) <= self.radius

# self.center.distance() : it is an instance of the Point class, 
# so self.center is a Point object, and Point is expected to define a method called distance().
# this method is part of the Point class and computes the Euclidean distance between two points.
# returns True if the distance between the circle's center and point pt is less than or equal to the circle's radius — 
# i.e., the point lies inside or on the edge of the circle.

if __name__ == '__main__':
    
    # Circle(x, y, r)
    c = Circle(3, 4, 2)
    print(c)  # Circle at (3, 4) with radius 2
    
    print(c.cover(Point(1, 6)))  # False
    print(c.cover(Point(4, 3)))  # True


# In[ ]:


print("Class 4")


# In[ ]:





# In[16]:


class Note:
    def __init__(self, content, category):
        self.content = content
        self.category = category

    def __str__(self):
        return '{} ({})'.format(self.content, self.category)
    

if __name__ == '__main__':
    n1 = Note('Drink a lot of water', 'health')
    n2 = Note('Wash hands frequently', 'health')
    n3 = Note('Always say "Thank you"', 'social')
    print(n1)
    print(n2)
    print(n3)


# In[18]:


import os
from os.path import exists

class Notebook:
    def __init__(self, title, filename):
        self.title = title
        self.notes = []           # Contains a list of Note objects (self.notes)
        self.filename = filename  # Stores/loads data from a text file (self.filename)
        self.load()               # self.load() to try loading notes from the file

    def load(self):
        if exists(self.filename):
            with open(self.filename, 'r') as fin:
                for index, line in enumerate(fin):
                    line = line.strip()
                    if index == 0:
                        self.title = line
                    else:
                        left = line.rindex('(')      # Extracts the content and category by finding the positions of the parentheses
                        right = line.rindex(')')     # Extracts the content and category by finding the positions of the parentheses
                        content = line[:left].strip()
                        category = line[left+1:right].strip()
                        self.add_note(content, category)   # Adds a new Note object

    def add_note(self, content, category):
        self.notes.append(Note(content, category))

    def save(self):
        with open(self.filename, 'w') as fout:
            fout.write(f'{self.title}\n')
            for note in self.notes:
                fout.write(f'{note}\n')

if __name__ == '__main__':
    
    nb = Notebook("John's notebook", 'john_notebook.txt')
    nb.add_note('Drink a lot of water', 'health')
    nb.add_note('Wash hands frequently', 'health')
    nb.add_note('Always say "Thank you"', 'social')

    nb.save()

# john_notebook.txt content
#
# John's notebook
# Drink a lot of water (health)
# Wash hands frequently (health)
# Always say "Thank you" (social)


# In[ ]:





# In[ ]:


print("Library Pickle:")

# What is pickle in Python?
# The pickle module is a built-in Python library that lets you save (serialize) Python objects to a file or string, 
# and later load (deserialize) them back into memory.

# Think of it like this:
# 🧠 You want to “remember” a Python object — like a list, dictionary, or even a trained ML model — and bring it back later. 
# pickle lets you do that.

# ✅ What it does:
# Serialization = converting a Python object into a byte stream
# Deserialization = converting that byte stream back into a Python object

# 🔧 Common Use Cases
# Saving the state of a program
# Saving trained models (e.g. from scikit-learn)
# Caching data (e.g. a preprocessed dataset)
# Inter-process communication


# In[ ]:





# In[19]:


import pickle

with open('test.dat', 'wb') as fout:
    pickle.dump([1, 2, 3], fout)
    pickle.dump({1: 'hello', 2: 'bye'}, fout)
    pickle.dump(100, fout)
    pickle.dump(Point(2, 3), fout)

with open('test.dat', 'rb') as fin:
    
    # l = pickle.load(fin)
    # d = pickle.load(fin)
    # n = pickle.load(fin)
    # print(l)
    # print(d)
    # print(n)
    # p = pickle.load(fin)
    # print(p)

    while True:
        try:
            curr = pickle.load(fin)
            print(curr)
        except EOFError:
            break


# In[ ]:





# In[ ]:


print("Re-writing the code by using the library pickle")


# In[26]:


from os.path import exists
import pickle

class Notebook:
    def __init__(self, title, filename):
        self.title = title
        self.notes = []
        self.filename = filename
        self.load()

    # load the notebook content from the file by the filename
    # update the title and populate self.notes

    def load(self):
        if exists(self.filename):
            with open(self.filename, 'rb') as fin:
                self.title = pickle.load(fin)
                self.notes = pickle.load(fin)

    def add_note(self, content, category):
        self.notes.append(Note(content, category))

    def save(self):
        with open(self.filename, 'wb') as fout:
            pickle.dump(self.title, fout)
            pickle.dump(self.notes, fout)

    def __str__(self):
        result = '{}\n'.format(self.title)
        for index, note in enumerate(self.notes, start=1):
            result += '{}. {}\n'.format(index, note)             # A numbered list of all notes
        return result


if __name__ == '__main__':
    nb = Notebook("John's notebook", 'john_notebook.dat')
    nb.add_note('Drink a lot of water', 'health')
    nb.add_note('Wash hands frequently', 'health')
    nb.add_note('Always say "Thank you"', 'social')

    nb.save()
    print(nb)


text = str(nb)
print(text)

print(nb.__str__())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




