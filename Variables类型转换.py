first_name = "albert"
last_name = "einstein"
message = first_name.title()+" "+last_name.title()+"once said,\"A person who never made a mistake never tried " \
                                                   "anything new.\" "
print(message)

print(first_name.title()+last_name.title())
print(first_name.upper()+last_name.upper())
print(first_name.lower()+last_name.lower())

famous_person = "albert einstein"
message = famous_person.title() + 'once said,\"A person who never made a mistake never tried'\
 'anything new.\"'
print(message)


Spacename = "  Albert Einstein  "
print(Spacename.rstrip())
print(Spacename.lstrip())
print(Spacename.strip())
print(Spacename)
print("Morning Albert Einstein:\n\tHave a good day！")

age = 18
print(type(age))
message = "Happy " + str(age) + "th Birthday!"
print(message)

'''some code from Mandy 20260509'''
print(2+6)
print(13-5)
print(2*4)
print(56/7)
mynumber = 123456
print("this is my favourite number " + str(mynumber))

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