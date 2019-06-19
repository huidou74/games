#!/usr/bin/python
#coding:utf-8
# 3大种族, 3大门派  神武回合制游戏

import sys
import time
import random
import create_renwu
import read_user_messages

tag =''
old_username =''


#   ---  游戏主体  ---- class两个类   一个是系统随机生成的   一个是玩家自定义的类
class Os_auto_user(object):
        def fengxi(self):
             hp_f = random.randint(3600, 4001)
             sd_f = random.randint(430, 501)
             gj_f = random.randint(700, 801)
             ll_f = random.randint(450, 500)
             fy_f = random.randint(1000, 1201)
             fengxi_default_attribute = {'FX': 20,
                                    'HP': hp_f,
                                    'MP': 2500,
                                    'GJ': gj_f,
                                    'FY': fy_f,
                                    'LL': ll_f,
                                    'SD': sd_f}  # 封系 默认的属性
             return fengxi_default_attribute

        def notfengxi(self):
            hp = random.randint(3000, 3301)
            gj = random.randint(900, 1001)
            ll = random.randint(500, 601)
            sd = random.randint(330, 400)
            fy = random.randint(800, 901)
            notfengxi_default_attribute = {'HP': hp,
                                           'MP': 2000,
                                           'GJ': gj,
                                           'FY': fy,
                                           'LL': ll,
                                           'SD': sd}  # 输出系 默认属性
            return notfengxi_default_attribute

        # 宠物普通属性
        # 宠物属性  血量 2500~2700 攻击 700~730 防御 500~600 速度 280~295 灵力350~380
        def chongwu(self):
            cw_hp = random.randint(2500, 2700)
            cw_gj = random.randint(700, 750)
            cw_ll = random.randint(350, 380)
            cw_sd = random.randint(280, 295)
            cw_fy = random.randint(700, 730)
            chongwu_attribute = {'HP': cw_hp,
                                 'GJ': cw_gj,
                                 'FY': cw_fy,
                                 'SD': cw_sd,
                                 'LL': cw_ll}  # 宠物 默认属性
            return chongwu_attribute

        def __init__(self,num,zhongzu,renzu,mozu,xianzu,fx,not_fx,select_zhongzu,num1=random.randint(1, 9)):
              self.num = num
              self.zhongzu = zhongzu
              self.renzu = renzu
              self.mozu = mozu
              self.xianzu = xianzu
              self.fx = fx
              self.not_fx = not_fx
              self.fengxi_default_attribute = self.fengxi()
              self.notfengxi_default_attribute = self.notfengxi()
              self.chongwu_attribute = self.chongwu()
              self.num1 = str(num1)
              self.select_zhongzu = select_zhongzu

        def os_select_user(self):
              zhongzu = self.zhongzu.get(self.num)
              if str(zhongzu) == '人族':    #人族
                     menpai = self.renzu.get(self.num1)
                     size = '{' + "'"+ zhongzu + "'" + ':' + "'" + str(menpai) +"'" + '}'
                     print ("系统随机选取\n种族: %s \n门派: %s\n" % (zhongzu,menpai))
                     return  (eval(size))
              elif str(zhongzu) == '魔族':   #魔族
                     menpai = self.mozu.get(self.num1)
                     size = '{' + "'"+ zhongzu + "'" + ':' + "'" + str(menpai) +"'" + '}'
                     print("系统随机选取\n种族: %s \n门派: %s\n" % (zhongzu, menpai))
                     return (eval(size))
              elif str(zhongzu) == '仙族':   #仙族
                     menpai = self.xianzu.get(self.num1)
                     size = '{' + "'"+ zhongzu + "'" + ':' + "'" + str(menpai) +"'" + '}'
                     print("系统随机选取\n种族: %s \n门派: %s\n" % (zhongzu, menpai))
                     return  (eval(size))
        def add_attribute(self):       # 返回的是字典，双层字典，包含了门派和属性
              # os_zhongzu = self.os_select_user().keys()  #返回系统选取的角色信息
              # os_menpai = self.os_select_user().values()
              for k,v in self.os_select_user().items():
                  # print (k)
                  # print (v)
                  if v in self.fx:         # v 是系统自定义的角色，后面的是门派的默认属性。所以到这里算是完成了 人物建模
                      return dict({v:self.fengxi_default_attribute})            # 判断是否是封系 ,封系入口
                  elif v in self.not_fx:
                      return dict({v: self.notfengxi_default_attribute})           # 输出系 ，  入口
                                   # 先建模 门派人物的默认属性，再用原先的默认值来加 门派的加强属性
        def user_add_attribute(self):              # 增加门派属性
           dict1 = self.add_attribute()
           for k, v in dict1.items():     # 就一个对 键值
               if k == '大唐':
                   dt_gj = ((int(v.get('GJ')) * 0.2)+int(v.get('GJ')))    # --> int  攻击加成
                   new_dt_gj = dict({'GJ':int(str(round(dt_gj,0)).split('.')[0])})              # 把 新的值更新进字典
                   v.update(new_dt_gj)
                   return dict({k:v})
               #TM 封印几率提高: 15%, 速度增加：30%。防御低：-15%，伤害低：-15%，
               elif k == '天魔':
                   tm_fx = (v.get('FX') + 15)             # 封印几率  加成
                   new_tm_fx = dict({'FX': tm_fx})
                   tm_sd = (v.get('SD')*0.3 + v.get('SD'))            # 速度  加成
                   new_tm_sd = dict({'SD': int(str(round(tm_sd, 0)).split('.')[0])})
                   tm_fy = (v.get('FY') - (v.get('FY')*0.15))           # 防御 降低
                   new_tm_fy = dict({'FY': int(str(round(tm_fy, 0)).split('.')[0])})
                   tm_gj = (v.get('GJ') - (v.get('GJ')*0.15))         # 攻击 降低
                   new_tm_gj = dict({'GJ': int(str(round(tm_gj, 0)).split('.')[0])})
                   for i in (new_tm_fx, new_tm_sd, new_tm_fy, new_tm_gj):
                       v.update(i)
                   return dict({k:v})
               # 封印几率提高：20%, 速度增加：30%。防御低：-15%，伤害低：-15%
               elif k == '方寸':
                   fc_fx = (v.get('FX') + 20)  # 封印几率  加成
                   new_fc_fx = dict({'FX': fc_fx})
                   fc_sd = (v.get('SD') * 0.3 + v.get('SD'))  # 速度  加成
                   new_fc_sd = dict({'SD': int(str(round(fc_sd, 0)).split('.')[0])})
                   fc_fy = (v.get('FY') - (v.get('FY') * 0.15))  # 防御 降低
                   new_fc_fy = dict({'FY': int(str(round(fc_fy, 0)).split('.')[0])})
                   fc_gj = (v.get('GJ') - (v.get('GJ') * 0.15))  # 攻击 降低
                   new_fc_gj = dict({'GJ': int(str(round(fc_gj, 0)).split('.')[0])})
                   for i in (new_fc_fx, new_fc_sd, new_fc_fy, new_fc_gj):
                       v.update(i)
                   return dict({k: v})
               # 物理伤害提高:20%   速度减慢   : -10%
               elif k == '狮驼':
                   st_gj = ((int(v.get('GJ')) * 0.2) + v.get('GJ'))  # --> int  攻击加成
                   new_dt_gj = dict({'GJ': int(str(round(st_gj, 0)).split('.')[0])})  # 把 新的值更新进字典
                   st_sd = ( v.get('SD') - (v.get('SD') * 0.1 ))  # 速度  降低
                   new_st_sd = dict({'SD': int(str(round(st_sd, 0)).split('.')[0])})
                   for i in (new_dt_gj, new_st_sd):
                       v.update(i)
                   return dict({k: v})
               # 魔王:  法系伤害提高:85%,  速度减慢 : -30% . 血量增加: +20% 技能: 观音坐莲, 飞沙走石
               elif k == '魔王':
                   mw_ll = (int(v.get('LL') * 0.85) + v.get('LL'))
                   new_mw_ll = dict({'LL': int(str(round(mw_ll, 0)).split('.')[0])})
                   mw_sd = (v.get('SD') - int((v.get('SD') * 0.3)))
                   new_mw_sd = dict({'SD': int(str(round(mw_sd, 0)).split('.')[0])})
                   mw_hp = (int(v.get('HP') * 0.2) + v.get('HP'))
                   new_mw_hp = dict({'HP': int(str(round(mw_hp, 0)).split('.')[0])})
                   for i in (new_mw_ll, new_mw_sd, new_mw_hp):
                       v.update(i)
                   return dict({k: v})
               # 盘丝:  封印几率提高:10%,  速度增加   : +20% . 防御曾强: +40%  ,攻击降低  10%
               elif k == '盘丝':
                   ps_fx = (v.get('FX') + 10)  # 封印几率  加成
                   new_ps_fx = dict({'FX': ps_fx})
                   ps_sd = (v.get('SD') * 0.2 + v.get('SD'))  # 速度  加成
                   new_ps_sd = dict({'SD': int(str(round(ps_sd, 0)).split('.')[0])})
                   ps_fy = (v.get('FY') + (v.get('FY') * 0.40))  # 防御 +
                   new_ps_fy = dict({'FY': int(str(round(ps_fy, 0)).split('.')[0])})
                   ps_gj = (v.get('GJ') - (v.get('GJ') * 0.1))  # 攻击 降低
                   new_ps_gj = dict({'GJ': int(str(round(ps_gj, 0)).split('.')[0])})
                   for i in (new_ps_fx, new_ps_sd, new_ps_fy, new_ps_gj):
                       v.update(i)
                   return dict({k: v})
               # 天宫     物理伤害高 :10%.  速度 +10%
               elif k == '天宫':
                   tg_gj = ((int(v.get('GJ')) * 0.1) + v.get('GJ'))  # --> int  攻击加成
                   new_tg_gj = dict({'GJ': int(str(round(tg_gj, 0)).split('.')[0])})  # 把 新的值更新进字典
                   tg_sd = (v.get('SD') + (v.get('SD') * 0.1))  #  速度增加
                   new_tg_sd = dict({'SD': int(str(round(tg_sd, 0)).split('.')[0])})
                   for i in (new_tg_gj, new_tg_sd):
                       v.update(i)
                   return dict({k: v})
               #龙宫     法系伤害高:80%,  速度减慢: -30%.   血量增加 :  +10%
               elif k == '龙宫':
                   lg_ll = (int(v.get('LL') * 0.8) + v.get('LL'))    # 法伤增加
                   new_lg_ll = dict({'LL': int(str(round(lg_ll, 0)).split('.')[0])})
                   lg_sd = (v.get('SD') - int((v.get('SD') * 0.3)))    # 速度降低
                   new_lg_sd = dict({'SD': int(str(round(lg_sd, 0)).split('.')[0])})
                   lg_hp = (int(v.get('HP') * 0.1) + v.get('HP'))     # 增加血量
                   new_lg_hp = dict({'HP': int(str(round(lg_hp, 0)).split('.')[0])})
                   for i in (new_lg_ll, new_lg_sd, new_lg_hp):
                       v.update(i)
                   return dict({k: v})
               # 五庄  物理伤害高:20%,  封印提高 :+5%. 速度提高  :+10%， 血量降低低:  -5%,  防御降低:  -10%
               elif k == '五庄':
                   wz_fx = (v.get('FX') + 5 )  # 封印几率  加成
                   new_wz_fx = dict({'FX': wz_fx})
                   wz_sd = (v.get('SD') * 0.1 + v.get('SD'))  # 速度  加成
                   new_wz_sd = dict({'SD': int(str(round(wz_sd, 0)).split('.')[0])})
                   wz_fy = (v.get('FY') - (v.get('FY') * 0.1))  # 防御 降低
                   new_wz_fy = dict({'FY': int(str(round(wz_fy, 0)).split('.')[0])})
                   wz_gj = (v.get('GJ') + (v.get('GJ') * 0.2))  # 攻击 增加
                   new_wz_gj = dict({'GJ': int(str(round(wz_gj, 0)).split('.')[0])})
                   wz_hp = (v.get('HP') - int(v.get('HP') * 0.05))   #  血量 降低
                   new_wz_hp = dict({'HP': int(str(round(wz_hp, 0)).split('.')[0])})
                   for i in (new_wz_fx, new_wz_sd, new_wz_fy, new_wz_gj, new_wz_hp):
                       v.update(i)
                   return dict({k: v})
        def chongwu_add_attribute(self):
           os_cw_dict = {1:'龙女',2:'天兵',3:'凤凰',4:'蛟龙',5:'龙女',6:'蛟龙',7:'天兵',8:'龙女',9:'龙女'}
           cw_random = random.randint(1, 9)
           cw = os_cw_dict.get(cw_random)
           cw_df = self.chongwu_attribute
           if cw == '龙女':
               cw_gj = (self.chongwu_attribute.get('GJ') * 0.2 + self.chongwu_attribute.get('GJ'))
               cw_df.update(dict({'GJ': int(str(round(cw_gj, 0)).split('.')[0])}))
               print ("系统随机自带宠物\n宠物名:        "+ cw+'\n' + "宠物属性增强: +20% 伤害")
               return dict({cw:cw_df})
           elif cw == '天兵':
               cw_fy = (self.chongwu_attribute.get('FY') * 0.2 + self.chongwu_attribute.get('FY'))
               cw_df.update(dict({'FY': int(str(round(cw_fy, 0)).split('.')[0])}))
               print("系统随机自带宠物\n宠物名:        "+ cw+'\n' +"宠物属性增强:  +20% 防御")
               return dict({cw: cw_df})
           elif cw == '凤凰':
               cw_sd = (self.chongwu_attribute.get('SD') * 0.2 + self.chongwu_attribute.get('SD'))
               cw_df.update(dict({'SD': int(str(round(cw_sd, 0)).split('.')[0])}))
               print("系统随机自带宠物\n宠物名:        "+ cw +'\n'+"宠物属性增强:  +20% 速度")
               return dict({cw: cw_df})
           elif cw == '蛟龙':
               cw_ll = (self.chongwu_attribute.get('LL') * 0.2 + self.chongwu_attribute.get('LL'))
               cw_df.update(dict({'LL': int(str(round(cw_ll, 0)).split('.')[0])}))
               print("系统随机自带宠物\n宠物名:        "+ cw +'\n'+"宠物属性增强:  +20% 法伤")
               return dict({cw: cw_df})


