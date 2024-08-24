#定义一个空数列
list = []
#创建一个类，定义列表增、删、查、改操作
class Stack:
    def __init__(self):
        pass
    def push(self,item):
        list.append(item)
        print("添加成功")
    def pop(self):
        if len(list) == 0:
            print("列表为空")
            return
        list.pop()
        print("删除成功")
        print(list)
    def view(self):
        if len(list) == 0:
            print("列表为空")
            return
        print(list)
    def alter(self,index,item):
        if len(list) == 0:
            print("列表为空")
            return
        list[index] = self.item
        print("修改成功")
        print(list)

def run():
    prompt = """1.添加元素
    2.删除元素
    3.查看元素
    4.修改元素"""
    #实例化对象
    stack = Stack()
    while True:
        print(prompt)
        choice = int(input("请输入你的选择："))
        if choice == 1:
            item = input("请输入要添加的元素：")
            stack.push(item)
            continue
        elif choice == 2:
            stack.pop()
            continue
        elif choice == 3:
            stack.view()
        elif choice == 4:
            index = int(input("请输入要修改的元素的索引："))
            item = input("请输入要修改的元素：")
            stack.alter(index,item)
            continue
        else:
            print("输入有误，退出程序")
            break
if __name__ == "__main__":
    run()


    
    