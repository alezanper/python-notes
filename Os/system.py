# Using system
import os

print("Using a command with system")
returned_value = os.system("mkdir other_directory")
print(returned_value)   # 0
