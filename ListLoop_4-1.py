# 4-1
names = ['Mily', 'Sunny', 'Angle', 'Lucky', 'Vicky']
for name in names:
    print(name.title() + " is my favorite pet.")
    print("You're my best friend, " + name.title() + ".\n")
print("These are all the pets I have.")

pizzas = ["Supreme pizza", "durian pizza", "steak pizza", "potato pizza", "chicken pizza"]
for pizza in pizzas:
    print("I like " + pizza.title() + ".\n")
print("I really love pizza!")

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 10):
    square = value**2
    squares.append(square)
print(squares)
"""
squares = [value**2 for value in range (1, 10)]
print(squares)"""

# 4-3

for num in range(1, 21):
    print(num)
# 4-5
numbers = []
for number in range(1, 101):
    numbers.append(number)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6
odd_numbers = []
for odd_number in range(1, 20, 2):
    odd_numbers.append(odd_number)
print(odd_numbers)

# 4-7
divisible_number = []
for number in range(3, 31, 3):
    divisible_number.append(number)
print(divisible_number)

# 4-8
cubes = []
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)
print(cubes)

cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)
print(cubes)

# 4-9
cube = [number**3 for number in range(1, 11)]
print(cube)


