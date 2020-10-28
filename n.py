# def prime(m):
#     for i in range(2,m):
#         if m%i == 0:
#             return False
#     return True

# n = eval(input())
# n = int(n)
# count = 0
# ls=[]
# while count<5:
#     if prime(n):
#         ls.append(n)
#         count+=1
#         n+=1
#     else:
#         n+=1
# print("{},{},{},{},{}".format(ls[0],ls[1],ls[2],ls[3],ls[4]))
n = input()
s=str(n)
a=set()
for ch in s:
    a.add(ch)
sum=0
for i in a:
    sum += int(i)
print(sum)