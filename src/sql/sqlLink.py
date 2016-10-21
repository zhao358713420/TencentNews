#coding:utf-8
import pymysql

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

def main():
    #连接数据库
    db = pymysql.connect("localhost","root","stone","tencent_news")
    cursor = db.cursor()
    urlList = getAllURL()
    for i in range(0,len(urlList)):
        urlList[i] = urlList[i].strip('\n')
        sql = "INSERT INTO all_url(number,url,date) VALUES (%d,'%s',CURDATE());"%(i,urlList[i])
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            print("失败")
            db.rollback()
        print(str(i)+"成功："+sql)
    db.close()
    


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0)) 