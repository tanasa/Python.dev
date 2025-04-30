#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


print("Descriptors :")


# In[3]:


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

get_ipython().run_line_magic('pinfo', 'care')
Descriptors are:

The underlying mechanism behind @property, @classmethod, @staticmethod

The cleanest way to intercept attribute access


# In[ ]:


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


# In[7]:


print("An example given in the class :")


# In[14]:


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





# In[15]:


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


# In[8]:


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





# In[13]:


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
        self.conversion = conversion  # exchange rate to USD

    def __get__(self, instance, owner):
        return getattr(instance, f"_{self.name}", 0)  # read e.g., instance._usd

    def __set__(self, instance, value):
        setattr(instance, f"_{self.name}", value)     # write e.g., instance._usd = value


# In[17]:


print("Descriptor base class for each currency type")


# In[16]:


# Descriptor base class for each currency type

class CurrencyType:
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


# Main container class for currency conversion
class Currency:
    usd = Usd()
    euro = Euro()
    pound = Pound()
    rupee = Rupee()

    def __init__(self, usd=None, euro=None, pound=None, rupee=None):
        if usd is not None:
            self._usd = usd
        elif euro is not None:
            self._usd = euro / Currency.euro.conversion
        elif pound is not None:
            self._usd = pound / Currency.pound.conversion
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


# In[ ]:





# In[ ]:




