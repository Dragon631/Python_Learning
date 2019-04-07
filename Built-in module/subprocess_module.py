#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

# cmd = 'netstat -an'
cmd = 'ipconfig /all'
result_call = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE)
# 成功获取输出内容， 但数据类型是bytes，需要进行decode，windows的默认编码为GBK
# 将返回值进行decode
result = result_call.stdout.read().decode('gbk')
print(result)

