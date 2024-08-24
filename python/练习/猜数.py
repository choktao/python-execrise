import random
# 生成随机数
num = random.randint(1,10)
#加入计数器
count = 0
# 用户输入与随机数比较
while count < 3:
    #保存用户输入
    pl1 = int(input("请输入1-10之间的数字："))
    if pl1 == num:
        print('猜对了')
        count +=1
        continue
    elif pl1 > num:
        print('猜大了')
        count +=1
        continue
    else:
        print('猜小了')
        count +=1
        continue
# 输出比较结果