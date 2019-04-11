# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     hashlib_module
   Description :
   Author :       a
   date:          2019/4/2
-------------------------------------------------
"""
__author__ = 'a'

import hashlib

# 加密字符串
str = "Hello_world1"
str2 = "大家好！我是中国人。"

# md5加密字符串，不安全
hashMd5 = hashlib.md5(str)
print(hashMd5)
# hexdigest() 转十六进制
result = hashMd5.hexdigest()
print(result)

# sha1加密字符串，不安全，可通过枚举法暴力破解
hashSha1 = hashlib.sha1(str)
print(hashSha1)
# hexdigest() 转十六进制
result = hashSha1.hexdigest()
print(result)

# sha256加密字符串，较安全，难破解
hashSha256 = hashlib.sha256(str)
print(hashSha256)
# hexdigest() 转十六进制
result = hashSha256.hexdigest()
print(result)

#另一种传值方法
hash = hashlib.sha256() # 括号内也可以传值，类型要求是bytes类型
hash.update(str2)
print(hash.hexdigest())

