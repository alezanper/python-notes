print ("something \n other")    
"""
something 
 other
"""

#print("\")	 
#It will fail

print("\\") 
# \

print("My name is", end=" ")    
print("Alexander")
# My Name is Alexander

print("My", "name", "is", "Alexander", sep="_") # 
# My_name_is_Alexander

print("My", "name", "is", sep="_", end=" ")
print("Alexander", "Benavides", sep="_", end=".\n")
# My_name_is Alexander_Benavides.


print("Using escape")
print("I am an \"Engineer\"") 
print('I am an "Engineer"')
# I am an "Engineer"

print("Using Basic math")
print(0o2020)    # octal
# 1040

print(0x2020)	# hexa
# 8224

print("when at least one argument is a float, the result is a float")
print(3 // 2)
# 1
print(3. // 2)	
# 1.0

print(12 % 4.5)	
# 3.0 (Module)

print(3 ** 3 ** 2)	
print(3 ** 9)
# 19683

print((9 / 2), (9 // 2))
# 4.5 4

print("Replication")
print("a"*3)
# aaa
print("2"*3)
# 222

print("A variable could be any type of data and is case sensitive")
a = 10
b = "Hello world!"
c = 11.1
d = True
print(a)
print(b)
print(c)
print(d)

# Print out type of variables
print(type(a))  #<class 'int'>
print(type(b))  #<class 'str'>
print(type(c))  #<class 'float'>
print(type(d))  #<class 'bool'>

print("Formatting data")
name = 'Alexander'
age = 33
"I'm {} and my age is {}".format(name, age)