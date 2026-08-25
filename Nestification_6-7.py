pets = []

for pets_num in range(0, 30):
    new_pet = {'Name': 'Vicky', 'Color': 'Black and White', 'Age': 10}
    pets.append(new_pet)

for pet in pets[0:3]:
    if pet['Color'] == 'Black and White':
        pet['Color'] = 'Yellow'
        pet['Name'] = 'Lucky'
        pet['Age'] = 5
    print(pet)
print("Total number of pets is " + str(len(pets)))

# 6-7, 6-8

pet_0 = {'name': 'Sunny', 'age': 1, 'color': 'White'}
pet_1 = {'name': 'Lucky', 'age': 5, 'color': 'Black and White'}
pet_2 = {'name': 'Vicky', 'age': 10, 'color': 'Black and White'}
animal = [pet_0, pet_1, pet_2]
for pet in animal:
    print(pet)

# 6-9
favorite_place = {
    'Sunny': ['Beijing', 'Guangzhou', 'Yunnan'],
    'Vicky': ['Chengdu'],
    'Mily': ['Chengdu', 'Hangzhou']
}
for name, places in favorite_place.items():
    if name == 'Vicky':
        print(name + "'s favorite place is:")
    else:
        print(name + "'s favorite place are:")
    for place in places:
        print(place)
# 更优雅的写法
favorite_place = {
    'Sunny': ['Beijing', 'Guangzhou', 'Yunnan'],
    'Vicky': ['Chengdu'],
    'Mily': ['Chengdu', 'Hangzhou']
}

for name, places in favorite_place.items():
    # 根据名字选择 is/are
    verb = "is" if name == 'Vicky' else "are"
    print(f"{name}'s favorite place {verb}:")

    for place in places:
        print(f" - {place}")
    print()  # 空行分隔

# 6-10
favorite_number = {
    'Vicky': [10, 27, 18],
    'Mily': [9, 7, 18],
    'Angle': [9, 3, 27],
    'Lucky': [5, 7, 26],
    'Sunny': [1, 10, 27]
}
for name, number in favorite_number.items():
    print(name + "'s favorite number are: ")
    for num in number:
        print(num)
