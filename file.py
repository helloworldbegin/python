#fname=input("请输入要打开的文件名称：")
#fo = open(fname,'r')
fo = open('c:/tmp/ham.txt','w+')
# for line in fo:
#     print(line)
print(fo.read())
ls=["毛泽东","邓小平","邓小平","江泽民","胡锦涛","习近平"]
fo.writelines(ls)
fo.seek(0)
print(fo.read())
fo.close()