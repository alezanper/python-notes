# Using lambda functions Basic
constant = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

print("Print lambda basics")
print(constant())   # 2
print(sqr(2))   # 4
print(pwr(2,3)) # 8


# example 2
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print("\nPrint a function values")
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
    # f(-2)=18
    # f(-1)=8
    # f(0)=2
    # f(1)=0
    # f(2)=2