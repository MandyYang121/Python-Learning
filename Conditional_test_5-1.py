# 5-1
car = 'subaru'
print("Is car =='subaru'? I predict True.")
print(car == 'subaru')
print(car == 'audi')

print("\nIs car =='audi'? I predict False")
print(car == 'audi')
print(car.upper())
print(car == 'audi')
print(car)

# 5-2
print("$$$$$$")
Name = "Sunny"
print(Name == "Sunny")
print(Name == "sunny")
print(Name == 'Lucky')
print(Name.lower())
print(Name.lower() == 'Sunny')

print("\n$$$$$$")
price_1 = 123
price_2 = 200
print(price_1 == price_2)
print(price_1 != price_2)
print(price_1 > price_2)
print(price_1 < price_2)
print(price_1 >= price_2)
print(price_1 <= price_2)
print(price_1 >= 200 and price_2 <= 210)
print(price_1 >= 200 or price_2 <= 200)

pets = ["Mily", "Angle", "Vicky", "Lucky", "Sunny", "Fin"]
favorite_pet = 'Lucky'
if favorite_pet in pets:
    print("Yes, Lucky in pets list.")
else:
    print("No")

# 5-3
alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points!')

alien_color = 'yellow'
if alien_color == 'green':
    print("You got 5 points!")

# practices
requested_toppings = ['mushrooms', 'pepperoni666', 'extra cheese']
if 'mushrooms' not in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('Finished making your pizza!')

# 5-4, 5-5
print('\n##########')
alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points!')
elif alien_color == 'Yellow':
    print('You got 10 points!')
else:
    print('You got 15 points!')

alien_color = 'yellow'
if alien_color == 'green':
    print('You got 5 points!')
elif alien_color == 'yellow':
    print('You got 10 points!')
else:
    print('You got 15 points!')

alien_color = 'red'
if alien_color == 'green':
    print('You got 5 points!')
elif alien_color == 'yellow':
    print('You got 10 points!')
else:
    print('You got 15 points!')

# 5-6
age = 4
if age < 2:
    print('Baby')
elif age < 4:
    print('Toddling children')
elif age < 13:
    print('Children')
elif age < 20:
    print('Teenager')
elif age < 65:
    print('Adult')
else:
    print('Senior citizen')

# 5-7

favorite_fruits = ['Bananas', 'Apples', 'Watermelons']
if 'Bananas' in favorite_fruits:
    print('I like Bananas.')
if 'Apples' in favorite_fruits:
    print("I like Apples.")
if 'Mangoes' in favorite_fruits:
    print("I like Mangoes.")
if 'Watermelons' in favorite_fruits:
    print("I like Watermelons.")

print('&&&&&&&&&&&&&&&&&&')
# practices
requested_toppings = ['mushrooms', 'pepperoni', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'pepperoni':
        print('Out of ' + requested_topping + '.')
    else:
        print('Adding ' + requested_topping + '.')


# 5-8
Users = ['Sunny', 'Admin', 'Vicky', 'Angle', 'Mily']
for Logged_in_user in Users:
    if Logged_in_user == 'Admin':
        print('---------')
        print('Hello Admin, would you like to see a status report?')
    else:
        print('Hello ' + Logged_in_user + ', thank you for logging in again.')

# 5-9
del Users[:]
print(Users)
if Users:
    print('Include users.')
else:
    print('No users.')

# 5-10 :区分大小写，大小写不一样认为doesn't be used.使用.lower使得大小写一致。
current_users = ['Sunny', 'Admin', 'Vicky', 'Angle', 'Mily']
new_users = ['Vicky', 'mily', 'Lucky', 'May', 'Finn']
# current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user in current_users:
        print("This user " + new_user + " has been used.")
    else:
        print("This user " + new_user + " doesn't be used.")
print('\n*************')
current_users = ['Sunny', 'Admin', 'Vicky', 'Angle', 'Mily']
new_users = ['Vicky', 'mily', 'Lucky', 'May', 'Finn']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("This user " + new_user + " has been used.")
    else:
        print("This user " + new_user + " doesn't be used.")

# 5-11 使用四种类型转换方法
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print('%drd' % num)
    else:
        print('{}th'.format(num))
