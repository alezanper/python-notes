class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    def get_sum(self):
        return self.__sum
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

print("Inheritance AddingStack example")
stack_object = AddingStack()
for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())
for i in range(5):
    print(stack_object.pop())

## Example 2 ##
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_TrackedVehicle = TrackedVehicle()

print("\nChecking classes inheritance")
print(issubclass(TrackedVehicle, Vehicle))  # True
print(issubclass(Vehicle, TrackedVehicle))  # False

print("\nVehicle analysis")
print(isinstance(my_vehicle, Vehicle))  # True
print(isinstance(my_land_vehicle, Vehicle)) # True
print(isinstance(my_TrackedVehicle, Vehicle))   # True

print("\nLand Vehicle analysis")
print(isinstance(my_vehicle, LandVehicle))  # False
print(isinstance(my_land_vehicle, LandVehicle)) # True
print(isinstance(my_TrackedVehicle, LandVehicle))   # True

print("\nTracked Vehicle analysis")
print(isinstance(my_vehicle, TrackedVehicle))  # False
print(isinstance(my_land_vehicle, TrackedVehicle)) # False
print(isinstance(my_TrackedVehicle, TrackedVehicle))   # True

my_vehicle_2 = my_vehicle
print("\nAre the objects equal?")
print(my_vehicle is my_vehicle_2)