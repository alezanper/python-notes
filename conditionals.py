print("Before take a view of conditionals is good to know about comparison")

# Comparison of booleans
print("True == False ->", True == False)    # False

# Comparison of integers
print("-5*15 != 75 ->", -5*15 != 75)  # True

# Comparison of strings
print('"Alex" == "@l3x" -> ',"Alex" == "@l3x") # False

# Compare a boolean with an integer
print("True == 5 ->", True == 5)    # False
print("True == 1 ->", True == 1)    # True
print("True == 0 ->", True == 0)    # False


# Simple Conditional
a = 3
b = 2
if a < b:
    print("a is less than b")
    print("more text")
else:
    print("b is less or equal to a")
print("outside of if statement")

# Conditional Block
a = 3
b = 2
if a < b:
    print("a is less than b")
    print("more text")
elif a == b:
    print("a is equal to b")
elif a < b + 10:
    print("a is less than b plus 10")
else:
    print("b is less than a")
print("outside of if statement")    

# Nested Conditionals
c = 10
d = 20
if c < d:
    print("c is less than d")
else:
    if c == d:
        print("c is equal to d")
    else:
        print("c is greater than d")

