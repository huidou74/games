#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
def if_username(user_JG):
    user_list = []
    with open('../conf/user_messages') as fd_r:
        while True:
            line = fd_r.readline()
            if not line:
                break
            user_list += [line.split('=')[0]]
    # for list 下面开始写
    # user_name = input("请创建您角色的用户名: ")
    for name in user_list:
        if user_JG == name:
            return 1


def old_username(user_name):
    user_list = []
    with open('../conf/user_messages') as fd_r:
        while True:
            line = fd_r.readline()
            if not line:
                break
            if user_name in line:

                return eval(line.split('=')[1].strip())



# a = old_username('hc')
# print (a)
# print (type(a))

# lines=[]
# with open('user_messages') as fd_r:
#     while True:
#         line = fd_r.readline()
#         if not line:
#             break
#         lines += [line.split('=')[0]]
# #     print (i)
# # for i in lines:
