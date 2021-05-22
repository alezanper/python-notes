print("Using a list")

mList = [10, 5, 7, 2, 1]
print(mList)

del mList[1]    # Removes 5 
print(mList)    # [10, 7, 2, 1]

mList.append(88)	# add 88 at the end
print(mList)    # [10, 7, 2, 1, 88]

mList.insert(0, 0)  # Add 0 to first position
print(mList)    # [0, 10, 7, 2, 1, 88]
