"""print('hello world')
a=(1,2,3,4,5)
print(a)
 锄禾日当午
 汗滴禾下土
print("haha"*3)
# 变量
# 赋值
name="张三"
print(name)
a=input("请输入：")
b=input("请输入：")
print("input获取的内容：",a+b)
#数据格式的转换"""
# type(233333)
# print(type(233333))
# print(type("笑死"))
# print(type(True))
# a=float(input("请输入："))
# b=float(input("请输入："))
# print("输入的结果是：",a+b)
# a="kahflhfdsdkjgskdh"
# print(len(a))
# 通过代码获取两端内容，并且计算它们长度的和
# a=input("请输入字符串：")
# b=input("请输入字符串：")
# len(a)
# len(b)
# print("两段内容长度的和为：",len(a)+len(b))
# a=(1,2,3,"haha","xixi","xixi",True,False)
# print(a[2])
#  print(a.index("haha"))
#  print(a.count("xixi"))
# b=(a,"hehe",1,2,3)
# print(b[0][3])
# 切片
# print(a[-1])
# print(a[0:4])
# print(a[4:6])
# print(a[:])
# 数组
# a=[1,2,3,"haha","xixi","xixi",True,False]
# a.append("数组")
# print(a)
# a.insert(0,"haha")
# print(a)
# b=a.pop(4)
# print(a)
# print(b)
# xx=["hello","nono"]
# a.extend(xx)
# print(a)
# a.remove("haha")
# print(a)
# 字典

a={"name":"张三","sex":"男","age":"24"}
# 字典的取值
# 字典的新增
# 字典的修改
# print(a["name"])
# a["height"]=186
# print(a)
# a["sex"]="女"
# print(a)
# b=a.get("name")
# print(a)
# print(b)
# c=a.pop("sex")
# print(c)
# print(a)
# d=a.get("hobby")
# print(d)
# a.update(name="李四")

"""获取用户输入的个人信息，并且存储到字典中
个人信息包括name,age,sex"""
x=input("请输入您的姓名：")
y=input("请输入您的年龄：")
z=input("请输入您的性别：")
a={"name":x,
   "age":y,
   "sex":z}
print(a)

