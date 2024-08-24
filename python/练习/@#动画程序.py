import time

# 定义@和#的初始数量（变量）
t_length = 20
a_length = 0
# 定义函数，使用while循环
def run():
    while True:
        # while循环打印@，减少#的数量
        print('\r%s@%s' % ('#' * a_length, '#' * (t_length - a_length)), end='')
        #加入try,except，防止程序崩溃
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:#空输入退出程序
            print('\nbye')
            break
        if a_length == t_length:
            a_length = 0
        a_length += 1
sRun = run()