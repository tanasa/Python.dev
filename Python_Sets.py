#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('''

Python Sets :

A set is a collection which is unordered, unchangeable, and unindexed.

No duplicate elements. If try to insert the same item again, it overwrites previous one.

An unordered collection. When we access all items, they are accessed without any specific order 
and we cannot access items using indexes as we do in lists.

Internally use hashing that makes set efficient for search, insert and delete operations. 
It gives a major advantage over a list for problems with these operations.

Mutable, meaning we can add or remove elements after their creation, 
the individual elements within the set cannot be changed directly.

''')


# In[2]:


# https://www.geeksforgeeks.org/sets-in-python/
# https://www.w3schools.com/python/python_sets.asp
# https://realpython.com/python-sets/
# https://docs.python.org/2/library/sets.html


# In[ ]:





# In[3]:


thisset = {"apple", "banana", "cherry"}
print(thisset)

# The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# A set can contain different data types:
# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
print(set1)


# In[4]:


# Access Items

# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[5]:


print('''

While you cannot modify the individual elements directly, you can still add or remove elements from the set.

.add()
.remove()

''')


# In[6]:


# Change Items

print("Once a set is created, you cannot change its items, but you can add new items.")

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)


# In[7]:


print("To add items from another set into the current set, use the update() method.")

# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)


# In[8]:


# Remove Item

# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


# In[9]:


# You can also use the pop() method to remove an item, 
# but this method will remove a random item, so you cannot be sure what item that gets removed.

# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # name 'thisset' is not defined


# In[10]:


print('''

There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

''')


# In[11]:


print("Union")

# Join set1 and set2 into a new set:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# In[12]:


# Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.
# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# In[13]:


# Use | to join multiple sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)


# In[14]:


print('''Join a Set and a Tuple''')

# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.

# Union of a Set and a List
set1 = {1, 2, 3}
list1 = [3, 4, 5]
result = set1.union(list1)
print(result)  # Output: {1, 2, 3, 4, 5}

# Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# Union of a Set and a Dictionary

set1 = {1, 2, 3}
dict1 = {4: "A", 5: "B"}
result = set1.union(dict1)  # Only dictionary keys are considered
print(result)  

# Union Using Dictionary Keys

set1 = {1, 2, 3}
dict1 = {3: "A", 4: "B", 5: "C"}
result = set1.union(dict1.keys())  # Explicitly using keys
print(result) 

# Union Using Dictionary Keys

result = set1.union(dict1.values())  # Union with values
print(result)  # Output: {'A', 'B', 'C', 'D'}

# Union with Both Keys and Values
# If you want to include both keys and values:

set1 = {1, 2, 3}
dict1 = {4: "X", 5: "Y"}
result = set1.union(dict1.keys(), dict1.values())  # Union with keys and values
print(result)  # Output: {1, 2, 3, 4, 5, 'X', 'Y'}


# In[15]:


print("Intersection")
# The intersection() method will return a new set, that only contains the items that are present in both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# The values True and 1 are considered the same value. The same goes for False and 0.


# In[16]:


print("Difference")

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)


# In[17]:


print("Symmetric Differences")

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# We can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)


# In[18]:


print('''

Set Methods :

Method	Shortcut	Description 
add()	 	                        Adds an element to the set
clear()	 	                        Removes all the elements from the set
copy()	        	                Returns a copy of the set
difference()	     -	            Returns a set containing the difference between two or more sets
difference_update()	-=	            Removes the items in this set that are also included in another, specified set
discard()	 	                    Remove the specified item
intersection()	        &	        Returns a set, that is the intersection of two other sets
intersection_update()	&=	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                Returns whether two sets have a intersection or not
issubset()	<=	                    Returns whether another set contains this set or not
         	<	                    Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	                Returns whether this set contains another set or not
 	            >	                Returns whether all items in other, specified set(s) is present in this set
pop()	 	                        Removes an element from the set
remove()	 	                    Removes the specified element
symmetric_difference()	        ^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	        |	                Return a set containing the union of sets
update()	    |=	                Update the set with the union of this set and others

''')


# In[ ]:





# In[19]:


# x1.isdisjoint(x2)
# x1.isdisjoint(x2) returns True if x1 and x2 have no elements in common:

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1.isdisjoint(x2)
x2 - {'baz'}
x1.isdisjoint(x2 - {'baz'})

# x1.issubset(x2)
# x1 <= x2

x1 = {'foo', 'bar', 'baz'}
x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'})
x2 = {'baz', 'qux', 'quux'}
x1 <= x2

# x1.issuperset(x2)
# x1 >= x2
# Determine whether one set is a superset of the other.
# A superset is the reverse of a subset. A set x1 is considered a superset of another set x2 if x1 contains every element of x2.

x1 = {'foo', 'bar', 'baz'}
x1.issuperset({'foo', 'bar'})
x2 = {'baz', 'qux', 'quux'}
x1 >= x2


# In[20]:


print('''

