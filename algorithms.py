# Bubble sort
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

# Caesar cipher.
# https://en.wikipedia.org/wiki/Caesar_cipher
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
print(cipher)

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)

# Find a word
big = 'Nabucodonosor'
s = 'donor'
a = []
flag = 'yes'
carry = 0
for i in s:
    l = big.find(i)
    a.append(l+carry)
    if (l != -1):
        big = big[l:]
        carry += l
    else:
        flag = 'no'
print(flag)