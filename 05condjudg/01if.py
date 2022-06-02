# 一个键盘录入判断
# input类型是str,需要先转为int
age = int(input("input age:"))

if age<=14:
  print("童年")
elif age>14 and age<=30:
  print("青年")
elif age>30 and age<60:
  print("中年")
else:
 print("其他")