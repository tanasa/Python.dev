#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print('''

What is a Decorator?

A decorator is a function that takes another function or class as input, wraps it, and returns a modified version of it — usually adding extra behavior.

✅ You “decorate” a function by adding @decorator_name above it.

@decorator
def original_function():
    pass

Is equivalent to:

def original_function():
    pass

original_function = decorator(original_function)

''')

def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper   # The decorator returns wrapper, so: say_hello = wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# So when you do: say_hello()
# You're actually calling wrapper() — not func() directly.
# But inside wrapper(), it calls func(), which is the original say_hello().

print('''

Relationship Summary:

Name	What it does
func()	The original function (e.g. say_hello)
wrapper()	The new wrapped function returned by the decorator
say_hello()	Now points to wrapper() (due to the decorator)

''')


# In[2]:


print('''

Updated version with *args, **kwargs:

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)  # pass the arguments through
        print("After the function")
        return result
    return wrapper

🧠 Why use *args and **kwargs?

Symbol	Meaning

*args	Positional arguments as a tuple

**kwargs	Keyword arguments as a dictionary

This makes your decorator flexible and reusable — 
you don’t have to know how many arguments the wrapped function expects.

''')

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

# Example 1: No-argument function (still works)

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#🔹 Example 2: Function with arguments

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# In[ ]:





# In[3]:


def bar(func):
    print('bar')
    return func

# same as foo = bar(foo)
@bar
def foo():
    print('foo')

# foo = bar(foo)
foo() 
# same as bar(foo)()
bar(foo)()

# Python defines foo() → then sees @bar → replaces foo = bar(foo)
# bar() runs:
# Prints 'bar'
# Returns the unmodified foo
# You later call foo() → 'foo' is printed


print('''

Key Concept

The decorator runs at definition time, not when you call foo().

That’s why 'bar' prints first — even before you invoke foo().

''')

print('''

What is definition time in Python?

Definition time is the moment when Python executes the lines that define your functions, classes, or decorators — 
that is, when your code is first loaded or run, not when the function is actually called.

''')

print('''

Python reads @bar and does this:

foo = bar(foo)
→ So bar() is called immediately — that's definition time.

But foo() is only run later, when you actually call it — that's call time.

''')

print('''

📌 Decorators always run at definition time

This is why decorators are often used to:

Log when a function is defined

Register functions in a framework (like Flask or Django)

Modify behavior before a function is ever called

''')


# In[4]:


bar(foo)()


# In[5]:


print("Trace Decorators :")


# In[6]:


import time

def trace(func):
    def call_func(*args):
        print('log --- call {} at {}'.format(func.__name__, time.strftime('%H:%M:%S')))
        print('log --- call {} with {}'.format(func.__name__, args))
        result = func(*args)
        print('log --- {} returns {}'.format(func.__name__, result))
        return result

    return call_func

@trace
def square(x):
    return x ** 2

@trace
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c


# print("call 1")
# print(square(5))

# print("call 2")
# trace(square)(5)

# print("call 3")
# foo = trace(square)
# print(foo(5))

print(square(5))
print(square(10))
print(quadratic(5, 1, 2, 3))


# In[7]:


print(' A parameterized decorator used for logging function calls to a file. ')


# In[8]:


# Defines a decorator factory trace(filename)
# That produces a decorator file_trace(func)
# That wraps any function to:
# Log its name
# Log its arguments
# Log the result
# Save all of that into a file

# trace(filename) returns a decorator.
# filename is passed in when using @trace('trace.log')
# file_trace(func) will be the actual decorator applied to square or quadratic

# call_func() wraps the original function.
# *args allows any number of positional arguments.

# Logs the function name and call time
# Logs the arguments passed to the function

import time

def trace(filename):
    def file_trace(func):
        def call_funct(*args):
            with open(filename, 'a+') as fout:
                fout.write('log --- call {} at {}\n'.format(func.__name__, time.strftime('%H:%M:%S')))
                fout.write('log --- call {} with {}\n'.format(func.__name__, args))
                result = func(*args)
                fout.write('log --- {} returns {}\n'.format(func.__name__, result))
                return result

        return call_funct
    return file_trace

@trace('trace.log')
def square(x):
    return x ** 2

@trace('trace.log')
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# trace('trace.log')(square)(10)
print(square(10))
print(square(5))
# equivalent with :
square = trace('trace.log')(square)

print(quadratic(5, 1, 2, 3))


# In[ ]:





# In[9]:


print('''

