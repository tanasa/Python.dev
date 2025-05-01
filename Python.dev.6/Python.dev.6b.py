#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## *italic* Python using inheritance, method overriding, and encapsulation
##  A constructor is a special method in a class that gets called automatically when you create a new object. Its main job is to initialize the object’s attributes — that is, to set up its internal state.

print("Inheritance :")


# In[8]:


print('''

Constructors :

A constructor is a special method in a class that gets called automatically when you create a new object. 
Its main job is to initialize the object’s attributes — that is, to set up its internal state.

In Python, the constructor is called __init__

''')


# In[ ]:


print("Example 1:")


# In[7]:


class Person:
    def __init__(self, name, age):
        self.name = name.upper()
        self.age = age

    def __str__(self):
        return 'My name is {} and I am {} years old.'.format(self.name, self.age)

    def happy_birthday(self):
        self.age += 1


class Student(Person):
    def __init__(self, name, age, school):
        # Person.__init__(self, name, age)           # working but not recommended
        super().__init__(name, age)                  # “Hey, use the Person constructor to initialize name and age.”
        self.school = school

    def __str__(self):
        return 'My name is {} and I am from {}!'.format(self.name, self.school)  # Overrides the Person.__str__ method:

    def graduate(self):
        self.name = 'Dr. {}'.format(self.name)

if __name__ == '__main__':
    
    john = Person('John', 18)
    print(john)
    john.happy_birthday()
    print(john)

    jack = Student('Jack', 20, 'Stanford')
    print(jack)
    jack.graduate()
    print(jack)

    # john.graduate()


# In[12]:


# "If Student inherits from Person, and Person.__init__() already defines name and age, why do we need to deal with them again in Student.

print('''

Here's the key distinction:

✅ Inheritance gives you access to the parent class methods and attributes,

❌ but it does NOT automatically call the parent class’s __init__() constructor unless you explicitly do so.

Jack = Student('Jack', 20, 'Stanford')

Python does:

Look for __init__() in Student.

Finds it — so it does not automatically call Person.__init__().

You must manually call the parent constructor using super().__init__(name, age) to initialize name and age.

💡 Think of it this way:

In Python, constructors (__init__) are not inherited the way other methods are. 

They’re overridden when you define a new __init__ in the child class.

You're not redefining the variables (name, age) — you're simply ensuring that the child class receives the needed inputs, so it can:

Initialize its own state (school)

And correctly delegate part of that state to the parent class (name, age)

Python doesn't magically pass constructor arguments from the child to the parent — you have to explicitly route them.

''')


# In[ ]:


print("Example 2:")


# In[15]:


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return '{}: ${}'.format(self.owner, self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# if the balance of a high-balance account is less than $1000 after withdraw
# add a $50 penalty
class HighBalanceAccount(BankAccount):  # To simulate a penalty system:
    
    def withdraw(self, amount):         # Overrides the withdraw() method from BankAccount
        # self.balance -= amount        # Instead of repeating the code self.balance -= amount, it uses:
        super().withdraw(amount)        # we use : super().withdraw(amount)
                                        # This calls the parent's withdraw() method
                                        # Why do we have amount here? Where is it coming from?
                                        # No, amount is not defined in the parent — it's passed in during the method call.
                                        # HighBalanceAccount.withdraw(h, 800)

# The amount comes from the user calling the method, not from the parent class.
# Why use super().withdraw(amount)?
# You're in a subclass, and you don’t want to duplicate the withdrawal logic from the parent. So instead of writing:
# self.balance -= amount
# You say: super().withdraw(amount)
# This calls the parent class (BankAccount)’s withdraw() method — and passes along the amount you received from the user.

        if self.balance < 1000:
                super().withdraw(50) 
        
if __name__ == '__main__':
    b = BankAccount('John', 1000)
    print(b)
    b.deposit(500)
    print(b)
    b.withdraw(800)
    print(b)

    print("calling High Balance Account")
    h = HighBalanceAccount('Jack', 1000)
    print(h)
    h.deposit(500)
    print(h)
    h.withdraw(800)
    print(h)


# In[16]:


print("Example 2: re-writing the code by GPT4")


# In[17]:


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'{self.owner}: ${self.balance}'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class HighBalanceAccount(BankAccount):
    
    def withdraw(self, amount):
        
        # First, withdraw the requested amount
        # amount is just a parameter, not an attribute
        # amount is local to the function.
        # It's passed in when the method is called.
        # It exists only inside the function — it is not stored in the object.
        # We do not have self.amount in the child class
        # Because we're not storing amount as part of the object
        
        super().withdraw(amount)

        # Then, check if the balance dropped below $1000
        
        if self.balance < 1000:      # self.balance is an instance attribute that was set earlier when the object was created.
                                     # It comes from the constructor in the parent class BankAccount
            print("Balance below $1000 — applying $50 penalty.")
            super().withdraw(50)     # Apply penalty
                                     # This calls the withdraw() method defined in the parent class

                                     # Summary
                                     # Expression	Comes from
                                     # self.balance	Set in the parent class's __init__()
                                     # super().withdraw(50)	Calls the parent class's withdraw()


if __name__ == '__main__':
    
    print("Regular Bank Account:")
    b = BankAccount('John', 1000)
    print(b)
    b.deposit(500)  # +$500 → $1500
    print(b)
    b.withdraw(800)  # -$800 → $700
    print(b)

    print("\n High Balance Account:")
    h = HighBalanceAccount('Jack', 1000) # Python does BankAccount.__init__(h, "Jack", 1000), self.balance = 1000
    print(h)
    h.deposit(500)   # +$500 → $1500
    print(h)
    h.withdraw(800)  # -$800 → $700 → penalty applied → $650
    print(h)


# In[ ]:


print("Example 3: re-writing the code by GPT4, changing the name of the functions")


# In[ ]:


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'{self.owner}: ${self.balance}'

    def deposit(self, amount):
        self.balance += amount

    def subtract_from_balance(self, amount):
        """This is the core balance update method (withdraw logic)"""
        self.balance -= amount


class HighBalanceAccount(BankAccount):
    def request_withdrawal(self, amount):
        """
        Handles a user-initiated withdrawal and applies a penalty
        if the balance falls below $1000.
        """

        # Subtract the withdrawal amount
        super().subtract_from_balance(amount)

        # Check if penalty should apply
        if self.balance < 1000:
            print("⚠️ Balance below $1000 — applying $50 penalty.")
            super().subtract_from_balance(50)


if __name__ == '__main__':
    print("Regular Bank Account:")
    b = BankAccount('John', 1000)
    print(b)
    b.deposit(500)
    print(b)
    b.subtract_from_balance(800)  # simulate withdrawal
    print(b)

    print("\n🟥 High Balance Account:")
    h = HighBalanceAccount('Jack', 1000)
    print(h)
    h.deposit(500)
    print(h)
    h.request_withdrawal(800)  # this triggers penalty logic
    print(h)


# In[ ]:





# In[ ]:





# In[ ]:




