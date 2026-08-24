names = ["Mily", "Angle", "Vicky", "Lucky", "Sunny", "Fin"]
print(names[0:3])
print(names[2:4])
print(names[-1])
print(names[-2:-4:-1])
print(names[-2:])
print(names[0:5:2])
print(names[-1:])

for name in names[0:3]:
    print(name)

numbers = []
for number in range(1, 11):
    numbers.append(number*2)
print(numbers)

numbers = [number*3 for number in range(1, 11)]
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

# Score
Scores = [58, 79, 65, 93, 80, 21, 85]
Scores.sort(reverse=True)
for Score in Scores[0:3]:
    print(Score)

# Copy List Slice
# 4-10
pets = ["Mily", "Angle", "Vicky", "Lucky", "Sunny", "Fin"]
print("The first three pets in the list are:")
print(pets[0:3])
print("The three pets from the middle of the list are:")
print(pets[2:5])
print("The last three pets in the list are:")
print(pets[-3:])

# 4-11
my_pizzas = ["Supreme pizza", "durian pizza", "steak pizza", "potato pizza", "chicken pizza"]
friend_pizzas = my_pizzas[:]
print("My favorite pizzas are: ")
my_pizzas.append("Pizza A")
print(my_pizzas)
for my_pizza in my_pizzas:
    print(my_pizza)
print("My friend's favorite pizzas are: ")
friend_pizzas.append("Pizza B")
print(friend_pizzas)
for friend_pizza in friend_pizzas:
    print(friend_pizza)

print("############")
print("My favorite pizzas are: ")
for i in range(3):
    my_pizzas[i] = my_pizzas[i] + " Pizza A"
    print(my_pizzas[i])

print("My friend's favorite pizzas are: ")
for i in range(3):
    friend_pizzas[i] = friend_pizzas[i] + " Pizza B"
    print(friend_pizzas[i])

# 4-12
