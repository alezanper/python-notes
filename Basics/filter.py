# Using filter
from random import seed, randint

seed(5)
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print("Using Filter")
print(data)         # [-3, 7, -6, -6, 4]
print(filtered)     # [4]
