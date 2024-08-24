#创建父类
class role:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon
    def show_me(self):
        print(f'我叫{self.name},我的ace是{self.weapon}')
#创建子类
class warrior(role):
    def attack(self,target):
        print(f'使用{self.weapon}攻击{target}')
class mage(role):
    def defend(self,target):
        print(f'使用{self.weapon}防御{target}')
if __name__ == '__main__':
    sa = warrior('shark','ark knight')#以warrior子类创建对象，会继承父类role的属性和方法
    astl = mage('astarl','hope')#以mage子类创建对象，会继承父类role的属性和方法
    sa.show_me()#调用warrior子类show_me方法（继承）
    astl.show_me()#调用mage子类show_me方法（继承）
    sa.attack('hope')#调用warrior子类自身的attack方法
    astl.defend('ark knight')#调用warrior子类自身的defend方法