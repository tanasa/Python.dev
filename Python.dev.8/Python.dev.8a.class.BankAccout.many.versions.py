#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


print("Classes :")


# In[ ]:





# In[8]:


print("Classes : example BankAccount() : balance = property(fget=_get_balance)")
print("Example code BankAccount() : version 1") 


# In[1]:


class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = balance

    # Defines how the object looks when you print it : print(account)
    def __str__(self):
        return '{}: ${}'.format(self._owner, self.__balance)

    def deposit(self, amount):
        if amount <= 0:
            print('Invalid amount to deposit')
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('Invalid amount to withdraw')
        elif amount > self.__balance:
            print('Not enough money to withdraw')
        else:
            self.__balance -= amount

    def _get_balance(self):
        return self.__balance

    balance = property(fget = _get_balance) # This makes .balance a property — looks like an attribute but works like a method.
    
    # Read-only access to balance:
    # You can see the balance (account.balance)
    # But you cannot set it (account.balance = 0 would cause an error unless you defined a setter)

# print(account.balance)
# Output: 1500
# ✅ You access it like a normal variable,
# ✅ But internally it's controlled by a function!

# 1. If the withdrawal amount is greater than the balance
# withdraw won't happen and an error message should be printed as "Not enough money to withdraw"
# 2. Both deposit and withdraw should not accept negative values
# if it happens, the transaction should not be complete and an error message
# should be printed as "Invalid amount to withdraw" or "Invalid amount to deposit"

if __name__ == '__main__':
   
    # ATM machine
    # the error message to be printed in the ATM console
    # print should be called here
    # error message to be properly generated here
    
    b = BankAccount('John', 1000)
    print(b)
    
    b.deposit(500)
    print(b)
    
    b.withdraw(2000)
    b.deposit(-2000)
    print(b)

    print(b.balance)

    print('''

balance = property(fget=_get_balance)
property() in Python allows attribute-like access to methods.

fget means: getter function — you can read the value.
But you did not define an fset (setter function)

    ''')

# b.balance = 100
# property 'balance' of 'BankAccount' object has no setter


# In[ ]:





# In[27]:


print("Property :")


# In[ ]:





# In[28]:


print('''

🧠 What is property() in Python?

property() is a built-in Python function.

It allows you to turn a method into an attribute.

This lets you control access to private data — while keeping the syntax clean and simple (like accessing .name instead of calling .get_name()).

📦 Basic Structure of property()

property(fget=None, fset=None, fdel=None, doc=None)

''')

print('''

Why is it called fget?

When you use the property() function in Python, it can take up to four functions:

Argument name	Purpose
fget	Function to get the attribute (getter)
fset	Function to set the attribute (setter)
fdel	Function to delete the attribute (deleter)
doc	Docstring (documentation string) for the property

''')


# In[29]:


print(''' 

1. Without using property()
You have to call methods explicitly to get, set, or delete the name.
''')

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name


p = Person("Alice")
print(p.get_name())    # ➔ Alice

p.set_name("Bob")
print(p.get_name())    # ➔ Bob

p.del_name()

# ✅ Works fine, but you always need to call methods like get_name() and set_name() — it's verbose and less elegant

print('''

2. With property()
Now you can pretend that _name is a normal attribute, but still control access internally.
''')

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    # Create a smart attribute 'name' that internally calls these methods
    name = property(fget=get_name, fset=set_name, fdel=del_name, doc="The person's name.")
    # creates a property object called name — a special object that controls access to _name through getter, setter, and deleter functions.

p = Person("Alice")
print(p.name)    # Internally calls get_name() → 'Alice'

p.name = "Bob"   # Internally calls set_name("Bob")
print(p.name)    # 'Bob'

del p.name       # Internally calls del_name()
# ✅ Cleaner and looks like normal attribute access to users!

print('''

Summary of the Difference:

Without property()	With property()
You must call .get_name(), .set_name() manually	You just use .name naturally
Less Pythonic, more like Java style	More Pythonic, cleaner syntax
Methods are obviously exposed	Methods hidden behind attribute access
Good for very strict control	Good for most real-world usage

''')

print('''

Now, why does property() offer protection?

Because it gives you full control over how the attribute is accessed, changed, or deleted — 
even though the user thinks they are just accessing a normal attribute.

In other words:

The user believes they are working with a simple variable: p.name

But you decide exactly what happens when they read (get), write (set), or delete (del) it.

You can add checks, validations, transformations, logging, etc., inside your get_name, set_name, or del_name.

🎯 In contrast
Without property(), the user can freely modify internal attributes (p._name) directly without any control.

With property(), even though the syntax is clean, you hide the real implementation and intercept every action.

''')


