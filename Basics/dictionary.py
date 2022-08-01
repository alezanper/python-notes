# Dictionaries are mutable
# keys are case sensitive

empty_dictionary = {}
print(empty_dictionary)

# Using constructor
base = [("sp", "spanish"),("en", "english")]
base_dictionary = dict(base)
print(base_dictionary)

dictionary = {"hola": "mundo", "hello": "world"}
print(dictionary['hola'])	# mundo

# Using a list
print("\nUsing a list with dictionary")
keys = ['hola', 'HOLA', 'hello', 'dog']
for key in keys:
    if key in dictionary:
        print(key, "->", dictionary[key])
    else:
        print(key, "is not in dictionary")

# Using keys function
print("\nUsing keys function with dictionary")
for key in dictionary.keys():
    if key in dictionary:
        print(key, "->", dictionary[key])
    else:
        print(key, "is not in dictionary")

# Using items() returns tuples 
print("\nUsing items function with dictionary")
for key, value in dictionary.items():
    print(key, "->", value)

# Nested Dictionaries
print("\nUsing nested dictionary")
d = {'key': ['a', 'b', 'c']}
print(d['key'][1])

# Operators
print("\nOperators")
a = [("sp", "Spanish"),("en", "English")]
b = [("du", "Russian"),("en", "English"), ("jp", "Japanese")]
dict_a = dict(a)
dict_b = dict(b)
print(dict_a)
print(dict_b)
print(dict_a == dict_b) # False (is equivalent?)
print(dict_a != dict_b) # True (is not equivalent?)

