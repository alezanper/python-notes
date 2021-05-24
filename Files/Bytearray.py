## Bytearray
# Only 0-255 values allowed 
from os import strerror

data = bytearray(16)    # fills the whole array with zeros.

for i in range(len(data)):
    data[i] = i

list = []
print("Using bytearray basic")
for b in data:
    list.append(hex(b))
print(list)     # ['0x0', '0x1', '0x2', '0x3', '0x4', '0x5', '0x6', '0x7', '0x8', '0x9', '0xa', '0xb', '0xc', '0xd', '0xe', '0xf']


## Bytearrays write and read

for i in range(len(data)):
    data[i] = i

print("\nWriting to a bytearray")
try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# read 1
print("\nReading from a bytearray 1")
try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# read 2
from os import strerror

print("\n\nReading from a bytearray 2")
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# read 3
print("\n\nReading from a bytearray 3")
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))