# In[31]:


print('''

Example: Adding validation with property()

''')

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        if not value:
            raise ValueError("Name cannot be empty!")
        self._name = value

    def del_name(self):
        raise AttributeError("Cannot delete name!")

    name = property(fget=get_name, fset=set_name, fdel=del_name, doc="The person's name.")

p = Person("Alice")

print(p.name)      # ✅ 'Alice'
p.name = "Bob"     # ✅ OK
# p.name = ""        # ❌ ValueError: Name cannot be empty!
# p.name = 123       # ❌ ValueError: Name must be a string!
# del p.name         # ❌ AttributeError: Cannot delete name!


# In[ ]:





# In[32]:


print('''

Another useful and slightly more interesting example with property() —
this time, we'll add extra behavior, not just simple getting and setting.

''')


# In[33]:


print('''

A Temperature class :

Suppose you want to store temperature in Celsius, but also allow people to get and set the temperature in Fahrenheit.
We can use property() to make it feel natural! 
''')

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Internal storage is always Celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero (-273.15°C)!")
        self._celsius = value

    def get_fahrenheit(self):
        return self._celsius * 9/5 + 32

    def set_fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

    celsius = property(fget=get_celsius, fset=set_celsius, doc="Temperature in Celsius")
    fahrenheit = property(fget=get_fahrenheit, fset=set_fahrenheit, doc="Temperature in Fahrenheit")

# What happens?
# Celsius and fahrenheit are both PROPERTIES.
# Internally, temperature is always stored in Celsius (_celsius).
# But users can work with Fahrenheit directly if they want!

t = Temperature(0)  # 0°C

print(t.celsius)     # ➔ 0
print(t.fahrenheit)  # ➔ 32.0

t.fahrenheit = 212   # Set temperature by Fahrenheit
print(t.celsius)     # ➔ 100

# it feels like you're just setting a normal .fahrenheit value,
# but internally it's calculating and converting everything properly!

# Why is this a good example?
# Added value: we convert temperatures automatically.
# Validation: we prevent temperatures below absolute zero.
# User-friendliness: clean and intuitive usage (t.celsius, t.fahrenheit).


# In[ ]:





# In[23]:


print('''

What are @property, @name.setter, and @name.getter?

When you define a property in Python using @property,

you are setting up one object (a property object) that can have:
a getter (for reading)
a setter (for assigning)
a deleter (for deleting)

''')

print('''

Decorator	Purpose

@property	Define a getter
@name.setter	Define a setter for the same property
@name.deleter	Define a deleter for the same property
@name.getter	Redefine or replace the getter (rarely needed)

''')

# If you already created a property, you could use @name.getter to re-attach or replace the getter!
# class Person:
#    def __init__(self, name):
#        self._name = name
#
#    @property
#    def name(self):
#        """Getter"""
#        return self._name
#
#    @name.getter
#    def name(self):
#        """Another way to define getter (not typical)"""
#        return self._name + '!'

# But usually this is unnecessary unless you're doing advanced stuff, like redefining or updating the property dynamically.

class Person:
    def __init__(self, name):
        self._name = name

    @property  # Step 1: defines the getter
    def name(self):
        return self._name
# This creates a property called name that knows how to read (get) the value of _name.
# p.name : it internally runs: p.name() → returns self._name
    
    @name.setter  # Step 2: defines the setter
    def name(self, value):
        self._name = value

# Now, when you assign to name like: p.name = "Bob"
# it internally runs: p.name(value="Bob") → self._name = value
# Again, it looks like a simple attribute assignment — 
# but it runs your controlled code!
    
    @name.deleter  # Step 3: defines the deleter
    def name(self):
        del self._name

# This adds a deleter method to the name property.
# Now, when you write: del p.name
# it internally runs: del p._name

p = Person("Alice")

print(p.name)    # Alice (getter)
p.name = "Bob"   # (setter)
print(p.name)    # Bob
del p.name       # (deleter)


# In[ ]:





# In[24]:


print("Classes : example BankAccount() : balance = property(fget=_get_balance)")
print("Example code BankAccount() : version 2") 


# In[25]:


# Error Codes

# ERROR_CODE_INVALID_AMOUNT_DEPOSIT = 1
# ERROR_CODE_INVALID_AMOUNT_WITHDRAW = 2
# ERROR_CODE_NOT_ENOUGH_MONEY = 3
# ERROR_CODE_NONE = 4

# These are constants representing possible outcomes:
# 1 → Invalid deposit
# 2 → Invalid withdraw
# 3 → Not enough money
# 4 → No error (transaction successful)


