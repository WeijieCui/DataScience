# A tuple is a fixed-length, immutable sequence of Python objects.
# 1 Creating a tuple
# 1.1 The easiest way to create one is with a comma-separated sequence of values.
tup = 4, 5, 6
print(tup)  # (4, 5, 6)
# 1.2 For better readability, you can also use parentheses.
nested_tup = ((4, 5, 6), (7, 8))
print(nested_tup)  # ((4, 5, 6), (7, 8))
# 1.3 You can convert any sequence or iterator to a tuple by invoking tuple.
tup_1 = tuple('string')
tup_2 = tuple([4, 0, 2])

# 2 Elements of a tuple
# 2.1 Elements can be accessed with square brackets [].
print(tup[0])  # 4
print(tup[-1])  # 6
# 2.2 Unpacking tuples
position = (4, 5, 6)
x, y, z = position
# 2.3 Iterating over sequences of tuples or lists.
points = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for x, y, z in points:
    print(x, y, z)

# 3 Methods
# 3.1 count
a = (1, 2, 2, 2, 3, 4, 2)
print(a.count(2))  # 4
# 3.2 index
print(a.index(2))  # 1
