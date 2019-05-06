# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     loawang_shot
   Description :
   Author :       a
   date:          2019/5/6
-------------------------------------------------
"""

"""
shoot - 开枪
gun - 枪
bullet - 子弹
bullet_clip - 子弹夹
enemy - 敌人
lethality - 杀伤力
"""


class Person(object):
    def __init__(self, name):
        self.name = name
        self.gun = None
        self.hp = 100

    # 装子弹 - 将子弹装弹夹里
    def loading_clips(self, bullet_clips_tmp, bullet_tmp):
        bullet_clips_tmp.loading_bullets(bullet_tmp)

    # 装弹夹 - 将弹夹装枪上
    def loading_guns(self, gun_tmp, bullet_clips_tmp):
        gun_tmp.loading_bullet_clip(bullet_clips_tmp)

    # 拿枪
    def hold_gun(self, gun_tmp):
        self.gun = gun_tmp

    # 开枪打敌人
    def shoot(self, enemy):
        self.gun.fire(enemy)

    def injure(self, lethality):
        if self.hp > 0 :
            self.hp -= lethality
        else:
            return "Game Over..."

    def __str__(self):
        if self.gun:
            return "%s生命值为%d, 有枪..." % (self.name, self.hp)
        else:
            if self.hp > 0:
                return "%s生命值为%d，没枪..." % (self.name, self.hp)
            else:
                return "%s已经Game Over!!!" % (self.name)



class Gun(object):
    def __init__(self, name):
        self.name = name
        self.bullet_clip = None

    def loading_bullet_clip(self, bullet_clips_tmp):
        self.bullet_clip = bullet_clips_tmp

    # 开火，取出一颗子弹
    def fire(self, enemy):
        bullet_tmp = self.bullet_clip.pop_up_bullet()
        if bullet_tmp:
            bullet_tmp.hit_enemy(enemy)  # 击中敌人
        else:
            return None

    def __str__(self):
        return "枪的信息：%s , %s" % (self.name, self.bullet_clip)


class BulletClip(object):
    def __init__(self, max_val):
        self.max_val = max_val
        self.bullet = []

    def loading_bullets(self, bullet_tmp):
        """将子弹装进弹夹里"""
        if len(self.bullet) < self.max_val:
            self.bullet.append(bullet_tmp)
        else:
            return self.bullet

    def pop_up_bullet(self):
        if self.bullet:
            return self.bullet.pop()
        else:
            return None

    def __str__(self):
        return "弹夹：%s/%s" % (len(self.bullet), self.max_val)


class Bullet(object):
    def __init__(self, lethality):
        self.lethality = lethality

    def hit_enemy(self, enemy):
        enemy.injure(self.lethality)

def main():
    """创建老王"""
    loawang = Person("loawang")

    """创建一把AK47"""
    ak47 = Gun("AK47")

    """创建一个子弹夹，最多20个"""
    bullet_clips = BulletClip(20)

    """创建一些子弹，杀伤力为10"""
    for i in range(10):
        bullet = Bullet(10)

        """老王将子弹装进弹夹里"""
        loawang.loading_clips(bullet_clips, bullet)

    """老王将弹夹装枪上"""
    loawang.loading_guns(ak47, bullet_clips)

    """老王拿枪"""
    loawang.hold_gun(ak47)

    """创建一个敌人小李"""
    xiaozhang = Person("xiaozhang")

    """老王开枪"""
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)
    loawang.shoot(xiaozhang)

    print(loawang, ak47)
    print(xiaozhang)


if __name__ == "__main__":
    main()

