names = ['Mily', 'Sunny', 'Angle', 'Lucky', 'Vicky']
# print original list
print(names)

# use 'sorted'
print(sorted(names))

# check the list order didn't change after using sorted
print(names)
print("$$$$$$$$$")

# use sorted and reverse
print(sorted(names, reverse=True))
# check the list order didn't change after using sorted
print(names)
print("$$$$$$$$$")

# use reverse to change the list order, and check the order was changed
names.reverse()
print(names)

names.reverse()
print(names)

# use sort to change the list order, check the order is changed
names.sort()
print(names)
print("$$$$$$$$$")

# use sort and reverse
names.sort(reverse=True)
print(names)

print(len(names))
