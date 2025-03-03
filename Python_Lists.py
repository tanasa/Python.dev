#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://www.geeksforgeeks.org/python-lists/


# In[2]:


print("Lists")


# In[3]:


print('''

List can contain duplicate items.
List in Python are Mutable. Hence, we can modify, replace or delete the items.
List are ordered. It maintain the order of elements based on how they are added.
Accessing items in List can be done directly using their position (index), starting from 0

''')


# In[4]:


# A few notes on the Lists in Python


# In[5]:


a = [10, 20, 15]

print(a[0]) # access first item
a.append(11) # add item
print(a)
a.remove(20) # remove item
print(a)


# In[6]:


# Creating List with Repeated Elements
# We can create a list with repeated elements using the multiplication operator.

# Create a list [2, 2, 2, 2, 2]
a = [2] * 5
print(a)

# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7
print(b)


# In[7]:


print('''

Adding Elements into List :
We can add elements to a list using the following methods:

append(): Adds an element at the end of the list.
extend(): Adds multiple elements to the end of the list.
insert(): Adds an element at a specific position.
''')


# In[ ]:





# In[8]:


# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 


# In[9]:


# Updating Elements into List
# We can change the value of an element by accessing it using its index.

a = [10, 20, 30, 40, 50]

# Change the second element
a[1] = 25 

print(a)  


# In[10]:


# We can remove elements from a list using:

# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.

a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)  


# In[11]:


# https://www.w3schools.com/python/python_lists_access.asp


# In[12]:


# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# In[13]:


# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# In[14]:


# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[1:5] = ["beans", "sweet peas"]
print(thislist)


# In[15]:


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# In[16]:


# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# In[17]:


# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# In[18]:


# The insert() method inserts an item at the specified index:
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# In[19]:


# Extend List
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# In[20]:


# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# In[21]:


# Remove Specified Item
# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# In[22]:


# If there are more than one item with the specified value, the remove() method removes the first occurrence:
# Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# In[23]:


# Remove Specified Index
# The pop() method removes the specified index.

# Example : Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# In[24]:


# The del keyword also removes the specified index:
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# In[25]:


# The del keyword can also delete the list completely.
# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist


# In[26]:


# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# In[ ]:





# In[27]:


# Loop Lists

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# In[28]:


# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
for i in range(len(thislist)):
  print(thislist[i])

# To print the list from the second element : 

# Using list slicing to start from index 2
print("printing a sliced list:")
for i in range(3, len(thislist)):
    print(thislist[i])

# Using list slicing to start from index 2
# Directly slicing the list (recommended)
print("printing a sliced list:") 
for item in thislist[2:]:
    print(item)


# In[29]:


# Using a While Loop

# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# In[30]:


# Looping using List Comprehension


# In[31]:


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# In[32]:


# A new list using a for statement :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# A new list without using a for statement :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


# In[33]:


# List Comprehension : newlist = [expression for item in iterable if condition == True]


# In[34]:


newlist = [x for x in fruits if x != "apple"]
print(newlist)


# In[35]:


# Note : ITERABLE : The iterable can be any iterable object, like a list, tuple, set etc.
# Range() : to use range() function to create an iterable.


# In[36]:


newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


# In[37]:


# Sort Lists :


# In[38]:


# Sorting the lists :
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)


# In[39]:


# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# In[40]:


# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# In[41]:


# The reverse() method reverses the current sorting order of the elements.

# Reverses the order of the elements in the list without sorting.
# The list remains in the same original order, just flipped.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# In[42]:


# Copy lists :


# In[43]:


# To copy a list : use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# To copy a list : use the : slice method
# Make a copy of a list with the : operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# In[44]:


# Join lists


# In[45]:


# Join two lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# In[46]:


print ('''

List Methods :
Python has a set of built-in methods that you can use on lists.

Method	Description :
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

''')


# In[47]:


# https://docs.python.org/3/tutorial/datastructures.html


# In[48]:


print('''

The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
Add an item to the end of the list. Similar to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, 
and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. 
If no index is specified, a.pop() removes and returns the last item in the list. 
It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()
Remove all items from the list. Similar to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. 
The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Similar to a[:].

''')


# In[49]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)

print("method : count()")
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits)

print("method : index()")    
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting at position 4
print(fruits)

print("method : reverse()")
print(fruits.reverse())
print(fruits) 

print("method : append()")
print(fruits.append('grape'))
print(fruits) 

print("method : sort()")
print(fruits.sort())
print(fruits) 

print("method : pop()")
print(fruits) 
print(fruits.pop())
print(fruits) 


# In[50]:


# You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None.
# This is a design principle for all mutable data structures in Python.


# In[51]:


print('''

Using Lists as Stacks :

The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). 
To add an item to the top of the stack, use append(). 
To retrieve an item from the top of the stack, use pop() without an explicit index. 

''')


# In[52]:


stack = [3, 4, 5]
stack.append(6)
print(stack)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)


# In[53]:


print('''

Using Lists as Queues :

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); 
however, lists are not efficient for this purpose. 

While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow 
(because all of the other elements have to be shifted by one).

''')


# In[54]:


from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")                  # Terry arrives
print(queue)
queue.append("Graham")                 # Graham arrives
print(queue)
print(queue.popleft())                 # The first to arrive now leaves
print(queue)
print(queue.popleft())                        # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrival


# In[ ]:





# In[55]:


print('''

How Python Handles Function Arguments :

In Python, function arguments are passed by object reference, which means Python uses pass-by-object-reference 
(also sometimes called pass-by-assignment). 
This is a mix of pass-by-value and pass-by-reference, depending on the type of object being passed.


Immutable objects (e.g., int, float, str, tuple):

Passed by value (effectively).
Changes to the parameter inside the function do not affect the original variable.

Mutable objects (e.g., list, dict, set):

Passed by reference (effectively).
Changes to the object inside the function affect the original variable.

''')


# In[56]:


# Examples
# Immutable Object (Pass-by-Value)
def modify(x):
    x = 10  # Assigning a new value creates a new local variable
    print("Inside function:", x)

num = 5
modify(num)
print("Outside function:", num)

# num remains 5 because integers are immutable, and x = 10 creates a new local variable inside the function.


# In[57]:


# Examples
# Mutable Object (Pass-by-Reference)

def modify_list(lst):
    lst.append(4)  # Modifying the list directly

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)


# In[58]:


print('''

Immutable types (e.g., int, str, tuple) behave like pass-by-value because reassigning a new value creates a new object.
Mutable types (e.g., list, dict, set) behave like pass-by-reference because modifying the object inside a function affects the original.

''')


# In[ ]:




