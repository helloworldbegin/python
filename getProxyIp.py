import requests
from bs4 import BeautifulSoup
from random import choice

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
ua = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/85.0.4183.69 Safari/537.36 Edg/85.0.564.36"
}

website = "https://www.kuaidaili.com/free/"

fpath = "c:/tmp/proxy_ip_list.txt"


def getHtmlText(url):
    ua=choice(user_agent)
    try:
        r = requests.get(url, headers=ua)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def addIp(proxy_ip_list, html):
    soup = BeautifulSoup(html, "html.parser")
    tbody = soup.find("tbody")
    trtag = tbody.find_all("tr")
    for i in trtag:
        proxy_ip_list.append(i.td.string + ":" + i.td.nextSibling.nextSibling.string)


def uniqIp(proxy_ip_list):
    uniq_proxy_ip_set = set(proxy_ip_list)
    proxy_ip_list = list(uniq_proxy_ip_set)


def main():
    proxy_ip_list = readFromFile(fpath)
    html = getHtmlText(website)
    addIp(proxy_ip_list, html)
    uniqIp(proxy_ip_list)

    cnt=1
    for i in proxy_ip_list:
        if checkIp(i, "https://book.douban.com"):
            print("{}:{}".format(cnt,i))
        else:
            print("{}:{}".format(cnt,i),end=";")
            print("remove ip {}".format(i))
            proxy_ip_list.remove(i)
        cnt=cnt+1

    f = open(fpath, "wt", encoding="utf-8")
    cnt=1
    for i in proxy_ip_list:
        f.write(i + "\n")
        print("{}: {}".format(cnt,i))
        cnt=cnt+1
    f.close()


def checkIp(ip, target_site):
    ua=choice(user_agent)
    r = requests.head(target_site, headers=ua, proxies={"http": ip})
    if r.status_code == 200:
        print(
            "request {} status code: {} ".format(r.request.url, r.status_code),
            "proxy {} OK!".format(ip),
        )
        return True
    else:
        print(r.status_code)
        return False


def readFromFile(fpath):
    proxy_ip_list = []
    f = open(fpath)
    for line in f:
        proxy_ip_list.append(line.strip("\n"))
    f.close()
    return proxy_ip_list


main()
