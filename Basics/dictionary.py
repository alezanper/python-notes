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

# Nested Ddictionaries
print("\nUsing nested dictionary")
d = {'key': ['a', 'b', 'c']}
print(d['key'][1])