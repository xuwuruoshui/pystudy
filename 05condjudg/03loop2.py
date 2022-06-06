from collections.abc import Iterable
from pickle import NONE


# dict遍历
map = {
    "id": 1,
    "age": 2,
    "name": "zhangsan"
}

# 遍历key
for ch in map:
    print(ch)

# 遍历value
for ch in map.values():
    print(ch)

# 同时迭代
for k, v in map.items():
    print(k, v)

# 下标打印
for i,v in enumerate([1,3,4,5]):
  print(i,v)

# 判断变量是否可迭代
print(isinstance('abc', Iterable))
print(isinstance(map, Iterable))
print(isinstance(['a', 'b', 'c'], Iterable))



