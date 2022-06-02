# 1、参数检查 isinstance()

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("错误类型")
    if x >= 0:
        return x
    elif x < 0:
        return -x


my_abs(-1)


# 2、默认参数坑

def add_end(list=[]):
    list.append("END")
    return list


# 默认不传值的坑,list居然会存在
# 有种闭包的感觉
print(add_end())
print(add_end())


# 因此改为
def add_end1(list=None):
    if list is None:
        # 新赋一个值
        list = []
    list.append("END")
    return list


print(add_end1())
print(add_end1())


# 3.可变参数,加个星表示tuple
def cal(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum


print(cal(1, 2, 3, 4, 5))
list = [1, 2, 3, 4]
print(cal(*list))


# 4.可变参数2,字典类型
def cal1(**kv):
    print(kv)


cal1(name="张三", age=10)
user = {"name":"张三", "age":10}
cal1(**user)