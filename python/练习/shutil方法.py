import shutil
with open('/home/student/Desktop/python/test.txt','rb') as sfobj:
    with open('/home/student/Desktop/python/test1.txt','wb') as dfobj:
        shutil.copyfileobj(sfobj,dfobj)
#复制文件对象的方法，参数1：源文件，参数2：目标文件（参数类型为文件对象）
shutil.copy('/home/student/Desktop/python/test.txt',
            '/home/student/Desktop/python/test2.txt')
#复制文件，不保留权限和元数据