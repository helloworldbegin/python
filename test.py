import random as r
# r.seed(10)
# a=r.random()
# print(a)
# r.seed(10)
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# r.shuffle(a)
# print(a)
# pi=0
# N=2
# for k in range(N):
#     pi+=1/pow(16,k)*( \
#         4/(8*k+1)-2/(8*k+4)-\
#         1/(8*k+5)-1/(8*k+6))
# print(pi)
from random import random
from time import perf_counter
start=perf_counter()
DARTS=1000*1000*10
hits=0
for i in range(1,DARTS+1):
    x,y=random(),random()
    if pow(x**2+y**2,0.5)<=1:
        hits+=1
pi=4*(hits/DARTS)
print("圆周率的值是：{}".format(pi))
print("运行时间是{:.5f}秒".format(perf_counter()-start))