class Player(Os_auto_user):

    def __init__(self, user_name,num,zhongzu,renzu,mozu,xianzu,fx,not_fx,select_zhongzu):
        Os_auto_user.__init__(self, num,zhongzu,renzu,mozu,xianzu,fx,not_fx,select_zhongzu)
        self.fx = fx
        self.not_fx = not_fx
        self.user_name = user_name
        self.zhongzu = zhongzu
        self.renzu = renzu
        self.p_fengxi_default_attribute = self.fengxi()
        self.p_notfengxi_default_attribute = self.notfengxi()
        self.p_chongwu_attribute = self.chongwu()
        self.select_zhongzu = select_zhongzu

    def if_player(self):
        zhongzu = self.zhongzu
        if str(zhongzu) == '人族':  # 人族
            menpai = self.renzu
            size = '{' + "'" + zhongzu + "'" + ':' + "'" + str(menpai) + "'" + '}'
            print("%s 玩家选择的是\n种族: %s \n门派: %s\n" % (self.user_name, zhongzu, menpai))
            return (eval(size))
        elif str(zhongzu) == '魔族':  # 魔族
            menpai = self.renzu
            size = '{' + "'" + zhongzu + "'" + ':' + "'" + str(menpai) + "'" + '}'
            print("%s 玩家选择的是\n种族: %s \n门派: %s\n" % (self.user_name, zhongzu, menpai))
            return (eval(size))
        elif str(zhongzu) == '仙族':  # 仙族
            menpai = self.renzu
            size = '{' + "'" + zhongzu + "'" + ':' + "'" + str(menpai) + "'" + '}'
            print("%s 玩家选择的是\n种族: %s \n门派: %s\n" % (self.user_name, zhongzu, menpai))
            return (eval(size))

    def player_add_attribute(self):
        for p_k, p_v in self.if_player().items():
            if p_v in self.fx:  # v 是系统自定义的角色，后面的是门派的默认属性。所以到这里算是完成了 人物建模
                return dict({p_v: self.p_fengxi_default_attribute})  # 判断是否是封系 ,封系入口
            elif p_v in self.not_fx:
                return dict({p_v: self.p_notfengxi_default_attribute})  # 输出系 ，  入口
                # 先建模 门派人物的默认属性，再用原先的默认值来加 门派的加强属性

    def player_user_add_atrrtibute(self):
        dict2 = self.player_add_attribute()
        for p_k, p_v in dict2.items():  # 就一个对 键值
            if p_k == '大唐':
                p_dt_gj = ((int(p_v.get('GJ')) * 0.2) + int(p_v.get('GJ')))  # --> int  攻击加成
                p_new_dt_gj = dict({'GJ': int(str(round(p_dt_gj, 0)).split('.')[0])})  # 把 新的值更新进字典
                p_v.update(p_new_dt_gj)
                return dict({p_k: p_v})
            # TM 封印几率提高: 15%, 速度增加：30%。防御低：-15%，伤害低：-15%，
            elif p_k == '天魔':
                p_tm_fx = (p_v.get('FX') + 15)  # 封印几率  加成
                p_new_tm_fx = dict({'FX': p_tm_fx})
                p_tm_sd = (p_v.get('SD') * 0.3 + p_v.get('SD'))  # 速度  加成
                p_new_tm_sd = dict({'SD': int(str(round(p_tm_sd, 0)).split('.')[0])})
                p_tm_fy = (p_v.get('FY') - (p_v.get('FY') * 0.15))  # 防御 降低
                p_new_tm_fy = dict({'FY': int(str(round(p_tm_fy, 0)).split('.')[0])})
                p_tm_gj = (p_v.get('GJ') - (p_v.get('GJ') * 0.15))  # 攻击 降低
                p_new_tm_gj = dict({'GJ': int(str(round(p_tm_gj, 0)).split('.')[0])})
                for i in (p_new_tm_fx, p_new_tm_sd, p_new_tm_fy, p_new_tm_gj):
                    p_v.update(i)
                return dict({p_k: p_v})
            # 封印几率提高：20%, 速度增加：30%。防御低：-15%，伤害低：-15%
            elif p_k == '方寸':
                p_fc_fx = (p_v.get('FX') + 20)  # 封印几率  加成
                p_new_fc_fx = dict({'FX': p_fc_fx})
                p_fc_sd = (p_v.get('SD') * 0.3 + p_v.get('SD'))  # 速度  加成
                p_new_fc_sd = dict({'SD': int(str(round(p_fc_sd, 0)).split('.')[0])})
                p_fc_fy = (p_v.get('FY') - (p_v.get('FY') * 0.15))  # 防御 降低
                p_new_fc_fy = dict({'FY': int(str(round(p_fc_fy, 0)).split('.')[0])})
                p_fc_gj = (p_v.get('GJ') - (p_v.get('GJ') * 0.15))  # 攻击 降低
                p_new_fc_gj = dict({'GJ': int(str(round(p_fc_gj, 0)).split('.')[0])})
                for i in (p_new_fc_fx, p_new_fc_sd, p_new_fc_fy, p_new_fc_gj):
                    p_v.update(i)
                return dict({p_k: p_v})
            # 物理伤害提高:20%   速度减慢   : -10%
            elif p_k == '狮驼':
                p_st_gj = ((int(p_v.get('GJ')) * 0.2) + p_v.get('GJ'))  # --> int  攻击加成
                p_new_dt_gj = dict({'GJ': int(str(round(p_st_gj, 0)).split('.')[0])})  # 把 新的值更新进字典
                p_st_sd = (p_v.get('SD') - (p_v.get('SD') * 0.1))  # 速度  降低
                p_new_st_sd = dict({'SD': int(str(round(p_st_sd, 0)).split('.')[0])})
                for i in (p_new_dt_gj, p_new_st_sd):
                    p_v.update(i)
                return dict({p_k: p_v})
            # 魔王:  法系伤害提高:85%,  速度减慢 : -30% . 血量增加: +20% 技能: 观音坐莲, 飞沙走石
            elif p_k == '魔王':
                p_mw_ll = (int(p_v.get('LL') * 0.85) + p_v.get('LL'))
                p_new_mw_ll = dict({'LL': int(str(round(p_mw_ll, 0)).split('.')[0])})
                p_mw_sd = (p_v.get('SD') - int((p_v.get('SD') * 0.3)))
                p_new_mw_sd = dict({'SD': int(str(round(p_mw_sd, 0)).split('.')[0])})
                p_mw_hp = (int(p_v.get('HP') * 0.2) + p_v.get('HP'))
                p_new_mw_hp = dict({'HP': int(str(round(p_mw_hp, 0)).split('.')[0])})
                for i in (p_new_mw_ll, p_new_mw_sd, p_new_mw_hp):
                    p_v.update(i)
                return dict({p_k: p_v})
            # 盘丝:  封印几率提高:10%,  速度增加   : +20% . 防御曾强: +40%  ,攻击降低  10%
            elif p_k == '盘丝':
                p_ps_fx = (p_v.get('FX') + 10)  # 封印几率  加成
                p_new_ps_fx = dict({'FX': p_ps_fx})
                p_ps_sd = (p_v.get('SD') * 0.2 + p_v.get('SD'))  # 速度  加成
                p_new_ps_sd = dict({'SD': int(str(round(p_ps_sd, 0)).split('.')[0])})
                p_ps_fy = (p_v.get('FY') + (p_v.get('FY') * 0.40))  # 防御 +
                p_new_ps_fy = dict({'FY': int(str(round(p_ps_fy, 0)).split('.')[0])})
                p_ps_gj = (p_v.get('GJ') - (p_v.get('GJ') * 0.1))  # 攻击 降低
                p_new_ps_gj = dict({'GJ': int(str(round(p_ps_gj, 0)).split('.')[0])})
                for i in (p_new_ps_fx, p_new_ps_sd, p_new_ps_fy, p_new_ps_gj):
                    p_v.update(i)
                return dict({p_k: p_v})
            # 天宫     物理伤害高 :10%.  速度 +10%
            elif p_k == '天宫':
                p_tg_gj = ((int(p_v.get('GJ')) * 0.1) + p_v.get('GJ'))  # --> int  攻击加成
                p_new_tg_gj = dict({'GJ': int(str(round(p_tg_gj, 0)).split('.')[0])})  # 把 新的值更新进字典
                p_tg_sd = (p_v.get('SD') + (p_v.get('SD') * 0.1))  # 速度增加
                p_new_tg_sd = dict({'SD': int(str(round(p_tg_sd, 0)).split('.')[0])})
                for i in (p_new_tg_gj, p_new_tg_sd):
                    p_v.update(i)
                return dict({p_k: p_v})
            # 龙宫     法系伤害高:80%,  速度减慢: -30%.   血量增加 :  +10%
            elif p_k == '龙宫':
                p_lg_ll = (int(p_v.get('LL') * 0.8) + p_v.get('LL'))  # 法伤增加
                p_new_lg_ll = dict({'LL': int(str(round(p_lg_ll, 0)).split('.')[0])})
                p_lg_sd = (p_v.get('SD') - int((p_v.get('SD') * 0.3)))  # 速度降低
                p_new_lg_sd = dict({'SD': int(str(round(p_lg_sd, 0)).split('.')[0])})
                p_lg_hp = (int(p_v.get('HP') * 0.1) + p_v.get('HP'))  # 增加血量
                p_new_lg_hp = dict({'HP': int(str(round(p_lg_hp, 0)).split('.')[0])})
                for i in (p_new_lg_ll, p_new_lg_sd, p_new_lg_hp):
                    p_v.update(i)
                return dict({p_k: p_v})
            # 五庄  物理伤害高:20%,  封印提高 :+5%. 速度提高  :+10%， 血量降低低:  -5%,  防御降低:  -10%
            elif p_k == '五庄':
                p_wz_fx = (p_v.get('FX') + 5)  # 封印几率  加成
                p_new_wz_fx = dict({'FX': p_wz_fx})
                p_wz_sd = (p_v.get('SD') * 0.1 + p_v.get('SD'))  # 速度  加成
                p_new_wz_sd = dict({'SD': int(str(round(p_wz_sd, 0)).split('.')[0])})
                p_wz_fy = (p_v.get('FY') - (p_v.get('FY') * 0.1))  # 防御 降低
                p_new_wz_fy = dict({'FY': int(str(round(p_wz_fy, 0)).split('.')[0])})
                p_wz_gj = (p_v.get('GJ') + (p_v.get('GJ') * 0.2))  # 攻击 增加
                p_new_wz_gj = dict({'GJ': int(str(round(p_wz_gj, 0)).split('.')[0])})
                p_wz_hp = (p_v.get('HP') - int(p_v.get('HP') * 0.05))  # 血量 降低
                p_new_wz_hp = dict({'HP': int(str(round(p_wz_hp, 0)).split('.')[0])})
                for i in (p_new_wz_fx, p_new_wz_sd, p_new_wz_fy, p_new_wz_gj, p_new_wz_hp):
                    p_v.update(i)
                return dict({p_k: p_v})

    def player_chongwu_add_attribute(self, select_cw):
        os_cw_dict = {1: '龙女', 2: '天兵', 3: '凤凰', 4: '蛟龙'}
        cw = os_cw_dict.get(int(select_cw))
        cw_df = self.p_chongwu_attribute
        if cw == '龙女':
            cw_gj = (self.p_chongwu_attribute.get('GJ') * 0.2 + self.p_chongwu_attribute.get('GJ'))
            cw_df.update(dict({'GJ': int(str(round(cw_gj, 0)).split('.')[0])}))
            print(self.user_name + "玩家选择的宠物\n宠物名:        " + str(cw) + '\n' + "宠物属性增强: +20% 伤害")
            return dict({cw: cw_df})
        elif cw == '天兵':
            cw_fy = (self.p_chongwu_attribute.get('FY') * 0.2 + self.p_chongwu_attribute.get('FY'))
            cw_df.update(dict({'FY': int(str(round(cw_fy, 0)).split('.')[0])}))
            print(self.user_name + "玩家选择的宠物\n宠物名:        " + str(cw) + '\n' + "宠物属性增强:  +20% 防御")
            return dict({cw: cw_df})
        elif cw == '凤凰':
            cw_sd = (self.p_chongwu_attribute.get('SD') * 0.2 + self.p_chongwu_attribute.get('SD'))
            cw_df.update(dict({'SD': int(str(round(cw_sd, 0)).split('.')[0])}))
            print(self.user_name + "玩家选择的宠物\n宠物名:        " + cw + '\n' + "宠物属性增强:  +20% 速度")
            return dict({cw: cw_df})
        elif cw == '蛟龙':
            cw_ll = (self.p_chongwu_attribute.get('LL') * 0.2 + self.p_chongwu_attribute.get('LL'))
            cw_df.update(dict({'LL': int(str(round(cw_ll, 0)).split('.')[0])}))
            print(self.user_name + "玩家选择的宠物\n宠物名:        " + cw + '\n' + "宠物属性增强:  +20% 法伤")
            return dict({cw: cw_df})


