students = ["张三","李四","王五"]

print(students)
# 长度
print("len:",len(students))
# 访问元素
print("student[0]:",students[0])
# 反向获取元素,以此类推
print("student[-1]:",students[-1])

# 插入
students.append("赵六")
print("插入后student[3]:",students[3])

# 插入到指定位置
students.insert(1,"test")
print("插入到位置1",students)

# 末尾删除
students.pop()
print("末尾删除:",students)

# 删除指定元素
students.pop(1)
print("删除位置1:",students)

# 修改
students[0] = "张三111"
print("修改第一个元素后:",students)


