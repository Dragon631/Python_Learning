# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     login_test
   Description :
   Author :       a
   date:          2019/4/3
-------------------------------------------------
"""
import json

# json_str = {"apple": "123", "Banana": "456", "Cat": "789"}
# json_file = open('userinfo.txt','wb')
# json.dump(json_str,json_file)
# json_file.close()

json_file = open('userinfo.txt','rb')
with open('DATA','rb') as f:
    data = json.load(f)
print(type(data))
print(data['apple'])

