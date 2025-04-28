#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print('''

Abstract Methods and Dynamic Binding

An abstract method is a method without implementation.

It is declared in an abstract base class (ABC) and marked with @abstractmethod.

A subclass must inherit and implement that method.

from abc import ABC, abstractmethod

Why do we need it? 
→ To force subclasses to provide specific behavior, ensuring a consistent API across different types.

Can an abstract method be called inside the class?
→ No, unless it is implemented. Trying to instantiate an abstract class directly raises an error.

''')


# In[2]:


print('''

Dynamic Binding:

When you call a method on an object, Python figures out at runtime which method to call based on the object's actual type.

Example: In ticket_02.py, classes override __str__() and get_price(), and Python uses the right version automatically.

''')


# In[3]:


print('''

Class Variables and Static Methods

Class Variables are shared among all instances.

Static Methods:

Marked with @staticmethod, they:

Do not receive self or cls.
Can still access and modify class variables (by using the class name explicitly).

Difference from @classmethod:

@classmethod gets cls as the first parameter and is used to modify the class itself.

@staticmethod is just a function grouped inside a class.

''')


# In[4]:


print('''

Access Control (Encapsulation)

Python has no built-in true access control like Java or C++.

But there are conventions:

_protected_variable → Hint: treat it as protected.

__private_variable → Name mangling: becomes _ClassName__private_variable.

print(obj._ClassName__private_variable)  # Still accessible!

Important:

It is only naming convention, not true protection.

In Java:

Use getter and setter methods to control access.

Allows validation inside the setter (important for safe encapsulation).

''')


# In[5]:


print('''

Managing Instance Variables

In Python, use the property() function:

fget → getter

fset → setter

fdel → deleter

✅ Provides indirect controlled access to attributes.

✅ But attributes are still technically public — it’s just a convention.

''')


# In[6]:


print('''

5. Multiple Inheritance

Python allows multiple inheritance (inherit from multiple classes).

Problem: methods from different classes might have the same name.

Solution: Python uses the Method Resolution Order (__mro__) to decide the correct method to call.

''')


# In[7]:


print('''

Keyword Arguments (*args and **kwargs)

*args: captures positional arguments into a tuple.

**kwargs: captures keyword arguments into a dictionary.

Example:

def func(*args, **kwargs):
    print(args)    # tuple
    print(kwargs)  # dictionary

''')    


# In[8]:


print('''

Exception Handling

Use raise ValueError to throw exceptions.
Use try ... except to catch and handle exceptions.

You can create your own exceptions by subclassing Exception.

class MyError(Exception):
    pass

''')


# In[9]:


print('''

Iterators and Generators

A for loop uses iter().

You can build custom iterators with __iter__() and __next__() methods.

for i in NumberStep(start, end, step):
    print(i)

Different from looping over a static list — dynamic sequence generation!

✅ You can even create infinite iterators (e.g., generating mathematical sequences to approximate π).

''')


# In[ ]:





# In[10]:


print('''

Generators and Yield

Generators simplify iterator writing by using the yield statement.

Instead of calculating all results at once, they generate values one-by-one.

def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

You can chain generators: one generator feeds another.

Comparison: | | Recursion | Generator | |:---|:---| | Narrowing down to base case | Can generate infinitely | | Solves finite problems | Creates continuous streams |

✅ Example of chain: Sieve of Eratosthenes for finding prime numbers.
''')


# In[11]:


print('''

Coroutines

Coroutines receive values with g.send() instead of just next(g).

Coroutines are like smart generators — they can be "pushed" values.

Methods:

g.send(value) — sends a value to the generator.

g.close() — terminates the generator.

If no generators:
✅ You would use classes with instance variables instead.

''')


# In[ ]:





# In[12]:


print('''

Context Managers

Context managers handle resource management (setup and teardown).

Example: with open('file.txt') as f:

Opens a file.

Automatically closes the file when exiting the with block.

