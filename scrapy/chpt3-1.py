# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     chpt3-1
   Description :
   Author :       a
   date:          2020/4/26
-------------------------------------------------
"""

import re
import random
import datetime

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError

pages = set()
random.seed(datetime.datetime.now())


# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl) :
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")) :
        if link.attrs['href'] is not None :
            if link.attrs['href'] not in internalLinks :
                internalLinks.append(link.attrs['href'])
    return internalLinks


# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl) :
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, features="html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0 :
        internalLinks = getInternalLinks(bsObj, startingPage)
        if len(internalLinks) == 0:
            print("InternalUrl is out.")
        # return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
        else:
            return internalLinks[random.randint(0, len(internalLinks) - 1)]
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    try :
        externalLink = getRandomExternalLink(startingSite)
        print("随机外链是：" + externalLink)
    #externalLink = getRandomExternalLink("https://www.wanweibaike.com")
    except URLError as e:
        print("打开链接出错：%s" %e)
    else:
        followExternalOnly(externalLink)


followExternalOnly("https://www.wanweibaike.com")
# followExternalOnly("https://baike.baidu.com")
# followExternalOnly("https://www.espn.com/")

