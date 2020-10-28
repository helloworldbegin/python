import requests
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnlist(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])
    pass

def printInfo(ulist,num):
    tlpt="{0:^5}{1:{5}^15}{2:^5}{3:^5}{4:^5}"
    print(tlpt.format("序号","校名","位置","类别","分数",chr(12288)))
    for i in range(num):
        print(tlpt.format(ulist[i][0],ulist[i][1],\
            ulist[i][2],ulist[i][3],ulist[i][4],chr(12288)))

def main():
    url="http://zuihaodaxue.cn/zuihaodaxuepaiming2020.html"
    ulist=[]
    html=getHtmlText(url)
    fillUnlist(ulist,html)
    printInfo(ulist,10)

main()