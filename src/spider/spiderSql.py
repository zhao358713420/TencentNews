#!/usr/bin/python3
#coding:utf-8
import requests
import re
import pymysql

#连接数据库
db = pymysql.connect("localhost","root","stone","tencent_news")
cursor = db.cursor()
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

#参数为网址，通过SQL语法，查询该url是否在all_url表中,存在则返回number
def getAllUrlNumber(url):
    sql = "SELECT number FROM all_url WHERE url = '%s';"%url
    number = -1
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            number = results[0][0]
        # cursor.commit()
    except Exception:
        print("失败："+sql)
        # database.rollback()
    return number
#得到all_url表中最后一个number
def getMaxNumber():
    sql = "SELECT MAX(number) FROM all_url;"
    cursor.execute(sql)
    number = cursor.fetchall()[0][0]
    return number
#参数为网址，通过sql语法，将该url插入all_url表中，成功返回number
def addUrlToAllUrl(url):
    sql = "INSERT INTO all_url(number,url,date) VALUES (%d,'%s',CURDATE());"%(getMaxNumber() + 1,url)
    number = getMaxNumber() + 1
    try:
        cursor.execute(sql)
        db.commit()
    except Exception:
        print("失败："+sql)
        number = -1
        db.rollback()
    return number

#参数为第i个网页，返回该网址
def getUrl(i):
    sql = "SELECT url FROM all_url WHERE number = %d;"%i
    try:
        cursor.execute(sql)
        url = cursor.fetchall()[0][0]
    except Exception as identifier:
        print("查找第"+str(i)+"个网页失败")
    return url
def main():
    i = 2045
    count = getMaxNumber()
    while True:
        print("正在爬取第"+str(i)+"页中url")
        homePageUrl = getUrl(i)
        text = getURLText(homePageUrl)
        pageUrlList = getPageURL(text)
        pageCount = 0
        for url in pageUrlList:
            if getAllUrlNumber(url) <= 0:
                count += 1
                pageCount += 1
                addUrlToAllUrl(url)
        print("爬取到"+str(pageCount)+"个URL")
        print("共爬取到"+str(count)+"个URL")
        i += 1
    print("爬取完成，共爬到"+str(count)+"条url")


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
