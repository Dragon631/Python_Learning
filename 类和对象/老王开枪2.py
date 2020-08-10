# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.gun = None

    def load_bullets(self, bullet_clip_tmp, bullet_tmp):
        bullet_clip_tmp.load_bullet(bullet_tmp)


    def load_bullet_clips(self, gun_tmp, bullet_clip_tmp):
        gun_tmp.load_bullet_clip(bullet_clip_tmp)


    def hold_gun(self, gun_tmp):
        self.gun = gun_tmp

    def shoot(self, enemy):
        self.gun.fire(enemy)

    def injure(self, sha_shang_li):
        self.hp -= sha_shang_li

    def __str__(self):
        if self.gun:
            return "%s, 能量：%d, 有把%s" % (self.name, self.hp, self.gun)
        else:
            if self.hp > 0:
                return "%s, 能量：%d" % (self.name, self.hp)
            else:
                return "%s 已挂！！" % (self.name)

class Gun(object):
    def __init__(self, name):
        self.name = name
        self.bullet_clip = None

    def load_bullet_clip(self, bullet_clip_tmp):
        self.bullet_clip = bullet_clip_tmp

    def fire(self, enemy):
        bullet_tmp = self.bullet_clip.pupup_bullet()
        if bullet_tmp:
            bullet_tmp.hit_enemy(enemy)
        else:
            return None

    def __str__(self):
        return "%s型号的枪" % (self.name)

class BulletClip(object):
    def __init__(self, max_num):
        self.max_num = max_num
        self.bullet_list = []

    def load_bullet(self, bullet_tmp):
        self.bullet_list.append(bullet_tmp)

    def pupup_bullet(self):
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None

    def __str__(self):
        if len(self.bullet_list) > 0:
            return "弹夹：%d/%d" % (len(self.bullet_list), self.max_num)
        else:
            return "弹夹没有子弹"


class Bullet(object):
    def __init__(self, sha_shang_li):
        self.sha_shang_li = sha_shang_li

    def hit_enemy(self, enemy):
        enemy.injure(self.sha_shang_li)


def main():

    laowang = Person("laowang")
    xiaochen = Person("xiaochen")

    ak47 = Gun("AK47")

    bullet_clip = BulletClip(20)

    for i in range(10):
        bullet = Bullet(10)
        laowang.load_bullets(bullet_clip, bullet)

    laowang.load_bullet_clips(ak47, bullet_clip)
    laowang.hold_gun(ak47)

    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)
    laowang.shoot(xiaochen)

    print(laowang)
    print(xiaochen)
    print(ak47)
    print(bullet_clip)


if __name__ == '__main__':

    main()

