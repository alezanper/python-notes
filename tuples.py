# Tuples are inmutables
t = (1, 2, 4, 8)
empty_tuple = ()
one_element_tuple= (1, )
print("Empty tuple ->", empty_tuple)
print("One element tuple ->", one_element_tuple)

# Mapping tuple to variables
tup = (1, 2, 3)
a, b, c = tup
print("\nThe sum of", tup, "components is:", a * b * c)    # 6

# tuple duplicates
tup = (1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9)
duplicates = tup.count(2)
print("\nThe 2 is", duplicates, "times in ", tup)    # outputs: 4

# Converting to tuples
my_list = ["car", "Ford", "flower", "Tulip"]
t = tuple(my_list)
print("\nList",my_list,"to tuple:",t)

