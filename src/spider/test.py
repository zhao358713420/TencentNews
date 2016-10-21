#coding:utf-8

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
#得到allUrlList，测试其重复率
def getCover():
    allUrlList = getAllURL()
    firstLength = len(allUrlList)
    newList = list(set(allUrlList))
    newList.sort(key=allUrlList.index)
    secondLength = len(newList)
    return firstLength-secondLength
def main():
    print(getCover())

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))