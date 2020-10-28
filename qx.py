txt=open("c:/tmp/data.csv")
ls=[]
for line in txt:
     line=line.replace("\n","")
     ls.append(line.split(","))
txt.close()   
# for item in ls:
#     for l in item:
#         item[item.index(l)] = l.strip(" ")
#         l = l.strip(" ")
#     print(",".join(item))
nls=ls[::-1]
# for i in range(len(ls)):
#     nls[len(ls)-1-i] = ls[i]
print(ls)
print(nls)
for item in nls:
    item= item[::-1]
    print(";".join(item))