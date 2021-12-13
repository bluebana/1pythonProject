"""
作者：YuanMengna
日期：2021年12月13日
"""
with open("日记.txt","r",encoding="utf8")as f:
    text=f.readlines()
for i in text:
    print(i)