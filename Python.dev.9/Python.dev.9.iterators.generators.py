#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Iterators :")

print('''

Concept	Explanation

Iterable	An object you can pass to iter(). Has __iter__(). (e.g., lists, strings)
Iterator	An object returned by iter(). Has __next__() and __iter__()

''')


# In[2]:


from collections.abc import Iterable, Iterator

colors = ['red', 'yellow', 'green', 'blue', 'black']

# for color in colors:
#    print(color)

print('=' * 80)
print(isinstance(colors, Iterable))   # Checks if colors (a list) is an Iterable → will print True.

color_iter = iter(colors)
print(isinstance(color_iter, Iterator)) # Converts the list to an iterator object.
# This object remembers the current position while iterating.

print(next(color_iter))
print(next(color_iter))
print(next(color_iter))
print(next(color_iter))
print(next(color_iter))

# print(next(color_iter))
# color_iter = iter(colors)
# ✅ Resetting the iterator — you must do this if the previous iterator has been consumed.

# for color in colors:
#    print(color)

while True:
    try:
        print(next(color_iter))
    except StopIteration:
        break
# ✅ This is manual iteration, equivalent to a for loop:

# Calls next() on the iterator repeatedly.
# When the iterator is exhausted, it raises StopIteration.
# The loop catches the exception and breaks out.
# This is exactly what Python’s for loop does behind the scenes!


# In[3]:


color_iter = iter(colors)
while True:
    try:
        print(next(color_iter))
    except StopIteration:
        break

print('I am done')


# In[4]:


print("Iterators : range() provides another example")

for i in range(3, 18, 5):
     print(i)

print(isinstance(range(3, 18, 5), Iterable))


# In[1]:


print("Simulation : version 1")


# In[5]:


from collections.abc import Iterable

# dummy NumberStep

class NumberStepIterator:
    def __init__(self):
        self._count = 0

    def __next__(self):
        self._count += 1     # Every time next() is called, it increments _count by 1.

        if self._count > 3:  # Important: this version always stops after 3 steps, regardless of start, end, step
            raise StopIteration

        return self._count

class NumberStep:
    def __init__(self, start, end, step): #  Constructor: saves start, end, and step values, but they are not used yet (dummy version).
        self._start = start
        self._end = end
        self._step = step

    # to make NumberStep Iterable
    def __iter__(self):
        return NumberStepIterator()     # ✅ __iter__() returns a new iterator object: NumberStepIterator.
                                        # ✅ This allows NumberStep to be iterable (i.e., usable inside for loops).

for i in NumberStep(3, 18, 5):
    print(i)

print("Manual iteration with while True:")

step = NumberStep(3, 18, 5)
number_iter = iter(step)

while True:
     try:
         print(next(number_iter))
     except StopIteration:
         break

# ✅ Same logic as the for loop — manual handling of the StopIteration exception.
# ✅ Prints exactly the same result as before: 1, 2, 3.

# ⚡ Very Important Observations:
# NumberStepIterator does not use start, end, step yet.
# (That's why it's called "dummy" in the comment.)
# Real NumberStepIterator would start at 3, end at 18, step by 5 — but that's not implemented yet.
# Right now, it just counts 1 → 2 → 3 → stop, no matter what the start/end/step are.


# In[ ]:


print("Simulation : version 2")


# In[6]:


# Working NumberStep

class NumberStepIterator:
    def __init__(self, start, end, step):

        # Start slightly *behind* the real start (start - step)
        # So that the first __next__() call brings us exactly to start

        # When you create the iterator, you want the first __next__() call to land exactly on start.
        # If you just stored start, then next() would advance it before yielding anything, and you'd get wrong first value.
        # So starting at start - step fixes the first step.
        # "The first .next() will do +step, so we have to set current = start - step to start cleanly at start."
        
        self._current = start - step
        self._end = end
        self._step = step

    def __next__(self):
        self._current += self._step
        
        if self._current >= self._end:
            raise StopIteration

        return self._current

class NumberStep:
    def __init__(self, start, end, step):
        self._start = start
        self._end = end
        self._step = step

    def __iter__(self):  # Return a fresh iterator when iter() is called
        return NumberStepIterator(
            self._start,
            self._end,
            self._step
        )


for i in NumberStep(3, 18, 5):
    print(i)

print("Manual Loop:")
print("-"*10)