# Error codes	No printing inside BankAccount methods, just return error codes
# manage()	    ATM function that interprets error codes and prints
# deposit() / withdraw()	Returns an error code instead of throwing exceptions or printing
# Encapsulation	__balance is private, balance is a read-only property

# Separation of concerns:

# BankAccount manages the money,
# ATM (manage()) manages printing error messages.
# Better for real-world programs where logic and presentation must be separated


# In[26]:


class BankAccount:
    
    ERROR_CODE_INVALID_AMOUNT_DEPOSIT = 1
    ERROR_CODE_INVALID_AMOUNT_WITHDRAW = 2
    ERROR_CODE_NOT_ENOUGH_MONEY = 3
    ERROR_CODE_NONE = 4

    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = balance

    def __str__(self):
        return '{}: ${}'.format(self._owner, self.__balance)

    def deposit(self, amount):
        if amount <= 0:
            return BankAccount.ERROR_CODE_INVALID_AMOUNT_DEPOSIT
        else:
            self.__balance += amount
            return BankAccount.ERROR_CODE_NONE

    def withdraw(self, amount):
        if amount <= 0:
            return BankAccount.ERROR_CODE_INVALID_AMOUNT_WITHDRAW
        elif amount > self.__balance:
            return BankAccount.ERROR_CODE_NOT_ENOUGH_MONEY
        else:
            self.__balance -= amount
            return BankAccount.ERROR_CODE_NONE

    def _get_balance(self):
        return self.__balance

    balance = property(fget = _get_balance)


# 1. if the withdrawal amount is greater than the balance
# withdraw won't happen and an error message should be printed as "Not enough money to withdraw"
# 2. both deposit and withdraw should not accept negative values
# if it happens, the transaction should not be complete and an error message
# should be printed as "Invalid amount to withdraw" or "Invalid amount to deposit"

if __name__ == '__main__':
    
    def manage(acct_func, amount):
        
        error_code = acct_func(amount)
        if error_code == BankAccount.ERROR_CODE_INVALID_AMOUNT_DEPOSIT:
            print('Invalid amount to deposit')
        elif error_code == BankAccount.ERROR_CODE_INVALID_AMOUNT_WITHDRAW:
            print('Invalid amount to withdraw')
        elif error_code == BankAccount.ERROR_CODE_NOT_ENOUGH_MONEY:
            print('Not enough money to withdraw')

    # ATM machine
    # the error message to be printed in the ATM console
    # print should be called here
    # error message to be properly generated here
    b = BankAccount('John', 1000)
    print(b)
    manage(b.deposit, 500)
    print(b)
    manage(b.withdraw, 2000)
    manage(b.deposit, -2000)
    print(b)

# manage() is a helper function that:

# Calls either a deposit or withdraw method on a BankAccount.
# Captures the returned error code.
# Prints a human-readable error message if something went wrong.

# Parameter	Meaning
# acct_func	A function — either deposit or withdraw of a BankAccount
# amount	How much money you want to deposit or withdraw

# ✨ Why is it smart?
# ✅ Separation of logic (BankAccount) and presentation (printing messages)
# ✅ Easy to change ATM behavior later (e.g., GUI, logs) without touching BankAccount class.


# In[ ]:





# In[ ]:


print("Another version of the code : ATM simulation : ")
print("Example code BankAccount() : version 3") 


# In[34]:


class InvalidAmountException(Exception):   # InvalidAmountException(Exception)

    TYPE_DEPOSIT = 1
    TYPE_WITHDRAW = 2

    def __init__(self, manage_type):
        self._manage_type = manage_type

    def _get_manage_type(self):
        return self._manage_type

    manage_type = property(fget=_get_manage_type) # manage_type property allows external access to _manage_type safely.

class NotEnoughMoneyException(Exception):
    def __init__(self, owner, amount):
        self._owner = owner
        self._amount = amount

    def _get_owner(self):
        return self._owner

    def _get_amount(self):
        return self._amount

    owner = property(fget=_get_owner)
    withdraw_amount = property(fget=_get_amount)

# property() is a built-in Python function that makes a method behave like an attribute.
# fget means "function to get the value" (getter).
# it connects the private methods _get_owner() and _get_amount() to public-looking attributes: owner and withdraw_amount.

# They allow you to access private data (_owner and _amount) like normal attributes, while still controlling access.
# Even though _owner and _amount are "protected" (with _ prefix), you can expose them read-only via owner and withdraw_amount.


class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = balance

    def __str__(self):
        return '{}: ${}'.format(self._owner, self.__balance)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException(InvalidAmountException.TYPE_DEPOSIT) # Raises InvalidAmountException if the amount is negative or zero.
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountException(InvalidAmountException.TYPE_WITHDRAW) # Raises InvalidAmountException if amount is ≤ 0.
        elif amount > self.__balance:
            raise NotEnoughMoneyException(self._owner, amount) # Raises NotEnoughMoneyException if withdrawal amount > balance.
        else:
            self.__balance -= amount

    def _get_balance(self):
        return self.__balance

    balance = property(fget=_get_balance)

# 1. if the withdrawal amount is greater than the balance
# withdraw won't happen and an error message should be printed as "Not enough money to withdraw"
# 2. both deposit and withdraw should not accept negative values
# if it happens, the transaction should not be complete and an error message
# should be printed as "Invalid amount to withdraw" or "Invalid amount to deposit"

if __name__ == '__main__':
    def manage(acct_func, amount):
        try:
            acct_func(amount)
        except NotEnoughMoneyException as ne:
            print('Not enough money to withdraw from {} account with ${}'.format(
                ne.owner,
                ne.withdraw_amount
            ))
        except InvalidAmountException as ie:
            msg = 'Invalid amount to withdraw' \
                if ie.manage_type == InvalidAmountException.TYPE_WITHDRAW \
                else 'Invalid amount to deposit'
            print(msg)
        except:
            print('Something goes wrong')

    # ATM machine
    # the error message to be printed in the ATM console
    # print should be called here
    # error message to be properly generated here
    b = BankAccount('John', 1000)
    print(b)
    manage(b.deposit, 500)
    print(b)
    manage(b.withdraw, 2000)
    manage(b.deposit, -2000)
    print(b)


# In[ ]:


print("Updated code : logging transactions")
print("Example code BankAccount() : version 4") 


# In[ ]:


class InvalidAmountException(Exception):
    TYPE_DEPOSIT = 1
    TYPE_WITHDRAW = 2

    def __init__(self, manage_type):
        self._manage_type = manage_type

    def _get_manage_type(self):
        return self._manage_type

    manage_type = property(fget=_get_manage_type)


class NotEnoughMoneyException(Exception):
    def __init__(self, owner, amount):
        self._owner = owner
        self._amount = amount

    def _get_owner(self):
        return self._owner

    def _get_amount(self):
        return self._amount

    owner = property(fget=_get_owner)
    withdraw_amount = property(fget=_get_amount)


class BankAccount:
    
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = balance
        self._transaction_log = []  # Transaction history

    def __str__(self):
        return f"{self._owner}: ${self.__balance}"

    def deposit(self, amount):
        if amount <= 0:
            self._transaction_log.append(f"Failed deposit: invalid amount ${amount}")
            raise InvalidAmountException(InvalidAmountException.TYPE_DEPOSIT)
        else:
            self.__balance += amount
            self._transaction_log.append(f"Deposit: ${amount} (new balance: ${self.__balance})")

    def withdraw(self, amount):
        if amount <= 0:
            self._transaction_log.append(f"Failed withdrawal: invalid amount ${amount}")
            raise InvalidAmountException(InvalidAmountException.TYPE_WITHDRAW)
        elif amount > self.__balance:
            self._transaction_log.append(f"Failed withdrawal: insufficient funds for ${amount}")
            raise NotEnoughMoneyException(self._owner, amount)
        else:
            self.__balance -= amount
            self._transaction_log.append(f"Withdrawal: ${amount} (new balance: ${self.__balance})")

    def _get_balance(self):
        return self.__balance

    balance = property(fget=_get_balance)

    def get_transaction_history(self):
        """Return the list of transaction logs."""
        return self._transaction_log


if __name__ == '__main__':
    def manage(acct_func, amount):
        try:
            acct_func(amount)
        except NotEnoughMoneyException as ne:
            print(f"Not enough money to withdraw from {ne.owner} account with ${ne.withdraw_amount}")
        except InvalidAmountException as ie:
            msg = "Invalid amount to withdraw" if ie.manage_type == InvalidAmountException.TYPE_WITHDRAW else "Invalid amount to deposit"
            print(msg)
        except Exception as e:
            print(f"An unexpected error occurred: {type(e).__name__} - {e}")

    # ATM Simulation
    b = BankAccount('John', 1000)
    print(b)

    manage(b.deposit, 500)   # Deposit $500
    print(b)

    manage(b.withdraw, 2000)  # Attempt to withdraw $2000 (should fail)
    manage(b.deposit, -2000)  # Attempt to deposit -$2000 (should fail)

    manage(b.withdraw, 400)   # Withdraw $400
    print(b)

    # Print Transaction Log
    print("\nTransaction History:")
    for entry in b.get_transaction_history():
        print(entry)


# In[ ]:





# In[ ]:




