# 格式化输出, c语言形式
print('Hello %s,Today is %d' % ('Bob', 12))

# 函数形式
print('Hello {0},Today is {1}'.format("Herry", 14))

# f-string
name = "Hellen"
price = 9.999
# 取两位小数,自动给我取整了
print(f'Hello {name}, you need pay {price:.2f}')


# string不可变
a = 'abc'
print(a.replace("a", "A"))
print(a)
