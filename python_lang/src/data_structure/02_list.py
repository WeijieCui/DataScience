# A list is a variable-length, mutable sequence of Python objects.
# 1 Creating a list
# 1.1 The easiest way to create one is with a comma-separated sequence of values.
a_list = [2, 3, 7, 4]
print(a_list)  # [2, 3, 7, 4]

# 2 Elements of a list
# 2.1 Elements can be accessed with square brackets [].
print(a_list[0])  # 2
print(a_list[-1])  # 4
# 2.2 You can concatenate lists using the + operator.
a_list += [5, 6, 7]  # [2, 3, 7, 4, 5, 6, 7]
# 2.3 Lists are mutable.
a_list[2] = 4
print(a_list)  # [2, 3, 4, 4, 5, 6, 7]
# 2.4 Iterating over a list.
for value in a_list:
    print(value)
# 2.5 Iterating over a list with index.
for index, value in enumerate(a_list):
    print(index, value)
# 2.6 Iterating over two lists by zip().
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
for name, age in zip(names, ages):
    print(name, age)

# 3 Methods
# 3.1 append
a_list.append(10)  # [2, 3, 4, 4, 5, 6, 7, 10]
# 3.2 insert
a_list.insert(1, 20)  # [2, 20, 3, 4, 4, 5, 6, 7, 10]
# 3.3 pop
n1 = a_list.pop(3)  # [2, 20, 3, 4, 5, 6, 7, 10]
# 3.4 remove
a_list.remove(4)  # [2, 20, 3, 5, 6, 7, 10]
# 3.5 in
print(2 in a_list)  # True
# 3.6 sort
a_list.sort()  # [2, 3, 5, 6, 7, 10, 20]
# 3.7 reverse
a_list.reverse()  # [20, 10, 7, 6, 5, 3, 2]
# 3.8 extend
a_list.extend([30, 40, 50])  # [20, 10, 7, 6, 5, 3, 2, 30, 40, 50]

# 4 Slicing
# 4.1 You can select sections of most sequence types by using slice notation.
a_list = [2, 3, 7, 4, 5, 6, 7]
print(a_list[1:5])  # [3, 7, 4, 5]
print(a_list[:5])  # [2, 3, 7, 4, 5]
print(a_list[3:])  # [4, 5, 6, 7]

# 5 List Comprehensions
# 5.1 List comprehensions provide a concise way to create lists.
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 5.2 A list comprehension consists of brackets containing an expression followed by a for clause.
# You can add more for or if clauses.
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
