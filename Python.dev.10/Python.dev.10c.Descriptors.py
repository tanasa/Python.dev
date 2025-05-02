#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print('''

About attributes :

📌 Special kinds of attributes

Instance attributes → defined in __init__() with self

Class attributes → shared across all instances

Dynamic attributes → added after object creation

Where are attributes stored ?

object.__dict__

''')

class Dog:
    def __init__(self, name):
        self.name = name

fido = Dog("Fido")
print(fido.__dict__)  # {'name': 'Fido'}

print('''

What are dynamic attributes?

Dynamic attributes are attributes that you add to an object after it's been created, not defined in the class body or __init__.

''')


# In[ ]:





# In[2]:


print("Descriptors :")


# In[1]:


print('''

Descriptors in Python are a powerful, advanced feature that most people use without even knowing it — through things like 

@property, 
staticmethod, 
classmethod.

Let’s explain descriptors clearly, from the ground up, with examples.

🧠 What is a Descriptor?
A descriptor is any object that defines at least one of these special methods:

__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)

✅ If an object implements any of those methods, it is a descriptor.

🎯 Why do descriptors exist?
They let you customize how attribute access works on an object.

A descriptor lets you control what happens when someone does:
object.attribute or object.attribute = value

✅ You can use descriptors to:

Add validation
Log access
Compute values dynamically
Manage internal storage
Build properties, methods, and more

When descriptors are used

Descriptors only work when:

They are class attributes, not instance attributes.
You access them through an instance (or class).

''')

print('''

Descriptors are:

The underlying mechanism behind @property, @classmethod, @staticmethod

The cleanest way to intercept attribute access

''')


# In[2]:


print('''

A classic and powerful example of a Python descriptor being used to model currency conversion.

🧠 What makes it a descriptor?

A Python descriptor is any class that defines one or more of:

__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)

Your class CurrencyType defines both: 

def __get__(self, instance, owner):
def __set__(self, instance, value)

And so are its subclasses: Usd, Euro, Pound, Rupee.

''')


# In[ ]:


print("An example given in the class :")


# In[ ]:


# This defines a descriptor NameDescriptor that manages access to a name attribute on a Person object.
# Descriptors are a way to customize attribute access, like what happens when you get, set, or delete an attribute.


# In[3]:


# 🧱 NameDescriptor class
# This is a descriptor because it defines at least one of the special methods:
# __get__(self, instance, owner)
# __set__(self, instance, value)
# __delete__(self, instance)
# It manages access to an internal attribute (_name) on the Person object.

class NameDescriptor:
    
    # instance is a Person object
    # owner is Person class
    
    def __get__(self, instance, owner):
        print('__get__ is called')
        try:
            return instance._name
        except AttributeError:
            return 'World'

    def __set__(self, instance, value):
        print('__set__ is called')
        instance._name = value

    def __delete__(self, instance):
        print('__delete__ is called')
        del instance._name


class Person:
    def __init__(self, name):
        self._name = name

    # def _get_name(self):
    #     return self._name
    #
    # name = property(fget=_get_name)
    
    name = NameDescriptor()  # Connects descriptor to the Person class

# The Person class has an attribute name that is a descriptor
# It operates on the internal _name field

if __name__ == '__main__':
    
   john = Person("John")    # sets _name directly
   print(john.name)         # triggers __get__ → prints and returns "John"

   john.name = "Johnny"     # triggers __set__ → updates _name
   print(john.name)         # __get__ → returns "Johnny"

   del john.name            # triggers __delete__ → removes _name
   print(john.name)         # __get__ → catches AttributeError → returns "World"


# In[ ]:


print('''

__get__

Called when you access person.name
Tries to return instance._name
If _name doesn’t exist (e.g. it was deleted), returns "World"

🔹 __set__

Called when you do person.name = "Alice"
Stores the value inside the instance under _name

__delete__

Called when you do del person.name
Deletes the _name attribute from the instance.

