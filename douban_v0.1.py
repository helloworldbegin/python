import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import perf_counter
import random
from getProxyIp import readFromFile

user_agent = [
    {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/85.0.4183.69 Safari/537.36 Edg/85.0.564.36"
    },
    {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    },
    {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
    },
]
proxy_ip_list = [
    "202.109.157.65:9000",
    "125.110.109.1:9000",
    "125.108.91.220:9000",
    "123.163.118.136:9999",
    "121.237.107.132:3000",
    "123.149.141.80:9999",
    "171.35.171.245:9999",
    "123.163.121.19:9999",
    "125.108.120.2:9000",
    "163.204.94.173:9999",
    "123.101.207.246:9999",
    "125.108.90.88:9000",
    "120.83.106.173:9999",
    "115.210.31.222:9000",
    "123.163.121.217:9999",
]

website = "https://book.douban.com/tag/"
category = "神经网络"


def getProxyIpHtmlText(url):
    ua = user_agent[1]
    try:
        r = requests.get(url, headers=ua)
        r.raise_for_status
        return r.text
    except:
        return ""


def getProxyIp(url):
    html = getProxyIpHtmlText(url)
    soup = BeautifulSoup(html, "html.parser")
    tbody = soup.find("tbody")
    trtag = tbody.find_all("tr")
    proxy_ip_list = []
    for i in trtag:
        proxy_ip_list.append(i.td.string + ":" + i.td.nextSibling.nextSibling.string)
    return proxy_ip_list


def getHtmlText(url, proxy_ip_list, encoding="utf-8"):
    ua = random.choice(user_agent)
    proxy_ip = random.choice(proxy_ip_list)
    try:
        r = requests.get(url, proxies={"http": proxy_ip}, headers=ua)
        r.raise_for_status
        r.encoding = encoding
        print(ua, proxy_ip)
        return r.text
    except:
        return "Error"


def getBookUrlList(book_url_list, url, proxy_ip_list):
    try:
        html = getHtmlText(url, proxy_ip_list)
        print(html[:100])
        soup = BeautifulSoup(html, "html.parser")
        atag = soup.findAll("a", attrs={"class": "nbg"})
        book_count = len(book_url_list)
        for i in atag:
            a = i.parent.nextSibling.nextSibling.a
            book_url_list.append([book_count + 1, a.attrs["title"], a.attrs["href"]])
            book_count = book_count + 1
        return book_url_list
    except:
        return


"""
在book_url_list中直接添加intro
"""


def getBookIntro(book_url_list, proxy_ip_list):
    for i in book_url_list:
        try:
            print(i[0], i[1])
            html = getHtmlText(i[2], proxy_ip_list)
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
            i.append('=HYPERLINK("{}","{}")'.format(i[3],i[1]))
        except:
            i.insert(2, None)
            continue


def writeToFile(fpath, content):
    f = open(fpath, "wt", encoding="utf-8")
    for i in content:
        f.write(",".join(i) + "\n")
    f.close()
    pass


def main():
    url = website + category
    book_url_list = []
    # kdlurl = "https://www.kuaidaili.com/free/"
    # proxy_ip_list=getProxyIp(kdlurl)
    # print(proxy_ip_list)
    proxy_ip_list=readFromFile("c:/tmp/proxy_ip_list.txt")
    print(proxy_ip_list)
    begin = perf_counter()
    page = 1
    for i in range(page):
        url = website + category + "/?start=" + str(i * 20) + "&type=T"
        book_url_list = getBookUrlList(book_url_list, url, proxy_ip_list)
    dur = perf_counter() - begin
    print("获取书籍名称和URL用时：{:.2f}秒".format(dur))
    intro_begin = perf_counter()

    getBookIntro(book_url_list, proxy_ip_list)

    dur = perf_counter() - intro_begin
    print("获取书籍信息用时:{:.2f}秒，平均每本书用时{:.2f}秒".format(dur, dur / len(book_url_list)))

    begin_write = perf_counter()

    df = pd.DataFrame(book_url_list, columns=["Index", "Name", "Intro", "Url","HyperLink"])
    df.set_index("Index", inplace=True)
    df.to_excel(
        "c:/tmp/豆瓣-{}.xlsx".format(category), sheet_name="豆瓣-{}".format(category)
    )

    dur = perf_counter() - begin_write
    print("处理和写入文件用时：{:.2f}秒".format(dur))


main()
