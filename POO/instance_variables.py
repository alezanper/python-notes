"""
class Python:
    population = 1					#Class variable
    victims = 0						#Class variable
    def __init__(self):
        self.length_ft = 3			#Instance Variable
        self.__venomous = False		#Instance Variable
"""   

class myClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val

# Creating objects 
myClass_1 = myClass()
myClass_2 = myClass(2)
myClass_3 = myClass(4)

# Adding values to instances
myClass_2.set_second(3)
myClass_3.third = 5

# __dist__ property shows the instance variables
print("Checking instance variables")
print(myClass_1.__dict__)	#{'first': 1}
print(myClass_2.__dict__)	#{'second': 3, 'first': 2}
print(myClass_3.__dict__)	#{'third': 5, 'first': 4}

class myClass:
    def __init__(self, val = 1):
        self.__first = val
    def set_second(self, val = 2):
        self.__second = val

myClass_1 = myClass()
myClass_2 = myClass(2)
myClass_3 = myClass(4)

myClass_3.__third = 5
myClass_2.set_second(3)

# __dist__ property shows the instance variables
print("\nChecking instance variables (private)")
print(myClass_1.__dict__)
print(myClass_2.__dict__)
print(myClass_3.__dict__)