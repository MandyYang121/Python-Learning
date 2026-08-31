# y = 10


def my_func(x):  # 参数也叫 x，隐藏了外面的 x
    x = 5       # 这里修改的是参数 x，不是外面的 x
    print(x)    # 输出 5
    return x


a = my_func(3)
print(a)        # 仍然是 10，没有被修改
