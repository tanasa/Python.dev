#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print("Context Managers :")


# In[2]:


print('''

🧠 What is a Context Manager?

A context manager is an object that defines actions to be performed when entering and exiting a block of code — 
typically used with the with statement.

✅ The classic example:

with open('file.txt') as f:
    data = f.read()

What happens:

open('file.txt') returns a context manager object (a file handler).

__enter__() is called → opens the file.

You do stuff inside the with block.

__exit__() is called → closes the file, even if an error occurs!

✅ Ensures cleanup is always performed (like closing files, releasing locks, or rolling back transactions).

''')

print('''

🧱 Key Methods of a Context Manager
To create a context manager manually, you define a class with:

class MyContextManager:
    def __enter__(self):
        # setup (e.g., open file, start timer)
        return resource

    def __exit__(self, exc_type, exc_value, traceback):
        # cleanup (e.g., close file, stop timer)
        return False  # or True to suppress exceptions

''')


# In[3]:


with open('zcourses.txt') as fin:
     for line in fin:
         line = line.strip()
         print(line)


# In[4]:


print("Examples of Context Managers :")

# with open('course-list1.txt') as fin:
#     for line in fin:
#         line = line.strip()
#         print(line)

class ManagedFile:
    def __init__(self, filename, mode='r'):
        self._filename = filename
        self._mode = mode

    def __enter__(self):
        print('enter...')
        self._opened_file = open(self._filename, self._mode)
        return self._opened_file

    def __exit__(self, *args):
        print('exit...')
        print(args)
        self._opened_file.close()


with ManagedFile('zcourses.txt') as fin:
    for line in fin:
        line = line.strip()
        print(line)

# another example
# https://github.com/openai/openai-cua-sample-app/blob/main/computers/base_playwright.py#L56
# https://github.com/openai/openai-cua-sample-app/blob/main/computers/base_playwright.py#L75
# https://github.com/openai/openai-cua-sample-app/blob/main/cli.py#L69


# In[5]:


print('''

This defines a class ManagedFile that acts as a context manager (i.e., works with the with statement).

Its job is to open a file, let you work with it, and then close it automatically — even if something goes wrong.

''')

print("EXPLANATIONS :")

class ManagedFile:
    def __init__(self, filename, mode='r'):
        self._filename = filename
        self._mode = mode

# This is the constructor. It:
# Stores the file name and open mode ('r' for read, 'w' for write, etc.)
# These are saved to instance variables so they can be used later.

    def __enter__(self):
        print('enter...')
        self._opened_file = open(self._filename, self._mode)
        return self._opened_file

# ✅ __enter__() is called automatically at the start of the with block.
# It prints "enter..." (for demo purposes).
# Opens the file and stores it in self._opened_file.
# Returns the file object so that the with block can use it.
    
    def __exit__(self, *args):
        print('exit...')
        print(args)
        self._opened_file.close()

# __exit__() is called automatically when leaving the with block — even if an exception occurred.
# It prints "exit..." and prints any exception info.
# It closes the file safely.

# ⚠️ The *args typically contain:
# exc_type → type of exception (or None)
# exc_value → the actual exception object
# traceback → traceback object
# If there was no exception, they are all None.

with ManagedFile('zcourses.txt') as fin:
    for line in fin:
        line = line.strip()
        print(line)

# another examples
# https://github.com/openai/openai-cua-sample-app/blob/main/computers/base_playwright.py#L56
# https://github.com/openai/openai-cua-sample-app/blob/main/computers/base_playwright.py#L75
# https://github.com/openai/openai-cua-sample-app/blob/main/cli.py#L69


# In[6]:


print("Another examples of Context Managers :")


# In[7]:


# Simple Timer Context Manager (measure execution time)

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

# When the with Timer(): block starts, Python calls __enter__().

    def __exit__(self, *args):
        self.end = time.time()
        print('Elapsed time:', self.end - self.start)

# ✅ What happens here:
# When the with block ends (whether normally or with an exception), Python calls __exit__().
# self.end = time.time() captures the current time at the end.
# self.end - self.start calculates the time difference (how long the block took).
    
# Usage
with Timer():
    time.sleep(2)  # Simulate some work

# What happens step-by-step:
# Timer().__enter__() is called:
# Starts timing
# Executes time.sleep(2):
# Waits for 2 seconds
# Timer().__exit__() is called:
# Stops timing
# Calculates elapsed time



# In[8]:


# Explanations : 
# Timer.__enter__()
#    → records start time
#    ↓
# Run the code inside the `with` block
#    ↓
# Timer.__exit__()
#    → records end time, prints elapsed time


# In[ ]:





# In[9]:


print("Use of Context Managers :")


# In[10]:


print('''

Example: Acquiring and Releasing a Lock

Suppose you are working in a multi-threaded Python program,
and you need to lock a shared resource so that only one thread accesses it at a time.

✅ You want to:

Acquire a lock before doing something critical

Release it afterward no matter what (even if there’s an error)

✅ This is a perfect job for a context manager.

''')


# In[11]:


print('''

Big takeaway:

Context managers are perfect for managing critical resources
(locks, database connections, file handles, network sockets, etc.)

Threading lock

Database transaction (BEGIN → COMMIT/ROLLBACK)

Open network connection (connect → close)

✅ All of these real-world systems use the same context manager pattern.

''')


# In[12]:


import threading
import time

class LockManager:
    def __init__(self, lock):
        self._lock = lock

    def __enter__(self):
        print("Acquiring lock...")
        self._lock.acquire()     # It acquires the lock → this blocks if another thread is already holding the lock
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing lock...")
        self._lock.release()      # It releases the lock → allowing another thread to enter the critical section.

# Create a global lock
lock = threading.Lock()

# Only one thread at a time can hold it.
# Others must wait.
    
def critical_section(name):
    with LockManager(lock):
        print(f"{name} is doing some work...")
        time.sleep(2)
        print(f"{name} finished work.")


# ✅ When a thread runs this:
# It enters a with LockManager(lock) block.
# This acquires the lock (if available), otherwise waits.
# Prints that it’s doing some work.
# Simulates work by sleeping for 2 seconds.
# Prints that it finished work.
# Exits the block → lock is automatically released.
# ✅ Only one thread can be inside this block at a time!
                          
# Simulate two threads
t1 = threading.Thread(target=critical_section, args=('Thread 1',))
t2 = threading.Thread(target=critical_section, args=('Thread 2',))

t1.start()
t2.start()
t1.join()
t2.join()

# .acquire() and .release() are real methods of Lock objects, and they control when threads can enter and leave critical sections!


# In[ ]:





# In[ ]:




