#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print("In this section : Dictionaries")
print("In this section : Recursion vs Iteration")


# In[ ]:





# In[2]:


print('''

What dict.setdefault() does:

setdefault() is a dictionary method that:

Checks if a key exists in the dictionary.
If the key exists, it returns its value.
If the key does not exist, it:
Adds the key to the dictionary with a default value you provide.
Then returns that default value.

Why is it useful?
It saves you from writing an if key not in dict: check manually.
It's shorter and cleaner when you want to initialize default values (like empty lists, sets, or counters).

''')

# Real-world example (building a dictionary of lists):

words = ['cat', 'car', 'dog', 'door']
d = {}

for word in words:
    first_letter = word[0]
    d.setdefault(first_letter, []).append(word)

print(d)

# setdefault() = "get me the value for this key — and if it doesn’t exist, create it with a default."
# It's a shortcut for safe, clean dictionary updating.


# In[ ]:





# In[3]:


# Our code is almost perfect and does a good job answering the question "How many people endorse each skill?" 
# — not just the raw number of endorsements per skill.

endorsements = {
    'Bob': ['Python', 'Java', 'HTML', 'CSS', 'C++', 'Python', 'Python'],
    'David': ['Python', 'WebDev', 'JavaScript', 'Python'],
    'Eric': ['Java', 'HTML', 'SQL'],
    'Frank': ['CSS', 'Python']
}

# what are my skills and how many people endorse each skill
# {'Python': 3, 'Java': 2, ...}

def get_skills(endorsements):
    result = {}

    for skills in endorsements.values():
        for skill in set(skills):
            result.setdefault(skill, 0)
            result[skill] += 1

    return result


skills = get_skills(endorsements)
print(skills)


# In[ ]:





# In[4]:


# An anagram is when you rearrange the letters of a word or phrase to make another word or phrase, using all the original letters exactly once.

# For example:
# "listen" → "silent"
# "evil" → "vile"
# "dusty" → "study"
# "conversation" → "voices rant on"

# In short: same letters, different order.


# In[5]:


# anagram: post, stop, pots, tops
# not anagrams: aab, abb

# You create an empty dictionary.
# This dictionary will group together words that are anagrams of each other.
# The key will be the sorted letters of the word (signature).
# The value will be a set of words that match that signature.

# In Short:
# Sort each word → to create a common signature.
# Group words with the same signature.
# Return a list of all groups.
  
# Returns a list of all anagrams
def form_anagrams(words):
    anagram_dict = {}

    for word in words:
        signature = ''.join(sorted(word))
        anagram_dict.setdefault(signature, set())
        anagram_dict[signature].add(word)

    return [list(ana) for ana in anagram_dict.values()]

words = ['abc', 'ab', 'bca', 'cab', 'd', 'da', 'ba', 'ad']
print(form_anagrams(words))

# [
#   ['abc', 'bca', 'cab'],
#   [...],
#   ...
#   ['d']
# ]

with open('zwords.txt') as fin:
    anagrams = form_anagrams([word.strip() for word in fin])
    print(sorted(anagrams, key=len, reverse=True)[:5])


# In[6]:


# Print out the top 5 biggest anagrams from zwords.txt

def form_anagrams(words):
    anagram_dict = {}

    for word in words:
        signature = ''.join(sorted(word))
        anagram_dict.setdefault(signature, set())
        anagram_dict[signature].add(word)

    return [list(ana) for ana in anagram_dict.values()]

with open('zwords.txt') as fin:
    anagrams = form_anagrams([word.strip() for word in fin])
    print(sorted(anagrams, key=len, reverse=True)[:5])

# What does key=len do?
# Here, len is the function used as the sorting key. So Python will:
# Take each element in anagrams,
# Apply len() to it,
# Sort the list based on that length.
# It does not sort the strings alphabetically — it sorts them by length.

# sorted(anagrams, key=len, reverse=True)


# In[7]:


print("Interlocked words: ")


# In[8]:


# A word is considered *interlocked* if:
#   - The sub-word formed by its even-indexed letters (word[::2]), and
#   - The sub-word formed by its odd-indexed letters (word[1::2])
# are both valid words.

# A valid word is one that appears in the dictionary file `words.txt`.

# Example:
#   "schooled" → even-indexed letters: "shoe", odd-indexed letters: "cold"
#    Both "shoe" and "cold" are valid words, so "schooled" is interlocked.


# In[9]:


# Print all the interlocked words from zwords.txt

# bisect_left: used for fast binary search in a sorted list.
# time: used to measure performance.

from bisect import bisect_left
import time

# Binary_search using bisect
# Efficient search for target in words, assuming words is sorted.
# Returns True if found

def binary_search(target, words):
    index = bisect_left(words, target)
    if index != len(words) and words[index] == target:
        return True
    else:
        return False

