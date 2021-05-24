# makedir

import os

print("Listing currect directory")
print(os.listdir()) # ['create_folder.py']

print("\nCreating new_directory")
os.mkdir("new_directory")
print(os.listdir()) # ['create_folder.py', 'new_directory']

# Create several directories 
print("\nCreating \"several/directory_1/directory_2/\"")
os.makedirs("several/directory_1/directory_2/")
print(os.getcwd())  # C:\python-notes\Os

print("\nMove to several")
os.chdir("several") # Change directory
print(os.listdir()) # ['directory_1']

print("\nMove to directory_1")
os.chdir("directory_1") # Change directory
print(os.listdir()) # ['directory_2']

print("\nRemove directory_2")
os.rmdir("directory_2")
print(os.listdir()) # []