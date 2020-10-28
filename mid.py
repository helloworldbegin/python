# def median(numbers):    #计算中位数
#     count=0
#     for i in numbers:
#         count=count+1
#     print(count)
#     ls=sorted(numbers)
#     if count %2==0:
#         print(count/2)
#         return (ls[int(count/2)]+ls[int(count/2)-1])/2
#     else:
#         return ls[count//2]
# a=eval(input())
# print(median(a))
#请在...补充一行或多行代码
#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    a= input()
    return eval(a)

def mean(numbers):#计算平均值
    n=0
    count=0
    for i in numbers:
        n=n+i
        count=count+1
    return n/count
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    count=0
    for i in numbers:
        count=count+1
    ls=sorted(numbers)
    if count %2==0:
        return ((ls[int(count/2)]+ls[int(count/2)-1])/2)
    else:
        return ls[count//2]
    
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))
