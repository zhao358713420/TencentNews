#coding:utf-8
import pymysql
import requests

#连接数据库
db = pymysql.connect("localhost","root","stone","tencent_news")
cursor = db.cursor()

#从url_info中得到text_number
def getTextNumber():
    sql = "SELECT text_number FROM url_info;"
    cursor.execute(sql)
    resultes = cursor.fetchall()
    textNUmber = resultes[0][0]
    return textNUmber

#参数为第i个网页，返回该网址
def getUrl(i):
    sql = "SELECT url FROM all_url_test WHERE number = %d;"%i
    try:
        cursor.execute(sql)
        url = cursor.fetchall()[0][0]
    except Exception as identifier:
        print("查找第"+str(i)+"个网页失败")
    return url
#参数为网站url，返回该网站的url
def getText(url):
    reponse = requests.get(url)
    text = reponse.text
    return text
#参数为网站text和number，将该text存入/pageText中，以number.htm命名
def writeText(text,number):
    fo = open("./pageText/"+str(number)+".htm","w")
    flag = True
    try:
        fo.write(text)
    except IOError as identifier:
        print("写入:"+str(number)+"失败")
        flag = False
    return flag
#参数为number,url，将number,url,date存入get_text_url
def addGetTextUrl(number,url):
    flag = True
    sql = "INSERT INTO get_url_text VALUES(%d,'%s',CURDATE());"%(number,url)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as identifier:
        print("添加第"+str(number)+"条get_text_url失败")
        db.rollback()
        flag = False
    return flag
#无参数，将url_info中的text_number+1
def textNumberPlus():
    number = getTextNumber() + 1
    sql = "UPDATE url_info SET text_number = %d;"%number
    flag = True
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as identifier:
        print("text_number + 1 失败")
        db.rollback()
        flag = False
    return flag

def main():
    while True:
        textNumber = getTextNumber()
        print("-------------爬取第"+str(textNumber)+"页中---------------")
        url = getUrl(textNumber)
        print("url : "+url)
        text = getText(url)
        print("得到text")
        if not writeText(text,textNumber):
            print("写入错误："+str(textNumber))
            break
        print("写入"+str(textNumber)+".htm成功")
        addGetTextUrl(textNumber,url)
        print("get_url_text添加成功")
        textNumberPlus()
        print("text_number添加成功")
        print("-------------爬取第"+str(textNumber)+"页成功---------------\n")
        if textNumber > 1000:
            break
    db.close()

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))