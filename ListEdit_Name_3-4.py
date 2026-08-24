bicycles = ['trek', 'Cannondale', 'redline', 'specialized']
message = "my favorite bicycle was a "+bicycles[0].title() + "."
print(message)
print(bicycles[-2])

names = ['Lily', 'Lucy', 'Jerry', 'Tom']
print("My name is " + names[2])
names.append("Gery")
names[1] = "Sunny"
names.insert(1, "Lucky")

# 注意del后边没有点，不是del.names
# 不再使用删除的元素用del.还需要继续使用该元素用pop
del names[4]
print(names)

# 弹出列表中最后一个值，并储存到新的变量popped_name中
popped_name = names.pop()
print(names)
print(popped_name)

# 删除值，虽然不知道该值的位置
too_young = 'Lily'
names.remove("Lily")
print(names)
print('The person ' + too_young + " is the youngest in this team.")

print("I would like to invite " + names[0] + ", "
      + names[1] + " and " + names[2] + " to have dinner with me.")

no_attended = "Jerry"
new_invited = "Vicky"
print(no_attended + " cannot attended this dinner.")
names.remove("Jerry")
names.append("Vicky")
print(names)
print("I would like to invite " + names[0] + ", "
      + names[1] + " and " + names[2] + " to have dinner with me.")
names.insert(0, "Angle")
names.insert(2, "Mily")
names.append("May")
print("I would like to invite " + names[0] + ", "
      + names[1] + ", " + names[2] + ", "
      + names[3] + ", " + names[4] + " and "
      + names[5] + " to have dinner with me.")
print(len(names))

popped_name = names.pop()
print("Sorry, cannot invite " + popped_name + " to have dinner with me.")
popped_name = names.pop()
print("Sorry, cannot invite " + popped_name + " to have dinner with me.")
popped_name = names.pop()
print("Sorry, cannot invite " + popped_name + " to have dinner with me.")
popped_name = names.pop()
print("Sorry, cannot invite " + popped_name + " to have dinner with me.")
print(names)

del names[1]
del names[0]
print(names)



