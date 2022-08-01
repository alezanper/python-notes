# Sets are by design uniques, therefore the set create unique values
# Sets has an optimized method for cjhecking wheter a specific element is contained. This is based on a data structure called hash table

print({1, 1, 1, 2, 3, 3, 3})    # {1, 2, 3}
print(set([1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 3, 6, 6, 20]))    # {1, 2, 3, 4, 5, 6, 20}
s = {1, 1, 1, 2, 3, 3, 3}
print(s)
s.add(5)
print(s)

hello = "hello"
print(set(hello))
