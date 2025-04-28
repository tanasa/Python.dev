#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Abstract Base Classes :")
# abc stands for "Abstract Base Classes" — it allows you to define abstract classes and abstract methods that must be overridden by subclasses


# In[2]:


from abc import ABC, abstractmethod
import random

# Ticket is an abstract base class (ABC) — it cannot be instantiated directly.
# Purpose: provide a template for different types of tickets (show ticket, movie ticket, etc.).
# When any Ticket is created (through a subclass), it gets a random 4-digit number.

class Ticket(ABC):
    def __init__(self):
        # randomly generated as a 4-digit number
        self.number = random.randint(1000, 9999)

    @abstractmethod
    def get_price(self):
        return NotImplemented

    def __str__(self):
        # dynamic binding
        return '{}: ${}'.format(self.number, self.get_price())

# get_price() is an abstract method.
# Any subclass of Ticket must implement get_price().

class ShowTicket(Ticket):
    def __init__(self):
        super().__init__()  # manually call the parent __init__
    
    def get_price(self):
        return 50

# If a movie ticket is purchased 10 days or more before the movie date
# the ticket price is $30. Otherwise, the ticket price is $40.

class MovieTicket(Ticket):
    def __init__(self, days):
        super().__init__()
        self.days_in_advance = days

    def get_price(self):
        return 30 if self.days_in_advance >= 10 else 40

# student's movie ticket is always half-price of the movie ticket.
# the string representation of the student's movie ticket
# should include (Student ID required) at the end

class StudentMovieTicket(MovieTicket):
    def get_price(self):
        return super().get_price() // 2

    def __str__(self):
        return '{} (Student ID required)'.format(super().__str__())

# super() goes to the parent class, which for StudentMovieTicket is MovieTicket.
# super().get_price() calls the get_price() method from MovieTicket, 
# NOT the StudentMovieTicket's own method (because you're in it right now).

# super().__str__() calls the parent's (MovieTicket → Ticket) __str__() method.
# Ticket.__str__() creates a string like:
# 1234: $30 or 5678: $40
# Then, StudentMovieTicket adds extra text to it: "(Student ID required)".
    
if __name__ == '__main__':
    
    t = ShowTicket()
    print(t)
    t2 = ShowTicket()
    print(t2)

    mt = MovieTicket(12)
    print(mt) # 1234: $30
    mt2 = MovieTicket(3)
    print(mt2)  # 1235: $40

    st = StudentMovieTicket(15)
    print(st)  # 2222: $15 (Student ID required)
    st2 = StudentMovieTicket(1)
    print(st2)  # 3333: $20 (Student ID required)


# In[ ]:





# In[3]:


from abc import ABC, abstractmethod
import random

# Instead of random numbers, tickets now have a sequential ticket number starting from 1.
# next_ticket_number is a class variable

class Ticket(ABC):
    next_ticket_number = 1

    def __init__(self):
        # make the ticket number to be generated
        # in a sequential order
        self.number = Ticket.next_ticket_number
        Ticket.next_ticket_number += 1

    @abstractmethod
    def get_price(self):
        return NotImplemented

    def __str__(self):
        # dynamic binding
        return '{}: ${}'.format(self.number, self.get_price()) # It dynamically calls the right get_price() based on subclass.


class ShowTicket(Ticket):
    def get_price(self):
        return 50

# If a movie ticket is purchased 10 days or more before the movie date
# the ticket price is $30. Otherwise, the ticket price is $40.

# Three class variables:
# minimum_day_in_advance = how many days early to get the discount (default 10 days).
# EARLY_BIRD_PRICE = $30
# FULL_PRICE = $40

class MovieTicket(Ticket):
    minimum_day_in_advance = 10
    EARLY_BIRD_PRICE = 30
    FULL_PRICE = 40

    def __init__(self, days):
        super().__init__()
        self.days_in_advance = days

    def get_price(self):
        return MovieTicket.EARLY_BIRD_PRICE \
            if self.days_in_advance >= MovieTicket.minimum_day_in_advance \
            else MovieTicket.FULL_PRICE

    @staticmethod
    def update_policy(new_days):
        MovieTicket.minimum_day_in_advance = new_days

# Static method (no self).
# Allows changing the advance days policy for all MovieTicket instances!

# student's movie ticket is always half-price of the movie ticket.
# The string representation of the student's movie ticket
# should include (Student ID required) at the end

class StudentMovieTicket(MovieTicket):
    def get_price(self):
        return super().get_price() // 2

    def __str__(self):
        return '{} (Student ID required)'.format(super().__str__())


if __name__ == '__main__':
    t = ShowTicket()
    print(t)
    t2 = ShowTicket()
    print(t2)

    mt = MovieTicket(12)
    print(mt) # 1234: $30
    mt2 = MovieTicket(3)
    print(mt2)  # 1235: $40

    st = StudentMovieTicket(15)
    print(st)  # 2222: $15 (Student ID required)
    st2 = StudentMovieTicket(1)
    print(st2)  # 3333: $20 (Student ID required)

    MovieTicket.update_policy(5)
    mt3 = MovieTicket(8)
    print(mt3)


# In[ ]:





# In[4]:


