print("using << and >> on Python")
a = 17
bin_a = bin(a)
print(a)    # 17
print(bin_a)    # 0b10001

a2 = a >> 1
bin_a2 = bin(a2)
print(a2)
print(bin_a2)

a3 = a2 >> 1
bin_a3 = bin(a3)
print(a3)
print(bin_a3)

a4 = a3 << 2
bin_a4 = bin(a4)
print(a4)
print(bin_a4)

print("\nNumbers")
print(11111111, "is equal to", 11_111_111)
print(.4, "is equal to", 0.4)
print(300000000.0, "is equal to", 3e8)