''')


# In[ ]:


print("A Simplified Version Using @property :")

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('@property getter is called')
        return getattr(self, '_name', 'World')

    @name.setter
    def name(self, value):
        print('@property setter is called')
        self._name = value

    @name.deleter
    def name(self):
        print('@property deleter is called')
        del self._name


john = Person("John")
print(john.name)      # Triggers getter
john.name = "Johnny"  # Triggers setter
print(john.name)
del john.name         # Triggers deleter
print(john.name)      # Triggers fallback return "World"

# When to use each?
# Use @property when managing simple attribute access with logic (e.g., validation, fallback)
# Use a descriptor class if you want to reuse the logic across multiple attributes or classes, or implement advanced behaviors


# In[ ]:





# In[12]:


print('''

The parameters getter, setter, and deleter refer to callable functions (typically methods) that define how an attribute should behave when:

    getter(instance) → is called to retrieve the value of the attribute (obj.attr).

    setter(instance, value) → is called to assign a new value to the attribute (obj.attr = value).

    deleter(instance) → is called to delete the attribute (del obj.attr).

These are usually passed as method references frrom another class.

''')


# In[18]:


# In a typical case : 

class MyClass:
    def __init__(self):
        self._x = 0

    def get_x(self):
        return self._x

    def set_x(self, value):
        if value >= 0:
            self._x = value
        else:
            raise ValueError("Value must be non-negative")

    def del_x(self):
        print("Deleting x")
        del self._x

    x = property(fget=get_x, fset=set_x, fdel=del_x)


# In this case:
    
# getter = get_x → defines how to access .x
# setter = set_x → defines how to assign .x = value
# deleter = del_x → defines behavior for del obj.x


# In[ ]:


print("Another example given in the class :")


# In[13]:


# This is a custom descriptor class. It mimics the behavior of property() but gives more explicit control.
# A descriptor class needs to define at least one of the following methods:
# __get__(self, instance, owner)
# __set__(self, instance, value)
# __delete__(self, instance)


# In[9]:


print("Explanations for the code below")

print('''

The __get__ method in a descriptor always receives two arguments besides self:

def __get__(self, instance, owner):

*** instance (INSTANCE) : this is the object instance that the descriptor was accessed through.

For example:

john = Person('John', 18)
print(john.name)

The descriptor is defined in Person.

When you do john.name, john is passed as instance.
If you access the descriptor from the class itself (e.g., Person.name), then instance will be None.

*** owner (OWNER)

This is the owner class where the descriptor is defined — usually the class where the attribute was declared.
In this case, it's the Person class.
It helps if you want to do something class-specific, or access class-level metadata.

''')    


# In[ ]:





# In[17]:


class DescriptorProperty:
    def __init__(self, getter = None, setter = None, deleter = None):  # These are stored internally to be used later when the property is accessed or set
        self._getter = getter
        self._setter = setter
        self._deleter = deleter

    def __get__(self, instance, owner):            # Triggered when the attribute is READ (e.g., john.age)
        if self._getter:
            return self._getter(instance)
        else:
            raise AttributeError('cannot get')

    def __set__(self, instance, value):            # Triggered when the attribute is ASSIGNED (e.g., john.age = 20)
        if self._setter:
            self._setter(instance, value)
        else:
            raise AttributeError('cannot set')

    def __delete__(self, instance):
        if self._deleter:
            self._deleter(instance)
        else:
            raise AttributeError('cannot delete')


class Person:
    def __init__(self, name, age):              # Stores name and age as private attributes (_name and _age).
        self._name = name
        self._age = age

    def _get_name(self):                        
        return self._name

    def _get_age(self): 
        return self._age

    def _set_age(self, age):
        if age > 0 and age > self._age:
            self._age = age

    name = DescriptorProperty(getter = _get_name)                  # the descriptor to the class-level attributes name and age.
    age = DescriptorProperty(getter = _get_age, setter = _set_age) # the descriptor to the class-level attributes name and age.

    # name = property(fget=_get_name)                            # Using a custom descriptor allows for more control, flexibility, and reuse if needed.
    # age = property(fget=_get_age, fset=_set_age)


if __name__ == '__main__':
    
    john = Person('John', 18)
    print(john.name)
    print(john.age)
    
    john.age = 20
    print(john.age)
    john.age = -5
    print(john.age)


# In[10]:


print('''

CUSTOM DESCRIPTORS :

Can be reused across classes.

Allow more logic (e.g., logging, caching, validation).

Can manage different attributes centrally.

