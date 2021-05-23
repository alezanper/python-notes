"""
class Python:
    population = 1					#Class variable
    victims = 0						#Class variable
    def __init__(self):
        self.length_ft = 3			#Instance Variable
        self.__venomous = False		#Instance Variable
"""   

## Class variables
class myClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        myClass.counter += 1

# Creating objects
class_1 = myClass()
class_2 = myClass(2)
class_3 = myClass(4)

print("Checking class variable counter")
print(class_1.counter)
print(class_2.counter)	
print(class_3.counter)	

class myClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        myClass.__counter += 1
        
myClass_1 = myClass()
myClass_2 = myClass(2)
myClass_3 = myClass(4)

print("\nChecking instance variables and class variable counter")
print(myClass_1.__dict__, myClass_1._myClass__counter)	#{'_myClass__first': 1} 3
print(myClass_2.__dict__, myClass_2._myClass__counter)	#{'_myClass__first': 2} 3
print(myClass_3.__dict__, myClass_3._myClass__counter)	#{'_myClass__first': 4} 3
