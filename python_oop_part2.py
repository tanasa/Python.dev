#!/usr/bin/env python
# coding: utf-8

# In[1]:


# How to define and use classes (https://www.murach.com/shop/murach-s-python-programming-detail)

# chapter 15


# In[2]:


# INHERITANCE :

# parent class, superclass
# child class, subclass

# A subclass can add new attributes and methods to the superclass
# It can also override a method from the superclass, 
# by providing its own version of the method.


# In[3]:


# To define a subclass
# class SubClassName(SuperClassName):

# To call a method or constructor of the superclass
# SuperClassName.methodName(self[, argumentList])


# In[4]:


from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name


# In[5]:


# The code for the Book subclass

@dataclass
class Book(Product): # Python calls the constructor of the superclass
     author:str = "" # add another attribute to the
    
     # override the getDescription method
     def getDescription(self):
         return f"{Product.getDescription(self)} by" f"{self.author}"

# The code for the subclass
@dataclass
class Book(Product): # Python calls the constructor of the superclass
     author:str = "" # add another attribute
    
     # override the getDescription method
     def getDescription(self):
         return f"{Product.getDescription(self)} by " f"{self.author}"
        
 
@dataclass
class Movie(Product): # Python calls the constructor of the superclass
     year:int = "" # add another attribute
    
     # override the getDescription method
     def getDescription(self):
         return f"{Product.getDescription(self)} " f"({self.year})"                


# In[6]:


# The code for the Book subclass with a constructor

# class Book(Product):
#     def __init__(self, name="", price=0.0, discountPercent=0, author=""):
#
      # call the constructor of the superclass
#      Product.__init__(self, name, price, discountPercent)

      # set the author
#      self.author = author


# In[7]:


# POLYMORPHISMS

# if we access a method of a superclass, and the method is overwritten in the subclass, 
# polymorphism determines which method is executed first based on object's type.


# In[8]:


# Code that uses the overridden methods

def main():
    
    # a tuple of Product objects
    products = (

        Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
        Book("The Big Short", 15.95, 34, "Michael Lewis"),
        Movie("The Holy Grail - DVD", 14.99, 68, 1975))
    
    print("PRODUCTS")
    print("")
    
    for product in products:
        print(product.getDescription())
        print()
    
if __name__ == "__main__":
   main()


# In[9]:


# A function for checking the object's type : isinstance(object)


# In[10]:


def show_product(product):
    
    w = 18
    print("PRODUCT DATA")
    
    print(f"{'Name:':{w}}{product.name}")

    if isinstance(product, Book):
        print(f"{'Author:':{w}}{product.author}")

    if isinstance(product, Movie):
        print(f"{'Year:':{w}}{product.year}")

    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    
    print()
    
def show_products(products):
    print("PRODUCTS")

    for i, product in enumerate(products, start=1):
         print(f"{i}. {product.getDescription()}")
         print()
        
def get_products():
    # return a tuple of Product, Book, and Movie objects
      return (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
              Book("The Big Short", 15.95, 34, "Michael Lewis"),
              Movie("The Holy Grail - DVD", 14.99, 68, 1975))


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


# In[ ]:


# __str__ METHOD : 

# it is a method that is called when the object needs to be converted to a string
# returns the name of the class and the value of the names and attributes


# In[ ]:


# __iter__ METHOD : 

# __iter__(self) : returns the iterator for an object and 
# initializes the index of the iterator
# We we can use the "yield" keyword in an iterator.

# An ITERATOR : allows the items to be processed one at a time in a sequence


# In[12]:


def main():
    print("The Dice Roller program\n")
    
    # Uncomment the following lines to allow user input for the number of dice
    # try:
    #     count = int(input("Enter the number of dice to roll: "))
    #     if count <= 0:
    #         raise ValueError
    # except ValueError:
    #     print("Please enter a valid positive integer.")
    #     return

    count = 5  # Default number of dice
    
    # Create a Dice object and add Die objects to it
    dice = Dice()
    for _ in range(count):
        die = Die()
        dice.addDie(die)
    
    # Initial roll
    dice.rollAll()
    print("YOUR ROLL: ", end="")
    
    for die in dice:
        print(die.value, end=" ")
    print("\n")
    
    # Interactive rolling
    
    while True:
        choice = input("Roll again? (y/n): ").strip().lower()
    
        if choice == 'y':
            dice.rollAll()
            print("YOUR ROLL: ", end="")
            for die in dice:
                print(die.value, end=" ")
            print("\n")
        elif choice == 'n':
            print("Bye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()

