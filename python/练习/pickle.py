import pickle

# 定义测试数据
test_list = [1, 2, 3, 4, 5]
test_dict = {'name': 'nina', 'age': 17}

try:
    # 写入数据
    with open('./练习/user.txt', 'wb') as f:
        f.write(pickle.dumps(test_list))  # 直接写入字节串
        pickle.dump(test_dict, f)  # 直接使用pickle.dump()

    # 读取数据
    with open('./练习/user.txt', 'rb') as f:
        test_list = pickle.load(f)  # 直接从文件对象加载
        test_dict = pickle.load(f)  # 继续从文件对象加载

    print(type(test_list))
    print(type(test_dict))

except Exception as e:
    print(f"发生错误: {e}")