slice = ["a", "b", "c"]

# 获取所有元素
print(slice[:])

# 获取前两个元素
print(slice[:2])

# 获取后两个元素
print(slice[1:])

# 获取第两个元素
print(slice[1:2])

# 反向获取元素
print(slice[-2:])


slice2 = list(range(100))
# 前11-20个数
print(slice2[10:20])

# 前10个数，每两个取一个
print(slice2[:10:2])

# 所有数，每5个取一个
print(slice2[::5])

# tuple和字符串也可以使用切片的方式
tp = (1, 3, 6, 9)
print(tp[1:2])

str = "abcdefg"
print(str[3:5])
