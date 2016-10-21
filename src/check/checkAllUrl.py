#!/usr/bin/python3
#coding:utf-8
import requests
import re
import pymysql

#连接数据库
db = pymysql.connect("localhost","root","stone","tencent_news")
cursor = db.cursor()

#得到all_url_test的list
def getAllUrlList():
    sql = "SELECT url FROM all_url_test WHERE number > -1;"
    cursor.execute(sql)
    results = cursor.fetchall()
    urlList = []
    for row in results:
        urlList.append(row[0])
    return urlList
#参数为list，返回重复元素的个数
def getRepeat(urlList):
    length1 = len(urlList)
    newList = list(set(urlList))
    newList.sort(key=urlList.index)
    length2 = len(newList)
    return length1 - length2

def main():
    print(getRepeat(getAllUrlList()))


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
