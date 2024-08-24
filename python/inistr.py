# name,age,list = 'nina',17,[1,2]
# #转换数据类型的拼接
# str01 = 'name:'+name+',age:'+str(age)
# print(str01)
# # %s
# str02 = "name: %s, age: %s, %s"% (name,age,list)
# print(str02)
# # f字符串
# str03 = f'name:{name},age:{age}'
# print(str03)
# alist = ['nina','hina','mmk']
# print('_'.join(alist))
# print('.'.join(alist))
def get_sum(n1,n2=100):
    print(n1+n2)
get_sum(1,2)