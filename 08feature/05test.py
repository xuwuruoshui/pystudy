#       1
#     1   1
#  1    2    1

def triangles():
    L = [1]
    while True:
          yield L
          L = [1] + [L[n] + L[n+1] for n in range(len(L) - 1)] + [1]


g = triangles()
print(next(g))
print(next(g))
print(next(g))
print(next(g))