''')


# In[ ]:





# In[ ]:


print("An example of how you can extend your DescriptorProperty to log access, assignment, and deletion of an attribute :")


# In[20]:


class DescriptorProperty:
    def __init__(self, getter=None, setter=None, deleter=None, name=None):
        self._getter = getter
        self._setter = setter
        self._deleter = deleter
        self._name = name  # just to make logging easier

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._getter:
            print(f"[LOG] Getting '{self._name}' for {instance}")
            return self._getter(instance)
        raise AttributeError("Cannot get attribute")

    def __set__(self, instance, value):
        if self._setter:
            print(f"[LOG] Setting '{self._name}' to {value} for {instance}")
            self._setter(instance, value)
        else:
            raise AttributeError("Cannot set attribute")

    def __delete__(self, instance):
        if self._deleter:
            print(f"[LOG] Deleting '{self._name}' for {instance}")
            self._deleter(instance)
        else:
            raise AttributeError("Cannot delete attribute")

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _get_name(self):
        return self._name

    def _get_age(self):
        return self._age

    def _set_age(self, age):
        if age > 0 and age > self._age:
            self._age = age
        else:
            print("[WARN] Invalid age assignment ignored")

    def _del_age(self):
        print("Actually deleting age...")
        del self._age

    name = DescriptorProperty(getter=_get_name, name="name")
    age = DescriptorProperty(getter=_get_age, setter=_set_age, deleter=_del_age, name="age")

# Sample Run :

john = Person("John", 18)
print(john.name)    # Logs access
print(john.age)     # Logs access

john.age = 20       # Logs assignment
john.age = -5       # Logs warning

del john.age        # Logs deletion


# In[ ]:





# In[ ]:


print("A more complex example given in the class :")


# In[ ]:


class CurrencyType:
    conversion = 1.0   # conversion is a class attribute that defines the conversion rate to USD.

    def __get__(self, instance, owner):         # __get__() converts from USD → target currency.
        return instance._usd * self.conversion

    def __set__(self, instance, value):
        instance._usd = value / self.conversion  # converts from target currency → USD and stores it in instance._usd

class Usd(CurrencyType):
    pass

# These subclasses inherit the conversion logic, and override only the conversion rate to USD.
# ✅ All conversions happen automatically!

class Euro(CurrencyType):  # ✅ These classes inherit the descriptor logic from CurrencyType, but override the conversion rate.
    conversion = 0.92

class Pound(CurrencyType): # ✅ These classes inherit the descriptor logic from CurrencyType, but override the conversion rate.
    conversion = 0.77

class Rupee(CurrencyType):  # ✅ These classes inherit the descriptor logic from CurrencyType, but override the conversion rate.
    conversion = 86.95


class Currency:    # ✅ These are class-level attributes that point to descriptor instances.
    
    usd = Usd()
    euro = Euro()
    pound = Pound()
    rupee = Rupee()

# These are class-level descriptors.
# Whenever you access currency.euro, Python internally calls:

    def __init__(self, usd=None, euro=None, pound=None, rupee=None):
        if usd:
            self.usd = usd
        elif euro:
            self.euro = euro
        elif pound:
            self.pound = pound
        elif rupee:
            self.rupee = rupee
        else:
            raise TypeError()

    def __str__(self):
        return ('{} usd = {} euro = {} pound = {} rupee'.format(
            self.usd,
            self.euro,
            self.pound,
            self.rupee
        ))

if __name__ == '__main__':
    
    # 1 usd = 0.92 euro = 0.77 pound = 86.95 rupee
    currency = Currency(usd=1000)
    print(currency) # 1000 usd = ... euro = ... pound = ... rupee
    
    currency.pound = 500
    print(currency) # ... usd = ... euro = 500 pound = ... rupee
    
    currency = Currency(rupee=10000)
    print(currency) # ... usd = ... euro = ... pound = 10000 rupee

# So any time you do:
# currency.euro = 500
# …it actually calls:
# Euro.__set__(currency, 500)

# …and when you access:
# currency.euro
# …it calls:
# Euro.__get__(currency, Currency)


# In[ ]:





# In[ ]:


print(
    
'''So why is _usd used specifically?

1. ✅ To store one single internal value (USD)
All other currencies (Euro, Pound, Rupee) are derived from USD.

