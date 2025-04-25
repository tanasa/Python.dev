.. code:: ipython3

    print(''' 
    
    About Dictionaries :
    
    dict get: [key]
    dict.get('key', default_value): safe access : return default_value if key does not exist
    
    dict set: [key] = value
    dict.setdefault('key', default_value): create a new key-value pair using default value if key does not exist
    
    in : to check if key exists
    
    ''')


.. parsed-literal::

     
    
    About Dictionaries :
    
    dict get: [key]
    dict.get('key', default_value): safe access : return default_value if key does not exist
    
    dict set: [key] = value
    dict.setdefault('key', default_value): create a new key-value pair using default value if key does not exist
    
    in : to check if key exists
    
    
    

.. code:: ipython3

    # Note  1

.. code:: ipython3

    # The underscore in sum_ is just used to avoid naming conflict with the built-in sum() function
    
    def sum_ave(numbers):
        sum_ = sum(numbers)
        ave = sum_ / len(numbers)
        return sum_, ave
    
    
    result = sum_ave([7, 4, 12, 18, 3, 2, 5])
    print(result)
    # (s, a) = result
    
    # The result is unpacked into variables s and a
    s, a = sum_ave([7, 4, 12, 18, 3, 2, 5])
    print(s, a)
    
    # An alternative :
    
    print(result[0], result[1])


.. parsed-literal::

    (51, 7.285714285714286)
    51 7.285714285714286
    51 7.285714285714286
    

.. code:: ipython3

    # Note 2
    print("Functions and arguments :")


.. parsed-literal::

    Functions and arguments :
    

.. code:: ipython3

    print('''
    
    The * before numbers means the function accepts any number of arguments.
    These arguments are automatically grouped into a tuple named numbers.
    
    ''')
    
    def sum_ave(*numbers):
        print(type(numbers))
        
        sum_ = sum(numbers)
        ave = sum_ / len(numbers)
        return sum_, ave
    
    
    s, a = sum_ave(7, 4, 12, 18, 3, 2, 5)
    print(s, a)
    s, a = sum_ave(7, 4, 12)
    print(s, a)


.. parsed-literal::

    
    
    The * before numbers means the function accepts any number of arguments.
    These arguments are automatically grouped into a tuple named numbers.
    
    
    <class 'tuple'>
    51 7.285714285714286
    <class 'tuple'>
    23 7.666666666666667
    

.. code:: ipython3

    # Note 3
    print("Functions and arguments :")
    print("Positional and Keyword arguments")


.. parsed-literal::

    Functions and arguments :
    Positional and Keyword arguments
    

.. code:: ipython3

    # Define a function that takes three required positional or keyword arguments: a, b, c
    
    def calculate(a, b, c):
        # Returns the result of: a cubed + b squared + c
        return a**3 + b**2 + c
    
    print(calculate(1, 2, 3))
    print(calculate(2, 3, 1))
    
    print(calculate(b=2, c=3, a=1))


.. parsed-literal::

    8
    18
    8
    

.. code:: ipython3

    # Define a function that takes two required arguments (a, b)
    # and any number of additional arguments (*c)
    
    def my_sum(a, b, *c):
        print(type(c))  # This will always print: <class 'tuple'>
        
        # Calculate a weighted sum:
        # 10 times 'a', plus 5 times 'b', plus the sum of any extra arguments in 'c'
        return 10 * a + 5 * b + sum(c)
    
    # Call with multiple extra arguments
    # a = 10, b = 3, c = (4, 8, 13)
    # Result = 10*10 + 5*3 + (4 + 8 + 13) = 100 + 15 + 25 = 140
    print(my_sum(10, 3, 4, 8, 13))  # Output: 140
    
    # Call with only a and b (no extras)
    # a = 10, b = 3, c = () (empty tuple)
    # Result = 10*10 + 5*3 = 100 + 15 = 115
    print(my_sum(10, 3))  # Output: 115


.. parsed-literal::

    <class 'tuple'>
    140
    <class 'tuple'>
    115
    

.. code:: ipython3

    # Define a function with a default value for 'c'
    # If 'c' is not provided in the function call, it will default to 10
    
    def calculate(a, b, c = 10):
        return a**3 + b**2 + c
    
    print(calculate(1, 2, 3))
    print(calculate(1, 2))


.. parsed-literal::

    8
    15
    


.. code:: ipython3

    print('''
    
    🧩 *args vs **kwargs in Python
    
    Feature	                    *args	                                         **kwargs
    Name stands for	            “arguments”	                                     “keyword arguments”
    Type	                     Tuple (TUPLE)	                                  Dictionary (DICTIONARY)
    Accepts	Extra positional arguments	                                          Extra keyword arguments
    Use case	                When number of positional arguments is unknown	  When number of named arguments is unknown
    
    ''')


.. parsed-literal::

    
    
    🧩 *args vs **kwargs in Python
    
    Feature	                    *args	                                         **kwargs
    Name stands for	            “arguments”	                                     “keyword arguments”
    Type	                     Tuple (TUPLE)	                                  Dictionary (DICTIONARY)
    Accepts	Extra positional arguments	                                          Extra keyword arguments
    Use case	                When number of positional arguments is unknown	  When number of named arguments is unknown
    
    
    

.. code:: ipython3

    # ✅ Example: *args
    
    def greet(*args):
        for name in args:
            print(f"Hello, {name}!")
    
    greet('Alice', 'Bob', 'Charlie')  # args is a tuple: ('Alice', 'Bob', 'Charlie')


.. parsed-literal::

    Hello, Alice!
    Hello, Bob!
    Hello, Charlie!
    

.. code:: ipython3

    # ✅ Example: **kwargs
    
    def show_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    show_info(name="Bogdan", age=34, country="USA") # kwargs is a dictionary: {'name': 'Bogdan', 'age': 34, 'country': 'USA'}


.. parsed-literal::

    name: Bogdan
    age: 34
    country: USA
    

.. code:: ipython3

    # ✅ Both Together
    
    def example(a, *args, **kwargs):
        print("a:", a)
        print("args:", args)
        print("kwargs:", kwargs)
    
    example(1, 2, 3, name="Alice", age=25)
    
    print('''
    
    🧠 How to Think About It:
    
    You Write This...	You Get This...
    func(1, 2, 3)	*args → (2, 3)
    func(name="Alice", age=30)	**kwargs → {'name': 'Alice', 'age': 30}
    
    ''')
    
    # You can't use *args after **kwargs — Python will throw a syntax error.


.. parsed-literal::

    a: 1
    args: (2, 3)
    kwargs: {'name': 'Alice', 'age': 25}
    
    
    🧠 How to Think About It:
    
    You Write This...	You Get This...
    func(1, 2, 3)	*args → (2, 3)
    func(name="Alice", age=30)	**kwargs → {'name': 'Alice', 'age': 30}
    
    
    

.. code:: ipython3

    # Unpacking when calling a function
    
    def greet(name, age, city):
        print(f"{name} is {age} years old and lives in {city}.")
    
    args = ("Alice", 28, "Paris")
    greet(*args)  # Unpacks tuple
    
    kwargs = {"name": "Bob", "age": 32, "city": "London"}
    greet(**kwargs)  # Unpacks dictionary
    
    print('''
    
    Summary Cheat Sheet:
    
    Syntax	            Use
    *args	            Accepts any number of positional arguments
    **kwargs	        Accepts any number of keyword arguments
    *args in call	    Unpacks a tuple/list into positional args
    **kwargs in call	Unpacks a dict into keyword args
    
    ''')


.. parsed-literal::

    Alice is 28 years old and lives in Paris.
    Bob is 32 years old and lives in London.
    
    
    Summary Cheat Sheet:
    
    Syntax	            Use
    *args	            Accepts any number of positional arguments
    **kwargs	        Accepts any number of keyword arguments
    *args in call	    Unpacks a tuple/list into positional args
    **kwargs in call	Unpacks a dict into keyword args
    
    
    


.. code:: ipython3

    print("One of the most common and sneaky Python pitfalls : using a mutable default argument (like a list or dictionary)")


.. parsed-literal::

    One of the most common and sneaky Python pitfalls : using a mutable default argument (like a list or dictionary)
    

.. code:: ipython3

    # The default value `arr=[]` is created ONCE, when the function is defined
    # It is NOT re-created with each call — it is shared across calls!
    
    def add_to(val, arr=[]):
        arr.append(val)  # This modifies the same list every time if no new list is passed
        return arr
    
    print(add_to(10))  # [10]
    print(add_to('a'))  # [10, 'a'] ← builds on the same list!
    
    # This behavior is unexpected for many programmers:
    # We expect add_to(10) to return [10]
    # Then add_to('a') to return ['a']
    # Instead, it keeps appending to the same list!


.. parsed-literal::

    [10]
    [10, 'a']
    

.. code:: ipython3

    print('''
    
    Key Takeaways :
    
    Mistake	                         Safer Practice
    def func(x, mylist=[])	         def func(x, mylist=None)
    Shared across function calls	 New list created every time when needed
    Leads to hard-to-track bugs	     Predictable, isolated behavior
    
    ''')


.. parsed-literal::

    
    
    Key Takeaways :
    
    Mistake	                         Safer Practice
    def func(x, mylist=[])	         def func(x, mylist=None)
    Shared across function calls	 New list created every time when needed
    Leads to hard-to-track bugs	     Predictable, isolated behavior
    
    
    


.. code:: ipython3

    # How to fix add_to() ?
    # so that every time I call add_to, it creates an empty list
    # and eventually returns a list with a single value of val
    
    print('''
    
    Why this works:
    
    arr=None avoids using a mutable object (like []) as a default argument.
    
    if arr is None: ensures a new list is created on each function call, if one wasn’t provided.
    
    ✅ This is the correct and safe way to use mutable defaults in Python.
    
    ''')
    
    def add_to_fixed(val, arr=None):
        if arr is None:
            arr = []
        arr.append(val)
        return arr
    
    
    print('-' * 80)
    print(add_to_fixed(3, ['a', 'b'])) # ['a', 'b', 3]
    print(add_to_fixed(10)) # [10]
    print(add_to_fixed('a'))
    
    print('''
    
    This illustrates the danger of using arr=[] as a default:
    
    The same list is used and modified across multiple calls.
    
    This leads to unexpected results like ['a', 10, 2], even though the user didn’t pass any list!
    
    ''')
    
    print('=' * 80)
    add_to(10)
    add_to('a')
    
    arr2 = add_to(2)
    print(arr2) # [10, 'a', 2]
    
    arr2.pop()
    print(add_to(4)) # [10, 'a', 4]
    
    # It shows the danger of using mutable default value
    # because the default value internal to the function object
    # is exposed and can be changed by the outside world
    
    print('''
    
    Behavior                    | add_to(val, arr=[])                     | add_to_fixed(val, arr=None)
    Creates new list each time? | ❌ No — reuses the same list |          ✅ Yes — creates a new one only when needed
    Safe and expected?          | ❌ No — prone to subtle bugs |          ✅ Yes — reliable and clean
    
    ''')


.. parsed-literal::

    
    
    Why this works:
    
    arr=None avoids using a mutable object (like []) as a default argument.
    
    if arr is None: ensures a new list is created on each function call, if one wasn’t provided.
    
    ✅ This is the correct and safe way to use mutable defaults in Python.
    
    
    --------------------------------------------------------------------------------
    ['a', 'b', 3]
    [10]
    ['a']
    
    
    This illustrates the danger of using arr=[] as a default:
    
    The same list is used and modified across multiple calls.
    
    This leads to unexpected results like ['a', 10, 2], even though the user didn’t pass any list!
    
    
    ================================================================================
    [10, 'a', 10, 'a', 2]
    [10, 'a', 10, 'a', 4]
    
    
    Behavior                    | add_to(val, arr=[])                     | add_to_fixed(val, arr=None)
    Creates new list each time? | ❌ No — reuses the same list |          ✅ Yes — creates a new one only when needed
    Safe and expected?          | ❌ No — prone to subtle bugs |          ✅ Yes — reliable and clean
    
    
    


.. code:: ipython3

    # Zip and unpack :
    
    names = ['Alice', 'Bob', 'Charles', 'David']
    ages = [18, 25, 22, 20]
    schools = ['Stanford', 'UCSC', 'Berkeley']
    
    result = list(zip(names, ages, schools))
    print(result)
    
    for name, age, school in zip(names, ages, schools):
        print(name, age, school, sep=':')
    
    prefix_sum_before = [26, 59, 78, 108]
    prefix_sum_after = [53, 61, 89, 129]
    
    diff = [a - b for a, b in zip(prefix_sum_after, prefix_sum_before)]
    print(diff)
    
    def is_abecedarian(word):
        for curr, next_ in zip(word[:-1], word[1:]):
            if curr > next_:
                return False
    
        return True
    
    print(is_abecedarian('accept'))
    print(is_abecedarian('brother'))


.. parsed-literal::

    [('Alice', 18, 'Stanford'), ('Bob', 25, 'UCSC'), ('Charles', 22, 'Berkeley')]
    Alice:18:Stanford
    Bob:25:UCSC
    Charles:22:Berkeley
    [27, 2, 11, 21]
    True
    False
    


.. code:: ipython3

    # Read student's scores and grade to check if they are consistent
    
    # grading policy:
    
    def assign_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    def validate(record):
        name, sid, *scores, grade = record.split(',') # The *scores "soaks up" the middle part, no matter how many scores are there.
        scores = [int(score) for score in scores]
        avg = sum(scores) / len(scores)
        actual_grade = assign_grade(avg)
        return name, sid, actual_grade == grade
    
    # *var	Collect the rest of the values into a list
    
    with open('zstudents.csv') as fin:
        for line in fin:
            record = line.strip()
            name, sid, valid = validate(record)
            if not valid:
                print(name, sid)


.. parsed-literal::

    Bob 1234
    David 1235
    Frank 1237
    


.. code:: ipython3

    # Generate A list of fruits sorted by name length (shortest to longest).
    
    fruits = ['grape', 'apple', 'orange', 'pear', 'strawberry', 'kiwi', 'apricot']
    print(sorted(fruits))
    
    fruits_length = map(len, fruits)      #  it returns a LAZY map object that computes the length of each fruit name.
                                          #  it doesn’t compute anything right away.
    print(list(fruits_length))            #  After this line, the fruits_length has been consumed — it's now empty !!!
    
    fruits_with_length = zip(fruits_length, fruits)  # zip() pairs each fruit’s length with the fruit name.
                                                     # zip() also creates a LAZY iterator.
                                                     # But more importantly: fruits_length is already used up!
                                                     # So you're effectively zipping an empty iterator with fruits, which gives an empty result.
                                                     # And printing the zip object itself gives a memory address like: <zip object at 0x0000019257A26740>
    print(fruits_with_length)
    
    sorted_fruits_by_length = sorted(fruits_with_length)
    print(sorted_fruits_by_length)
    
    sorted_fruits = map(lambda entry: entry[-1], sorted_fruits_by_length)
    print(list(sorted_fruits))


.. parsed-literal::

    ['apple', 'apricot', 'grape', 'kiwi', 'orange', 'pear', 'strawberry']
    [5, 5, 6, 4, 10, 4, 7]
    <zip object at 0x0000021E3B417F00>
    []
    []
    

.. code:: ipython3

    # How to Fix It
    # Either don’t consume the map() before using it, or store it as a list early on:
    
    fruits = ['grape', 'apple', 'orange', 'pear', 'strawberry', 'kiwi', 'apricot']
    
    # Convert the map to a list immediately so it can be reused
    fruits_length = list(map(len, fruits))
    print(fruits_length)  # Now safe to print
    
    # Use the list of lengths for zip
    fruits_with_length = list(zip(fruits_length, fruits))  # Convert to list to see contents
    print(fruits_with_length)
    
    sorted_fruits_by_length = sorted(fruits_with_length)
    print(sorted_fruits_by_length)
    
    sorted_fruits = list(map(lambda entry: entry[-1], sorted_fruits_by_length)) # entry[-1] grabs the fruit name.
    print(sorted_fruits)                                                        # map(lambda e: e[-1], ...)	Extracts just the names in sorted order


.. parsed-literal::

    [5, 5, 6, 4, 10, 4, 7]
    [(5, 'grape'), (5, 'apple'), (6, 'orange'), (4, 'pear'), (10, 'strawberry'), (4, 'kiwi'), (7, 'apricot')]
    [(4, 'kiwi'), (4, 'pear'), (5, 'apple'), (5, 'grape'), (6, 'orange'), (7, 'apricot'), (10, 'strawberry')]
    ['kiwi', 'pear', 'apple', 'grape', 'orange', 'apricot', 'strawberry']
    

.. code:: ipython3

    print('''
    
    What is Lazy Evaluation?
    
    Lazy evaluation means:
    
    "Don’t compute anything until you absolutely need the result."
    
    In Python, many built-in functions like map(), zip(), filter(), and even range() (in Python 3) return lazy objects — 
    also known as iterators or generators.
    
    They don’t perform work immediately, but instead wait until you loop over them, or convert them to a list or tuple.
    
    ✅ Why Use Lazy Evaluation?
    
    Benefit	Explanation :
    💾 Memory-efficient	Doesn’t store all items in memory (great for big data)
    ⚡ Faster to create	Just sets up the logic, doesn’t compute right away
    🔄 Reusable logic	Useful for streams or pipelines where only part of the data is needed
    
    ''')
    
    # Examples of Lazy Functions
    
    # 1. map() : applies a function to each item, but doesn't do it until you ask for it:
    
    squares = map(lambda x: x**2, [1, 2, 3])
    print(squares)         # <map object at ...>
    print(list(squares))   # [1, 4, 9]
    
    # 2. zip()
    # Pairs up elements lazily:
    
    z = zip([1, 2], ['a', 'b'])
    print(z)              # <zip object at ...>
    print(list(z))        # [(1, 'a'), (2, 'b')]
    
    # 3. range() (Python 3+)
    # Doesn't generate all numbers at once:
    
    r = range(1000000)
    print(r)              # range(0, 1000000)
    print(list(r[:5]))    # [0, 1, 2, 3, 4]
    
    # 🚨 Gotchas with Lazy Evaluation
    # They can be used only once:
    
    z = zip([1, 2], [3, 4])
    print(list(z))   # [(1, 3), (2, 4)]
    print(list(z))   # [] ← already consumed!
    
    # You must convert them to see results:
    
    f = map(str.upper, ['apple', 'banana'])
    print(f)          # <map object ...>
    print(list(f))    # ['APPLE', 'BANANA']


.. parsed-literal::

    
    
    What is Lazy Evaluation?
    
    Lazy evaluation means:
    
    "Don’t compute anything until you absolutely need the result."
    
    In Python, many built-in functions like map(), zip(), filter(), and even range() (in Python 3) return lazy objects — 
    also known as iterators or generators.
    
    They don’t perform work immediately, but instead wait until you loop over them, or convert them to a list or tuple.
    
    ✅ Why Use Lazy Evaluation?
    
    Benefit	Explanation :
    💾 Memory-efficient	Doesn’t store all items in memory (great for big data)
    ⚡ Faster to create	Just sets up the logic, doesn’t compute right away
    🔄 Reusable logic	Useful for streams or pipelines where only part of the data is needed
    
    
    <map object at 0x0000021E3B0F58D0>
    [1, 4, 9]
    <zip object at 0x0000021E3B3FF140>
    [(1, 'a'), (2, 'b')]
    range(0, 1000000)
    [0, 1, 2, 3, 4]
    [(1, 3), (2, 4)]
    []
    <map object at 0x0000021E3B3E9330>
    ['APPLE', 'BANANA']
    

.. code:: ipython3

    print('''
    
    Are all generators and iterators lazy?
    ✅ Yes — by definition, generators and iterators in Python are lazy.
    
    That means:
    
    They do not compute or store values all at once — they compute and return values one at a time, on demand.
    
    🧠 Let's break it down:
    
    🔁 What is an iterator?
    
    An iterator is any object in Python that:
    
    Implements the __iter__() and __next__() methods
    
    Delivers one item at a time
    
    Remembers where it left off
    
    Raises StopIteration when it’s out of items
    
    ✅ All built-in lazy tools like map(), zip(), filter(), and range() (in Python 3) are iterators.
    
    🔥 What is a generator?
    
    A generator is a special type of iterator, created by:
    
    A function using yield
    
    Or a generator expression, like (x*x for x in range(10))
    
    Generators are:
    
    Automatically lazy
    
    Use less memory
    
    Pause after each yield and resume later.
    
    ''')


.. parsed-literal::

    
    
    Are all generators and iterators lazy?
    ✅ Yes — by definition, generators and iterators in Python are lazy.
    
    That means:
    
    They do not compute or store values all at once — they compute and return values one at a time, on demand.
    
    🧠 Let's break it down:
    
    🔁 What is an iterator?
    
    An iterator is any object in Python that:
    
    Implements the __iter__() and __next__() methods
    
    Delivers one item at a time
    
    Remembers where it left off
    
    Raises StopIteration when it’s out of items
    
    ✅ All built-in lazy tools like map(), zip(), filter(), and range() (in Python 3) are iterators.
    
    🔥 What is a generator?
    
    A generator is a special type of iterator, created by:
    
    A function using yield
    
    Or a generator expression, like (x*x for x in range(10))
    
    Generators are:
    
    Automatically lazy
    
    Use less memory
    
    Pause after each yield and resume later.
    
    
    

.. code:: ipython3

    print('''
    
    Key Python Concept Used
    
    setdefault(key, default_value)
    → If key is already in the dictionary, do nothing.
    → If key is missing, insert it with the provided default_value.
    
    ''')


.. parsed-literal::

    
    
    Key Python Concept Used
    
    setdefault(key, default_value)
    → If key is already in the dictionary, do nothing.
    → If key is missing, insert it with the provided default_value.
    
    
    

.. code:: ipython3

    # dict.setdefault(key, default)
    
    # Problem : 
    
    # Checks if the key exists in the dictionary.
    # If it does, it returns the existing value.
    
    # If it doesn't, it:
    # Inserts the key with the given default value
    
    # Returns that default value
    # dict.setdefault(key, default_value)

.. code:: ipython3

    # Part 1: Count the frequency of each letter
    # return a dict with letter -> freq
    
    def letter_count(word):
        result = {}
        for letter in word:
            # if letter in result:
            #     result[letter] += 1
            # else:
            #     result[letter] = 1
            result.setdefault(letter, 0)
            result[letter] += 1
        return result
    
    
    word = "pneumonoultramicroscopicsilicovolcanoconiosis"
    freqs = letter_count(word)
    
    print("Frequency :")
    print(freqs)
    
    # {
    #   "p": 2,
    #   "n": 4,
    #   "e": 1,
    #   "u": 2,
    #   "m": 2,
    #   "o": 9,
    #   "l": 3,
    #   "t": 1,
    #   "r": 2,
    #   "a": 2,
    #   "i": 6,
    #   "c": 6,
    #   "s": 4,
    #   "v": 1
    # }
    
    # Part 2: Invert the frequency dictionary
    # reverse table: freq -> [letters]
    # {
    #   6: ['i', 'c']
    # }
    
    # d: key -> value
    # return: value -> [keys]
    
    # Build a new dictionary where:
    # The keys are the values from the original dictionary (e.g., frequency counts like 2, 3, 1).
    # The values are lists of keys from the original dictionary that shared that frequency.
    # In short: reverse key and value
    
    def get_reverse(d):
        result = {}
    
        for key, value in d.items():
            result.setdefault(value, [])
            result[value].append(key)
    
        return result
    
    # print("Reverse lookup :")
    reversed_lookup = get_reverse(freqs)
    print("Reverse lookup :")
    print(reversed_lookup)
    
    # {2: ['p', 'u', 'm', 'r', 'a'], 4: ['n', 's'], 1: ['e', 't', 'v'], 9: ['o'], 3: ['l'], 6: ['i', 'c']}
    
    # In Python, iterating over a dictionary (like in for key in dict) only looks at the keys — not the values.
    # sorted(reversed_lookup) automatically sorts the dictionary's keys (NOT its values).
    
    sorted_freqs = sorted(reversed_lookup, reverse=True)
    print(sorted_freqs)
    
    print('Most frequent letters: {}'.format(reversed_lookup[sorted_freqs[0]]))
    print('Second most frequent letters: {}'.format(reversed_lookup[sorted_freqs[1]]))
    print('Third most frequent letters: {}'.format(reversed_lookup[sorted_freqs[2]]))
    print('Least frequent letters: {}'.format(reversed_lookup[sorted_freqs[-1]]))


.. parsed-literal::

    Frequency :
    {'p': 2, 'n': 4, 'e': 1, 'u': 2, 'm': 2, 'o': 9, 'l': 3, 't': 1, 'r': 2, 'a': 2, 'i': 6, 'c': 6, 's': 4, 'v': 1}
    Reverse lookup :
    {2: ['p', 'u', 'm', 'r', 'a'], 4: ['n', 's'], 1: ['e', 't', 'v'], 9: ['o'], 3: ['l'], 6: ['i', 'c']}
    [9, 6, 4, 3, 2, 1]
    Most frequent letters: ['o']
    Second most frequent letters: ['i', 'c']
    Third most frequent letters: ['n', 's']
    Least frequent letters: ['e', 't', 'v']
    

