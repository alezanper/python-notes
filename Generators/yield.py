## Using Yield Basic Example
def my_yield_iterator(n):
    for i in range(n):
        yield i

print("Simple example")
for v in my_yield_iterator(10):
    print(v)

## Generator to produce the first n powers of 2
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

print("\nFirst n powers of 2")
for v in powers_of_2(8):
    print(v)

t = [x for x in powers_of_2(8)]
print(t)

u = list(powers_of_2(8))
print(u)

for i in range(20):
    if i in powers_of_2(6):
        print(i)

## Fibonacci using yield
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print("\nFibonacci example")
print(fibs)