# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     mysql_ops
   Description :
   Author :       a
   date:          2019/4/3
-------------------------------------------------
"""
__author__ = 'a'

import pymysql.cursors
import types

# 连接数据库

connect = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "cGnfs@2018.",
    database = "mysql"
    )

cursor = connect.cursor()
# 创建user表
# cursor.execute("drop table if exist user")
# sql = """CREATE TABLES IF NOT EXISTS `user` (
#     `id` int(11) NOT NULL AUTO_INCREMENT,
#     `name` varchar(255) NOT NULL,
#     `age` int(11) NOT NULL,
#     PRIMARY KEY(`id`)
#     ) ENGINE=InnoDB DEFAULT CHARSET=uft8 AUTO_INCREMENT=0"""

tables = cursor.execute("show create table user")
# columns = cursor.execute("show columns from user")

tbs = list(cursor.fetchall())
print(tbs)