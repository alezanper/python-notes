#__module__
# As you know, any module named __main__ is actually not a module, but the file currently being run.

class my_class:
    pass

print(my_class.__module__)  #__main__
obj = my_class()
print(obj.__module__)   #__main__
