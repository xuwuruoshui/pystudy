# set
# 去重
s = set([1, 2, 3, 2, 4, 3])
print(s)

# 添加
s.add("fff")
print(s)

# 删除
s.remove(3)
print("移除第3个", s)

# 交集/并集
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1&s2)
print(s1|s2)