class Fighting(object):
    os_name = ''
    os_attr = {}
    os_cw_name = ''
    os_cw_attr = {}
    player_name = ''
    player_attr = {}
    player_cw_name = ''
    player_cw_attr = {}
    os_fengyin = 0
    player_fengyin = 0
    def __init__(self,os_messages, os_chongwu, player_messages, player_chongwu, player):
        self.os_messages = os_messages      # 进来的都是 dict
        self.os_chongwu = os_chongwu
        self.player_messages = player_messages
        self.player_chongwu = player_chongwu
        self.player = player                       # 玩家的个性名字
        for k, v in self.os_messages.items():     #这是这个类开始  首先执行的东西,先把这个双层字典分解为类的公有属性
            Fighting.os_name = k
            Fighting.os_attr = v
        for k, v in self.os_chongwu.items():
            Fighting.os_cw_name = k
            Fighting.os_cw_attr = v
        for k, v in self.player_messages.items():
            Fighting.player_name = k
            Fighting.player_attr = v
        for k, v in self.player_chongwu.items():
            Fighting.player_cw_name = k
            Fighting.player_cw_attr = v

    def num_random(self):     # 封印几率
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        return int(str(num1) + str(num2))

    def os_random_num(self):        # 输出  系统 选择 攻击方式
        os_attack = {1:'物理攻击',2:'单体伤害技能',3:'群体攻击',4:'群体攻击',5:'药',6:'特殊技能',7:'物理攻击',8:'特殊技能',9:'单体伤害技能',10:'药'}
        os_num = random.randint(1,10)
        return os_attack.get(os_num)

    # def time_sleep(self):
    #     time.sleep(2)

    def fengyin(self, num):      # num 需要传值
        size = self.num_random()
        if size >= (80 - int(num)):
            print('本次封印几率为: ' + str(size) + '%' + '\n触发封印')
            return 2
        else:
            print('本次封印几率为: ' + str(size) + '%' + '\n封印失败!')  # return  size     # --->  是 int()
            return 0
    def start_if_sudu(self):    # 优先级是   先判断速度 ----判断用户的 -- 出手---- 判定伤害（封印几率）---- 写入类的公有属性 ---无线循环直到HP为0   ，即结束
        sudu_dict = {'su_os_attr' : Fighting.os_attr.get('SD'),
                     'su_os_cw_attr' : Fighting.os_cw_attr.get('SD'),
                     'su_player_attr' : Fighting.player_attr.get('SD'),
                     'su_player_cw_arrt' : Fighting.player_cw_attr.get('SD')}
        # print (sudu_dict)
        list_sd = []
        while True:
            k_a = max(sudu_dict, key=lambda k: sudu_dict[k])  # 用了一个 lambda 函数，a 是字典。 把max()里面需要的key值 赋给 lambda  然后用它去取 values 再比较大小
            sudu_dict.pop(k_a)
            list_sd.append(k_a)
            if not sudu_dict:  # 判断字典为不为空，为空就退出
                break
        return list_sd

    def start_attack(self):          #开始攻击前的判断   如果是玩家先，则  跳转去用户输入，如果是系统则 导入随机数 进行攻击。技能优先级高
        list_sd = self.start_if_sudu()
        if Fighting.player_attr.get('HP') <= 0:
            print ("游戏结束！"+ self.os_name+ "   胜利！")
            sys.exit()
        elif Fighting.os_attr.get('HP') <= 0:
            print("游戏结束！" + self.player_name+' : ' + self.player +"   胜利！")
            sys.exit()
        one = list_sd.pop(0)  # 第一个出手         #还有攻击的算法，，，，  后面的就是判别谁的 HP 为0 则退出 判定谁赢了
        self.if_attack(one)
        time.sleep(2)
        if Fighting.player_attr.get('HP') <= 0:
            print ("游戏结束！"+ self.os_name+ "   胜利！")
            sys.exit()
        elif Fighting.os_attr.get('HP') <= 0:
            print("游戏结束！" + self.player_name+' : ' + self.player +"   胜利！")
            sys.exit()
        two = list_sd.pop(0)   #第二个出手
        self.if_attack(two)
        time.sleep(2)
        if Fighting.player_attr.get('HP') <= 0:
            print ("游戏结束！"+ self.os_name+ "   胜利！")
            sys.exit()
        elif Fighting.os_attr.get('HP') <= 0:
            print("游戏结束！" + self.player_name+' : ' + self.player +"   胜利！")
            sys.exit()
        three = list_sd.pop(0)
        self.if_attack(three)
        time.sleep(2)
        if Fighting.player_attr.get('HP') <= 0:
            print ("游戏结束！"+ self.os_name+ "   胜利！")
            sys.exit()
        elif Fighting.os_attr.get('HP') <= 0:
            print("游戏结束！" + self.player_name+' : ' + self.player +"   胜利！")
            sys.exit()
        four = list_sd.pop(0)
        self.if_attack(four)
        time.sleep(2)
        if Fighting.player_attr.get('HP') <= 0:
            print ("游戏结束！"+ self.os_name+ "   胜利！")
            sys.exit()
        elif Fighting.os_attr.get('HP') <= 0:
            print("游戏结束！" + self.player_name+' : ' + self.player +"   胜利！")
            sys.exit()

    def if_attack(self,data):
        if data == 'su_os_attr':    # 又分 大唐，天魔，'方寸，狮驼，魔王，盘丝，'天宫，龙宫，五庄
            if self.os_name == '大唐':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '连击', '群体攻击': '背水一战', '药': '吃药', '特殊技能': '舍身一击'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + jineng_dict.get(jineng))
                    time.sleep(1)
                    self.os_dt_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
            elif self.os_name == '天魔':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '连击', '群体攻击': '暗器', '药': '吃药', '特殊技能': '封印'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                    time.sleep(1)
                    self.os_tm_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
            elif self.os_name == '方寸':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '五雷咒', '群体攻击': '天地道法', '药': '吃药', '特殊技能': '封印'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                    time.sleep(1)
                    self.os_fc_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
            elif self.os_name == '狮驼':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '象形', '群体攻击': '鹰击', '药': '吃药', '特殊技能': '连环击'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                    time.sleep(1)
                    self.os_st_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
            elif self.os_name == '魔王':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '观音坐莲', '群体攻击': '飞沙走石', '药': '吃药', '特殊技能': '三味真火'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                    time.sleep(1)
                    self.os_mw_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
            elif self.os_name == '盘丝':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '夺命蛛丝', '群体攻击': '千蛛手', '药': '吃药', '特殊技能': '含情脉脉'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                    time.sleep(1)
                    self.os_ps_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
            elif self.os_name == '天宫':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '怒雷', '群体攻击': '雷霆万钧', '药': '吃药', '特殊技能': '五雷轰顶'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                    time.sleep(1)
                    self.os_tg_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
            elif self.os_name == '龙宫':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '龙腾', '群体攻击': '龙旋雨击', '药': '吃药', '特殊技能': '龙啸九天'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                    time.sleep(1)
                    self.os_lg_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
            elif self.os_name == '五庄':
                if Fighting.player_attr.get('HP') > 0:
                    jineng = self.os_random_num()
                    jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '烟雨剑法', '群体攻击': '天罡剑气', '药': '吃药', '特殊技能': '天神合一'}
                    print('系统 技能： ' + self.os_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                    time.sleep(1)
                    self.os_wz_attack(jineng)
                    print (Fighting.os_name +'  状态：  '+ str(Fighting.os_attr) + '\n宠物状态 : '+Fighting.os_cw_name+' : '+ str(Fighting.os_cw_attr)+'\n\n')
                    print (Fighting.player_name +'  状态：  '+ str(Fighting.player_attr)+ '\n宠物状态 : '+ Fighting.player_cw_name +' : '+ str(Fighting.player_cw_attr)+'\n\n')
                else:
                    print(Fighting.os_name + " 系统玩家胜利！ ")
                    sys.exit()
        elif data == 'su_os_cw_attr' :
            if Fighting.player_attr.get('HP') > 0:
                if self.os_cw_name == '龙女' or self.os_cw_name == '天兵' or self.os_cw_name == '凤凰':
                    print(self.os_cw_name + "\n宠物攻击")
                    print(self.player_name + ':  承受伤害为 ' + str(
                        abs(Fighting.os_cw_attr.get('GJ') - (Fighting.player_attr.get('FY') * 0.8))))
                    size = (Fighting.player_attr.get('HP') - abs(
                        Fighting.os_cw_attr.get('GJ') - Fighting.player_attr.get(
                            'FY') * 0.8))  # 更新血量 = 玩家血量- （系统宠物攻击-（玩家防御*0.8））
                    print(self.os_name + ' HP:' + str(size))
                    dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                    Fighting.player_attr.update(dict_size)
                elif self.os_cw_name == '蛟龙' :
                    print (self.os_cw_name + "\n宠物攻击")
                    print(self.player_name + ':  法系伤害为 ' + str( abs(Fighting.os_cw_attr.get('LL') - (Fighting.player_attr.get('LL') * 0.8))))
                    size = (Fighting.player_attr.get('HP') - abs(Fighting.os_cw_attr.get('LL') - Fighting.player_attr.get('LL') * 0.8))  # 更新血量 = 玩家血量- （系统宠物攻击-（玩家防御*0.8））
                    print(self.os_name + ' HP:' + str(size))
                    dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                    Fighting.player_attr.update(dict_size)
            else:
                print(Fighting.os_name + " 系统玩家胜利！ ")
                sys.exit()
        elif data == 'su_player_attr':
            print ('玩家')               # 玩家速度判断的 入口！！
            self.if_player_attack()
        elif data == 'su_player_cw_arrt':
            if Fighting.os_attr.get('HP') > 0:
                if self.player_cw_name == '龙女' or self.player_cw_name == '天兵' or self.player_cw_name == '凤凰':
                    print(self.player_cw_name + "\n宠物攻击")
                    print(self.os_name + ':  承受伤害为 ' + str( abs(Fighting.player_cw_attr.get('GJ') - (Fighting.os_attr.get('FY') * 0.8))))
                    size = (Fighting.os_attr.get('HP') - abs(Fighting.player_cw_attr.get('GJ') - Fighting.os_attr.get('FY') * 0.8))  # 更新血量 = 玩家血量- （系统宠物攻击-（玩家防御*0.8））
                    print(self.player_name + ' HP:' + str(size))
                    dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                    Fighting.os_attr.update(dict_size)
                elif self.player_cw_name == '蛟龙':
                    print (self.player_cw_name + "\n宠物攻击")
                    print(self.os_name + ':  法系伤害为 ' + str( abs(Fighting.player_cw_attr.get('LL') - (Fighting.os_attr.get('LL') * 0.8))))
                    size = (Fighting.os_attr.get('HP') - abs(Fighting.player_cw_attr.get('LL') - Fighting.os_attr.get('LL') * 0.8))  # 更新血量 = 玩家血量- （系统宠物攻击-（玩家防御*0.8））
                    print(self.player_name + ' HP:' + str(size))
                    dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                    Fighting.os_attr.update(dict_size)
            else:
                print(Fighting.os_name + " 玩家胜利！ ")
                sys.exit()

    def player_input(self):
        a = random.randint(0,100)
        if a <= 15 :
            player_dict = {1: '物理攻击', 2: '单体伤害技能', 3: '群体攻击', 4: '特殊技能'}
            player = input("1:'物理攻击',2:'单体伤害技能',3:'群体攻击',4:'特殊技能'\n请选择使用的技能： ")
            if player in '1234':
                return player_dict.get(int(player))
            else:
                print("输入错误请重新输入！")
                self.player_input()
        elif a >= 16 and a < 30:
            player_dict = {1: '物理攻击', 2: '单体伤害技能', 3: '群体攻击', 4: '药'}
            player = input("1:'物理攻击',2:'单体伤害技能',3:'群体攻击',4:'药'\n请选择使用的技能： ")
            if player in '1234':
                return player_dict.get(int(player))
            else:
                print("输入错误请重新输入！")
                self.player_input()
        elif a >= 30:
            player_dict = {1: '物理攻击', 2: '单体伤害技能', 3: '群体攻击'}
            player = input("1:'物理攻击',2:'单体伤害技能',3:'群体攻击'  \n请选择使用的技能： ")
            if player in '123':
                return player_dict.get(int(player))
            else:
                print("输入错误请重新输入！")
                self.player_input()

    def os_dt_attack(self, data):    #1: '物理攻击',2:'单体伤害技能95%',3:,3:'群体攻击75%',4:'药+500',5:'特殊技能'
        if Fighting.os_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    abs(Fighting.os_attr.get('GJ') - (Fighting.player_attr.get('FY') * 0.8))))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ')*0.9 - Fighting.player_attr.get(
                    'FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':  # 连击
                print(self.player_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)) + 'X  两次伤害')
                size = (Fighting.player_attr.get('HP') - abs(
                    (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                total = (size - abs((Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(total, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size)  # 存入
            elif data == '群体攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))  # 人
                print(self.player_cw_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('GJ') * 0.8) - Fighting.player_cw_attr.get('FY')))  # 宠物
                size = (Fighting.player_attr.get('HP') - (
                        abs(Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - (
                            abs(Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_cw_name + ' HP:' + str(size_cw))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.player_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.os_name + " 吃药 +500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.os_name + ' HP:' + str(size))
                Fighting.os_attr.update(dict_size)
            elif data == '特殊技能':
                print(self.player_name + ":  承受巨大伤害 " + str(
                    (Fighting.os_attr.get('GJ') * 1.5) - (Fighting.player_attr.get('FY') * 0.8)))
                print(self.os_name + ":  特殊技能自我扣血 " + str(Fighting.os_attr.get('GJ') * 0.2))

                size = (Fighting.player_attr.get('HP') - abs(
                    (Fighting.os_attr.get('GJ') * 1.5) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                size_os = abs(Fighting.os_attr.get('HP') - (Fighting.os_attr.get('GJ') * 0.2))
                dict_size_os = {'HP': int(str(round(size_os, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size_os)  # 存入结果 自我扣血
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
        else:
            print(Fighting.os_name + " 被封印了。本回合不动作")
            Fighting.os_fengyin = Fighting.os_fengyin - 1

    def os_tm_attack(self, data):
        if Fighting.os_fengyin == 0 :
            if data == '特殊技能':
                Fighting.player_fengyin = self.fengyin(self.os_attr.get('FX'))
            elif data == '物理攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    Fighting.os_attr.get('GJ') - (Fighting.player_attr.get('FY') * 0.8)))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ') - Fighting.player_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':
                print(self.player_name + ':  承受伤害 ' + str(
                        (Fighting.os_attr.get('GJ') ) - (Fighting.player_attr.get('FY') * 0.8)) + 'X  两次伤害')
                size = (Fighting.player_attr.get('HP') - abs(
                        (Fighting.os_attr.get('GJ')* 0.8 ) - (Fighting.player_attr.get('FY') * 0.8)))
                total = (size - abs((Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(total, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入
            elif data == '群体攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))  # 人
                print(self.player_cw_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('GJ') * 0.8) - Fighting.player_cw_attr.get('FY')))  # 宠物
                size = (Fighting.player_attr.get('HP') - abs((Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - (
                            abs(Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_name + ' HP:' + str(size_cw))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else:
                    print(self.player_cw_name + "宠物已死，出局")
            elif data == '药':
                print(self.os_name + " 吃药 + 500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.os_attr.update(dict_size)
        else:
            print(Fighting.os_name + " 被封印了。本回合不动作")
            Fighting.os_fengyin = Fighting.os_fengyin - 1

    def os_fc_attack(self, data):          #   方寸
        if Fighting.os_fengyin == 0 :
            if data == '特殊技能':
                Fighting.player_fengyin = self.fengyin(self.os_attr.get('FX'))
            elif data == '物理攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    Fighting.os_attr.get('GJ') - (Fighting.player_attr.get('FY') * 0.8)))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ') - Fighting.player_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':             # 固伤
                print(self.player_name + ':  承受伤害 ' + str(Fighting.os_attr.get('LL')*1.3 ))
                size = (Fighting.player_attr.get('HP') - (Fighting.os_attr.get('LL')*1.3))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('LL') * 0.8) - (Fighting.player_attr.get('LL') * 0.8)))  # 人
                print(self.player_cw_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('LL') * 0.8) - Fighting.player_cw_attr.get('LL')))  # 宠物
                size = (Fighting.player_attr.get('HP') - abs(
                        (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - abs(
                            (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_cw_name + ' HP:' + str(size))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else:
                    print(self.player_cw_name + "宠物已死，出局")
            elif data == '药':
                print(self.os_name + " 吃药 + 500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.os_name + ' HP:' + str(size))
                Fighting.os_attr.update(dict_size)
        else:
            print(Fighting.os_name + " 被封印了。本回合不动作")
            Fighting.os_fengyin = Fighting.os_fengyin - 1

    def os_st_attack(self, data):     # 狮驼
        if Fighting.os_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.player_name + ':  承受伤害 ' + str(abs(Fighting.os_attr.get('GJ') - (Fighting.player_attr.get('FY') * 0.8))))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ')*0.9 - Fighting.player_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':  #
                print(self.player_name + ':  承受伤害 ' + str(abs(Fighting.os_attr.get('GJ') - Fighting.player_attr.get('FY'))))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ') * 1.2 - Fighting.player_attr.get('FY') ))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('GJ') * 0.9) - (Fighting.player_attr.get('FY') * 0.8)))  # 人
                print(self.player_cw_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('GJ') * 0.9) - Fighting.player_cw_attr.get('FY')))  # 宠物

                size = (Fighting.player_attr.get('HP') - abs(
                        (Fighting.os_attr.get('GJ') * 0.9) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - abs((Fighting.os_attr.get('GJ') * 0.9) - (Fighting.player_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_name + ' HP:' + str(size_cw))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.player_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.os_name + " 吃药 +500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.os_name + ' HP:' + str(size))
                Fighting.os_attr.update(dict_size)

            elif data == '特殊技能':    #  3 连击
                print(self.player_name + ":  1连伤害 " + str(
                    (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                size = (Fighting.player_attr.get('HP') - abs(
                    (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size)  # 存入结果1 人物
                time.sleep(1)
                print(self.player_name + ":  2连伤害 " + str(
                    (Fighting.os_attr.get('GJ') * 0.9) - (Fighting.player_attr.get('FY') * 0.8)))
                size2 = (Fighting.player_attr.get('HP') - abs(
                    (Fighting.os_attr.get('GJ') * 0.9) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size2 = {'HP': int(str(round(size2, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size2)  # 存入结果2 人物
                time.sleep(1)
                print(self.player_name + ":  3连伤害 " + str(
                    (Fighting.os_attr.get('GJ') * 1.3) - (Fighting.player_attr.get('FY') * 0.8)))
                size3 = (Fighting.player_attr.get('HP') - abs(
                    (Fighting.os_attr.get('GJ') * 1.3) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size3 = {'HP': int(str(round(size3, 0)).split('.')[0])}
                print(self.os_name + ' HP:' + str(dict_size3))
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size3)  # 存入结果3 人物
                time.sleep(1)
                size_os = abs(Fighting.os_attr.get('HP') - (Fighting.os_attr.get('GJ') * 0.1))
                dict_size_os = {'HP': int(str(round(size_os, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size_os)  # 存入结果 自我扣血
                print(self.os_name + ":  特殊技能自我扣血 " + str(Fighting.os_attr.get('GJ') * 0.2))
        else:
            print(Fighting.os_name + " 被封印了。本回合不动作")
            Fighting.os_fengyin = Fighting.os_fengyin - 1

    def os_mw_attack(self, data):
        if Fighting.os_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    abs(Fighting.os_attr.get('GJ') - (Fighting.player_attr.get('FY') * 0.8))))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ') - Fighting.player_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':  #    观音坐莲
                print(self.player_name + ':  法系伤害 ' + str((Fighting.os_attr.get('LL') *0.9) - (Fighting.player_attr.get('LL'))) + 'X  两次伤害')
                size = (Fighting.player_attr.get('HP') - abs((Fighting.os_attr.get('LL') * 0.9) - (Fighting.player_attr.get('LL'))))
                total = (size - abs((Fighting.os_attr.get('LL') * 0.9) - (Fighting.player_attr.get('LL'))))
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(total, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size)  # 存入
            elif data == '群体攻击':
                print(self.player_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('LL') * 0.8) - (Fighting.player_attr.get('LL') )))  # 人
                print(self.player_cw_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('LL') * 0.8) - Fighting.player_cw_attr.get('LL')))  # 宠物
                size = (Fighting.player_attr.get('HP') - abs((Fighting.os_attr.get('LL') * 0.8) - (Fighting.player_attr.get('LL'))))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - (
                            abs(Fighting.os_attr.get('LL') * 0.8) - (Fighting.player_cw_attr.get('LL'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_cw_name + ' HP:' + str(size_cw))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.player_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.os_name + " 吃药 +500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.os_name + ' HP:' + str(size))
                Fighting.os_attr.update(dict_size)
            elif data == '特殊技能':
                print(self.player_name + ":  承受巨大伤害 " + str(
                    (Fighting.os_attr.get('LL') * 2) - (Fighting.player_attr.get('LL') * 0.8)))
                print(self.os_name + ":  特殊技能自我扣血 " + str(Fighting.os_attr.get('GJ') * 0.2))

                size = (Fighting.player_attr.get('HP') - abs(
                    (Fighting.os_attr.get('LL') * 2) - (Fighting.player_attr.get('LL') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                size_os = abs(Fighting.os_attr.get('HP') - (Fighting.os_attr.get('LL') * 0.3))
                dict_size_os = {'HP': int(str(round(size_os, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size_os)  # 存入结果 自我扣血
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))

    def os_ps_attack(self, data):
        if Fighting.os_fengyin == 0 :
            if data == '特殊技能':
                Fighting.player_fengyin = self.fengyin(self.os_attr.get('FX'))
            elif data == '物理攻击':
                print(self.player_name + ':  固定伤害 ' + str(
                    Fighting.os_attr.get('GJ') - (Fighting.player_attr.get('FY') * 0.8)))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ') - Fighting.player_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':             # 固伤
                print(self.player_name + ':  固定伤害 ' + str(Fighting.os_attr.get('LL')*1.3 ))
                size = (Fighting.player_attr.get('HP') - (Fighting.os_attr.get('LL')*1.3))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.player_name + ':  固定伤害 ' + str(
                    (Fighting.os_attr.get('LL') ) - (Fighting.player_attr.get('LL') * 0.8)))  # 人
                print(self.player_cw_name + ':  固定伤害 ' + str(
                    (Fighting.os_attr.get('LL') ) - Fighting.player_cw_attr.get('LL')* 0.8))  # 宠物

                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('LL') - (Fighting.player_attr.get('LL') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - abs(Fighting.os_attr.get('LL') - (Fighting.player_cw_attr.get('LL')*0.8)))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_cw_name + ' HP:' + str(size))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else:
                    print(self.player_cw_name + "宠物已死，出局")
            elif data == '药':
                print(self.os_name + " 吃药 + 500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.os_name + ' HP:' + str(size))
                Fighting.os_attr.update(dict_size)
        else:
            print(Fighting.os_name + " 被封印了。本回合不动作")
            Fighting.os_fengyin = Fighting.os_fengyin - 1

    def os_tg_attack(self, data):
        if Fighting.os_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.player_name + ':  承受伤害 ' + str(abs(Fighting.os_attr.get('GJ') - (Fighting.player_attr.get('FY')))))

                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ') - Fighting.player_attr.get('FY') ))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':  #  怒雷
                print(self.player_name + ':  承受伤害 ' + str(abs(Fighting.os_attr.get('GJ')*1.5 - (Fighting.player_attr.get('FY')*0.7))))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ') * 1.5 - Fighting.player_attr.get('FY') * 0.7))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.player_name + ':  承受伤害 ' + str((Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))  # 人
                print(self.player_cw_name + ':  承受伤害 ' + str((Fighting.os_attr.get('GJ') * 0.8) - Fighting.player_cw_attr.get('FY')* 0.8))  # 宠物

                size = (Fighting.player_attr.get('HP') - abs(
                        (Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - abs((Fighting.os_attr.get('GJ') * 0.8) - (Fighting.player_cw_attr.get('FY')* 0.8)))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_name + ' HP:' + str(size_cw))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.player_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.os_name + " 吃药 +500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.os_name + ' HP:' + str(size))
                Fighting.os_attr.update(dict_size)

            elif data == '特殊技能':    #  五雷轰顶
                wuleihongding = random.randint(0,100)
                if wuleihongding <= 35:
                    print ('本次几率为: '+ str(wuleihongding)+ '%'+ "   五雷轰顶成功" )
                    print(self.player_name + ":  承受巨大伤害 " + str((Fighting.player_attr.get('HP') * 0.65)))
                    size = (Fighting.player_attr.get('HP') - (Fighting.player_attr.get('HP') * 0.65))
                    dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                    Fighting.player_attr.update(dict_size)  # 存入结果 人物
                    print(self.os_name + ' HP:' + str(size))
                    print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                else :
                    print("本次几率为： "+ str(wuleihongding)+ '%' + "   五雷轰顶失败")
                    print(self.player_name + ":  承受少量伤害 " + str((Fighting.player_attr.get('HP') * 0.15)))
                    size = (Fighting.player_attr.get('HP') - (Fighting.player_attr.get('HP') * 0.15))
                    dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                    Fighting.player_attr.update(dict_size)  # 存入结果 人物
                    print(self.os_name + ' HP:' + str(size))
                    print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
        else:
            print(Fighting.os_name + " 被封印了。本回合不动作")
            Fighting.os_fengyin = Fighting.os_fengyin - 1

    def os_lg_attack(self, data):
        if Fighting.os_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.player_name + ':  承受伤害 ' + str(abs(Fighting.os_attr.get('GJ') - (Fighting.player_attr.get('FY')))))

                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ') - Fighting.player_attr.get('FY') ))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':
                print(self.player_name + ':  法系伤害 ' + str(abs(Fighting.os_attr.get('LL') - (Fighting.player_attr.get('LL')*0.8))))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('LL') - Fighting.player_attr.get('LL') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.player_name + ':  法系伤害 ' + str((Fighting.os_attr.get('LL') * 0.8) - (Fighting.player_attr.get('LL') * 0.8)))  # 人
                print(self.player_cw_name + ':  法系伤害 ' + str((Fighting.os_attr.get('LL') * 0.8) - Fighting.player_cw_attr.get('LL')* 0.8))  # 宠物

                size = (Fighting.player_attr.get('HP') - abs(
                        (Fighting.os_attr.get('LL') * 0.8) - (Fighting.player_attr.get('LL') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - abs((Fighting.os_attr.get('LL') * 0.8) - (Fighting.player_cw_attr.get('LL')* 0.8)))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_name + ' HP:' + str(size_cw))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.player_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.os_name + " 吃药 +500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.os_name + ' HP:' + str(size))
                Fighting.os_attr.update(dict_size)

            elif data == '特殊技能':    #  龙啸九天
                print(self.player_name + ":  承受巨大伤害 " + str((Fighting.player_attr.get('HP') * 0.2+Fighting.os_attr.get('LL')*0.6)))
                size = (Fighting.player_attr.get('HP') - (Fighting.player_attr.get('HP') * 0.2 + Fighting.os_attr.get('LL')*0.6))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size)  # 存入结果 人物
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
        else:
            print(Fighting.os_name + " 被封印了。本回合不动作")
            Fighting.os_fengyin = Fighting.os_fengyin - 1

    def os_wz_attack(self, data):
        if Fighting.os_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.player_name + ':  承受伤害 ' + str(abs(Fighting.os_attr.get('GJ')*0.8 - (Fighting.player_attr.get('FY') ))))
                size = (Fighting.player_attr.get('HP') - abs(Fighting.os_attr.get('GJ')*0.8 - Fighting.player_attr.get('FY') ))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.player_attr.update(dict_size)
            elif data == '单体伤害技能':  # 连击
                print(self.player_name + ':  承受伤害 ' + str(
                    (Fighting.os_attr.get('GJ') * 0.7) - (Fighting.player_attr.get('FY'))) + 'X  两次伤害')
                size = (Fighting.player_attr.get('HP') - abs(
                    (Fighting.os_attr.get('GJ') * 0.7) - (Fighting.player_attr.get('FY'))))
                total = (size - abs((Fighting.os_attr.get('GJ') * 0.7) - (Fighting.player_attr.get('FY'))))
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                dict_size = {'HP': int(str(round(total, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size)  # 存入
            elif data == '群体攻击':
                print(self.player_name + ':  承受伤害 ' + str((Fighting.os_attr.get('GJ') * 0.7) - (Fighting.player_attr.get('FY'))))  # 人
                print(self.player_cw_name + ':  承受伤害 ' + str((Fighting.os_attr.get('GJ') * 0.7) - Fighting.player_cw_attr.get('FY')))  # 宠物
                size = (Fighting.player_attr.get('HP') - (abs(Fighting.os_attr.get('GJ') * 0.7) - (Fighting.player_attr.get('FY'))))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                Fighting.player_attr.update(dict_size)  # 存入结果 人物

                if Fighting.player_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.player_cw_attr.get('HP') - (abs(Fighting.os_attr.get('GJ') * 0.7) - (Fighting.player_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_cw_name + ' HP:' + str(size_cw))
                    Fighting.player_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.player_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.os_name + " 吃药 +500 HP ! ")
                size = Fighting.os_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.os_name + ' HP:' + str(size))
                Fighting.os_attr.update(dict_size)
            elif data == '特殊技能':
                print(self.os_name + ":  增加自我双倍血量 " + str((Fighting.os_attr.get('HP')*2)))
                size = (Fighting.os_attr.get('HP')* 2 )
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size)  # 存入结果 人物
                print(self.os_name + ' HP:' + str(size))
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
        else:
            print(Fighting.os_name + " 被封印了。本回合不动作")
            Fighting.os_fengyin = Fighting.os_fengyin - 1

    def if_player_attack(self):
        data = self.player_input()     # 这里是技能选择
        if self.player_name == '大唐':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '连击', '群体攻击': '背水一战', '药': '吃药', '特殊技能': '舍身一击'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + str(jineng_dict.get(jineng)))
                time.sleep(1)
                self.player_dt_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()
        elif self.player_name == '天魔':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '连击', '群体攻击': '暗器', '药': '吃药', '特殊技能': '封印'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + jineng_dict.get(jineng))
                time.sleep(1)
                self.player_tm_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()
        elif self.player_name == '方寸':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '五雷咒', '群体攻击': '天地道法', '药': '吃药', '特殊技能': '封印'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + jineng_dict.get(jineng))
                time.sleep(1)
                self.player_fc_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()
        elif self.player_name == '狮驼':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '象形', '群体攻击': '鹰击', '药': '吃药', '特殊技能': '连环击'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + jineng_dict.get(jineng))
                time.sleep(1)
                self.player_st_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()
        elif self.player_name == '魔王':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '观音坐莲', '群体攻击': '飞沙走石', '药': '吃药', '特殊技能': '三味真火'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + jineng_dict.get(jineng))
                time.sleep(1)
                self.player_mw_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()
        elif self.player_name == '盘丝':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '夺命蛛丝', '群体攻击': '千蛛手', '药': '吃药', '特殊技能': '含情脉脉'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + jineng_dict.get(jineng))
                time.sleep(1)
                self.player_ps_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()
        elif self.player_name == '天宫':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '怒雷', '群体攻击': '雷霆万钧', '药': '吃药', '特殊技能': '五雷轰顶'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + jineng_dict.get(jineng))
                time.sleep(1)
                self.player_tg_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()
        elif self.player_name == '龙宫':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '龙腾', '群体攻击': '龙旋雨击', '药': '吃药', '特殊技能': '龙啸九天'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + jineng_dict.get(jineng))
                time.sleep(1)
                self.player_lg_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()
        elif self.player_name == '五庄':
            if Fighting.os_attr.get('HP') > 0:
                jineng = data
                jineng_dict = {'物理攻击': '普通攻击', '单体伤害技能': '烟雨剑法', '天罡剑气': '龙旋雨击', '药': '吃药', '特殊技能': '天神合一'}
                print('玩家选择的技能： ' + self.player_name + ' 使用 ' + jineng_dict.get(jineng))
                time.sleep(1)
                self.player_wz_attack(jineng)
                # 下面的两个 print 是返回 当前角色状态
                print(Fighting.os_name + '  状态：  ' + str(
                    Fighting.os_attr) + '\n宠物状态 : ' + Fighting.os_cw_name + ' : ' + str(Fighting.os_cw_attr) + '\n\n')
                print(Fighting.player_name + '  状态：  ' + str(
                    Fighting.player_attr) + '\n宠物状态 : ' + Fighting.player_cw_name + ' : ' + str(
                    Fighting.player_cw_attr) + '\n\n')
            else:
                print(self.player + " 恭喜您赢了 ！ ")
                sys.exit()




# 将 player 的方法重写 一遍  还没写完， 这个地方需要一个入口 方法  还要写， 写完这两个就可以把类放 主体内执行了，最后完善结尾
    def player_dt_attack(self, data):    #1: '物理攻击',2:'单体伤害技能95%',3:,3:'群体攻击75%',4:'药+500',5:'特殊技能'
        if Fighting.player_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.os_name + ':  承受伤害 ' + str(
                    abs(Fighting.player_attr.get('GJ') - (Fighting.os_attr.get('FY') * 0.8))))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ')*0.9 - Fighting.os_attr.get(
                    'FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':  # 连击
                print(self.os_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)) + 'X  两次伤害')
                size = (Fighting.os_attr.get('HP') - abs(
                    (Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                total = (size - abs((Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                print(self.os_name + '的 HP:' + str( Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(total, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size)  # 存入
            elif data == '群体攻击':
                print(self.os_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))  # 人
                print(self.os_cw_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('GJ') * 0.8) - Fighting.os_cw_attr.get('FY')))  # 宠物
                size = (Fighting.os_attr.get('HP') - (
                        abs(Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - (
                            abs(Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_cw_name + ' HP:' + str(size_cw))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.os_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.player_name + " 吃药 +500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)
            elif data == '特殊技能':
                print(self.os_name + ":  承受巨大伤害 " + str(
                    (Fighting.player_attr.get('GJ') * 1.5) - (Fighting.os_attr.get('FY') * 0.8)))
                print(self.player_name + ":  特殊技能自我扣血 " + str(Fighting.player_attr.get('GJ') * 0.2))

                size = (Fighting.os_attr.get('HP') - abs(
                    (Fighting.player_attr.get('GJ') * 1.5) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                size_os = abs(Fighting.player_attr.get('HP') - (Fighting.player_attr.get('GJ') * 0.2))
                dict_size_os = {'HP': int(str(round(size_os, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size_os)  # 存入结果 自我扣血
                print (self.os_name + '的 HP:' + str( Fighting.os_attr.get('HP')))
        else:
            print(Fighting.player_name + " 被封印了。本回合不动作")
            Fighting.player_fengyin = Fighting.player_fengyin - 1

    def player_tm_attack(self, data):
        if Fighting.player_fengyin == 0 :
            if data == '特殊技能':
                Fighting.os_fengyin = self.fengyin(self.player_attr.get('FX'))
            elif data == '物理攻击':
                print(self.os_name + ':  承受伤害 ' + str(
                    Fighting.player_attr.get('GJ') - (Fighting.os_attr.get('FY') * 0.8)))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ') - Fighting.os_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':
                print(self.os_name + ':  承受伤害 ' + str(
                        (Fighting.player_attr.get('GJ') ) - (Fighting.os_attr.get('FY') * 0.8)) + 'X  两次伤害')
                size = (Fighting.os_attr.get('HP') - abs(
                        (Fighting.player_attr.get('GJ')* 0.8 ) - (Fighting.os_attr.get('FY') * 0.8)))
                total = (size - abs((Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(total, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入
            elif data == '群体攻击':
                print(self.os_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))  # 人
                print(self.os_cw_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('GJ') * 0.8) - Fighting.os_cw_attr.get('FY')))  # 宠物
                size = (Fighting.os_attr.get('HP') - abs((Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - (
                            abs(Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_name + ' HP:' + str(size_cw))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else:
                    print(self.os_cw_name + "宠物已死，出局")
            elif data == '药':
                print(self.player_name + " 吃药 + 500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)
        else:
            print(Fighting.player_name + " 被封印了。本回合不动作")
            Fighting.player_fengyin = Fighting.player_fengyin - 1

    def player_fc_attack(self, data):          #   方寸
        if Fighting.player_fengyin == 0 :
            if data == '特殊技能':
                Fighting.os_fengyin = self.fengyin(self.player_attr.get('FX'))
            elif data == '物理攻击':
                print(self.os_name + ':  承受伤害 ' + str(
                    Fighting.player_attr.get('GJ') - (Fighting.os_attr.get('FY') * 0.8)))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ') - Fighting.os_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':             # 固伤
                print(self.os_name + ':  承受伤害 ' + str(Fighting.player_attr.get('LL')*1.3 ))
                size = (Fighting.os_attr.get('HP') - (Fighting.player_attr.get('LL')*1.3))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.os_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('LL') * 0.8) - (Fighting.os_attr.get('LL') * 0.8)))  # 人
                print(self.os_cw_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('LL') * 0.8) - Fighting.os_cw_attr.get('LL')))  # 宠物
                size = (Fighting.os_attr.get('HP') - abs(
                        (Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - abs(
                            (Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_cw_name + ' HP:' + str(size))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else:
                    print(self.os_cw_name + "宠物已死，出局")
            elif data == '药':
                print(self.player_name + " 吃药 + 500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)
        else:
            print(Fighting.player_name + " 被封印了。本回合不动作")
            Fighting.player_fengyin = Fighting.player_fengyin - 1

    def player_st_attack(self, data):     # 狮驼
        if Fighting.player_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.os_name + ':  承受伤害 ' + str(abs(Fighting.player_attr.get('GJ') - (Fighting.os_attr.get('FY') * 0.8))))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ')*0.9 - Fighting.os_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':  #
                print(self.os_name + ':  承受伤害 ' + str(abs(Fighting.player_attr.get('GJ') - Fighting.os_attr.get('FY'))))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ') * 1.2 - Fighting.os_attr.get('FY') ))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.os_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('GJ') * 0.9) - (Fighting.os_attr.get('FY') * 0.8)))  # 人
                print(self.os_cw_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('GJ') * 0.9) - Fighting.os_cw_attr.get('FY')))  # 宠物

                size = (Fighting.os_attr.get('HP') - abs(
                        (Fighting.player_attr.get('GJ') * 0.9) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - abs((Fighting.player_attr.get('GJ') * 0.9) - (Fighting.os_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_name + ' HP:' + str(size_cw))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.os_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.player_name + " 吃药 +500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)

            elif data == '特殊技能':    #  3 连击
                print(self.os_name + ":  1连伤害 " + str(
                    (Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                size = (Fighting.os_attr.get('HP') - abs(
                    (Fighting.player_attr.get('GJ') *0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size)  # 存入结果1 人物
                time.sleep(1)
                print(self.os_name + ":  2连伤害 " + str(
                    (Fighting.player_attr.get('GJ') * 0.9) - (Fighting.os_attr.get('FY') * 0.8)))
                size2 = (Fighting.os_attr.get('HP') - abs(
                    (Fighting.player_attr.get('GJ') * 0.9) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size2 = {'HP': int(str(round(size2, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size2)  # 存入结果2 人物
                time.sleep(1)
                print(self.os_name + ":  3连伤害 " + str(
                    (Fighting.player_attr.get('GJ') * 1.3) - (Fighting.os_attr.get('FY') * 0.8)))
                size3 = (Fighting.os_attr.get('HP') - abs(
                    (Fighting.player_attr.get('GJ') * 1.3) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size3 = {'HP': int(str(round(size3, 0)).split('.')[0])}
                print(self.player_name + ' HP:' + str(dict_size3))
                Fighting.os_attr.update(dict_size3)  # 存入结果3 人物
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                time.sleep(1)
                size_os = abs(Fighting.player_attr.get('HP') - (Fighting.player_attr.get('GJ') * 0.1))
                dict_size_os = {'HP': int(str(round(size_os, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size_os)  # 存入结果 自我扣血
                print(self.player_name + ":  特殊技能自我扣血 " + str(Fighting.player_attr.get('GJ') * 0.2))
        else:
            print(Fighting.player_name + " 被封印了。本回合不动作")
            Fighting.player_fengyin = Fighting.player_fengyin - 1

    def player_mw_attack(self, data):
        if Fighting.player_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.os_name + ':  承受伤害 ' + str(abs(Fighting.player_attr.get('GJ') - (Fighting.os_attr.get('FY') * 0.8))))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ') - Fighting.os_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':  #    观音坐莲
                print(self.os_name + ':  法系伤害 ' + str((Fighting.player_attr.get('LL') *0.9) - (Fighting.os_attr.get('LL'))) + 'X  两次伤害')
                size = (Fighting.os_attr.get('HP') - abs((Fighting.player_attr.get('LL') * 0.9) - (Fighting.os_attr.get('LL'))))
                total = (size - abs((Fighting.player_attr.get('LL') * 0.9) - (Fighting.os_attr.get('LL'))))
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(total, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size)  # 存入
            elif data == '群体攻击':
                print(self.os_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('LL') * 0.8) - (Fighting.os_attr.get('LL') )))  # 人
                print(self.os_cw_name + ':  承受伤害 ' + str(
                    (Fighting.player_attr.get('LL') * 0.8) - Fighting.os_cw_attr.get('LL')))  # 宠物
                size = (Fighting.os_attr.get('HP') - abs((Fighting.player_attr.get('LL') * 0.8) - (Fighting.os_attr.get('LL'))))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - (
                            abs(Fighting.player_attr.get('LL') * 0.8) - (Fighting.os_cw_attr.get('LL'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_cw_name + ' HP:' + str(size_cw))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.os_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.player_name + " 吃药 +500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)
            elif data == '特殊技能':
                print(self.os_name + ":  承受巨大伤害 " + str((Fighting.player_attr.get('LL') * 2) - (Fighting.os_attr.get('LL') * 0.8)))
                print(self.player_name + ":  特殊技能自我扣血 " + str(Fighting.player_attr.get('GJ') * 0.2))

                size = (Fighting.os_attr.get('HP') - abs(
                    (Fighting.player_attr.get('LL') * 2) - (Fighting.os_attr.get('LL') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                size_os = abs(Fighting.player_attr.get('HP') - (Fighting.player_attr.get('LL') * 0.3))
                dict_size_os = {'HP': int(str(round(size_os, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size_os)  # 存入结果 自我扣血
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))

    def player_ps_attack(self, data):
        if Fighting.player_fengyin == 0 :
            if data == '特殊技能':
                Fighting.os_fengyin = self.fengyin(self.player_attr.get('FX'))
            elif data == '物理攻击':
                print(self.os_name + ':  固定伤害 ' + str(
                    Fighting.player_attr.get('GJ') - (Fighting.os_attr.get('FY') * 0.8)))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ') - Fighting.os_attr.get('FY') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':             # 固伤
                print(self.os_name + ':  固定伤害 ' + str(Fighting.player_attr.get('LL')*1.3 ))
                size = (Fighting.os_attr.get('HP') - (Fighting.player_attr.get('LL')*1.3))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.8））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.os_name + ':  固定伤害 ' + str(
                    (Fighting.player_attr.get('LL') ) - (Fighting.os_attr.get('LL') * 0.8)))  # 人
                print(self.os_cw_name + ':  固定伤害 ' + str(
                    (Fighting.player_attr.get('LL') ) - Fighting.os_cw_attr.get('LL')* 0.8))  # 宠物

                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('LL') - (Fighting.os_attr.get('LL') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - abs(Fighting.player_attr.get('LL') - (Fighting.os_cw_attr.get('LL')*0.8)))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_cw_name + ' HP:' + str(size))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else:
                    print(self.os_cw_name + "宠物已死，出局")
            elif data == '药':
                print(self.player_name + " 吃药 + 500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)
        else:
            print(Fighting.player_name + " 被封印了。本回合不动作")
            Fighting.player_fengyin = Fighting.player_fengyin - 1

    def player_tg_attack(self, data):
        if Fighting.player_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.os_name + ':  承受伤害 ' + str(abs(Fighting.player_attr.get('GJ') - (Fighting.os_attr.get('FY')))))

                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ') - Fighting.os_attr.get('FY') ))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':  #  怒雷
                print(self.os_name + ':  承受伤害 ' + str(abs(Fighting.player_attr.get('GJ')*1.5 - (Fighting.os_attr.get('FY')*0.7))))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ') * 1.5 - Fighting.os_attr.get('FY') * 0.7))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.os_name + ':  承受伤害 ' + str((Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))  # 人
                print(self.os_cw_name + ':  承受伤害 ' + str((Fighting.player_attr.get('GJ') * 0.8) - Fighting.os_cw_attr.get('FY')* 0.8))  # 宠物

                size = (Fighting.os_attr.get('HP') - abs((Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_attr.get('FY') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - abs((Fighting.player_attr.get('GJ') * 0.8) - (Fighting.os_cw_attr.get('FY')* 0.8)))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_name + ' HP:' + str(size_cw))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.os_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.player_name + " 吃药 +500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)

            elif data == '特殊技能':    #  五雷轰顶
                wuleihongding = random.randint(0,100)
                if wuleihongding <= 35:
                    print ('本次几率为: '+ str(wuleihongding)+ '%'+ "   五雷轰顶成功" )
                    print(self.os_name + ":  承受巨大伤害 " + str((Fighting.os_attr.get('HP') * 0.65)))
                    size = (Fighting.os_attr.get('HP') - (Fighting.os_attr.get('HP') * 0.65))
                    dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                    Fighting.os_attr.update(dict_size)  # 存入结果 人物
                    print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                else :
                    print("本次几率为： "+ str(wuleihongding)+ '%' + "   五雷轰顶失败")
                    print(self.os_name + ":  承受少量伤害 " + str((Fighting.os_attr.get('HP') * 0.15)))
                    size = (Fighting.os_attr.get('HP') - (Fighting.os_attr.get('HP') * 0.15))
                    dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                    Fighting.os_attr.update(dict_size)  # 存入结果 人物
                    print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
        else:
            print(Fighting.player_name + " 被封印了。本回合不动作")
            Fighting.player_fengyin = Fighting.player_fengyin - 1

    def player_lg_attack(self, data):
        if Fighting.player_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.os_name + ':  承受伤害 ' + str(abs(Fighting.player_attr.get('GJ') - (Fighting.os_attr.get('FY')))))

                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ') - Fighting.os_attr.get('FY') ))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':
                print(self.os_name + ':  法系伤害 ' + str(abs(Fighting.player_attr.get('LL') - (Fighting.os_attr.get('LL')*0.8))))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('LL') - Fighting.os_attr.get('LL') * 0.8))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '群体攻击':
                print(self.os_name + ':  法系伤害 ' + str((Fighting.player_attr.get('LL') * 0.8) - (Fighting.os_attr.get('LL') * 0.8)))  # 人
                print(self.os_cw_name + ':  法系伤害 ' + str((Fighting.player_attr.get('LL') * 0.8) - Fighting.os_cw_attr.get('LL')* 0.8))  # 宠物

                size = (Fighting.os_attr.get('HP') - abs((Fighting.player_attr.get('LL') * 0.8) - (Fighting.os_attr.get('LL') * 0.8)))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - abs((Fighting.player_attr.get('LL') * 0.8) - (Fighting.os_cw_attr.get('LL')* 0.8)))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.player_name + ' HP:' + str(size_cw))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.os_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.player_name + " 吃药 +500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)

            elif data == '特殊技能':    #  龙啸九天
                print(self.os_name + ":  承受巨大伤害 " + str((Fighting.os_attr.get('HP') * 0.2+Fighting.player_attr.get('LL')*0.6)))
                size = (Fighting.os_attr.get('HP') - (Fighting.os_attr.get('HP') * 0.2 + Fighting.player_attr.get('LL')*0.6))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size)  # 存入结果 人物
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
        else:
            print(Fighting.player_name + " 被封印了。本回合不动作")
            Fighting.player_fengyin = Fighting.player_fengyin - 1

    def player_wz_attack(self, data):
        if Fighting.player_fengyin == 0:  # 没封中
            if data == '物理攻击':
                print(self.os_name + ':  承受伤害 ' + str(abs(Fighting.player_attr.get('GJ')*0.8 - (Fighting.os_attr.get('FY') ))))
                size = (Fighting.os_attr.get('HP') - abs(Fighting.player_attr.get('GJ')*0.8 - Fighting.os_attr.get('FY') ))  # 返回值 = 玩家血量- （系统的攻击-（玩家防御*0.5））
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}  # 四舍五入
                Fighting.os_attr.update(dict_size)
            elif data == '单体伤害技能':  # 连击
                print(self.os_name + ':  承受伤害 ' + str((Fighting.player_attr.get('GJ') * 0.7) - (Fighting.os_attr.get('FY'))) + 'X  两次伤害')
                size = (Fighting.os_attr.get('HP') - abs((Fighting.player_attr.get('GJ') * 0.7) - (Fighting.os_attr.get('FY'))))
                total = (size - abs((Fighting.player_attr.get('GJ') * 0.7) - (Fighting.os_attr.get('FY'))))
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                dict_size = {'HP': int(str(round(total, 0)).split('.')[0])}
                Fighting.os_attr.update(dict_size)  # 存入
            elif data == '群体攻击':
                print(self.os_name + ':  承受伤害 ' + str((Fighting.player_attr.get('GJ') * 0.7) - (Fighting.os_attr.get('FY'))))  # 人
                print(self.os_cw_name + ':  承受伤害 ' + str((Fighting.player_attr.get('GJ') * 0.7) - Fighting.os_cw_attr.get('FY')))  # 宠物
                size = (Fighting.os_attr.get('HP') - (abs(Fighting.player_attr.get('GJ') * 0.7) - (Fighting.os_attr.get('FY'))))
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
                Fighting.os_attr.update(dict_size)  # 存入结果 人物

                if Fighting.os_cw_attr.get('HP') > 0:
                    size_cw = (Fighting.os_cw_attr.get('HP') - (abs(Fighting.player_attr.get('GJ') * 0.7) - (Fighting.os_cw_attr.get('FY'))))
                    dict_size_cw = {'HP': int(str(round(size_cw, 0)).split('.')[0])}
                    print(self.os_cw_name + ' HP:' + str(size_cw))
                    Fighting.os_cw_attr.update(dict_size_cw)  # 存入结果 宠物
                else :
                    print (self.os_cw_name + "宠物已死，出局")

            elif data == '药':
                print(self.player_name + " 吃药 +500 HP ! ")
                size = Fighting.player_attr.get('HP') + 500
                dict_size = {'HP': size}
                print(self.player_name + ' HP:' + str(size))
                Fighting.player_attr.update(dict_size)
            elif data == '特殊技能':
                print(self.player_name + ":  增加自我当前双倍的血量 " + str((Fighting.player_attr.get('HP')*2)))
                size = (Fighting.player_attr.get('HP')* 2 )
                dict_size = {'HP': int(str(round(size, 0)).split('.')[0])}
                Fighting.player_attr.update(dict_size)  # 存入结果 人物
                print(self.player_name + '的 HP:' + str(Fighting.player_attr.get('HP')))
                print(self.os_name + '的 HP:' + str(Fighting.os_attr.get('HP')))
        else:
            print(Fighting.player_name + " 被封印了。本回合不动作")
            Fighting.player_fengyin = Fighting.player_fengyin - 1




while True:
       print("欢迎来到神武世界\n请先创建玩家角色名 再选择你的 种族 和 门派:\n")
       # 用户选择状态
       # 3种族
       user_name = input("请创建您玩家角色名\n或者使用已创建过的的角色名: ")
       if user_name != 'q':
              if_user_name = read_user_messages.if_username(user_name)
              while True:
                     if if_user_name == 1:
                            old_username = input("该用户已存在, 是否使用原先创建过的角色名登录? \n y:是  n:返回")
                            if old_username == 'y':
                                   tag = 1
                            elif old_username == 'n':
                                   break
                            else:
                                   print("输入错误，请重新输入！")
                            # 游戏简介
                            create_renwu.fen_xi()
                            create_renwu.ren_zu()
                            create_renwu.mo_zu()
                            create_renwu.xian_zu()
                            # 3种族
                            if tag == 1:  # 将存在的玩家角色信息读出来
                                   for k, v in read_user_messages.old_username(user_name).items():
                                          old_remwu = k
                                          old_menpai = v

                                   # 返回了已存在玩家角色的信息 参数有 （角色名user_name 。种族old_remwu 。门派old_menpai）这里是第二个入口
                                   print('系统将默认引用原先的玩家角色信息\n角色名:  %s\n种族  :  %s\n门派  :  %s' % (user_name,old_remwu,old_menpai))
                            tag = 0
                            status = input("开始游戏请输入: 'start' \n退出游戏请输入: 'exit'").lower()
                            if status == 'start':
                                for k, v in read_user_messages.old_username(user_name).items():
                                    old_remwu = k
                                    old_menpai = v
                                #   传入接口参数  user_JG   zhong_zu  mp_JG  # 这里是第一个入口 开始游戏
                                a = Os_auto_user(num=create_renwu.os_num,
                                                 select_zhongzu=create_renwu.random_zhongzu.get(
                                                     create_renwu.os_num),
                                                 zhongzu=create_renwu.random_zhongzu,
                                                 renzu=create_renwu.random_renzu_menpai,
                                                 mozu=create_renwu.random_mozu_menpai,
                                                 xianzu=create_renwu.random_xianzu_menpai,
                                                 fx=create_renwu.fx,
                                                 not_fx=create_renwu.not_fx)

                                b = Player(user_name=user_name,
                                           zhongzu=old_remwu,
                                           renzu=old_menpai,
                                           fx=create_renwu.fx,
                                           not_fx=create_renwu.not_fx,
                                           num=create_renwu.os_num,
                                           mozu=create_renwu.random_mozu_menpai,
                                           xianzu=create_renwu.random_xianzu_menpai,
                                           select_zhongzu=create_renwu.random_zhongzu.get(create_renwu.os_num))

                                c = Fighting(os_messages=a.user_add_attribute(),
                                             os_chongwu=a.chongwu_add_attribute(),
                                             player_messages=b.player_user_add_atrrtibute(),
                                             player_chongwu=b.player_chongwu_add_attribute(1),
                                             player='hc')

                                while True:
                                    c.start_attack()

                            elif status == 'exit':
                                sys.exit()
                            else:
                                print("输入错误, 请重新输入！")

                     else:
                            create_renwu.ren_wu()
                            ren_wu = input("请输入你选择的 种族:  ").lower()
                            if ren_wu == 'q':
                                   break
                            # 3门派
                            zhong_zu = create_renwu.men_pai(ren_wu)
                            while True:
                                   if tag == 1:
                                          print('创建用户成功, 等待 %s 玩家确认是否开启游戏!' % old_username)
                                   else:
                                          men_pai = input("请输入你选择的 门派:  ").lower()
                                          if men_pai == 'q':
                                                 break
                                          mp_JG = create_renwu.menpai_JG(men_pai)
                                          if mp_JG == 'error':
                                                 break
                                          user_JG = {zhong_zu: mp_JG}
                                          print('您的选择是\n''种族:  ' + zhong_zu + '\n''门派:  ' + mp_JG + '\n')
                                          with open('../conf/user_messages', 'a+') as fd_w:
                                                 fd_w.write(user_name + '=' + str(user_JG) + '\n')
                                                 print('创建用户成功, 等待 %s 玩家确认是否开启游戏!' % user_name)
                                          status = input("开始游戏请输入: 'start' \n退出游戏请输入: 'exit'").lower()
                                          if status == 'start':
                                              #   传入接口参数  user_JG   zhong_zu  mp_JG  # 这里是第一个入口 开始游戏
                                              a = Os_auto_user(num=create_renwu.os_num,
                                                               select_zhongzu=create_renwu.random_zhongzu.get(
                                                                   create_renwu.os_num),
                                                               zhongzu=create_renwu.random_zhongzu,
                                                               renzu=create_renwu.random_renzu_menpai,
                                                               mozu=create_renwu.random_mozu_menpai,
                                                               xianzu=create_renwu.random_xianzu_menpai,
                                                               fx=create_renwu.fx,
                                                               not_fx=create_renwu.not_fx)

                                              b = Player(user_name=user_JG,
                                                         zhongzu=zhong_zu,
                                                         renzu=mp_JG,
                                                         fx=create_renwu.fx,
                                                         not_fx=create_renwu.not_fx,
                                                         num=create_renwu.os_num,
                                                         mozu=create_renwu.random_mozu_menpai,
                                                         xianzu=create_renwu.random_xianzu_menpai,
                                                         select_zhongzu=create_renwu.random_zhongzu.get(
                                                             create_renwu.os_num))

                                              c = Fighting(os_messages=a.user_add_attribute(),
                                                           os_chongwu=a.chongwu_add_attribute(),
                                                           player_messages=b.player_user_add_atrrtibute(),
                                                           player_chongwu=b.player_chongwu_add_attribute(1),
                                                           player='hc')

                                              while True:
                                                  c.start_attack()

                                          elif status == 'exit':
                                              sys.exit()
                                          else:
                                              print("输入错误, 请重新输入！")

       elif user_name == 'q':
              break
       else:
              print ("\n\n输入有误，请重新输入！ 退出请输入: 'q' ")


























# for kk,vv in v.items():   # 把值里的 字典循环出来拿到 它的默认属性   测试 完成
#     print (kk)
#     print (type(vv))
# print ("system user messages: \n os user : "+ self.add_attribute())

#判断你自动创建的角色  对应上 是不是封系  再加默认属性！


# ddd={'HP': 123}
# for k, v in ddd.items():
#     print type(k)   --> <type 'str'>
#     print type(v)   --> <type 'int'>
# <type 'int'>












# print (c.os_random_num())   #测试 随机技能
# print (type(c.start_if_sudu()))
# c.start_attack()   #测试速度

# print (c.start_if_sudu())      #  测试 出手的优先级   判别
#输出结果
#{'su_os_attr': 549, 'su_os_cw_attr': 284, 'su_player_attr': 569, 'su_player_cw_arrt': 291}
#['su_player_attr', 'su_os_attr', 'su_player_cw_arrt', 'su_os_cw_attr']




#---------------------------------------
# c.start_sudu()
# 测试属性
# c.wirte_class_attr()
# print ('==================================================')
# print (Fighting.os_name)
# print (Fighting.os_attr)
# # print (Fighting.os_cw_name)
# # print (Fighting.os_cw_attr)
# print (Fighting.player_name)
# print (Fighting.player_attr)
# print (Fighting.player_cw_name)
# print (Fighting.player_cw_attr)



# c = Fighting(os_user=,
# #              os_cw=,
# #              player_user=,
# #              player_cw=)

# print (b.if_player())
# print (b.player_user_add_atrrtibute())   #玩家加成后的属性
# print (b.player_chongwu_add_attribute(4))    #玩家选择的宠物

# a.os_select_user()

# #   os_messages, os_chongwu, player_messages, player_chongwu
# os_messages = a.user_add_attribute()
# # print (os_messages )   #系统选出来的角色属性
#
#
# os_chongwu = a.chongwu_add_attribute()
# # print ( os_chongwu )    #宠物
# # # 玩家 角色的属性  混乱    待决定！！！！！！！！！！！！！
#
#
#
# player_messages = b.player_user_add_atrrtibute()
# # print (player_messages)   #玩家加成后的属性
#
# player_chongwu = b.player_chongwu_add_attribute(1)
# print (player_chongwu)   #玩家选择的宠物

# print ('```````````````````````````````````````````````````````````````')

# print (attribute.fengxi())
# print (attribute.notfengxi())
# print (attribute.chongwu())
#
# print ()
#
# print (attribute.fengxi())
# print (attribute.notfengxi())
# print (attribute.chongwu())






# print (os_user)    # 角色 属性 字典输出
# print(cw)      # 宠物 属性 字典输出




# print (os_user.values())
 # print (create_renwu.random_xianzu_menpai)
# print (os_user)

# print (os_auto_user.notfengxi_default_attribute)   #查看类属性值

# while True:
#        print("欢迎来到神武世界\n请先创建玩家角色名 再选择你的 种族 和 门派:\n")
#        # 用户选择状态
#        # 3种族
#        user_name = input("请创建您玩家角色名\n或者使用已创建过的的角色名: ")
#        if user_name != 'q':
#               if_user_name = read_user_messages.if_username(user_name)
#               while True:
#                      if if_user_name == 1:
#                             old_username = input("该用户已存在, 是否使用原先创建过的角色名登录? \n y:是  n:返回")
#                             if old_username == 'y':
#                                    tag = 1
#                             elif old_username == 'n':
#                                    break
#                             else:
#                                    print("输入错误，请重新输入！")
#                             # 游戏简介
#                             create_renwu.fen_xi()
#                             create_renwu.ren_zu()
#                             create_renwu.mo_zu()
#                             create_renwu.xian_zu()
#                             # 3种族
#                             if tag == 1:  # 将存在的玩家角色信息读出来
#                                    for k, v in read_user_messages.old_username(user_name).items():
#                                           old_remwu = k
#                                           old_menpai = v
#                                    # 返回了已存在玩家角色的信息 参数有 （角色名user_name 。种族old_remwu 。门派old_menpai）这里是第二个入口
#                                    print('系统将默认引用原先的玩家角色信息\n角色名:  %s\n种族  :  %s\n门派  :  %s' % (user_name,old_remwu,old_menpai))
#                      else:
#                             create_renwu.ren_wu()
#                             ren_wu = input("请输入你选择的 种族:  ").lower()
#                             if ren_wu == 'q':
#                                    break
#                             # 3门派
#                             zhong_zu = create_renwu.men_pai(ren_wu)
#                             while True:
#                                    if tag == 1:
#                                           print('创建用户成功, 等待 %s 玩家确认是否开启游戏!' % old_username)
#                                    else:
#                                           men_pai = input("请输入你选择的 门派:  ").lower()
#                                           if men_pai == 'q':
#                                                  break
#                                           mp_JG = create_renwu.menpai_JG(men_pai)
#                                           if mp_JG == 'error':
#                                                  break
#                                           user_JG = {zhong_zu: mp_JG}
#                                           print('您的选择是\n'
#                                                 '种族:  ' + zhong_zu + '\n'
#                                                                '门派:  ' + mp_JG + '\n')
#                                           with open('../conf/user_messages', 'a+') as fd_w:
#                                                  fd_w.write(user_name + '=' + str(user_JG) + '\n')
#                                                  print('创建用户成功, 等待 %s 玩家确认是否开启游戏!' % user_name)
#                                    status = input("开始游戏请输入: 'start' \n退出游戏请输入: 'exit'").lower()
#                                    if status == 'start':
#                                           #   传入接口参数  user_JG   zhong_zu  mp_JG  # 这里是第一个入口 开始游戏
#                                           a = Os_auto_user(num=create_renwu.os_num,
#                                                            select_zhongzu=create_renwu.random_zhongzu.get(
#                                                                create_renwu.os_num),
#                                                            zhongzu=create_renwu.random_zhongzu,
#                                                            renzu=create_renwu.random_renzu_menpai,
#                                                            mozu=create_renwu.random_mozu_menpai,
#                                                            xianzu=create_renwu.random_xianzu_menpai,
#                                                            fx=create_renwu.fx,
#                                                            not_fx=create_renwu.not_fx)
#
#                                           b = Player(user_name=user_JG,
#                                                      zhongzu=zhong_zu,
#                                                      renzu=mp_JG,
#                                                      fx=create_renwu.fx,
#                                                      not_fx=create_renwu.not_fx,
#                                                      num=create_renwu.os_num,
#                                                      mozu=create_renwu.random_mozu_menpai,
#                                                      xianzu=create_renwu.random_xianzu_menpai,
#                                                      select_zhongzu=create_renwu.random_zhongzu.get(create_renwu.os_num))
#
#                                           c = Fighting(os_messages=a.user_add_attribute(),
#                                                        os_chongwu=a.chongwu_add_attribute(),
#                                                        player_messages=b.player_user_add_atrrtibute(),
#                                                        player_chongwu=b.player_chongwu_add_attribute(1),
#                                                        player='hc')
#
#                                           while True:
#                                               c.start_attack()
#
#                                    elif status == 'exit':
#                                           sys.exit()
#                                    else:
#                                           print("输入错误, 请重新输入！")
#        elif user_name == 'q':
#               break
#        else:
#               print ("\n\n输入有误，请重新输入！ 退出请输入: 'q' ")









       # print (user_JG)

       # 判断输入的该用户是否存在

       # with open('user_messages') as fd_r:
       #     for i in fd_r:
       #         print (i),

       # 封印几率
       # random_int.fengyin(10)
# def attribute():
#     hp_f = random.randint(3600, 4001)
#     sd_f = random.randint(400, 501)
#     gj_f = random.randint(700, 801)
#     ll_f = random.randint(400, 500)
#     fy_f = random.randint(1000, 1201)
#     fengxi_default_attribute = {'FX': 20,
#                                 'HP': hp_f,
#                                 'MP': 2500,
#                                 'GJ': gj_f,
#                                 'FY': fy_f,
#                                 'LL': ll_f,
#                                 'SD': sd_f}  # 封系 默认的属性
#     hp = random.randint(3000, 3301)
#     gj = random.randint(900, 1001)
#     ll = random.randint(500, 601)
#     sd = random.randint(300, 400)
#     fy = random.randint(800, 901)
#     notfengxi_default_attribute = {'HP': hp,
#                                    'MP': 2000,
#                                    'GJ': gj,
#                                    'FY': fy,
#                                    'LL': ll,
#                                    'SD': sd}  # 输出系 默认属性
#     # 宠物普通属性
#     # 宠物属性  血量 2500~2700 攻击 700~730 防御 500~600 速度 280~295 灵力350~380
#     cw_hp = random.randint(2500, 2700)
#     cw_gj = random.randint(700, 750)
#     cw_ll = random.randint(350, 380)
#     cw_sd = random.randint(280, 295)
#     cw_fy = random.randint(700, 730)
#     chongwu_attribute = {'HP': cw_hp,
#                          'GJ': cw_gj,
#                          'FY': cw_fy,
#                          'SD': cw_sd,
#                          'LL': cw_ll}  # 宠物 默认属性