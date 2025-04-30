#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[7]:


# write Python code to read all the words from words.txt
# print all the words that start with x

with open('znames.txt') as fin:
    for line in fin:
        word = line.strip()
        if word.lower().startswith('x'):
            print(word)


# In[ ]:





# In[8]:


from word_checker import is_abecedarian

# write Python code to read all the words from zwords.txt
# print all the words that are palindrome
# print(is_palindrome('kayak'))

with open('znames.txt') as fin:
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)


# In[ ]:





# In[9]:


from word_checker import is_palindrome

# write the Python code to find the longest palindrome word in words.txt

# longest_palindrome_so_far

with open('znames.txt') as fin:
    longest_so_far = ''
    for line in fin:
        word = line.strip()
        if is_palindrome(word):
            if len(word) >= len(longest_so_far):
                longest_so_far = word
    print(longest_so_far)


# In[ ]:





# In[11]:


from word_checker import is_palindrome, is_abecedarian

# write the Python code to find
# both the first longest palindrome word
# and the first longest abecedarian word
# in znames.txt

# with open('words.txt') as fin:
#     longest_palindrome_so_far = ''
#     longest_abecedarian_so_far = ''
#     for line in fin:
#         word = line.strip()
#         if is_palindrome(word):
#             if len(word) > len(longest_palindrome_so_far):
#                 longest_palindrome_so_far = word
#         if is_abecedarian(word):
#             if len(word) > len(longest_abecedarian_so_far):
#                 longest_abecedarian_so_far = word
#     print(longest_palindrome_so_far)
#     print(longest_abecedarian_so_far)

# def find_longest_palindrome():
#     with open('words.txt') as fin:
#         longest_palindrome_so_far = ''
#         for line in fin:
#             word = line.strip()
#             if is_palindrome(word):
#                 if len(word) > len(longest_palindrome_so_far):
#                     longest_palindrome_so_far = word
#
#     return longest_palindrome_so_far
#
#
# def find_longest_abecedarian():
#     with open('words.txt') as fin:
#         longest_abecedarian_so_far = ''
#         for line in fin:
#             word = line.strip()
#             if is_abecedarian(word):
#                 if len(word) > len(longest_abecedarian_so_far):
#                     longest_abecedarian_so_far = word
#
#     return longest_abecedarian_so_far
#
#
# print(find_longest_palindrome())
# print(find_longest_abecedarian())

def find_longest(check_func):
    with open('znames.txt') as fin:
        longest_so_far = ''
        for line in fin:
            word = line.strip()
            if check_func(word):
                if len(word) >= len(longest_so_far):
                    longest_so_far = word

    return longest_so_far

print(find_longest(is_palindrome))
print(find_longest(is_abecedarian))


# In[ ]:




