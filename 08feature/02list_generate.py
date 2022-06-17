# 列表生成

# 生成1-10的平方
# 普通使用
import os
L = range


# 语法糖版

# for后面循环的结果给前面的表达式使用
# 比如for的结果给 x*x使用
print([x * x for x in range(1, 11)])

# 1-10偶数平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 两层循环
print([m + n for m in 'ABC' for n in 'CDE'])

# 获取文件和目录
print([d for d in os.listdir('.')])

# 列表中的元素都转为小写
list = ["Abc", "DeF", "gHI"]
print([l.lower() for l in list])

# if else前置. if结果在前面,else结果在后面
print([x*x if x % 2 == 0 else -x for x in range(1, 11)])
