# A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets.
# 1 Creation of set
num_set = {1, 2, 3, 4, 5}
print(num_set)  # {1, 2, 3, 4, 5}

# 2 Access Items
for num in num_set:
    print(num)

# 3 Methods
# 3.1 add()	Adds an element to the set
num_set.add(6)  # {1, 2, 3, 4, 5, 6}
# 3.2 remove()	Removes the specified element
num_set.remove(2)  # {1, 3, 4, 5, 6}

# 4 Set Operations
num_set_1 = {1, 3, 4, 5, 6}
num_set_2 = {1, 2, 3, 4, 7}
# 4.1 union()	Returns a set containing the union of sets
num_set_3 = num_set_1.union(num_set_2)  # {1, 3, 4, 5, 6, 7}
print(num_set_3)
# 4.2 intersection()	Returns a set, that is the intersection of two other sets
num_set_4 = num_set_1.intersection(num_set_2)  # {1, 3, 4}
print(num_set_4)
# 4.3 difference()	Returns a set containing the difference between two or more sets
num_set_5 = num_set_1.difference(num_set_2)  # {5, 6}
print(num_set_5)
# 4.4 symmetric_difference()	Returns a set with the symmetric differences of two sets
num_set_6 = num_set_1.symmetric_difference(num_set_2)  # {2, 5, 6, 7}
print(num_set_6)
