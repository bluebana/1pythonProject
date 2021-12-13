"""
这个是为了测试模板设置功能
作者：YuanMengna
日期：2021年12月11日
"""
""" 第一种判断语句"""
# a=1
# b=2
# if a>b:
#     print("a比b大")
# else:
#     print("b比a大")
""" 第二种判断语句"""
# a=2
# if a==1:
#     print("haha")
""" 第三种判断语句"""
# a=int(input("请输入年龄："))
# if a>60:
#     print("你应该退休了")
# elif a>20:
#     print("家庭的责任很重大")
# elif a>10:
#     print("时间过得很快")
# else:
#     print("童年时光最美好")
#
# a=10
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")
"""while循环"""
# a=10
# while a<20:
#     print("haha")
#     a=a+1
"""假设有10个学生的成绩，10个人分别是：一、二、三、、、； 
并且名字和成绩需要对应上，而且大于60的和小于等于60的需要分开存放"""
# 用字典存放姓名和成绩
# 录入用input
# 分类用数组存放
# highchegnji={}
# lowchengji={}
# studentlist = ["yi","er","san","si","wu","liu"]
# a=0
# # while a < len(studentlist):
#       chengji=int(input("请输入"+studentlist[a]+"的成绩："))
#       if chengji >= 60:
#             highchegnji[studentlist[a]]=chengji
#       else:
#             lowchengji[studentlist[a]]=chengji
#       a=a+1
# print("大于60的有",highchegnji)
# print("小于60的有",lowchengji)
"""for循环"""
# 遍历
# a="你好，今天你吃了吗？"
# for i in a:
#     print(i)
# 数列生成器：range 步长/步进
# b=list(range(0,100,10))
# for i in b:
#     print(i)
# """用for循环实现上面的练习"""
# highchegnji={}
# lowchengji={}
# studentlist = ["yi","er","san","si","wu","liu"]
# for i in studentlist:
#       chengji=int(input("请输入"+i+"的成绩："))
#       if chengji >= 60:
#             highchegnji[i]=chengji
#       else:
#             lowchengji[i]=chengji
# print("大于60的有",highchegnji)
# print("小于60的有",lowchengji)
"""九九乘法表"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end="  ")
#     print()
"""end的作用是控制打印时的格式
   print()可以实现换行
   占位符还有/n
   /t"""

"""练习一：模拟一个红绿灯的功能，红灯30次，绿灯35次，黄灯5次，如此循坏
 练习二：使用代码实现注册的功能：用户输入账号和密码，
 要求账号长度为5-8位，密码6-12位，并且账号必须小写字母开头，并且存储到字典{username:password}中"""
# while 1<2:
#     for i in range(30):
#         print("红")
#     for i in range(35):
#         print("绿")
#     for i in range(5):
#         print("黄")
# 练习二
# userinfo={}
# username=input("请输入5-8位的账号名：")
# if len(username)>=5 and len(username)<=8:
#     if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#         password = input("请输入6-12位的密码：")
#         if len(password) >= 6 and len(password) <= 12:
#             userinfo[username] = password
#         else:
#             print("请输入正确的密码格式")
#     else:
#         print("账号的首字母必须为小写！")
# else:
#         print("请输入正确的账号名")
# print(userinfo)

# # 红绿灯题目的优化答案：用字典提高代码可维护性
# light={"红灯":30,"绿灯":35,"黄灯":5}
# for i in light:
#     for j in range(light[i]):
#         print (i,"倒计时还有",light[i]-j,"秒")

# continue和break
# for i in range(10):
#    if i==4:
#        continue
#    print(i)
#
# for i in range(10):
#    if i==4:
#        break
#    print(i)
"""对于嵌套循环，break只会跳过一层循环"""
for i in range(1,10):
    for j in range(1,i+1):
        if i==5:
            break
        print(i,"*",j,"=",i*j,end="  ")
    print()