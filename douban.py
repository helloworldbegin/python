import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import perf_counter

ua = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/85.0.4183.69 Safari/537.36 Edg/85.0.564.36"
}

website = "https://book.douban.com/tag/"
category = "名著"


def getHtmlText(url, encoding="utf-8"):
    try:
        r = requests.get(url, headers=ua)
        r.raise_for_status
        r.encoding = encoding
        return r.text
    except:
        return "Error"


def getBookUrlList(book_url_list, url):
    html = getHtmlText(url)
    print(html[:100])
    soup = BeautifulSoup(html, "html.parser")
    atag = soup.findAll("a", attrs={"class": "nbg"})
    book_count = len(book_url_list)
    for i in atag:
        a = i.parent.nextSibling.nextSibling.a
        book_url_list.append([book_count + 1, a.attrs["title"], a.attrs["href"]])
        book_count = book_count + 1
    return book_url_list


"""在book_url_list中直接添加intro"""


def getBookIntro(book_url_list):
    # cnt = 0
    for i in book_url_list:
        print(i[0], i[1])
        html = getHtmlText(i[2])
        soup = BeautifulSoup(html, "html.parser")
        divtag = soup.find("div", attrs={"class": "intro"})
        if divtag.a != None:
            divtag = divtag.parent.nextSibling.nextSibling.div
        p = divtag.p
        string = p.string
        p = p.nextSibling
        while p != None and p.string:
            string = string + p.string
            p = p.nextSibling
        i.insert(2, string)
        # cnt += 1


def writeToFile(fpath, content):
    f = open(fpath, "wt", encoding="utf-8")
    for i in content:
        f.write(",".join(i) + "\n")
    f.close()
    pass


def main():
    url = website + category
    book_url_list = []
    book_info_list = []
    # book_url_list=getBookUrlList(book_url_list,url)
    # for i in book_url_list:
    #     name=i[0]
    #     book_url=i[1]
    #     book_info=[]
    #     book_info=getBookInfo(book_info,i[1])
    #     book_info.insert(0,name)
    #     book_info.append(book_url)
    #     book_info_list.append(book_info)
    # writeToFile("c:/tmp/doubanbook.csv",book_info_list)
    begin = perf_counter()
    page = 1
    for i in range(page):
        url = website + category + "/?start=" + str(i * 20) + "&type=T"
        # print(url)
        book_url_list = getBookUrlList(book_url_list, url)
    # print(book_url_list)
    dur = perf_counter() - begin
    print("获取书籍名称和URL用时：{:.2f}秒".format(dur))
    intro_begin = perf_counter()
    getBookIntro(book_url_list)
    dur = perf_counter() - intro_begin
    print("获取书籍信息用时:{:.2f}秒，平均每本书用时{:.2f}秒".format(dur,dur/len(book_url_list)))
    # print(book_url_list)
    # f=open("c:/tmp/doubanbookfive.txt","wt",encoding="utf-8")
    # for i in book_info_list:
    #     print(len(i))
    #     f.write(str(i)+"\n")
    # f.close()
    # for i in range(len(book_url_list)):
    #     index=['name','url']
    #     item=pd.Series(i,index=index)
    #     df=pd.DataFrame(columns=['name','url'])
    #     df.append(item)
    #     #print(item)
    # index = range(1, len(book_url_list) + 1)
    begin_write = perf_counter()
    df = pd.DataFrame(book_url_list, columns=["Index", "Name", "Intro", "Url"])
    df.set_index("Index", inplace=True)
    df.to_excel("c:/tmp/豆瓣-{}.xlsx".format(category))
    dur = perf_counter() - begin_write
    print("处理和写入文件用时：{:.2f}秒".format(dur))


main()
