#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print("RECURSION:")


# In[2]:


# This function recursively converts a decimal number into base-3 (ternary), but in reverse order.

def magic(val):
    dig = '' + str(val % 3)            # This gives the remainder when dividing val by 3 — the rightmost digit in base-3.

    if val // 3 > 0:
        return dig + magic(val // 3)   # This gives the quotient, i.e. the "next step" in converting to base-3.

    return dig

print(magic(32))


# In[ ]:





# In[3]:


print("HOPSCOTCH:")

# Hopscotch is a classic children's game played on the ground, typically drawn with chalk on pavement or marked on indoor floors. 
# It combines jumping, balance, and counting, and it's popular around the world with slight regional variations


# In[4]:


# Count how many valid paths exist from the top-left corner (0,0) to the bottom-right corner (R-1,C-1), where:
# Movement is only down and right (strictly increasing row and column).
# You can only move to a cell that has a different color from the current one.


def get_ways(grid, i, j):
    
    R = len(grid) - 1             # Defines the maximum row and column indices.
    C = len(grid[0]) - 1          # Defines the maximum row and column indices.

    if i == R and j == C:         # base case
       return 1                   # if you're at the bottom-right corner, you've completed a valid path — return 1
    
    result = 0                    # recursive step 
    for x in range(i + 1, R + 1):
        for y in range(j + 1, C + 1):
            if grid[i][j] != grid[x][y]:
                result += get_ways(grid, x, y)
    return result

# It checks all positions strictly to the right and below (i+1...R, j+1...C)
# Only moves to cells with a different color
# For each valid move, it recursively counts paths from that cell

with open('hopscotch_map_2.in') as fin:
    
    R, C = [int(part) for part in fin.readline().strip().split()]
    grid = []                      # The variable grid becomes a list of lists — more specifically:
                                   # grid: List[List[str]] : It’s a 2D list (a list of rows)
    for _ in range(R):
        line = fin.readline().strip()
        grid.append(list(line))

    result = get_ways(grid, 0, 0)
    print(result)

# A list of lists can be considered a matrix in Python.
# grid[i][j]	Means
# i	Row index
# j	Column index

# import numpy as np
# arr = np.array(grid)
# NumPy is faster and supports true matrix math.


# In[ ]:





# In[5]:


print("NUMBER of ISLANDS:")


# In[6]:


# This code is a classic solution to the "Number of Islands" problem using a Depth-First Search (DFS) approach 
# (specifically a recursive flood fill algorithm).
# 🏝️ Goal: count how many islands are in the map.
# An island is a group of 1s (land) connected up, down, left, or right (not diagonally).
# 0 means water.


# In[7]:


# 0 means water and 1 means land
# how many islands in the map

map_ = [
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1]
]

R = len(map_)
C = len(map_[0])

islands = 0

visited = []  # visited keeps track of which cells have already been processed to avoid double-counting.

for i in range(R):
    visited.append([False] * C)

def flood_fill(i, j):
    
    visited[i][j] = True   # This function marks the current land cell as visited, and recursively explores its unvisited land neighbors 
                           # (top, bottom, left, right).
    
    if i > 0 and map_[i-1][j] == 1 and not visited[i-1][j]:
        flood_fill(i-1, j)
    if i < R-1 and map_[i+1][j] == 1 and not visited[i+1][j]:
        flood_fill(i+1, j)
    if j > 0 and map_[i][j-1] == 1 and not visited[i][j-1]:
        flood_fill(i, j-1)
    if j < C-1 and map_[i][j+1] == 1 and not visited[i][j+1]:
        flood_fill(i, j+1)

for i in range(R):
    for j in range(C):
        if map_[i][j] == 1 and not visited[i][j]:
            islands += 1
            flood_fill(i, j)

print(islands)

# Why does a single 1 count as an island?
# Because:
# It is land (1)
# It is not connected to any other land cells
# So, it's a valid island of size 1


# In[ ]:





# In[8]:


print("MERGE SORT : a recursive solution, Divide et Impera (divide and conquer)")
# it is a solution proposed in class


# In[9]:


# mergesort() recursively splits the array into halves until each part is sorted (size 1).
# merge() then combines those sorted parts back together in order.
# merge_sub() is a small helper that inserts values into the original array during the merging process.

def merge_sub(arr, merge_index, sub, sub_index):
    arr[merge_index] = sub[sub_index]
    sub_index += 1
    return sub_index

# pre-condition: arr[start:middle+1] is sorted and
#                arr[middle+1:end+1] is sorted
# post-condition: arr[start:end] is sorted

def merge(arr, start, middle, end):
    left = arr[start:middle+1]
    right = arr[middle+1:end+1]
    left_index = 0
    right_index = 0

    merge_index = start
    while merge_index <= end:
        if right_index >= len(right):
            left_index = merge_sub(arr, merge_index, left, left_index)
        elif left_index >= len(left):
            right_index = merge_sub(arr, merge_index, right, right_index)
        elif left[left_index] < right[right_index]:
            left_index = merge_sub(arr, merge_index, left, left_index)
        else:
            right_index = merge_sub(arr, merge_index, right, right_index)

        merge_index += 1

def mergesort(arr, start, end):
    if start >= end:
        return

    middle = (start + end) // 2
    mergesort(arr, start, middle)
    mergesort(arr, middle+1, end)
    merge(arr, start, middle, end)


arr = [8, 1, 4, 6, 2, 5, 3, 7]
print(arr)
mergesort(arr, 0, len(arr) - 1)
print(arr)


# In[10]:


print("MERGE SORT : a recursive solution, Divide et Impera (divide and conquer) : a simpler solution")


# In[11]:


def merge_sort(arr):
    
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Split the array into two halves
    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    # Step 2: Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    
    result = []
    i = 0  # index for left half
    j = 0  # index for right half

    # Compare elements from both halves and add the smaller one to the result
    # This loop runs as long as both lists have unprocessed elements.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        # If the current element in left is smaller than in right, add it to the result.
        # Move the pointer i to the next element in left.
        # Otherwise, add the element from right and advance the pointer j.

    # If there are leftover elements in either half, add them all
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage:
arr = [8, 1, 4, 6, 2, 5, 3, 7]
print("Original array:", arr)

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)


# In[ ]:





# In[ ]:





# In[12]:


print("KNAPSACK : a recursive solution, DYNAMIC PROGRAMMING")

# Imagine you are a traveler with a backpack (knapsack) that can carry a limited weight, say 10 kg. 
# You have a set of items to choose from, and each item has:

# A weight (how heavy it is)
# A value (how useful or profitable it is)
# Your goal is to:
# Choose a subset of items that maximizes total value, without exceeding the total weight your knapsack can carry.

# Why it’s important:
# The knapsack problem models real-world resource allocation:
# Limited capacity (memory, budget, time)
# Choose among options with trade-offs (cost vs benefit)
# Solve efficiently with techniques like dynamic programming, greedy, or branch & bound


# In[13]:


# You have a set of items, each with a weight and a value.
# You have a knapsack (bag) that can carry at most max_weight.
# Your goal is to maximize the total value of items placed in the knapsack without exceeding its weight limit.
# Each item can be used at most once.


# In[14]:


# 1. optimal sub-structures: the optimal solution to the original problem
# can be constructed by combining the optimal solutions to its similar sub-problems
# 2. overlapping sub-problems: the number of the unique sub-problems is small

# (weight, value)
items = [
    (2, 3), (3, 4), (4, 5), (5, 6)
]

# knapsack capacity: max weight a bag can hold
max_weight = 10

# dp[i][w] as the maximum value that can be obtained using the first i items
# with the knapsack capacity as w

dp = []

for i in range(len(items) + 1):
    dp.append([0] * (max_weight + 1))


print(dp)
print(len(dp))

# We create a 2D DP table dp with dimensions (number of items + 1) × (max_weight + 1)
# dp[i][w] will hold the maximum value you can get using the first i items and a bag with capacity w
# Initialize all values to 0 (base cases: no items or no capacity)

# Iterate over each item (starting from item 1)
# items[index - 1] because dp[0][...] is the 0-item row (base case)
# Unpack the weight and value of the current item

# If the item fits in the knapsack (i.e., doesn't exceed the current weight limit):
# You choose the better of:
# * Not taking the item → value stays the same (dp[index-1][weight])
# * Taking the item → add its value to the remaining capacity (dp[index-1][weight - item_weight] + item_value)

# If the item does not fit, you can't take it, so inherit the value from the row above.
# dp[-1][-1] is the maximum value you can achieve using all items with a full knapsack (capacity = 10)

for index in range(1, len(dp)):
    for weight in range(1, len(dp[index])):
        item_weight, item_value = items[index - 1]
        if item_weight <= weight:
            dp[index][weight] = max(
                dp[index-1][weight],
                dp[index-1][weight-item_weight] + item_value
            )
        else:
            dp[index][weight] = dp[index-1][weight]

print(dp)
print(dp[-1][-1])

# [
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3],
# [0, 0, 3, 4, 4, 7, 7, 7, 7, 7, 7],
# [0, 0, 3, 4, 5, 7, 8, 9, 9, 12, 12],
# [0, 0, 3, 4, 5, 7, 8, 9, 10, 12, 13]
# ]


# In[15]:


print("KNAPSACK : a recursive solution, DYNAMIC PROGRAMMING : comments")


# In[16]:


# List of items: each item is a (weight, value) pair
items = [(2, 3), (3, 4), (4, 5), (5, 6)]

# Maximum weight the knapsack can carry
max_weight = 10

# Number of items
n = len(items)
print(n)

# Create a 2D table where dp[i][w] means:
# the maximum value we can get using the first i items with a max weight of w

dp = []

for i in range(n + 1):
    row = [0] * (max_weight + 1)
    dp.append(row)

# Fill the table row by row
for i in range(1, n + 1):  # i represents the number of items considered so far
    item_weight, item_value = items[i - 1]   # current item's weight and value
    
    for w in range(1, max_weight + 1):  # go through each possible weight
        if item_weight <= w:
            # We can choose to include this item or not
            dp[i][w] = max(
                dp[i - 1][w],                        # not taking the item
                dp[i - 1][w - item_weight] + item_value  # taking the item
            )
        else:
            # Can't take the item, if does not fit in the bag
            dp[i][w] = dp[i - 1][w]


# w is the current capacity of the knapsack we're testing
# we'll try to compute the best value possible using the first i items with a max weight w

# Print the entire table (optional, for understanding)
for row in dp:
    print(row)

# The answer is in the last cell: max value we can carry
print("Maximum value that fits into the knapsack:", dp[n][max_weight])


# In[17]:


# We make a table with:
# n + 1 rows → for 0 to n items
# max_weight + 1 columns → for weight capacities from 0 to max_weight
# Each row i in the DP table represents:

# The best possible value you can achieve using the first i items.
# Rows represent:
# dp[0] = using 0 items
# 
# dp[1] = using first 1 item
#
# ...

# dp[n] = using all n items

# So we need n + 1 rows to include the case where we use no items at all — which is the base case.

# Why max_weight + 1 columns?

# Each column w represents:
# The best possible value with a knapsack of capacity w.
# So we need max_weight + 1 columns to include weight 0 up to max_weight.  


# In[18]:


print("KNAPSACK : a recursive solution, DYNAMIC PROGRAMMING : a simpler solution")


# In[19]:


# Items: (weight, value)

items = [(2, 3), (3, 4), (4, 5), (5, 6)]
max_weight = 10

n = len(items)

# Create a DP table with n+1 rows and max_weight+1 columns
dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

# Fill the table
for i in range(1, n + 1):
    weight, value = items[i - 1]
    for w in range(max_weight + 1):
        if weight <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
        else:
            dp[i][w] = dp[i - 1][w]

# Final result: maximum value we can carry
print("Max value in knapsack:", dp[n][max_weight])


# In[20]:


print("KNAPSACK : a recursive solution, DYNAMIC PROGRAMMING and BACKTRACKING : a simpler solution")


# In[21]:


# Items: (weight, value)
items = [(2, 3), (3, 4), (4, 5), (5, 6)]
max_weight = 10
n = len(items)

# Step 1: Build DP table
dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = items[i - 1]
    for w in range(max_weight + 1):
        if weight <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
        else:
            dp[i][w] = dp[i - 1][w]

# Step 2: Backtrack to find which items were included
w = max_weight
selected_items = []

for i in range(n, 0, -1):  # go backward through items
    if dp[i][w] != dp[i - 1][w]:  # item was taken
        selected_items.append(items[i - 1])
        w -= items[i - 1][0]  # subtract the weight of the item

# Step 3: Output results
print("Max value in knapsack:", dp[n][max_weight])
print("Selected items (weight, value):", list(reversed(selected_items)))


# In[22]:


# Why it is Dynamic Programming:

# It solves subproblems:
# For each item and each weight capacity, it finds the best solution by building on previous solutions.
# It stores results in a table (dp) to avoid recalculating the same subproblems — this is called memoization (when done with a table, it’s tabulation).

# It considers all combinations of items (in a smart, efficient way) to guarantee the optimal solution.

# ❌ Why it is not Greedy:

# A greedy algorithm:
# Makes the best immediate (local) choice at each step.
# Does not go back to reconsider decisions.
# Often doesn’t give the optimal answer for problems like 0/1 knapsack.

