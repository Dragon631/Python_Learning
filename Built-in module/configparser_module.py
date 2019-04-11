#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser, os


conf = configparser.ConfigParser()
if os.path.exists('ini'):
    os.remove('ini')

conf.read('ini',encoding='utf8')

# 添加section
conf.add_section('db')

# 设置option的值
conf.set('db', 'db_host', 'localhost')
conf.set('db', 'db_port', '69')
conf.set('db', 'db_user', 'test')
conf.set('db', 'db_pass', 'test')

conf.add_section('concurrent')
conf.set('concurrent', 'thread', '10')
conf.set('concurrent', 'processor', '20')

# 写回文件的方式如下：（使用configparser的write方法）
# conf.write(open('ini','w'))

with open('ini', 'w') as configfile:
    conf.write(configfile)

"""
# 检查section是否存在，bool值
if not conf.has_section('default'):

    # 添加section
    conf.add_section('default')

# 检查option是否存在，bool值
if not conf.has_option('default', 'db_host'):

    # 添加option
    conf.set('default', 'db_host', '1.1.1.1')
conf.write(open('ini', 'w'))

# 删除section 和 option
conf.remove_section('default')
"""

# 获取所用的section节点
conf.read('ini', encoding='utf-8')
s = conf.sections()
print(s)

# 获取指定section 的options。即将配置文件某个section 内key 读取到列表中
k = conf.options('db')
print("The value of db section are:", k)

# 获取指点section下指点option的值
v = conf.get('db', 'db_host')  # 同conf['db']['db_host']
print(v)
# x = conf['db']['db_host']
# print(x)

# 获取指点section的所用配置信息
i = conf.items('db')
print(i)

# 修改某个option的值，如果不存在则创建
conf.set('db', 'db_port', '3308')

# conf.write(open('ini', 'w'))
with open('ini', 'w') as cf:
    conf.write(cf)

print(conf['db']['db_port'])