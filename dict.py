#encoding:utf-8
#
# dict = {'name':'donghao','school':'nyist'}
# print(dict)

# del dict['name']
# print(dict)
# dict.clear()
#
# print(dict['name'])

# print(dict.items())
# for i in dict.items():
#     print(i)
# import sys
# list = [1,2,3,4]
#
# it = iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit

#
#
# fruit = ['   banana','  orange lo','apple']
# # print([x.strip() for x in fruit])
#
# src = [1,2,3,4,5,6,7]
# print([x*2 for x in src if x<4])
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print(matrix)
# print([[row[i] for row in matrix] for i in range(4)])

# import sys
# for i in sys.argv:
#     print(i)import sys
# print(dir(sys))
# print('路径为：',sys.path)
#

# src = dict([('name','donghao'),('age',18)])
# print(src)
# print('name' in src)

# my = dict(name='donghao',age=20,school = 'nyist')
# for v in my.values():
#     print(v)
#
# for x in range(1,11):
#     print(repr(x).rjust(2),repr(x*x).rjust(3),end='')
#     print(repr(x*x*x).rjust(6))
fo = open('基础笔记.txt',"r+",encoding='utf-8')
print('文件名是：',fo.name)
# print(fo)
# # fid = fo.fileno()
# # print(fid)
# # fo.close()
# for index in range(10):
#     line = next(fo)
#     print('第%d行---%s'%(index,line))
# fo.close()
#
# line = fo.read(20)
# # print(line)
# line = fo.readline(10)
# print(line)
# fo.close()
#
# for line in fo.readlines():
#     print(line)
str = 'my name is donghao'
fo.write(str)
fo.close()

