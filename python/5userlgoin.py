#定义一个空字典，用于放入后续加入的用户名和密码
userdb = {}
#添加注册函数
def register():
    #获取输入的用户名
    username = input("请输入用户名：")
    # 判断用户是否已经存在
    if username in userdb:
        print("用户名已存在，请重新输入")
    else:
        # 获取输入的密码
        # 不存在则添加用户至userdb字典
        password = input("请输入密码：")
        userdb[username] = password#使用键值对添加不会覆盖原字典
#添加登陆函数
def login():
    # 获取用户名
    username = input("请输入用户名：")
    # 获取登陆密码
    password = input("请输入密码：")
    # 判断用户名和密码是否匹配
    if userdb[username] == password:
        #判断登陆成功
        print('登陆成功')
        #判断登陆失败
    else:
        print('登陆失败')
#循环询问判断执行不同的函数
while True:
    #显示选择菜单
    print("0.退出")
    print("1.注册")
    print("2.登陆")
    #获取用户选择
    u_choice = input("请选择：")  
    #根据选择执行不同的函数
    if u_choice not in ["0","1","2"]:
        print("输入错误，请重新输入")
        continue
    if u_choice == "0":
        print('bye-bye')
        break
    elif u_choice == "1":
        register()
        continue
    else :
        login()




