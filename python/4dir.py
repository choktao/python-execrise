info = {
    'name':'nina',
    'age':17,
    'gender':'female',
    'band':'togenashi'
}
# print(info.keys())
# print(info.values())
# print(info.items())
# for k in info.keys():
#     print(k)
#     print(info[k])
info.update({'name':'hina','band':'diamond dust'})
print(info)
print(info.pop('band'))
print(info)