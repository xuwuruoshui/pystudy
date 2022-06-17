
# 迭代器
g = (x*x for x in range(10))
# 一般使用for遍历不适用next,next超过了会error
# print(next(g))
# for n in g:
#     print(n)


# 斐波拉契
# def fib(max):
#     # 双指针
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n = n+1
#     return 'done'


# fib(10)

# yield
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 使用for发现没有return打印
for res in fib(6):
    print(res)
# 使用无限循环
while True:
  try:
    print("x:",next(g))
  except StopIteration as e:
    print("generate return value:",e.value)
    break



# yield具体使用
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


# 和迭代器又有不同，这个priht也会记录。像程序中断在哪里，有点像调试的断点
for res in odd():
    print(res)

