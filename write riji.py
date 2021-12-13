"""
作者：YuanMengna
日期：2021年12月13日
"""
import time
now=time.strftime("%y-%m-%d %H:%M:%S")
text=input("请输入今天的心情：")
with open("日记.txt","a",encoding="utf8")as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("----------------------------\n")



