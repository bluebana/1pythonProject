"""
作者：YuanMengna
日期：2021年12月12日
"""
# class声明类的名字，首字母必须要大写
# 面向对象编程，类就是我们的对象

class Petdog():#固定的写法
    """我的宠物小狗"""
    def __init__(self,bark,height,sex,color):
        self.bark=bark
        self.height=height
        self.sex=sex
        self.color=color

    def ability(self,num):
        """小狗的能力！"""
        print("你的bark为"+self.bark+"height为"+self.height+"的小狗开始了")
        if num==1:
            print("作揖")
        elif num==2:
            print("取物")
        else:
            print("看家")

    def personnality(self):
        """小狗的个性！"""
        print("你的bark为" + self.bark + "height为" + self.height + "的小狗非常地")
        print("开朗！温柔！超级喜欢主人！聪明！")

    def friends(self):
        """小狗的朋友~"""
        print("你的bark为" + self.bark + "height为" + self.height + "的小狗的朋友是")
        print("大黄、毛毛、喵喵")

# 实例化
aa=Petdog("miaomiao","50cm","female","yellow")
print(aa.height)
aa.ability(2)
aa.friends()

#在括号里Petcat继承了Petdog,前者是子类，后者是父类
class Petcat(Petdog):
    def personnality(self):#重写
        print("害羞")

bb=Petcat("MIAOMIAO","25CM","female","black")
bb.ability(1)
bb.personnality()

"""__init__其实是类object的方法之一，
在定义init时其实就是对object做了重写"""