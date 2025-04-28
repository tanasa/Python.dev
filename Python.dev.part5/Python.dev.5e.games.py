#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print("Input :")

name = input('What is your name? ')
print('Hello {}!'.format(name))

age = int(input('How old are you? '))
age += 1
print('You will be {} next year.'.format(age))


# In[2]:


# Generate 500 random words and write them into a text file:

import random

# Sample list of words to pick from
words = ['apple', 'banana', 'cherry', 'date', 'elephant', 'flower', 'grape', 'house', 'ice', 'jungle', 
         'kite', 'lemon', 'mountain', 'night', 'orange', 'penguin', 'queen', 'river', 'sun', 'tree', 
         'umbrella', 'violet', 'whale', 'xylophone', 'yacht', 'zebra']

# Open a file for writing
with open('zwords.txt', 'w') as file:
    for _ in range(500):
        word = random.choice(words)
        file.write(word + '\n')  # Write each word on a new line

print("500 random words have been written to 'zwords.txt'.")


# In[ ]:





# In[ ]:





# In[3]:


print("Random Art")


# In[4]:


# random.randint(a, b)
# random.choice(seq)
# random.shuffle(seq)

# Function	What it does	Example
# random.random()	Returns random float between 0 and 1	random.random() → 0.472
# random.uniform(a, b)	Returns random float between a and b	random.uniform(1.5, 5.5)
# random.sample(seq, k)	Returns k unique elements randomly from the sequence	random.sample([1,2,3,4], 2) → [2,4]
# random.seed(n)	Initializes the random number generator to make results repeatable


# In[5]:


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


# In[ ]:





# In[6]:


import random

class RandomWordGenerator:
    def __init__(self, filename, min_len, max_len):
        self._word_list = []

        with open(filename) as fin:
            for word in fin:
                word = word.strip().lower()
                if min_len <= len(word) <= max_len:
                    self._word_list.append(word)

    def _get_random_word(self):
        return random.choice(self._word_list)

    random_word = property(fget=_get_random_word)

if __name__ == '__main__':
    word_gen = RandomWordGenerator('zwords.txt', 5, 8)
    for _ in range(10):
        print(word_gen.random_word)   


# In[ ]:





# In[7]:


# Tkinter is a standard GUI (Graphical User Interface) library for Python. It provides tools and widgets necessary for creating desktop applications 
# with graphical elements.


# In[ ]:





# In[8]:


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
    canvas.create_rectangle(left, top, right, bottom, outline=color) # Draws a rectangle on the canvas using create_rectangle().
    # ✅ Each time you call draw_rectangle(canvas), you get one colorful random rectangle.

for _ in range(1000):
    draw_rectangle(canvas)

window.mainloop()

# Draw Many Rectangles
# Loops 1000 times.
# Each loop, draws one random rectangle on the canvas.
# Result: the canvas becomes full of colorful, overlapping random rectangles!
# ✅ 🎨 It will look like a chaotic abstract "modern art" painting


# In[ ]:





# In[9]:


print("Interactive Game:")


# In[10]:


from abc import ABC, abstractmethod

class InteractiveGame(ABC):
    @abstractmethod
    def get_instruction(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    def _get_prompt(self):
        return 'What is your guess? '

    @abstractmethod
    def can_continue(self):
        pass

    @abstractmethod
    def validate(self, guess):
        pass

    @abstractmethod
    def evaluate(self, valid_guess):
        pass

    @abstractmethod
    def respond(self, result):
        pass

    prompt = property(fget=_get_prompt)


# In[ ]:





# In[11]:


class Hangman(InteractiveGame):
    def __init__(self):
        self._tries = 8
        self._secret_word = RandomWordGenerator('zwords.txt', 5, 8).random_word
        self._guessed_letters = []
        self._guessed_word_so_far = ['_'] * len(self._secret_word)

    def get_instruction(self):
        return 'Guess my secret word.'

    def validate(self, guess):
        if len(guess) != 1:
            raise ValueError('Invalid guess: one letter at a time')
        elif guess > 'z' or guess < 'a':
            raise ValueError('Invalid guess: type a lower-case letter')

        return guess

    def evaluate(self, valid_guess):
        self._guessed_letters.append(valid_guess)

        # self._secret_word: hello
        # self._guessed_word_so_far: ['_', '_', '_', '_', '_']
        # valid_guess: 'e'
        # self._guessed_word_so_far: ['_', 'e', '_', '_', '_']

        for index, letter in enumerate(self._secret_word):
            if letter == valid_guess:
                self._guessed_word_so_far[index] = valid_guess

        if '_' not in self._guessed_word_so_far:
            return True, None
        else:
            if valid_guess not in self._secret_word:
                self._tries -= 1
            return False, ' '.join(self._guessed_word_so_far)

    def get_status(self):
        
        result = 'You have {} {} to guess my secret word.'.format(
            self._tries,
            'chances' if self._tries > 1 else 'chance'
        )
        
        result += '\n'
        result += 'Used letters: {}'.format(' '.join(self._guessed_letters))
        return result

    def can_continue(self):
        return self._tries > 0

    def respond(self, result):
        if result:
            return 'Congratulations! You have guessed my secret word: {}.'.format(self._secret_word)
        else:
            return 'Sorry! My secret word is {}.'.format(self._secret_word)


# In[ ]:





# In[12]:


class InteractiveGameDriver:
    def __init__(self, game):
        if not isinstance(game, InteractiveGame):
            raise ValueError('Invalid game')
        self._game = game

    def play(self):
        print(self._game.get_instruction())

        while self._game.can_continue():
            print(self._game.get_status())

            guess = input(self._game.prompt)
            try:
                valid_guess = self._game.validate(guess)
                result, hint = self._game.evaluate(valid_guess)

                if result:
                    break
                elif hint is not None:
                    print(hint)

            except ValueError as err:
                print(err)

        print(self._game.respond(result))


# In[13]:


if __name__ == '__main__':
    dr = InteractiveGameDriver(Hangman())
    dr.play()


# In[ ]:




