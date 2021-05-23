# Inheritance overwritten
class A:
    var = 100
    def fun(self):
        return 101

class B(A):
    var = 200
    def fun(self):
        return 201

class C(B):
    pass

my_class = C()
print(my_class.var, my_class.fun()) # 200 201