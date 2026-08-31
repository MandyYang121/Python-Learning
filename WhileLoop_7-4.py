
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != "quit":
    message = input(prompt)
    # print(message)
    if message != "quit":
        print(message)

prompt = "\n---Tell me something, and I will repeat it back to you:"
prompt += "\n---Enter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print("########")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        print(current_number)

x = 1
while x <= 5:
    print(x)
    x += 1

# 7-4
prompt = "We will add this topping on your pizza!"
prompt += "\n--Please enter your topping: ---"

active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

# 7-6(7-4 使用active and break)
prompt = "7-4break - We will add this topping on your pizza!"
prompt += "\n--Please enter your topping: ---"

active = True
while active:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(message)

# 7-5
prompt = "Please enter your age (or 'q' to quit): "
active = True
while active:

    age_input = input(prompt).lower()

    # 检查是否要退出
    if age_input.lower() == "q":
        print("Exiting the program.")
        break

        # 这是一个健壮的输入校验机制。
        # 尝试转为整数,避免异常输入导致的代码错误。比如输入abc
    try:
        age = int(age_input)
    except ValueError:  # 如果转换失败（输入的不是数字）
        print("Invalid input! Please enter a number or 'q' to quit.")
        continue  # 跳过本次循环，重新输入

    age = int(age_input)
    if age < 3:
        print("Free")
    elif age <= 12:
        print("10$")
    else:
        print("15$")

# 7-5
# prompt = ...缩进在 while True:内的话，会在每次循环中都执行。
# 虽然功能上影响不大（只是重复赋值），但逻辑上不合理（提示语不需要每次循环都重新定义）。
"""
while True:
    prompt = "Please enter your age (or 'q' to quit): "
    age_input = input(prompt)

    # 检查是否要退出
    if age_input.lower() == "q":
        print("Exiting the program.")
        break
"""
# 7-6(7-4 使用active and break)