step = NumberStep(3, 18, 5)
number_iter = iter(step)
while True:
     try:
         print(next(number_iter))
     except StopIteration:
         break


# In[7]:


print("# This class is both an iterable and an iterator at the same time!")

print('''

🧠 Visual Concept Map:

NumberStep(start, end, step)
↓
__iter__() → returns self
↓
__next__() advances current
↓
If current >= end → StopIteration

Else → return current
''')


# In[ ]:


print("Simulation : version 3")


# In[8]:


# Final version NumberStep
# This class is both an iterable and an iterator at the same time!
# In professional Python, it is very common to make small classes both iterable and iterator 
# (like your version), especially if the iterator is stateless or simple.

class NumberStep:
    def __init__(self, start, end, step):
        self._current = start - step
        self._end = end
        self._step = step

    def __next__(self):
        self._current += self._step

        if self._current >= self._end:
            raise StopIteration

        return self._current

    def __iter__(self):  
        return self


for i in NumberStep(3, 18, 5):
    print(i)


# In[ ]:





# In[9]:


print("Another Iterators: generate Pi")

print('''

A class to generate approximations of π using a well-known mathematical series called the Leibniz series:
This formula slowly approximates π by adding and subtracting reciprocals of odd numbers.

''')


# In[10]:


print(
'''
_index → how many terms generated so far.

_max_index → how many terms maximum to generate (after that, stop iteration).

_denominator → starts at 1, then increases by 2 each time (1, 3, 5, 7, 9, ...).

_sign → alternates between +1 and -1 (for adding and subtracting terms).

_curr → accumulates the series sum.
''')

class PiSeq:
    
    def __init__(self, max_term):
        self._index = 0
        self._max_index = max_term
        self._denominator = 1
        self._sign = 1
        self._curr = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1

        if self._index > self._max_index:
            raise StopIteration

        self._curr += self._sign / self._denominator
        self._sign *= -1         # Flips the sign for the next term:
        self._denominator += 2   # Increases the denominator to the next odd number:

        return 4 * self._curr

# It creates a PiSeq object with max_term=10.
# For each term, it calculates a better and better approximation of π.
# Prints the approximation at each step.

for v in PiSeq(10):
    print(v)


# In[ ]:





# In[11]:


print("Another Iterators: Reverse Iterable")


# In[12]:


class ReverseIterable:
    def __init__(self, itrbl):
        
        self._list = list(itrbl)       # Save the given iterable as a list (forces materialization)
                                       # list(itrbl) forces evaluation of the iterable.
        self._curr_index = len(itrbl)  # Start from the length of the list (one position beyond the last item)

    def __iter__(self):                # Returns self, meaning the object is both the Iterable and the Iterator.
        return self

    def __next__(self):
        # 1. what is the next value
        # 2. what is the stop criteria
        self._curr_index -= 1
        if self._curr_index < 0:
            raise StopIteration

        return self._list[self._curr_index]
        
        # self._list is the list of items we are iterating over in reverse.
        # self._curr_index is the current position in that list (counting backward).

if __name__ == '__main__':            # It ensures that the testing code only runs if the file is executed directly, not imported as a module.
    
    reverse_list = ReverseIterable(
        [10, 3, 'abc', 'dak', 47, 100, 'hello', 9]
    )
    for item in reverse_list:
        print(item)

    reverse_text = ReverseIterable('hello world')
    for letter in reverse_text:
        print(letter)

    reverse_range = ReverseIterable(range(3, 18, 5))
    for number in reverse_range:
        print(number)


# In[ ]:





# In[13]:


print("Generators :")


# In[14]:


print('''

Important Details:

yield pauses the function, saving its local variables.

After yielding a value, execution resumes right after the yield when next() is called again.

A generator does not recompute from scratch; it remembers where it left off.

✅ Very memory efficient for large sequences!

''')


# In[15]:


# It uses yield → making it a generator function.

def count_down(n):
    print('Count down from {}'.format(n))

    while n > 0:
        print('Get next')
        # print(n)
        yield n
        n -= 1

    print('Done')

def count():
    yield 4
    yield 10
    yield 5
    yield 7
    yield 1
    yield 0


if __name__ == '__main__':
    
    g = count_down(3)  # <class 'generator'>
    print(type(g))

