# Using __bases__ attribute

class A:
    pass
class B:
    pass
class C(A, B):
    pass

def printBases(my_class):
    print('( ', end='')

    for x in my_class.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(A)   # ( object )
printBases(B)   # ( object )
printBases(C)   # ( A B )