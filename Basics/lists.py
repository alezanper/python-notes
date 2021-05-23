print("Using a list")

my_list = [10, 5, 7, 2, 1]
print(my_list)

del my_list[1]    # Removes 5 
print(my_list)    # [10, 7, 2, 1]

my_list.append(88)	# add 88 at the end
print(my_list)    # [10, 7, 2, 1, 88]

my_list.insert(0, 0)  # Add 0 to first position
print(my_list)    # [0, 10, 7, 2, 1, 88]

print("\nSorting Lists")
sortedList = my_list.sort()
print(my_list)    # The list is sorted on same memory space [0, 1, 2, 7, 10, 88]
print(sortedList)   # no new list will be generated
my_list.reverse()
print(my_list)    # [88, 10, 7, 2, 1, 0]

print("\nCopying some part of the list.")
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # it creates a new list
print(new_list) #[8,6]

print("\nUsing in Operator")
my_list = [-2, 3, 7, 0, 4]
print(5 in my_list)		# False
print(5 not in my_list)	# True
print(0 in my_list)	# True

print("\nCreating Lists")
star = "*"
print([star for i in range(5)])     # ['*', '*', '*', '*', '*'] 1d
print([[star for j in range(2)] for k in range(3)])	# it Creates a matriz 3x2 2d
print([[[star for r in range(1)] for f in range(2)] for t in range(3)])  # 3x2x1 3d

print("\npop() removes the last element in a list")
my_list = [-2, 3, 7, 0, 4]
print(my_list)
print(my_list.pop(), "was removed")
print(my_list)

# Using lists reference 
print("\nUsing list Reference")
x = ["a","b","c"]
y = x
y[1] = "z"
# Print the same
print(x)
print(y)

# For creating a copy with different data memory you should use
print("\nCreating a copy using data memory and not a reference")
y=x[:]
# or
y=list(x)
y = y + ["o"]
# Print different lists
print(x)
print(y)

# Creating a list using generators
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print("\nCreating a list using generators")
print(list_1)   # [1, 10, 100, 1000, 10000, 100000]
print(list_2)   # [1, 10, 100, 1000, 10000, 100000]


## Conditionals on lists

the_list = []
for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print("\nCreating a list using conditionals")
print(the_list) # [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]