#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import logging

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

log = logging.critical("%s This is a message..." %(date))
print(log)