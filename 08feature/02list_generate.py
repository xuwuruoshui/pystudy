# 列表生成

# 生成1-10的平方
# 普通使用
L = range

# 语法糖版
print([x * x for x in range(1,11)])

# 1-10偶数平方
print([x * x for x in range(1,11) if x%2==0])