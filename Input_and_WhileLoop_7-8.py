# 7-8 熟食店
# 三明治订单
sandwich_orders = ['tuna', 'pastrami', 'cheese', 'veggie']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwich.append(current_sandwich)

print("All the finished sandwiches are:")
for sandwich in finished_sandwich:
    print(sandwich)

# 7-9 五香烟熏牛肉卖完了
# 先重置列表（模拟重新开始）
sandwich_orders = ['tuna', 'pastrami', 'cheese', 'pastrami', 'veggie', 'pastrami']  # 确保pastrami至少3次
finished_sandwiches = []

# 打印“pastrami卖完了”
print("Sorry, pastrami is sold out!")

# 删除所有pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 继续制作剩余三明治（复用7-8的逻辑）
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# 打印完成的三明治
print("\nAll sandwiches are ready (no pastrami):")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-10 梦想的度假胜地 - 使用列表
destinations = []  # 存储梦想的度假胜地

while True:
    destination = input("If you could visit one place in the world, where would you go? (enter 'quit' to stop) ")
    if destination.lower() == 'quit':
        break
    destinations.append(destination)

# 打印调查结果
print("\nDream destinations:")
for dest in destinations:
    print(dest)

# 7-10 梦想的度假胜地 - 使用字典
places = {}  # 存储梦想的度假胜地
polling_active = True

while polling_active:
    name = input("What is your name?")
    place = input("If you could visit one place in the world, where would you go?")

    places[name] = place

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == "no":
        polling_active = False

print("Result:")
for name, place in places.items():
    print(name + " wants to visit place " + place + " in the world.")

