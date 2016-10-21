#!/usr/bin/python3
#coding:utf-8
import requests
import re

#参数为网站URL，通过get得到网页的response，然后返回response.text
def getURLText(homePageURL):
    homePageResponse = requests.get(homePageURL)
    homePageText = homePageResponse.text
    return homePageText

#参数为网页的text，通过正则表达式，得到新闻类URL的List，返回该list
def getPageURL(homePageText):
    URLList = []
    #通过正则表达式，将符合格式的URL放入findallList
    reString = r"http://news\.qq\.com/a/.*?\.htm"
    pattern = re.compile(reString,re.I)
    findallLiat = pattern.findall(homePageText)
    #将URL去重，并存入URLList
    for url in findallLiat:
        if url not in URLList:
            URLList.append(url)
    return URLList

#无参数，返回allURL文件中URL的List
def getAllURL():
    try:
        fo = open("./URL/allURL.txt","r")
    except IOError:
        print("getAllurl中allURL.txt打开错误")
        return
    allURLList = fo.readlines()
    # print(allURLList)
    for num in range(0,len(allURLList)):
        allURLList[num] = allURLList[num].strip('\n')
    fo.close()
    return allURLList

#参数为网站地址，将地址加入allURL.txt,返回True或False
def writeAllURL(url):
    try:
        fo = open("./URL/allURL.txt","a")
    except IOError as identifier:
        print("writeAllUrl中allURL.txt打开错误")
        return False
    fo.write(url)
    fo.close()
    return True



def main():
    i = 655
    count = 0
    while True:
        print("正在爬取第"+str(i)+"页中url")
        allUrlList = getAllURL()
        homePageUrl = allUrlList[i]
        text = getURLText(homePageUrl)
        pageUrlList = getPageURL(text)
        pageCount = 0
        for url in pageUrlList:
            if url not in allUrlList:
                count += 1
                pageCount += 1
                writeAllURL(url+"\n")
        print("爬取到"+str(pageCount)+"个URL")
        print("共爬取到"+str(count)+"个URL")
        i += 1
    print("爬取完成，共爬到"+str(count)+"条url")


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
