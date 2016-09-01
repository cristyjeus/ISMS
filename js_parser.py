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


    def __init__(self,url,tag,attr,baseUrl): # 파싱할 url, 태그, 속성 초기화
        self.url = url
        self.tag = tag
        self.attr = attr
        self.baseUrl = baseUrl

    def getTags(self): #태그 파싱
        try:
            html = urlopen(self.url)
            soup = BeautifulSoup(html,"html.parser")
            return soup.find_all(self.tag)
        except:
            print("exception error : " + self.url)
            #exit()
            return False

    def getAttrs(self,arr): #원하는 속성 파싱후 중복제거한 리스트 리턴
        arrAttr = []
        for attr in arr :
            tmp=replaceType(replaceType(attr[self.attr],"?",None,"remove"))
            arrAttr.append(attr)
        arrAttr = list(set(arrAttr))
        return arrAttr

    def checkUrl(self): #디렉토리 접근후 상대경로 체크
        chking = self.url[len(self.baseUrl):self.url.rfind("/")]
        if chking != "" and chking != "/":
            #print(chking+" : chking : " +self.url)
            return chking
        return False

    def getPatternAttrs(self,arr,*args): # 원하는 속성 패턴검색해서 파싱후 중복제거한 리스트 리턴 패턴은 원하는 만큼 설정 가능
        argsSize = len(args)
        import re
        arrAttr = []
        for i in args: #속성 검사 시작
            for attr in arr:
                if re.match(i,attr[self.attr]):
                    temp = attr[self.attr]

                    if self.checkUrl() !=False and attr[self.attr][:1] == ".":
                        #tmp = self.replaceType(attr[self.attr],"?",None,"remove") #?뒤 제거
                        temp = self.checkUrl() + self.replaceType(attr[self.attr],".","/","replace")
                        #print(temp+"pt")

                    arrAttr.append(temp)
        #arrAttr.sort()
        arrAttr = list(set(arrAttr))
        return arrAttr

    def setUrl(self,url):
        self.url = url

    def setAttr(self,attr):
        self.attr = attr

    def setTag(self,tag):
        self.tag = tag

    def replaceType(self, attr, search, replace, option):# .(dot) remove function
        if option=="replace":
            if attr[0:1]==".":
                attr = attr.replace("./","/")
        if option=="remove":
            if attr.find(search):
                attr = attr[0:attr.rfind(search)]
        return attr

    #def searchAll(self,):


if __name__ == "__main__":
    counter = 0 # 검사한 url 갯수
    checkedUrl = [] # 체크 완료한 url
    tags = [] #뽑아낸 태그들
    attrs = [] # 뽑아낸 속성들
    temp = [] #임시 저장소
    url = "http://220.86.25.65:9999"
    result = 0 #
    count = 3
    #print(len(url)) 테스트 url 길이 24

    while result < count:
        attr = "/main.asp"
        if 0 < len(attrs):
            attr = temp[result]
        #print(attr)
        if attr[0:1]==".":
            attr = attr.replace("./","/")

        parse = cparser(url+attr,"a","href",url)
        #print(attr)
        if (parse.getTags()):
            tags = parse.getTags()
            attrs = parse.getPatternAttrs(tags,"[/]","[./]","[../]","[ ]")
            temp = attrs+temp
            temp = list(set(temp))
            print("temp : " , temp)
            result = result+1
            count = len(temp)
