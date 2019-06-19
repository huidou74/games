#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
import random
def num_random():    #
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    return int(str(num1) + str(num2) )
size = num_random()
def fengyin(x):     ## x 是传入的形参
    if size >= (80-int(x)):
        print('本次封印几率为: ' + str(size) + '%' + '\n触发封印')
        #return size
    else:
        print('本次封印几率为: ' + str(size) + '%' + '\n封印失败!')
        #return  size     # --->  是 int()


