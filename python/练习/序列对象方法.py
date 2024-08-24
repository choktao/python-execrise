from random import randint

alist = list('hello')#list函数=[]定义列表
# print(type(alist))
# print(alist)

astr = str(alist) #转换成字符串
# print(type(astr))
# print(astr)
lstr = ['h', 'e', 'l', 'l', 'o']
# print(type(str(lstr)))
atuple = tuple() #转换成元组
# print(tuple('hello'))
# print(type(tuple('hello')))
list1 = [10,'nina']
for i in range(len(list1)):
    print(f'{i},{list1[i]}')

for item in enumerate(list1):
    print(type(item))

for index, value in enumerate(list1):
    print(f"Index: {index}, Value: {value}")