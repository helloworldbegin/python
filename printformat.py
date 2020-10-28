# num= input()
# for i in range(1,eval(num)+1,2):
#     print("{0:^{1}}".format('*'*i,eval(num)))
# str = input()
# ywl="abcdefghijklmnopqrstuvwxyz"
# ywu=ywl.upper()
# mwl="defghijklmnopqrstuvwxyzabc"
# mwu=mwl.upper()
# for c in str:
#     if c in ywl:
#         print(mwl[ywl.index(c)],end="")
#     elif c in ywu:
#         print(mwu[ywu.index(c)],end="")
#     else:
#         print(c,end="")
import time
long = 100
start=time.perf_counter()
print("执行开始".center(long//2,"-"))
for i in range(long+1):
    a="*"*i
    b="."*(long-i)
    c=(i/long)*100
    dur=time.perf_counter()-start
    print("{:3.0f}[{}->{}]{:.2f}s".format(c,a,b,dur),end="\r")
    time.sleep(0.01)
print("\n"+"执行结束".center(long//2,'-'))