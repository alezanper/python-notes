# Sets are by design uniques, therefore the set create unique values
# Sets has an optimized method for cjhecking wheter a specific element is contained. This is based on a data structure called hash table

print({1, 1, 1, 2, 3, 3, 3})    # {1, 2, 3}
print(set([1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 3, 6, 6, 20]))    # {1, 2, 3, 4, 5, 6, 20}
s = {1, 1, 1, 2, 3, 3, 3}
print(s)
s.add(5)
print(s)

hello = "hello"
print(set(hello))   # {'h', 'e', 'l', 'o'}

print("\nUsing Operators")
a = {1,2,3,4,5,6,7,8,9}
b = {4,3,6,9}
print(a)
print(b)
print(a==b) # False
print(a!=b) # True
print(a<=b) # False (a is a subset of b?)
print(b<=a) # True (b is a subset of a?)
print(a>=b) # True (a is a superset of b?)
print(a|b) # Union {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a&b) # Intersection {9, 3, 4, 6}
print(a-b) # set of elements in a but not in b {1, 2, 5, 7, 8}

