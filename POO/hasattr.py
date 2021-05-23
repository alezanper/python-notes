class my_Class:
    a = 1
    def __init__(self):
        self.b = 2
        
my_Class_1 = my_Class()
print(hasattr(my_Class_1, 'b'))		#True
print(hasattr(my_Class_1, 'a'))		#True
print(hasattr(my_Class, 'b'))   #False
print(hasattr(my_Class, 'a'))	#True