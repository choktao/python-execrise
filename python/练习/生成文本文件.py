import os
# 定义获取文件名的函数
def get_fname():
    while True:#循环+break目的是检查是否存在同文件名
        fname = input('filename:\t')
        if not os.path.exists(fname):
            break#不存在则跳出循环
        print('already exists')
    return fname#返回文件名，以便调用
# 定义获取文件内容的函数
def get_fcontent():
    content = [] # 定义一个空列表
    print('enter end to quit')#提示输入结束
    while True:
        line = input('line:\t')
        if line != 'end':
            content.append(line)#将输入的内容添加到列表中
        else :
            break
    return content#返回列表，以便调用
# 定义写入文件的函数
def wfile(fname,content):#传入前面获取的参数
    with open(fname,'w') as fobj:
        fobj.writelines(content)#写入文件
# 调用函数
fname = get_fname()
content = get_fcontent()
wfile(fname,content)