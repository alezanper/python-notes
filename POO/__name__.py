# Using __name__ attribute
class my_class:
    pass

print(my_class.__name__)    # my_class
obj = my_class()
print(type(obj).__name__)   # my_class