usd, euro, pound, rupee are virtual attributes controlled by descriptors.

Here, _usd is not passed as an argument to the method.

Yet it's used as: instance._usd

So how does this work?

__get__(self, instance, owner)
self = the descriptor instance (e.g. the Euro, Usd, Pound, etc.)

instance = the instance of the class where the descriptor is used
→ in your case, a Currency object

✅ So instance._usd just accesses an attribute of the Currency object.

So where is _usd actually coming from?

It's not passed as an argument.
It is created dynamically inside the descriptor like this:

instance._usd = value / self.conversion

_usd	A private variable on the instance, dynamically created

That’s why it “just works”
In Python, you don’t have to predefine instance variables like _usd.
You can create them on the fly:

class A:
    pass

a = A()
a.x = 42  # totally valid

So in plain words:

_usd is not passed to the descriptor — it is stored on the instance (Currency object) by the descriptor itself during assignment.

''')

print('''

🧠 In plain words:

_usd does not need to be declared in advance.

Python lets you add attributes to objects on the fly, unless restricted (e.g., with __slots__).

So self._usd = ... creates _usd the first time it's used.

''')


# In[ ]:





# In[ ]:


print(''' A simpler version :

No __get__ or __set__ magic

No on-the-fly _usd created by a descriptor

All data stored in a clear _usd variable set once in __init__

Conversion happens via explicit methods (like .from_usd() and .to_usd())

''')


# In[21]:


class CurrencyConverter:
    def __init__(self, conversion_rate):
        self.conversion_rate = conversion_rate

    def to_usd(self, amount):
        return amount / self.conversion_rate

    def from_usd(self, usd_amount):
        return usd_amount * self.conversion_rate


class Currency:
    def __init__(self, usd=None, euro=None, pound=None, rupee=None):
        
        self.converter = {                              # It creates a dictionary
                                                        # dictionaries can store any type of object, including objects with methods.  
            'usd': CurrencyConverter(1.0),
            'euro': CurrencyConverter(0.92),            # self.converter['euro'] returns an instance of the CurrencyConverter class.
            'pound': CurrencyConverter(0.77),
            'rupee': CurrencyConverter(86.95)
        }

        if usd is not None:
            self._usd = usd
        elif euro is not None:
            self._usd = self.converter['euro'].to_usd(euro)
        elif pound is not None:
            self._usd = self.converter['pound'].to_usd(pound)
        elif rupee is not None:
            self._usd = self.converter['rupee'].to_usd(rupee)
        else:
            raise ValueError("You must provide one currency amount.")

    def get_usd(self):
        return self._usd

    def get_euro(self):
        return self.converter['euro'].from_usd(self._usd)

    def get_pound(self):
        return self.converter['pound'].from_usd(self._usd)

    def get_rupee(self):
        return self.converter['rupee'].from_usd(self._usd)

    def set_pound(self, amount):
        self._usd = self.converter['pound'].to_usd(amount)

    def __str__(self):
        return f"{self.get_usd():.2f} USD = {self.get_euro():.2f} EUR = {self.get_pound():.2f} GBP = {self.get_rupee():.2f} INR"


# In[ ]:





# In[ ]:


print('''

Simplified Code (no _usd logic reuse)

Keep __get__ and __set__ to demonstrate descriptor behavior

Remove the shared _usd variable

Use per-currency storage (e.g. self._usd, self._euro, etc.)

Used getattr() / setattr()	Dynamically access attributes like _usd, _euro, etc.

