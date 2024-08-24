#定义一个空字典存帐号密码
users = {}
#创建注册函数
def register():
    name = input('请输入用户名：')
    pw = input('请输入密码：')
    #判断帐号是否已经存在
    if users.key(name) == None:
        users[name] = pw
        print('注册成功')
    else:
        print('该帐号已经存在')
    return users 
#创建登陆函数
def login():
    name = input('请输入用户名：')
    pw = input('请输入密码：')
    if users.get(name) == pw:
        print('登陆成功')
        return
    else:
        print('帐号或密码错误')
#创建菜单函数
def menu():
    print('--------欢迎来到注册登陆系统--------')
    print('1.注册')
    print('2.登陆')
    print('3.退出')
    while True:
        choice = int(input('请输入选项：'))
        if choice == 1:
            register()
            continue
        elif choice == 2:
            login()
            pass
        elif choice == 3:
            print('谢谢使用')
            exit()
menu()