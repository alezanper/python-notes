# Counting Characters
# Reading character by character
from os import strerror
try:
    cnt = 0
    s = open('file.txt', "rt", encoding = "utf-8")
    ch = s.read(1)
    print("Counting characters, reading character by character:")
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# Counting Characters
# Load whole file on memory
from os import strerror

try:
    cnt = 0
    s = open('file.txt', "rt", encoding = "utf-8")
    content = s.read()
    print("\nCounting characters, reading whole file on memory:")
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

## Using the readline
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('file.txt', 'rt', encoding = "utf-8")
    line = s.readline()
    print("\nCounting characters, reading line by line:")
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Using redlines()
try:
    ccnt = lcnt = 0
    s = open('file.txt', 'rt', encoding = "utf-8")
    lines = s.readlines(20)    #to read not more than a specified number of bytes at once
    print("\nCounting characters, using readlines()")
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))



# processing texts
from os import strerror

try:
    ccnt = lcnt = 0
    print("\nCounting characters")
    for line in open('file.txt', 'rt', encoding = "utf-8"):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))