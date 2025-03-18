#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

################################# 2.1 

# Compute number_of friends

list_friends = [node for friends in friendships for node in friends]
number_friends = len(set(list_friends)) # the number of unique nodes
print(number_friends)

# Create an adjancency matrix of the friendships

m = [[0 for _ in range(number_friends)] for _ in range(number_friends)]
print("Initial adjancency matrix:")
for row in m:
    print(row)
    
for node1, node2 in friendships:
    m[node1][node2] = 1
    m[node2][node1] = 1  

print("\nUpdated adjacency matrix:")
for row in m:
    print(row)
    
# Count occurrences of "1" in the matrix, where "1" represents a friendship / relationship
x_count = sum(row.count(1) for row in m)
print("Average number of friendships (connections per node):", x_count / number_friends)

################################# 2.2

# Count occurrences of "1" (frienships) in each column (for each friend)
column_counts = [sum(1 for row in m if row[i] == 1) for i in range(number_friends)]

# Pair each value with its original index
indexed_counts = list(enumerate(column_counts))
sorted_counts = sorted(indexed_counts, key = lambda x: x[1], reverse=True)

print("People that have many friends")
df = pd.DataFrame(sorted_counts, columns=["Friend ID", "Friendship Count"])
print(df.to_string(index=False))

################################# 2.3

def indirect_friends(uid, m):
    """
    Finds second-level friends (friends of friends) for a given user.
    """
   
    # Find direct friends
    direct_friends = set()
    for i, val in enumerate(m[uid]):
        if val == 1:
            direct_friends.add(i)
    
    # Find indirect / second-level friends 
    indirect_friends = set()
    for friend in direct_friends:
        for j, val in enumerate(m[friend]):
            if val == 1 and j not in direct_friends and j != uid:
                indirect_friends.add(j)
    
    return sorted(indirect_friends)

# Compute second-level (indirect) friends for given user IDs
indirect_friends(3,m)

# Compute second-level (indirect) friends for all users
all_indirect_friends = {uid: indirect_friends(uid, m) for uid in range(number_friends)}

# Create and display DataFrame
df_indirect_friends = pd.DataFrame(all_indirect_friends.items(), \
                                   columns=["User ID", "Second-Level Friends"])
print(df_indirect_friends.to_string(index=False))