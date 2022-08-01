print("Creating a List")
list = [i for i in range(10)]
print(list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

print("Creating a Set")
set = {i for i in range(10)}
print(set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print()

print("Creating a Generator")   # when results do not need to be stored in memory
generator = (i for i in range(10))
print(sum(generator))
print(generator) 
print()

print("Creating a Dictionary")
dictionary = {i:i*i for i in range(10)}
print(dictionary) 
print()