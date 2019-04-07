#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json


"""
JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。
JSON的数据格式其实就是python里面的字典格式，里面可以包含方括号括起来的数组，也就是python里面的列表
"""

str = 'Hello World!'
li = [11, 22, 33, 44]
dic = {
    'name':'April',
    'info':['a', 'b', 'c', 'd'],
    'age': 33
}
tup = (1, 2, 3 ,4)

"""
dumps 和 dump 序列化方法
dumps 只完成了序列化为str，可以格式化所有的基本数据类型为字符串
dump 必须传文件描述符，将序列化的str保存到文件中
"""
str_jdp = json.dumps(str)
li_jdp = json.dumps(li)
dic_jdp = json.dumps(dic)
tup_jdp = json.dumps(tup)

print('*'*50)
print("\033[32;1mstring to json.dumps\033[0m %s \033[32;1m \ntype:\033[0m %s" %(str_jdp,type(str_jdp)))
print('*'*50)
print("\033[32;1mlist to json.dumps\033[0m %s \033[32;1m \ntype:\033[0m %s" %(li_jdp,type(str_jdp)))
print('*'*50)
print("\033[32;1mdict to json.dumps\033[0m %s \033[32;1m \ntype:\033[0m %s" %(dic_jdp,type(str_jdp)))
print('*'*50)
print("\033[32;1mtuple to json.dumps\033[0m %s \033[32;1m \ntype:\033[0m %s" %(tup_jdp,type(str_jdp)))
print('*'*50)

with open("test.json", "w", encoding='utf-8') as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
    f.write(json.dumps(dic, indent=4))
    # json.dump(a,f,indent=4)   # 和上面的效果一样

lstr = ["a", "b", "c", "d"]
fw = open('test1.json', 'w')
json.dump(lstr, fw)
fw.close()

fw = open('test1.json', 'r')
fd = json.load(fw)
fw.close()
print("\033[31;5mlist to json.dumps\033[0m %s \033[31;5m \ntype:\033[0m %s" %(fd,type(fd)))

"""
loads 和 load  反序列化方法
loads 只完成了反序列化
load 只接收文件描述符，完成了读取文件和反序列化，将包含str类型的JSON文档反序列化为一个python对象
记忆：load/loads 将文件中的 ' 去掉，将 " 变成 '
"""
dic_str = '{ "name": "April", "info": ["a", "b", "c", "d"], "age": 33 }'
jdata = json.loads(dic_str, encoding='utf-8')
print("\033[32;1mPython obj:\033[0m %s " %jdata)
print("\033[32;1mType:\033[0m", type(jdata))

with open('test.json', 'r', encoding='utf-8') as f:
    jdata = json.loads(f.read())
    print(jdata)
    # f.seek(0) # offset -- 开始的偏移量，无返回值
    # jdata1 = json.load(f)  # 等效于 json.loads(f.read())
    # print(jdata1)

with open('test.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)  # 等效于 json.loads(f.read())
    print(jdata)