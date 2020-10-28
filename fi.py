f=open("c:/tmp/latex.log",'rt')
txt=f.read()
f.close()
count={}
for ch in txt:
    if ch in 'abcdefghijklmnopqrstuvwxyz':
        count[ch]=count.get(ch,0)+1
ls=list(count.items())
ls.sort()
print("共{}字符".format(len(txt)),end="")
for i in ls:
    print(",{}:{}".format(i[0],i[1]),end="")
print()