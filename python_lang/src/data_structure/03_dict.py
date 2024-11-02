# A dict is a collection of key-value pairs. It is unordered, changeable and indexed.
# 1 Create a dictionary
# In Python, dictionaries are written with curly brackets, and they have keys and values.
num_count = {}
nums = [1, 2, 1, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
for num in nums:
    if num in num_count:  # check if the key exists in the dictionary
        num_count[num] += 1
    else:
        num_count[num] = 1
print(num_count)  # {1: 4, 2: 3, 3: 3, 4: 2, 5: 2}

# 2 Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
for key in num_count:
    print(key, num_count[key])
# You can also use items() method to get the key-value pairs
for key, value in num_count.items():
    print(key, value)
