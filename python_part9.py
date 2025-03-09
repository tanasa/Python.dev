#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Simple examples of OOP using @dataclass


# In[39]:


from dataclasses import dataclass

@dataclass
class Multiplier:
    num1:int = 0
    num2:int = 0

    def getProduct(self):
        return self.num1 * self.num2

def main():
    m = Multiplier()
    m.num1 = 7
    m.num2 = 3
    print(f"{m.num1} X {m.num2} = {m.getProduct()}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[40]:


# OBJECT COMPOSITION and ENCAPSULATION : 


# In[41]:


from dataclasses import dataclass, field
import random

@dataclass
class Die:
    _value: int = field(default=1, init=False)  # Start with default value of 1

    def getValue(self):
        return self._value  # Access the protected attribute _value

    def setValue(self, value):
       if value < 1 or value > 6:
           raise ValueError("Die value must be from 1 to 6.")
       else:
           self.__value = value
        #  self._value = value  # Allow controlled setting of _value
               
    def roll(self):
        self._value = random.randrange(1, 7)  # Update _value with a random roll

class Dice:
    def __init__(self):
        self.dice_list = []  # More descriptive name for list of dice
  
    def addDie(self, die):
        self.dice_list.append(die)

    def rollAll(self):
        for die in self.dice_list:
            die.roll()

def main():
    print("The Dice Roller program")
    print()
   
    # Get number of dice from user
    count = int(input("Enter the number of dice to roll: "))
   
    # Create Dice object and add Die objects to it
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    # Optionally set initial values using setValue
    print("Setting initial values for each die:")
    for index, die in enumerate(dice.dice_list, start=1):
        initial_value = index % 6 + 1  # Set initial values in a range from 1 to 6
        die.setValue(initial_value)
        print(f"Die {index} initial value set to: {die.getValue()}")

    choice = "y"
    while choice.lower() == "y":
        # Roll the dice
        dice.rollAll()
 
        # Display to the user
        print("YOUR ROLL: ", end="")
       
        for die in dice.dice_list:
            print(die.getValue(), end=" ")  # Access the die value
        print("\n")
 
        choice = input("Roll again? (y/n): ")

    print("Bye!")

if __name__ == "__main__":
    main()


# In[42]:


# We can re-write the code above by using two decorators :
# @ property 
# @ <property_name>.setter
# @ <property_name>.getter


# In[43]:


from dataclasses import dataclass, field
import random

@dataclass
class Die:
    _value: int = field(default=1, init=False)  # Initialize with default value of 1

    @property
    def value(self):
        """Getter for the die's value."""
        return self._value

    @value.setter
    def value(self, value):
        """Setter for the die's value, allowing controlled access."""
        self._value = value

    def roll(self):
        """Simulate rolling the die and update _value with a random number between 1 and 6."""
        self._value = random.randrange(1, 7)

class Dice:
    def __init__(self):
        self.dice_list = []  # Holds the list of Die objects
  
    def addDie(self, die):
        self.dice_list.append(die)

    def rollAll(self):
        for die in self.dice_list:
            die.roll()

def main():
    print("The Dice Roller program")
    print()
   
    # Get number of dice from user
    count = int(input("Enter the number of dice to roll: "))
   
    # Create Dice object and add Die objects to it
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    # Optionally set initial values using the property setter
    print("Setting initial values for each die:")
    for index, die in enumerate(dice.dice_list, start = 1):
        die.value = (index % 6) + 1  # Set initial values using the property setter
        print(f"Die {index} initial value set to: {die.value}")  # Access using the property getter

    choice = "y"
    while choice.lower() == "y":
        # Roll the dice
        dice.rollAll()
 
        # Display to the user
        print("YOUR ROLL: ", end="")
       
        for die in dice.dice_list:
            print(die.value, end=" ")  # Access using the property getter
        print("\n")
 
        choice = input("Roll again? (y/n): ")

    print("Bye!")

if __name__ == "__main__":
    main()


# In[44]:


# Providing an example with other decorator @<property_name>.setter:
# @ property 
# @ <property_name>.setter
# @ <property_name>.getter


# In[45]:


class MyClass:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        """Getter for value"""
        return self._value

    @value.getter
    def value(self):
        """This is the same as the previous getter, but defined explicitly."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter for value"""
        self._value = new_value

# Create an instance of MyClass
my_instance = MyClass()

# Access the value using the getter
print("Initial value:", my_instance.value)  # Output: 0

# Set a new value using the setter
my_instance.value = 42

# Access the updated value
print("Updated value:", my_instance.value)  # Output: 42


# In[46]:


# Example with @property, @<property_name>.getter, and @<property_name>.setter


# In[47]:


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Private attribute to store the temperature in Celsius

    @property
    def celsius(self):
        """Getter for Celsius temperature."""
        return self._celsius

    @celsius.getter
    def celsius(self):
        """Explicit Celsius getter with additional behavior."""
        print("Accessing the temperature in Celsius")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for Celsius temperature with validation."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Getter for Fahrenheit temperature, computed from Celsius."""
        return (self._celsius * 9/5) + 32

    @fahrenheit.getter
    def fahrenheit(self):
        """Explicit Fahrenheit getter with additional behavior."""
        print("Accessing the temperature in Fahrenheit")
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for Fahrenheit temperature, setting the Celsius equivalent."""
        self._celsius = (value - 32) * 5/9

# Using the Temperature class
temp = Temperature(25)   # Initialize temperature to 25°C
print(temp.celsius)      # Accessing in Celsius, calls the custom getter
temp.celsius = 30        # Set new temperature in Celsius

print(temp.fahrenheit)   # Access temperature in Fahrenheit, calls the custom getter
temp.fahrenheit = 86     # Set temperature in Fahrenheit, updating Celsius
print(temp.celsius)      # Access the updated Celsius temperature


# In[48]:


# Here is another example, demonstrating a Rectangle class with width and height attributes. 
# It uses properties and custom getters/setters to calculate and update the area.


# In[49]:


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter for width."""
        return self._width

    @width.getter
    def width(self):
        """Explicit getter for width."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for width, ensuring it's positive."""
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        """Getter for height."""
        return self._height

    @height.getter
    def height(self):
        """Explicit getter for height."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for height, ensuring it's positive."""
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        """Calculates the area based on width and height."""
        return self._width * self._height

    @area.getter
    def area(self):
        """Explicit getter for area."""
        return self._width * self._height


# Usage of Rectangle class
rect = Rectangle(5, 10)

# Access width and height using the getters
print("Width:", rect.width)    # Output: 5
print("Height:", rect.height)  # Output: 10

# Access area (computed property)
print("Area:", rect.area)      # Output: 50

# Update width and height using the setters
rect.width = 7
rect.height = 14

# Access updated values and area
print("Updated Width:", rect.width)   # Output: 7
print("Updated Height:", rect.height) # Output: 14
print("Updated Area:", rect.area)     # Output: 98


# In[50]:


# PRODUCTS


# In[51]:


from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:float = 0
 
    def getDescription(self):
        return self.name

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100
 
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
   
@dataclass
class Book(Product):
    author:str = ""
 
    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.author}"
               
class Movie(Product):
    year:int = 0
 
    def getDescription(self):
        return f"{Product.getDescription(self)} ({str(self.year)})"

 
product = Book("Catcher in the Rye", 9.99, "J. D. Salinger")
if isinstance(product, Product):
    print("This is a product.")
if isinstance(product, Movie):
    print("This is a movie.")
if isinstance(product, Book):
    print("This is a book.")


# In[52]:


## def show_products(products):
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
              print("Product number out of range. "
                    "Please try again.")
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





# In[53]:


# the __iter__ method :


# In[54]:


# The __iter__ method is a special method in Python that makes an object iterable.


# In[55]:


# It is part of Python’s iterator protocol, which allows objects to be looped over in a for loop or used with functions 
# like list(), sum(), and many others that require iterable objects. 
# When you define __iter__ in a class, you're essentially telling Python how to start iterating over instances of that class.


# In[56]:


# By defining __iter__, you control the behavior of iteration for your class, 
# allowing for custom sequences or iterating over specific properties


# In[57]:


class MyNumbers:
    
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0  # Track the current state for iteration

    def __iter__(self):
        self.current = 0  # Reset for new iteration
        return self  # Returning self, because this class also defines __next__

    def __next__(self):
        if self.current < self.max_num:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration  # End of iteration
            
numbers = MyNumbers(5)
for number in numbers:
    print(number)  # Output will be 0, 1, 2, 3, 4

# When for number in numbers: is called, Python internally calls numbers.__iter__(). 
# Since MyNumbers returns self from __iter__, the same instance becomes its own iterator.
# __next__: Python repeatedly calls __next__() on the object until StopIteration is raised, signaling the end of the sequence.


# In[58]:


class UpperCaseNames:
    def __init__(self, names):
        self.names = names
        self.index = 0  # Track the position in the list for iteration

    def __iter__(self):
        self.index = 0  # Reset the index each time a new iteration starts
        return self

    def __next__(self):
        if self.index < len(self.names):
            current_name = self.names[self.index].upper()  # Get the current name in uppercase
            self.index += 1
            return current_name
        else:
            raise StopIteration  # End of iteration


names = UpperCaseNames(["alice", "bob", "charlie"])
for name in names:
    print(name)  # Output will be ALICE, BOB, CHARLIE


# In[59]:


# __iter__: When the for loop begins, names.__iter__() is called, setting self.index to 0 and returning self.
# __next__: Each time __next__() is called, it:

#    Checks if self.index is within the list length.
#    Converts the name at the current index to uppercase.
#    Increments the index by 1 and returns the name in uppercase.

# StopIteration: Once self.index reaches the end of the list, StopIteration is raised, ending the iteration.


# In[60]:


class Fibonacci:
    def __init__(self, max_count):
        self.max_count = max_count  # Total terms to generate
        self.count = 0              # Track the current term count
        self.a, self.b = 0, 1       # Starting values for the Fibonacci sequence

    def __iter__(self):
        self.count = 0  # Reset count each time a new iteration starts
        self.a, self.b = 0, 1  # Reset the first two Fibonacci numbers
        return self

    def __next__(self):
        if self.count < self.max_count:
            self.count += 1
            value = self.a
            self.a, self.b = self.b, self.a + self.b  # Update to the next pair in the sequence
            return value
        else:
            raise StopIteration  # End of iteration


fib_sequence = Fibonacci(10)
for number in fib_sequence:
    print(number)  # Output will be the first 10 Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


# In[61]:


# In the example below :

# __init__: Sets up the initial and ending values.
# __iter__: Returns self, making the class its own iterator.
# __next__:

# Checks if current is within the range (i.e., less than or equal to end).
# If so, it returns current and increments it for the next call.
# Once current exceeds end, it raises StopIteration, ending the loop.


# In[ ]:





# In[62]:


class Counter:
    def __init__(self, start, end):
        self.current = start  # Starting point
        self.end = end        # Maximum limit for counting

    def __iter__(self):
        return self  # Returning self because this object is its own iterator

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1  # Move to the next number
            return value
        else:
            raise StopIteration  # End of iteration


counter = Counter(1, 5)
for number in counter:
    print(number)  # Output: 1, 2, 3, 4, 5


# In[63]:


# __post_init__ is a special method used in data classes. 
# Data classes were introduced in Python 3.7 via the dataclasses module 
# to provide a convenient way to define classes that primarily store data.

# The __post_init__ method is unique to data classes and allows you to customize what happens right after the generated __init__ method runs.
# It’s especially useful for any additional initialization or validation you might need after the main __init__ method 
# has populated the fields.

# additional INITIALIZATION
# additional VALIDATION


# In[64]:


from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

# Usage
try:
    person = Person("Alice", -5)
except ValueError as e:
    print(e)  # Output: Age cannot be negative


# In[65]:


from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")

# Usage
try:
    emp = Employee("John Doe", -5000)
except ValueError as e:
    print(e)  # Output: Salary cannot be negative


# In[66]:


from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    range_min: float = 0.0
    range_max: float = 100.0

    def __post_init__(self):
        if not (self.range_min <= self.x <= self.range_max):
            raise ValueError(f"x must be between {self.range_min} and {self.range_max}")
        if not (self.range_min <= self.y <= self.range_max):
            raise ValueError(f"y must be between {self.range_min} and {self.range_max}")

# Usage
try:
    point = Point(150, 50)
except ValueError as e:
    print(e)  # Output: x must be between 0.0 and 100.0


# In[ ]:





# In[67]:


# the __str__ method :


# In[68]:


# The __str__ method in a Python class is a special method that is used to define a human-readable string representation of an object. 
# When you call the str() function or use the print() function on an instance of a class, Python looks for this method to determine 
# how to convert the object to a string.

# Purpose of __str__
# Human-Readable Output: The main goal of __str__ is to provide a user-friendly string representation of an object. 
# This representation is typically more informal and easier to understand than the output of __repr__.
# Custom Formatting: You can customize how the object is presented when converted to a string, making it clearer what the object represents.


# In[69]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Usage
person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old


# In[70]:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# Usage
car = Car("Toyota", "Camry", 2022)
print(car)  # Output: 2022 Toyota Camry


# In[71]:


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"


book = Book("1984", "George Orwell")
print(str(book))   # Output: 1984 by George Orwell
print(repr(book))  # Output: Book(title='1984', author='George Orwell')


# In[72]:


# The __repr__ method in Python is a special method that defines a formal string representation of an object. 
# The primary purpose of __repr__ is to provide an unambiguous string representation that ideally could be used to recreate the object. 
# This is especially useful for debugging and logging, as it gives developers insight into the internal state of an object.


# In[73]:


def __repr__(self):
    return "string representation"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


point = Point(3, 4)
print(repr(point))  # Output: Point(x=3, y=4)

# __repr__ Method: Returns a string that includes the class name and the values of its attributes in a way that could help reconstruct the object.
# Printing the Object: When you call repr(point), it invokes the __repr__ method, resulting in the output "Point(x=3, y=4)".

