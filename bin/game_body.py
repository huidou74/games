#!/usr/bin/python
#-*- coding:utf-8 -*-
# BY :   H .c
a = [str(i) for i in range(1,10)]
ren = ['大唐','天魔','方寸']
mo = ['狮驼' , '魔王' , '盘丝']
xian = ['天宫', '龙宫' , '五庄']

def dict1(abc):
    def zhongzu_menpai_list(abc):
        renzu_list = []
        for i in range(0, 3):
            for x in ren:
                renzu_list.append(x)
        return renzu_list

    return (dict(zip(a, zhongzu_menpai_list(abc))))

# print (dict(zip(a,zhongzu_menpai_list(ren))))






# import sys
# def maaa():
#     print("OK is game body")
#     return  sys.exit
