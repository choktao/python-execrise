#导入随机数模块
import random
#定义所有选项列表
all_choices = ['石头','剪刀','布']
#存入玩家选择变量
player = input('选择出拳（石头/剪刀/布）:')
computer = random.choice(all_choices)
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('玩家赢')
    else:
        print('玩家输')
elif player == '剪刀':
    if computer == '剪刀':
        print('平局')
    elif computer == '布':
        print('玩家赢')
    else:
        print('玩家输')
elif player == '布':
    if computer == '布':
        print('平局')
    elif computer == '石头':
        print('玩家赢')
    else:
        print('玩家输')
else: 
    print('请输入(石头/剪刀/布)')
