# message = input("Your age: ")
# print("My age is " + message)

message_1 = "--- Basic Information ---"
message_1 += "\nPlease enter your name: "
name = input(message_1)
print("My name is " + name)

age = input("How old are you? ")
age = int(age)
can_vote = age >= 18
# can_vote是Bool型，也需要转换成str
print("Can I vote? " + str(can_vote))

# 7-1
car = input("What kind of car do you want to rent? ")
print("Let me see if I can find you a " + car + ".")

# 7-2
seat = input("How many people will be join? ")
seat = int(seat)
if seat >= 8:
    print("There aren't enough seats here.")
else:
    print("We have enough seats.")

# 7-3
number = input("Please enter a number: ")
number = int(number)
if number % 10 == 0:
    print("This number is an integer multiple of 10.")
else:
    print("This number is NOT an integer multiple of 10.")
