li = ['alex','jerry','tom','barry','wall']
print(len(li))
li1 = li[::2]
print(li1)
li.append('mike')
print(li)
li.insert(0,'Tony')
print(li)
li[1] = 'kelly'
print(li)
l2 = [1,'a',3,4,'heart']
li.extend(l2)
print(li)
li.remove('barry')
print(li)
li.pop(1)
print(li)