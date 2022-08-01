# Packing
print("Packing a tuple")
values = 1,2,3,4
print(values)
print()

# Unpacking
print("Unpacking a tuple")
a,b,c,d = range(0,4)
print(a,b,c,d)
print() 

print("Using on loops")
for x,y in [(1,2), (3,4), (5,6)]:
    print(x+y)
print()

print("Swapping values")
a=1
b=2
print(a,b)
a,b = b,a
print(a,b)

print("Applying to fibonacci")
def fibonacci(stop):
    a, b = 0, 1
    f =[a]
    while b<stop:
        a, b = b, a+b
        f.append(a)
    return f
print(fibonacci(10))
