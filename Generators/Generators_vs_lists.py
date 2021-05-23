# List comprehensions vs. generators
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")   # 1 0 1 0 1 0 1 0 1 0
print()

for v in the_generator:
    print(v, end=" ")   # 1 0 1 0 1 0 1 0 1 0
print()