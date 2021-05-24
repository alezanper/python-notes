# Open a File
# Opening file.txt in read mode, returning it as a file object:
stream = open("file.txt", "rt", encoding = "utf-8")
print(stream.read()) # printing the content of the file