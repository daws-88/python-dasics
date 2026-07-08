s_1 = {}
s_2 = set()
sample = {'a', 'a', 'b'}
print(type(sample),sample)

# sets are unorderd collections 
# sets  remove duplicates
# print(dir(sample))
"""
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""
sample.add('x')
print(sample)

# orderd collection like list, tuple, dict supports indexing
# unorderd collections does not support indexing
# print(sample[1])

s1 = {'1', '2', '3', '4', '5'}
s2= {'2', '4', '6'}
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)

# 1. difference()
# Returns a new set.
# Does not modify the original set.

# 2. difference_update()
# Modifies the original set.
# Returns None.