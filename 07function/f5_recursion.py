# 汉诺塔
# n个盘子放在柱子a上,小盘子放大盘子上面，要将a上的所有柱子移动到c上
# 要求: 大盘子不能在小盘子上面

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)


move(3, "A", "B", "C")
