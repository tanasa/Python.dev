#!/usr/bin/env python
# coding: utf-8

# In[1]:


# How to define and use classes (https://www.murach.com/shop/murach-s-python-programming-detail)

# chapter 14

# UML (Unified Modeling Language) is the industry standard used to describe the classes and objects 
# of an object-oriented application

# Objectives :

# Describe the concept of object composition.
# Describe the concept of encapsulation.
# Distinguish between public and private attributes.
# Describe the use of getter and setter methods.


# In[2]:


# In Python, __init__() is a special method known as the initializer or CONSTRUCTOR of a class. 

# It is automatically invoked when a new instance of the class is created. 
# The primary purpose of the __init__() method is to initialize the object's attributes 
# with specific values or perform any setup required for the new instance.

# The __init__() method is typically used to set up the initial state of an object 
# by assigning values to the object's attributes.


# In[3]:


# The double underscores are part of Python's naming conventions for special or "MAGIC" methods. 
# These special methods are used by Python to handle certain object-oriented programming tasks automatically.

# These methods are not meant to be directly called by users but are instead invoked automatically by Python 
# when certain actions are performed on an object.


# In[4]:


# OOP groups VARIABLES and FUNCTIONS into data structures called OBJECTS

# a CLASS has :

# ATTRIBUTES
# METHODS

# Once you create an object from a class, the object has :

# an IDENTITY (an unique address)
# a STATE (the data that it stores)
# a BEHAVIOUR (the methods that it contains)

# The process of creating an object from a CLASS is called INSTANTIATION.

# ENCAPSULATION (data hiding): allows to hide the data attributes of an object from other code that uses the object.


# In[5]:


import sys
import os

sys.path.append('/home/bogdan/miniconda3/lib/python3.9/site-packages')


# In[6]:


# from module_name import ClassName1[, ClassName2]...

from dataclasses import dataclass
import objects

# a class called Product :
# a class with three attributes and two methods

# The dataclass decorator of the data classes module allows you to add attributes to your classes
# without having to explicitly code a constructor method.

# The methods of a class must take a reference to the object itself as their first parameters 
# (it is called self).

@dataclass # a dataclass decorator

class Product:
    name:str = ""              # attribute 1
    price:float = 0.0          # attribute 2
    discountPercent:float = 0.0  # attribute 3
  
    # a method that uses two attributes
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100
  
    # a method that calls another method
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()


# In[7]:


# to create an object
# objectName = ClassName([parameters])


# In[8]:


# create two product objects

product1 = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62)
product2 = Product('National Hardware 3/4" Wire Nails', 5.06, 0)


# In[9]:


# print data for product1 to console

print("PRODUCT DATA")
print(f"Name: {product1.name}")
print(f"Price: {product1.price:.2f}")
print(f"Discount percent: {product1.discountPercent:d}%")
print(f"Discount amount: {product1.getDiscountAmount():.2f}")
print(f"Discount price: {product1.getDiscountPrice():.2f}")


# In[10]:


# print data for product2 to console

print("PRODUCT DATA")
print(f"Name: {product2.name}")
print(f"Price: {product2.price:.2f}")
print(f"Discount percent: {product2.discountPercent:d}%")
print(f"Discount amount: {product2.getDiscountAmount():.2f}")
print(f"Discount price: {product2.getDiscountPrice():.2f}")


# In[11]:


# To access the ATTRIBUTES of an object : 

# objectName.attributeName

# SET an attribute :
product1.discountPercent = 40

# GET an attribute :
percent = product1.discountPercent
print(percent)


# In[12]:


# To access the METHODS of an object : 

# objectName.methodName[(parameters)]


# In[13]:


# The syntax of a class with attributes

# With a dataclass DECORATOR :

# @dataclass                           # dataclass decorator
# class ClassName:
#    attrName1:type [= default_value] # first attribute
#    attrName2:type [= default_value] # second attribute
# ...

# With a CONSTRUCTOR :

# class ClassName:
#    def __init__(self[, parameters]): # the constructor
#        self.attrName1 = attrValue1       # first attribute
#        self.attrName2 = attrValue2       # second attribute
        
# Like any other method, an __init__() or __post_init__() method must take a reference to
# the object itself as its first parameters. This reference is called SELF.


# In[14]:


# An example by using __init__ : a class that has three attributes

class Product:
    def __init__(self, name = "", price = 0.0, discount_percent = 0):
        self.name = name
        self.price = price
        self.discountPercent = discount_percent

    def getDiscountAmount(self):
        
        discountAmount = self.price * self.discountPercent / 100
        return discountAmount
    
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
    

# discountAmount = product.getDiscountAmount()
# discountPrice = product.getDiscountPrice()


# In[15]:


# more functions : 

def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.name}")
    print()
    
def show_product(product):
    w = 18
    print(f"{'Name:':{w}}{product.name}")
    print(f"{'Price:':{w}}{product.price:.2f}")
    print(f"{'Discount percent:':{w}}{product.discountPercent:d}%")
    print(f"{'Discount amount:':{w}}{product.getDiscountAmount():.2f}")
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print()
    
def get_products():
    # return a tuple of Product objects
    return (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
            Product('National Hardware 3/4" Wire Nails', 5.06, 0),
            Product("Economy Duct Tape, 60 yds, Silver", 7.24, 0))

def get_product(products):
    while True:
        try:
            number = int(input("Enter product number: "))
            if number < 1 or number > len(products):
                print("Product number out of range. Please try again.")
            else:
                return products[number-1]
        except ValueError:
                print("Invalid number. Please try again.")
        print()
                      
                      
def main():
    print("The Product Viewer program")
    print()

    products = get_products()
    show_products(products)
    choice = "y"

    while choice.lower() == "y":
          product = get_product(products)
          show_product(product)
          
          choice = input("View another product? (y/n): ")
          print()

    print("Bye!")
                      
if __name__ == "__main__":
   main()


# In[16]:


# OBJECT COMPOSITION :

# it is a way to combine SIMPLE objects into COMPLEX objects.
# for example, a DICE object may contain multiple DIE object.

import random
from dataclasses import dataclass

@dataclass
class Die:
     value:int = 1
    
     def roll(self):
        self.value = random.randrange(1, 7)

class Dice:
        # explicit constructor
        def __init__(self):
            self.list = []

        def addDie(self, die):
            self.list.append(die)

        def rollAll(self):
            for die in self.list:
                die.roll()
                

def main():
    print("The Dice Roller program")
    print()
    
    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))

    # create Dice object and add Die objects to it
    dice = Dice()
    
    for i in range(count):
        die = Die()
        dice.addDie(die)
        
        choice = "y"

        while choice.lower() == "y":
              # roll the dice
              dice.rollAll()

              # display to the user
              print("YOUR ROLL: ", end="")

              for die in dice.list:
                   print(die.value, end=" ")
              print("\n")
            
              choice = input("Roll again? (y/n): ")

        print("Bye!")
            
if __name__ == "__main__":
     main()


# In[18]:


# get the number of dice from the user
# count = int(input("Enter the number of dice to roll: "))

count = 5

dice = Dice()
for i in range(count):
    die = Die()
    dice.addDie(die)
    
print(die.value)
die.roll()

print(dice.list)
dice.rollAll()


# In[19]:


# ENCAPSULATION (data hiding)


# In[20]:


# PUBLIC METHODS
# PRIVATE METHODS : these can be accessed indirectly through public methods / INTERFACES


# In[21]:


# for example : for the class Die described above :

# __value : a PRIVATE ATTRIBUTE
# getValue() : PUBLIC METHOD to get the ATTRIBUTE
# setValue() : PUBLIC METHOD to set the ATTRIBUTE
# roll()  : a PUBLIC METHOD

# The double underscores (__) identify the attributes that are private.


# In[22]:


# The Die class with a PUBLIC ATTRIBUTE named value

@dataclass
class Die:
    value:int = 1
    
    def roll(self):
        self.value = random.randrange(1, 7)
        return self.value

# Code that directly SETS and GETS the public attribute

die = Die()
die.value = 7 
print("Die:", die.value)


# In[23]:


# The Die class with a PRIVATE ATTRIBUTE named __value

@dataclass
class Die:
    __value:int = 1

    def getValue(self):
        return self.__value

    def roll(self):
        self.__value = random.randrange(1, 7)

# Code that attempts to directly set a private attribute

die = Die()
die.__value = 6
print("Die:", die.getValue())


# In[24]:


# The Die class with methods that access a PRIVATE ATTRIBUTE :
# getValue
# setValue

@dataclass
class Die:
    __value:int = 1

    def getValue(self):
        return self.__value

    def setValue(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
        else:
            self.__value = value

    def roll(self):
        self.__value = random.randrange(1, 7)


# In[25]:


# GETTER method : gets the value of an attribute (ACCESSOR)
# SETTER method : sets the value of an attribute (MUTATOR)

die = Die()
die.setValue(6)
print("Die:", die.getValue())

# using invalid data : 
# die = Die()
# die.setValue(-1)


# In[26]:


# A PROPERTY : a type of method that is used to GET and SET a PRIVATE ATTRIBUTE

# @property : the getter method for the property
# @propertyName.setter : the setter method for the specified property


# In[28]:


# A Die class that uses a property to access a private attribute

@dataclass
class Die:
     __value:int = 1

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
    else:
        self.__value = value


# In[29]:


die = Die()
die.value = 6
print("Die:", die.value)

# die = Die()
# die.value = -1


# In[30]:


# If we only code a GETTER, we create a READ-ONLY property ; 
# if we only code a SETTER, we create a WRITE-ONLY property.


# In[31]:


import random
from dataclasses import dataclass
@dataclass
class Die:
     __value:int = 1

     @property # read-only
     def value(self):
         return self.__value

     def roll(self):
         self.__value = random.randrange(1, 7)


# In[32]:


class Dice:
    def __init__(self):
        self.__list = []

    @property # read-only
    def list(self):
        return tuple(self.__list)

    def addDie(self, die):
        self.__list.append(die)

    def rollAll(self):
        for die in self.__list:
            die.roll()
            


# In[33]:


# The __post_init__() method in Python is a special method used in conjunction with the @dataclass decorator 
# from the dataclasses module.
# ● It is called after the __init__() method has been executed and all the fields of the dataclass 
# have been initialized.
# ● The primary purpose of __post_init__() is to perform additional initialization or validation tasks 
# that depend on the values of the dataclass fields.

