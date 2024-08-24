class role:
    def __init__(self,name,weapon):#定义初始化属性
        self.name=name
        self.weapon=weapon
    def attack(self,target):
        print(f'我是{self.name},使用{self.weapon},攻击了{target}')
    
if __name__=='__main__':
    pl1 = role('akira','sword')
    pl1.attack('agito')