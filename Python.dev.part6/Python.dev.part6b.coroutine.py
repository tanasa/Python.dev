#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Coroutines :")


# In[2]:


print('''

🧠 What is a Coroutine in Python?

✅ Coroutine = A special kind of generator that can receive data (not just produce it).

✅ Normal generator → produces values (yield).
✅ Coroutine → can also receive values into itself (yield, and send()).

In short:
Generators "pull" values out.
Coroutines can "push" values in.

🎯 How are they different from regular generators?

Feature	Generator	Coroutine
yield	Yes	Yes
send()	No	Yes
Direction	Output only	Input + Output
Purpose	Produce data	Control flows, pipelines, event handling

''')


# In[ ]:





# In[3]:


print('''

Yes! .send() is a method on generator objects in Python —
but it only exists if the generator contains a yield expression that can receive values.

''')

def my_coroutine():
    print('Coroutine started!')
    while True:
        value = yield
        print('Received:', value)

# yield waits for a value to be sent into it.
# send(value) is used to send a value into the coroutine.

coro = my_coroutine()   # Create the coroutine (does not run yet)
next(coro)              # Prime it (move to first yield)

coro.send(10)           # Output: Received: 10
coro.send(20)           # Output: Received: 20
coro.send('hello')      # Output: Received: hello

print('''

📢 Important:

Before sending a value with send(), you must prime the coroutine by calling next(coro) first.
(Otherwise, you get a TypeError: can't send non-None value to a just-started generator.)

After that, send() resumes the coroutine and injects data where the yield is.
''')


# In[4]:


print('''

📚 Short Summary:

Concept	Meaning
Generator	Function that produces data lazily (yield)
Coroutine	Function that can receive data dynamically (yield + send())

✅ Coroutines are great for asynchronous programming, pipelines, event-driven systems, and managing state.
✅ In modern Python, async def and await are built on coroutines!

🧠 Let's be super clear:

When you create a generator (any function with yield inside),
the resulting object has these methods:

Method	What it does
.next()	Advances to the next yield
.send(value)	Sends a value into the generator at the point of yield
.throw()	Throws an exception inside the generator
.close()	Terminates the generator

''')

print('''

📢 So:
✅ You successfully sent the value 42.
✅ It printed "Got: 42".
✅ After that, since there are no more instructions, Python raised StopIteration.

''')



def my_gen():
    x = yield   # yield with ability to receive a value
    print('Got:', x)

g = my_gen()   # Create generator object
next(g)        # Prime it (run until first yield)

# g.send(42)     # Send 42 into the generator
# 🔥 How to avoid StopIteration crashing your code :

try:
    g.send(42)
except StopIteration:
    pass  # It's normal, generator finished

# 🔥 How to avoid StopIteration crashing your code :

def my_gene():
    while True:
        x = yield
        print('Got:', x)

g = my_gene()
next(g)  # Prime it

g.send(42)   # Got: 42
g.send(77)   # Got: 77
g.send('hello')  # Got: hello


# In[ ]:





# In[5]:


print("Pipelines of co-routines:")


# In[ ]:





# In[6]:


# in the input file : zcourses.txt

# Network Fundamentals
# Computer Networking Essentials*, 3 units
# Switching and Routing, 3 units
# TCP/IP Essentials, 2 units
# Wireless Communications and Mobile Antenna Design, Introduction, 3 units

# Linux System Administration
# Linux, Introduction, 2.5 units
# Linux System and Network Administration*, 3 units
# Linux System Performance in the Cloud and Data Center, 3 units
# Linux Systems Programming, 3 units
# Relational Database Design and SQL Programming*, 3 units
# Perl Programming, Comprehensive, 2 units
# Python for Programmers, 3 units  


# In[7]:


# The pipeline of coroutines :

# Strips newline characters
# Splits each line into title and units
# Sends:
# course titles to one coroutine to detect core courses (marked with *)
# unit strings to another coroutine to add total units
# Prints everything


# In[ ]:





# In[8]:


# ✅ Waits for values sent in via .send(line), then prints them.

def printer():
    try:
        while True:
            line = yield
            print(line)
    except GeneratorExit:
        print('printer finished')

# ✅ Waits for lines, strips newline/whitespace, and forwards the clean line to another coroutine (cr).

def new_line_remover(cr):
    next(cr)
    try:
        while True:
            line = yield
            line = line.strip()
            cr.send(line)
    except GeneratorExit:
        print('new_line_remover finished')
        cr.close()

# ✅ Splits each incoming line using the given delimiter (,).
# ✅ Sends the first part (e.g. course name) to cr1, and the second part (e.g. units) to cr2.

def separator(delimiter, cr1, cr2):
    next(cr1)
    next(cr2)
    try:
        while True:
            line = yield
            try:
                pos = line.rindex(delimiter)
                part1 = line[:pos].strip()
                part2 = line[pos + 1:].strip()
                cr1.send(part1)
                cr2.send(part2)
            except ValueError:
                pass
    except GeneratorExit:
        print('separator finished')
        cr1.close()
        cr2.close()

# ✅ If a title ends with *, it’s a core course — add to a list.
# ✅ At the end (on .close()), it sends the list of core courses to the next coroutine.

def core_course_checker(marker, cr):
    core_course_list = []
    next(cr)
    try:
        while True:
            title = yield
            if title.endswith(marker):
                core_course_list.append(title)
    except GeneratorExit:
        print('core_course_checker finished')
        cr.send(str(core_course_list))
        cr.close()

# ✅ Extracts the numeric part from strings like "4 units" and sums them.
# ✅ At the end, sends a message like "Total units: 12" to the next coroutine.

def unit_adder(cr):
    total = 0
    next(cr)

    try:
        while True:
            units = yield
            try:
                total += float(units.split()[0])
            except ValueError:
                pass
    except GeneratorExit:
        print('unit_adder finished')
        cr.send('Total units: {}'.format(total))
        cr.close()


# ✅ printer() is the end of the chain (gets final outputs).
# ✅ core_course_checker and unit_adder send their results there at the end.
# ✅ separator() splits lines into (title, units) → each goes down one of the branches.
# ✅ new_line_remover() is the first stage: strips whitespace before splitting.
    
processor = new_line_remover(
    separator(
        ',',
        core_course_checker('*', printer()),
        unit_adder(printer())
    )
)
next(processor)

# processor is a coroutine.
# processor is the HEAD of the coroutine pipeline.
# You send data into it, and it handles the whole chain.

with open('zcourses.txt') as fin:
    for line in fin:
        processor.send(line)

    processor.close()

# ✅ This sends each input line into the coroutine pipeline, and it flows through:
# new_line_remover
# separator
# core_course_checker and unit_adder
# printer
# ✅ Until everything is processed and printed!


# In[ ]:





# In[ ]:




