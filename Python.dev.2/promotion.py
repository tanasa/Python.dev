# a contest has 4 levels: bronze, silver, gold and platinum
# before the contest, we have
# - 30 students in bronze
# - 19 in silver
# - 33 in gold
# - 26 in platinum
# in the contest,
# - new students can enter it at the bronze (basic) level
# - existing students can be promoted to the next level
# - except that the platinum students will keep their level
# after the contest, we have
# - 40 in bronze
# - 28 in silver
# - 8 in gold
# - 53 in platinum
# tell me that in the contest
# - number of students who enter the contest at the bronze level
# - number of students who are promoted from bronze to silver
# - number of students who are promoted from silver to gold
# - number of students who are promoted from gold to platinum

from prefix_sum import prefix_sum

before = [26, 33, 19, 30] # from platinum to bronze
after = [53, 8, 28, 40]

prefix_sum_before = prefix_sum(before)
prefix_sum_after = prefix_sum(after)

print(prefix_sum_before)
print(prefix_sum_after)

# promotion = []
# for index in range(len(prefix_sum_before)):
#     diff = prefix_sum_after[index] - prefix_sum_before[index]
#     promotion.append(diff)

promotion = list(map(lambda af, bf: af - bf, prefix_sum_after, prefix_sum_before))

print(promotion) # [27, 2, 11, 21]
