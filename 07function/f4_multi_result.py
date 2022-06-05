# 多返回值,其实返回的是元组tuple
import math


# x轴,y轴, step步长,angle角度
def mov(x, y, step, angle=0):
    nx = x + step * math.cos(angle) 
    ny = y - step * math.sin(angle)
    return nx, ny


# Π 180度
print(mov(10, 10, 1, math.pi/6))
print(mov(10, 10, 1, math.pi/3)[1])
print(mov(10, 10, 1))