# my_binary_search is a manual version of binary search.
def my_binary_search(target, words):
    low = 0
    high = len(words) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == words[mid]:
            return True
        elif target < words[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False

with open('zwords.txt') as fin:
    words = []
    for line in fin:
        word = line.strip()
        words.append(word)

    start = time.time()

    interlocked = []

    for word in words:
        even_part = word[::2]
        odd_part = word[1::2]

        # if even_part in words and odd_part in words:
        if binary_search(even_part, words) and binary_search(odd_part, words):
            interlocked.append(word)

    end = time.time()

    print('{} seconds'.format(end - start))

    print(interlocked[:10])


# In[10]:


print("Interlocked words: using set() :")

print('''

You use a set() instead of a list() because set lookup is much faster — almost instant.

Here's why:

Data Structure	Lookup Time (Checking if item in collection)
list	slow: O(n) — you might have to check every element
set	fast: O(1) — Python uses a hash table internally

''')


# In[11]:


# Another version of the code : using SET()

# This script reads a list of words from words.txt into a set for fast lookup.
# It searches for interlocked words — words where the even-indexed and odd-indexed letters each form valid words.
# If both parts exist in the set, the word is added to the interlocked list.
# Finally, it prints the total time taken and the list of interlocked words found.

# print all the interlocked words from zwords.txt

import time

with open('zwords.txt') as fin:
    words = set()
    for line in fin:
        word = line.strip()
        words.add(word)

    start = time.time()

    interlocked = []

    for word in words:
        even_part = word[::2]
        odd_part = word[1::2]

        if even_part in words and odd_part in words:
            interlocked.append(word)

    end = time.time()

    print('{} seconds'.format(end - start))

    print(interlocked[:6])


# In[ ]:





# In[12]:


print("RECURSION : example 1")


# In[13]:


print("Abecedarian")

# is_abecedarian_recur(word) checks if a word's letters are in alphabetical order.
# For example:
# "accept" → a, c, c, e, p, t → in order.
# "brother" → b, r, o, t, h, e, r → not in order.
# It works recursively:
# If the word has 0 or 1 letters → True.
# Otherwise, it checks:
# Is the first letter ≤ second letter? (alphabetically)
# And then calls itself on the rest of the word.

def is_abecedarian_recur(word):
    if len(word) <= 1:
        return True

    return word[0] <= word[1] and is_abecedarian_recur(word[1:])

print(is_abecedarian_recur('accept'))
print(is_abecedarian_recur('brother'))


# In[ ]:





# In[14]:


print("RECURSION : example 2")


# In[15]:


# This function replaces all occurrences of target in msg with replacement.

# It first splits the msg by the target, creating a list of chunks.
# Then it joins those chunks with the replacement.

import time

def replace_all(msg, target, replacement):
    return replacement.join(msg.split(target))

print(replace_all('to be or not to be', 'to', '2')) # 2 be or not 2 be
print(replace_all('gogogo', 'go', 'gone')) # gonegonegone
print(replace_all('aaaaa', 'aaa', 'b')) # baa
print(replace_all('advanced calculus', 'math', 'physics')) # advanced calculus

def replace_all_recur(msg, target, replace):
    try:
        pos = msg.index(target)
        return (msg[:pos] + replace +
                replace_all_recur(msg[pos+len(target):], target, replace))
    except Exception:
        return msg

print(replace_all_recur('to be or not to be', 'to', '2')) # 2 be or not 2 be
print(replace_all_recur('gogogo', 'go', 'gone')) # gonegonegone
print(replace_all_recur('aaaaa', 'aaa', 'b')) # baa
print(replace_all_recur('advanced calculus', 'math', 'physics')) # advanced calculus


# In[16]:


print("RECURSION : example 3 : ")


# In[17]:


print("Factorial :")
# factorial(n) computes the factorial of n, defined as n! = n × (n-1) × (n-2) × ... × 1.

def factorial(n):
    if n < 0:
        # sanity check
        return -1
    elif n == 0:
        # base case
        return 1

    # recursive step
    return n * factorial(n - 1)

print(factorial(20))
print(factorial(-1))


# In[18]:


print("RECURSION : example 4 : FIBONACCI ")


# In[19]:


# Fibonacci series : F(1)=1,F(2)=1,and for n≥3,F(n)=F(n−1)+F(n−2)

# Here are three versions of the Fibonacci function in Python, showing:
# Iterative
# Recursive (no memoization)
# Recursive with memoization (top-down dynamic programming)

print("FIBONACCI : iteration")
# 1. Iterative version (most efficient)
def fib_iter(n):
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b if n > 1 else 1

print("FIBONACCI : using iteration")
print(fib_iter(20))

# 2. Fibonacci using recursion without memoization (slow)
print("FIBONACCI : using recursion without memoization (slow)")

def fib_recur(n):
    if n <= 2:
        return 1
    return fib_recur(n - 1) + fib_recur(n - 2)

print(fib_recur(20))

# 3. Fibonacci using recursion with memoization (fast & elegant)
print("FIBONACCI : using recursion with memoization / caching (fast)")

memo = {1: 1, 2: 1}

def fib_memo(n):
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print("Recursive with memo:", fib_memo(20))  # Output: 55

# Explanations : 
# memo = {1: 1, 2: 1}
# This saves already known values:
# fib(1) = 1
# fib(2) = 1
# Memoization means: store results after computing them once, so you don't recompute them again.

# Function fib_memo(n):
# Checks: Is n already calculated and stored in memo?
# if n in memo:
#    return memo[n]
# If not, it recursively computes:
# memo[n] = fib_memo(n - 1) + fib_memo(n - 2)

# First compute fib(n-1), then fib(n-2).
# Add the two results.
# Save memo[n] for later.
# Finally, return memo[n].


# In[ ]:





# In[20]:


print("Set recursion limit : sys.setrecursionlimit ")


# In[21]:


import sys

# Set recursion limit to a larger number, e.g., 5000
sys.setrecursionlimit(5000)

memo = {1: 1, 2: 1}

def fib(n):
    if n in memo:
        return memo[n]
    else:
        result = fib(n - 1) + fib(n - 2)
        memo[n] = result
        return result

print(fib(2000))


# In[ ]:





# In[22]:


print("Counters:")


# In[23]:


# Quick Definition:

# A Counter takes a list (or any iterable) and counts how many times each element appears.
# It’s like a super-powered dictionary where the default value is always 0 and it just adds 1 every time it sees an item.

from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(words)
print(counter)


# In[ ]:





# In[24]:


print('''

Main Data Structures in collections library :

Name	What it is	Quick Example	Use Case

namedtuple	Tuple with named fields	Point(x=1, y=2)	Replaces simple classes

deque	Double-ended queue (fast appends/pops from both sides)	deque([1,2,3])	Queues, sliding windows

Counter	Counts occurrences of elements	Counter('hello') → {'h':1,'e':1,'l':2,'o':1}	Counting things fast

OrderedDict	Dict that remembers insertion order (before Python 3.7)	OrderedDict()	Order-sensitive data

defaultdict	Dict with default value if key missing	defaultdict(int)	Avoid KeyError, auto-initialize

ChainMap	Combine multiple dicts together	ChainMap(d1, d2)	Multiple context lookups

''')


# In[25]:


print('''

Quick Highlights:

1. namedtuple
Like a lightweight class : easy to create and access fields by name.

''')

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print(p.x, p.y)  # 2 3


# In[26]:


print('''
2. deque
Double-ended queue — fast insert/remove from both ends (unlike normal list).

Good for queues, sliding window problems.
''')

from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(d)  # deque([0, 1, 2, 3, 4])
d.pop()   # 4
d.popleft()  # 0


# In[27]:


print('''

3. Counter
Automatically counts elements.
''')

from collections import Counter

c = Counter('banana')
print(c)  # Counter({'a': 3, 'n': 2, 'b': 1})
print(c.most_common(1))  # [('a', 3)]


# In[28]:


print('''

4. OrderedDict
Before Python 3.7, regular dicts didn’t guarantee order.

OrderedDict preserved insertion order.
''')

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)  # OrderedDict([('a', 1), ('b', 2)])