print('''

What is a Static Method?

A static method is a method inside a class that does not operate on a specific object (instance) or on the class itself.
It behaves like a regular function, but lives inside the class for logical grouping.

👉 Key:

It does NOT access self (the instance).

It does NOT access cls (the class).

It is called from the class or an instance, but doesn't care who calls it.

How to define a static method?

You define it with the @staticmethod decorator:

class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x + y
''')


# In[5]:


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# You can call static methods like this:

print(Calculator.add(3, 5))       # Output: 8
print(Calculator.multiply(4, 7))  # Output: 28

# Or from an instance:

c = Calculator()
print(c.add(10, 2))   # Also works, but still not using `self`


# In[6]:


# 🧩 Example where static methods make sense:
# Suppose you are writing a MovieTicket class.
# You want a simple function that just validates the number of days entered.

class MovieTicket:
    @staticmethod
    def validate_days(days):
        if days < 0:
            raise ValueError("Days cannot be negative.")


# ✅ This validation has nothing to do with a particular movie ticket object.
# ✅ It's a logical utility inside the MovieTicket world.
# ✅ So it's best to put it inside the class as a static method.

# Another Real Example: (from our code)

@staticmethod
def update_policy(new_days):
    MovieTicket.minimum_day_in_advance = new_days

# You don't need a particular ticket to change the company policy.
# This operation is global for MovieTicket, so static method is fine (but in some designs, class methods would also work here).


# In[ ]:





# In[7]:


# What happens if we do not include @staticmethod when defining a method like update_policy?
# Suppose you REMOVE @staticmethod, and you have this code:

class MovieTicket(Ticket):
    minimum_day_in_advance = 10

    def update_policy(new_days):
        MovieTicket.minimum_day_in_advance = new_days

# Looks okay, right? But now...
# If you try to call it like this:

MovieTicket.update_policy(5)

# 👉 Python throws an error:
# TypeError: update_policy() missing 1 required positional argument: 'new_days'

# Why?
# When you call MovieTicket.update_policy(5), Python automatically tries to pass the class itself as the first argument.
# BUT update_policy(new_days) expects only 1 argument, not 2.
# → Mismatch between what Python passes and what your function expects.

# Why does this happen?
# In a class:
# If a method does not have @staticmethod or @classmethod, Python treats it like a regular instance method.
# Regular methods expect the first argument to be self (an instance).
# Static methods tell Python:
# "Hey! Don’t pass self or cls. Just call me like a normal function."
# Without @staticmethod, Python tries to sneak an extra argument and everything crashes.

# How to fix if you forget @staticmethod?
# Add @staticmethod (✅ clean and correct)
# OR change the method to accept an extra (useless) self argument:

def update_policy(self, new_days):
    MovieTicket.minimum_day_in_advance = new_days

# BUT then you have to call it on an instance, not the class :

# mt = MovieTicket(5)
# mt.update_policy(8)  # Works now

print('''

🚀 Very short:

Situation	What Happens

No @staticmethod	Python expects self automatically. If you call on class, it crashes.

With @staticmethod	Python does not pass self. Works normally like a function inside the class.

🎯 Final advice:

✅ If your method does not use self (the object) or cls (the class itself), 
and is just a helper function → always use @staticmethod.

''')


# In[8]:


print('''

Quick Comparison Table:

Regular Method	Static Method	Class Method
First argument is self	No automatic first argument	First argument is cls
Works with instance data	No access to instance or class	Works with class data
def method(self,...)	@staticmethod + def method(...)	@classmethod + def method(cls,...)

Most common	Used for grouping related logic	Used when you want to create/modify class itself.

''')


# In[ ]:





# In[9]:


print("Class methods :")


# In[10]:


print('''

What is a class method in Python?

A class method is a method that is bound to the class, not the instance of the class.
It can modify the class state that applies across all instances of the class.

You define a class method using the @classmethod decorator.

It always receives the class itself (cls) as the first argument, not self (which is the instance).

''')

class Dog:
    number_of_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.number_of_dogs += 1

    @classmethod
    def get_number_of_dogs(cls):
        return cls.number_of_dogs

# Example usage:
dog1 = Dog('Rex')
dog2 = Dog('Buddy')

print(Dog.get_number_of_dogs())   # Output: 2


# In[11]:


print('''

Key points to remember about class methods:

Feature	Description

Decorator	@classmethod

First parameter	Always cls, referring to the class

Purpose	Access or modify class state that is shared across all instances

Call	Can be called from the class (Dog.get_number_of_dogs()) or from an instance (dog1.get_number_of_dogs())

''')


# In[12]:


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    @classmethod
    def from_string(cls, book_string):
        title, pages = book_string.split('-')
        return cls(title, int(pages))

# Create a Book instance using a string
book = Book.from_string('Harry Potter-500')
print(book.title)  # Output: Harry Potter
print(book.pages)  # Output: 500


# In[13]:


# Book.from_string('Harry Potter-500')
# is equivalent to:
# Book('Harry Potter', 500)
# but much cleaner if you are parsing data from a string!


# In[14]:


# Why is This Useful?
# When you get data in a different format (e.g., a string from a file, a database, or user input), you often need special constructors.
# @classmethod lets you create alternative ways to make objects, not just using __init__ directly.

