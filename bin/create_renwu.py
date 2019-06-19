#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
import random
a = [str(i) for i in range(1,10)]
ren = ['大唐', '天魔', '方寸']
mo = ['狮驼', '魔王', '盘丝']
xian = ['天宫', '龙宫', '五庄']
menpai_dict = {'dt':'大唐','tm':'天魔','fc':'方寸','st':'狮驼','mw':'魔王','ps':'盘丝','tg':'天宫','lg':'龙宫','wz':'五庄'}
fx = ['天魔', '方寸', '盘丝', '五庄']
not_fx = ['大唐', '狮驼', '魔王', '天宫', '龙宫']


def dict1(menpai):
    def zhongzu_menpai_list(abc):
        renzu_list = []
        for i in range(0, 3):
            for x in abc:
                renzu_list.append(x)
        return renzu_list
    return dict(zip(a, zhongzu_menpai_list(menpai)))

#先 选种族
random_zhongzu = {1:'人族', 2:'魔族', 3:'仙族', 4:'仙族', 5:'魔族', 6:'人族', 7:'人族', 8:'魔族', 9:'仙族'}
#再 选门派
random_renzu_menpai  = dict1(ren)
random_mozu_menpai   = dict1(mo)
random_xianzu_menpai = dict1(xian)
os_num=random.randint(1, 9)


def ren_wu():
       print ("请选择你的 种族 和 门派\n支持中文输入, 或者简写(比如'人族'，即: 'RZ'. 比如'大唐'，即: 'DT'")
       print ("人族:\n"
              "大唐(DT) , 天魔(TM) , 方寸(FC)\n")
       print ("魔族:\n"
              "狮驼(ST) , 魔王(MW) , 盘丝(PS)\n")
       print ("仙族:\n "
              "天宫(TG) , 龙宫(LG) , 五庄(WZ)\n")

def menpai_JG(menpai):
       if menpai in menpai_dict.keys() or menpai_dict in menpai_dict.values():
              if menpai in menpai_dict.values():
                     return menpai  # 直接返回值
              return menpai_dict.get(menpai)  # 从 key get到的值
       else:
              print ("输入有误! 请重新输入 门派!\n")
              return 'error'

def men_pai(x_z):
       if x_z == 'rz' or x_z == "人族":
              print ('封系:      '
                     '天魔,  方寸\n')
              print ("物理攻击:  "
                     "大唐\n")
              print ("法系攻击:  "
                     "无\n")
              return '人族'
       elif x_z == 'mz' or x_z == '魔族':
              print ('封系:      '
                     '盘丝\n')
              print ("物理攻击:  "
                     "狮驼\n")
              print ("法系攻击:  "
                     "魔王\n")
              return '魔族'
       elif x_z == 'xz' or x_z == '仙族':
              print ('封系:      '
                     '五庄\n')
              print ("物理攻击:  "
                     "天宫\n")
              print ("法系攻击:  "
                     "龙宫\n")
              return '仙族'
       else:
              print ("输入有误! 请重新输入 种族!\n")

def fen_xi():
       print ("角色默认属性值\n封系    : 天魔,  方寸,  盘丝,  五庄\n"
              "  封印几率：20%  血量: 3600~4000  魔量: 2500 攻击力: 700~800     防御: 1000~1200  灵力: 400       速度: 400~500\n")
       print ("非封系  : 大唐,    狮驼,  魔王,  天宫,  龙宫\n "
              "  封印几率：0%   血量: 3000~3300  魔量: 2000 攻击力: 900~1000    防御: 800~900   灵力: 500~600   速度: 300~400\n")

def ren_zu():
       print ("人族\n"
              "大唐:    物理伤害提高：20%, 其他属性平均  技能: 横少千军，先发制人，后发制人\n"
              "天魔:  封印几率提高: 15%, 速度增加：30%。防御低：-15%，伤害低：-15%， 技能: 飞镖\n"
              "方寸:  封印几率提高：20%, 速度增加：30%。防御低：-15%，伤害低：-15%， 特殊技能: 五雷咒（打魔族追加伤害+100%）宠物属性：提升15%\n\n")




def mo_zu():
       print ("魔族\n"
              "狮驼:  物理伤害提高:20%   速度减慢   : -10% . 技能: 连环击,   飞击        其他平均\n"
              "魔王:  法系伤害提高:85%,  速度减慢   : -30% . 血量增加: +20%,    技能: 观音坐莲, 飞沙走石    其他平均\n"
              "盘丝:  封印几率提高:10%,  速度增加   : +20% . 防御曾强: +40%,   攻击降低:  -10% 技能: 封印, 蜘蛛群攻   .其他平均\n\n")


def xian_zu():
       print ("仙族\n"
              "天宫     物理伤害高 :10%.  速度增加:    +10%技能: 怒雷(破防 +30%）             其他平均\n"
              "龙宫     法系伤害高:80%,  速度减慢:    -30%.   血量增加 :  +10%    技能: 龙腾(单体) 龙旋雨击(群体)    其他平均\n"
              "五庄   物理伤害高:20%,  封印提高   :+5%. 速度提高  :+20%， 血量降低低:  -5%,  防御降低:  -10%  技能: 烟雨剑法 封印\n\n")
def chong_wu():
       print ("宠物\n"
              "龙女 :   伤害提高:  20%\n"
              "天兵 :   防御增加:  20%\n"
              "凤凰 :   速度增加:  20%\n"
              "蛟龙 :   法伤提高:  20%\n")