''')

class CurrencyType:
    def __init__(self, name, conversion=1.0):
        self.name = name               # e.g., "usd", "euro"
        self.conversion = conversion   # exchange rate to USD

    def __get__(self, instance, owner):
        return getattr(instance, f"_{self.name}", 0)  # read e.g., instance._usd

    def __set__(self, instance, value):
        setattr(instance, f"_{self.name}", value)     # write e.g., instance._usd = value


# In[ ]:


print("Descriptor base class for each currency type")


# In[22]:


# Descriptor base class for each currency type

class CurrencyType:                                                #  custom descriptor (CurrencyType)
    def __init__(self, name, conversion):
        self.name = name
        self.conversion = conversion  # Exchange rate to USD

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return round(instance._usd * self.conversion, 2)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name.capitalize()} cannot be negative.")
        instance._usd = value / self.conversion


# Currency-specific subclasses
class Usd(CurrencyType):
    def __init__(self):
        super().__init__('usd', 1.0)

class Euro(CurrencyType):
    def __init__(self):
        super().__init__('euro', 0.92)

class Pound(CurrencyType):
    def __init__(self):
        super().__init__('pound', 0.77)

class Rupee(CurrencyType):
    def __init__(self):
        super().__init__('rupee', 86.95)


print("Descriptors only work as class attributes !!!")

# We define these as class attributes so that Python's descriptor protocol (__get__ and __set__) works automatically.
# Descriptors must be defined at the class level — not in __init__ — for Python to trigger their behavior.

# Main container class for currency conversion

class Currency:        # In the Currency class, the internal canonical representation of all currency amounts is _usd
                       # All currency values (euro, pound, rupee) are converted to and from USD.
    usd = Usd()        # Usd, which inherits CurrencyType) to the class Currency. This tels python :
                       # "Hey, when someone accesses currency.usd, call the __get__() method of this descriptor."
    euro = Euro()
    pound = Pound()
    rupee = Rupee()

    def __init__(self, usd=None, euro=None, pound=None, rupee=None):
        if usd is not None:
            self._usd = usd
        elif euro is not None:
            self._usd = euro / Currency.euro.conversion
        elif pound is not None:
            self._usd = pound / Currency.pound.conversion # Python looks for pound in the class → finds Currency.pound which is a descriptor object
        elif rupee is not None:
            self._usd = rupee / Currency.rupee.conversion
        else:
            raise ValueError("Provide at least one currency amount.")

    def __str__(self):
        return (
            f"${self.usd} USD = €{self.euro} EUR = "
            f"£{self.pound} GBP = ₹{self.rupee} INR"
        )


# Example usage

if __name__ == '__main__':
    
    currency = Currency(usd=1000)
    print(currency)
    # Output: $1000.0 USD = €920.0 EUR = £770.0 GBP = ₹86950.0 INR

    currency.pound = 500
    print(currency)
    # Output: $649.35 USD = €597.4 EUR = £500.0 GBP = ₹56456.5 INR

    currency = Currency(rupee=10000)
    print(currency)
    # Output: $115.01 USD = €105.81 EUR = £88.56 GBP = ₹10000.0 INR


# Since Currency.pound defines __get__, Python calls:
# Pound.__get__(self=Currency.pound, instance=currency, owner=Currency)
# Similarly for __set__:
# currency.pound = 500
# Calls Currency.pound.__set__(instance=currency, value=500)

# About .conversion() :
# conversion comes from the CurrencyType base class, because:
# class Pound(CurrencyType):
#    def __init__(self):
#        super().__init__('pound', 0.77)
# So, 
# Currency.pound is an instance of Pound
# Pound inherits from CurrencyType

# CurrencyType defines:
# def __init__(self, name, conversion):
#    self.name = name
#    self.conversion = conversion

# Therefore, Currency.pound.conversion → accesses the .conversion attribute initialized as 0.77.


# In[ ]:





# In[ ]:


print(" Dynamic Attributes :")


# In[ ]:


print('''

Dynamic attributes are attributes that you add to an object after it's been created, not defined in the class body or __init__.

✅ They’re created on the fly using assignment syntax or functions like setattr().

''')

class Animal:
    pass

dog = Animal()
dog.name = "Fido"            # dynamic attribute
dog.age = 5                  # another dynamic attribute

print(dog.name)              # Fido
print(dog.age)               # 5

print(dog.__dict__)  # {'name': 'Fido', 'age': 5}


print('''Alternative: Using setattr()''')

# You can also add dynamic attributes like this:

setattr(dog, "breed", "Labrador")
print(dog.breed)  # Labrador

# equivalent with 

dog.breed = "Labrador"

print('''Detecting dynamic attributes''')

if hasattr(dog, 'age'):
    print("Age exists")

print(getattr(dog, 'name'))      # → Fido
print(dog.__dict__)              # shows all instance-level attributes

# Risk	: Easy to create unintended fields by mistake


# In[ ]:





# In[ ]:





# In[ ]:




