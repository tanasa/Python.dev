#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print("Interface Demo")


# In[2]:


from abc import ABC, abstractmethod

class Foo(ABC):
    def method1(self):
        return 'method1'

    def call_method2(self):
        # dynamic binding
        print(self.method2())

    @abstractmethod
    def method2(self):        # This method must be implemented in a subclass.
        return NotImplemented


class Bar(Foo):
    #  This is dynamic binding: self.method2() will resolve to the correct version of method2() depending on the actual class of the object 
    # at runtime.
    
    def method2(self):   # If it's a Bar, it will call Bar.method2() even though call_method2() is defined in Foo.
        return 'method2 from Bar'
                         # This implements the required method2() from Foo.
                         # Now Bar can be instantiated — it's no longer abstract.

if __name__ == '__main__':
    b = Bar()
    print(b.method1())
    print(b.method2())
    b.call_method2()


# In[ ]:





# In[3]:


print("Random Numbers")


# In[4]:


import random

# randomly generate a 4-digit number
print(random.randint(1000, 9999))

for _ in range(10):
    print(random.randint(1, 6))


colors = ['red', 'black', 'yellow', 'green', 'pink', 'white', 'blue']
for _ in range(3):
    print(random.choice(colors))

numbers = [i + 1 for i in range(10)]
print(numbers)
random.shuffle(numbers)
print(numbers)


# In[5]:


print("Classes : Tickets")


# In[6]:


print('''

OOP Concepts Demonstrated

Abstraction	@abstractmethod get_price() in Ticket

Polymorphism	get_price() behaves differently in each subclass

Inheritance	ShowTicket, MovieTicket, StudentMovieTicket all inherit from Ticket

Encapsulation	Each object stores its own number and price rules

Dynamic binding	__str__() calls self.get_price() — resolved at runtime

Constructor chaining	super().__init__() in subclasses

''')


# In[7]:


from abc import ABC, abstractmethod
import random

class Ticket(ABC):
    def __init__(self):
        # randomly generated as a 4-digit number
        self.number = random.randint(1000, 9999)

    @abstractmethod
    def get_price(self):      # Forces subclasses to define their own price logic. This is dynamic binding or runtime polymorphism.
        return NotImplemented

    def __str__(self):
        # dynamic binding
        return f'{self.number}: ${self.get_price()}'


class ShowTicket(Ticket):
    def get_price(self):
        return 50

# If a movie ticket is purchased 10 days or more before the movie date
# the ticket price is $30. Otherwise, the ticket price is $40.

class MovieTicket(Ticket):
    def __init__(self, days):
        super().__init__()
        self.days_in_advance = days

    def get_price(self):
        return 30 if self.days_in_advance >= 10 else 40


# student's movie ticket is always half-price of the movie ticket.
# The string representation of the student's movie ticket
# should include (Student ID required) at the end

class StudentMovieTicket(MovieTicket):
    # In Python class methods, the first parameter must be self — 
    # it's how the method gets access to the specific object instance it’s called on.
    def get_price(self):
        return super().get_price() // 2   # It comes from the parent class, which in this case is MovieTicket.

    def __str__(self):
        return '{} (Student ID required)'.format(super().__str__())


if __name__ == '__main__':
    
    t = ShowTicket()
    print(t)
    t2 = ShowTicket()
    print(t2)

    mt = MovieTicket(12)
    print(mt) # 1234: $30
    mt2 = MovieTicket(3)
    print(mt2)  # 1235: $40

    st = StudentMovieTicket(15)
    print(st)  # 2222: $15 (Student ID required)
    st2 = StudentMovieTicket(1)
    print(st2)  # 3333: $20 (Student ID required)


# In[ ]:





# In[8]:


print("Class Variables :")


# In[9]:


class Foo:

    c = 10  # # class variable (shared by all instances)

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
             # which shadows the class variable Foo.c
    print(f.c)
    print(Foo.c)
    print(f.calc()) # calc still uses Foo.c, not f.c
                    # def calc(self):
                    # return self.a + self.b + Foo.c  # explicitly uses class variable
                    # still refers to Foo.c, not self.c, so the result is still 13
    # “Use the variable c defined in the class Foo — not on the instance self.”
    # f.c = 5  # Creates instance variable
    # It doesn't affect the value used in calc(), because calc() hardcodes access to Foo.c, the class variable.


# In[10]:


print("Class Variables : expanding the previous code")


# In[11]:


# ✅ What is a static method?

# A static method is a method that:
# Belongs to the class, not to any specific object.
# Does not take self or cls as the first argument.
# Is called on the class itself, not on an instance.
# Cannot access instance variables (self.something) directly.
# Often used to update or operate on class-level data.


# In[12]:


from abc import ABC, abstractmethod
import random

class Ticket(ABC):
    next_ticket_number = 1   # This is a class variable shared across all tickets — it allows ticket numbers to be assigned sequentially.

    def __init__(self):      # Constructor
        # To make the ticket number to be generated in a sequential order
        self.number = Ticket.next_ticket_number
        Ticket.next_ticket_number += 1  # instead of self.next_ticket_number += 1, because 
                                        # because: next_ticket_number is a class variable, not an instance variable
                                        # so you should access and modify it via the class: Ticket.next_ticket_number
    @abstractmethod
    def get_price(self):
        return NotImplemented

    def __str__(self):
        # dynamic binding
        return '{}: ${}'.format(self.number, self.get_price())


class ShowTicket(Ticket):
    def get_price(self):
        return 50

# If a movie ticket is purchased 10 days or more before the movie date
# the ticket price is $30. Otherwise, the ticket price is $40.

class MovieTicket(Ticket):
    minimum_day_in_advance = 10       # Class Constants / class variables
    EARLY_BIRD_PRICE = 30             # Class Constants / class variables
    FULL_PRICE = 40                   # Class Constants / class variables

    def __init__(self, days):
        super().__init__()
        self.days_in_advance = days

    def get_price(self):
        return MovieTicket.EARLY_BIRD_PRICE \
            if self.days_in_advance >= MovieTicket.minimum_day_in_advance \
            else MovieTicket.FULL_PRICE

    @staticmethod
    def update_policy(new_days):
        MovieTicket.minimum_day_in_advance = new_days # This method updates the class variable minimum_day_in_advance.
                                                      # It changes the value of the class variable:
                                                      # MovieTicket.minimum_day_in_advance = 5
                                                      # Often used to update or operate on class-level data.
# student's movie ticket is always half-price of the movie ticket.
# The string representation of the student's movie ticket
# should include (Student ID required) at the end

class StudentMovieTicket(MovieTicket):
    def get_price(self):
        return super().get_price() // 2

    def __str__(self):
        return '{} (Student ID required)'.format(super().__str__())


if __name__ == '__main__':
    
    t = ShowTicket()
    print(t)
    t2 = ShowTicket()
    print(t2)

    mt = MovieTicket(12)
    print(mt) # 1234: $30
    mt2 = MovieTicket(3)
    print(mt2)  # 1235: $40

    st = StudentMovieTicket(15)
    print(st)  # 2222: $15 (Student ID required)
    st2 = StudentMovieTicket(1)
    print(st2)  # 3333: $20 (Student ID required)

    MovieTicket.update_policy(5)
    mt3 = MovieTicket(8)
    print(mt3)


# In[ ]:





# In[13]:


print("Class Variables : private, public, protected")


# In[14]:


class LoginRecord:
    def __init__(self, username, password, expiry_days):
        self.username = username            # public
        self.__password = password          # private (by convention + name mangling) (can be accessed via name mangling)
        self._expiry_days = expiry_days     # protected (by convention) : “intended for internal use.”

if __name__ == '__main__':
    john_login = LoginRecord('john', 'secret', 4)

    print(john_login.username)
    print(john_login._LoginRecord__password) # _ClassName__varname → _LoginRecord__password (name mangling)
    print(john_login._expiry_days)


# In[15]:


class LoginRecord:
    def __init__(self, username, password, expiry_days):
        self.username = username            # public
        self.__password = password          # private
        self._expiry_days = expiry_days     # protected (convention)

    def get_masked_password(self):
        return '*' * len(self.__password)


class AdminLoginRecord(LoginRecord):
    def __init__(self, username, password, expiry_days, level):
        super().__init__(username, password, expiry_days)
        self.level = level

    def show_info(self):
        print(f"Username: {self.username}")         # ✅ public → accessible
        print(f"Expiry days: {self._expiry_days}")  # ⚠️ protected → accessible but discouraged
        # print(f"Password: {self.__password}")     # ❌ ERROR: private → not accessible directly
        print(f"Masked password: {self.get_masked_password()}")
        print(f"Level: {self.level}")

if __name__ == '__main__':
    admin = AdminLoginRecord("admin", "secretpass", 30, "superuser")
    admin.show_info()


# In[16]:


print("Class Variables : Getters and Setters")


# In[17]:


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
        if age > 0 and age > self._age:
            self._age = age

    def __get_ssn(self):
        if hasattr(self, '_Person__ssn'):
            return '***-**-{}'.format(self.__ssn[-4:])
        else:
            return '(no SSN on file)'

    def __del_ssn(self):
        if hasattr(self, '_Person__ssn'):
            print('ssn will be deleted')
            del self.__ssn
        else:
            print('ssn already deleted')

    name = property(fget=_get_name)
    age = property(fget=_get_age, fset=_set_age)
    ssn = property(fget=__get_ssn, fdel=__del_ssn)


if __name__ == '__main__':
    john = Person('John', 18, '123-45-6789')
    print(john.name)        # John
    print(john.age)         # 18

    john.age = 20
    print(john.age)         # 20

    john.age = -5           # invalid
    print(john.age)         # still 20

    print(john.ssn)         # ***-**-6789

    del john.ssn
    print(john.ssn)         # (no SSN on file)

    print("\nGetters and Setters:")
    print(f"Name: {john.name}")
    print(f"Age: {john.age}")
    john.age = 25
    print(f"Updated Age: {john.age}")


# why we not use name mangling __Person__ssn, when doing : print(john.ssn) ?
# When you write: print(john.ssn), Python Python for a property named ssn in the class. You defined:
# ssn = property(fget=_get_ssn, fdel=_del_ssn)

# This means that:
# john.ssn calls the method john._get_ssn() under the hood
# john.ssn is now a property interface, not direct variable access
# This is how you enforce encapsulation while hiding the actual implementation (i.e., __ssn)


# In[18]:


# Using name mangling : john._Person__ssn

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
        if age > 0 and age > self._age:
            self._age = age

    def _get_ssn(self):
        return '***-**-{}'.format(self.__ssn[-4:])

    # def _del_ssn(self):
    #    print('ssn will be deleted')
    #    del self.__ssn

    name = property(fget =_get_name)
    age = property(fget =_get_age, fset =_set_age)
    # ssn = property(fget =_get_ssn, fdel =_del_ssn)
    ssn = property(fget =_get_ssn)

if __name__ == '__main__':
    john = Person('John', 18, '123-45-6789')

    # Using public API
    print("Public property access:")
    print(john.name)        # John
    print(john.age)         # 18
    print(john.ssn)         # ***-**-6789

    # Using direct name-mangled access (discouraged)
    print("\nDirect access via name mangling:")
    print(john._Person__ssn)  # 123-45-6789

    # Deleting ssn using property
    # del john.ssn
    # print("\nAfter deleting ssn:")

    # This will now fail because __ssn is deleted
    try:
        print(john._Person__ssn)  # Will raise AttributeError
    except AttributeError:
        print("❌ __ssn no longer exists (AttributeError)")


# In[ ]:





# In[19]:


print("Code that attempts to implement Multiple Inheritance")


# In[20]:


class Animal:
    number_of_animals = 0

    def __init__(self, name):
        self._name = name
        Animal.number_of_animals += 1


class Dog(Animal):
    def __init__(self, name, breed, color):
        Animal.__init__(self, name)
        self._breed = breed
        self._color = color

    def _get_color(self):
        return self._color

    color = property(fget = _get_color)


class Domestic(Animal):
    def __init__(self, name, address):
        Animal.__init__(self, name)
        self._address = address

    def _get_address(self):
        return self._address

    address = property(fget = _get_address)


class HomePuppy(Dog, Domestic):
    def __init__(self, name, breed, color, address):
        # super().__init__(name, breed, color, address)
        Dog.__init__(self, name, breed, color)
        Domestic.__init__(self, name, address)

# The order of arguments is determined entirely by your __init__() definition in HomePuppy
# Python will expect the arguments in the same order as they're listed in the method signature.
# You (as the programmer) specified the order: first name, then breed, then color, then address.

if __name__ == '__main__':
    
    p = HomePuppy('John', 'Chihuahua', 'brown', 'San Jose') 
    # The expected order is : name → breed → color → address
    # p = HomePuppy(name='John', breed='Chihuahua', color='brown', address='San Jose')
   
    print(p.color)
    print(p.address)
    print(Animal.number_of_animals)
    print(HomePuppy.__mro__)  # shows method resolution order (MRO)

# !!!  
# !!!  Why does Animal.number_of_animals equal 2, not 1 or 3 ???
# !!!  

# ⚠️ Problem: Double counting
# The key: Animal.__init__() is called twice
# You're using multiple inheritance, and explicitly calling both base initializers:
# Dog.__init__(self, name, breed, color)
# Domestic.__init__(self, name, address)
# Both Dog and Domestic independently call:
# Animal.__init__(self, name)
# So in total:
# Dog.__init__() → calls Animal.__init__() → 🐾 +1
# Domestic.__init__() → also calls Animal.__init__() → 🐾 +1
# ✅ Total = 2 animals created, according to Animal.number_of_animals


# In[ ]:





# In[21]:


print("Code that implements Multiple Inheritance in a proper way")

print('''
      
It uses cooperative multiple inheritance via super() : super().__init__(**info)

You're absolutely right to notice that Animal is a superclass, so it might seem odd at first to see: super().__init__(**info)

✅ Why we use super().__init__(...) even in a superclass ???

🔑 The short answer:

In Python multiple inheritance, every class in the hierarchy — including the top one — should call super().__init__() to enable cooperative inheritance.

What if you skip it?	You break the constructor chain — some classes won’t be initialized !

Excellent — you're now working with a fully cooperative multiple inheritance design using super() and **info to propagate arguments through 
the method resolution order (MRO). This is exactly how multiple inheritance should be structured in Python.

''')

print('''

MRO-Friendly __init__ Structure

All __init__() methods use:

def __init__(..., **info):
    super().__init__(**info)

This:

Enables the MRO to work cleanly

Ensures each class is initialized once

Avoids duplicate Animal.number_of_animals += 1 calls

Allows flexible argument passing

''')


# In[22]:


class Animal:
    number_of_animals = 0

    def __init__(self, name, **info):
        super().__init__(**info)
        self.name = name
        Animal.number_of_animals += 1


class Dog(Animal):
    def __init__(self, breed, color, **info):
        super().__init__(**info)
        self._breed = breed
        self._color = color

    def _get_color(self):
        return self._color

    color = property(fget=_get_color)


class Domestic(Animal):
    def __init__(self, address, **info):
        super().__init__(**info)
        self._address = address

    def _get_address(self):
        return self._address

    address = property(fget=_get_address)


class HomePuppy(Dog, Domestic):
    def __init__(self, **info):
        super().__init__(**info)


if __name__ == '__main__':
    
    p = HomePuppy(name='John', breed='Chihuahua', color='brown', address='San Jose')
    print(p.color)
    print(p.address)
    print(Animal.number_of_animals)
    print(HomePuppy.__mro__)


# In[23]:


# HomePuppy.__init__ receives all the keyword arguments
# super() sends them up the MRO
# Each class extracts the keyword arguments it needs, e.g.:
# Dog takes breed and color
# Domestic takes address
# Animal takes name
# So when super() is used in HomePuppy, the constructor chain follows that order and each __init__() gets called exactly once — 
# thanks to the cooperative use of super()


# In[24]:


print("Code that implements Multiple Inheritance in a proper way. It is fully rewritten following the pattern :")

print('''

def __init__(self, **info):
    self._something = info.pop("something")
    ...
    super().__init__(**info)


This approach:

Extracts only the arguments each class needs

Raises KeyError if required arguments are missing (which is good for validation)

Ensures super().__init__() only receives what's needed further up the MRO

''')


# In[25]:


# Final re-written code :

class Animal:
    number_of_animals = 0

    def __init__(self, **info):
        self.name = info.pop("name")
        Animal.number_of_animals += 1
        super().__init__(**info)


class Dog(Animal):
    def __init__(self, **info):
        self._breed = info.pop("breed")
        self._color = info.pop("color")
        super().__init__(**info)

    def _get_color(self):
        return self._color
    
    def _get_breed(self):
        return self._breed

    color = property(fget=_get_color)


class Domestic(Animal):
    def __init__(self, **info):
        self._address = info.pop("address")
        super().__init__(**info)

    def _get_address(self):
        return self._address

    address = property(fget=_get_address)


class HomePuppy(Dog, Domestic):
    def __init__(self, **info):
        super().__init__(**info)


if __name__ == '__main__':
    
    p = HomePuppy(name='John', breed='Chihuahua', color='brown', address='San Jose')
    print(p.color)                       # brown
    print(p.address)                     # San Jose
    print(Animal.number_of_animals)      # 1
    print(HomePuppy.__mro__)             # MRO tuple


# In[ ]:





# In[ ]:





# In[26]:


print("Random Art using mainloop()")


# In[27]:


import tkinter
import random

width = 500
height = 500
window = tkinter.Tk()
window.title('Random Art')
canvas = tkinter.Canvas(window, width=width, height=height)
canvas.pack()

def draw_rectangle(canvas):
    top = random.randint(10, height - 50)
    left = random.randint(10, width - 50)
    bottom = random.randint(top + 30, height - 10)
    right = random.randint(left + 30, width - 10)
    colors = ['red', 'yellow', 'green', 'pink', 'purple', 'blue']
    color = random.choice(colors)
    canvas.create_rectangle(left, top, right, bottom, outline=color)

for _ in range(1000):
    draw_rectangle(canvas)

window.mainloop()


# In[ ]:




