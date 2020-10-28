# import random
# num = eval(input())
# random.seed(123)
# hit = 0
# for i in range(num):
#     x = random.random()
#     y = random.random()
#     if pow(x**2+y**2,0.5)< 1:
#         hit+=1
# print("{:.6f}".format(4*hit/num))
err=0
l1=input()
l2=input()
while True:
    if l1 == "Kate" and l2 == "666666":
        print("登录成功！")
        break
    else:
        err+=1
        if err >=3:
            print("3次用户名或者密码均有误！退出程序。")
            break
        l1=input()
        l2=input()