#########################
# Pyton version : 3.4
# BeautifulSoup version : 4
# Made By : Jang JI SU
# Date : 2016-08-23
# -*- coding:UTF-8 -*-
########################

try:
# For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
# Fall back to Python 2's urllib2
    from urllib2 import urlopen

from bs4 import BeautifulSoup

class cparser:


    def __init__(self,url,tag,attr): # 파싱할 url, 태그, 속성 초기화
        self.url = url
        self.tag = tag
        self.attr = attr

    def getTags(self): #태그 파싱
        try:
            html = urlopen(self.url)
            soup = BeautifulSoup(html,"html.parser")
            return soup.find_all(self.tag)
        except:
            print("exception error")
            exit()

    def getAttrs(self,arr): #원하는 속성 파싱후 중복제거한 리스트 리턴
        arrAttr = []
        for attr in arr :
            arrAttr.append(attr[self.attr])
        arrAttr = list(set(arrAttr))
        return arrAttr

    def getPatternAttrs(self,arr,*args): # 원하는 속성 패턴검색해서 파싱후 중복제거한 리스트 리턴
        argsSize = len(args)
        import re
        arrAttr = []
        for attr in arr:
            for i in args:
                if re.match(i,attr[self.attr]):
                    arrAttr.append(attr[self.attr])
        arrAttr = list(set(arrAttr))
        return arrAttr

    def setUrl(self,url):
        self.url = url

    def setAttr(self,attr):
        self.attr = attr

    def setTag(self,tag):
        self.tag = tag


if __name__ == "__main__":
    parse = cparser("http://220.86.25.65:9999","a","href")
    tags = []
    attrs = []
    temp = []
    tags = parse.getTags()
    temp = tags
    attrs = parse.getPatternAttrs(tags,"[/]","[./]","[../]","[ ]")
    temp = attrs
    print(temp)
