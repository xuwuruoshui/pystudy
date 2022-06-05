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
user = {"name": "张三", "age": 10}
cal1(**user)


# 5.命名关键字参数
# 5.1调用时*后面都得带名字
def person(name, age, *, city, job):
    print(name, age, city, job)


# 调用时必须把名字带上
person("张三", 12, city="成都", job="工程师")


# 5.2已经有一个*了，后面都得带名字
def person1(name, age, *arg, city, job):
    print(name, age, arg, city, job)


# 传string默认转元组
person1("张三", 12, "aaa", city="成都", job="工程师")


# 6.参数组合顺序
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1, 2)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


