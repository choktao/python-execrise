import string
from random import choice
#定义有字母数字的字符串池
all_chars = string.ascii_letters + string.digits
#定义函数
def ran_password(n=8):#变量n确定长度
#创建空字符串保存密码
    password = ''
    for i in range(n):
        password += choice(all_chars)
    return password
if __name__ == '__main__':
    print(ran_password())