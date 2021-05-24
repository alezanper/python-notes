## Using Write
from os import strerror

try:
    new_file = open('newfile.txt', 'wt', encoding="utf-8")  # A new file (newfile.txt) is created.
    print("Write character by character")
    for i in range(10):
        s = "Line #" + str(i+1) + "\n"
        for ch in s:
            new_file.write(ch)
    new_file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# using write 
from os import strerror

try:
    new_file = open('newfile.txt', 'wt', encoding="utf-8")
    print("Write line by line")
    for i in range(10):
        new_file.write("Line #" + str(i+1) + "\n")
    new_file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))