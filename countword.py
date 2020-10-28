def getText():
    txt = open("c:/tmp/hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch," ")
    return txt
txt = getText()
words = txt.split()
count = {}
for word in words:
    count[word] = count.get(word,0) + 1
danci = list(count.items())
danci.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,num = danci[i]
    print("{0:<10}{1:>4}".format(word,num))