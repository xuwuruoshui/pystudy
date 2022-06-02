# 循环

# list、tuple循环
names = ["aaa","bbb","ccc"]
for name in names:
  print(name)

# for in
sum = 0
for i in [1,2,3,4,5,6,7,8,9,10]:
  sum+=i
print(sum)

# range
# range生成100个sequence,从0到99
sum1 = 0
for i in list(range(101)):
  sum1+=i
print(sum1)


# loop
n = 100
sum3 = 0
while n > 0:
    sum3 = sum3 + n
    n = n-1
print(sum3)

# break
# 加到50跳出循环
n = 100
sum4 = 0
while n > 0:
    sum4 = sum4 + n
    n = n-1
    if n==50:
      break
print(sum4)


# continue
# 不加50,50直接跳过
n = 101
sum4 = 0
while n > 0: 
  n = n-1
  if n==50:
      continue
  sum4 = sum4 + n
    
print(sum4)