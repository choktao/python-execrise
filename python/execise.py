def get_info(name,age):
    # 异常触发ValueError，提示为无效信息
    if 120 > age > 0:
        print('%s is %s years old' %(name,age))
    else:
        # 当age不在范围内，触发raise抛出异常
        raise ValueError('无效年龄')
get_info(input('name:'),int(input('age:')))

