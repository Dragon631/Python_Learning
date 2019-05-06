# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     老王开枪
   Description :
   Author :       a
   date:          2019/5/6
-------------------------------------------------
"""
class Person(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.gun = None  # 保存对枪的引用

    # 装弹夹，将弹夹装上枪杆子上
    def loading_bullet_clip(self, gun_tmp, bullet_clip_tmp):
        gun_tmp.load_clip(bullet_clip_tmp)

    # 装子弹，将子弹装进弹夹中
    def loading_bullet(self, bullet_clip_tmp, bullet_tmp):
        bullet_clip_tmp.load_bullet(bullet_tmp)

    # 拿枪，将枪的信息保存到拿枪人身上
    def hold_gun(self, gun_tmp):
        self.gun = gun_tmp

    # 开枪射击，枪开火
    def shoot(self, enemy):
        self.gun.fire(enemy)

    def injure(self, power_tmp):
        self.hp -= power_tmp

    def __str__(self):
        if self.gun:
            return "我是%s，我的生命值为：%s, 我有枪：%s" %(self.name, self.hp, self.gun)
        else:
            return "我是%s，我的生命值为：%s, 我没枪：%s" %(self.name, self.hp, self.gun)

class Gun(object):
    def __init__(self, name):
        self.name = name
        self.bullet_clip = None # 保存对弹夹的引用

    # 枪上弹夹，保存弹夹信息
    def load_clip(self, bullet_clip_tmp):
        self.bullet_clip = bullet_clip_tmp

    # 枪开火射击，发出一颗子弹
    def fire(self, enemy):
        bullet_tmp = self.bullet_clip.pop_up_bullet()
        if bullet_tmp:
            bullet_tmp.hit_enemy(enemy)
        else:
            print("弹夹没有子弹...")

    def __str__(self):
        return "枪支型号：%s" % self.name

class BulletClip(object):
    def __init__(self, max_num):
        self.max_num = max_num
        self.bullet_list = []  # # 保存子弹

    #  弹夹装子弹，保存在弹夹中的子弹列表中
    def load_bullet(self, bullet_tmp):
        if len(self.bullet_list) < self.max_num:
            return self.bullet_list.append(bullet_tmp)
        else:
            return self.bullet_list

    def pop_up_bullet(self):
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None

    def __str__(self):
        return "弹夹信息：%d/%d" % (len(self.bullet_list), self.max_num)

class Bullet(object):
    def __init__(self, power):
        self.power = power

    def hit_enemy(self, enemy):
        enemy.injure(self.power)

def main():
    # 创建老王
    laowang = Person("laowang")

    # 创建AK47
    ak47 = Gun("AK47")

    # 创建弹夹，子弹量
    bullet_clip = BulletClip(20)

    # 创建子弹，威力值 10
    bullet = Bullet(10)

    # 老王安装弹夹，将弹夹装(保存)到枪上
    laowang.loading_bullet_clip(ak47, bullet)

    # 老王装子弹，将子弹装到弹夹里
    laowang.loading_bullet(bullet_clip, bullet)

    # 老王拿枪
    laowang.hold_gun(ak47)

    # 创建敌人xiaoli
    xiaoli = Person("xiaoli")

    # 老王开枪，开枪打小李
    laowang.shoot(xiaoli)

    print(laowang)
    print(xiaoli)

    # print(bullet_clip)


if __name__ == "__main__":

    main()