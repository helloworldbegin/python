import requests
import time
from threading import Thread
from bs4 import BeautifulSoup


class Queue:
    def __init__(self):
        self.data = list()

    def isEmpty(self):
        return self.data == []

    def size(self):
        return len(self.data)

    def put(self, item):
        self.data.append(item)

    def get(self):
        if self.size() > 0:
            return self.data.pop(0)
        else:
            return None

    def last(self):
        if self.size() > 0:
            return self.data[-1]
        else:
            return [0]


ua = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/86.0.4240.42 Safari/537.36 Edg/86.0.622.19"
}


def getHtmlText(url, encoding="utf-8"):
    try:
        r = requests.get(url, headers=ua)
        r.raise_for_status()
        return r.text
    except:
        return "Error"


def getPicContent(url):
    try:
        r = requests.get(url, headers=ua)
        r.raise_for_status()
        return r.content
    except:
        return "Error"


def getPicList(start_url, page, pic_queue):
    for num in range(1, page + 1):
        url = start_url + "/?page=" + str(num)
        html = getHtmlText(url)
        soup = BeautifulSoup(html, "html.parser")
        divtag = soup.find("div", attrs={"class": "page-content text-center"})
        imgtag = divtag.findAll("img")
        for i in imgtag:
            print(i.attrs["alt"])
            print(i.attrs["data-original"])
            pic_queue.put(
                [pic_queue.last()[0] + 1, i.attrs["alt"], i.attrs["data-original"]]
            )


def dlPic(pic_queue):
    # print(pic_queue)
    # pic_cnt = 0
    while pic_cnt < page * 68:
        pic_info = pic_queue.get()

        pic_index = pic_info[0]
        pic_name = pic_info[1]
        pic_url = pic_info[2]

        # print(pic_name, pic_url)
        img = getPicContent(pic_url)
        try:
            f = open(
                "c:/tmp/doutula/{}_{}.{}".format(
                    pic_index, pic_name, pic_url.split(".")[-1]
                ),
                "wb",
            )
        except:
            f = open(
                "c:/tmp/doutula/{}_{}.{}".format(
                    pic_index,
                    pic_name.replace("/", "**slash**"),
                    pic_url.split(".")[-1],
                ),
                "wb",
            )
        f.write(img)
        f.close()

    # f = open('c:/tmp/doutula/{}'.format(pic_name))


def main():
    start_url = "https://www.doutula.com/photo/list/"
    page = 2
    pic_queue = Queue()
    get_pic_queue_thread = Thread(target=getPicList, args=(start_url, page, pic_queue))
    dl_pic_thread = Thread(target=dlPic, args=(pic_queue))

    get_pic_queue_thread.start()
    time.sleep(5)
    dl_pic_thread.start()

    # get_pic_queue_thread.join()
    # dl_pic_thread.join()


if __name__ == "__main__":
    main()