✅ Great for clean and safe resource management.

''')


# In[13]:


print('''

Descriptors

Descriptors are classes that manage access to another attribute.

They implement methods like __get__(), __set__(), __delete__().

✅ Descriptors allow you to build your own property-like behavior manually. 
✅ Very useful for data validation and separation of responsibilities.

''')


# In[14]:


print('''

Decorators

Decorators allow you to modify a function without changing its code.

They are different from classic OOP inheritance.

✅ Decorators are very powerful because:

You can wrap functions easily.

You can add functionality (like logging, timing, tracing) without touching the original logic.

''')


# In[15]:


def my_decorator(func):
    def wrapper():
        print('Before function call')
        func()
        print('After function call')
    return wrapper

@my_decorator
def say_hello():
    print('Hello!')

# Call the decorated function
say_hello()


# In[ ]:





# In[16]:


print('''

What happens when you run this?

say_hello() is no longer the original function.

It is now the wrapper() function returned by my_decorator.

So when you call say_hello(), it actually calls wrapper(), which:

Prints "Before function call"

Calls the original say_hello() (prints "Hello!")

Prints "After function call"

''')


# In[17]:


print(''' Bonus Tip:

If you want the decorator to also work for functions that accept arguments, you should modify the wrapper() to accept *args and **kwargs:

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before function call')
        func(*args, **kwargs)
        print('After function call')
    return wrapper
✅ Now your decorator will work with any function: whether it takes arguments or not!

✅ Now, wrapper accepts:

*args → any number of positional arguments

**kwargs → any number of keyword arguments

✅ It passes them safely to func(*args, **kwargs).

''')

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before function call')
        func(*args, **kwargs)
        print('After function call')
    return wrapper

@my_decorator
def say_hello(name):
    print(f'Hello, {name}!')

say_hello('Alice')
say_hello('Bob')


# In[18]:


print('''
    
Bonus Professional Tip:

If you want to preserve the original function's name and docstring (important in real projects), 
you should also use functools.wraps(func) inside the decorator:

''')

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Before function call')
        func(*args, **kwargs)
        print('After function call')
    return wrapper

@my_decorator
def say_hello(name):
    print(f'Hello, {name}!')

say_hello('Alice')
say_hello('Bob')


# In[ ]:





# In[19]:


print("Decorator Factory:")


# In[20]:


print('''

What is a Decorator Factory?

A decorator factory is: a function that RETURNS a decorator.

It accepts arguments that customize how the decorator behaves.

✅ Normal decorator:

@decorator
def my_function():
    pass
✅ Decorator factory:

@decorator(argument)
def my_function():
    pass

Here, decorator(argument) returns the real decorator, which wraps my_function.

''')

print('''

🚀 Summary of Decorator Factory:

Concept	Meaning
Normal Decorator	Takes a function and returns a wrapper
Decorator Factory	Takes arguments, then returns a decorator
Useful for	Parameterizing decorators (example: repeat times, add delays, authorization levels, etc.)

''')


# In[21]:


print('''

Full Example: Decorator Factory that prints a message before and after calling the function

def decorator_factory(before_message, after_message):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            print(before_message)
            result = func(*args, **kwargs)  # Call the original function
            print(after_message)
            return result
        return wrapper
    return real_decorator
✅ decorator_factory(before_message, after_message):

Takes two arguments: what to print before and after the function call.

Returns the real decorator.

✅ The real decorator:

Takes the function func.

Returns a wrapper that:

Prints the before_message.

Calls the function.

Prints the after_message

''')


# In[22]:


def decorator_factory(before_message, after_message):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            print(before_message)
            result = func(*args, **kwargs)  # Call the original function
            print(after_message)
            return result
        return wrapper
    return real_decorator
    
@decorator_factory('Starting the function...', 'Function finished!')
def say_hello(name):
    print(f"Hello, {name}!")

say_hello('Alice')


# In[ ]:




