import time
length = 100
start = time.perf_counter()
print("执行开始".center(length//2,"="))
for i in range(length+1):
    a = "*" * i
    b = "." * (length - i)
    c = (i / length) * 100
    dur = time.perf_counter() - start
    print("{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="\r")
    time.sleep(0.05)
print("\n"+"执行结束".center(length//2,"="))