# Each next(g) call will:
# Print "Get next",
# Yield the next n (3, 2, 1),
# Until n = 0, then the generator will print "Done" and raise StopIteration.
       
    print("Manually advancing the generator :") 
    v = next(g)
    print(v)
    v = next(g)
    print(v)
    v = next(g)
    print(v)
    # v = next(g)
    # print(v)

    print("Advancing the generator in a for loop:") 
    for v in g:
        print(v)

    print('='*80)

    for v in count():
        print(v)


# In[ ]:





# In[16]:


# GPT4 : 🛠 Countdown Generator with Delays (Animation-like)

import time

def animated_count_down(n, delay=1):
    print(f"⏳ Starting countdown from {n}...")

    while n > 0:
        print(f"🔥 {n}")
        yield n
        n -= 1
        time.sleep(delay)  # Wait for 'delay' seconds before continuing

    print("🚀 Liftoff! 💥")

if __name__ == '__main__':
    for _ in animated_count_down(5, delay=0.5):  # 0.5 second pause between steps
        pass       # We don’t need the yielded values here; just using for timing


# In[ ]:





# In[17]:


print("Pi Generator:")

def pigen():
    curr = 0
    denominator = 1
    sign = 1

    # Infinite generator for approximating π using the Leibniz series
    while True:
        curr += sign / denominator        # Add or subtract the next term
        yield 4 * curr                    # Yield current approximation of π
        sign *= -1                        # Alternate sign
        denominator += 2                 # Move to next odd denominator

def firstn(g, n):
    for _ in range(n):
        print(next(g))

# This function takes two arguments:
# g: any generator (in this case, the output of pigen())
# n: the number of values to generate (here, 10)
# The for _ in range(n): loop calls next(g) 10 times, 
# asking the generator for the next approximation of π, and prints each one.
                                                                          
firstn(pigen(), 10)


# In[ ]:





# In[18]:


print("Pi Accelerator :")

def pigen():
    curr = 0
    denominator = 1
    sign = 1

    while True:
        curr += sign / denominator
        yield 4 * curr
        sign *= -1
        denominator += 2

# Now this is the clever part — a method to speed up the convergence using a nonlinear extrapolation method, 
# often called Aitken’s Δ² Process (a sequence acceleration technique).

# Thus, it keeps using new approximations from the slow generator pigen() but produces a much faster-converging sequence.

def accelerator(g):
    s1 = next(g)    # First π approximation
    s2 = next(g)    # Second π approximation
    s3 = next(g)    # Third π approximation

    while True:
        result = s3 - (s3 - s2)**2 / (s3 - 2*s2 + s1)
        yield result
        s1, s2, s3 = s2, s3, next(g)


def firstn(g, n):
    for _ in range(n):
        print(next(g))

# Start with pigen() generator (slow π approximations).
# Wrap it with accelerator() (faster convergence).
# Print the first 1000 accelerated results.

firstn(accelerator(pigen()), 10)


# In[ ]:





# In[19]:


print("Generate the even numbers :")

# This is a generator function.
# It starts at start and keeps yielding consecutive integers forever.
# Every time next() is called, it returns the current number and increments it by 1.

def numbers(start):
    current = start
    while True:
        yield current
        current += 1

# This is another generator function that wraps another generator g (in this case, numbers).
# Calls next(g) to get the next number.
# If the number is even (current % 2 == 0), it yields it.
# If not, it simply skips it (does not yield odd numbers).
# So this generator filters out odd numbers, and only yields even numbers.

def even_numbers(g):
    while True:
        current = next(g)
        if current % 2 == 0:
            yield current

# firstn(g, n):
# Receives a generator g and prints the first n values produced by it.
# even_numbers(numbers(11)):
# First, numbers(11) generates numbers starting at 11.
# then, even_numbers() filters this stream, only passing even numbers.
# firstn(..., 10):
# Prints the first 10 even numbers starting from 11.

if __name__ == '__main__':
    def firstn(g, n):
        for _ in range(n):
            print(next(g))

    firstn(even_numbers(numbers(11)), 10)


# In[ ]:





# In[20]:


print("Building generators and creating filters dynamically :")


# In[21]:


# to generate the next number

def numbers(start):
    current = start
    while True:
        yield current
        current += 1

# to filter out even numbers
# def not_div_by_2(g):
#     for i in g:
#         if i % 2 != 0:
#             yield i
#     # while True:
#     #     current = next(g)
#     #     if current % 2 != 0:
#     #         yield current

# to filter out numbers divisible by 3
# def not_div_by_3(g):
#     for i in g:
#         if i % 3 != 0:
#             yield i

