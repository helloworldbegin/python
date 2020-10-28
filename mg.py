# ls=[]
# for i in range(1000,10000):
#     a=str(i)
#     he=eval(a[0])**4+eval(a[1])**4+eval(a[2])**4+eval(a[3])**4
#     if he == i:
#         ls.append(he)
# for item in ls:
#     print(item)
# he = 0
# ls=[]
# for i in range(2,100):
#     ls.append(i)
# for k in range(2,100):
#     for m in range(2,k):
#         if k%m==0:
#             ls.remove(k)
#             break
# for item in ls:
#     he=he+item
# print(ls)
# print(he)
# he = 0
# ls=[]
# for i in range(2,100):
#     ls.append(i)
# for k in range(3,100):
#     for m in range(2,k):
#         if k%m==0:
#             ls.remove(k)
#             break
# for item in ls:
#     he=he+item
# print(he)
import random

def genpwd(length):
    return random.randint(10**(length-1),10**(length))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
