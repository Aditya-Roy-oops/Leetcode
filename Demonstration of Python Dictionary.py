# Demonstration of Python Dictionary

# 1. Creating dictionaries
dict1 = {}  # Empty dictionary
dict2 = {'a': 1, 'b': 2}  # Using curly braces
dict3 = dict([('c', 3), ('d', 4)])  # Using dict() with list of tuples
dict4 = dict(e=5, f=6)  # Using keyword arguments

# 2. Accessing values
print(dict2['a'])  # Access by key
print(dict2.get('b'))  # Using get()

# 3. Adding and updating values
dict2['c'] = 3  # Add new key-value
dict2['a'] = 10  # Update existing key

# 4. Removing items
del dict2['b']  # Remove by key
value = dict2.pop('c')  # Remove and return value
item = dict2.popitem()  # Remove and return last inserted item (tuple)

# 5. Dictionary methods
dict5 = {'x': 1, 'y': 2, 'z': 3}
print(dict5.keys())      # dict_keys(['x', 'y', 'z'])
print(dict5.values())    # dict_values([1, 2, 3])
print(dict5.items())     # dict_items([('x', 1), ('y', 2), ('z', 3)])

# 6. Iterating over dictionary
for key in dict5:
    print(key, dict5[key])

for key, value in dict5.items():
    print(key, value)

# 7. Checking existence
if 'x' in dict5:
    print("Key 'x' exists")

# 8. Copying dictionary
dict6 = dict5.copy()
dict7 = dict(dict5)

# 9. Clearing dictionary
dict6.clear()

# 10. Merging dictionaries
dict8 = {'a': 1, 'b': 2}
dict9 = {'b': 3, 'c': 4}
dict8.update(dict9)  # dict8 now {'a': 1, 'b': 3, 'c': 4}

# 11. Dictionary comprehensions
squares = {x: x*x for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# 12. Setting default values
d = {}
d.setdefault('key', 'default')  # Adds 'key' with value 'default' if not present

# 13. Fromkeys
keys = ['a', 'b', 'c']
dict10 = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

# 14. Nested dictionaries
nested = {'outer': {'inner': 42}}
print(nested['outer']['inner'])