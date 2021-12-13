"""
作者：YuanMengna
日期：2021年12月13日
说明：学习python的方法
"""
"""可以检查要求账号长度为5-8位，密码6-12位，
并且账号必须小写字母开头"""

# def checkname(username):
#     """
#     可以检查要求账号长度为5-8位，密码6-12位，并且账号必须小写字母开头
#     """
#     if len(username) >=5 and len(username) <=8:
#         if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#             return True
#         else:
#             return "账号的首字母必须为小写！"
#     else:
#         return "请输入正确的账号名"

# def:方法定义
# checkname:方法名字
# username：方法的参数
# 方法的逻辑代码

# 使用方法：
# a="和·skjgh"
# checkname(a)
def jiafa(a,b):
    """
    这个方法的作用是做加法
    """
    return(a+b)

# jiafa(1,1)

# a=[]
# print(a.append("哈哈"))  #没有返回值
# print(jiafa(1,1))  #print改成Return之后就有返回值了

# 有返回值以后做注册可以对账号名的操作进行单独的封装

# userinfo={}
# username=input("请输入5-8位的账号名：")
# password = input("请输入6-12位的密码：")
# if checkname(username)==True:
#     if len(password) >= 6 and len(password) <= 12:
#         userinfo[username] = password
#     else:
#         print("请输入正确的密码格式")
# else:
#     print(checkname(username))

"""异常捕获"""
# try:
#     print(1+"1")
# except:
#     print("代码错了")

"""异常类"""
# try:
#     print(1+"1")
# except Exception as e:
#     print("代码错了",e)
# 显示代码错误的具体信息
#
# a=input("请输入名字;")
# b=input("请输入年龄")
# try:
#     if int(b)>18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except:
#     print("请输入正确的年龄")

# try异常捕获可以：处理用户输入的数据

# 关于python的包,引入包的时候在整个代码文件最前面进行声明
# import time
# for i in range(10):
#     time.sleep(2)
#     print(i)

# import random
# a=random.randint(0,100)
# print(a)

"""练习：定义一个方法，用来判断用户输入的账号密码是否符合规范"""

def checkuserinfo(username,password):
    """
    用来判断用户输入的账号密码是否符合规范
    """
    userinfo={}
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
            if len(password) >= 6 and len(password) <= 12:
                userinfo[username] = password
                return userinfo
            else:
             return "请输入正确的密码格式"
        else:
         return "账号的首字母必须为小写！"
    else:
         return "请输入正确的账号名"

a=input("请输入用户名：")
b=input("请输入密码：")
print(checkuserinfo(a,b))