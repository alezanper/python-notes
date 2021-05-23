# Using map with lambda
list_1 = [x for x in range(5)]  # [0 1 2 3 4]
list_2 = list(map(lambda x: 2 ** x, list_1))    # [1, 2, 4, 8, 16]

print("Map list to function")
print(list_2)
for x in map(lambda x: x * x, list_2):
    print(x, end=' ')   # 1 4 16 64 256 
print()