a Class that uses a special method called __call__ to make an instance behave like a Function.

''')


# In[ ]:





# In[10]:


class Adder:
    def __init__(self, base):
        self._base = base        # adder5 = Adder(5) sets self._base = 5

    def __call__(self, value):   # the magic: __call__ lets you use the instance like a function
        self._base += value
        return self._base

adder5 = Adder(5)
print(adder5(10))   # So adder5(10) is the same as adder5.__call__(10)
print(adder5(3))    # So adder5(10) is the same as adder5.__call__(3)

# Adds value to the stored _base
# Returns the updated total

# First call: 5 + 10 = 15
# Second call: 15 + 3 = 18

# Why use __call__?
# It makes objects:
# Behave like functions
# Carry internal state (like memory)
# Useful in functional-style OOP, decorators, machine learning layers (e.g., PyTorch)

# ✅ Summary
# Feature	Description
# __call__	Lets an object be used like a function
# self._base	Keeps internal state
# adder5(10)	Updates and returns _base += 10
# Result	15, then 18


# In[ ]:





# In[ ]:





# In[11]:


import time

class Trace:
    def __init__(self, filename):
        self._filename = filename

    def __call__(self, func):   # __call__ as a Decorator ; Makes Trace instances act like decorators.
        def call_funct(*args):
            with open(self._filename, 'a+') as fout:
                fout.write('log --- call {} at {}\n'.format(func.__name__, time.strftime('%H:%M:%S')))
                fout.write('log --- call {} with {}\n'.format(func.__name__, args))
                result = func(*args)
                fout.write('log --- {} returns {}\n'.format(func.__name__, result))
                return result

        return call_funct

@Trace('trace.log')    # equivalent to square = Trace('trace.log')(square)
def square(x):
    return x ** 2

@Trace('trace.log')    # equivalent to square = Trace('trace.log')(quadratic)
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# trace('trace.log')(square)(10)
print(square(10))
print(quadratic(5, 1, 2, 3))
print(square(5))


# It wraps a function func and returns call_func, which:
# Logs the function name and call time.
# Logs the function arguments.
# Calls the original function.
# Logs the return value.
# Returns the results.
# This pattern is great for debugging, auditing, or profiling code behavior.


# In[ ]:





# In[12]:


print("Memorization decorator : applied to Fibonacci")
# This code defines a memoized version of the recursive Fibonacci function using a decorator. 
# Purpose:
# To optimize recursive function calls by caching results of previous function calls so that redundant calculations are avoided.


# In[13]:


def memorized(func):
    cache = {}               # cache is a dictionary used to store previously computed results.

    def call_func(*args):    # call_func is the inner wrapper function.
        v = cache.get(args)  # it checks if the arguments args have been seen before by looking them up in the cache.
        if v is not None:    # cache[args] if args in cache else None
           return v          #  we return the cached result (i.e. v) to avoid recomputation.

        r = func(*args)      # If the result isn't cached, it computes the result r by calling the original function.
        cache[args] = r      # Save r in the cache for future use, and returns this freshly computed result
        return r

    return call_func

# v: comes from the cache.
# r: comes from the actual function call.

@memorized
def fibonacci(n):
    if n in (1, 2):
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(200))


# In[ ]:





# In[14]:


# The code above is equivalent to :
# Replaced v and r with a single variable result to capture either cached or newly computed output.
# This version is more concise and behaves identically.


# In[15]:


def memorized(func):
    cache = {}

    def call_func(*args):
        result = cache.get(args)
        if result is None:
            result = func(*args)
            cache[args] = result
        return result

    return call_func


@memorized
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(200))


# In[ ]:





# In[ ]:





# In[ ]:




