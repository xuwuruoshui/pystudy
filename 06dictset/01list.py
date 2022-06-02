# 字典类型
map = {"Jerry": {"age": 1}, "Themth": {"age": 2}, "Bob": 1}
print(map)
print(map["Jerry"])
print(map["Bob"])

map["Jerry"] = {"sex": 0}
print(map["Jerry"])

# 访问不存在的key报错
# print(map["Lake"])
# method1: 判断后再决定是否获取
if "Lake" in map:
  print(map["Lake"])
else:
  print("Lake is nil")

# method2: 使用get解决
print(map.get("Lake"))


# 删除
print(map.pop("Themth"))
print(map)