# Using Default values
def get_fullname(first_name, last_name="Benavides"):
    print("Hello, my name is", first_name, last_name)
print("Calling get_fullname")
get_fullname("Alex")    # Using default value
get_fullname("Alex", "Ocampo")  # Overriding default value

def sum(x,y,z):
	return x + 2 + y
print("\nCalling sum")
print(sum(0, z=1, y=2)) # 4

def sum_fail(x,y,z):
	return x + 2 + y
#print("Calling sum fail")
#print(sum_fail(0, x=1, y=2)) # TypeError: sum_fail() got multiple values for argument 'x'

# Global variable
def my_function():
    global var
    var = 2
    print("var value inside function:", var)

print("\nUsing Global variables")
var = 1
print("var value outside function:", var)
my_function()
print("var value after function:", var)