# def not_div_by_5(g):
#     for i in g:
#         if i % 5 != 0:
#             yield i

# def not_div_by_7(g):
#     for i in g:
#         if i % 7 != 0:
#             yield i

def not_div_by(g, factor): # filters a stream (g) and yields only numbers not divisible by factor.
    for i in g:
        if i % factor != 0:
            yield i


if __name__ == '__main__':
    
    def firstn(g, n):
        for _ in range(n):
            print(next(g))

    # firstn(
    #     not_div_by_7(
    #         not_div_by_5(
    #             not_div_by_3(
    #                 not_div_by_2(
    #                     numbers(2)
    #                 )
    #             )
    #         )
    #     )
    #     , 10)

    firstn(
        not_div_by(
            not_div_by(
                not_div_by(
                    not_div_by(
                        numbers(2),
                        2
                    ), 3
                ), 5
            ), 7
        ), 10
    )

# If you wanted to clean up this even more, you could build the pipeline automatically like:
# To avoid nested function calls :

factors = [2, 3, 5, 7]
g = numbers(2)

for f in factors:
    g = not_div_by(g, f)

firstn(g, 10)

# You loop over each factor (2, 3, 5, and 7).
# Each time, you "wrap" the current generator g with a new filter using not_div_by.

# What happens exactly?
# First: filter out numbers divisible by 2.
# Then: filter the remaining numbers to remove those divisible by 3.
# Then: further filter to remove numbers divisible by 5.
# Then: further filter to remove numbers divisible by 7.
# This builds a chain of filters — each one applying on top of the previous

# for f in factors:
#    g = not_div_by(g, f)
# what happens is not that all numbers are generated at once — instead:

# g is still a lazy generator.
# Each not_div_by(g, f) wraps the previous generator g.

# Each number is pulled one at a time (sequentially) through the whole chain of filters.
# Imagine you call next(g) at the very end, after all wrapping.

# When you call next(g), here’s what happens:
# g asks the wrapped not_div_by(7) filter: "Give me the next good number."
# not_div_by(7) asks the wrapped not_div_by(5) filter: "Give me the next good number."
# not_div_by(5) asks not_div_by(3): "Give me the next good number."
# not_div_by(3) asks not_div_by(2): "Give me the next good number."
# not_div_by(2) asks the original numbers(2) generator: "Give me the next raw number."

# Then at every layer:
# Each filter checks if the number satisfies its rule.
# If yes → passes it to the next filter.
# If no → discards it and asks for the next number again.
# Only after passing all filters, the number is actually yielded to you!


# In[22]:


print("Building a prime number generator using the Sieve of Eratosthenes idea! ")


# In[23]:


def numbers_from(start): # This infinite generator produces numbers starting from start and keeps incrementing.
                         # It never stops unless you limit it manually.
    current = start
    while True:
        yield current
        current += 1

# This is a filter generator:
# Takes a generator g (sequence of numbers) and a factor.
# Yields only numbers that are NOT divisible by factor.

def not_div_by(g, factor):
    for i in g:
        if i % factor != 0:
            yield i


# ✅ This is the magic part:
# It grabs the next number from the sequence (that hasn't been filtered yet).
# Yields it as a prime.
# Updates the generator g:
# Now filter out multiples of this newly found prime.
# ✅ It keeps refining the sequence:
# First removes multiples of 2,
# Then multiples of 3,
# Then multiples of 5,

# This is a generator-based Sieve of Eratosthenes!

def prime_gen(g):
    while True:
        prime = next(g)
        yield prime
        g = not_div_by(g, prime)

# A helper function:
# Given a generator g and a number n,
# Prints the first n values from the generator.

def firstn(g, n):
    for _ in range(n):
        print(next(g))

if __name__ == '__main__':

    firstn(prime_gen(numbers_from(2)), 10)

# ✅ Here's what happens step-by-step:
# numbers_from(2) → 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
# prime_gen() grabs 2:
# Yields 2.
# Filters out all multiples of 2.
# From the remaining numbers:
# Grabs 3.
# Yields 3.
# Filters out all multiples of 3.
# From the remaining numbers:
# Grabs 5 (since 4 was filtered by 2).
# Yields 5.
# Filters out multiples of 5.
# And so on...
# ✅ It keeps yielding primes indefinitely.
# ✅ But firstn(..., 10) only prints the first 10 primes


# In[ ]:




