#coding:utf-8
import pymysql

# global db 
db = pymysql.connect("localhost","root","stone","tencent_news")
# global cursor 
cursor = db.cursor()
#参数为网址，通过SQL语法，查询该url是否在all_url表中,存在则返回number
# def getAllUrlNumber(url):
#     sql = "SELECT number FROM tencent_news.all_url WHERE url = '%s';"%url
#     number = -1
#     try:
#         # global cursor
#         cursor.execute(sql)
#         number = cursor.fetchall()[0][0]
#         # db.commit()
#     except Exception:
#         print("失败："+sql)
#         print(Exception.__context__)
#         # global db
#         # db.rollback()
#     # number = cursor.execute(sql)
#     #     cursor.commit()
#     return number
#参数为网址，通过SQL语法，查询该url是否在all_url表中,存在则返回number
def getAllUrlNumber(url):
    sql = "SELECT number FROM all_url WHERE url = 'http://news.qq.com/a/20131025/009002.htm';"
    number = -1
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            number = results[0][0]
        # cursor.commit()
    except Exception:
        print(len(results))
        print("失败："+sql)
        # database.rollback()
    return number
def main():
    #连接数据库
    print(getAllUrlNumber("http://news.qq.com"))
    db.close()
    


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0)) 