z.intersection_update() : x1.intersection_update(x2) and x1 &= x2 update x1, retaining only elements found in both x1 and x2
z.union_update()  : x1.update(x2) and x1 |= x2 add to x1 any elements in x2 that x1 does not already have
z.difference_update()  : x1.difference_update(x2) and x1 -= x2 update x1, removing elements found in x2
x1.symmetric_difference_update(x2) : x1.symmetric_difference_update(x2) and x1 ^= x2 update x1, retaining elements found in either x1 or x2, but not both
''')


# In[21]:


# x1.update(x2[, x3 ...])
# x1 |= x2 [| x3 ...]

# Modify a set by union.

# x1.update(x2) and x1 |= x2 add to x1 any elements in x2 that x1 does not already have:

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 |= x2
print(x1)
{'qux', 'foo', 'bar', 'baz'}

x1.update(['corge', 'garply'])
print(x1)
{'qux', 'corge', 'garply', 'foo', 'bar', 'baz'}


# In[22]:


# x1.intersection_update(x2[, x3 ...])
# x1 &= x2 [& x3 ...]

# Modify a set by intersection.

# x1.intersection_update(x2) and x1 &= x2 update x1, retaining only elements found in both x1 and x2:

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 &= x2
print(x1)
{'foo', 'baz'}

x1.intersection_update(['baz', 'qux'])
print(x1)
{'baz'}


# In[23]:


# x1.difference_update(x2[, x3 ...])
# x1 -= x2 [| x3 ...]

# Modify a set by difference.

# x1.difference_update(x2) and x1 -= x2 update x1, removing elements found in x2:

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 -= x2
print(x1)
{'bar'}

x1.difference_update(['foo', 'bar', 'qux'])
print(x1)
set()


# In[24]:


# x1.symmetric_difference_update(x2)
# x1 ^= x2

# Modify a set by symmetric difference.

# x1.symmetric_difference_update(x2) and x1 ^= x2 update x1, retaining elements found in either x1 or x2, but not both:

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
 
x1 ^= x2
print(x1)
{'bar', 'qux'}

x1.symmetric_difference_update(['qux', 'corge'])
print(x1)
{'bar', 'corge'}


# In[ ]:





# In[25]:


print(
'''
Python Frozen Sets

A frozenset in Python is an immutable version of a regular set. 
Unlike normal sets, frozenset elements cannot be modified after creation, 
making them hashable and suitable as dictionary keys or elements in another set.

Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting 
the frozen set or sets to which they are applied.

While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.

''')


# In[26]:


# Same as {"a", "b","c"}
s = set(["a", "b","c"])

print("Normal Set")
print(s)

# A frozen set
fs = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(fs)


# In[27]:


fs = frozenset([1, 2, 3, 4, 5])
print(fs)  # Output: frozenset({1, 2, 3, 4


# In[28]:


print('''

Key Properties of Frozenset

✅ Immutable – Cannot add, remove, or change elements.
✅ Hashable – Can be used as a dictionary key or a set element.
✅ Supports set operations – Intersection, union, difference, etc.

''')


# In[29]:


print("Set Operations with Frozensets")

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print("Union (| or .union())")
print(fs1 | fs2)  # Output: frozenset({1, 2, 3, 4, 5})
print(fs1.union(fs2))  # Output: frozenset({1, 2, 3, 4, 5})

print("Intersection (& or .intersection())")
print(fs1 & fs2)  # Output: frozenset({3})
print(fs1.intersection(fs2))  # Output: frozenset({3})

print("Difference (- or .difference())")
print(fs1 - fs2)  # Output: frozenset({1, 2})
print(fs1.difference(fs2))  # Output: frozenset({1, 2})

print("Symmetric Difference (^ or .symmetric_difference())")
print(fs1 ^ fs2)  # Output: frozenset({1, 2, 4, 5})
print(fs1.symmetric_difference(fs2))  # Output: frozenset({1, 2, 4, 5})


# In[30]:


print('''

Using Frozensets as Dictionary Keys

Since frozenset is hashable, it can be used as a dictionary key

''')

d = {frozenset([1, 2, 3]): "group1", 
     frozenset([4, 5]): "group2"}

print(d[frozenset([1, 2, 3])])        # Output: group1


# In[31]:


print('''Nesting Frozensets

Since frozensets are immutable, they can be elements of a set of sets.

''')

nested_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(nested_sets)  # Output: {frozenset({1, 2}), frozenset({3, 4})}


# In[32]:


print('''

When to Use Frozensets?

🔹 When you need an immutable set (e.g., to prevent accidental modification).
🔹 When using sets as dictionary keys or elements in another set.
🔹 When working with data that should remain unchanged for security or consistency.

''')


# In[33]:


print('''

Operators for Sets
Sets and frozen sets support the following operators:

Operators	Notes
key in s	    containment check
key not in s	non-containment check
s1 == s2	    s1 is equivalent to s2
s1 != s2	    s1 is not equivalent to s2
s1 <= s2	    s1 is subset of s2
s1 < s2	        s1 is proper subset of s2
s1 >= s2	    s1 is superset of s2
s1 > s2	        s1 is proper superset of s2
s1 | s2	        the union of s1 and s2
s1 & s2	        the intersection of s1 and s2
s1 – s2	        the set of elements in s1 but not s2
s1 ˆ s2	        the set of elements in precisely one of s1 or s2

''')


# In[ ]:




