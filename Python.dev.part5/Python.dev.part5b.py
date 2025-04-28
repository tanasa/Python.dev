#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print("Classes: Getters abd Setters")


# In[2]:


class Person:
    def __init__(self, name, age, ssn):
        self._name = name
        self._age = age
        self.__ssn = ssn

    def _get_name(self):
        return self._name

    def _get_age(self):
        return self._age

    def _set_age(self, age):
        # data validation
        if age > 0 and age > self._age:
            self._age = age

    def _get_ssn(self):
        # data mask
        return '***-**-{}'.format(self.__ssn[-4:])

    def _del_ssn(self):
        print('ssn will be deleted')
        del self.__ssn

    name = property(fget=_get_name)
    age = property(fget=_get_age, fset=_set_age)
    ssn = property(fget=_get_ssn, fdel=_del_ssn)

if __name__ == '__main__':
    
    john = Person('John', 18, '123-45-6789')
    print(john.name)
    print(john.age)
    john.age = 20
    print(john.age)
    
    john.age = -5   # No effect
    print(john.age)
    # print(john.ssn)

    del john.ssn
    # print(john.ssn)


    print(john._get_name())
    print(john._get_age())
    john._set_age(20)
    print(john._get_age())
    
    john._set_age(-5)
    print(john._get_age())
    # print(john.get_ssn())


# In[3]:


class Person:
    def __init__(self, name, age, ssn):
        self._name = name
        self._age = age
        self.__ssn = ssn

    # 1. Create 'name' property with getter only
    @property
    def name(self):
        return self._name

    # (No setter for name — it’s read-only)

    # 2. Create 'age' property with getter
    @property
    def age(self):
        return self._age

    # Attach a setter to 'age'
    @age.setter
    def age(self, value):
        if value > 0 and value > self._age:
            self._age = value

    # 3. Create 'ssn' property with getter
    @property
    def ssn(self):
        return '***-**-{}'.format(self.__ssn[-4:])

    # Attach a deleter to 'ssn'
    @ssn.deleter
    def ssn(self):
        print('SSN will be deleted')
        del self.__ssn


if __name__ == '__main__':
    john = Person('John', 18, '123-45-6789')

    # Accessing name (getter)
    print(john.name)

    # Accessing and setting age (getter + setter)
    print(john.age)
    john.age = 20
    print(john.age)

    john.age = -5  # Invalid update (ignored)
    print(john.age)

    # Accessing masked SSN (getter)
    print(john.ssn)

    # Deleting SSN (deleter)
    del john.ssn

    # After deletion, next access would raise AttributeError if uncommented
    # print(john.ssn)


# In[4]:


print('''

BONUS: If you split into separate functions : Suppose you want to split getter into a separate method —
then you would write @<property_name>.getter explicitly.

''')

class Person:
    def __init__(self, name, age, ssn):
        self._name = name
        self._age = age
        self.__ssn = ssn

    # -------- NAME --------
    def _get_name(self):
        print("Getting name...")
        return self._name

    @property
    def name(self):
        return self._get_name()

    @name.getter
    def name(self):
        print("Accessing name through @name.getter...")
        return self._name

    # No setter for name (it's read-only)

    # -------- AGE --------
    def _get_age(self):
        print("Getting age...")
        return self._age

    def _set_age(self, new_age):
        print(f"Trying to set age to {new_age}...")
        if new_age > 0 and new_age > self._age:
            self._age = new_age
            print("Age updated successfully.")
        else:
            print("Invalid age. No update.")

    @property
    def age(self):
        return self._get_age()

    @age.getter
    def age(self):
        print("Accessing age through @age.getter...")
        return self._age

    @age.setter
    def age(self, value):
        self._set_age(value)

    # -------- SSN --------
    def _get_ssn(self):
        return '***-**-{}'.format(self.__ssn[-4:])

    def _del_ssn(self):
        print('Deleting SSN...')
        del self.__ssn

    @property
    def ssn(self):
        return self._get_ssn()

    @ssn.getter
    def ssn(self):
        print("Accessing SSN through @ssn.getter...")
        return '***-**-{}'.format(self.__ssn[-4:])

    @ssn.deleter
    def ssn(self):
        self._del_ssn()


# --- RUN ---
if __name__ == '__main__':
    john = Person('John', 18, '123-45-6789')

    # Name
    print(john.name)  # Access name

    # Age
    print(john.age)   # Access age
    john.age = 20     # Update age
    print(john.age)

    john.age = -5     # Invalid age
    print(john.age)

    # SSN
    print(john.ssn)   # Access masked SSN
    del john.ssn      # Delete SSN

    # Try accessing deleted SSN (will raise AttributeError)
    # print(john.ssn)


# We can re-write the code by using :
# @property for creating the property ✅
# @<property_name>.setter for setting ✅
# @<property_name>.deleter for deleting ✅
# No need for separate .getter decorators!
# clean, compact version focusing only on property + setter + deleter.

# Getter is automatically provided when you write @property.
# Setter is added with @property_name.setter.
# Deleter is added with @property_name.deleter.
# No need to manually define .getter unless you want special behavior.


# In[ ]:





# In[5]:


print("Class Variables:")


# In[ ]:





# In[6]:


print("Shadowing :")


# In[7]:


print('''

Shadowing happens when:

An object or function hides another object or function with the same name in a more local (closer) scope.

In our example:

Foo.c is a class variable.

When you write f.c = 5, you create an instance variable named c for the object f.

Now, whenever you access f.c, Python finds the instance variable first : it shadows the class variable Foo.c.

f.c (instance) SHADOWS Foo.c (class).

''')

print('''

Python looks for attributes in this order:

First, in the instance (like f.__dict__)
Then, in the class (like Foo.__dict__)
Then, in the parent classes (if any)

If it finds a matching name earlier (at the instance level), it stops searching - that is shadowing.

''')


# In[8]:


class Foo:

    c = 10  # class variable

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        return self.a + self.b + Foo.c


if __name__ == '__main__':
    f = Foo(1, 2)
    print(f.a)
    print(f.b)
    print(f.c)
    print(Foo.c)
    print(f.calc())

    print('=' * 40)

    f.c = 5  # add an instance variable c to f,
             # which shadows the class variable Foo.c, for that object only.
    print(f.c)
    print(Foo.c)
    print(f.calc()) # Thus, no matter what f.c is,
                    # calc() will always use Foo.c (10), not the instance variable!


# ✅ The final value of f.calc() is 13.
# ✅ Shadowing f.c does not affect calc(), because calc() uses Foo.c directly.


# In[9]:


# Let’s now see what happens if you change calc() to use self.c instead of Foo.c.
# ✅ Notice: calc() now uses self.c instead of Foo.c.

class Foo:
    c = 10  # class variable

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        return self.a + self.b + self.c   # <--- Now using self.c


f = Foo(1, 2)

print(f.a)   # ➔ 1
print(f.b)   # ➔ 2
print(f.c)   # ➔ 10 (from Foo.c)
print(Foo.c) # ➔ 10
print(f.calc())

# Now shadowing: SHADOWING : 

f.c = 5  # Create instance variable f.c
# Foo.c = 10 (class — still unchanged)

print(f.c)    # ➔ 5 (instance c)
print(Foo.c)  # ➔ 10 (class c)
print(f.calc())

# Inside calc() now:
# return self.a + self.b + self.c
# = 1 + 2 + 5
# = 8

# Key Point
# Version of calc()	Result
# return self.a + self.b + Foo.c	Always 13 (uses class variable, no shadowing effect)
# return self.a + self.b + self.c	13 before shadowing, 8 after shadowing (instance variable c overrides class variable)


# In[10]:


print('''

Final Conclusion:

If you use Foo.c inside calc(), it always uses the class variable (shadowing doesn't matter).

If you use self.c inside calc(), shadowing directly changes what calc() computes!

✅ Changing from Foo.c → self.c makes the object behave more dynamically based on its local attributes.

''')


# In[11]:


# If you modify the class variable itself (through the class, not through an instance),
# all instances that have NOT shadowed it will see the new value.
# ✅ Because class variables are shared across instances unless shadowed.

class Foo:
    c = 10  # Class variable

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        return self.a + self.b + self.c  # Using self.c

if __name__ == '__main__':
    f1 = Foo(1, 2)
    f2 = Foo(3, 4)

    print(f1.calc())  # 1 + 2 + 10 = 13
    print(f2.calc())  # 3 + 4 + 10 = 17

    print('-' * 40)

    # Modify the class variable Foo.c directly!
    Foo.c = 20

    print(f1.calc())  # 1 + 2 + 20 = 23
    print(f2.calc())  # 3 + 4 + 20 = 27

    print('-' * 40)

    # Now shadow the class variable in f1
    f1.c = 5                        # You shadow the class variable only in f1

    print(f1.calc())  # 1 + 2 + 5 = 8
    print(f2.calc())  # 3 + 4 + 20 = 27


print("Shows only instance variables :")
print(f1.__dict__)   # Shows only instance variables
print("Shows class variables :")
print(Foo.__dict__)  # Shows class variables


# In[12]:


print("How a method itself can be shadowed (overwritten) just for one instance?!")


# In[13]:


print('''

🔥 Shadowing a method for just one instance!
In Python, methods are just attributes too.
That means you can override (shadow) a method for only one specific object, without affecting other instances!

🧠 Basic Idea:
Normally, methods are stored in the class.

If you assign a new method directly to an instance,
it shadows (overrides) the class method only for that instance.

''')


# In[14]:


print("METHOD BINDING")


# In[15]:


class Foo:
    def greet(self):
        print("Hello from Foo class!")

if __name__ == '__main__':
    f1 = Foo()
    f2 = Foo()

    f1.greet()  # Hello from Foo class!
    f2.greet()  # Hello from Foo class!

    print('-' * 40)

    # Now shadow the greet method for f1 only
    def new_greet(self):
        print("Hello from f1 instance only!")

    f1.greet = new_greet.__get__(f1)  # Bind the new function to f1 : OK

    f1.greet()  # Hello from f1 instance only!
    f2.greet()  # Hello from Foo class!

print(f1.__dict__)
print(Foo.__dict__)

# Let’s be very careful: this is METHOD BINDING
# f1.greet = new_greet.__get__(f1) : No, this is not name mangling.
# Name mangling and binding methods are two very different concepts in Python.


# In[16]:


print("NAME MANGLING")

class Foo:
    def __init__(self):
        self.__hidden = 42

f = Foo()

# Wrong way: AttributeError
# print(f.__hidden)

# Correct way (access mangled name)
print(f._Foo__hidden)  # ➔ 42

# Name mangling is designed to:
# Prevent accidental access,
# Not to provide strong security!
# ✅ It is "weak" protection — just a way to avoid name clashes in subclasses.


# In[ ]:





# In[17]:


print('''

In Python, if you want to bind a new method properly to an instance (so that it behaves like a normal method and automatically receives self), 
you can use types.MethodType from the built-in types module.

types.MethodType() is the professional, safe way to bind a new method to an instance!

It's better and safer than manually doing f1.greet = new_greet.__get__(f1). 
''')

import types  # <-- import the types module!

class Foo:
    def greet(self):
        print("Hello from Foo class!")

if __name__ == '__main__':
    f1 = Foo()
    f2 = Foo()

    f1.greet()  # Hello from Foo class!
    f2.greet()  # Hello from Foo class!

    print('-' * 40)

    # Define a new function
    def new_greet(self):
        print("Hello from f1 instance only!")

    # Bind it to f1 using types.MethodType
    f1.greet = types.MethodType(new_greet, f1)

    f1.greet()  # Hello from f1 instance only!
    f2.greet()  # Hello from Foo class!

print(f1.greet)  # <bound method new_greet of <__main__.Foo object at ...>>
print(f2.greet)  # <bound method Foo.greet of <__main__.Foo object at ...>>


# In[ ]:





# In[18]:


print('''Methods in Python :

+ Public → Anyone can call
- Private → Only the same class can call
# Protected → Same class and subclasses can call

''')


# In[19]:


class LoginRecord:
    def __init__(self, username, password, expiry_days):
        self.username = username
        self._expiry_days = expiry_days 
        # "This is a protected attribute — please treat it as internal/private, but technically it's still accessible."
        # It is NOT name mangled.
        self.__password = password  #  This starts with two underscores __, so Python applies name mangling.
                                    # Python renames it internally to: _LoginRecord__password
                                    #  This is meant to discourage direct access from outside the class — weak "privacy".
                                    # To access it manually from outside (which you usually avoid), you must do:
                                    # print(john_login._LoginRecord__password)  # ➔ 'secret' 
                                       
if __name__ == '__main__':
    john_login = LoginRecord('john', 'secret', 4)

    print(john_login.username)
    print(john_login._LoginRecord__password)
    print(john_login._expiry_days)


# 🎯 Big Lessons:
# Double underscores __var = Name mangling (not true security, but "discourages" access).
# Single underscore _var = Protected (by convention only).
# No underscore = Public (completely open).
# Python trusts you to be responsible — it gives guidelines, not strict enforcement.

dir(john_login) # You can see the mangled name explicitly!


# In[20]:


print('''

accessify — Detailed Overview

''')


# In[21]:


print('''

accessify — Detailed Overview

accessify is a Python library that lets you explicitly declare methods as:

@private — Only accessible inside the class itself.

@protected — Accessible inside the class and subclasses.

(default) — No decoration = public method.

It enforces this at runtime:
👉 If someone tries to call a @private method from outside the class, an exception is raised, stopping them.

''')

from accessify import private, protected

class MyClass:
    def __init__(self):
        self.name = "Accessify Example"

    @private
    def my_private_method(self):
        print("This is PRIVATE and should not be called from outside!")

    @protected
    def my_protected_method(self):
        print("This is PROTECTED and accessible in subclasses.")

    def public_method(self):
        print("This is PUBLIC and anyone can call it.")

    def internal_call(self):
        # OK: private method can be called *inside* the class
        self.my_private_method()
        self.my_protected_method()

obj = MyClass()
obj.public_method()        # Works!
obj.internal_call()        # Works (calls private & protected internally)


# In[22]:


print('''

Subclass Behavior (for @protected)

If you subclass and call a @protected method, it works:

''')

class SubClass(MyClass):
    def call_protected(self):
        self.my_protected_method()   # ✅ Allowed

    def call_private(self):
        self.my_private_method()     # ❌ Still forbidden


sub = SubClass()
sub.call_protected()  # OK
# sub.call_private()    # Error


# In[ ]:





# In[ ]:




