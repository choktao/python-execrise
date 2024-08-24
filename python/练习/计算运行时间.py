import time
result = 0
#截取代码运行前的时间戳
start = time.time()
for i in range(100000):
    result += i
#截取代码运行后的时间戳
end = time.time()
diff = end - start
print(diff)