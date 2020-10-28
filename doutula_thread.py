import requests
import time
from threading import Thread
from bs4 import BeautifulSoup


ua = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/86.0.4240.42 Safari/537.36 Edg/86.0.622.19'}


def getHtmlText(url, encoding = 'utf-8'):
    try:
        r = requests.get(url, headers = ua)
        r.raise_for_status()
        return r.text
    except:
        return 'Error'


def getPicContent(url):
    try:
        r = requests.get(url, headers = ua)
        r.raise_for_status()
        return r.content
    except:
        return 'Error'
        

def getPicList(url, pic_list):
    html = getHtmlText(url)
    soup = BeautifulSoup(html, "html.parser")
    divtag = soup.find("div", attrs = {"class":"page-content text-center"})
    imgtag = divtag.findAll("img")
    for i in imgtag:
        # print(i.attrs['alt'])
        # print(i.attrs['data-original'])
        pic_list.append([len(pic_list) + 1, i.attrs['alt'], i.attrs['data-original']])


def dlPic(pic_list):
    # print(pic_list)
    while len(pic_list) > 0:
        pic_info = pic_list.pop()

        pic_index = pic_info[0]
        pic_name = pic_info[1]
        pic_url = pic_info[2]

        # print(pic_name, pic_url)
        img = getPicContent(pic_url)
        try:
            f = open('c:/tmp/doutula/{}.{}'.format(pic_name, pic_url.split('.')[-1]), 'wb')
        except:
            f = open('c:/tmp/doutula/{}.{}'.format(pic_name.replace('/','**slash**'), pic_url.split('.')[-1]), 'wb')
        f.write(img)
        f.close()

    # f = open('c:/tmp/doutula/{}'.format(pic_name))

def main():
    url = 'https://www.doutula.com/photo/list/'
    pic_list = list()
    get_pic_list_thread = Thread(target = getPicList, args = (url, pic_list))
    dl_pic_thread = Thread(target = dlPic, args = (pic_list,))

    get_pic_list_thread.start()
    time.sleep(5)
    dl_pic_thread.start()

    # get_pic_list_thread.join()
    # dl_pic_thread.join()

if __name__ == "__main__":
    main()