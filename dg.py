# hello = input()
# def rvs(abc):
#     if abc=="":
#         return abc
#     else:
#         return rvs(abc[1:])+abc[0]
# print("shuruwei:{},fanzhuanhou:{}".format(hello,rvs(hello)))

num  = eval(input())
count=0
def hn(n,src,dst,mid):
    global count
    if n == 1:
        count=count+1
        print("[STEP{:>4}]    {}->{}".format(count,src,dst))
    else:
        hn(n-1,src,mid,dst)
        count+=1
        print("[STEP{:>4}]    {}->{}".format(count,src,dst))
        hn(n-1,mid,dst,src)
hn(num,"A","C","B")