# In[29]:


print('''

5. defaultdict
Dict with a default value type if key not found.

No more KeyError!
''')

from collections import defaultdict

dd = defaultdict(int)
dd['apple'] += 1
print(dd)  # defaultdict(<class 'int'>, {'apple': 1})


# In[30]:


print('''

6. ChainMap
Combine multiple dictionaries into one "view".

python
Copy
Edit
from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
cm = ChainMap(d1, d2)
print(cm['b'])  # 2 (takes from d1 first)
print(cm['c'])  # 4

''')


# In[ ]:





# In[31]:


print("Other data structures :")


# In[32]:


print(''' 

🧠 From heapq module

Name	Description
heapq	Priority queue (min-heap) based on a list

''')

import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappop(heap)  # pops 1, the smallest


# In[33]:


print(
'''

📚 From queue module

Name	Description
Queue	Thread-safe FIFO queue
LifoQueue	Stack (Last In First Out)
PriorityQueue	Queue where elements are dequeued by priority

''')


# In[34]:


print(
'''

Built-ins:
    list, tuple, dict, set, str

collections:
    deque, Counter, defaultdict, OrderedDict, ChainMap, namedtuple

advanced:
    heapq (priority heap)
    queue (FIFO, LIFO, PriorityQueue)
    collections.abc (interfaces like Iterable, Sequence)

third-party:
    numpy arrays, pandas dataframes, bitarrays

''')


# In[ ]:




