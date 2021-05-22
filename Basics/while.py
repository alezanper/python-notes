# while loops
total = 0
j = 0
while j < 5:
    total += j
    j += 1
print(total)    # 10

# Using a list with a while loop
mList = [1, 2, 3, 5, 7]
total = 0
i = 0
while i < len(mList) and mList[i] > 0:
    total += mList[i]
    i += 1
print(total)    # 18

# You can use break for finish the loop
mList = [1, 2, 3, -1, 5, 7]
total = 0
i = 0
for element in mList:
    if element <= 0:
        break
    total += element
print(total)    # 6

# You can use True for infinite loop
_list = [1, 2, 3, -1, 5, 7]
total = 0
i = 0
while True:
    if _list[i] <= 0:
        break
    total += _list[i]
    i += 1
print(total)