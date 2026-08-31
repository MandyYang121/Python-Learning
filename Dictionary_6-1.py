# 6-1
friend = {
    'first_name': 'Lan',
    'last_name': 'Meng',
    'age': 10,
    'city': 'Beijing'
}
print(friend)

# 6-2
favorite_number = {
    'Vicky': 10,
    'Mily': 9,
    'Angle': 9,
    'Lucky': 5,
    'Sunny': 1
}
for name, number in favorite_number.items():
    print(name + ' favorites number is ' + str(number))
print("$$$$$")
for name in favorite_number.keys():
    print('Name ' + name + " is included in name list.")
# 遍历字典时候，默认遍历所有键
print("&&&&&&")
for name in favorite_number:
    print('Name ' + name + " is included in name list.")
# 6-3, 6-4, 6-5
words = {
    'Apple': 'a fruit.',
    'Hamburg': 'a food.',
    'Beijing': 'a city.',
    'Football': 'a sport.',
    'Cat': 'an animal. '
}
for word, meaning in words.items():
    print(word + ' is ' + meaning)
print("word list is:")
for word in words.keys():
    print(word)
for meaning in words.values():
    print(meaning)
new_list = ['Hamburg', 'Beijing', 'Peony']
for word in new_list:
    if word not in words.keys():
        print('Please add this word ' + word + ' in word list.')

print('&&&&&&&&&&&& page90')
# practices (page91 and page92, #6.3.3,sorted/set)
favorite_number = {
    'Vicky': 10,
    'Mily': 9,
    'Angle': 9,
    'Lucky': 5,
    'Sunny': 1
}
names = ['Angle', 'Lucky']
for name, number in sorted(favorite_number.items()):
    print(name)
    if name in names:
        print('Hi ' + name +
              ', I know your favorite number is ' +
              str(number))
    else:
        print("Hi " + name +
              ", your name doesn't in the name list.")

for number in set(favorite_number.values()):
    print(number)


